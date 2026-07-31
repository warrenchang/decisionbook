#!/usr/bin/env python3
"""Quality-assurance checks for the DPN static textbook repository.

Run from the repository root:
    python scripts/qa_repository.py

The script writes QA_REPORT.md and qa-report.json in the repository root and exits
with a non-zero status only when a release-blocking error is found.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup, Tag

WORD_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+(?:[’'\-][A-Za-zÀ-ÖØ-öø-ÿ0-9]+)*")
CHAPTER_RE = re.compile(r"^(\d{2})-")
REQUIRED_CHAPTER_HEADINGS = {
    "learning-goals": "Learning goals",
    "key-ideas": "Key ideas",
    "study-and-practice": "Study and practice",
    "references-cited-in-this-chapter": "References cited in this chapter",
}


@dataclass
class Issue:
    level: str
    code: str
    file: str
    detail: str


def norm_ref(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().rstrip(".").casefold()


def visible_word_count(main: Tag) -> int:
    """Count chapter words up to, but not including, the reference section."""
    chunks: list[str] = []
    for child in main.children:
        if not isinstance(child, Tag):
            continue
        if child.get("id") == "references-cited-in-this-chapter":
            break
        if "page-nav" in child.get("class", []):
            continue
        chunks.append(child.get_text(" ", strip=True))
    return len(WORD_RE.findall(" ".join(chunks)))


def resolve_local_path(base_file: Path, href: str, docs_root: Path) -> tuple[Path | None, str | None]:
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or href.startswith("mailto:") or href.startswith("tel:"):
        return None, None
    path_part = unquote(parsed.path)
    fragment = unquote(parsed.fragment) if parsed.fragment else None
    if not path_part:
        return base_file, fragment
    resolved = (base_file.parent / path_part).resolve()
    try:
        resolved.relative_to(docs_root.resolve())
    except ValueError:
        return resolved, fragment
    return resolved, fragment


def heading_levels(soup: BeautifulSoup) -> list[int]:
    return [int(tag.name[1]) for tag in soup.find_all(re.compile(r"^h[1-6]$"))]


def audit(repo: Path) -> tuple[dict, list[Issue]]:
    repo = repo.resolve()
    docs = repo / "docs"
    chapters_dir = docs / "chapters"
    source_chapters_dir = repo / "chapters"
    appendices_dir = docs / "appendices"
    issues: list[Issue] = []

    html_files = sorted(docs.rglob("*.html"))
    chapter_html = sorted(chapters_dir.glob("*.html"))
    appendix_html = sorted(appendices_dir.glob("*.html"))
    source_chapters = sorted(source_chapters_dir.glob("*.md"))
    css_path = docs / "assets" / "style.css"
    css_text = css_path.read_text(encoding="utf-8", errors="replace") if css_path.exists() else ""
    tables_responsive_in_css = bool(
        re.search(r"table\s*\{[^}]*display\s*:\s*block", css_text, re.I | re.S)
        and re.search(r"table\s*\{[^}]*overflow-x\s*:\s*auto", css_text, re.I | re.S)
    )

    parsed_cache: dict[Path, BeautifulSoup] = {}
    id_cache: dict[Path, set[str]] = {}

    def parsed(path: Path) -> BeautifulSoup:
        if path not in parsed_cache:
            parsed_cache[path] = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
        return parsed_cache[path]

    def ids_for(path: Path) -> set[str]:
        if path not in id_cache:
            id_cache[path] = {t.get("id") for t in parsed(path).find_all(id=True) if t.get("id")}
        return id_cache[path]

    # Required release files.
    required = [
        docs / "index.html",
        docs / "references.html",
        docs / "about.html",
        docs / "assets" / "style.css",
        docs / "assets" / "site.js",
        docs / ".nojekyll",
        repo / ".github" / "workflows" / "pages.yml",
        repo / "README.md",
        repo / "GITHUB_UPLOAD_CHECKLIST.md",
        repo / "scripts" / "qa_repository.py",
        repo / "CITATION_AUDIT.md",
        repo / "STRUCTURE_AND_EDITORIAL_REPORT.md",
    ]
    for path in required:
        if not path.exists():
            issues.append(Issue("error", "missing-required-file", str(path.relative_to(repo)), "Required release file is missing."))

    # Chapter sequence and source/render parity.
    chapter_numbers: list[int] = []
    for path in chapter_html:
        m = CHAPTER_RE.match(path.name)
        if not m:
            issues.append(Issue("error", "chapter-filename", str(path.relative_to(repo)), "Chapter filename does not begin with a two-digit number."))
        else:
            chapter_numbers.append(int(m.group(1)))
    expected_numbers = list(range(1, len(chapter_html) + 1))
    if chapter_numbers != expected_numbers:
        issues.append(Issue("error", "chapter-sequence", "docs/chapters", f"Expected chapter sequence {expected_numbers}; found {chapter_numbers}."))
    if len(source_chapters) != len(chapter_html):
        issues.append(Issue("error", "source-render-parity", "chapters", f"Markdown chapters: {len(source_chapters)}; rendered chapters: {len(chapter_html)}."))

    # General HTML, accessibility, links, images, tables, headings.
    total_images = 0
    missing_alt = 0
    figure_count = 0
    unique_figure_sources: set[str] = set()
    table_count = 0
    table_without_headers = 0
    table_without_wrapper = 0
    internal_links_checked = 0
    broken_links = 0
    broken_fragments = 0
    duplicate_id_pages = 0
    heading_jump_pages = 0

    for path in html_files:
        soup = parsed(path)
        rel = str(path.relative_to(repo))
        html = soup.find("html")
        if not html or not html.get("lang"):
            issues.append(Issue("warning", "missing-lang", rel, "The html element has no language declaration."))
        if not soup.find("meta", attrs={"name": "viewport"}):
            issues.append(Issue("warning", "missing-viewport", rel, "Viewport metadata is missing."))
        if not soup.title or not soup.title.get_text(strip=True):
            issues.append(Issue("error", "missing-title", rel, "HTML title is missing or empty."))
        if not soup.find("main", id="main"):
            issues.append(Issue("error", "missing-main", rel, "Main landmark with id='main' is missing."))
        if not soup.find("a", class_="skip-link"):
            issues.append(Issue("warning", "missing-skip-link", rel, "Skip-to-content link is missing."))

        ids = [t.get("id") for t in soup.find_all(id=True)]
        dup_ids = sorted(k for k, v in Counter(ids).items() if k and v > 1)
        if dup_ids:
            duplicate_id_pages += 1
            issues.append(Issue("error", "duplicate-id", rel, f"Duplicate HTML ids: {', '.join(dup_ids)}."))

        levels = heading_levels(soup)
        for a, b in zip(levels, levels[1:]):
            if b > a + 1:
                heading_jump_pages += 1
                issues.append(Issue("warning", "heading-jump", rel, f"Heading hierarchy jumps from h{a} to h{b}."))
                break

        for img in soup.find_all("img"):
            total_images += 1
            alt = img.get("alt")
            if alt is None or not alt.strip():
                missing_alt += 1
                issues.append(Issue("error", "missing-alt", rel, f"Image '{img.get('src', '')}' lacks meaningful alternative text."))
            src = img.get("src", "")
            resolved, _ = resolve_local_path(path, src, docs)
            if resolved is not None and not resolved.exists():
                issues.append(Issue("error", "missing-image", rel, f"Image target does not exist: {src}."))

        for fig in soup.find_all("figure"):
            figure_count += 1
            img = fig.find("img")
            if img and img.get("src"):
                unique_figure_sources.add(img["src"])
            if not fig.find("figcaption"):
                issues.append(Issue("warning", "missing-figcaption", rel, "A figure has no figcaption."))

        for table in soup.find_all("table"):
            table_count += 1
            if not table.find("th"):
                table_without_headers += 1
                issues.append(Issue("error", "table-no-header", rel, "A data table has no header cells."))
            parent = table.parent
            has_wrapper = isinstance(parent, Tag) and "table-wrapper" in parent.get("class", [])
            if not has_wrapper and not tables_responsive_in_css:
                table_without_wrapper += 1
                issues.append(Issue("warning", "table-not-responsive", rel, "A table has neither a responsive wrapper nor a global overflow rule."))

        for a in soup.find_all("a", href=True):
            href = a["href"].strip()
            if not href or href.startswith(("http://", "https://", "mailto:", "tel:", "javascript:")):
                continue
            internal_links_checked += 1
            target, fragment = resolve_local_path(path, href, docs)
            if target is None:
                continue
            # Directory links should resolve to index.html in static hosting.
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                broken_links += 1
                issues.append(Issue("error", "broken-link", rel, f"Broken local link: {href}."))
                continue
            if fragment and target.suffix.lower() in {".html", ".htm"}:
                if fragment not in ids_for(target):
                    broken_fragments += 1
                    issues.append(Issue("error", "broken-fragment", rel, f"Link fragment '#{fragment}' is absent in {target.relative_to(docs)}."))

    # Chapter-level requirements and word counts.
    chapter_word_counts: dict[str, int] = {}
    chapter_ref_counts: dict[str, int] = {}
    chapter_refs_union: dict[str, str] = {}
    missing_required_sections = 0
    incorrect_h1 = 0
    chapter_figure_count = 0
    chapter_table_count = 0
    chapter_figure_sources: set[str] = set()

    for i, path in enumerate(chapter_html, start=1):
        soup = parsed(path)
        rel = str(path.relative_to(repo))
        main = soup.find("main", id="main")
        if not main:
            continue
        h1 = main.find("h1")
        if not h1 or not re.match(rf"Chapter\s+{i}\.", h1.get_text(" ", strip=True)):
            incorrect_h1 += 1
            issues.append(Issue("error", "chapter-h1", rel, f"Expected H1 to begin 'Chapter {i}.'."))
        for section_id, label in REQUIRED_CHAPTER_HEADINGS.items():
            if not main.find(id=section_id):
                missing_required_sections += 1
                issues.append(Issue("error", "missing-chapter-section", rel, f"Required section missing: {label}."))
        wc = visible_word_count(main)
        chapter_word_counts[path.name] = wc
        refs = [r.get_text(" ", strip=True) for r in main.select("div.reference")]
        chapter_ref_counts[path.name] = len(refs)
        for ref in refs:
            chapter_refs_union[norm_ref(ref)] = ref
        chapter_figure_count += len(main.find_all("figure"))
        for img in main.select("figure img[src]"):
            chapter_figure_sources.add(img["src"])
        chapter_table_count += len(main.find_all("table"))

    # Previous/next navigation follows the cumulative reading order. Part-overview pages
    # intentionally sit between the final chapter of one part and the first chapter of the next.
    chapter_parts: list[int] = []
    for path in chapter_html:
        soup = parsed(path)
        kicker = soup.select_one("main#main .chapter-kicker")
        match = re.search(r"Part\s+(\d+)", kicker.get_text(" ", strip=True) if kicker else "")
        chapter_parts.append(int(match.group(1)) if match else 0)
    for i, path in enumerate(chapter_html):
        soup = parsed(path)
        nav = soup.select_one("nav.page-nav")
        rel = str(path.relative_to(repo))
        if not nav:
            issues.append(Issue("error", "missing-page-nav", rel, "Previous/next chapter navigation is missing."))
            continue
        prev = nav.select_one("a.prev")
        nxt = nav.select_one("a.next")
        part = chapter_parts[i]
        if i == 0 or chapter_parts[i - 1] != part:
            expected_prev = f"part-{part}.html"
        else:
            expected_prev = chapter_html[i - 1].name
        if i == len(chapter_html) - 1:
            expected_next = "appendix-a-portable-course-tools.html"
        elif chapter_parts[i + 1] != part:
            expected_next = f"part-{part + 1}.html"
        else:
            expected_next = chapter_html[i + 1].name
        if prev is None or Path(urlsplit(prev.get("href", "")).path).name != expected_prev:
            issues.append(Issue("error", "wrong-prev", rel, f"Previous link should target {expected_prev}."))
        if nxt is None or Path(urlsplit(nxt.get("href", "")).path).name != expected_next:
            issues.append(Issue("error", "wrong-next", rel, f"Next link should target {expected_next}."))

    # Editorial regression and visual-assignment checks.
    combined_chapter_text = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in source_chapters)
    stale_patterns = {
        "self-service judgment": "The Chapter 13 subtitle should say self-serving judgment.",
        "Chapter 18 described rationalization": "A forward reference to the narrator chapter remains stale.",
        "preparation discussed in Chapter 13": "The integrative-negotiation cross-reference should point to Chapter 31.",
        "As Earlier": "A capitalization error remains in a transition.",
    }
    for pattern, detail in stale_patterns.items():
        if pattern in combined_chapter_text:
            issues.append(Issue("error", "stale-editorial-text", "chapters", detail))

    if chapter_figure_count != len(chapter_html):
        issues.append(Issue("error", "chapter-figure-count", "docs/chapters", f"Expected one figure per chapter ({len(chapter_html)}); found {chapter_figure_count}."))
    if len(chapter_figure_sources) != len(chapter_html):
        issues.append(Issue("error", "chapter-figure-uniqueness", "docs/chapters", f"Expected {len(chapter_html)} unique chapter figures; found {len(chapter_figure_sources)}."))
    for i, path in enumerate(chapter_html, start=1):
        soup = parsed(path)
        figures = soup.select("main figure")
        if len(figures) == 1:
            caption = figures[0].find("figcaption")
            if not caption or not caption.get_text(" ", strip=True).startswith(f"Figure {i}.1."):
                issues.append(Issue("warning", "figure-number", str(path.relative_to(repo)), f"Chapter figure caption should begin 'Figure {i}.1.'."))
        learning = [h for h in soup.select("main h2") if h.get_text(" ", strip=True).casefold() == "learning goals"]
        if len(learning) != 1:
            issues.append(Issue("error", "learning-goals-duplicate", str(path.relative_to(repo)), f"Expected one Learning goals heading; found {len(learning)}."))

    # Global bibliography equals union of chapter references.
    global_refs: list[str] = []
    refs_page = docs / "references.html"
    if refs_page.exists():
        global_refs = [r.get_text(" ", strip=True) for r in parsed(refs_page).select("div.reference")]
    global_map = {norm_ref(r): r for r in global_refs}
    refs_missing_global = sorted(set(chapter_refs_union) - set(global_map))
    refs_uncited_global = sorted(set(global_map) - set(chapter_refs_union))
    duplicate_global_refs = len(global_refs) - len(global_map)
    if refs_missing_global:
        issues.append(Issue("error", "refs-missing-global", "docs/references.html", f"{len(refs_missing_global)} chapter references are absent from the global bibliography."))
    if refs_uncited_global:
        issues.append(Issue("error", "refs-uncited-global", "docs/references.html", f"{len(refs_uncited_global)} global references are not used in any chapter list."))
    if duplicate_global_refs:
        issues.append(Issue("error", "refs-duplicate-global", "docs/references.html", f"{duplicate_global_refs} duplicate bibliography entries found."))

    # Machine-readable citation audit.
    citation_audit_path = repo / "citation-audit.json"
    citation_summary = {}
    if citation_audit_path.exists():
        try:
            citation_data = json.loads(citation_audit_path.read_text(encoding="utf-8"))
            if isinstance(citation_data, dict):
                citation_summary = citation_data.get("summary", citation_data)
            unresolved = citation_summary.get("unresolved_citations")
            if unresolved not in (None, 0, [], {}):
                issues.append(Issue("error", "unresolved-citations", "citation-audit.json", f"Citation audit reports unresolved citations: {unresolved}."))
        except Exception as exc:  # noqa: BLE001
            issues.append(Issue("error", "citation-audit-json", "citation-audit.json", f"Cannot parse citation audit: {exc}."))
    else:
        issues.append(Issue("error", "citation-audit-missing", "citation-audit.json", "Machine-readable citation audit is missing."))

    # Search index.
    search_entries = 0
    search_path = docs / "search-index.json"
    if search_path.exists():
        try:
            search_data = json.loads(search_path.read_text(encoding="utf-8"))
            search_entries = len(search_data) if isinstance(search_data, list) else 0
            if search_entries < len(chapter_html):
                issues.append(Issue("error", "search-index-short", "docs/search-index.json", f"Only {search_entries} search entries for {len(chapter_html)} chapters."))
        except Exception as exc:  # noqa: BLE001
            issues.append(Issue("error", "search-index-json", "docs/search-index.json", f"Cannot parse search index: {exc}."))
    else:
        issues.append(Issue("error", "search-index-missing", "docs/search-index.json", "Search index is missing."))

    # EPUB integrity and required package resources.
    epub_files = sorted((docs / "downloads").glob("*.epub")) if (docs / "downloads").exists() else []
    epub_summary: dict[str, object] = {"files": len(epub_files)}
    if not epub_files:
        issues.append(Issue("error", "epub-missing", "docs/downloads", "No EPUB file found."))
    else:
        epub = epub_files[0]
        try:
            with zipfile.ZipFile(epub) as zf:
                names = zf.namelist()
                bad_member = zf.testzip()
                first = zf.infolist()[0] if zf.infolist() else None
                mimetype_ok = False
                if first and first.filename == "mimetype" and first.compress_type == zipfile.ZIP_STORED:
                    mimetype_ok = zf.read("mimetype") == b"application/epub+zip"
                required_epub = ["META-INF/container.xml"]
                missing_epub = [name for name in required_epub if name not in names]
                nav_candidates = [n for n in names if n.lower().endswith(("nav.xhtml", "nav.html"))]
                opf_candidates = [n for n in names if n.lower().endswith(".opf")]
                cover_candidates = [n for n in names if "cover" in Path(n).name.lower() and n.lower().endswith((".png", ".jpg", ".jpeg", ".svg", ".xhtml", ".html"))]
                xhtml_count = len([n for n in names if n.lower().endswith((".xhtml", ".html"))])
                epub_summary.update({
                    "path": str(epub.relative_to(repo)),
                    "size_bytes": epub.stat().st_size,
                    "mimetype_valid": mimetype_ok,
                    "zip_test": bad_member is None,
                    "navigation_present": bool(nav_candidates),
                    "package_document_present": bool(opf_candidates),
                    "cover_resource_present": bool(cover_candidates),
                    "xhtml_documents": xhtml_count,
                })
                if bad_member:
                    issues.append(Issue("error", "epub-corrupt", str(epub.relative_to(repo)), f"Corrupt ZIP member: {bad_member}."))
                if not mimetype_ok:
                    issues.append(Issue("error", "epub-mimetype", str(epub.relative_to(repo)), "EPUB mimetype is absent, compressed, or incorrect."))
                if missing_epub or not nav_candidates or not opf_candidates or not cover_candidates:
                    issues.append(Issue("error", "epub-structure", str(epub.relative_to(repo)), "EPUB lacks its required container/navigation/package files or the intended cover resource."))
        except Exception as exc:  # noqa: BLE001
            issues.append(Issue("error", "epub-open", str(epub.relative_to(repo)), f"Cannot open EPUB: {exc}."))

    # Root redirect and deployment workflow sanity.
    root_index = repo / "index.html"
    if not root_index.exists():
        issues.append(Issue("warning", "root-index-missing", "index.html", "Root convenience redirect is missing."))
    else:
        text = root_index.read_text(encoding="utf-8", errors="replace")
        if "docs/index.html" not in text:
            issues.append(Issue("warning", "root-index-target", "index.html", "Root redirect does not mention docs/index.html."))
    workflow = repo / ".github" / "workflows" / "pages.yml"
    if workflow.exists():
        wt = workflow.read_text(encoding="utf-8", errors="replace")
        for needle in ("actions/configure-pages", "actions/upload-pages-artifact", "actions/deploy-pages", "path: docs"):
            if needle not in wt:
                issues.append(Issue("error", "workflow-config", str(workflow.relative_to(repo)), f"Deployment workflow is missing '{needle}'."))

    errors = [i for i in issues if i.level == "error"]
    warnings = [i for i in issues if i.level == "warning"]

    total_body_words = sum(chapter_word_counts.values())
    min_wc = min(chapter_word_counts.values()) if chapter_word_counts else 0
    max_wc = max(chapter_word_counts.values()) if chapter_word_counts else 0
    avg_wc = round(total_body_words / len(chapter_word_counts), 1) if chapter_word_counts else 0

    report = {
        "status": "PASS" if not errors else "FAIL",
        "release_blocking_errors": len(errors),
        "warnings": len(warnings),
        "repository": str(repo),
        "content": {
            "chapters_markdown": len(source_chapters),
            "chapters_html": len(chapter_html),
            "appendices_html": len(appendix_html),
            "chapter_body_words_excluding_references": total_body_words,
            "average_chapter_words": avg_wc,
            "shortest_chapter_words": min_wc,
            "longest_chapter_words": max_wc,
            "chapter_figures": chapter_figure_count,
            "unique_chapter_figure_sources": len(chapter_figure_sources),
            "chapter_tables": chapter_table_count,
        },
        "bibliography": {
            "global_reference_entries": len(global_refs),
            "unique_global_reference_entries": len(global_map),
            "unique_references_in_chapter_lists": len(chapter_refs_union),
            "chapter_references_missing_from_global": len(refs_missing_global),
            "global_references_not_in_chapter_lists": len(refs_uncited_global),
            "duplicate_global_entries": duplicate_global_refs,
            "machine_audit_summary": citation_summary,
        },
        "web": {
            "html_files": len(html_files),
            "internal_links_checked": internal_links_checked,
            "broken_links": broken_links,
            "broken_fragments": broken_fragments,
            "images": total_images,
            "images_missing_alt": missing_alt,
            "figures_all_pages": figure_count,
            "unique_figure_sources_all_pages": len(unique_figure_sources),
            "tables_all_pages": table_count,
            "tables_without_headers": table_without_headers,
            "tables_without_responsive_wrapper": table_without_wrapper,
            "pages_with_duplicate_ids": duplicate_id_pages,
            "pages_with_heading_jumps": heading_jump_pages,
            "search_index_entries": search_entries,
        },
        "epub": epub_summary,
        "chapter_word_counts": chapter_word_counts,
        "chapter_reference_counts": chapter_ref_counts,
        "issues": [asdict(i) for i in issues],
    }
    return report, issues


def make_markdown(report: dict, issues: list[Issue]) -> str:
    content = report["content"]
    bib = report["bibliography"]
    web = report["web"]
    epub = report["epub"]
    status_icon = "PASS" if report["status"] == "PASS" else "FAIL"
    lines = [
        "# Quality-assurance report",
        "",
        f"**Release status: {status_icon}**",
        "",
        "This report was produced by `scripts/qa_repository.py`. A PASS means that the automated release checks found no broken internal links, unresolved bibliography correspondence, missing required chapter sections, inaccessible chapter figures, or invalid EPUB container structure.",
        "",
        "## Release summary",
        "",
        "| Check | Result |",
        "|---|---:|",
        f"| Rendered chapters | {content['chapters_html']} |",
        f"| Editable Markdown chapters | {content['chapters_markdown']} |",
        f"| Appendices | {content['appendices_html']} |",
        f"| Chapter body words, excluding reference lists | {content['chapter_body_words_excluding_references']:,} |",
        f"| Average chapter length | {content['average_chapter_words']:,.0f} words |",
        f"| Shortest / longest chapter | {content['shortest_chapter_words']:,} / {content['longest_chapter_words']:,} words |",
        f"| Chapter diagrams / unique assignments | {content['chapter_figures']} / {content['unique_chapter_figure_sources']} |",
        f"| Responsive chapter tables | {content['chapter_tables']} |",
        f"| Global bibliography entries | {bib['global_reference_entries']} |",
        f"| Chapter references absent from global bibliography | {bib['chapter_references_missing_from_global']} |",
        f"| Global references absent from chapter lists | {bib['global_references_not_in_chapter_lists']} |",
        f"| Duplicate global references | {bib['duplicate_global_entries']} |",
        f"| Internal links checked | {web['internal_links_checked']:,} |",
        f"| Broken paths / broken fragments | {web['broken_links']} / {web['broken_fragments']} |",
        f"| Images missing alternative text | {web['images_missing_alt']} |",
        f"| Tables lacking headers / responsive wrappers | {web['tables_without_headers']} / {web['tables_without_responsive_wrapper']} |",
        f"| Pages with duplicate IDs | {web['pages_with_duplicate_ids']} |",
        f"| Search-index entries | {web['search_index_entries']} |",
        f"| EPUB ZIP integrity | {'Pass' if epub.get('zip_test') else 'Fail'} |",
        f"| EPUB mimetype and package structure | {'Pass' if epub.get('mimetype_valid') and epub.get('navigation_present') and epub.get('package_document_present') and epub.get('cover_resource_present') else 'Fail'} |",
        f"| Release-blocking errors | {report['release_blocking_errors']} |",
        f"| Non-blocking warnings | {report['warnings']} |",
        "",
        "## What was checked",
        "",
        "- Sequential chapter numbering and parity between editable Markdown and rendered HTML.",
        "- Presence of learning goals, key ideas, study-and-practice material, and chapter-specific references in every chapter.",
        "- Correct previous/next chapter navigation after the structural reordering.",
        "- Local paths and fragment identifiers across the complete prebuilt site.",
        "- Alternative text, captions, file existence, table headers, responsive overflow behavior, duplicate IDs, and heading hierarchy.",
        "- Exact set equality between the union of chapter reference lists and the global bibliography.",
        "- Machine-readable citation-audit status, search-index integrity, GitHub Pages deployment files, and EPUB container validity.",
        "",
        "## Citation scope",
        "",
        "The citation checks establish author–year/bibliography correspondence and ensure that the published reference list contains only works represented in chapter reference lists. They do not independently reproduce every study or establish that every source supports every clause at systematic-review depth. That remains a scholarly editorial judgment, particularly for contested or context-sensitive effects.",
        "",
        "## Issues",
        "",
    ]
    if not issues:
        lines.append("No automated issues were found.")
    else:
        for level in ("error", "warning"):
            subset = [i for i in issues if i.level == level]
            if not subset:
                continue
            lines.extend([f"### {level.title()}s", ""])
            for i in subset:
                lines.append(f"- `{i.code}` — **{i.file}**: {i.detail}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", default=Path(__file__).resolve().parents[1], type=Path)
    args = parser.parse_args()
    report, issues = audit(args.repo)
    repo = args.repo.resolve()
    (repo / "qa-report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    (repo / "QA_REPORT.md").write_text(make_markdown(report, issues), encoding="utf-8")
    print(json.dumps({
        "status": report["status"],
        "release_blocking_errors": report["release_blocking_errors"],
        "warnings": report["warnings"],
        "chapters": report["content"]["chapters_html"],
        "body_words": report["content"]["chapter_body_words_excluding_references"],
        "figures": report["content"]["chapter_figures"],
        "tables": report["content"]["chapter_tables"],
        "references": report["bibliography"]["global_reference_entries"],
        "broken_links": report["web"]["broken_links"] + report["web"]["broken_fragments"],
    }, indent=2))
    return 1 if report["release_blocking_errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
