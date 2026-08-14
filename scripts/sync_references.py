#!/usr/bin/env python3
"""Synchronize references.qmd with the union of canonical chapter reference blocks.

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
CONFIG = ROOT / "_quarto.yml"
MASTER = ROOT / "references.qmd"
CHAPTER_LINE = re.compile(r"^\s*-\s+(chapters/[^\s]+\.qmd)\s*$", re.MULTILINE)
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


def clean_reference(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def reference_key(value: str) -> str:
    value = clean_reference(value).rstrip(".").casefold()
    value = value.replace("’", "'").replace("“", '"').replace("”", '"')
    value = value.replace("–", "-").replace("—", "-")
    value = re.sub(r"[*_`]", "", value)
    value = re.sub(r"\s*([,;:()])\s*", r"\1", value)
    return value


def sort_key(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    return "".join(char for char in decomposed if not unicodedata.combining(char))


def chapter_references() -> list[str]:
    unique: dict[str, str] = {}
    for path in canonical_chapters():
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
        "This master bibliography is the deduplicated union of the works cited in the canonical chapters. "
        "Each chapter also provides its own cited-reference list.\n\n"
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
        print(f"PASS: references.qmd contains {len(chapter_references())} unique chapter references.")
        return 0
    MASTER.write_text(expected, encoding="utf-8")
    print(f"Updated references.qmd with {len(chapter_references())} unique chapter references.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
