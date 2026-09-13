"""Write the editorial coverage record from reviewed decisions and source manifests."""
from pathlib import Path
import csv,difflib,hashlib,json,re,runpy,unicodedata
ROOT=Path(__file__).resolve().parents[2]; AUDIT=Path(__file__).resolve().parent
TEMP=Path('/private/tmp/decision-book-lecture-concepts-20260912')
BEFORE={x['file']:x for x in json.loads((AUDIT/'book-topics-before.json').read_text())}
CHAPTERS=sorted((ROOT/'chapters').glob('[0-9][0-9]-*.qmd'))
TITLE_REASONS={
1:'Retains the normative/descriptive contrast and the functional decision loop.',
2:'Names the chapter\'s workflow for alternatives, opportunity costs, information, and robustness.',
3:'The core constraint underlying selection, divided attention, and switching; retained from the preceding title revision.',
4:'Covers perception as inference, priors, prediction error, and precision; generative AI remains optional.',
5:'Expectations change forecasts and, through identifiable pathways, outcomes; selective evidence belongs primarily in Chapter 10.',
6:'Covers emotion, bodily state, self, others, and subjective comparison without listing every value input.',
7:'Keeps the organizing question of retrospective explanation; includes introspection, confabulation, choice blindness, and dissonance.',
8:'Now names both intuitive and deliberative processing, including expertise and their interaction.',
9:'Retains the requested three mechanisms; dilution is an extension of representativeness.',
10:'Now explicitly names confirmation bias and motivated reasoning, the chapter\'s central mechanisms.',
11:'Retains the memorable three principal context effects; the subtitle and new evaluation section cover the broader comparison theme.',
12:'Covers equivalent descriptions, memory questions, and communicative framing without an overlong heading.',
13:'Adds priming to the title because it is a substantial treatment distinct from fluency and familiarity.',
14:'Matches conditional probability, reference classes, natural frequencies, and Bayes.',
15:'Now makes overconfidence visible alongside sampling, streaks, regression, and calibration; the subtitle retains the statistical scope.',
16:'Covers expected value/utility, risk, ambiguity, compounding-related growth, and decision consequences.',
17:'Matches reference dependence, value and weighting functions, loss aversion, and their boundaries.',
18:'Matches feedback, rare-event sampling, recency, exploration, and normalization of risk.',
19:'Preserves the specifically requested Intertemporal Decision Making and Why Later Loses to Now subtitle.',
20:'The common home for labeling, bracketing, payment coupling, sunk cost, and diversification.',
21:'Separates cue-linked habits, motivational attraction, pleasure, and practical self-control.',
22:'Spans forecasting, experience, remembered utility, life evaluation, connection, and meaning.',
23:'Names the dependence of a best move on others\' actions and expectations.',
24:'Covers limited strategic depth, equilibrium as benchmark, learning, and evolutionary models.',
25:'Separates strategic cooperation from altruism, inequality, intentions, and norms.',
26:'Matches social information, conformity, norm expectations, and cascades.',
27:'Replaces Prices as Social Signals with the full scope: efficiency, arbitrage, mispricing, bubbles, and investor behavior.',
28:'Retains the three mechanisms that organize authority, group information, and bystander responsibility.',
29:'Preserves the main social-meaning argument; personality is a bounded optional lens, not a replacement theme.',
30:'Covers routes, sources, resistance, commitments, self-persuasion, and ethical influence.',
31:'Retains the explanatory focus on attention, identity, emotion, simulation, and identifiable victims.',
32:'Distinguishes practical message construction from the mechanisms in Chapter 31.',
33:'Keeps the umbrella for grounding, pragmatic inference, projection, and verified understanding.',
34:'Covers responsive listening, appreciation, warm honesty, apology, and forgiveness.',
35:'Names negotiation as preparation, interaction, implementation, and learning; introduces principled negotiation.',
36:'Uses the standard course term for alternatives, reservation values, opening offers, concessions, and claiming value.',
37:'Uses the standard course term for interests, logrolling, differences, and Pareto improvement.',
38:'Names contingent agreements, multiple offers, verification, process, and implementation.',
39:'Matches the practical workflow and distinguishes design from the contested depleted-resource account.',
40:'Covers menus, defaults, friction, choice overload, feedback, welfare, and governance.',
41:'Keeps the process focus on independent estimates, noise, disagreement, review, and accountable judgment.',
42:'Now explicitly names AI as well as data; the chapter centers on prediction, valuation, causal benefit, and accountable action.'}
def clean_title(x):return re.sub(r'\s*\{[^}]*\}\s*$','',x).strip()
records=[]
for p in CHAPTERS:
 s=p.read_text();n=int(p.name[:2]);file=str(p.relative_to(ROOT));title=clean_title(re.search(r'^# (.+)$',s,re.M)[1])
 ep=re.search(r'^::: [^\n]*\.chapter-epigraph',s,re.M);assert ep
 subs=re.findall(r'^\*([^\n]+)\*$',s[:ep.start()],re.M);assert len(subs)==1,(file,subs)
 before=clean_title(BEFORE[file]['title'])
 records.append({'chapter':n,'file':file,'before':before,'title':title,'subtitle':subs[0],'changed':before!=title,'rationale':TITLE_REASONS[n]})
