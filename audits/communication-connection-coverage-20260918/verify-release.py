#!/usr/bin/env python3
"""Verify the lecture coverage destinations and the revised book release."""
from pathlib import Path
from zipfile import ZipFile
from collections import Counter
import hashlib, json, re
BASE=Path(__file__).resolve().parent
ROOT=BASE.parent.parent
rows=json.loads((BASE/'coverage.json').read_text())
source=json.loads((BASE/'source-inventory.json').read_text())
assert len(rows)==81 and [r['page'] for r in rows]==list(range(1,82))
assert hashlib.sha256(Path(source['path']).read_bytes()).hexdigest()==source['sha256'], 'Source PDF changed'
html_cache={}; checked=[]
with ZipFile(ROOT/'docs/Decision-in-the-Making.epub') as z:
    xhtml={n:z.read(n).decode('utf-8') for n in z.namelist() if n.endswith('.xhtml')}
for row in rows:
    if not row['rendered']:continue
    filename=row['rendered']; ident=row['anchor']; chapter=row['chapter']
    html=html_cache.setdefault(filename,(ROOT/filename).read_text())
    assert len(re.findall(r'\sid="'+re.escape(ident)+r'"',html))==1, ('HTML anchor',row['page'],ident)
    candidates=[(n,s) for n,s in xhtml.items() if f'id="chapter-{chapter}-start"' in s]
    assert len(candidates)==1, ('EPUB chapter',chapter)
    name,epub=candidates[0]
    epub_ident = f'{ident}-{chapter-1}' if ident == 'take-it-forward' else ident
    assert len(re.findall(r'\sid="'+re.escape(epub_ident)+r'"',epub))==1, ('EPUB anchor',row['page'],epub_ident)
    checked.append({'page':row['page'],'chapter':chapter,'anchor':ident,'epub_anchor':epub_ident,'epub':name})
ch33=(ROOT/'docs/chapters/33-communication-language-is-not-a-file-transfer.html').read_text()
ch34=(ROOT/'docs/chapters/34-connection-and-repair-warm-honesty-makes-truth-usable.html').read_text()
ch38=(ROOT/'docs/chapters/38-designing-better-agreements.html').read_text()
assert 'id="fig-lie-cues-belief-gap"' in ch33
assert 'id="fig-lie-cues-belief-gap"' not in ch38
assert '33-communication-language-is-not-a-file-transfer.html#lie-detection' in ch38
assert 'rate enjoyment, awkwardness, and connection from 0 to 10' in ch34
assert 'Stay on your side of the net during conflict' in (ROOT/'docs/search.json').read_text()
report={'source_pdf_unchanged':True,'pages_accounted_for':81,'coverage_rows_with_verified_destinations':len(checked),'actions':dict(Counter(r['action'] for r in rows)),'html_and_epub_anchors_unique':True,'lie_detection_relocation_preserved':True,'search_updated':True,'checked':checked,'artifact_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'chapters/33-communication-language-is-not-a-file-transfer.qmd',ROOT/'chapters/34-connection-and-repair-warm-honesty-makes-truth-usable.qmd',ROOT/'docs/Decision-in-the-Making.epub']}}
(BASE/'release-verification.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(f'PASS: 81 pages accounted for, {len(checked)} HTML and EPUB coverage destinations verified, source PDF unchanged.')
