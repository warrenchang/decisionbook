#!/usr/bin/env python3
"""Refresh reader-facing chapter links after structural revisions.

Canonical source filenames carry the current chapter number and title. This
script still derives numbering and titles from the HTML profile, redirects
links from retained merged sources, and refreshes Markdown labels that begin
with ``Chapter N``.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "_quarto-html.yml"
CHAPTER_LINE = re.compile(r"^\s{8}-\s+(chapters/[^\s]+\.qmd)\s*$", re.MULTILINE)
PART_LINE = re.compile(r"^\s{4}-\s+part:\s+(parts/[^\s]+\.qmd)\s*$", re.MULTILINE)
H1 = re.compile(r"^#\s+(.+?)(?:\s+\{[^}]+\})?\s*$", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

REDIRECTS = {
    "01-the-choice-is-the-tip-of-the-iceberg.qmd": "01-how-decisions-should-be-made-and-how-they-actually-are.qmd",
    "01-decision-making-is-a-process-not-a-moment.qmd": "01-how-decisions-should-be-made-and-how-they-actually-are.qmd",
    "02-a-rational-benchmark-not-a-portrait.qmd": "02-building-a-better-decision-alternatives-opportunity-cost-information-and-robustness.qmd",
    "02-building-a-better-decision-rationality-alternatives-and-opportunity-cost.qmd": "02-building-a-better-decision-alternatives-opportunity-cost-information-and-robustness.qmd",
    "appendix-a-portable-course-tools.qmd": "appendix-c-portable-course-tools.qmd",
    "appendix-b-portable-course-tools.qmd": "appendix-c-portable-course-tools.qmd",
    "appendix-b-index-of-major-course-examples.qmd": "appendix-d-index-of-major-course-examples.qmd",
    "appendix-c-index-of-major-course-examples.qmd": "appendix-d-index-of-major-course-examples.qmd",
    "appendix-c-how-behavioral-evidence-is-built.qmd": "appendix-e-how-behavioral-evidence-is-built.qmd",
    "appendix-d-how-behavioral-evidence-is-built.qmd": "appendix-e-how-behavioral-evidence-is-built.qmd",
    "appendix-d-when-evidence-breaks.qmd": "appendix-f-when-evidence-breaks.qmd",
    "appendix-e-when-evidence-breaks.qmd": "appendix-f-when-evidence-breaks.qmd",
    "appendix-f-evolutionary-explanations-of-value-choice-and-rationality.qmd": "appendix-b-evolutionary-explanations-of-value-choice-and-rationality.qmd",
    "retired-opportunity-cost-information-and-better-options.qmd": "02-building-a-better-decision-alternatives-opportunity-cost-information-and-robustness.qmd",
    "retired-heuristics-the-adaptive-toolbox.qmd": "08-fast-and-frugal-thinking.qmd",
    "retired-resemblance-is-not-probability.qmd": "09-what-feels-likely-availability-affect-and-resemblance.qmd",
    "retired-fluency-familiarity-and-the-feeling-of-truth.qmd": "13-accessibility-familiarity-and-ease.qmd",
    "retired-wanting-craving-and-self-control.qmd": "21-habits-wanting-and-self-control.qmd",
    "retired-asset-bubbles.qmd": "27-markets-mispricing-and-bubbles.qmd",
    "retired-conformity-norms-and-social-proof.qmd": "26-social-norms-and-conformity-when-other-people-become-evidence.qmd",
    "retired-anchors-concessions-and-bargaining-tactics.qmd": "36-preparing-and-claiming-value.qmd",
}


def canonical() -> list[Path]:
    return [ROOT / item for item in CHAPTER_LINE.findall(CONFIG.read_text(encoding="utf-8"))]


def title(path: Path) -> str:
    match = H1.search(path.read_text(encoding="utf-8"))
    if not match:
        raise ValueError(f"Missing H1 in {path.relative_to(ROOT)}")
    return match.group(1).strip()


def source_files(chapters: list[Path]) -> list[Path]:
    files = set(chapters)
    config = CONFIG.read_text(encoding="utf-8")
    files.update(ROOT / item for item in PART_LINE.findall(config))
    files.update(ROOT.glob("appendices/*.qmd"))
    for name in (
        "index.qmd",
        "how-to-use-this-book.qmd",
        "how-to-read-evidence.qmd",
        "concept-index.qmd",
        "about.qmd",
    ):
        path = ROOT / name
        if path.exists():
            files.add(path)
    return sorted(files)


def redirect_target(raw: str) -> str:
    if ".qmd" not in raw:
        return raw
    path_part, marker, fragment = raw.partition("#")
    name = Path(path_part).name
    replacement = REDIRECTS.get(name)
    if not replacement:
        return raw
    redirected = str(Path(path_part).with_name(replacement))
    if name.startswith("appendix-"):
        return f"{redirected}#{fragment}" if marker else redirected
    # Headings in merged chapters are deliberately rebuilt. A chapter-level
    # link is safer than retaining an anchor that may now identify other text.
    return redirected


def refresh(path: Path, numbering: dict[Path, tuple[int, str]]) -> bool:
    original = path.read_text(encoding="utf-8")

    def replace_link(match: re.Match[str]) -> str:
        label, raw_target = match.groups()
        target = redirect_target(raw_target)
        source_part = target.split("#", 1)[0].split("?", 1)[0]
        if not source_part.endswith(".qmd"):
            return f"[{label}]({target})"
        resolved = (path.parent / source_part).resolve()
        details = numbering.get(resolved)
        if details and re.match(r"^Chapters?\s+\d+", label):
            number, chapter_title = details
            if re.match(r"^Chapter\s+\d+\s*[,—:-]", label):
                label = f"Chapter {number}, {chapter_title}"
            elif re.fullmatch(r"Chapter\s+\d+", label):
                label = f"Chapter {number}"
            elif re.match(r"^Chapter\s+\d+\b", label):
                label = re.sub(r"^Chapter\s+\d+", f"Chapter {number}", label)
        return f"[{label}]({target})"

    revised = MARKDOWN_LINK.sub(replace_link, original)
    if revised == original:
        return False
    path.write_text(revised, encoding="utf-8")
    return True


def main() -> int:
    chapters = canonical()
    numbering = {path.resolve(): (index, title(path)) for index, path in enumerate(chapters, 1)}
    changed = [path for path in source_files(chapters) if refresh(path, numbering)]
    print(f"Refreshed chapter links in {len(changed)} file(s).")
    for path in changed:
        print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