(AUDIT/'chapter-titles.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
lines=['# Chapter title review','All 42 titles were checked against their learning goals, major sections, and developed concepts. The baseline includes the six concise titles already edited before this pass. One italic subtitle is retained for each chapter. Filenames and existing link targets are preserved.','| Ch. | Reviewed title | Decision and reason |','| --- | --- | --- |']
for r in records:lines.append(f"| {r['chapter']} | **{r['title']}** | {'Changed from '+r['before']+'. ' if r['changed'] else 'Retained. '}{r['rationale']} |")
(AUDIT/'chapter-titles.md').write_text('\n\n'.join(lines[:2])+'\n\n'+'\n'.join(lines[2:])+'\n')
# Machine screen false negatives require editorial decisions, not forced additions.
resolutions={
('01','Dominance'):('25','The opening Prisoner\'s Dilemma works through strict dominance; Golden Balls distinguishes weak dominance. Chapter 11 also develops dominated decoys.'),
('09','Integral affect'):('06','The valuation chapter distinguishes integral emotion from incidental spillover; Chapter 9 applies affect to probability judgments.'),
('09','Misattribution of arousal'):('06','The valuation chapter develops the Dutton-Aron study and the limits of the arousal inference.'),
('12','Communicative framing'):('12','Covered in questions that contain an answer and framing in management, negotiation, and policy; the label is broader than a distinct missing mechanism.'),
('14','Likelihood ratio'):('14','Bayesian updating and likelihoods are worked numerically. No separate likelihood-ratio teaching requirement was found; an extra odds-form derivation was not added.'),
('16','Compounding'):('19','Interest compounding has its own section in Chapter 19; Chapter 16 separately handles repeated multiplicative risk and ruin.'),
('16','Kelly criterion'):('16','The named criterion occurred in a supplemental third-party PDF, not the inspected core teaching units. Retained the book\'s growth, risk, and ruin discussion without adding an investment-sizing prescription.'),
('21','Ego depletion'):('39','Full account and replication qualifications in Willpower is not one depletable fuel; Appendix F also records the evidence status.'),
('21','Marshmallow test'):('19','Full treatment and reliability/background qualifications belong in intertemporal choice; Appendix F carries the later evidence.'),
('22','Hedonic well-being'):('22','Developed through experienced affect, life evaluation, and their contrast with eudaimonic meaning. The first lexical lecture hit concerns hedonic editing in mental accounting and is not a direct source for this concept.'),
('23',"Prisoner's dilemma"):('25','The game is the opening worked payoff matrix in the cooperation chapter; repeating it in Chapter 23 would duplicate the treatment.'),
('23','Unraveling'):('24','The beauty-contest reasoning and repeated movement toward lower choices are developed in behavioral game theory.'),
('24','Experience-weighted attraction'):('24','No distinct EWA requirement was found in the extracted teaching units, including an acronym search. The chapter already distinguishes payoff, action, belief, and counterfactual feedback; a new formal model was not added.'),
('24','Quantal response'):('24','No distinct QRE requirement was found in the extracted teaching units, including an acronym search. Did not expand the course into an additional formal estimation model.'),
('25','Assortment'):('25','Explicit positive assortment is now introduced with reputation, networks, and institutions.'),
('28','Group polarization'):('28','No separate polarization or risky-shift topic was found in the extracted core units. Existing shared-information, conformity, and groupthink mechanisms were retained without treating them as synonyms for polarization.'),
('29','WEIRD samples'):('29','The chapter spells out Western, educated, industrialized, rich, and democratic and explains sampling limits. The machine\'s lecture match to an ordinary word weird is not evidence of this acronym.'),
('31','Information gap'):('32','Loewenstein\'s account is fully developed under message curiosity in Chapter 32; Chapter 31 already introduces attention and curiosity.'),
('41','Algorithm appreciation'):('42','The Logg et al. finding is now explicitly named in Trust, valuation, and responsibility; the aversion/appreciation distinction spans Chapters 41 and 42.'),
('42','AI governance'):('42','Developed as human authority, objectives, authorization, review, and remedies, with NIST cited; no additional generic section needed.'),
('F','Selective reporting'):('F','Developed under flexible analysis and publication selection; already distinguishes analysis selection from misconduct.'),
('F','Statistical significance'):('F','The reporting gate, false positives, low power, Type S/M errors, and differences between significance and effect size are developed; Appendix E supplies the planned-analysis workflow.')}
(AUDIT/'screen-resolutions.json').write_text(json.dumps([{'screen_home':k[0],'concept':k[1],'actual_home':v[0],'decision':v[1]} for k,v in resolutions.items()],ensure_ascii=False,indent=2)+'\n')
screen=json.loads((AUDIT/'concept-screen.json').read_text());missing=[]
for r in screen:
 k=(r['home'],r['concept']);resolved=resolutions.get(k)
 r['editorial_home']=resolved[0] if resolved else r['home']
 actual=r['editorial_home']
 target=next((ROOT/'chapters').glob(actual+'-*.qmd')) if actual.isdigit() else next((ROOT/'appendices').glob('appendix-'+actual.lower()+'-*.qmd'))
 r['reviewed_book_file']=str(target.relative_to(ROOT))
 r['editorial_note']=resolved[1] if resolved else 'Located in the chapter body; the lexical hit is a navigation aid, not an independent adequacy or source-validity score.'
 r['status']='placement or scope resolved' if resolved else 'body passage located' if r['body_match'] else 'unresolved screen flag'
 if r['status']=='unresolved screen flag':missing.append(k)
(AUDIT/'coverage-map.json').write_text(json.dumps(screen,ensure_ascii=False,indent=2)+'\n')
with (AUDIT/'coverage-map.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Concept','Initial home','Reviewed home','Status','Editorial note','Reviewed book file','Initial matched section','First lexical source','Slide/page'])
 for r in screen:
  h=r['lecture_matches'][0] if r['lecture_matches'] else {}
  w.writerow([r['concept'],r['home'],r['editorial_home'],r['status'],r['editorial_note'],r['reviewed_book_file'],r['book_section'],h.get('source',''),h.get('page','')])
