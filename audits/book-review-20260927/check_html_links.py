#!/usr/bin/env python3
"""Check local file/fragment targets in all configured HTML book pages."""
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / 'docs'


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids, self.links = set(), []
        self.feed(path.read_text())

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])


sources = re.findall(r'^\s*-\s+(?:part:\s+)?([^\s]+\.qmd)\s*$',
                     (ROOT / '_quarto-html.yml').read_text(), re.M)
pages = [DOCS / Path(p).with_suffix('.html') for p in sources]
cache, errors, checked = {}, [], 0
for path in pages:
    if not path.exists():
        errors.append(f'Missing configured page: {path.relative_to(ROOT)}')
        continue
    page = cache.setdefault(path, Page(path))
    for href in page.links:
        url = urlsplit(href)
        if url.scheme or url.netloc or not href:
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        if url.path.startswith('/'):
            target = DOCS / unquote(url.path).lstrip('/')
        if target.is_dir():
            target = target / 'index.html'
        checked += 1
        if not target.exists():
            errors.append(f'{path.relative_to(DOCS)}: missing file {href}')
        elif url.fragment and target.suffix == '.html':
            if target not in cache:
                cache[target] = Page(target)
            if unquote(url.fragment) not in cache[target].ids:
                errors.append(f'{path.relative_to(DOCS)}: missing fragment {href}')

result = dict(configured_pages=len(pages), local_links_checked=checked,
              issues=sorted(set(errors)), passed=not errors)
Path(__file__).with_name('html-link-check.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
raise SystemExit(bool(errors))
