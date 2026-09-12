#!/usr/bin/env python3
"""Synchronize references.qmd with the union of canonical chapter and appendix references.

Run from the repository root:
    python3 scripts/sync_references.py
    python3 scripts/sync_references.py --check
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "_quarto-html.yml"
MASTER = ROOT / "references.qmd"
CHAPTER_LINE = re.compile(r"^\s*-\s+(chapters/[^\s]+\.qmd)\s*$", re.MULTILINE)
APPENDIX_LINE = re.compile(r"^\s*-\s+(appendices/[^\s]+\.qmd)\s*$", re.MULTILINE)
REFERENCE_BLOCK = re.compile(
    r"^::: \{\.reference\}\s*\n(.*?)\n:::\s*$", re.MULTILINE | re.DOTALL
)


def canonical_chapters() -> list[Path]:
    paths = [ROOT / match for match in CHAPTER_LINE.findall(CONFIG.read_text(encoding="utf-8"))]
    missing = [path for path in paths if not path.exists()]
    if missing:
        joined = ", ".join(str(path.relative_to(ROOT)) for path in missing)
        raise SystemExit(f"Missing canonical chapter(s): {joined}")
    if len(paths) != len(set(paths)):
        raise SystemExit("The canonical chapter list contains a duplicate path.")
    return paths


def canonical_reference_sources() -> list[Path]:
    """Return reader-facing chapters and appendices that contribute cited works."""
    config = CONFIG.read_text(encoding="utf-8")
    paths = canonical_chapters() + [ROOT / match for match in APPENDIX_LINE.findall(config)]
    missing = [path for path in paths if not path.exists()]
    if missing:
        joined = ", ".join(str(path.relative_to(ROOT)) for path in missing)
        raise SystemExit(f"Missing canonical reference source(s): {joined}")
    if len(paths) != len(set(paths)):
        raise SystemExit("The canonical reference-source list contains a duplicate path.")
    return paths


def clean_reference(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def reference_key(value: str) -> str:
    value = clean_reference(value).rstrip(".").casefold()
    value = value.replace("’", "'").replace("“", '"').replace("”", '"')
    value = value.replace("–", "-").replace("—", "-")
    value = re.sub(r"[*_`]", "", value)
    value = re.sub(r"\s*([,;:()])\s*", r"\1", value)
    return value


def _alphabetic_text(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    return "".join(char for char in decomposed if char.isalnum() and not unicodedata.combining(char))


def _author_sort_key(author_text: str) -> tuple[tuple[str, str], ...]:
    # Reference authors use surname/initial pairs. An ampersand is punctuation,
    # not a name: Wood, Quinn ... must precede Wood & Runger, for example.
    author_text = re.sub(r"\((?:Ed|Eds|Trans)\.\)", "", author_text)
    author_text = re.sub(r"(?:,\s*)?\bet al\.\s*$", "", author_text, flags=re.IGNORECASE)
    author_text = re.sub(r",\s*(?:Jr\.|Sr\.|II|III|IV)(?=,|\s*$)", "", author_text)
    fields = [field.strip().lstrip("& ") for field in author_text.rstrip(". ").split(",")]
    initials = re.compile(r"(?:[A-ZÀ-ÖØ-Þ][.\-\s]*)+")
    if len(fields) % 2 == 0 and all(initials.fullmatch(fields[i]) for i in range(1, len(fields), 2)):
        return tuple((_alphabetic_text(fields[i]), _alphabetic_text(fields[i + 1])) for i in range(0, len(fields), 2))
    # Corporate authors and other unpaired author credits sort as one name.
    return ((_alphabetic_text(author_text), ""),)


def sort_key(value: str) -> tuple:
    """Order author lists, then date and title, without changing citation text.

    Tuple prefixes put a sole author before that author with collaborators,
    and a shorter author list before the same list extended by another author.

    >>> sort_key("Wood, W., Quinn, J. M., & Kashy, D. A. (2002). Habits.") < sort_key("Wood, W., & Rünger, D. (2016). Psychology of habit.")
    True
    >>> sort_key("Strayer, D. L., Drews, F. A., & Johnston, W. A. (2003). Driving.") < sort_key("Strayer, D. L., & Johnston, W. A. (2001). Distraction.")
    True
    >>> sort_key("Wood, W. (2025). Sole author.") < sort_key("Wood, W., & Neal, D. T. (2007). Collaborators.")
    True
    >>> sort_key("Doe, J., & Roe, A. (2025). Two authors.") < sort_key("Doe, J., Roe, A., & Smith, B. (1990). Three authors.")
    True
    >>> sort_key("Ho, M. Y., Worthington, E. L., Jr., Cowden, R. G., et al. (2024). Forgiveness.") < sort_key("Holt-Lunstad, J., Smith, T. B., & Layton, J. B. (2010). Relationships.")
    True
    """
    plain = re.sub(r"[*_`]", "", value)
    date = re.search(r"\((?:(\d{4})([a-z]?)(?:,[^)]*)?|(n\.d\.))\)", plain)
    if date is None:
        return (_author_sort_key(plain), -1, "", "", _alphabetic_text(plain))
    authors = _author_sort_key(plain[:date.start()].strip())
    year = int(date.group(1)) if date.group(1) else -1
    suffix = date.group(2) or ""
    title = plain[date.end():].lstrip(". ")
    title = re.sub(r"^(?:a|an|the)\s+", "", title, flags=re.IGNORECASE)
    return (authors, year, suffix, _alphabetic_text(title), _alphabetic_text(plain))


def chapter_references() -> list[str]:
    unique: dict[str, str] = {}
    for path in canonical_reference_sources():
        text = path.read_text(encoding="utf-8")
        for raw in REFERENCE_BLOCK.findall(text):
            reference = clean_reference(raw)
            key = reference_key(reference)
            if not reference:
                raise SystemExit(f"Empty reference block in {path.relative_to(ROOT)}")
            unique.setdefault(key, reference)
    return sorted(unique.values(), key=sort_key)


def rendered_master() -> str:
    blocks = "\n\n".join(f"::: {{.reference}}\n{reference}\n:::" for reference in chapter_references())
    return (
        "# References {.unnumbered}\n\n"
        "This master bibliography is the deduplicated union of the works cited in the canonical chapters and appendices. "
        "Each chapter and appendix also provides its own cited-reference list.\n\n"
        f"{blocks}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if references.qmd is out of sync.")
    args = parser.parse_args()
    expected = rendered_master()
    current = MASTER.read_text(encoding="utf-8") if MASTER.exists() else ""
    if args.check:
        if current != expected:
            print("FAIL: references.qmd is not synchronized with canonical chapter reference blocks.")
            return 1
        print(f"PASS: references.qmd contains {len(chapter_references())} unique chapter-and-appendix references.")
        return 0
    MASTER.write_text(expected, encoding="utf-8")
    print(f"Updated references.qmd with {len(chapter_references())} unique chapter-and-appendix references.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
