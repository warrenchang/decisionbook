#!/usr/bin/env python3
"""Refresh reader-facing chapter links after the 2026 structural consolidation.

The source filenames are intentionally stable where possible, so their numeric
prefixes do not represent reader-facing chapter numbers. This script derives
numbers and titles from the canonical HTML profile, redirects links from merged
source files, and refreshes Markdown labels that begin with ``Chapter N``.
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
    "03-opportunity-cost-information-and-better-options.qmd": "02-a-rational-benchmark-not-a-portrait.qmd",
    "09-heuristics-the-adaptive-toolbox.qmd": "04-fast-answers-slow-inspection.qmd",
    "11-resemblance-is-not-probability.qmd": "10-feeling-and-availability-as-shortcuts.qmd",
    "17-fluency-familiarity-and-the-feeling-of-truth.qmd": "16-priming-and-the-active-mental-context.qmd",
    "20-wanting-craving-and-self-control.qmd": "19-habits-when-decisions-move-downstairs.qmd",
    "44-asset-bubbles.qmd": "43-behavioral-finance.qmd",
    "23-conformity-norms-and-social-proof.qmd": "22-social-learning-mimicry-and-attribution.qmd",
    "32-anchors-concessions-and-bargaining-tactics.qmd": "31-preparing-to-claim-value.qmd",
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
