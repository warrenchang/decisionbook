#!/usr/bin/env python3
"""Remove Quarto's trailing template space from newly added review navigation."""
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r'(<div class="sidebar-item-container">)[ \t]+(?=\n\s*<a href="[^"]*part-[1-7]-review\.html")')

def main():
    changed = 0
    for path in (ROOT / 'docs').rglob('*.html'):
        before = path.read_text()
        after = PATTERN.sub(r'\1', before)
        if after != before:
            path.write_text(after)
            changed += 1
    print(f'Normalized review navigation in {changed} HTML files')

if __name__ == '__main__':
    main()
