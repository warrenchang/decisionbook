"""Check that deleted prose is absent from the generated editions and search index."""
from pathlib import Path
from html.parser import HTMLParser
import json,re,zipfile
ROOT=Path(__file__).resolve().parents[2];AUDIT=Path(__file__).resolve().parent
class Text(HTMLParser):
    def __init__(self):super().__init__();self.chunks=[]
    def handle_data(self,data):self.chunks.append(data)
def norm(s):return re.sub(r'[^a-z0-9]','',s.casefold())
def html_text(s):
    p=Text();p.feed(s);return norm(' '.join(p.chunks))
files=re.findall(r'^\s*-\s+(?:part:\s+)?([^\s]+\.qmd)\s*$',(ROOT/'_quarto-html.yml').read_text(),re.M)
all_sources=norm('\n'.join((ROOT/f).read_text() for f in files))
with zipfile.ZipFile(ROOT/'docs/Decision-in-the-Making.epub') as z:
    epub=''.join(html_text(z.read(n).decode()) for n in z.namelist() if n.endswith('.xhtml') and '/text/' in n)
def strings(value):
    if isinstance(value,str):yield value
    elif isinstance(value,list):
        for item in value:yield from strings(item)
    elif isinstance(value,dict):
        for item in value.values():yield from strings(item)
search=norm(' '.join(strings(json.loads((ROOT/'docs/search.json').read_text()))))
checks=[];cache={};seen=set()
for edit in json.loads((AUDIT/'edits.json').read_text()):
    pieces=edit.get('removed',[])
    if not edit['after']:pieces=pieces or [edit['before']]
    for piece in pieces:
        target=norm(piece)
        if len(target)<40 or target in all_sources or target in seen:continue
        seen.add(target);f=edit['file']
        if f not in cache:cache[f]=html_text((ROOT/'docs'/Path(f).with_suffix('.html')).read_text())
        assert target not in cache[f],('old HTML text',f,piece)
        assert target not in epub,('old EPUB text',f,piece)
        assert target not in search,('old search text',f,piece)
        checks.append({'file':f,'removed_text':piece,'html':'PASS','epub':'PASS','search':'PASS'})
(AUDIT/'rendered-removals-qa.json').write_text(json.dumps({'status':'PASS','checked':len(checks),'records':checks},ensure_ascii=False,indent=2)+'\n')
print(f'PASS: {len(checks)} deleted passages or sentences absent from HTML, EPUB, and search.')
