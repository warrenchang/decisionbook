"""Verify retained navigation anchors and summarize the section hierarchy revision."""
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
AUDIT = Path(__file__).resolve().parent

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = Counter()
        self.capture = None
        self.headings = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids[attrs['id']] += 1
        if re.fullmatch('h[1-6]', tag):
            self.capture = {'tag': tag, 'id': attrs.get('id'), 'text': ''}
    def handle_data(self, data):
        if self.capture is not None:
            self.capture['text'] += data
    def handle_endtag(self, tag):
        if self.capture is not None and tag == self.capture['tag']:
            self.headings.append(self.capture)
            self.capture = None

sources = json.loads((AUDIT / 'source-baseline.json').read_text())
headings = json.loads((AUDIT / 'rendered-heading-baseline.json').read_text())
changes = []
missing = []
duplicates = []
for file, old in sources.items():
    current = (ROOT / file).read_text()
    if current != old:
        changes.append({'file': file,
                        'before_headings': len(re.findall(r'^#{2,6} ', old, re.M)),
                        'after_headings': len(re.findall(r'^#{2,6} ', current, re.M))})
    rendered = ROOT / 'docs' / Path(file).with_suffix('.html')
    page = Page()
    page.feed(rendered.read_text())
    for old_heading in headings.get(file, []):
        anchor = old_heading.get('id')
        if anchor and not page.ids[anchor]:
            missing.append({'file': file, **old_heading})
    duplicates.extend({'file': file, 'id': anchor, 'count': n}
                      for anchor, n in page.ids.items() if n > 1)
result = {'reviewed_sources': len(sources), 'changed_sources': changes,
          'heading_count_reduction': sum(x['before_headings'] - x['after_headings'] for x in changes),
          'old_rendered_heading_ids_checked': sum(bool(h.get('id')) for v in headings.values() for h in v),
          'missing_old_heading_ids': missing, 'duplicate_rendered_ids': duplicates}
(AUDIT / 'rendered-hierarchy-qa.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k:v for k,v in result.items() if k != 'changed_sources'},indent=2))
raise SystemExit(bool(missing or duplicates))
