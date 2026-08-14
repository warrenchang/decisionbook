#!/usr/bin/env python3
"""Run source and rendered-output checks for the canonical Quarto textbook."""

from __future__ import annotations

import html
import json
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path

from qa_figure_connectors import audit as audit_connectors
from sync_references import canonical_chapters, chapter_references, reference_key


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "QA_REPORT.md"
JSON_REPORT = ROOT / "qa-report.json"
WORD = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+(?:[’'\-][A-Za-zÀ-ÖØ-öø-ÿ0-9]+)*")
H1 = re.compile(r"^# (.+)$", re.MULTILINE)
HEADING = re.compile(r"^(#{2,6})\s+(.+?)\s*$", re.MULTILINE)
ID = re.compile(r"\{[^}\n]*#([A-Za-z][\w:.-]*)[^}\n]*\}")
FIGURE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)\{([^}\n]*)\}")
QMD_LINK = re.compile(r"\[[^\]]+\]\(([^)#?]+\.qmd)(?:#[^)]+)?\)")
REFERENCE_BLOCK = re.compile(r"^::: \{\.reference\}\s*\n(.*?)\n:::\s*$", re.MULTILINE | re.DOTALL)
REQUIRED = (
    "Learning goals",
    "Key ideas",
    "Study and practice",
    "References cited in this chapter",
)


@dataclass
class Issue:
    level: str
    code: str
    file: str
    detail: str


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def strip_reference_tail(text: str) -> str:
    marker = re.search(r"^## References cited in this chapter\s*$", text, re.MULTILINE)
    return text[: marker.start()] if marker else text


def normalize_token(value: str) -> str:
    value = re.sub(r"[’']s$", "", value.strip(), flags=re.I)
    value = unicodedata.normalize("NFKD", value.casefold().replace("’", "'"))
    return re.sub(r"[^a-z0-9]", "", "".join(char for char in value if not unicodedata.combining(char)))


def likely_citation_tokens(text: str) -> list[tuple[str, str, str]]:
    """Extract the nearest author surname and year from author-date citations."""
    tokens: list[tuple[str, str, str]] = []
    for match in re.finditer(r"\(([^()]{0,350}\b(?:18|19|20)\d{2}[a-z]?(?:\s*/\s*(?:18|19|20)\d{2})?[^()]*)\)", text):
        chunk = match.group(1)
        for segment in chunk.split(";"):
            years = re.findall(r"\b((?:18|19|20)\d{2}[a-z]?)\b", segment)
            if not years:
                continue
            before = segment[: segment.find(years[0])]
            before = re.sub(r"^(?:e\.g\.,?|see|cf\.)\s*", "", before.strip(), flags=re.I)
            surname = re.search(
                r"([A-Z][A-Za-zÀ-ÖØ-öø-ÿ’'\-]+)(?:\s+et\s+al\.|\s*(?:&|and)\s*[A-Z][A-Za-zÀ-ÖØ-öø-ÿ’'\-]+|(?:,\s*[A-Z][A-Za-zÀ-ÖØ-öø-ÿ’'\-]+)*)?\s*,?\s*$",
                before,
            )
            if surname:
                tokens.extend((surname.group(1), year, segment.strip()) for year in years)
    for match in re.finditer(
        r"\b([A-Z][A-Za-zÀ-ÖØ-öø-ÿ’'\-]+)(?:\s+et\s+al\.|\s+(?:&|and)\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ’'\-]+)?(?:[’']s)?\s*\(((?:18|19|20)\d{2}[a-z]?)\)",
        text,
    ):
        tokens.append((match.group(1), match.group(2), match.group(0)))
    return tokens


def reference_author_years(reference: str) -> set[tuple[str, str]]:
    year_match = re.search(r"\(((?:18|19|20)\d{2}[a-z]?)(?:[/,][^)]*)?\)", reference)
    if not year_match:
        return set()
    author_text = reference[: year_match.start()]
    years = {year_match.group(1)}
    years.update(re.findall(r"Original work (?:published|ca\.)\s*((?:18|19|20)\d{2})", reference, flags=re.I))
    stopwords = {"and", "the", "de", "del", "van", "von", "jr", "sr", "eds", "ed"}
    names = {
        normalize_token(value)
        for value in re.findall(r"\b[A-ZÀ-ÖØ-Þ][A-Za-zÀ-ÖØ-öø-ÿ’'\-]{1,}\b", author_text)
        if normalize_token(value) not in stopwords
    }
    return {(name, year) for name in names for year in years if name}


