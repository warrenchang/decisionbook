# Book comparison review ledger

This ledger records the full 61-component review, source verification, and independent review for the comparison-context revision. See `book-comparisons-20260911.md` for the release summary.


---

# Root review: Chapter 42, other book components, and writing skills

Date: 2026-09-11. Baseline: the 61 canonical QMDs in `before/`, preserving the prior ABT revision. Reviewed Chapter 42 and the 19 configured front/back/Part components; collaborators reviewed Chapters 1–41. Focus: a numerical or performance claim carrying an argument must provide its relevant comparison where it appears.

## Chapter 42

- **Flint opening and field case:** Replaced the isolated 15% hit rate with approximately 80% under model-guided targeting versus 15% in 2018 after priorities changed. The field case also gives approximately 70% after model-guided targeting resumed. The source is the supplied *Power and Prediction*, chapter 15, together with the original project team's February 2020 report. Preserved the separate 18.8% versus 2.0% backtesting comparison; those are unnecessary visits under a different comparison, not excavation hit rates from randomized field groups. One footnote identifies the denominator and successive programme phases.
- **Inference price:** Added US$20 versus US$0.07 per million tokens, with November 2022/October 2024 and the same GPT-3.5-level MMLU performance already specified. The Stanford report supplies those values; no current-price extrapolation was added.
- **Customer support:** Named working without the assistant as the comparator for the existing 15% issues-resolved-per-hour increase from the staggered rollout.
- **MASAI:** Labeled AI-supported screening and standard double reading beside 1.55/1.76 interval cancers per 1,000 women. Added sensitivity 80.5%/73.8% and specificity 98.5% in both groups. Preserved the non-inferiority finding and rate-ratio interval.
- **Physician trial:** Added current published median diagnostic-reasoning scores per case of 76% with LLM access versus 74% with conventional resources alone. The separately administered standardized-prompt assessment scored 92%. Retained the adjusted difference of 2 percentage points and its interval. Independent review confirmed the observation unit and the distinction between access effects and standalone performance.
- Other Chapter 42 comparisons were retained: hypothetical rain losses/thresholds; matched-score health-need proxy comparison; prediction versus treatment benefit; medical-AI trust comparisons; workflow baseline and experiment design. No hypothetical benchmarks were presented as observed results.

## Source verification

- Supplied book: `/Users/huz/Library/CloudStorage/OneDrive-SyddanskUniversitet/Teaching/Data Driven Decision Making/Books/Power and Prediction - Ajay Agrawal.epub`, chapter 15, “The New Judges.” Approximate 80%, 15%, and 70% phase hit rates are explicitly reported. AUROC 0.95 is a different metric and was not substituted for hit rate.
- Webb, Abernethy, and Schwartz (2020), *Flint's Service Line Replacement Program, 2016–2019*, pp. 2–3: https://storage.googleapis.com/flint-storage-bucket/d4gx_2019%20%282%29.pdf. Defines the excavation hit-rate denominator, reports 0.15 for 2018, and plots the change and recovery.
- Stanford HAI, 2025 AI Index, chapter 1, inference costs: https://hai.stanford.edu/assets/files/hai_ai-index-report-2025_chapter1_final.pdf. Stanford's explanatory page also gives both prices: https://hai.stanford.edu/news/ai-index-2025-state-of-ai-in-10-charts. Used the stated dates, without repeating that page's inconsistent shorthand duration.
- Brynjolfsson, Li, and Raymond (2025), *Generative AI at Work*: https://academic.oup.com/qje/article/140/2/889/7990658. Existing published 15% average productivity result; clarified comparator only.
- Gommers et al. (2026), published trial abstract: https://pubmed.ncbi.nlm.nih.gov/41620232/. All paired quantities and non-inferiority result verified.
- Goh et al. (2024), current JAMA abstract/Table 2/“LLM Alone”: https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395. Current physician medians are 76/74, although some older accounts report different values. Standalone median remains 92.
- Bateson, Nettle, and Roberts (2006), original experiment already cited in Chapter 25/Appendix F: https://pmc.ncbi.nlm.nih.gov/articles/PMC1686213/. Same outcome and flower-image comparator; the rounded “nearly three times” result is retained.

## Other configured components

| Component | Disposition |
|---|---|
| Evidence-reading guide | Added a transparent hypothetical 10→12 versus 100→120 cases/hour example to explain why a 20% claim needs its baseline and units. The opening's deliberately incomplete training claim is retained because identifying its missing comparison is the exercise. |
| Appendix F | Matched the watched-eyes paragraph to Chapter 25: nearly three times the contributions per unit consumed in eye-image versus flower-image weeks. Replication rates/effect magnitudes, publication/null comparisons, and selection-simulation true/selected estimates already supply their benchmarks. |
| Appendix A | Hypothetical option scores, weights, and value thresholds define their alternatives. The unanchored 30% weight is intentionally presented as a problem for the reader to diagnose. Retained. |
| Appendix B | Formal/evolutionary alternatives and Schelling simulation before/after segregation rates already identify the comparisons. Retained. |
| Appendix C | Portable tools ask for reference classes, alternatives, criteria, and comparison plans; no isolated empirical performance numbers to repair. Retained. |
| Appendix D | Example index links to explanatory chapters; no standalone numerical argument. Retained. |
| Appendix E | Worked clinic example gives 380/600 versus 417/600, 63.3% versus 69.5%, and the 6.2-point difference. Other instructional comparisons identify groups/outcomes or deliberately ask students to diagnose missing information. Retained. |
| Seven Part introductions | Qualitative contrasts and named concepts, without isolated outcome rates needing new controls. Retained. |
| Preface, use guide, about | No unsupported performance comparison requiring amendment. Retained. |
| Concept index and references | Navigation/bibliographic material; retained. Reference synchronization check passed for 834 entries. |

