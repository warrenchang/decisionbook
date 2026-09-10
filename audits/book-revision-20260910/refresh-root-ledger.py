from pathlib import Path
import json,re,hashlib,xml.etree.ElementTree as ET
base=Path('audits/book-revision-20260910');inv=json.loads((base/'inventory.json').read_text())
changes={
'index.qmd':['Developed one imagined hiring committee through the preface.','Separated predicting, valuing, and learning before introducing social extensions.','Removed repeated conceptual catalogues and ethical summaries; closed at the opening vote.'],
'how-to-use-this-book.qmd':['Replaced author-facing structural instructions with practical reading guidance.','Explained optional notes and the new part reading maps; retained routes and stable term definitions.'],
'how-to-read-evidence.qmd':['Used an imagined training claim to explain comparison, measurement, size, uncertainty, and transport.','Consolidated repeated cautions into a six-question evidence audit.'],
'about.qmd':['Replaced the opening subject catalogue with the practical purpose of the book.','Updated the SDU institutional link and clarified version information.'],
'appendices/appendix-a-rational-choice-and-decision-analysis.qmd':['Kept a job-offer decision as the explanatory context.','Corrected feasible versus considered sets and strengthened utility-model assumptions.','Retained equations and formal distinctions while shortening repeated applications.'],
'appendices/appendix-b-evolutionary-explanations-of-value-choice-and-rationality.qmd':['Led with one ordinary choice and separated the explanatory questions.','Moved Sapolsky, Bennett, and population models into optional notes.','Removed duplicate tables and repeated warnings; specified admissible replicator weights.','Reproduced the Schelling teaching run and simplified its illustration without changing states or values.'],
'appendices/appendix-c-portable-course-tools.qmd':['Rewrote compressed lists as usable instructions.','Linked the tool finder to explicit tool anchors and moved strategic tools to a dedicated section.','Clarified probability scoring, arbitration, and the limits of urge-observation exercises.'],
'appendices/appendix-e-how-behavioral-evidence-is-built.qmd':['Used the imagined clinic-reminder study throughout.','Grouped thirteen research steps into five phases, retaining individual headings.','Clarified assignment, missingness, noncompliance, and the ITT/LATE relationship.','Reproduced the synthetic study and simplified three methods diagrams.'],
'appendices/appendix-f-when-evidence-breaks.qmd':['Led with a publication-selection problem and moved the evidence catalogue after the explanation.','Removed repeated inventories and differentiated nonreplication, reanalysis, and integrity notices.','Completed primary-source audit of all twenty evidence-map entries; corrected replication scope and the dated deadline-study retraction.','Reproduced the selection simulation, added shared quantitative axes, and preserved source data byte for byte.']}
rows=[]
for f in inv['sources']:
 if f['owner']!='root' or f['path'] in ['concept-index.qmd','appendices/appendix-d-index-of-major-course-examples.qmd']:continue
 p=Path(f['path']);s=p.read_text();r=dict(f)
 if f['path']=='references.qmd':
  r.update(review_status='Generated and checked against the exact deduplicated union of canonical chapter and appendix reference blocks.',full_read=False,substantive_changes=['Synchronized changed citations and corrected bibliographic variants; metadata-source checks are recorded with the owning chapters and appendices.'])
 else:
  r.update(full_read=True,review_status='Full source read and revised',substantive_changes=changes.get(f['path'],['Replaced a catalogue of mechanisms with a concrete situation, three organizing questions, and a bridge to the part.','Replaced the repeated whole-book diagram with a compact three-question reading route.']))
 r.update(words_after=len(re.findall(r"\b[\w’'-]+\b",s)),sha256_after=hashlib.sha256(p.read_bytes()).hexdigest())
 rows.append(r)
figs=[]
for f in inv['figures']+[{'path':'figures/cover.png','owner':'root','used_by':['_quarto.yml','_quarto-epub.yml']}]:
 if f['owner']!='root':continue
 p=Path(f['path']);r=dict(f);v=[]
 if p.suffix=='.svg':v=[float(z) for z in ET.parse(p).getroot().attrib['viewBox'].split()][2:]
 r.update(semantic_review=True,individual_visual_inspection=True,contact_sheet_inspection=True,source_viewbox=v or 'raster',visual_status='REVISED_PASS' if p.suffix=='.svg' else 'REVIEWED_RETAINED',caption_and_alt_consistent=True,sha256_after=hashlib.sha256(p.read_bytes()).hexdigest(),rendered_fallback=str(p.with_suffix('.png')),visual_inspection='Every final PNG inspected individually; root contact sheets 1 and 2 inspected. Transformed text bounds checked in all fourteen SVGs. Final destination checks recorded separately.')
 if 'master-loop-part' in p.stem:r['change']='Three-question reading map with large type; arrows indicate reading order.'
 elif p.stem=='master-loop':r['change']='Compact vertical decision map, explicit social context, one feedback path, no fixed-stage claim.'
 elif p.stem=='selected-literature-simulation':r['change']='Matplotlib histograms with explicit shared scales and percentages within each displayed set; unchanged simulated estimates and selection rule.'
 elif p.stem=='schelling-emergence':r['change']='Shorter labels, larger type, preserved all three simulated states and summary values; detailed provenance moved to prose.'
 elif p.suffix=='.svg':r['change']='Reduced concept lists and redundant boxes; one clear question per stage; captions and alt text synchronized.'
 else:r['change']='Retained; image and text inspected.'
 figs.append(r)
(base/'root-ledger.json').write_text(json.dumps({'owner':'root','sources':rows,'figures':figs,'word_count_method':"len(re.findall(r\"\\b[\\w’'-]+\\b\", source)) includes markup and reference blocks",'scientific_followups':['appendices-a-e-f-independent-scientific-review.md (worker 29–41; A/E/F)','Follow-up review of B/C and evidence guide (worker 01–14)'],'validation':['simulation-checks.json','root-svg-text-qa.json','root-figures-contact-1.png','root-figures-contact-2.png']},indent=2,ensure_ascii=False)+'\n')
print(len(rows),'root sources plus two delegated indexes;',len(figs),'root figures including cover')
