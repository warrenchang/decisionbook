#!/usr/bin/env python3
"""Record final artifacts, source provenance and the precise figure-review scope."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote,urlsplit
import hashlib,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).parent
paths=re.findall(r'^\s*-\s*(?:part:\s*)?([^\s]+\.qmd)\s*$',(ROOT/'_quarto-html.yml').read_text(),re.M)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
class Images(HTMLParser):
 def __init__(self,s):super().__init__();self.images=[];self.feed(s)
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='img' and 'figures/' in d.get('src',''):self.images.append(d['src'])
assets={}
for p in paths:
 html=ROOT/'docs'/Path(p).with_suffix('.html')
 for src in Images(html.read_text()).images:
  f=(html.parent/unquote(urlsplit(src).path)).resolve()
  rel=f.relative_to(ROOT/'docs').as_posix();assets.setdefault(rel,[]).append(p)
changes=set(subprocess.check_output(['git','diff','--name-only','--','figures/'],cwd=ROOT,text=True).splitlines())
compact={x['figure'] for x in json.loads((OUT/'compact-figure-placements.json').read_text())}
ledger=[]
for rel,uses in sorted(assets.items()):
 changed=rel in changes
 is_compact=Path(rel).name in compact
 if changed:
  review='Individually inspected final rendering and independent semantic/layout review. New compact diagrams also measured at 1440/390; calibration chart retains a wide reading pane.'
 else:
  review='Retained artwork inspected on book-wide contact sheets; final image loading, alt text and page containment checked. No new exhaustive per-label scientific audit is claimed.'
 ledger.append({'asset':rel,'status':'REVISED' if changed else 'PASS','review_scope':review,'narrow_screen':'fits column' if is_compact else 'existing responsive raster or contained wide-diagram pane; no portrait conversion claimed','used_by':uses,'source_sha256':sha(ROOT/rel),'html_sha256':sha(ROOT/'docs'/rel),'source_matches_html':sha(ROOT/rel)==sha(ROOT/'docs'/rel)})
(OUT/'figure-ledger.json').write_text(json.dumps(ledger,indent=2)+'\n')
lines=['# Figure review ledger','','Status applies only to the stated scope. Retained figures were reviewed on the complete contact-sheet set; all rendered placements were checked for loading, alternative text and page containment. The eleven new compact diagrams were individually inspected and measured at desktop 1440 and phone 390; the changed communication-calibration chart was individually inspected. EPUB XHTML was checked at 768 and 390. Wide retained SVGs still require horizontal viewing.','','| Asset | Status | Narrow-screen presentation | Review |','| --- | --- | --- | --- |']
for r in ledger:lines.append(f"| `{r['asset']}` | {r['status']} | {r['narrow_screen']} | {r['review_scope']} |")
(OUT/'figure-ledger.md').write_text('\n'.join(lines)+'\n')
reports={
 'source_qa':ROOT/'qa-report.json',
 'html_figures':ROOT/'audits/rendered-figure-qa.json',
 'epub_figures':ROOT/'audits/rendered-epub-figure-qa.json',
 'html_links':OUT/'html-links.json',
 'reading_route':OUT/'reading-route-qa.json',
}
result={'artifacts':{},'sources':{p:sha(ROOT/p) for p in paths},'figure_assets':len(assets),'figure_placements':sum(map(len,assets.values())),'figure_source_html_match':all(r['source_matches_html'] for r in ledger),'checks':{name:json.loads(p.read_text()) for name,p in reports.items()},'epub_qa_report':(ROOT/'EPUB_QA_REPORT.md').read_text(),'scope':'Local edition only. Extracted EPUB rendering in Chromium is not a native-reader compatibility guarantee.'}
for p in ['docs/index.html','docs/Decision-in-the-Making.epub','_epub/Decision-in-the-Making.epub','scripts/build_reading_figures.py','scripts/sync_references.py','_quarto-html.yml','_quarto-epub.yml','quarto-custom.scss','epub-custom.css']:
 f=ROOT/p;result['artifacts'][p]={'sha256':sha(f),'bytes':f.stat().st_size}
(OUT/'final-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print('Recorded',len(assets),'assets;',sum(map(len,assets.values())),'placements; source/output match:',result['figure_source_html_match'])