## Skills and figure

Added one concise comparison rule to each of `huanren-writing-style`, `huanren-paper-style`, and `huanren-referee-style`. The rules require relevant controls/baselines and enough outcome, unit, population, and period information to interpret a result. They forbid inventing a benchmark. The general skill keeps essential contrasts in the main text and secondary methodological detail in footnotes. All prior skill content was preserved; frontmatter/schema screening passed with Ruby YAML. The skill-creator Python validation helper needs PyYAML, which is unavailable in the installed Python runtimes, so it was not claimed as run successfully.

Updated the watched-eyes SVG description and visible ratio label to name flower weeks and the contribution denominator. Regenerated the PNG using Sharp and inspected the rendered changed label for containment and legibility. This was a label repair, not a new book-wide layout audit. The browser-backed fallback helper failed to launch and produced no output; the final raster was rendered offline. Final HTML/EPUB asset and text parity checks are recorded in the release report; no live browser/EPUB-reader visual inspection is claimed.


---

# Comparative-evidence review: Chapters 1–15

Date: 2026-09-11. Scope: the 15 active canonical Chapter 1–15 QMDs listed in `sources.json`. Comparison baseline: `before/`. Read the current `huanren-writing-style` skill, including its new instruction to put a meaningful baseline beside an argumentative number or performance claim.

Reviewed numerical examples, research/performance claims, captions/alt text, and tables in context. Dates, sample sizes, enumerated steps, hypothetical decision parameters, and definitions were not treated as effects needing an invented comparison. Comparisons already visible in the immediate setup or accompanying figure were retained unless the argumentative result itself left a salient alternative unstated.

Result: six focused passage revisions in four chapters; 11 chapters retained. Net addition: 80 words. No general prose rewrite, new references, or new empirical sources were added to the book's reference blocks; the added empirical details were checked against works already cited there.

## Chapter dispositions

| Chapter | Disposition | Comparison examined and reason |
|---|---|---|
| 1 | Retained | Survival/mortality frames, decoy presence/removal, opt-in/opt-out/active choice, and message-by-emotional-state alternatives are explicit in their setups. The Google redesign paragraph identifies the design change and reports a qualitative uplift; the corporate report supplies no numerical magnitude to add. Mars's 1997 timing is descriptive chronology, with its existing source detail preserved. |
| 2 | Retained | The DVD example puts 75% in the ordinary-choice condition beside 55% with the opportunity-cost reminder, for the same sample and purchase. The 39-experiment synthesis explicitly compares its smaller effect with the original. The 82/78 job scores and undefined 30% criterion weight are hypothetical teaching quantities, not unsupported performance claims. |
| 3 | Revised | The 83% gorilla miss rate previously stood alone. Added that all 24 radiologists reported seeing the gorilla when shown its image afterward, making the search task versus subsequent image inspection visible. Sensory throughput/behavioral-rate estimates already identify the compared constructs; their footnote remains. Single versus divided attention supplies the performance comparison for the multitasking discussion. |
| 4 | Retained | Perceptual examples explicitly keep the symbol, light, line, or drawing constant while varying context; the Easter/October interpretation comparison and subsequent research are identified. Jennings's age and operation date are chronology. Newly sighted participants' initial difficulty and subsequent improvement are already contrasted. |
| 5 | Revised, three passages | (1) The 35% launch base rate now means the proportion of comparable launches reaching the table's retention target, avoiding confusion with a 35% user-retention rate. (2) The mindset intervention now reports its estimated 0.10 GPA-point advantage over controls, with the four-point scale, grade period, core-subject outcome, and lower-achieving population. The tenth-grade advanced-math follow-up explicitly reports 36% intervention versus 33% control across both achievement groups. (3) Pygmalion's greater gains now identify IQ as the outcome and classmates not singled out as the comparison. |
| 6 | Retained | Same-wine/different-price and blind-tasting conditions, regular versus discounted energy drink, scarcity conditions, and aroused versus neutral intertemporal choices already identify the alternatives. Sample sizes and the 123-country coverage are descriptive, not effect sizes. |
| 7 | Retained | Choice-blindness cases explicitly contrast the selected face with the substituted/rejected face. Dissonance and choice-spreading examples identify strong versus weak external justification and chosen versus rejected options. No isolated quantitative performance result required a baseline. |
| 8 | Retained | Bat-and-ball arithmetic fully specifies the two prices and their relation. Practice, feedback, and expertise claims identify their relevant conditions; Type 1/Type 2 are definitions, not performance estimates. |
| 9 | Retained | The assertiveness study puts six versus twelve retrieved examples beside the counterintuitive judgment difference. Face-based election prediction explicitly uses chance as its baseline; no accuracy percentage was claimed. Hypothetical ecological-return alternatives are already paired. |
| 10 | Retained | The 2–4–6 task contrasts rival rules and diagnostic/non-diagnostic triples. Mixed evidence, prior positions, labels, and role-assignment examples identify their comparison conditions. No standalone numeric performance claim required repair. |
| 11 | Retained | Anchor values 10 and 65 are explicitly compared. Subscription prices and decoy-choice counts place 84/16 beside 32/68, with the zero-choice decoy and group denominators visible. The Gandhi age is an anchor illustration. |
| 12 | Retained | Equivalent survival/mortality, lean/fat, employment, salary-reference, and disease-program quantities are fully paired. The Loftus figure gives the speed estimates and false-memory percentages with their wording/control groups. Treatment risk is shown as 2 per 1,000 versus 1 per 1,000, alongside relative and absolute changes. |
| 13 | Revised | The fictional review-system message now names the previous system as the baseline for faster reviews and clarifies employee understanding of the criteria as the second outcome. No fictional numerical result was invented. The separate fictional completion pilot already compares 62% with 74% over three months. Repeated/new statements and fluent/disfluent presentation provide the research alternatives. |
| 14 | Retained | Base-rate examples give the pools, sensitivity, false-positive rate, posterior, and changing prior with consistent denominators. The undefined “80 percent accurate” claim is deliberately diagnosed and then unpacked. The platform-success exercise intentionally asks readers to recover the missing denominator; supplying it would defeat the exercise. |
| 15 | Revised | The Monty Hall paragraph now places staying's 1/3 beside switching's 2/3 under the same host protocol; this value was already in the adjacent figure and alt text. Coin-sequence categories, sample-size/standard-error values, regression expectations, calibration bins, Brier outcomes, and model/reference-class predictions already include the needed comparisons. |

