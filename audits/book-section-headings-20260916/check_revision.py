"""Verify the heading revision against the preceding prose-revision snapshot."""
from collections import Counter
import gzip
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import re
import zipfile

AUDIT = Path(__file__).resolve().parent
ROOT = AUDIT.parents[1]
BASE = json.loads(gzip.decompress((AUDIT / 'before-sources.json.gz').read_bytes()))
EDITS = json.loads((AUDIT / 'heading-edits.json').read_text())
spec = importlib.util.spec_from_file_location('reading_layers', ROOT / 'audits/book-redundant-hedging-20260916/check_reading_layers.py')
layers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(layers)


def normalize(text):
    return ' '.join(text.replace('’', "'").replace('“', '"').replace('”', '"').split())


class Titles(HTMLParser):
    def __init__(self):
        super().__init__()
        self.captures = []
        self.stack = []
        self.titles = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag not in layers.VOID:
            self.stack.append(tag)
        if re.fullmatch(r'h[1-6]', tag) or {'callout-title-container', 'callout-title'} & set(attrs.get('class', '').split()):
            self.captures.append({'depth': len(self.stack), 'text': []})

    def handle_data(self, text):
        for capture in self.captures:
            capture['text'].append(text)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == tag:
                self.stack = self.stack[:i]
                break
        ended = [c for c in self.captures if c['depth'] > len(self.stack)]
        for capture in ended:
            self.titles.append(normalize(''.join(capture['text'])))
            self.captures.remove(capture)


def parse_titles(text):
    parser = Titles()
    parser.feed(text)
    return parser.titles


