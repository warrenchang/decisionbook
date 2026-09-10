"""Refresh final source/asset hashes and compare this revision with its saved baseline."""
from pathlib import Path
import hashlib
import json
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[2]
AUDIT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'scripts'))
from qa_quarto_book import strip_reference_tail, word_count

def digest(data):
    return hashlib.sha256(data).hexdigest()

inventory = json.loads((AUDIT / 'inventory.json').read_text())
ledgers = ['root-ledger.json', 'chapters_01_14-ledger.json',
           'chapters_15_28-ledger.json', 'chapters_29_41-ledger.json', 'indexes-ledger.json']
source_reviews, figure_reviews = {}, {}
for name in ledgers:
    data = json.loads((AUDIT / name).read_text())
    for row in data.get('sources', []):
        source_reviews[row['path']] = {'ledger': name, 'full_read': row.get('full_read', row.get('read_complete', False))}
    for row in data.get('figures', []):
        figure_reviews[row['path']] = {'ledger': name,
            'individual_visual_inspection': row.get('individual_visual_inspection', False),
            'contact_sheet_inspection': row.get('contact_sheet_inspection', row.get('contact_sheet_inspected', False))}

sources, figures = [], []
with zipfile.ZipFile(AUDIT / 'before.zip') as archive:
    for original in inventory['sources']:
        path = original['path']
        before = archive.read(path)
        after = (ROOT / path).read_bytes()
        row = dict(original, **source_reviews.get(path, {}),
                   sha256_after=digest(after), changed=before != after,
                   source_words_after=len(re.findall(r"\b[\w’'-]+\b", after.decode())))
        if path.startswith('chapters/'):
            row['chapter_text_words_before'] = word_count(strip_reference_tail(before.decode()))
            row['chapter_text_words_after'] = word_count(strip_reference_tail(after.decode()))
        sources.append(row)
    for original in inventory['figures']:
        path = original['path']
        before = archive.read(path)
        after = (ROOT / path).read_bytes()
        figures.append(dict(original, **figure_reviews.get(path, {}),
                            sha256_before=digest(before), sha256_after=digest(after), changed=before != after))
cover = 'figures/cover.png'
figures.append(dict(path=cover, owner='root', **figure_reviews.get(cover, {}),
                    sha256_after=digest((ROOT / cover).read_bytes()), changed=False))

chapters = [row for row in sources if row['path'].startswith('chapters/')]
before = sum(row['chapter_text_words_before'] for row in chapters)
after = sum(row['chapter_text_words_after'] for row in chapters)
summary = {
    'baseline_commit': inventory['baseline_commit'],
    'configured_sources': len(sources),
    'full_read_sources': sum(bool(row.get('full_read')) for row in sources),
    'generated_reference_sources': 1,
    'chapters': len(chapters),
    'chapter_text_words_before': before,
    'chapter_text_words_after': after,
    'chapter_text_reduction_percent': round(100 * (before - after) / before, 2),
    'word_count_scope': 'Approximate chapter text including optional notes, captions, tables and equations; excludes YAML, local references, fenced code, HTML tags and URLs. Same qa_quarto_book.word_count method applied to saved baseline and final source.',
    'unique_figures_including_cover': len(figures),
    'figures_changed': sum(row['changed'] for row in figures),
    'figures_individually_inspected': sum(bool(row.get('individual_visual_inspection')) for row in figures),
    'figures_contact_sheet_inspected': sum(bool(row.get('contact_sheet_inspection')) for row in figures),
}
artifacts = []
for path in ['docs/Decision-in-the-Making.epub', 'QA_REPORT.md', 'EPUB_QA_REPORT.md',
             'audits/rendered-figure-qa.json', 'audits/rendered-epub-figure-qa.json',
             'audits/book-revision-20260910/final-html-link-audit.json']:
    p = ROOT / path
    if p.exists():
        artifacts.append({'path': path, 'sha256': digest(p.read_bytes()), 'bytes': p.stat().st_size})
(AUDIT / 'final-coverage.json').write_text(json.dumps({'summary': summary, 'sources': sources,
    'figures': figures, 'artifacts': artifacts}, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(summary, indent=2))