## Sources and number provenance

- **Chapter 3, Drew, Võ, and Wolfe (2013):** [Primary author manuscript, Results: Experiment 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC3964612/). Reports 20 of 24 radiologists not reporting the gorilla during the task and all 24 reporting it when subsequently shown Figure 1. The added second “24” repeats the same study sample for the distinct inspection context. No novice comparison was added; the main lesson concerns search and awareness rather than a ranking of professional competence.
- **Chapter 5, launch forecast:** The existing table defines success as at least 90% of paid users remaining active after 90 days, with a 45% forecast. The existing 35% reference-class rate was retained and its event definition aligned with that target. No new number or empirical claim.
- **Chapter 5, Yeager et al. (2019):** [Primary paper, Average effects on core course GPAs; Advanced mathematics course enrolment in tenth grade](https://pmc.ncbi.nlm.nih.gov/articles/PMC6786290/). The paper reports the adjusted core-GPA treatment advantage as 0.10 grade points for lower-achieving ninth-graders relative to controls; the GPA scale is four points. It reports advanced-math participation of 33% in control versus 36% in intervention for the full-cohort follow-up, rather than only the lower-achieving subgroup. These are the only newly supplied empirical effect/rate numbers in this pass. Existing statements about modest effects and school context remain.
- **Chapter 5, Rosenthal and Jacobson (1968):** [Original book, preface pp. vii–viii](https://gwern.net/doc/statistics/bias/1968-rosenthal-pygmalionintheclassroom.pdf). The authors identify IQ gains and the remaining children not singled out for teacher attention as the comparison. Added no effect size or sample count; retained the existing book citation and subsequent-review discussion.
- **Chapter 13:** Explicitly fictional message already present in the chapter. Added the previous-system comparator and clarified the outcome wording. No new number or factual claim about a real organization.
- **Chapter 15:** Staying's 1/3 is already specified in `fig-monty-hall-protocol` and follows directly from the unchanged standard host protocol. The Selvin (1975) citation is retained. The added inline `$1/3$` is the only mathematical change; no equation, probability rule, figure, or table was altered.
- **Chapter 1 source check, no edit:** [Google's December 2012 report](https://adsense.googleblog.com/2012/12/enhancing-text-ads-on-google-display.html) reports click uplift from experiments with the bundled design enhancements but supplies no percentage. No benchmark magnitude was manufactured.

## Verification

Re-read all six resulting passages against their surrounding argument and the pre-pass snapshot. `ch01-15-checks.json` records per-file comparison results and numerical additions. All 15 chapters preserve headings, explicit IDs, reference blocks, figure/caption/alt lines, Markdown/HTML tables, links, footnote definitions and markers, and display mathematics. Inline mathematics differs only by the deliberately added Monty Hall `$1/3$` comparator. Existing numerical values were not removed or changed. The four edited source files pass `git diff --check`.

Sources are frozen. No render, commit, push, asset, build-output, or skill changes were performed. No unresolved material scientific concern was introduced by these revisions.


---

# Chapters 16–29: comparative-evidence review, 2026-09-11

Reviewed numerical and performance claims in the current canonical QMDs, including the context immediately around them, figure captions/alt text and tables. The question was whether a result supporting the argument identifies its relevant baseline or alternative at the point of use, with the same outcome and interpretable units/context. Preserved earlier motivation and qualification edits.

**Outcome:** eight comparison issues corrected in seven chapters, across ten short passages (including one figure caption and its alt text). Net change: +88 words. Seven chapters required no source changes. No new references were needed; all repaired claims already cited the relevant primary studies. No assets, builds, skill files, commits or publishing actions were performed.

## Issues corrected

| Chapter / location | Gap | Correction and evidence |
|---|---|---|
| 17 / outbreak framing | The sentence compared selection of the sure option in one frame with selection of the risky option in the other, leaving readers to calculate the matched comparison. | Now compares sure-choice rates directly: 72% in the gain frame versus 22% in the loss frame; retains the reported 78% selecting the risky loss-frame option. The 22% is both reported by the original paper and the complement of the existing 78%. See source A. |
| 19 / future-self imagery | “Roughly twice” omitted actual allocations, total budget and the identity of the comparison group. | Study 1 now reports mean retirement allocations of $172 versus $80 from a hypothetical $1,000 windfall, comparing an older own-avatar with a current own-avatar. See source B. |
| 20 / theatre season tickets | Discounts were said to reduce attendance without explicitly naming the comparison. | Names full-price tickets as the baseline and preserves the first-half/later-half distinction. No numerical estimate added. Verified in the original experiment; see source C. |
| 20 / gasoline accounts | The correct income comparator was present, but “fifteen times more” made the ratio's wording ambiguous. | Uses “fifteen times as strongly … as” for the same approximate ratio. Conditions, baseline model, citation and numerical meaning are unchanged. |
| 22 / prosocial spending | “Positive effects” supplied neither the dependent outcome nor the comparison behavior. | Now specifies greater self-reported happiness at the end of the day for people assigned to spend on others versus those assigned to spend on themselves. No numerical estimate added. See source D. |
| 25 / watched eyes | The flower condition was described earlier, but the ratio sentence, caption and alt did not name it; “three times higher” was ambiguous. | All three now report contributions per unit consumed nearly three times as high in eye-image weeks as in flower-image weeks. Same rounded result and existing Bateson et al. (2006) citation. Root was notified that the SVG description and visible ratio label need matching language; root confirmed ownership of that update. |
| 26 / petrified wood | “Increased theft” had no visible alternative and could be read as a comparison with no sign. | Now compares the two actual signs: 7.92% of marked pieces stolen under the sign emphasizing visitors taking wood versus 1.67% under the sign asking visitors not to remove it. The unit is marked pieces, not visitors. See source E. |
| 27 / investor turnover | “Substantially lower” hid the scale of the performance comparison. | Now gives annualized net returns of 11.4% for the most active fifth of brokerage households versus 18.5% for the least active fifth, over February 1991–January 1997. See source F. |

## Primary-source verification

**A — Tversky and Kahneman (1981), p. 453, Problems 1 and 2.** The original displays 72% for Program A and 22% for Program C, with 78% for Program D. These are independent gain- and loss-frame samples answering equivalent outcome choices. [Original paper, Stanford copy](https://stanford.edu/class/psych205/papers/Tversky-Kahneman-1981.pdf).

**B — Hershfield et al. (2011), Study 1, pp. S26–S28.** The allocation task asks how a hypothetical $1,000 would be divided among four uses. The published results give mean retirement allocations of $172 for future-self exposure and $80 for current-self exposure. The book uses the rounded means printed in the article, not an inferred savings-account balance or actual retirement contribution. [Author-hosted published paper](https://www.dangoldstein.com/papers/Hershfield_Goldstein_et_al_Increasing_Saving_Behavior_Age_Progressed_Renderings_Future_Self.pdf).

**C — Arkes and Blumer (1985), Experiment 2, pp. 127–128.** Randomly ordered ticket types were full price ($15), a $2 discount and a $7 discount. In the first half of the season the full-price group used more tickets than either discount group; later group differences were not significant. These source amounts/results were inspected to verify the comparator; no new quantities were inserted into this book passage. [Original paper, university copy](https://cognition.aau.at/bg/BA/Arkes%20%26%20Blumer%201985.pdf).

**D — Dunn, Aknin and Norton (2008), p. 1688, randomized experiment.** Participants were assigned to spend on themselves or others and reported happiness later that day; the prosocial group reported higher post-spending happiness in the analysis controlling morning happiness. The revised sentence names the measured outcome and the alternative without introducing an unreported raw-scale effect size. [Author-hosted paper](https://dunn.psych.ubc.ca/wp-content/uploads/2010/12/spending-money-on-others-promotes-happiness.pdf).

**E — Cialdini et al. (2006), pp. 8–10, dependent variable, results and Figure 1.** The outcome was the fraction of planted, marked wood pieces stolen. The descriptive/strong-focus condition had 19 stolen out of 240, or 7.92%; the injunctive/strong-focus condition had 5 out of 300, or 1.67%. The comparison is between sign conditions, not against absence of a sign or percentage of visitors stealing. [Published paper hosted by the US Forest Service](https://research.fs.usda.gov/download/treesearch/45277.pdf).

**F — Barber and Odean (2000), pp. 774–775 and Figure 1.** Highest- and lowest-turnover quintiles have annualized geometric returns after bid–ask spread and commissions of 11.4% and 18.5%, respectively. The figure specifies February 1991 through January 1997 as the return period. Both groups use the same calculation and period. [Author-hosted published paper](https://faculty.haas.berkeley.edu/odean/Papers%20current%20versions/Individual_Investor_Performance_Final.pdf).

## Coverage and retained dispositions

| Chapter | Disposition of other consequential numerical/performance claims |
|---|---|
| 16 | Retained. Sure/risky options, entry fee and net value, certainty equivalent and risk premium, Allais pairs and Ellsberg bets all identify the alternatives. Risk communication already gives 2 versus 1 per 1,000 over one year plus relative and absolute changes. Project costs/payoffs and arithmetic-versus-compounded wealth provide their own benchmarks. Elicitation classifications are discussed across named methods. |
| 17 | Retained beyond framing edit. Value-function and weighting estimates are model parameters with the relevant benchmark explained nearby. Investment purchase/current prices and repeated-gamble comparisons are explicit. Replication counts describe tested items/contrasts; no artificial control rate was added. |
| 18 | Retained. Opening payoffs and expected values are paired; the probability of missing the rare gain has its sample size and outcome. Description/experience contrasts identify the information conditions. Pain-treatment communication explicitly compares a fact box with simulated experience. Historical sample periods and numbers of draws are not treatment-performance claims requiring invented controls. |
| 19 | Retained beyond imagery edit. Intertemporal payoffs, dates, hidden zeros, search paths and compounding examples expose the alternatives. Reliability precedes the marshmallow waiting comparison. Retraction and replication statements retain their study distinction; dates do not need comparators. |
| 20 | Retained beyond two short corrections. Travel savings compare equal amounts/time; mental-budget table names the prior-expense condition and controls. Winners sold versus losers retained has a 3.41-percentage-point difference with common market-adjusted outcome and one-year horizon. Hypothetical stock allocations are 40% versus 90% under named return-horizon displays. Taxi targets compare high- and low-wage days. |
| 21 | Retained. Fresh/stale popcorn and stronger/weaker habits are explicitly crossed in the prose. The 66-day median and 18–254-day range describe modeled time to 95% of the plateau; they are not an intervention's success rate requiring a control group. |
| 22 | Retained beyond spending edit. Income findings compare specified welfare measures, samples and later analyses; threshold dollars include the original period. California/Midwest predictions are compared with reported life satisfaction. No new “normal” mortality or happiness baseline was invented for association summaries. |
| 23 | Retained. Payoff matrices, best responses, coordination thresholds and bargaining outcomes give relevant alternatives. Market-rule applications describe planned comparisons without claiming unobserved performance. |
| 24 | Retained. The reasoning ladder, equilibrium and hypothetical opponent distribution are explicit. The fitted mean number of reasoning steps is a model parameter, not a comparative prediction-accuracy result. |
| 25 | Retained beyond ratio edit. Repeated-game thresholds are derived from defined payoffs. Ultimatum and dictator discussions identify game rules and historical study contexts; allocation-type percentages describe a common sample. Fairness bars contain the compared vignettes and percentages. Golden Balls jackpot size is descriptive stakes information; no invented laboratory control was attached to it. |
| 26 | Retained beyond park-sign edit. Hotel towel reuse names the environmental-appeal alternative; energy feedback distinguishes high/low users and approval-cue conditions. Cultural-market figure names independent-choice benchmarks. Mimicry figure and alt report all four action rates in actions/minute. Human/chimpanzee comparisons specify the relevant task and human comparison samples. |
| 27 | Retained beyond turnover edit. NASDAQ changes include start/peak/later levels and dates. Palm–3Com compares implied residual value with its valuation relation. Laboratory prices have an explicit expected-dividend benchmark. Trader-type proportions describe classifications rather than relative performance. Earnings-drift and anomaly comparisons name the return contrast/benchmark. |
| 28 | Retained. Bystander evidence contrasts believed presence of other witnesses, dangerous versus ambiguous settings and support availability. Milgram variants and Burger's different stopping protocol remain distinct. Counts of teams/participants are sample descriptors, not outcome rates. |
| 29 | Retained. The honor figure and alt provide control/insult cortisol changes for both measured regional groups: 42/79% and 39/33%, respectively; the design footnote remains. Other numbers label lenses, samples or hypothetical amounts, not missing comparative effect claims. |

## Verification and handoff

All revised passages were reread. Fifteen checks pass for each of the fourteen chapters: reconstruction from only the recorded changes; unchanged headings, mathematical expressions, citation parentheticals, footnote definitions/markers, IDs, crossreferences, links, div structure, table content/captions and full reference blocks; only the recorded watched-eyes caption/alt changed; no unresolved footnote markers. `git diff --check` passes for the assigned QMDs.

Detailed before/after records and source pointers: `ch16-29-edits.json`. Final checks, source hashes and chapter word deltas: `ch16-29-checks.json`. Starting snapshots: `ch16-29-before/`. QMD sources are frozen for the parent's render.


---

# Comparative-evidence review — Chapters 30–41

Completed 11 September 2026. Canonical QMD sources are frozen for rendering. This pass audited numerical/performance claims carrying the argument, including relevant prose, captions, alt text and tables. It did not add comparators to dates, sample sizes, fictional design choices or mathematical definitions. Fifteen targeted replacements in eight chapters add 174 words in total. The only added number is the original deception meta-analysis's 50% chance benchmark; all existing numbers remain.

Exact replacements: `ch30-41-changes.json`. Baselines: the twelve chapter QMD files saved directly in this audit directory before this pass. Reproducible preservation check: `validate-ch30-41.py`; results: `ch30-41-validation.json`.

## Chapter dispositions

| Chapter | Disposition and consequential comparisons | Word delta |
|---|---|---:|
| 30 — Persuasion | Revised photocopier result to name the no-reason request. Revised sequential-request evidence to compare the target request with making it alone. Retained synthetic fitted curves: observed data and future value already share units and context; pilot durations are proposed design choices. | +18 |
| 31 — Stories | Retained. Identifiable-person giving is already compared with statistical-need information. Transportation, coupling and comprehension claims are associations/mechanism evidence, not unbenchmarked numerical performance claims. No numerical comparison needed for the fictional Sara case. | 0 |
| 32 — Evidence-aligned message | Retained. The message examples and evidence-routing table are methodological/conceptual examples, not measured improvements with omitted controls. Their comparison questions and test conditions are already explicit. | 0 |
| 33 — Communication | Retained. Email/voice example puts expected accuracy (~78% sender/~90% receiver), actual email accuracy (56%) and actual voice accuracy (73.1%) together for the same task. Perspective-getting is explicitly compared with imagining another's perspective. Romantic-couple accuracy compares actual performance with chance and expected performance. | 0 |
| 34 — Connection and repair | Revised Aron experiment to specify immediate closeness after reciprocal disclosure versus comparable small-talk tasks. Retained question-asking differences, predicted versus experienced connection, experiences versus factual claims, and forgiveness workbook versus waitlist at two weeks. The 4,598 adults is sample size, not an effect. | +6 |
| 35 — Negotiation design | Revised Rackham/Carlisle behavior result to name the average-performing comparison group. Retained strategic definitions, hypothetical case, and context-dependent emotion/power mechanisms; these do not report an isolated numerical outcome. | +8 |
| 36 — Claiming value | Revised decreasing-concession evidence: counteroffers compared with constant or single-large concessions; interactive final-deal disadvantage compared specifically with a single concession. Retained all BATNA, reservation, target, surplus, ZOPA and package numbers: alternatives and monetary units are adjacent and explicit. | +17 |
| 37 — Creating value | Retained. Logrolling and Pareto examples expose the alternative packages directly. Historical monetary amounts in the Harrison case are descriptive amounts attached to their roles, not unsupported effect sizes. | 0 |
| 38 — Agreements | Revised MESO benefits to name single-package offers. Added 50% chance beside 54% truth/lie classification; retained 47% lies and 61% truths. Retained actual-versus-believed cue correlations in the figure and the direct-question omission/commission distinction. | +16 |
| 39 — Behavior design | Revised vaccination outcome and reminder-without-planning comparator; goal-attainment outcome and MCII control conditions; and the audiobook study's gift-certificate/exercise-encouragement control. Retained hypothetical savings percentages, example durations and workflow thresholds as explicit design examples. | +45 |
| 40 — Choice architecture | Revised automatic enrollment to name previous opt-in regime. Revised tax-notice and financial-aid intervention contrasts and the no-report household comparison for energy use. Retained the MPG example's common 100-mile trip and gallon outcomes, nudge-unit versus journal-study percentage-point effects (their different study collections are already identified), Google's bundled before/after redesign, and the vaccination reminder control. No unavailable Google effect size invented. | +42 |
| 41 — Decision hygiene | Revised reason-writing comparison to judges proceeding directly to judgment. Revised debriefing to name individual/team performance, before/no-debrief comparisons and standardized-difference units. Retained mechanical/statistical versus unaided judgment, checklist before/after hospitals, 70%-forecast calibration definition, and hypothetical journal's paired editing-time, correction and helpfulness outcomes/thresholds. | +22 |

## Source verification for additions

All added factual comparators are supported by the already-cited source. Reference entries and citation text were retained; the URLs below document the primary-source check rather than introduce a new bibliography.

1. **Ch30, reason-giving:** Langer, Blank & Chanowitz (1978), original paper text and table, [paper scan](https://www.scribd.com/document/536286679/copy-machine-study-ellen-langer). The low-cost request compared no reason, a placebic reason and a substantive reason. The revision adds no compliance percentages and retains the higher-cost change in pattern.
2. **Ch30, small initial request:** Freedman & Fraser (1966), original paper's performance and one-contact conditions, [primary paper hosted at MIT](https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Influence_Compliance/Freedman_Fraser_Foot-in-the-door.pdf). The revision specifies prior compliance, not mere exposure to a request.
3. **Ch30, rejected large request:** Cialdini et al. (1975), abstract and experiments explicitly compare rejection-then-moderation with asking solely for the smaller favor, [primary paper hosted at MIT](https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Influence_Compliance/Cialdini.et.al.Reciprocal.Concessions.Procedure.1975.article.pdf).
4. **Ch34, closeness:** Aron et al. (1997), Study 1/abstract: greater postinteraction closeness than comparable small-talk tasks, [publisher record](https://doi.org/10.1177/0146167297234003). “Immediate” identifies the measured outcome; this does not assert lasting relationships or a duration of benefit.
5. **Ch35, negotiation behavior:** Rackham & Carlisle (1978), primary paper explicitly compares skilled and average negotiators, [original paper scan](https://www.scribd.com/document/795244419/The-Effective-Negotiator-Part-I-Rackham-Neil); [indexed primary abstract](https://eric.ed.gov/?id=EJ215552). This remains observational, not a training-effect estimate.
6. **Ch36, concessions:** Tey et al. (2021), [publisher's study descriptions](https://doi.org/10.1016/j.obhdp.2021.05.003) and [institutional record](https://ink.library.smu.edu.sg/lkcsb_research/6735/). Study 1a: decreasing versus constant concessions; Study 1b adds the single-concession condition. Interactive Study 2 compares decreasing versus a single concession on final agreement. The prose does **not** imply that the final-deal comparison was against constant concessions. The seven-study total and target-protection finding are retained.
7. **Ch38, MESOs:** Leonardelli et al. (2019), primary abstract states six experiments comparing MESOs with a single package offer, [institutional paper](https://research-management.mq.edu.au/ws/portalfiles/portal/132609298/132287967.pdf) and [author institution record](https://www.kellogg.northwestern.edu/academics-research/research/detail/2019/multiple-equivalent-simultaneous-offers-reduce-the-negotiator-dilemma-how/). No new effect size added.
8. **Ch38, 50% benchmark — sole new number:** Bond & DePaulo (2006), p. 216 explicitly identifies guessing at 50% correct; p. 214 reports 54% overall, 47% for lies and 61% for truths. [Original published paper in released records](https://assets.aclu.org/live/uploads/document/foia/2006-Personality-and-Social-Psychology-Review-Accuracy-of-Deception-Judgements.pdf). The paper usually used equal truth/lie counts and its overall metric averaged the two classification accuracies. The addition is a chance benchmark, not an empirical control group's score or a claim about natural truth/lie prevalence.
9. **Ch39, planning:** Milkman et al. (2011), same reminder-without-planning comparison already explicitly documented in Chapter 40. The revision harmonizes the two locations and identifies vaccination among employees as the outcome/population. No new rate added.
10. **Ch39, MCII:** Wang et al. (2021), [primary article](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.565202/full), “Literature Search and Criteria for Inclusion”: controls received no treatment or the same additional behavior-change support without MCII. “Control conditions without the combined exercise” covers both designs. The claim remains modest average goal-attainment gains; no additional effect size or universal superiority claim.
11. **Ch39, temptation bundling:** Milkman, Minson & Volpp (2014), sections 2/3.2 and Appendix experiment flow, [author-hosted primary paper](https://faculty.wharton.upenn.edu/wp-content/uploads/2013/11/2013_Mgmt_Sci_2.pdf). Control participants received a bookstore gift certificate and were encouraged to exercise. The gym-only condition initially increased visits relative to this group. The manuscript retains “initially”; no 51%/29% numbers added.
12. **Ch40, default:** Madrian & Shea (2001), [primary publisher abstract](https://academic.oup.com/qje/article-abstract/116/4/1149/1903159?login=false). The same employer's prior enrollment required affirmative participation; automatic enrollment changed that default. The addition names the opt-in baseline without adding participation rates.
13. **Ch40, tax notices:** Bhargava & Manoli (2015), [author-hosted primary paper](https://www.cmu.edu/dietrich/sds/docs/bhargava/bhargava-aer-2015.pdf), pp. 3501/3507 (PDF pp. 13/19), complexity interventions and Table 5. The complex notice was based on the original IRS CP09/27 letter with information standardized; the simple notice produced more responses. The new text says “based on” rather than claiming the comparator was an unchanged original mailing. No rate added.
14. **Ch40, aid assistance:** Bettinger et al. (2012), [author-hosted primary paper](https://scholar.harvard.edu/files/btl/files/bettinger_long_et_al_2012_role_of_application_assistance_and_info_-_qje.pdf), p. 9: three arms distinguish assistance plus personalized information, personalized information alone, and a control receiving only a general-information brochure (also provided to treatment groups). The abstract reports gains for assistance/information and no improvement for information alone. The primary paper was verified through indexed text when direct opening failed. No enrollment or aid rate added.
15. **Ch40, home energy:** Allcott & Rogers (2014), [primary article](https://www.povertyactionlab.org/sites/default/files/research-paper/899%20Allcott%20and%20Rogers%20AER2014%20The%20Short-Run%20and%20Long-Run%20Effects%20of%20Behavioral%20Interventions.pdf), randomized report/no-report design and persistence analysis. The new text compares households assigned reports with no-report households and carries that difference into the statement about persistence. No conservation percentage added.
16. **Ch41, reason-writing:** Liu (2018), [author's primary abstract](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2912693). Study 1 compares writing reasons before judgment with proceeding directly to the decision-making stage; Study 2 finds a similar effect from a forced deliberation period. The text retains both comparisons and the induced-negative-feeling outcome.
17. **Ch41, debriefing:** Tannenbaum & Cerasoli (2013), [primary paper](https://cebma.org/assets/Uploads/Tannenbaum-Cerasoli.pdf), pp. 235–236 method and p. 239/Table 1 results. It pools **within-unit pre/post comparisons and between-group no-treatment comparisons** and restricts outcomes to performance. The result stays 46 independent samples, N=2,136 and average d=.67. “Before it or in no-debrief control groups” makes both comparison types explicit; “standardized difference” identifies d's units. It does not recast every sample as a randomized between-group study or convert d into a percentage improvement.

## Verification and remaining concerns

- Read the revised passages in their surrounding source context. Each addition names an outcome or comparison rather than inserting a generic caution paragraph.
- All headings, IDs, math expressions, reference blocks, footnote markers/definitions, links, figure/caption/alt lines, table lines and fenced-block boundaries match the pre-pass copies exactly.
- Replaying the fifteen logged replacements reproduces all twelve final chapter files exactly. No existing number was removed or changed; only “50” was added in Chapter 38.
- All footnote references resolve locally. No new references or footnotes were needed. No figure or table changes, builds, commits or pushes were performed.
- No unresolved substantive concern identified in the added comparisons. The debriefing and aid-study designs were checked specifically to prevent an incorrect control description.


---

# Independent review of Chapter 42 comparisons and writing-skill updates

Date: 2026-09-11. Read-only review against `/private/tmp/book-comparisons-20260911/before`, the supplied *Power and Prediction* extraction, and the current primary sources. No book or skill files were edited by this reviewer.

**Verdict: pass.** All newly supplied numerical contrasts match their cited sources. The chapter distinguishes successive field phases, a backtesting simulation, a randomized workflow evaluation, and a separate model-only assessment. I found no overstated causal conclusion in the revised comparisons.

**Minor precision issue resolved:** Recommended naming the Goh observation unit explicitly. Root changed the sentence to “Their median diagnostic-reasoning scores **per case** were…”, and I verified the change in the source. JAMA's reported medians are across scored cases, not medians of a single aggregated score for each physician. The values themselves were already correct. No outstanding recommendation remains.

## Findings and sources

| Comparison | Verdict and interpretation | Source checked |
|---|---|---|
| Flint, about 80% → 15% → about 70% | Pass. The supplied book's Chapter 15 reports these approximate rates in the original targeting, changed-priorities, and restored-targeting sequence. Webb's report defines the denominator as all excavations, confirms 0.15 for the whole of 2018, documents concentration on low-risk precincts, and reports recovery after model-based prioritization resumed. The new footnote correctly treats these as successive programme phases with different excavation locations and remaining stocks. It does not present the difference as a randomized treatment effect. | Supplied `/private/tmp/book-motivations/Power and Prediction - Ajay Agrawal.txt`, Chapter 15 and its note 2; [Webb, Abernethy, and Schwartz (2020), §§3–3.2 and Figures 2–3](https://storage.googleapis.com/flint-storage-bucket/d4gx_2019%20%282%29.pdf). |
| Flint, 18.8% unnecessary visits versus 2.0% | Pass. The paper explicitly labels the proposed value as a backtesting simulation against the actual 2016–17 procedure. Keeping this in a separate paragraph avoids conflating the simulation with the later field phases. “Could the search become more efficient still?” accurately motivates a further procedural improvement over the existing programme. | [Abernethy et al. (2018), §4.2.2, p. 9 of the PDF](https://arxiv.org/pdf/1806.10692). |
| Stanford, US$20 → US$0.07 per million tokens | Pass. Both prices and dates match the report's fixed MMLU performance threshold corresponding to GPT-3.5. The benchmark is identified in the main sentence; 20/0.07 is about 285.7, supporting “more than 280-fold.” These are inference prices, not a claim about total decision-system expenditure. The report's 3:1 weighting of input/output prices is secondary methodology and does not require an added main-text qualification. | [2025 AI Index, Chapter 1, p. 41, Inference Cost and Figure 1.3.22](https://hai.stanford.edu/assets/files/hai_ai-index-report-2025_chapter1_final.pdf). |
| Customer support, 15% more issues resolved per hour | Pass. The revised sentence names working without the assistant as the comparator and retains the staggered-rollout design. The final QJE article reports 5,172 agents and the 15% average increase. It is not described as a randomized trial. | [Brynjolfsson, Li, and Raymond (2025), abstract and study design](https://academic.oup.com/qje/article/140/2/889/7990658). |
| MASAI, 1.55 versus 1.76 per 1,000 women; 80.5% versus 73.8% sensitivity; 98.5% specificity in both | Pass. Intervention/control labels and denominators match the authors' current abstract. The ratio 0.88 and its 95% CI 0.65–1.18 are correct. The trial's prespecified non-inferiority margin was 20%; the chapter describes non-inferiority without turning the lower point estimate into evidence of a statistically established reduction in interval cancer. Sensitivity and specificity refer to the evaluated screening workflows, as the text states. The earlier workload result remains clearly separated as the 2023 interim analysis. | [Gommers et al. (2026), author abstract, Methods and Findings](https://pubmed.ncbi.nlm.nih.gov/41620232/); [Lång et al. (2023), clinical safety analysis](https://www.sciencedirect.com/science/article/pii/S147020452300298X). |
| Goh, physicians 76% versus 74%; model alone 92% | Pass; observation unit now explicit. The current JAMA abstract, Results, and Table 2 all give 76/74, with an adjusted difference of 2 percentage points and 95% CI −4 to 8. The model-only result is the median per-case score across three runs using a common zero-shot prompt, graded with the human outputs. The chapter correctly identifies this as a separate assessment, uses the same rubric, and retains the nonsignificant physician-access result. No reliance was placed on conflicting older news figures. | [Goh et al. (2024), Study Design, Table 2, and LLM Alone](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395). |

## Three writing skills

Read the current complete `SKILL.md` files for `huanren-writing-style`, `huanren-paper-style`, and `huanren-referee-style`.

- **General writing:** The new rule applies to argumentative numbers and performance claims across writing, identifies control/baseline/alternative/before-and-after comparisons, requires enough outcome/unit/population/period information, prohibits invented benchmarks, and explicitly keeps the essential comparison in the main text with secondary detail in a footnote.
- **Paper writing:** The rule places aligned comparisons at the point of use in prose, captions, and tables. It fits the existing evidence-and-identification guidance and does not require repetitive qualification paragraphs.
- **Referee writing:** The rule requires the reviewer to state the relevant comparator and identify an actual manuscript omission precisely. It is compatible with raising only supported concerns and avoids assuming that an isolated number establishes improvement.

All three additions are concise and consistent with the user's preference. None forces a comparator onto descriptive dates, sample sizes, or mathematical definitions, and none conflicts with the main-text-contrast/secondary-footnote approach.

## Reviewed source state

Chapter 42 SHA-256 after verifying the resolved observation-unit clarification: `249cbb1554c0e0723463249f4828b3414456b20137d480c4b59e5fd586f47975`.

Skill SHA-256 values: general writing `c240d9e459e2290c0d65a298867397b482ef44e432a7528cb4558dee9196931b`; paper `e3dd523aba1b6bde4fa32c1b448c49aa97a7ed580248b7719f841ca7fc3082fe`; referee `a071dc31c8478436d527c4283ac22b50c627fbf6209e1f337c5fa2a3e3f5691f`.

No browser/local-HTML inspection, render, build, commit, push, book mutation, or skill mutation was performed. This audit report is the only file created.
