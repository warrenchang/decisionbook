#!/usr/bin/env python3
"""Verify reviewed cleanup against canonical SVGs and isolated generator execution.

Run with Matplotlib 3.11.1 (the version recorded in the simulation's raw SVG):
  MPLCONFIGDIR=/private/tmp/figure-mpl python verify_generators.py
Only audit/tmp outputs are written; canonical figures and raw data are read-only.
"""
import sys,pathlib,json,hashlib,importlib.util,csv,platform
ROOT=pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from reviewed_figure_cleanup import clean_svg
OUT=ROOT/'tmp/figure-declutter-20260927/generator-check/final';OUT.mkdir(parents=True,exist_ok=True);(OUT/'figures').mkdir(exist_ok=True)
sha=lambda s:hashlib.sha256(s.encode()).hexdigest()
manifest=json.loads((ROOT/'scripts/reviewed_figure_cleanup.json').read_text())
results=[]
for name,entry in manifest['figures'].items():
 reviewed=(ROOT/'figures'/name).read_text()
 assert sha(reviewed)==entry['output_sha256'],(name,'canonical output hash')
 inv=[];delta=0
 for p in entry['patches']:
  start=p['start']+delta;end=start+len(p['after']);assert reviewed[start:end]==p['after'],(name,'reverse patch')
  inv.append((start,end,p['before']));delta+=len(p['after'])-len(p['before'])
 raw=reviewed
 for start,end,before in reversed(inv):raw=raw[:start]+before+raw[end:]
 assert sha(raw)==entry['input_sha256'],(name,'reconstructed input hash')
 assert clean_svg(name,raw)==reviewed
 assert clean_svg(name,reviewed)==reviewed
 rejected=False
 try:clean_svg(name,raw+'<!-- unreviewed drift -->')
 except ValueError:rejected=True
 assert rejected,(name,'unreviewed drift must fail')
 results.append({'asset':name,'canonical_hash_matches':True,'reverse_patch_input_hash_matches':True,'exact_patch_replay':True,'reviewed_output_is_noop':True,'unreviewed_drift_rejected':True})
def module(name):
 spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
executions=[]
def check(name,generated):
 reviewed=(ROOT/'figures'/name).read_text();assert generated==reviewed,(name,'isolated generator output mismatch')
 (OUT/'figures'/name).write_text(generated)
 executions.append({'asset':name,'matches_canonical_bytes':True,'sha256':sha(generated),'isolated_output':str((OUT/'figures'/name).relative_to(ROOT))})
new=module('build_new_chapter_figures');check('finance-event-study-drift.svg',clean_svg('finance-event-study-drift.svg',new.event_study()))
reading=module('build_reading_figures');reading.ROOT=OUT
for fun,name in [(reading.fluency_pathway,'fluency-pathway.svg'),(reading.urge_observation,'urge-wave-observation.svg')]:
 fun();check(name,(OUT/'figures'/name).read_text())
coord=module('build_coordination_experience_figures');coord.ROOT=OUT
coord.cold_water();check('cold-water-better-ending.svg',(OUT/'figures/cold-water-better-ending.svg').read_text())
# The unlisted second asset must continue to regenerate without altered behavior.
coord.stag_hunt();check('stag-hunt-belief-payoffs.svg',(OUT/'figures/stag-hunt-belief-payoffs.svg').read_text())
methods=module('build_methods_appendix_figures');generated,rows,metadata=methods.selected_literature_simulation();check('selected-literature-simulation.svg',generated)
with (ROOT/'figures/source/selected-literature-simulation.csv').open() as f:source=list(csv.DictReader(f))
assert len(rows)==len(source)==2000
for fresh,old in zip(rows,source):
 for key,value in fresh.items():
  if isinstance(value,bool):assert str(value)==old[key],(key,fresh['study'])
  elif isinstance(value,(float,int)):assert float(value)==float(old[key]),(key,fresh['study'])
  else:assert value==old[key]
prior_metadata=json.loads((ROOT/'figures/source/selected-literature-simulation.json').read_text())
for key,value in metadata.items():assert value==prior_metadata[key],(key,'metadata drift')
import matplotlib,numpy
prepare_path=ROOT/'tmp/figure-declutter-20260927/generator-check/prepare-checks.json'
report={'date':'2026-09-27','status':'PASS','runtime':{'python':sys.version,'executable':sys.executable,'platform':platform.platform(),'matplotlib':matplotlib.__version__,'numpy':numpy.__version__},'manifest_entries_verified':len(results),'actual_generator_outputs_verified':len(executions),'manifest_checks':results,'isolated_executions':executions,'prior_raw_reconstruction':json.loads(prepare_path.read_text()) if prepare_path.exists() else None,'simulation_data_verification':{'rows':len(rows),'all_source_CSV_values_identical':True,'all_source_metadata_identical':True,'selected_studies':metadata['selected_studies'],'mean_selected_estimates':metadata['mean_selected_estimates']},'prior_manifest_archive':'audits/figure-declutter-20260927/generator-manifest-before.json','prior_drift_preserved':{'asset':'urge-wave-observation.svg','note':'Task-start canonical gradient redesign predates this task but was not represented by prior cleanup output. Its raw generator input matched the old manifest hash; exact patches now preserve the current canonical SVG unchanged.'},'canonical_assets_or_raw_data_written':False,'verification_script':str(pathlib.Path(__file__).relative_to(ROOT))}
(ROOT/'audits/figure-declutter-20260927/generator-verification.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:report[k] for k in ['status','manifest_entries_verified','actual_generator_outputs_verified','simulation_data_verification']},indent=2))
