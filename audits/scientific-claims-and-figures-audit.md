# Scientific claims and figures audit

**Scope:** all 87 distinct reader-facing visual assets and a book-wide screen of the manuscript's substantive claims, completed 29 August 2026. Repeated figure placements were checked in their local chapter context. This audit complements the geometric and rendering checks in `figure-visual-audit.md`.

## What this audit can and cannot establish

The audit asked four questions of every figure: (1) Is the represented relationship scientifically defensible? (2) Does the visual encode sequence, hierarchy, causation, magnitude, or universality that the evidence does not establish? (3) Is its provenance clear—empirical redraw, theoretical model, or author teaching synthesis? (4) Does the caption state the relevant boundary?

The manuscript was also screened for strong universal language, exact quantitative claims, construct slippage, causal overstatement, and conflicts between text and figure. High-priority claims were checked against the cited primary study or review. This is not a claim that every sentence in a large interdisciplinary textbook has been independently replicated. It is a documented scientific editorial audit: no critical falsehood remained after the corrections below, while disagreements and remaining identification limits are stated where readers encounter them.

## Outcome

The 87 unique visuals fall into three non-overlapping audit dispositions:

- **45 context-appropriate figures:** the scientific relationship and boundary were already adequate; captions and chapter sources identify what is being shown.
- **23 semantic revisions:** the figure or surrounding claim was changed because the former design implied an unsupported sequence, hierarchy, mechanism, magnitude, or universality.
- **19 author syntheses relabelled:** these are useful navigation or practice models, but not validated scientific stage models. Their captions now say so explicitly.

Every revised SVG has a matching PNG fallback. Final HTML and EPUB rendering, connector geometry, text containment, and mobile-width checks are recorded separately by the release QA.

## Semantic revisions

| Asset | Scientific problem found | Current representation and boundary |
|---|---|---|
| `attention-bottleneck` | A funnel invited subtraction of incomparable information-rate estimates. | Sensory acquisition and deliberate behavioural control are shown as separate order-of-magnitude measurements; the figure explicitly says not to subtract them. |
| `attention-filter` | A hard filter implied that unattended information has no effect. | Attention prioritizes information for conscious report and deliberate use; limited unattended processing remains possible. |
| `judgment-and-decision-making-according-to-predictive-processing` | Precision, attention, prediction error, prediction, and valuation were too easily conflated. | Precision is defined as estimated prediction-error reliability; attention is related but not identical; the architecture is labelled a theoretical synthesis with variants. |
| `expectation-loop` | A single circular chain collapsed distinct pathways and made self-fulfilment look automatic. | Four parallel pathways—physiology, behaviour, interpersonal response, and resources/opportunities—can operate alone or together; feedback can be self-fulfilling or self-defeating. |
| `fast-slow` | Two-system shorthand could be read as two brain modules or mutually exclusive mechanisms. | Type 1 and Type 2 are presented as feature clusters; processing can mix and practice can change task demands. |
| `anchor-decoy` | The visual treated labels as mechanisms and the decoy effect as unconditional. | The anchoring finding is separated from competing insufficient-adjustment, selective-accessibility, and scale-construction accounts; attraction effects are conditional on option geometry and task. |
| `fluency-pathway` | Ease appeared to determine truth, safety, and liking. | Fluency can influence familiarity, confidence, liking, and judged truth; risk and safety inferences are explicitly context-dependent. |
| `decision-experience-states` | Description and experience were each labelled information-poor in a way the evidence does not support. | The figure compares different information and sampling structures; deep uncertainty is conditional, not inherent to either mode. |
| `habit-loop` | Urge appeared to be a necessary stage of every habit. | The core path is context/cue → response tendency → action → immediate consequence → learning update; wanting is a possible side path. |
| `reward-prediction-error-shift` | A textbook conditioning pattern and an applied progress-cue hypothesis were visually merged. | The three canonical cue/reward patterns are separated from the proposed application to progress signals. |
| `wanting-liking` | A discrepancy appeared to guarantee successful relearning. | The discrepancy provides possible evidence and an opening for relearning; it does not guarantee change. |
| `mental-accounting-map` | The operations looked mandatory and money appeared always fungible. | Labelling, bracketing, payment–consumption coupling, and account closure are optional and combinable; fungibility applies only to unrestricted otherwise-equivalent resources. |
| `strategic-situation-diagnostic` | Archetypes appeared mutually exclusive; anti-coordination appeared outside the coordination family. | The archetypes can overlap, and anti-coordination is located within the broader coordination family. |
| `social-learning-culture` | Observation and copying appeared sufficient for a fixed progression to cumulative culture. | Innovation, social learning, transmission fidelity, retention/institutions, and selection/correction are nonsequential contributors; accumulation can preserve useful modifications or error. |
| `social-pathways` | Informational influence and normative pressure were collapsed into one feedback loop. | The routes are parallel: belief updating can occur without dissent cost, and public conformity can occur without private belief change. |
| `cultural-market-study-redraw` | Schematic bar heights carried four-decimal labels that looked like recovered estimates. | The plot now communicates only the published directional comparison and labels its heights as schematic; participant denominators and comparison procedure remain visible. |
| `story-update` | A writing template looked like a scientific definition of story and a guaranteed action sequence. | AND–BUT–THEREFORE is labelled one narrative-design template; evidence, belief revision, intention, and action remain separate claims. |
| `communication-iceberg` | A pyramid/iceberg metaphor implied a fixed hidden proportion and hierarchy. | Utterance, plausible interpretations, contextual inference, and grounding are shown as an iterative recoverable process without a fixed ratio. |
| `pareto` | The earlier frontier invited a false ordering and confused feasible, efficient, and mutually preferred outcomes. | The redraw distinguishes the feasible set, Pareto frontier, reference agreement, and mutually improving region without ranking all frontier points. |
| `agreement-design` | A linear sequence made verification, implementation, and review look like guaranteed stages. | Agreement design is a revisable workflow with conditional feedback, authority, evidence, adaptation, and exit. |
| `behavior-design` | A pyramid visually asserted that recovery is a universal foundation. | Figure 39.1 is now an iterative Define → Diagnose → Redesign → Test → Learn workflow. Recovery is a conditional branch triggered by lapse, failure, or changed context—not a prerequisite or permanent base. |
| `bias-and-noise` | Bias and noise appeared exhaustive and independent. | They are shown as distinct diagnostic components that can co-occur; total error can also include measurement and model error. |
| `human-ai-judgment` | The previous flow risked assigning valuation and accountability to the model. | Predictive assistance, human valuation, contestability, verification, override, and human accountability are separated. |

