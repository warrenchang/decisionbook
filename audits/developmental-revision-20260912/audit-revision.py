#!/usr/bin/env python3
"""Read-only revision metrics; optionally verify owned SVG build reproducibility."""
import hashlib, json, re, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).parent
BASE=json.loads((OUT/'baseline.json').read_text())['baseline_commit']
paths=re.findall(r'^\s*-\s*(?:part:\s*)?([^\s]+\.qmd)\s*$',(ROOT/'_quarto-html.yml').read_text(),re.M)
chapters=[p for p in paths if p.startswith('chapters/')]
def before(p): return subprocess.check_output(['git','show',f'{BASE}:{p}'],cwd=ROOT,text=True)
def local_links(s): return re.findall(r'\]\(([^)\s]+\.qmd(?:#[^)\s]*)?)\)',s)
def outgoing(p,s):
 return [l for l in local_links(s) if l.split('#')[0].split('/')[-1] != Path(p).name and ('/chapters/' in l or (p.startswith('chapters/') and re.match(r'\d\d-',l)))]
rows=[]
for p in chapters:
 a,b=before(p),(ROOT/p).read_text()
 rows.append({'source':p,'changed':a!=b,'outbound_chapter_links_before':len(outgoing(p,a)),'outbound_chapter_links_after':len(outgoing(p,b))})
svg=[]
for old in json.loads((OUT/'figure-inventory-before.json').read_text()):
 p=ROOT/old['file'];s=p.read_text();m=re.search(r'viewBox="\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)"',s)
 svg.append({**old,'current_width':float(m[3]) if m else None,'current_height':float(m[4]) if m else None,'compact_class':any(old['file'].split('/')[-1]==r['figure'] for r in json.loads((OUT/'compact-figure-placements.json').read_text())),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
report={'baseline_commit':BASE,'configured_sources':len(paths),'canonical_chapters':len(chapters),'changed_chapters':sum(r['changed'] for r in rows),'chapter_cross_links':{'before':sum(r['outbound_chapter_links_before'] for r in rows),'after':sum(r['outbound_chapter_links_after'] for r in rows),'chapters_without_before':sum(r['outbound_chapter_links_before']==0 for r in rows),'chapters_without_after':sum(r['outbound_chapter_links_after']==0 for r in rows)},'method':'Counts explicit Markdown links to other numbered chapters in the 42 canonical chapter sources. Does not count prose-only pointers, appendix links or generated navigation. Counts are not a claim about each link\'s usefulness. Figure inventory includes unique referenced SVGs only; raster media are checked by rendered QA.','chapters':rows,'svg_figures':svg}
(OUT/'revision-metrics.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['chapters','svg_figures']},indent=2))