# No reference is removed relative to the snapshots made before this turn's edits.
h=runpy.run_path(str(ROOT/'scripts/sync_references.py'));refpat=h['REFERENCE_BLOCK'];deleted=[];added=set();diff=[];changes=[]
for p in sorted((TEMP/'before').rglob('*.qmd')):
 rel=p.relative_to(TEMP/'before');dest=ROOT/rel
 old=p.read_text();new=dest.read_text()
 oldrefs={h['reference_key'](x) for x in refpat.findall(old)};newrefs={h['reference_key'](x) for x in refpat.findall(new)}
 deleted.extend({'file':str(rel),'reference':x} for x in sorted(oldrefs-newrefs));added.update(newrefs-oldrefs)
 if old!=new:
  changes.append({'file':str(rel),'before_sha256':hashlib.sha256(old.encode()).hexdigest(),'after_sha256':hashlib.sha256(new.encode()).hexdigest(),'net_words':len(new.split())-len(old.split())})
  diff.extend(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='before/'+str(rel),tofile='after/'+str(rel)))
(AUDIT/'revision.patch').write_text(''.join(diff))
summary={'snapshot_sources_compared':len(list((TEMP/'before').rglob('*.qmd'))),'changed_snapshot_sources':changes,'removed_reference_entries':deleted,'new_reference_texts':len(added),'changed_chapter_titles':sum(r['changed'] for r in records),'screen_rows':len(screen),'unresolved_screen_flags':missing}
(AUDIT/'source-verification.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print('Titles reviewed:',len(records),'changed:',sum(r['changed'] for r in records),'removed references:',len(deleted),'unresolved flags:',missing)
assert not deleted
# Source labels use one-based physical slides/pages; printed slide counters sometimes differ.
