#!/usr/bin/env python3
"""One-time exact repair driven by the first rendered HTML audit; no prose rewrite."""
from pathlib import Path
import json,re,subprocess,hashlib
root=Path(__file__).resolve().parents[2]
audit=Path(__file__).resolve().parent
if (audit/'cross-format-title-link-repairs.json').exists():
 raise SystemExit('One-time migration already applied and superseded. Use read-only final-output audits; do not rerun this historical repair.')
broken=json.loads((audit/'final-html-link-audit.json').read_text())['missing_or_invalid_links']
changes=[]
before={}

def read(path):
 p=root/path
 if path not in before:before[path]=p.read_text()
 return p.read_text()
def write(path,text):
 (root/path).write_text(text)
def plain(text):
 return subprocess.run(['/usr/local/bin/quarto','pandoc','--from','markdown','--to','plain'],input=text,text=True,capture_output=True,check=True).stdout

for issue in broken:
 if issue['source']=='concept-index.html' or issue['url'].startswith('#'):
  continue
 path=issue['source'].replace('.html','.qmd');fragment=issue['fragment'];s=read(path)
 pattern=r'([^)\s]+\.qmd)#'+re.escape(fragment)+r'(?=\))'
 matches=list(re.finditer(pattern,s))
 assert matches,(path,fragment)
 s,n=re.subn(pattern,r'\1',s)
 write(path,s)
 changes.append({'path':path,'type':'remove_unnecessary_title_fragment','fragment':fragment,'links_changed':n})

callouts=[
('chapters/04-the-predictive-mind-perception-is-inference.qmd','## Research Lens: from predictive processing to active inference','research-lens-from-predictive-processing-to-active-inference'),
('chapters/06-valuation-how-options-become-worth-choosing.qmd','## How value works is not why a value system exists','how-value-works-is-not-why-a-value-system-exists'),
('chapters/06-valuation-how-options-become-worth-choosing.qmd','## Research note: are needs a hierarchy?','research-note-are-needs-a-hierarchy'),
('chapters/13-accessibility-familiarity-and-ease.qmd','## Evidence Boundary: concealed cues are not mind control','evidence-boundary-concealed-cues-are-not-mind-control'),
('chapters/27-markets-mispricing-and-bubbles.qmd','## Advanced research track: auditing an event study','advanced-research-track-auditing-an-event-study'),
('chapters/27-markets-mispricing-and-bubbles.qmd','### Research Lens: five patterns, five open diagnoses','research-lens-five-patterns-five-open-diagnoses'),
]
for path,heading,anchor in callouts:
 s=read(path);pattern=r'(^::: \{[^\n]+)(\}\n)'+re.escape(heading)+r'(?=\n)'
 matches=list(re.finditer(pattern,s,re.M));assert len(matches)==1,(path,anchor)
 s=re.sub(pattern,lambda m:m.group(1)+' #'+anchor+m.group(2)+heading+' {#'+anchor+'-title}',s,count=1,flags=re.M)
 write(path,s);changes.append({'path':path,'type':'surviving_callout_div_id','anchor':anchor,'title_id':anchor+'-title'})

path='how-to-use-this-book.qmd';s=read(path)
old='[Appendix C](appendices/appendix-c-portable-course-tools.qmd)';new='[Appendix C](appendices/appendix-c-portable-course-tools.qmd#ethical-audit)';assert old in s;s=s.replace(old,new,1)
old='| Start here |';new='| Suggested route |';assert old in s;s=s.replace(old,new,1)
write(path,s);changes.extend([{'path':path,'type':'explicit_epub_destination','before':old,'anchor':'ethical-audit'},{'path':path,'type':'table_header','before':'Start here','after':'Suggested route','authorized_by':'root'}])
checks=[]
for path,original in before.items():
 current=(root/path).read_text()
 a=plain(original);b=plain(current)
 if path=='how-to-use-this-book.qmd':a=a.replace('Start here','Suggested route')
 # Plain table column padding can differ after the authorized header rename.
 assert re.sub(r'\s+',' ',a)==re.sub(r'\s+',' ',b),path
 checks.append({'path':path,'visible_text_preserved_except_authorized_header':True,'sha256_before':hashlib.sha256(original.encode()).hexdigest(),'sha256_after':hashlib.sha256(current.encode()).hexdigest()})
(audit/'rendered-fragment-repairs.json').write_text(json.dumps({'changes':changes,'checks':checks,'first_html_audit_issues':len(broken),'build_status':'sources ready; final HTML and EPUB rerender required'},indent=2)+'\n')
print(json.dumps({'changed_files':len(before),'removed_title_fragments':sum(c.get('links_changed',0) for c in changes),'restored_callout_anchors':len(callouts),'source_ready':True}))
