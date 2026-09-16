"""Check the edited reading layers against the recorded clean baseline."""
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[2]
AUDIT = Path(__file__).resolve().parent
BASE = (AUDIT / 'baseline-commit.txt').read_text().strip()
SOURCES = list(dict.fromkeys(re.findall(
    r'(?:- |part: )([^\s]+\.qmd)', (ROOT / '_quarto-html.yml').read_text())))
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
        'meta', 'param', 'source', 'track', 'wbr'}


class ReadingLayers(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.math = []
        self.headings = []
        self.ids = []
        self.boxes = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get('class', '').split()
        if attrs.get('id'):
            self.ids.append(attrs['id'])
            if tag == 'section' or re.fullmatch(r'h[1-6]', tag):
                self.headings.append(attrs['id'])
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])
        if 'mathematical-analysis' in classes:
            self.boxes.append(attrs.get('id', ''))
        if (tag == 'span' and 'math' in classes) or tag == 'math':
            self.math.append({
                'kind': 'display' if 'display' in classes or attrs.get('display') == 'block' else 'inline',
                'callout': any('callout' in cs for _, cs in self.stack),
                'mathematical_analysis': any('mathematical-analysis' in cs for _, cs in self.stack),
            })
        if tag not in VOID:
            self.stack.append((tag, classes))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                self.stack = self.stack[:i]
                break


def parse(text):
    result = ReadingLayers()
    result.feed(text)
    return result


def inspect():
    issues = []
    rows = []
    preservation = []
    old_headings = json.loads((AUDIT / 'baseline-heading-anchors.json').read_text())
    old_math = json.loads((AUDIT / 'baseline-rendered-math.json').read_text())
    for source in SOURCES:
        current = (ROOT / source).read_text()
        before = subprocess.check_output(['git', 'show', f'{BASE}:{source}'], cwd=ROOT, text=True)
        refs = lambda s: re.findall(r'^::: \{\.reference\}\n(.*?)\n:::', s, re.S | re.M)
        anchors = lambda s: set(re.findall(r'\{[^}\n]*#([\w-]+)', s))
        code = lambda s: re.findall(r'```python\n(.*?)\n```', s, re.S)
        kept = {
            'source': source,
            'changed': before != current,
            'references_unchanged': refs(before) == refs(current),
            'explicit_anchors_preserved': anchors(before) <= anchors(current),
            'python_examples_unchanged': code(before) == code(current),
        }
        preservation.append(kept)
        if source.startswith('appendices/appendix-a-') and before != current:
            issues.append('The dedicated mathematical appendix was unexpectedly changed')
        if not all(kept[k] for k in ['references_unchanged', 'explicit_anchors_preserved', 'python_examples_unchanged']):
            issues.append(f'{source}: preservation check failed')
        rendered = parse((ROOT / 'docs' / Path(source).with_suffix('.html')).read_text())
        missing = set(old_headings.get(source, [])) - set(rendered.ids)
        if missing:
            issues.append(f'{source}: missing old heading anchors {sorted(missing)}')
        if len(rendered.ids) != len(set(rendered.ids)):
            issues.append(f'{source}: duplicate HTML identifiers')
        outside = [m for m in rendered.math if not m['callout']]
        if source.startswith('chapters/') and outside:
            issues.append(f'{source}: {len(outside)} math expressions outside optional callouts')
        expected_boxes = current.count('.mathematical-analysis')
        if expected_boxes != len(rendered.boxes):
            issues.append(f'{source}: expected {expected_boxes} mathematical boxes, found {len(rendered.boxes)}')
        rows.append({'source': source, 'math_total': len(rendered.math),
                     'main_inline': sum(m['kind'] == 'inline' for m in outside),
                     'main_display': sum(m['kind'] == 'display' for m in outside),
                     'mathematical_boxes': len(rendered.boxes)})

    epub_rows = []
    with zipfile.ZipFile(ROOT / 'docs/Decision-in-the-Making.epub') as archive:
        for name in archive.namelist():
            if not name.endswith('.xhtml'):
                continue
            rendered = parse(archive.read(name).decode())
            is_chapter = any(re.fullmatch(r'chapter-\d+-start', i) for i in rendered.ids)
            if not is_chapter and not rendered.boxes:
                continue
            outside = [m for m in rendered.math if not m['callout']]
            if outside:
                issues.append(f'{name}: {len(outside)} main-text EPUB math expressions')
            duplicates = [i for i, n in Counter(rendered.ids).items() if n > 1 and i.startswith('math-')]
            if duplicates:
                issues.append(f'{name}: duplicated mathematical-analysis anchors {duplicates}')
            epub_rows.append({'file': name, 'is_chapter': is_chapter, 'main_math': len(outside), 'math_total': len(rendered.math),
                              'mathematical_boxes': len(rendered.boxes)})
    if sum(r['is_chapter'] for r in epub_rows) != 42:
        issues.append('EPUB inspection did not cover all 42 chapters')
    if not sum(r['math_total'] for r in epub_rows):
        issues.append('EPUB inspection found no mathematics to validate')
    chapter_sources = [r for r in rows if r['source'].startswith('chapters/')]
    baseline_chapters = [r for r in old_math if r['source'].startswith('chapters/')]
    report = {
        'status': 'PASS' if not issues else 'FAIL', 'issues': issues,
        'configured_sources_reviewed': len(SOURCES),
        'chapters_reviewed': len(chapter_sources),
        'chapters_revised': sum(p['changed'] for p in preservation if p['source'].startswith('chapters/')),
        'baseline_main_inline_math': sum(r['main_inline'] for r in baseline_chapters),
        'baseline_main_display_math': sum(r['main_display'] for r in baseline_chapters),
        'final_main_inline_math': sum(r['main_inline'] for r in chapter_sources),
        'final_main_display_math': sum(r['main_display'] for r in chapter_sources),
        'mathematical_analysis_boxes': sum(r['mathematical_boxes'] for r in rows),
        'html': rows, 'epub': epub_rows,
        'limits': ['Counts concern rendered text mathematics, not notation embedded in figures.',
                   'EPUB structure is checked here; native-reader pagination is not tested.'],
    }
    (AUDIT / 'reading-layers-qa.json').write_text(json.dumps(report, indent=2) + '\n')
    (AUDIT / 'source-preservation-qa.json').write_text(json.dumps({
        'status': 'PASS' if all(p['references_unchanged'] and p['explicit_anchors_preserved'] and p['python_examples_unchanged'] for p in preservation) else 'FAIL',
        'sources': preservation,
    }, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k not in ['html', 'epub']}, indent=2))
    return 1 if issues else 0


if __name__ == '__main__':
    raise SystemExit(inspect())