The revisions draw especially on the cited reviews and frameworks for attention and processing without awareness, predictive processing, dual-process theory, expectations, habit, behaviour change, social influence, communication grounding, and human–AI judgment. Full bibliographic records remain in the chapters where the claims are taught.

## Author teaching syntheses now labelled at the point of use

These figures organize the book or turn evidence into a practical workflow. They are not presented as validated universal stage models:

`master-loop`; `master-loop-part-1`; `master-loop-part-2`; `master-loop-part-3`; `master-loop-part-4`; `master-loop-part-5`; `master-loop-part-6`; `master-loop-part-7`; `valuation`; `narrator-learning`; `belief-protection-loop`; `intertemporal-choice`; `persuasion-update`; `story-evidence-braid`; `conversation-needs-map`; `conversation-repair`; `choice-architecture`; `structured-judgment-pipeline`; `decision-improvement-cycle`.

Their captions now identify them as teaching or prescriptive syntheses and, where relevant, state that stages may overlap, recur, or be skipped. A repeated master loop is counted once in the 87-asset inventory.

## Context-appropriate figures

The following figures passed the semantic audit without requiring a scientific redesign. “Pass” means that the relationship shown is suitable for the accompanying claim and boundary; it does not convert an illustration into independent evidence.

`decision-loop`; `decision-making-according-to-behavioral-evidence`; `rational-benchmark`; `option-information`; `heuristic-substitution`; `daughter-finger-counting`; `affect-panda-sea-star`; `affect-availability`; `prototype-probability`; `context-mechanisms`; `wording-memory-study-redraw`; `priming-pathway`; `probability-judgment-map`; `risky-decision-map`; `prospect-theory-map`; `experience-rare-event-sampling`; `habit-formation-curve`; `urge-wave-observation`; `mental-accounting-evidence-redraw`; `subjective-well-being-six-lenses`; `income-wellbeing-evidence-synthesis`; `three-lenses-strategic-behavior`; `level-k-reasoning-ladder`; `cooperation-architecture`; `social-preference-games-redraw`; `mimicry-study-redraw`; `norm-message-diagnostic`; `finance-euro-efficiency`; `behavioral-finance-audit`; `finance-event-study-drift`; `asset-bubble-feedback`; `bubble-trader-strategies-redraw`; `culture-meaning-map`; `culture-triad-monkey-panda-banana`; `culture-honor-study-redraw`; `communication-grounding`; `communication-calibration-evidence`; `intent-behavior-impact-cycle`; `negotiation-architecture`; `zopa`; `first-offer-information-matrix`; `decision-audit`; `claim-to-design-pipeline`; `selected-evidence-pipeline`; `huanren-warren-zhang-profile`.

