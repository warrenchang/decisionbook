"""Verify personal story content and note-box labels in both book editions."""
from pathlib import Path
from html.parser import HTMLParser
import json,re,zipfile
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
class Text(HTMLParser):
    def __init__(self): super().__init__(); self.parts=[]
    def handle_data(self,data): self.parts.append(data)
def plain(s):
    p=Text();p.feed(s);return re.sub(r'\s+',' ',' '.join(p.parts)).strip()
def norm(s):return re.sub(r'[^a-z0-9]','',s.casefold())
expected={
 '04':['From my experience: an urge at the toilet door'],
 '08':['From my experience: my daughter learning to count'],
 '12':['From my experience: a fall becomes a somersault','From my experience: leaving the amusement park'],
 '17':['From my experience: a holiday that became €300 more expensive'],
 '21':['From my experience: replacing cola with sparkling water'],
 '40':['From my experience: one egg or two?'],
}
with zipfile.ZipFile(ROOT/'docs/Decision-in-the-Making.epub') as z:
    epub_documents=[z.read(n).decode() for n in z.namelist() if n.endswith('.xhtml') and '/text/' in n]
    epub_text=norm(' '.join(plain(s) for s in epub_documents))
    epub_boxes=[]
    for s in epub_documents:
        root=ET.fromstring(s)
        epub_boxes.extend(el for el in root.iter() if 'personal-example' in el.get('class','').split())
assert len(epub_boxes)==7, len(epub_boxes)
for box in epub_boxes:
    text=' '.join(''.join(box.itertext()).split())
    assert 'From my experience:' in text[:120],text[:150]
checks=[]
for ch,titles in expected.items():
    source=next((ROOT/'chapters').glob(ch+'-*.qmd'))
    html=(ROOT/'docs/chapters'/source.with_suffix('.html').name).read_text()
    rendered=norm(plain(html))
    for title in titles:
        assert norm(title) in rendered,(ch,'HTML',title)
        assert norm(title) in epub_text,(ch,'EPUB',title)
        checks.append({'chapter':ch,'title':title})
search=norm((ROOT/'docs/search.json').read_text())
for phrase in ['Sometimes she even reminds me that the five minutes are up and we should leave.',
               'Replacing it with sparkling water has also worked well for me',
               'doing it in a restaurant would feel awkward']:
    assert norm(phrase) in epub_text,phrase
    assert norm(phrase) in search,phrase
assert norm('Would you like to leave now or in ten minutes?') not in epub_text
assert norm('A personal illustration: from a fall to a somersault') not in epub_text
(OUT/'edition-qa.json').write_text(json.dumps({'status':'PASS','stories':checks,'html_epub_search':'PASS'},ensure_ascii=False,indent=2)+'\n')
print('PASS: all seven personal-story labels and boxes in HTML/EPUB; new stories indexed; old wording removed.')