def reference_title_year_key(reference: str) -> str | None:
    match = re.search(r"\(((?:18|19|20)\d{2})[a-z]?(?:[/,][^)]*)?\)\.\s+(.+?)[.?!](?:\s+|$)", reference)
    if not match:
        return None
    title = normalize_token(match.group(2))
    return f"{match.group(1)}:{title}" if title else None


def word_count(text: str) -> int:
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    return len(WORD.findall(text))


def figure_svg_path(source: Path, target: str) -> Path | None:
    clean = target.split("#", 1)[0].split("?", 1)[0]
    path = (source.parent / clean).resolve()
    try:
        path.relative_to(ROOT)
    except ValueError:
        return None
    return path


def svg_has_accessible_metadata(path: Path) -> bool:
    try:
        root = ET.parse(path).getroot()
    except (ET.ParseError, OSError):
        return False
    tags = {element.tag.rsplit("}", 1)[-1] for element in root}
    return "title" in tags and "desc" in tags


def audit() -> tuple[dict[str, object], list[Issue], dict[str, object]]:
    issues: list[Issue] = []
    try:
        chapters = canonical_chapters()
    except SystemExit as exc:
        return {}, [Issue("error", "canonical-chapters", "_quarto.yml", str(exc))], {}

    if len(chapters) != 38:
        issues.append(Issue("error", "chapter-count", "_quarto.yml", f"Expected 38 canonical chapters; found {len(chapters)}."))

    global_ids: list[tuple[str, str]] = []
    figure_paths: set[Path] = set()
    body_words: dict[str, int] = {}
    reference_blocks = 0
    table_count = 0
    unresolved_citations: list[dict[str, object]] = []
    citation_chapters: list[dict[str, object]] = []

    for chapter in chapters:
        text = chapter.read_text(encoding="utf-8")
        headings = [match.group(2).strip() for match in HEADING.finditer(text)]
        h1s = H1.findall(text)
        if len(h1s) != 1:
            issues.append(Issue("error", "chapter-h1", rel(chapter), f"Expected one H1; found {len(h1s)}."))
        for required in REQUIRED:
            if required not in headings:
                issues.append(Issue("error", "required-section", rel(chapter), f"Missing section: {required}."))
        for hashes, heading in HEADING.findall(text):
            if len(hashes) in {2, 3} and re.match(r"^(?:worked\s+)?transfer\b", heading, re.I):
                issues.append(Issue("warning", "ambiguous-transfer-heading", rel(chapter), f"Reader-facing heading remains: {heading}."))

        ids = ID.findall(text)
        for item in ids:
            global_ids.append((item, rel(chapter)))
        local_dupes = sorted(value for value, count in Counter(ids).items() if count > 1)
        if local_dupes:
            issues.append(Issue("error", "duplicate-id", rel(chapter), f"Duplicate IDs: {', '.join(local_dupes)}."))

        body = strip_reference_tail(text)
        body_words[rel(chapter)] = word_count(body)
        local_references = [re.sub(r"\s+", " ", value).strip() for value in REFERENCE_BLOCK.findall(text)]
        reference_blocks += len(local_references)
        local_keys = [reference_key(value) for value in local_references]
        duplicate_local = sorted(key for key, count in Counter(local_keys).items() if count > 1)
        if duplicate_local:
            issues.append(Issue("error", "duplicate-chapter-reference", rel(chapter), f"Found {len(duplicate_local)} duplicated normalized reference(s)."))
        available = set().union(*(reference_author_years(value) for value in local_references)) if local_references else set()
        chapter_unresolved: list[dict[str, str]] = []
        seen_citations: set[tuple[str, str]] = set()
        for author, year, raw in likely_citation_tokens(body):
            key = (normalize_token(author), year)
            if not key[0] or key in available or key in seen_citations:
                continue
            seen_citations.add(key)
            item = {"file": rel(chapter), "first_author": author, "year": year, "citation": raw}
            unresolved_citations.append(item)
            chapter_unresolved.append({"first_author": author, "year": year, "citation": raw})
            issues.append(Issue("error", "unresolved-citation", rel(chapter), f"No local reference matched: {raw}."))
        citation_chapters.append(
            {
                "file": rel(chapter),
                "title": h1s[0] if h1s else chapter.stem,
                "reference_count": len(local_references),
                "references": local_references,
                "unresolved": chapter_unresolved,
            }
        )
        table_count += len(re.findall(r"^:\s+.+\{#tbl-", text, re.MULTILINE))

        for alt, target, attrs in FIGURE.findall(text):
            if not alt.strip() or not re.search(r'\bfig-alt="[^"]+"', attrs):
                issues.append(Issue("error", "figure-alt", rel(chapter), f"Figure lacks caption or fig-alt: {target}."))
            path = figure_svg_path(chapter, target)
            if path is None or not path.exists():
                issues.append(Issue("error", "missing-figure", rel(chapter), f"Missing figure: {target}."))
                continue
            figure_paths.add(path)
            if path.suffix.lower() == ".svg" and not svg_has_accessible_metadata(path):
                issues.append(Issue("error", "svg-metadata", rel(path), "SVG must contain title and desc elements."))

        for target in QMD_LINK.findall(text):
            linked = (chapter.parent / target).resolve()
            if not linked.exists():
                issues.append(Issue("error", "broken-qmd-link", rel(chapter), f"Broken source link: {target}."))

    global_duplicate_ids = sorted(
        (value, sorted(file for item, file in global_ids if item == value))
        for value, count in Counter(item for item, _ in global_ids).items()
        if count > 1
    )
    for value, files in global_duplicate_ids:
        issues.append(Issue("error", "global-duplicate-id", ", ".join(files), f"ID appears more than once: {value}."))

    for path in sorted(figure_paths):
        if path.suffix.lower() != ".svg":
            continue
        for detail in audit_connectors(path):
            issues.append(Issue("error", "figure-connector", rel(path), detail))

    master_text = (ROOT / "references.qmd").read_text(encoding="utf-8")
    master_blocks = re.findall(r"^::: \{\.reference\}\s*\n(.*?)\n:::\s*$", master_text, re.MULTILINE | re.DOTALL)
    master_keys = {reference_key(value) for value in master_blocks}
    chapter_keys = {reference_key(value) for value in chapter_references()}
    if master_keys != chapter_keys:
        issues.append(
            Issue(
                "error",
                "master-references",
                "references.qmd",
                f"Master/chapter mismatch: {len(chapter_keys - master_keys)} missing and {len(master_keys - chapter_keys)} extra.",
            )
        )
    if len(master_blocks) != len(master_keys):
        issues.append(Issue("error", "duplicate-master-reference", "references.qmd", "Master bibliography contains duplicate normalized entries."))
    title_groups: dict[str, list[str]] = {}
    for reference in master_blocks:
        key = reference_title_year_key(reference)
        if key:
            title_groups.setdefault(key, []).append(reference)
    for values in title_groups.values():
        distinct = {reference_key(value) for value in values}
        if len(distinct) > 1:
            issues.append(
                Issue(
                    "error",
                    "near-duplicate-reference",
                    "references.qmd",
                    f"The same title/year appears in {len(distinct)} reference variants: {values[0]}",
                )
            )

    rendered_missing = 0
    rendered_alt_missing = 0
    for chapter in chapters:
        html_path = ROOT / "docs" / "chapters" / f"{chapter.stem}.html"
        if not html_path.exists():
            rendered_missing += 1
            issues.append(Issue("error", "missing-rendered-chapter", rel(html_path), "Canonical chapter has not been rendered."))
            continue
        rendered = html_path.read_text(encoding="utf-8", errors="replace")
        for tag in re.findall(r"<img\b[^>]*>", rendered, flags=re.I):
            match = re.search(r'\balt="([^"]*)"', tag, flags=re.I)
            if match is None or not html.unescape(match.group(1)).strip():
                rendered_alt_missing += 1
                issues.append(Issue("error", "rendered-alt", rel(html_path), "Rendered image lacks alternative text."))

    summary: dict[str, object] = {
        "canonical_chapters": len(chapters),
        "chapter_body_words": sum(body_words.values()),
        "shortest_chapter_words": min(body_words.values(), default=0),
        "longest_chapter_words": max(body_words.values(), default=0),
        "chapter_reference_blocks": reference_blocks,
        "master_unique_references": len(master_keys),
        "chapter_figures": len(figure_paths),
        "chapter_tables": table_count,
        "rendered_chapters_missing": rendered_missing,
        "rendered_images_missing_alt": rendered_alt_missing,
        "unresolved_citations": len(unresolved_citations),
        "errors": sum(issue.level == "error" for issue in issues),
        "warnings": sum(issue.level == "warning" for issue in issues),
        "body_words_by_chapter": body_words,
    }
    citation_data: dict[str, object] = {
        "summary": {
            "chapters": len(chapters),
            "published_unique_cited_references": len(chapter_references()),
            "chapter_reference_blocks": reference_blocks,
            "unresolved_citations": len(unresolved_citations),
        },
        "chapters": citation_chapters,
        "unresolved_citations": unresolved_citations,
    }
    return summary, issues, citation_data


