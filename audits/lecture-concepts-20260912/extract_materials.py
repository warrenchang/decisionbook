"""Read-only teaching-source extraction; full text stays in a temporary directory."""
from pathlib import Path
import collections, hashlib, json, re, zipfile, posixpath
import xml.etree.ElementTree as ET
from pypdf import PdfReader

OUT=Path('/private/tmp/decision-book-lecture-concepts-20260912')
AUDIT=Path(__file__).resolve().parent
BASE=Path('/Users/ra25fi/Library/CloudStorage')
ROOTS={}
for host in ['Aalborg','Syddansk']:
    teach=BASE/f'OneDrive-{host}Universitet'/'Teaching'
    ROOTS[f'BE-{host}']=teach/'Behavioral Economics/01_Teaching_Materials/Lecture Notes'
    ROOTS[f'DPN-{host}']=teach/'Decision, Persuasion, and Negotiation/Notes'
A='{http://schemas.openxmlformats.org/drawingml/2006/main}'
P='{http://schemas.openxmlformats.org/presentationml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
REL='{http://schemas.openxmlformats.org/package/2006/relationships}'
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def pptx(raw):
    import io
    pages=[]
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        prs=ET.fromstring(z.read('ppt/presentation.xml'))
        rels={r.get('Id'):r.get('Target') for r in ET.fromstring(z.read('ppt/_rels/presentation.xml.rels'))}
        for i,item in enumerate(prs.find(P+'sldIdLst'),1):
            target=rels[item.get(R+'id')]
            name=posixpath.normpath(posixpath.join('ppt',target)) if not target.startswith('/') else target[1:]
            slide=ET.fromstring(z.read(name))
            texts=[];titles=[]
            for sp in slide.iter(P+'sp'):
                lines=[''.join(t.text or '' for t in p.iter(A+'t')) for p in sp.iter(A+'p')]
                lines=[s for s in lines if s.strip()]
                texts.extend(lines)
                ph=sp.find('.//'+P+'ph')
                if ph is not None and ph.get('type') in ['title','ctrTitle']:titles.extend(lines)
            for frame in slide.iter(A+'tbl'):
                texts.extend(''.join(t.text or '' for t in p.iter(A+'t')) for p in frame.iter(A+'p'))
            notes=[]
            sr=posixpath.join(posixpath.dirname(name),'_rels',posixpath.basename(name)+'.rels')
            if sr in z.namelist():
                for rel in ET.fromstring(z.read(sr)):
                    if rel.get('Type','').endswith('/notesSlide'):
                        nn=posixpath.normpath(posixpath.join(posixpath.dirname(name),rel.get('Target')))
                        note=ET.fromstring(z.read(nn))
                        for sp in note.iter(P+'sp'):
                            ph=sp.find('.//'+P+'ph')
                            if ph is not None and ph.get('type') in ['sldNum','hdr','ftr','dt']:continue
                            notes.extend(''.join(t.text or '' for t in p.iter(A+'t')) for p in sp.iter(A+'p'))
            pages.append({'page':i,'title':' | '.join(titles),'hidden':slide.get('show')=='0','text':'\n'.join(texts),'notes':'\n'.join(notes)})
    return pages

def extract(path,raw):
    if path.suffix.lower()=='.pptx':return pptx(raw)
    if path.suffix.lower()=='.pdf':
        reader=PdfReader(path)
        return [{'page':i,'title':'','text':p.extract_text() or '','notes':''} for i,p in enumerate(reader.pages,1)]
    if path.suffix.lower()=='.docx':
        with zipfile.ZipFile(path) as z:doc=ET.fromstring(z.read('word/document.xml'))
        return [{'page':None,'title':'','text':'\n'.join(''.join(t.text or '' for t in p.iter(W+'t')) for p in doc.iter(W+'p')),'notes':''}]
    return [{'page':None,'title':'','text':raw.decode(errors='replace'),'notes':''}]

def main():
    OUT.mkdir(exist_ok=True)
    inventory=[];unique={};errors=[]
    for label,root in ROOTS.items():
        for path in sorted(root.rglob('*')):
            if not path.is_file() or path.suffix.lower() not in ['.pptx','.pdf','.docx','.tex']:continue
            rel=path.relative_to(root).as_posix()
            if path.name.startswith('~$') or any(p.lower()=='exams' for p in path.parts):continue
            # Reading-library articles are evidence leads, not additional taught topics.
            if 'Readings/' in rel and path.suffix.lower()=='.pdf':continue
            raw=path.read_bytes();sha=hashlib.sha256(raw).hexdigest()
            row={'source_root':label,'relative_path':rel,'sha256':sha,'bytes':len(raw)}
            inventory.append(row)
            if sha in unique:
                row['duplicate_of']=unique[sha]['source'];continue
            source=f'{label}/{rel}'
            try:
                pages=extract(path,raw)
                content='\n'.join(p['text']+'\n'+p['notes'] for p in pages)
                item={'source':source,'sha256':sha,'path':str(path),'pages':pages,'words':len(content.split())}
                unique[sha]=item
                row.update({'pages':len(pages),'words':item['words'],'text_sha256':hashlib.sha256(content.encode()).hexdigest()})
            except Exception as e:
                row['error']=str(e);errors.append({'source':source,'error':str(e)})
    (OUT/'extracted.json').write_text(json.dumps(list(unique.values()),ensure_ascii=False))
    (AUDIT/'source-inventory.json').write_text(json.dumps({'roots':{k:str(v) for k,v in ROOTS.items()},'files':inventory,'errors':errors},indent=2,ensure_ascii=False)+'\n')
    stats={'source_paths':len(inventory),'unique_files':len(unique),'exact_duplicates':sum('duplicate_of' in r for r in inventory),'pages_or_slides':sum(len(x['pages']) for x in unique.values()),'extracted_words':sum(x['words'] for x in unique.values()),'errors':errors}
    print(json.dumps(stats,ensure_ascii=False,indent=2),flush=True)

if __name__=='__main__':main()
