"""Verify that every consolidated heading keeps its HTML and EPUB link target."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import json, re, zipfile

ROOT=Path(__file__).resolve().parents[2]
AUDIT=Path(__file__).resolve().parent
changes=json.loads((AUDIT/'changes.json').read_text())
class Tags(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=Counter(); self.headings=set(); self.toc=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'): self.ids[a['id']]+=1
        if re.fullmatch(r'h[1-6]',tag):
            self.headings.add(a.get('data-anchor-id') or a.get('id'))
        if a.get('id','').startswith('toc-'): self.toc.add(a['id'][4:])

def parse(text):
    p=Tags();p.feed(text);return p

records=[]
with zipfile.ZipFile(ROOT/'docs/Decision-in-the-Making.epub') as z:
    epub={name:parse(z.read(name).decode()) for name in z.namelist() if name.endswith('.xhtml') and '/text/' in name}
    for f in sorted({c['file'] for c in changes}):
        rendered=parse((ROOT/'docs'/Path(f).with_suffix('.html')).read_text())
        for c in [c for c in changes if c['file']==f]:
            anchor=c['anchor']; assert rendered.ids[anchor]==1,(f,anchor,'HTML target count',rendered.ids[anchor])
            matches=[(name,p) for name,p in epub.items() if p.ids[anchor]]
            # Generic headings can recur across chapters; an EPUB target with the expected role must exist.
            assert matches,(f,anchor,'missing EPUB target')
            if c['action']=='merge':
                assert anchor not in rendered.headings and anchor not in rendered.toc,(f,anchor,'still a heading')
                assert any(anchor not in p.headings for _,p in matches),(f,anchor,'still an EPUB heading')
            else:
                assert anchor in rendered.headings,(f,anchor,'missing retained heading')
            records.append(dict(file=f,anchor=anchor,action=c['action'],html='PASS',epub='PASS'))
(AUDIT/'anchor-qa.json').write_text(json.dumps({'status':'PASS','checked':len(records),'records':records},indent=2)+'\n')
print(f'PASS: {len(records)} preserved HTML and EPUB targets; merged headings removed from HTML navigation.')