def render_report(summary: dict[str, object], issues: list[Issue]) -> str:
    status = "PASS" if not any(issue.level == "error" for issue in issues) else "FAIL"
    lines = [
        "# Quality-assurance report",
        "",
        f"**Release status: {status}**",
        "",
        "This report was generated by `scripts/qa_quarto_book.py` from the canonical Quarto source and the rendered HTML book.",
        "",
        "## Summary",
        "",
        "| Check | Result |",
        "| --- | ---: |",
    ]
    labels = {
        "canonical_chapters": "Canonical chapters",
        "chapter_body_words": "Chapter body words",
        "shortest_chapter_words": "Shortest chapter",
        "longest_chapter_words": "Longest chapter",
        "chapter_reference_blocks": "Chapter reference blocks",
        "master_unique_references": "Unique master references",
        "chapter_figures": "Unique chapter figures",
        "chapter_tables": "Captioned chapter tables",
        "rendered_chapters_missing": "Rendered chapters missing",
        "rendered_images_missing_alt": "Rendered images missing alt text",
        "unresolved_citations": "Unresolved author–year citations",
        "errors": "Release-blocking errors",
        "warnings": "Warnings",
    }
    for key, label in labels.items():
        lines.append(f"| {label} | {summary.get(key, 'n/a')} |")
    lines.extend(["", "## Issues", ""])
    if not issues:
        lines.append("No automated issues were found.")
    else:
        lines.extend(["| Level | Code | File | Detail |", "| --- | --- | --- | --- |"])
        for issue in issues:
            detail = issue.detail.replace("|", "\\|")
            lines.append(f"| {issue.level.upper()} | `{issue.code}` | `{issue.file}` | {detail} |")
    lines.extend(
        [
            "",
            "## Scope",
            "",
            "The audit checks canonical chapter membership, required learning sections, source and rendered figures, alternative text, SVG metadata, connector attachment, duplicate cross-reference IDs, source links, and exact master-bibliography union. Visual aesthetics are also reviewed separately from rendered figure contact sheets; scientific source support still requires editorial judgment.",
            "",
        ]
    )
    return "\n".join(lines)


