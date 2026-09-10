"""Verify source retention and HTML/EPUB inclusion after restoring three discussions."""
from pathlib import Path
import subprocess,re,json,zipfile,unicodedata,sys
from html.parser import HTMLParser
from xml.etree import ElementTree as ET
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'scripts'))
import sync_references as s
ROOT=Path(__file__).resolve().parents[2]
TARGETS=[('10-beliefs-that-defend-themselves','positive-illusions',3),('32-building-an-evidence-aligned-message','curiosity',1),('34-connection-and-repair-warm-honesty-makes-truth-usable','forgiveness',3)]
def norm(x):return re.sub(r'\W','',unicodedata.normalize('NFKD',x).casefold())
def orderkey(r):
 author,year=r.split('(',1)
 return (re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFKD',author.casefold())),year[:4],r.casefold())
class Nodes(HTMLParser):
 def __init__(self):super().__init__();self.notes={};self.refs=[];self.active=None;self.depth=0;self.buf=[];self.collapsed=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if self.active:
   if tag=='div':self.depth+=1
   if 'collapse' in a.get('class','').split():self.collapsed.append(self.active)
  elif tag=='div':
   if a.get('id','').startswith('research-note-'):self.active=a['id']
   elif 'reference' in a.get('class','').split():self.active='ref'
   if self.active:self.depth=1;self.buf=[]
 def handle_endtag(self,tag):
  if tag=='div' and self.active:
   self.depth-=1
   if not self.depth:
    value=' '.join(''.join(self.buf).split())
    if self.active=='ref':self.refs.append(value)
    else:self.notes[self.active]=value
    self.active=None
 def handle_data(self,data):
  if self.active:self.buf.append(data)
with zipfile.ZipFile(ROOT/'docs/Decision-in-the-Making.epub') as z:
 epub={n:z.read(n).decode() for n in z.namelist() if n.endswith('.xhtml')}
checks=[]
for stem,topic,added in TARGETS:
 path='chapters/'+stem+'.qmd';new=(ROOT/path).read_text();old=subprocess.check_output(['git','show','HEAD:'+path],cwd=ROOT,text=True)
 refs=s.REFERENCE_BLOCK.findall(new);before=s.REFERENCE_BLOCK.findall(old)
 noteid='research-note-'+topic
 h=Nodes();h.feed((ROOT/('docs/chapters/'+stem+'.html')).read_text())
 matches=[(n,t) for n,t in epub.items() if 'id="'+noteid+'"' in t];assert len(matches)==1
 e=Nodes();e.feed(matches[0][1])
 source_note=re.search(r'::: \{#'+noteid+r'[^\n]+\}\n(.*?)\n:::',new,re.S).group(1)
 # Every prose paragraph in the authored note must survive both renderings.
 paragraphs=[p for p in source_note.split('\n\n') if p and not p.startswith('#')]
 c={'chapter':path,'note_id':noteid,'epub_document':matches[0][0],'added_references':len(refs)-len(before),'all_previous_references_preserved':set(before)<=set(refs),'source_references_alphabetical':refs==sorted(refs,key=orderkey),'html_references_match_source':[norm(r) for r in refs]==[norm(r) for r in h.refs],'epub_references_match_source':[norm(r) for r in refs]==[norm(r) for r in e.refs],'note_prose_present_in_html':all(norm(p) in norm(h.notes[noteid]) for p in paragraphs),'note_prose_present_in_epub':all(norm(p) in norm(e.notes[noteid]) for p in paragraphs),'html_note_collapsible':noteid in h.collapsed}
 assert c['added_references']==added,c
 assert all(v for k,v in c.items() if isinstance(v,bool)),c
 checks.append(c)
report={'baseline_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'master_references':len(s.chapter_references()),'checks':checks,'passed':True}
assert report['master_references']==805
Path(__file__).with_name('verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
