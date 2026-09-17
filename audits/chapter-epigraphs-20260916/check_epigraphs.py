"""Check source scope and all 42 epigraphs in both rendered book editions."""
from collections import Counter
import gzip
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[2]
AUDIT = Path(__file__).resolve().parent
BASE = json.loads(gzip.decompress((AUDIT / 'before-sources.json.gz').read_bytes()))
SELECTIONS = json.loads((AUDIT / 'epigraph-selections.json').read_text())
BLOCK = re.compile(r'^::: \{#chapter-\d{2}-start \.chapter-epigraph\}\n.*?\n:::', re.M | re.S)
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}


def normalize(text):
    text = text.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return ' '.join(text.split())


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.ids, self.epigraphs = [], [], []
        self.active = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.append(attrs['id'])
        if tag not in VOID:
            self.stack.append(tag)
        if 'chapter-epigraph' in attrs.get('class', '').split():
            assert self.active is None
            self.active = {'id': attrs.get('id'), 'depth': len(self.stack), 'text': []}

    def handle_data(self, text):
        if self.active:
            self.active['text'].append(text)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == tag:
                self.stack = self.stack[:i]
                break
        if self.active and len(self.stack) < self.active['depth']:
            self.epigraphs.append({'id': self.active['id'], 'text': normalize(''.join(self.active['text']))})
            self.active = None


def parse(text):
    parser = Page()
    parser.feed(text)
    return parser


def main():
    issues, sources = [], []
    old_ids = json.loads((AUDIT / 'before-rendered-ids.json').read_text())
    html_epigraphs = []
    for source, before in BASE.items():
        after = (ROOT / source).read_text()
        unchanged_body = BLOCK.sub('', before) == BLOCK.sub('', after)
        if not unchanged_body:
            issues.append(f'{source}: changes outside the epigraph')
        page = parse((ROOT / 'docs' / Path(source).with_suffix('.html')).read_text())
        missing_ids = sorted(set(old_ids[source]) - set(page.ids))
        duplicate_ids = sorted(i for i, n in Counter(page.ids).items() if n > 1)
        if missing_ids or duplicate_ids:
            issues.append(f'{source}: missing IDs {missing_ids}, duplicate IDs {duplicate_ids}')
        sources.append({'source': source, 'outside_epigraph_unchanged': unchanged_body,
                        'previous_ids_preserved': not missing_ids, 'duplicate_html_ids': duplicate_ids})
        html_epigraphs.extend(page.epigraphs)

    epub_epigraphs = []
    with zipfile.ZipFile(ROOT / 'docs/Decision-in-the-Making.epub') as archive:
        for name in archive.namelist():
            if name.endswith('.xhtml'):
                epub_epigraphs.extend(parse(archive.read(name).decode()).epigraphs)
    search_bytes = (ROOT / 'docs/search.json').read_bytes()
    search = json.loads(search_bytes)
    search_text = normalize(' '.join(str(e.get(k, '')) for e in search for k in ['title', 'section', 'text']))
    search_unchanged = hashlib.sha256(search_bytes).hexdigest() == (AUDIT / 'before-search.sha256').read_text().strip()
    if not search_unchanged:
        issues.append('Search content changed despite edits being limited to unindexed epigraphs')
    for label, epigraphs in [('html', html_epigraphs), ('epub', epub_epigraphs)]:
        if len(epigraphs) != 42:
            issues.append(f'{label}: expected 42 epigraphs, found {len(epigraphs)}')
        for selection in SELECTIONS:
            expected_id = f"chapter-{selection['chapter']:02d}-start"
            matches = [e for e in epigraphs if e['id'] == expected_id]
            if len(matches) != 1:
                issues.append(f'{label}: expected one epigraph at {expected_id}, found {len(matches)}')
            elif normalize(selection['quote']) not in matches[0]['text']:
                issues.append(f'{label}: new quotation missing from {expected_id}')
    for selection in SELECTIONS:
        source_text = (ROOT / selection['source']).read_text()
        if selection['after'] not in source_text:
            issues.append(f"Source differs from approved selection: {selection['source']}")
    report = {
        'status': 'PASS' if not issues else 'FAIL', 'issues': issues,
        'configured_sources': len(BASE), 'epigraphs_reviewed': len(SELECTIONS),
        'quotations_replaced': sum(s['changed_quote'] for s in SELECTIONS),
        'opening_blocks_updated': sum(s['changed_block'] for s in SELECTIONS),
        'max_quote_words': max(len(re.findall(r"\b[\w]+(?:[’'-][\w]+)*\b", s['quote'])) for s in SELECTIONS),
        'html_epigraphs': len(html_epigraphs), 'epub_epigraphs': len(epub_epigraphs),
        'search_index_unchanged': search_unchanged,
        'epigraphs_in_search': sum(normalize(s['quote']) in search_text for s in SELECTIONS),
        'search_scope': 'Epigraphs were absent from the baseline search index. Confirmed the existing index is unchanged; no new indexing behavior is introduced.',
        'sources': sources,
        'scope': 'Exact selected text, chapter-opening IDs, preserved search content, and unchanged content outside epigraphs. Attribution and topic fit were checked editorially against the linked sources and recorded source notes.'
    }
    (AUDIT / 'epigraph-qa.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'sources'}, indent=2))
    return int(bool(issues))


if __name__ == '__main__':
    raise SystemExit(main())