def citation_markdown(data: dict[str, object]) -> str:
    summary = data.get("summary", {})
    if not isinstance(summary, dict):
        summary = {}
    chapters = data.get("chapters", [])
    unresolved = data.get("unresolved_citations", [])
    lines = [
        "# Citation audit",
        "",
        f"Canonical chapters: **{summary.get('chapters', 0)}**",
        "",
        f"Unique references in the master union: **{summary.get('published_unique_cited_references', 0)}**",
        "",
        f"Chapter reference blocks: **{summary.get('chapter_reference_blocks', 0)}**",
        "",
        f"Unresolved author–year citations: **{summary.get('unresolved_citations', 0)}**",
        "",
        "## Chapter counts",
        "",
        "| Chapter | Reference blocks | Unresolved |",
        "| --- | ---: | ---: |",
    ]
    if isinstance(chapters, list):
        for item in chapters:
            if isinstance(item, dict):
                lines.append(f"| {item.get('title', item.get('file', ''))} | {item.get('reference_count', 0)} | {len(item.get('unresolved', [])) if isinstance(item.get('unresolved'), list) else 0} |")
    lines.extend(["", "## Unresolved citation strings", ""])
    if not unresolved:
        lines.append("None.")
    elif isinstance(unresolved, list):
        for item in unresolved:
            if isinstance(item, dict):
                lines.append(f"- `{item.get('file', '')}` — {item.get('citation', '')}")
    lines.extend(
        [
            "",
            "The automated matcher checks author–year correspondence against each chapter's own reference list. It does not determine whether a source supports every clause or replace scholarly copyediting.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    summary, issues, citation_data = audit()
    REPORT.write_text(render_report(summary, issues), encoding="utf-8")
    JSON_REPORT.write_text(
        json.dumps({"summary": summary, "issues": [asdict(issue) for issue in issues]}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (ROOT / "citation-audit.json").write_text(json.dumps(citation_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (ROOT / "CITATION_AUDIT.md").write_text(citation_markdown(citation_data), encoding="utf-8")
    print(f"QA {'PASS' if not any(issue.level == 'error' for issue in issues) else 'FAIL'}: {summary.get('errors', 1)} error(s), {summary.get('warnings', 0)} warning(s).")
    return 1 if any(issue.level == "error" for issue in issues) else 0


if __name__ == "__main__":
    sys.exit(main())
