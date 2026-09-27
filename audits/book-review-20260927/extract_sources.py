"""Read-only inventory of lecture sources; extract text, notes, and visual pointers.

Run with the bundled Python (pypdf installed). Extracted text is scratch data;
the manifest and this extractor preserve provenance without republishing decks.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json
import posixpath
import re
import zipfile
import xml.etree.ElementTree as ET
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
OUT = Path('/private/tmp/decisionbook-review-20260927-sources')
TEACHING = Path('/Users/ra25fi/Library/CloudStorage/OneDrive-SyddanskUniversitet/Teaching')
ROOTS = {
    'BE': TEACHING / 'Behavioral Economics/Lecture Notes',
    'DPN': TEACHING / 'Decision, Persuasion, and Negotiation/Notes',
}
NS = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
      'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
BE_INCLUDE = {'Archives', 'BE2026', 'DPN2026', 'Lecture Notes PDF', 'PDF topics 2026', 'Readings'}

def rels(z, owner):
    name = posixpath.join(posixpath.dirname(owner), '_rels', posixpath.basename(owner)+'.rels')
    if name not in z.namelist(): return {}
    return {r.get('Id'): dict(r.attrib) for r in ET.fromstring(z.read(name))}

def target(owner, dest):
    return posixpath.normpath(posixpath.join(posixpath.dirname(owner), dest)).lstrip('/') if not dest.startswith('/') else dest.lstrip('/')

def paragraphs(root, namespace='a'):
    return [''.join(p.itertext()) if namespace=='plain' else ''.join(t.text or '' for t in p.findall('.//'+namespace+':t', NS))
            for p in root.findall('.//'+namespace+':p', NS)]

def pptx(path):
    pages=[]
    with zipfile.ZipFile(path) as z:
        owner='ppt/presentation.xml'
        pr=rels(z,owner)
        for n,sid in enumerate(ET.fromstring(z.read(owner)).findall('.//p:sldId', NS),1):
            s=target(owner,pr[sid.get('{'+NS['r']+'}id')]['Target'])
            root=ET.fromstring(z.read(s)); sr=rels(z,s)
            notes=[]; visual=[]
            for relationship in sr.values():
                typ=relationship['Type'].rsplit('/',1)[-1]
                dest=target(s,relationship['Target']) if relationship.get('TargetMode')!='External' else relationship['Target']
                if typ=='notesSlide' and dest in z.namelist():
                    nr=ET.fromstring(z.read(dest))
                    for shape in nr.findall('.//p:sp',NS):
                        placeholder=shape.find('.//p:ph',NS)
                        if placeholder is not None and placeholder.get('type') in ('sldNum','hdr','ftr','dt'):continue
                        notes.extend(paragraphs(shape))
                if typ in ('image','chart','diagramData','video','audio'):visual.append({'kind':typ,'target':dest})
            text='\n'.join(p for p in paragraphs(root) if p.strip())
            pages.append({'page':n,'xml':s,'hidden':root.get('show')=='0',
                          'text':text,'notes':'\n'.join(p for p in notes if p.strip()),
                          'visual_assets':visual,'visual_review_flag':bool(visual) and len(text.split())<35})
    return pages

def extract(path):
    if path.suffix.lower()=='.pptx':return pptx(path)
    if path.suffix.lower()=='.pdf':
        pages=[]
        for i,p in enumerate(PdfReader(path).pages):
            text=p.extract_text() or ''
            pages.append({'page':i+1,'text':text,'notes':'',
                          'visual_review_flag':len(text.split())<35})
        return pages
    with zipfile.ZipFile(path) as z:
        text='\n'.join(paragraphs(ET.fromstring(z.read('word/document.xml')),'w'))
        return [{'page':1,'text':text,'notes':'','visual_assets':[],'visual_review_flag':False}]

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    manifest=[]; seen={}
    for group,root in ROOTS.items():
        for path in sorted(root.rglob('*')):
            if not path.is_file() or path.suffix.lower() not in ('.pptx','.pdf','.docx') or path.name.startswith('~$'):continue
            rel=path.relative_to(root)
            if group=='BE' and len(rel.parts)>1 and rel.parts[0] not in BE_INCLUDE:continue
            digest=hashlib.sha256(path.read_bytes()).hexdigest()
            sid=group+'-'+hashlib.sha256(str(rel).encode()).hexdigest()[:12]
            row={'id':sid,'group':group,'relative_path':str(rel),'source_path':str(path),
                 'sha256':digest,'size_bytes':path.stat().st_size,'format':path.suffix.lower()[1:]}
            if digest in seen:
                row.update({'duplicate_of':seen[digest]['id'],'extraction':seen[digest]['extraction'],
                            'text_path':seen[digest]['text_path'],'units':seen[digest]['units']})
            else:
                try:
                    pages=extract(path)
                    dest=OUT/(sid+'.json'); dest.write_text(json.dumps(pages,ensure_ascii=False,indent=2))
                    txt=OUT/(sid+'.txt')
                    txt.write_text('\n\n'.join(f"### {group}/{rel} — {p['page']}\n{p['text']}\nSPEAKER NOTES:\n{p['notes']}" for p in pages))
                    row.update({'extraction':str(dest),'text_path':str(txt),'units':len(pages),
                                'notes_units':sum(bool(p['notes'].strip()) for p in pages),
                                'visual_review_units':[p['page'] for p in pages if p['visual_review_flag']]})
                    seen[digest]=row
                except Exception as exc:row['error']=repr(exc)
            manifest.append(row)
    (HERE/'source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'files':len(manifest),'formats':dict(Counter(r['format'] for r in manifest)),
                      'exact_duplicates':sum('duplicate_of' in r for r in manifest),
                      'unique_units':sum(r.get('units',0) for r in manifest if 'duplicate_of' not in r),
                      'errors':[r for r in manifest if 'error' in r],'scratch':str(OUT)},ensure_ascii=False))

if __name__=='__main__':main()
