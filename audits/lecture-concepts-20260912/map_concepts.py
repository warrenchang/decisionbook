"""Reproducible curriculum screen; editorial judgments are recorded separately.

Source matches locate passages for inspection. They are not evidence of scientific
validity or of adequate explanation. Only canonical Quarto body text is searched.
"""
from pathlib import Path
import csv, json, re, unicodedata

ROOT=Path(__file__).resolve().parents[2]
AUDIT=Path(__file__).resolve().parent
TEMP=Path('/private/tmp/decision-book-lecture-concepts-20260912')

# Primary teaching homes selected after reviewing the chapter outlines and the
# current and archived course units. '=' supplies spelling/terminology aliases.
TOPICS='''
01|Normative decision science=normative|Descriptive decision science=descriptive|Prescriptive decision science=prescriptive|Rationality=rational|Dominance=dominan|Description invariance=invariance|Process versus outcome=outcome
02|Opportunity cost|Alternatives=alternative|Constraints=constraint|Value of information|Sensitivity analysis=sensitivity|Robustness=robust|Bounded rationality
03|Selective attention=attention|Inattentional blindness|Change blindness|Top-down attention=top-down|Bottom-up attention=bottom-up|Divided attention=divided|Working memory|Task switching=switching|Attention economy|Default mode network|Central executive network|Salience network
04|Perception as inference=inference|Predictive processing|Prediction error|Precision weighting=precision|Prior expectations=prior|Active inference|Ambiguous perception=ambig|Generative AI
05|Forecast construction=forecast|Self-fulfilling prophecy=self-fulfilling|Self-defeating prediction=self-defeating|Placebo|Nocebo|Pygmalion effect=Pygmalion|Growth mindset=mindset|Learned helplessness=helplessness|Stereotype threat
06|Valuation|Automatic evaluation|Common currency|Somatic marker|Iowa Gambling Task|Interoception|Allostasis|Hot-cold empathy gap=empathy gap|Visceral influences=visceral|Self-related value=self|Social value=other people
07|Limits of introspection=introspect|Choice blindness|Confabulation|Cognitive dissonance|Self-perception|Post-choice rationalization=rationaliz|Hindsight bias=hindsight|Outcome bias|Organizational sensemaking=sensemaking
08|Dual-process theories=dual-process|Intuition|Deliberation|System 1|System 2|Attribute substitution|Recognition heuristic|Take-the-best|Satisficing|Ecological rationality|Recognition-primed decision making=recognition-primed
09|Availability heuristic=availability|Affect heuristic|Representativeness|Dilution effect=dilution|Integral affect=integral|Incidental affect=incidental|Misattribution of arousal=arousal|Affect and risk perception=risk
10|Confirmation bias|Myside bias|Biased assimilation|Motivated reasoning|Self-serving attribution=self-serving|Fundamental attribution error|Bias blind spot|Barnum effect|Positive illusions|Unrealistic optimism
11|Anchoring|Insufficient adjustment|Selective accessibility|Halo effect|Horn effect|Decoy effect=decoy|Attraction effect|Contrast effect=contrast|Compromise effect=compromise|Joint evaluation|Separate evaluation|Evaluability|Preference reversal|Prominence hypothesis
12|Framing|Risky-choice framing|Attribute framing|Goal framing|Gain versus loss frame=gain|Misinformation effect=misinformation|False memory=memory|Communicative framing=communicative
13|Priming|Semantic priming=semantic-priming|Conceptual priming=concept|Affective priming=affective-priming|Context-dependent memory|Encoding specificity=encoding-specificity|Processing fluency|Cognitive ease|Mere-exposure effect|Illusory-truth effect|Source monitoring=source memory|Subliminal cues=masked
14|Base rates=base rate|Conditional probability|Bayesian updating=Bayes|Natural frequencies|Likelihood ratio|Reference class|Conjunction rule=conjunction|Disjunction rule=disjunction|Independence=independen
15|Law of small numbers|Gambler's fallacy=gambler|Hot-hand effect=hot hand|Random clusters=cluster|Regression to the mean|Overconfidence|Overestimation|Overplacement|Overprecision|Dunning-Kruger=Dunning|Planning fallacy|Inside view=inside-view|Outside view|Calibration|Resolution|Brier score|Illusion of control
16|Expected value|Expected utility|Certainty equivalent|Risk aversion|Ambiguity aversion|Allais paradox=Allais|Ellsberg paradox=Ellsberg|St. Petersburg paradox=Petersburg|Compounding|Geometric mean|Probability of ruin=ruin|Kelly criterion=Kelly
17|Prospect theory|Reference dependence=reference point|Loss aversion|Diminishing sensitivity|Probability weighting|Fourfold pattern|Certainty effect|Endowment effect|IKEA effect|Status quo bias
18|Description-experience gap|Rare-event sampling=rare event|Optional stopping|Recency|Contingent sampling|Reinforcement learning|Exploration-exploitation trade-off=exploration|Normalcy bias
19|Intertemporal choice=intertemporal|Exponential discounting=exponential|Hyperbolic discounting=hyperbolic|Present bias=present-bias|Dynamic inconsistency=inconsisten|Magnitude effect=magnitude|Sign effect=sign effect|Date-delay framing=date|Hidden-zero effect=hidden-zero|Subjective time|Anticipation=savor|Episodic future thinking|Future-self continuity=future self|Precommitment=commitment|Scarcity and bandwidth=scarcity
20|Mental accounting|Fungibility=fungib|Acquisition utility|Transaction utility|Sunk costs=sunk cost|Escalation of commitment|Payment coupling=coupling|Pain of paying=pain|Mental budgets=budget|Choice bracketing=bracket|House-money effect=house money|Break-even effect=break-even|Disposition effect|Hedonic editing|Naive diversification|Diversification bias|1/n heuristic|Daily income targets
21|Habit formation=habit|Automaticity|Cue-response learning=cue|Positive reinforcement|Negative reinforcement|Reward prediction error|Dopamine|Incentive salience|Wanting versus liking=liking|Ego depletion|Urge surfing|RAIN|BRAIN|Marshmallow test|Self-control
22|Subjective well-being|Life satisfaction|Hedonic well-being=hedonic|Eudaimonic well-being=eudaimon|Predicted utility|Decision utility|Experienced utility|Remembered utility|Affective forecasting|Impact bias|Focalism|Projection bias|Peak-end rule=peak-end|Duration neglect|Hedonic adaptation=adaptation|Focusing illusion|Income and happiness=income|Social comparison
23|Strategic interdependence|Best response|Nash equilibrium|Prisoner's dilemma=prisoner|Coordination game=coordination|Focal points=focal|Stag hunt|Chicken game=chicken|Battle of the sexes|Volunteer's dilemma=volunteer|Commitment|Dollar auction|Unraveling=unravel
24|Level-k|Cognitive hierarchy|Beauty contest|Experience-weighted attraction|Quantal response|Strategic learning=learning|Equilibrium versus behavior=equilibrium
25|Social preferences|Altruism|Inequity aversion|Reciprocity|Ultimatum game|Dictator game|Trust game|Public goods|Conditional cooperation|Costly punishment=punishment|Repeated cooperation=repeated|Reputation|Assortment|Intention-based reciprocity=intention
26|Social learning|Mimicry|Informational influence=informational|Normative influence=normative|Conformity|Social proof|Descriptive norm|Injunctive norm|Dynamic norm|Pluralistic ignorance|False consensus|Information cascades=cascade|Herding=herd
27|Market efficiency=efficien|Efficient market hypothesis=efficient-market|Joint-hypothesis problem=joint test|Limits to arbitrage|Mispricing|Asset bubbles=bubble|Greater-fool reasoning=resale|Synchronization risk|Momentum|Investor overtrading=trading|Leverage|Systemic risk=systemic|Short selling=short-selling
28|Obedience|Authority|Bystander effect|Diffusion of responsibility|Groupthink|Shared-information bias=shared information|Group polarization|Psychological safety
29|Culture|Social identity=identity|Individualism|Collectivism|Analytic versus holistic cognition=holistic|Tightness-looseness=tightness|Power distance|Face culture=face|Honor culture=honor|Dignity culture=dignity|Big Five|Personality traits|WEIRD samples=WEIRD
30|Persuasion|Source credibility=credibility|Ethos|Logos|Pathos|Elaboration likelihood model|Heuristic-systematic model|Sufficiency principle|Sleeper effect|Fear appeals|Reactance|Foot-in-the-door|Door-in-the-face|Self-persuasion|Commitment and consistency=commitment|Reciprocity|Scarcity|Liking|Unity
31|Narrative persuasion|Transportation|Identification|Self-reference|Curiosity|Information gap=information-gap|Identifiable victim=identifiable|Compassion and statistics=statistics|Narrative simulation=simulation|Interbrain coupling=coupling
32|ABT|STORY|SUCCES|Narrative index|Audience model=audience|Evidence-aligned message=evidence|Social value of sharing=sharing
33|Common ground|Pragmatic inference=pragmat|Shared reality|Egocentric projection=egocentr|Illusion of transparency|Illusion of understanding|Perspective-taking|Perspective-getting|Listening feedback=feedback
34|Responsive listening=listening|Validation|Deep conversation=deep|Appreciation|Warm honesty|Co-rumination|Apology|Forgiveness|Ben Franklin effect|Social connection=connection
35|Principled negotiation=principled|Interests versus positions=positions|Value creation versus claiming=value|Negotiation preparation=prepar|Negotiator's dilemma=dilemma
36|BATNA|Reservation value|Aspiration=aspiration|ZOPA|Bargaining surplus=surplus|First offers=first offer|Precise offers=precision|Range offers=range|Reciprocal concessions=reciprocal|Bargaining power=power|Deadlines=deadline
37|Fixed-pie bias=fixed-pie|Logrolling|Issue priorities=priorities|Pareto efficiency|Integrative bargaining=integrative|Information exchange=information|Differences in risk preferences=risk|Differences in forecasts=forecast
38|MESO|Contingent contracts=contingent|Post-settlement settlements=post-settlement|Staged disclosure|Asymmetric information=information|Lie detection|Mediation|Arbitration|Process negotiation=process|Implementation=implementation
39|B=MAP|Implementation intentions|Mental contrasting|WOOP|Temptation bundling|Friction|Prompts=prompt|Habit discontinuity=context change|Commitment devices=commitment
40|Nudges=nudge|Defaults|Choice overload|Active choice|Sludge|Simplification|Salience|Feedback|Digital choice architecture=digital|Dark patterns=dark|Welfare and autonomy=autonomy
41|Noise|Structured judgment|Independent judgment|Aggregation|Premortem|Red team|Decision journal|Algorithm aversion|Algorithm appreciation|Human-AI judgment=AI|Forecasting tournament=forecasting
42|Predictive versus causal models=causal|Machine learning|Out-of-sample validation=validation|Data leakage=leakage|Prediction target=target|Feedback loops=feedback|AI governance=governance|Causal experiment=experiment
A|Utility axioms=axiom|Completeness|Transitivity|Independence axiom=independence|Decision tree|Expected-utility representation=expected utility|Value of perfect information=perfect information
B|Proximate versus ultimate explanations=proximate|Evolutionary mismatch|Maslow's hierarchy=Maslow|Kenrick's motives=Kenrick|Natural selection=selection|Evolutionary game theory=evolutionary game|Evolutionarily stable strategy=evolutionarily stable|Replicator dynamics=replicator|Schelling segregation=Schelling
E|Research question|Operationalization=operational|Hypothesis|Counterfactual|Confounding|Random sampling|Random assignment|Within-subject design=within|Between-subject design=between|Factorial design=factorial|Field experiment=field|Incentives=incentiv|Statistical power=power|Attrition|Noncompliance|Intention-to-treat|Local average treatment effect=local average|Spillovers|Hawthorne effect=Hawthorne|John Henry effect=John Henry|Internal validity|External validity|Research ethics=ethic|Reproducible workflow=reproduc
F|Replication|Reproducibility|Publication bias|Questionable research practices|Preregistration|HARKing|Multiple testing=multiplicity|Selective reporting|Retraction|Expression of concern|Effect size|Statistical significance|P-hacking|Type S error|Type M error
'''

