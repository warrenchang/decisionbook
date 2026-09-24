from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as E
import json,hashlib,re
ROOT=Path('/Users/ra25fi/Library/CloudStorage/OneDrive-AalborgUniversitet/Teaching/Decision, Persuasion, and Negotiation/Notes')
BE=Path('/Users/ra25fi/Library/CloudStorage/OneDrive-AalborgUniversitet/Teaching/Behavioral Economics/01_Teaching_Materials/Lecture Notes/DPN2026')
OUT=Path('/private/tmp/decision-social-influence-20260924/source-extracts')
OUT.mkdir(parents=True,exist_ok=True)
ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main','p':'http://schemas.openxmlformats.org/presentationml/2006/main'}
files=list(ROOT.glob('*.pptx'))+list(BE.glob('*.pptx'))
rows=[]
for f in files:
 b=f.read_bytes(); row={'path':str(f),'file':f.name,'sha256':hashlib.sha256(b).hexdigest(),'mtime':f.stat().st_mtime,'bytes':len(b)}
 with ZipFile(f) as z:
  slides=[]
  rels={r.attrib['Id']:r.attrib['Target'] for r in E.fromstring(z.read('ppt/_rels/presentation.xml.rels'))}
  order=[rels[e.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']] for e in E.fromstring(z.read('ppt/presentation.xml')).findall('.//p:sldId',ns)]
  for position,target in enumerate(order,1):
   name='ppt/'+target.lstrip('/') if not target.startswith('/ppt/') else target.lstrip('/')
   e=E.fromstring(z.read(name)); num=int(re.search(r'(\d+)\.xml',name).group(1))
   paras=[''.join(t.itertext()) for p in e.findall('.//a:p',ns) for t in [p] ]
   # Filter to a:t text only to omit XML numbers etc.
   paras=[''.join(t.text or '' for t in p.findall('.//a:t',ns)) for p in e.findall('.//a:p',ns)]
   note_name=f'ppt/notesSlides/notesSlide{num}.xml'; notes=[]
   rel=f'ppt/slides/_rels/slide{num}.xml.rels'
   if rel in z.namelist():
    for r in E.fromstring(z.read(rel)):
     if r.attrib.get('Type','').endswith('/notesSlide'): note_name='ppt/'+r.attrib['Target'].lstrip('../')
   if note_name in z.namelist():
    ne=E.fromstring(z.read(note_name)); notes=[''.join(t.text or '' for t in p.findall('.//a:t',ns)) for p in ne.findall('.//a:p',ns)]
   slides.append({'slide':position,'slide_part_number':num,'text':'\n'.join(x for x in paras if x.strip()),'notes':'\n'.join(x for x in notes if x.strip()),'images':len(e.findall('.//p:pic',ns)),'hidden':e.attrib.get('show')=='0'})
  row['slides']=slides; row['text_sha256']=hashlib.sha256(json.dumps(slides,sort_keys=True).encode()).hexdigest()
 rows.append(row)
OUT.joinpath('dpn-deck-extracts.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
for r in rows:
 if r['file'].startswith('DPN0') or r['file'] in ['03. Social Influence.pptx','04. Principles of Influence.pptx','05. Persuasion2026.pptx']:
  print(r['file'],len(r['slides']),r['sha256'][:12],r['path'])
  for s in r['slides']:
   print(s['slide'],s['text'].split('\n')[0][:110],f"[images={s['images']} notes={len(s['notes'])}]")
