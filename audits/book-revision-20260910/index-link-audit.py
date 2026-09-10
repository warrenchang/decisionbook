from pathlib import Path
import json,re,subprocess
root=Path.cwd();files=[Path('concept-index.qmd'),Path('appendices/appendix-d-index-of-major-course-examples.qmd')];links=[]
for p in files:
 for m in re.finditer(r'\[([^\]]*)\]\(([^)]+)\)',p.read_text()):
  label,url=m.groups()
  if url.startswith(('http:','https:','mailto:')):continue
  target,_,anchor=url.partition('#');dest=(p.parent/target).resolve() if target else p.resolve()
  if dest.suffix!='.qmd':continue
  links.append({'source':str(p),'label':label,'target':str(dest.relative_to(root)),'anchor':anchor,'url':url})
ids={}
for f in sorted({x['target'] for x in links}):
 p=Path(f)
 if not p.exists():continue
 ast=json.loads(subprocess.run(['quarto','pandoc','--from','markdown','--to','json'],input=p.read_text(),text=True,stdout=subprocess.PIPE,check=True).stdout);got=set()
 def walk(x):
  if isinstance(x,dict):
   for v in x.values():walk(v)
  elif isinstance(x,list):
   if len(x)==3 and isinstance(x[0],str) and isinstance(x[1],list) and isinstance(x[2],list) and x[0]:got.add(x[0])
   for v in x:walk(v)
 walk(ast);ids[f]=got
bad=[x for x in links if x['target'] not in ids or (x['anchor'] and x['anchor'] not in ids[x['target']])]
Path('audits/book-revision-20260910/index-link-audit.json').write_text(json.dumps({'local_links':len(links),'targets':len(ids),'broken':bad},indent=2)+'\n')
Path('/private/tmp/index-target-ids.json').write_text(json.dumps({k:sorted(v) for k,v in ids.items()},indent=2))
print(json.dumps(bad,indent=2));print('local links',len(links),'targets',len(ids),'broken',len(bad))