def norm(s):
    s=unicodedata.normalize('NFKD',s).casefold()
    s=''.join(c for c in s if not unicodedata.combining(c))
    s=re.sub(r'[‐‑‒–—−]', '-', s).replace('’', "'")
    s=re.sub(r'[*_`]', '', s)
    s=re.sub(r'[^a-z0-9\s/]', ' ', s)
    return re.sub(r'\s+',' ',s).strip()

def terms(label, alias):
    choices=[label,alias]
    if '-' in alias:choices.append(alias.replace('-',' '))
    if ' ' in alias:choices.append(alias.replace(' ','-'))
    return list(dict.fromkeys(norm(t) for t in choices))

def main():
    lectures=json.loads((TEMP/'extracted.json').read_text())
    # Current editions first, then original subject-specific lecture units.
    priority=[102,103,104,105,106,107,108,109,111,112,113,114,195,196,197,198,199,200,201,202,24,21,37,67,65,2,6,12,31,33,39,41,43,45,47,49,51,53,54,55,61,63,68,72,74,76,77,82]
    order=priority+[i for i in range(len(lectures)) if i not in priority]
    sources=[]
    for i in order:
        d=lectures[i]
        for p in d['pages']:
            if re.match(r'^(references|sources|bibliography)',p['title'],re.I):continue
            sources.append((d,p,norm(p['text'])))
    homes={p.name[:2]:p for p in (ROOT/'chapters').glob('[0-9][0-9]-*.qmd')}
    for k in ['A','B','E','F']:homes[k]=next((ROOT/'appendices').glob(f'appendix-{k.lower()}-*.qmd'))
    out=[]
    for group in TOPICS.strip().splitlines():
        home,*concepts=group.split('|');p=homes[home];body=p.read_text().split('## References cited')[0]
        # Prefer developed body passages over labels in learning goals and the epigraph.
        paragraphs=re.split(r'\n\s*\n',re.sub(r'^:::.*$', '', body, flags=re.M))
        for c in concepts:
            label,alias=c.split('=',1) if '=' in c and c!='B=MAP' else (c,c)
            ts=terms(label,alias)
            hits=[]
            for d,page,txt in sources:
                if any(t in txt for t in ts):
                    hits.append({'source':d['source'],'sha256':d['sha256'],'page':page['page'],'title':page['title']})
                    if len(hits)==2:break
            matches=[]
            for j,x in enumerate(paragraphs):
                if x.startswith(('>','![')):continue
                if any(t in norm(x) for t in ts):
                    if x.startswith('#') and j+1<len(paragraphs):x=x+'\n\n'+paragraphs[j+1]
                    matches.append(x)
            excerpt=max(matches,key=lambda x: min(len(x),700)) if matches else ''
            offset=body.find(excerpt) if excerpt else -1
            heads=list(re.finditer(r'^#{2,3} (.+)$',body[:offset],re.M)) if offset>=0 else []
            section=heads[-1][1] if heads else 'Opening / chapter overview'
            out.append({'concept':label,'home':home,'book_file':str(p.relative_to(ROOT)),'book_section':section,'book_excerpt':excerpt[:950], 'lecture_matches':hits,'body_match':bool(matches),'source_match':bool(hits),'match_method':'normalized labels and declared aliases; editorial adequacy requires passage review'})
    (AUDIT/'concept-screen.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    with (AUDIT/'concept-screen.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['Concept','Home','Book file','Section','Body match','Lecture source','Slide/page'])
        for x in out:
            h=x['lecture_matches'][0] if x['lecture_matches'] else {}
            w.writerow([x['concept'],x['home'],x['book_file'],x['book_section'],x['body_match'],h.get('source',''),h.get('page','')])
    print('Concept groups:',len(out),'Body matches:',sum(x['body_match'] for x in out),'Source matches:',sum(x['source_match'] for x in out))
    for x in out:
        if not x['body_match']:print('BODY REVIEW',x['home'],x['concept'],json.dumps(x['lecture_matches'][:1],ensure_ascii=False))
    for x in out:
        if not x['source_match']:print('SOURCE REVIEW',x['home'],x['concept'])

if __name__=='__main__':main()
