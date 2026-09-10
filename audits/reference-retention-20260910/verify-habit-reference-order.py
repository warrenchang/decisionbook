from pathlib import Path
from html.parser import HTMLParser
import json,re,sys,subprocess,zipfile,xml.etree.ElementTree as ET,unicodedata
sys.path.insert(0,'scripts');import sync_references as s
b=Path('audits/reference-retention-20260910');p=Path('chapters/21-habits-wanting-and-self-control.qmd');new=p.read_text();old=subprocess.check_output(['git','show','HEAD:'+str(p)],text=True);baseline=subprocess.check_output(['git','show','d0a1f75:'+str(p)],text=True)
refs=s.REFERENCE_BLOCK.findall(new)
def author(v):return re.split(r'\(\d{4}\)',v,maxsplit=1)[0].strip()
def key(v):
 v=unicodedata.normalize('NFKD',v).casefold();return re.sub(r'[^a-z0-9]+',' ',''.join(c for c in v if not unicodedata.combining(c))).strip()
class RefParser(HTMLParser):
 def __init__(self):super().__init__();self.depth=0;self.buf=[];self.refs=[]
 def handle_starttag(self,tag,attrs):
  if self.depth:
   if tag=='div':self.depth+=1
  elif tag=='div' and 'reference' in dict(attrs).get('class','').split():self.depth=1;self.buf=[]
 def handle_endtag(self,tag):
  if self.depth and tag=='div':
   self.depth-=1
   if self.depth==0:self.refs.append(' '.join(''.join(self.buf).split()))
 def handle_data(self,data):
  if self.depth:self.buf.append(data)
h=RefParser();h.feed(Path('docs/chapters/21-habits-wanting-and-self-control.html').read_text())
with zipfile.ZipFile('docs/Decision-in-the-Making.epub') as z:
 files=[n for n in z.namelist() if n.endswith('.xhtml') and 'id="fig-habit-loop"' in z.read(n).decode()];assert len(files)==1
 root=ET.fromstring(z.read(files[0]));er=[' '.join(''.join(e.itertext()).split()) for e in root.iter() if 'reference' in e.attrib.get('class','').split()]
checks={'source_entries':len(refs),'html_entries':len(h.refs),'epub_entries':len(er),'entries_unchanged_from_pushed_revision':sorted(refs)==sorted(s.REFERENCE_BLOCK.findall(old)),'entries_unchanged_from_before_book_revision':sorted(refs)==sorted(s.REFERENCE_BLOCK.findall(baseline)),'chapter_body_unchanged':new.split('## References cited in this chapter')[0]==old.split('## References cited in this chapter')[0],'source_alphabetical':refs==sorted(refs,key=key),'html_matches_source_order':[key(author(v)) for v in h.refs]==[key(author(v)) for v in refs],'epub_matches_source_order':[key(author(v)) for v in er]==[key(author(v)) for v in refs],'authors_in_order':[author(v) for v in refs],'epub_document':files[0]}
assert all(v for v in checks.values()) and checks['html_entries']==checks['epub_entries']==checks['source_entries']==12
(b/'habit-reference-order-verification.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False)+'\n');print(json.dumps(checks,indent=2,ensure_ascii=False))
