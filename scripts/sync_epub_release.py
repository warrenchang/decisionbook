#!/usr/bin/env python3
"""Copy the staged Quarto EPUB beside the rendered HTML release.

The HTML and EPUB profiles intentionally use different output directories so
that one Quarto render cannot clean the other format. Both profiles call this
idempotent post-render hook. It is a no-op until an EPUB has been staged.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from normalize_epub_toc import normalize_epub


ROOT = Path(__file__).resolve().parents[1]
FILENAME = "Decision-in-the-Making.epub"
SOURCE = ROOT / "_epub" / FILENAME
TARGET = ROOT / "docs" / FILENAME


def main() -> int:
    if not SOURCE.is_file():
        print("No staged EPUB found; HTML release left unchanged.")
        return 0

    parts, chapters = normalize_epub(SOURCE)
    print(f"Normalized staged EPUB navigation: {parts} Parts, {chapters} numbered chapters")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE, TARGET)
    print(f"Copied staged EPUB to {TARGET}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