## Claim corrections made alongside the figure audit

- **Expectation effects:** the wine-price study is described as a change in reported pleasantness and medial-orbitofrontal activity consistent with altered experienced valuation, not as a unique neural mechanism. The energy-drink study distinguishes the experimental price-information effect from its proposed expectancy mediator.
- **Stereotype threat:** the text now reports heterogeneity, the negligible-to-small estimate under operationally plausible cognitive-testing conditions, and publication-bias evidence. It does not diagnose stereotype threat from a performance gap alone.
- **Elaboration likelihood:** central and peripheral routes are described as ends of an elaboration continuum; mixed processing and multiple roles for the same variable are explicit; high elaboration is not equated with unbiased rationality.
- **Dunning–Kruger pattern:** the text distinguishes metacognitive explanations from regression, measurement, and score-construction artefacts.
- **Attention:** limited selection for conscious report and deliberate use is distinguished from the stronger and unsupported claim that unattended information has no effect.
- **Prospect theory:** reference dependence is treated as a model to test, not a universal property of every decision.
- **Defaults:** a default is the outcome implemented without an active choice; friction, switching costs, endorsement, inertia, and loss aversion remain distinguishable possible mechanisms.
- **Behavioural finance:** return notation, the ex-dividend assumption, event dates, and NASDAQ level changes were made explicit and source-checkable.
- **Cultural-market evidence:** schematic directions are separated from exact recovered estimates.

## Core source checks for the most consequential revisions

- Michie, van Stralen, and West (2011), COM-B as an interacting system: https://doi.org/10.1186/1748-5908-6-42
- Fogg (2009), behaviour as the convergence of motivation, ability, and prompt/trigger: https://doi.org/10.1145/1541948.1541999
- Kwasnicka et al. (2016), maintenance mechanisms and relapse/recovery boundaries: https://doi.org/10.1080/17437199.2016.1151372
- Mudrik and Deouell (2022), limits and evidence for processing without awareness: https://doi.org/10.1146/annurev-neuro-110920-033151
- Evans and Stanovich (2013), defining features and cautions in dual-process theories: https://doi.org/10.1177/1745691612460685
- Wood and Rünger (2016), habit formation and habitual control: https://doi.org/10.1146/annurev-psych-122414-033417
- Clark and Brennan (1991), grounding in communication: https://doi.org/10.1037/10096-006
- Shewach, Sackett, and Quint (2019), stereotype-threat boundary in operational testing: https://doi.org/10.1037/apl0000420
- Bond and DePaulo (2006), unaided deception-judgment accuracy: https://doi.org/10.1207/s15327957pspr1003_2
- Vrij, Hartwig, and Granhag (2019), weak and unreliable nonverbal deception cues: https://doi.org/10.1146/annurev-psych-010418-103135
- Brett, Ramirez-Marin, and Galoni (2021), cross-cultural negotiation theory and measurement: https://doi.org/10.34891/20210918-525
- Wall and Dunne (2012), limits and heterogeneity of mediation evidence: https://doi.org/10.1111/j.1571-9979.2012.00336.x

## Release gate

The final post-revision release checks passed on 29 August 2026:

- the canonical source-and-render audit reported 0 errors and 0 warnings;
- all 91 SVG files parsed successfully, and the connector audit passed for 83 arrow-bearing reader figures;
- the HTML and EPUB profiles rendered successfully with 7 Parts and 41 numbered chapters;
- the EPUB package audit reported 0 errors;
- headless-browser inspection loaded all 89 configured HTML figure placements at desktop and phone widths and all 88 EPUB placements at tablet and phone widths, with no broken image, overflow, containment, or caption issues;
- the concept index contains 344 unique stable anchors, 806 internal concept links, and 797 clickable *See also* links, with no unresolved target and no concept anchor added to EPUB navigation; and
- a rendered-output link scan found no broken internal file or fragment link.

These checks establish source consistency, package integrity, and rendering quality for this version. They do not turn an illustrative diagram into empirical evidence or substitute for later source rechecking when claims, figures, or cited literatures change.