def main():
    expected = BASE.copy()
    for edit in EDITS:
        assert expected[edit['file']].count(edit['before']) == 1
        expected[edit['file']] = expected[edit['file']].replace(edit['before'], edit['after'], 1)
    for edit in json.loads((AUDIT / 'chapter26-prose-edits.json').read_text()):
        assert expected[edit['file']] == edit['before_after_headings']
        expected[edit['file']] = edit['after']
    for edit in json.loads((AUDIT / 'index-edits.json').read_text()):
        assert edit['before'] in expected[edit['file']]
        expected[edit['file']] = expected[edit['file']].replace(edit['before'], edit['after'], 1)

    issues, preservation, html_rows, epub_rows = [], [], [], []
    before_ids = json.loads((AUDIT / 'before-rendered-ids.json').read_text())
    for source, before in BASE.items():
        after = (ROOT / source).read_text()
        row = {'source': source, 'matches_edit_log': expected[source] == after}
        for label, pattern in [
            ('references_unchanged', r'^::: \{\.reference\}\n(.*?)\n:::'),
            ('code_unchanged', r'^```.*?\n.*?\n```'),
            ('figure_markup_unchanged', r'^!\[.*?\]\([^\n]+'),
            ('display_math_unchanged', r'\$\$.*?\$\$'),
        ]:
            row[label] = re.findall(pattern, before, re.M | re.S) == re.findall(pattern, after, re.M | re.S)
        anchors = lambda s: set(re.findall(r'\{[^}\n]*#([\w-]+)', s))
        row['explicit_anchors_preserved'] = anchors(before) <= anchors(after)
        # The crash heading now names 1987. Compare numbers outside headings;
        # all heading changes themselves are checked by the exact edit replay.
        body_numbers = lambda s: re.findall(r'\b\d+(?:\.\d+)?%?', re.sub(r'^#{1,6} .*$', '', s, flags=re.M))
        row['body_numbers_unchanged'] = body_numbers(before) == body_numbers(after)
        if not all(v for k, v in row.items() if k != 'source'):
            issues.append(f'{source}: source preservation failed')
        preservation.append(row)

        html = (ROOT / 'docs' / Path(source).with_suffix('.html')).read_text()
        parsed = layers.parse(html)
        missing = sorted(set(before_ids[source]) - set(parsed.ids))
        duplicate = sorted(i for i, n in Counter(parsed.ids).items() if n > 1)
        if missing or duplicate:
            issues.append(f'{source}: missing IDs {missing}; duplicate IDs {duplicate}')
        titles = parse_titles(html)
        for edit in [e for e in EDITS if e['file'] == source]:
            if not any(normalize(edit['new_title']) in t for t in titles):
                issues.append(f'{source}: revised title missing from HTML: {edit["new_title"]}')
            if any(normalize(edit['old_title']) == t for t in titles):
                issues.append(f'{source}: old heading remains in HTML: {edit["old_title"]}')
            if edit['anchor'] and edit['anchor'] not in parsed.ids:
                issues.append(f'{source}: revised heading has lost its previous anchor')
        outside = [m for m in parsed.math if not m['callout']]
        if source.startswith('chapters/') and outside:
            issues.append(f'{source}: math outside optional callouts')
        html_rows.append({'source': source, 'missing_ids': missing, 'duplicate_ids': duplicate,
                          'main_math': len(outside), 'mathematical_boxes': len(parsed.boxes)})

    epub_titles = []
    baseline_duplicates = json.loads((AUDIT / 'baseline-epub-duplicate-ids.json').read_text())['duplicates']
    with zipfile.ZipFile(ROOT / 'docs/Decision-in-the-Making.epub') as archive:
        for name in archive.namelist():
            if not name.endswith('.xhtml'):
                continue
            xhtml = archive.read(name).decode()
            epub_titles.extend(parse_titles(xhtml))
            parsed = layers.parse(xhtml)
            duplicate_counts = {i: n for i, n in Counter(parsed.ids).items() if n > 1}
            duplicate = sorted(duplicate_counts)
            introduced_duplicates = sorted(i for i, n in duplicate_counts.items()
                                           if n > baseline_duplicates.get(name, {}).get(i, 1))
            is_chapter = any(re.fullmatch(r'chapter-\d+-start', i) for i in parsed.ids)
            outside = [m for m in parsed.math if not m['callout']]
            if introduced_duplicates or (is_chapter and outside):
                issues.append(f'{name}: new duplicate IDs {introduced_duplicates}; chapter main math {len(outside) if is_chapter else 0}')
            epub_rows.append({'file': name, 'is_chapter': is_chapter, 'pre_existing_duplicate_ids': duplicate,
                              'introduced_duplicate_ids': introduced_duplicates,
                              'main_math': len(outside), 'mathematical_boxes': len(parsed.boxes)})
    for edit in EDITS:
        if not any(normalize(edit['new_title']) in t for t in epub_titles):
            issues.append(f'EPUB: revised title missing: {edit["new_title"]}')
    if sum(r['is_chapter'] for r in epub_rows) != 42:
        issues.append('Expected all 42 chapters in the EPUB')
    report = {'status': 'PASS' if not issues else 'FAIL', 'issues': issues,
              'configured_sources': len(BASE), 'heading_changes': len(EDITS),
              'files_with_heading_changes': len({e['file'] for e in EDITS}),
              'total_files_changed': sum(BASE[f] != expected[f] for f in BASE),
              'html_mathematical_boxes': sum(r['mathematical_boxes'] for r in html_rows),
              'epub_mathematical_boxes': sum(r['mathematical_boxes'] for r in epub_rows),
              'pre_existing_epub_duplicate_wrapper_ids': sum(len(r['pre_existing_duplicate_ids']) for r in epub_rows),
              'limits': ['Existing EPUB callout wrapper duplicate IDs are recorded against the preceding commit; no new duplicates are allowed.',
                         'Visual EPUB checks use extracted XHTML, not native-reader pagination.'],
              'sources': preservation, 'html': html_rows, 'epub': epub_rows}
    (AUDIT / 'revision-qa.json').write_text(json.dumps(report, indent=2) + '\n')
    source_ok = all(all(v for k, v in row.items() if k != 'source') for row in preservation)
    (AUDIT / 'source-preservation-qa.json').write_text(json.dumps({
        'status': 'PASS' if source_ok else 'FAIL', 'sources': preservation}, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k not in ['sources', 'html', 'epub']}, indent=2))
    return int(bool(issues))


if __name__ == '__main__':
    raise SystemExit(main())
