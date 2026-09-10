from pathlib import Path
import sys,re,json,zipfile,subprocess
sys.path.insert(0,'scripts');import sync_references as s;import qa_quarto_book as q
def same_work(a,b):
 da=re.search(r'https?://doi.org/([^\s]+)',a);db=re.search(r'https?://doi.org/([^\s]+)',b)
 return bool((da and db and da.group(1).rstrip('.')==db.group(1).rstrip('.')) or (q.reference_title_year_key(a) and q.reference_title_year_key(a)==q.reference_title_year_key(b)))
B=Path('audits/reference-retention-20260910');z=zipfile.ZipFile('audits/book-revision-20260910/before.zip')
def revised_text(path):
 return subprocess.check_output(['git','show','2b5a22f:'+str(path)],text=True)
oldmaster=z.read('references.qmd').decode();newmaster=revised_text('references.qmd')
old={s.reference_key(x):x for x in s.REFERENCE_BLOCK.findall(oldmaster)};new={s.reference_key(x):x for x in s.REFERENCE_BLOCK.findall(newmaster)}
unold={k:v for k,v in old.items() if k not in new};unnew={k:v for k,v in new.items() if k not in old};changed=[]
for k,v in list(unold.items()):
 hits=[(nk,nv) for nk,nv in unnew.items() if same_work(v,nv)]
 if len(hits)==1:
  nk,nv=hits[0];changed.append({'before':v,'after':nv});del unold[k];del unnew[nk]
rows=[];dropped=[]
for p in s.canonical_reference_sources():
 rel=str(p.relative_to(Path.cwd()));oldtext=z.read(rel).decode();newtext=revised_text(rel);oldrefs={s.reference_key(x):x for x in s.REFERENCE_BLOCK.findall(oldtext)};newrefs={s.reference_key(x):x for x in s.REFERENCE_BLOCK.findall(newtext)}
 for k,v in oldrefs.items():
  if k not in newrefs:
   corrected=next((x for x in newrefs.values() if same_work(x,v)),None)
   rows.append({'source':rel,'reference':v,'status':'updated record' if corrected else ('removed locally, retained elsewhere' if k in new else 'removed from book bibliography'),'replacement':corrected})
 oldbody=q.strip_reference_tail(oldtext);newbody=q.strip_reference_tail(newtext)
 toks=lambda t:{(q.normalize_token(a),y):(a,y,raw) for a,y,raw in q.likely_citation_tokens(t)}
 ot=toks(oldbody);nt=toks(newbody)
 for k,(a,y,raw) in ot.items():
  if k not in nt:
   passages=[p for p in oldbody.split('\n\n') if a in p and y in p]
   matches=[v for v in oldrefs.values() if k in q.reference_author_years(v)]
   dropped.append({'source':rel,'author':a,'year':y,'citation':raw,'references':matches,'old_passages':passages,'author_still_in_new_body':a.casefold() in newbody.casefold()})
out={'baseline':'d0a1f75','revised':'2b5a22f','counts':{'before':len(old),'after':len(new),'removed':len(unold),'added':len(unnew),'updated_records':len(changed)},'removed':[{'reference':v,'old_sources':[r['source'] for r in rows if r['reference']==v]} for v in unold.values()],'added':list(unnew.values()),'updated':changed,'local_reference_changes':rows,'disappeared_citation_candidates':dropped}
for r in rows:
 if r['status']=='removed locally, retained elsewhere':
  r['current_reference_homes']=[str(p.relative_to(Path.cwd())) for p in s.canonical_reference_sources() if any(s.reference_key(v)==s.reference_key(r['reference']) for v in s.REFERENCE_BLOCK.findall(revised_text(p.relative_to(Path.cwd()))))]
(B/'reference-retention-diff.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(out['counts']);print('LOCAL CHANGES');print('\n'.join(r['source'].split('/')[-1][:3]+' '+r['status']+': '+r['reference'][:115] for r in rows));print('DISAPPEARED CITATION CANDIDATES',len(dropped));print('\n'.join(str(i)+' '+r['source'].split('/')[-1][:3]+' '+r['citation'][:110]+' retained name='+str(r['author_still_in_new_body']) for i,r in enumerate(dropped)))
