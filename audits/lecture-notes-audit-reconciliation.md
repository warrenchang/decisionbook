# Lecture Notes audit reconciliation

**Status: PASS**

## Coverage

- Independent audit ledgers: 3
- Raw audit rows: 236
- Overlap rows reconciled: 7
- Unique source files represented: 229
- Source files missing from audits: 0
- Audit paths not present in the source folder: 0
- Verification errors: 0

Each unique source path appears once in the merged CSV. Overlapping assignments are reconciled without counting a file twice. Source files are verified against current byte size and SHA-256; the source directory is not modified.

## Input ledgers

- `/private/tmp/lecture-audit-foundations-risk.csv`
- `/private/tmp/lecture-audit-methods-happiness.csv`
- `/private/tmp/lecture-audit-strategy-finance.csv`

## Format counts

| Format | Files |
| --- | ---: |
| aux | 1 |
| bbl | 1 |
| blg | 1 |
| docx | 12 |
| gz | 1 |
| ini | 2 |
| jpg | 7 |
| log | 1 |
| nav | 1 |
| nlogo | 7 |
| none | 3 |
| out | 1 |
| pdf | 59 |
| png | 35 |
| pptx | 94 |
| snm | 1 |
| tex | 1 |
| toc | 1 |

## Source-group counts

| Source group | Files |
| --- | ---: |
| 01 Foundations — anatomy/predictive evaluation manuscripts | 5 |
| 01 Foundations — decision process | 4 |
| 01 Foundations — introduction to behavioral economics | 2 |
| 01 Foundations — neuroeconomics | 1 |
| 01 Foundations — neuroscience of judgment and decision | 4 |
| 01 Foundations — predictive processing, free energy, and active inference | 1 |
| 01 Foundations — predictive processing, free energy, and active inference \|\| ADDITIONAL AUDIT: Foundations and neuroscience / active inference | 1 |
| 01 Foundations — predictive processing, free energy, and active inference \|\| ADDITIONAL AUDIT: Top-level repaired active-inference assets | 3 |
| 01 Foundations — science of decision making | 3 |
| 01–02 Perception — optical illusions and indirect seeing | 3 |
| 02 Attention — selection, prediction, and expectation | 4 |
| 02 Biases — story protection and contextual judgment | 3 |
| 02 Context — cognitive ease and familiarity | 2 |
| 02 Heuristics and biases — combined lecture | 3 |
| 02 Heuristics — adaptive shortcuts | 2 |
| 02 Heuristics — two-process thinking | 5 |
| 03 Choice architecture and nudge | 6 |
| 03 Context — framing, priming, and contextual influence | 4 |
| 03 Habits and behavior design | 6 |
| 04 Probability judgment | 2 |
| 04 Probability judgment \|\| ADDITIONAL AUDIT: Root synthesis/Probability judgment | 1 |
| 04 Prospect theory and reference-dependent choice | 2 |
| 04 Prospect theory and reference-dependent choice \|\| ADDITIONAL AUDIT: Root synthesis/Prospect theory | 1 |
| 04 Risky decision making | 2 |
| 04 Risky decision making \|\| ADDITIONAL AUDIT: Root synthesis/Risky decision-making | 1 |
| 05/Cooperation and coordination | 2 |
| 05/Evolutionary game theory | 4 |
| 05/Evolutionary game theory/NetLogo models | 7 |
| 05/Evolutionary game theory/TeX build | 9 |
| 05/Evolutionary game theory/images | 44 |
| 05/Evolutionary game theory/research article | 2 |
| 05/Social preferences and norms | 6 |
| 05/Strategic interdependence | 6 |
| 05/Strategic interdependence and behavioral game theory | 3 |
| 06/Asset bubbles | 5 |
| 06/Behavioral finance and investment decisions | 6 |
| 06/Intertemporal choice | 3 |
| 06/Mental accounting | 5 |
| 06/Money and mind composite | 1 |
| 07/Decision from experience | 3 |
| 07/Market experiment | 1 |
| 07/Newsvendor/operations | 1 |
| 08 - Research Methods | 7 |
| 09 - Additional Topics | 1 |
| 09 - Additional Topics / ABT | 1 |
| 09 - Additional Topics / cooperation | 2 |
| 09 - Additional Topics / evolutionary game theory | 1 |
| 09 - Additional Topics / happiness and behavioral finance | 1 |
| 09 - Additional Topics / legacy decision theory | 1 |
| 09 - Additional Topics / negotiation extensions | 1 |
| 09 - Additional Topics / neuroscience and self-help | 1 |
| 09 - Additional Topics / risk elicitation and operations | 1 |
| 09 - Additional Topics / subjective well-being | 4 |
| DPN2026 lecture sequence | 7 |
| Lecture Notes root | 1 |
| Readings | 1 |
| Readings / AI, prediction, and complexity | 8 |
| Readings / instructor notes | 2 |
| Readings / priming and goal setting | 4 |
| Readings / research design and replication | 6 |

## Exact duplicate groups

- `a27184154813c22c9f59e7f75cd3311757125b058e3229160332a4bafcd863dd`
  - `03 - Context, Habits and Choice Architecture/00. Choice Architecture.pptx`
  - `BE06. Choice Architecture.pptx`
- `86f8bc5e09f78e4ac019508ca11245da576b139733d15e26f277157a1a5a0ce4`
  - `05 - Strategic and Social Decisions/11. Behavioral Game Theory.pptx`
  - `11. Behavioral Game Theory.pptx`
- `f3a98cb874b947aca17adc73a808c3559f5d91876411cacbb7c46591204c8881`
  - `05 - Strategic and Social Decisions/11. Strategic Interdependence.pptx`
  - `BE08. Strategic Interdependence.pptx`
- `48742da32a2ae8631e3e7d41bab6ffa2a285a48905ef2fa94779b52ebb0cac37`
  - `06 - Time, Money and Finance/14. Asset Bubbles.pptx`
  - `BE10. Asset Bubbles .pptx`
- `bb7623ee5d3fb0efffaee430b19057c29b6884527a36c5d2c4ca25ebff2f8c35`
  - `06 - Time, Money and Finance/15. Investment Decisions.pptx`
  - `BE09. Investment Decisions.pptx`
- `7ec30f77c8c4285a85bdc3ce4b0f800b62e7ac226a0a95e3d010370b8317966f`
  - `06 - Time, Money and Finance/19. Mental Acounting.pptx`
  - `BE07. Mental Acounting.pptx`

## Verification exceptions

None.

## Rights and integration rule

The audit records mixed and uncertain rights in many legacy slide assets. The book may link to an external video, reproduce public-domain or appropriately licensed material with attribution, or create an original diagram/table from verified facts or data. Cosmetic modification is not treated as a copyright workaround. Journal-result images and simulation screenshots are redrawn or independently regenerated only when their underlying values, model, parameters, and provenance can be verified.

## Exact-path ledger

The full twenty-field ledger is `audits/lecture-notes-coverage.csv`. The compact table below supports visual inspection; it does not replace the CSV.

| # | Source path | Format | Role | Recommended destination |
| ---: | --- | --- | --- | --- |
| 1 | `.DS_Store` | none | macOS administrative artifact | none |
| 2 | `01 - Foundations and Neuroscience/01. Introduction to Behavioral Economics.pdf` | pdf | flattened/print lecture export | Open the foundations part with decision process, then rational benchmark; retain a short boxed history/methods section in the rational-benchmark chapter and move model-science depth to an optional methods box. |
| 3 | `01 - Foundations and Neuroscience/01. Introduction to Behavioral Economics.pptx` | pptx | supporting lecture source | Open the foundations part with decision process, then rational benchmark; retain a short boxed history/methods section in the rational-benchmark chapter and move model-science depth to an optional methods box. |
| 4 | `01 - Foundations and Neuroscience/02. Anatomy of Decision-Making.pptx` | pptx | supporting lecture source | Integrate selectively across foundation/predictive/valuation chapters; use the five diagnostic questions as a reusable end-of-part tool. |
| 5 | `01 - Foundations and Neuroscience/02. Neuroscience of Decision-Making.pdf` | pdf | flattened/print lecture export | Place a short methods-and-claims box before constructed value; integrate distributed valuation into the valuation chapter, prediction error into habits, and mentalizing into communication/negotiation rather than creating a brain-region catalogue. |
| 6 | `01 - Foundations and Neuroscience/02. Science of Decision-Making.pdf` | pdf | flattened/print lecture export | Use as a cross-chapter synthesis after predictive mind and valuation; place formal free-energy material in an optional appendix/toolbox. |
| 7 | `01 - Foundations and Neuroscience/02. Science of Decision-Making.pptx` | pptx | supporting lecture source | Use as a cross-chapter synthesis after predictive mind and valuation; place formal free-energy material in an optional appendix/toolbox. |
| 8 | `01 - Foundations and Neuroscience/0x. Neuroscience of Decision-Making.pptx` | pptx | supporting lecture source | Place a short methods-and-claims box before constructed value; integrate distributed valuation into the valuation chapter, prediction error into habits, and mentalizing into communication/negotiation rather than creating a brain-region catalogue. |
| 9 | `01 - Foundations and Neuroscience/Active Inference  -  Repaired.pptx` | pptx | concise decision-making active-inference lecture \|\| ADDITIONAL AUDIT: canonical concise teaching deck | After chapter 06, add a bounded optional toolkit; integrate epistemic action into probability/decision hygiene and negotiation questions. \|\| ADDITIONAL AUDIT: chapters/06-the-predictive-mind.qmd plus a short application box in chapters/35-decision-hygiene.qmd |
| 10 | `01 - Foundations and Neuroscience/Anatomy of Decision 1.docx` | docx | long-form draft/reference manuscript | Integrate selectively across foundation/predictive/valuation chapters; use the five diagnostic questions as a reusable end-of-part tool. |
| 11 | `01 - Foundations and Neuroscience/Anatomy of Decision-Making.pdf` | pdf | flattened/print lecture export | Integrate selectively across foundation/predictive/valuation chapters; use the five diagnostic questions as a reusable end-of-part tool. |
| 12 | `01 - Foundations and Neuroscience/Anatomy of Decision.docx` | docx | long-form draft/reference manuscript | Integrate selectively across foundation/predictive/valuation chapters; use the five diagnostic questions as a reusable end-of-part tool. |
| 13 | `01 - Foundations and Neuroscience/Anatomy_of_Decision_Making_with_Predictive_Evaluation  -  Repaired.pptx` | pptx | repaired/generated editable teaching source | Integrate selectively across foundation/predictive/valuation chapters; use the five diagnostic questions as a reusable end-of-part tool. |
| 14 | `01 - Foundations and Neuroscience/Neuroeconomics.pptx` | pptx | supporting lecture source | Chapter 07 valuation, with a compact evidence-boundary box rather than a separate anatomy catalogue. |
| 15 | `01 - Foundations and Neuroscience/Science_of_Decision_Making_Updated_Lecture  -  Repaired.pptx` | pptx | repaired/generated editable teaching source | Use as a cross-chapter synthesis after predictive mind and valuation; place formal free-energy material in an optional appendix/toolbox. |
| 16 | `01 - Foundations and Neuroscience/The Predictive Brain in Behavioral Economics.docx` | docx | long-form draft/reference manuscript | After chapter 06, add a bounded optional toolkit; integrate epistemic action into probability/decision hygiene and negotiation questions. |
| 17 | `01 - Foundations and Neuroscience/You_Do_Not_See_the_World_Directly_Presentation  -  Repaired.pptx` | pptx | repaired/generated editable teaching source | Use 3–5 carefully redrawn, accessible demonstrations in chapter 06; move the remainder to an optional visual lab. |
| 18 | `01. Decision Making Process.pptx` | pptx | recent 26-slide synthesis; unsafe as citation authority | Chapters 01–03, followed by the narrator/decision-record material later; make the studio cumulative across those chapters. |
| 19 | `02 - Attention, Heuristics and Biases/02. Limited attention.pptx` | pptx | supporting lecture source | Attention → predictive mind → constructed value → expectation, before two-process thinking and heuristics. |
| 20 | `02 - Attention, Heuristics and Biases/03&04. Two systems of thinking.pdf` | pdf | flattened/print lecture export | After attention/prediction/expectation, then transition directly to ecological-fit heuristics. |
| 21 | `02 - Attention, Heuristics and Biases/03. Two systems of thinking.pdf` | pdf | flattened/print lecture export | After attention/prediction/expectation, then transition directly to ecological-fit heuristics. |
| 22 | `02 - Attention, Heuristics and Biases/03. Two systems of thinking.pptx` | pptx | supporting lecture source | After attention/prediction/expectation, then transition directly to ecological-fit heuristics. |
| 23 | `02 - Attention, Heuristics and Biases/04. Heuristics.pdf` | pdf | flattened/print lecture export | Chapter 09 general toolkit, then chapters 10–12 for the three major probability-related families. |
| 24 | `02 - Attention, Heuristics and Biases/04. Heuristics.pptx` | pptx | supporting lecture source | Chapter 09 general toolkit, then chapters 10–12 for the three major probability-related families. |
| 25 | `02 - Attention, Heuristics and Biases/04.1. Optical Illusions.pdf` | pdf | flattened/print lecture export | Use 3–5 carefully redrawn, accessible demonstrations in chapter 06; move the remainder to an optional visual lab. |
| 26 | `02 - Attention, Heuristics and Biases/04.1. Optical Illusions.pptx` | pptx | supporting lecture source | Use 3–5 carefully redrawn, accessible demonstrations in chapter 06; move the remainder to an optional visual lab. |
| 27 | `02 - Attention, Heuristics and Biases/05. Biases.pdf` | pdf | flattened/print lecture export | Chapters 13–17, with evidence-boundary boxes and an end-of-part debiasing/decision-hygiene bridge. |
| 28 | `02 - Attention, Heuristics and Biases/05. Biases.pptx` | pptx | supporting lecture source | Chapters 13–17, with evidence-boundary boxes and an end-of-part debiasing/decision-hygiene bridge. |
| 29 | `02 - Attention, Heuristics and Biases/07. Cognitive Ease.pdf` | pdf | flattened/print lecture export | Chapter 17 after framing and priming; retain a short communication/design application. |
| 30 | `02 - Attention, Heuristics and Biases/07. Cognitive Ease.pptx` | pptx | supporting lecture source | Chapter 17 after framing and priming; retain a short communication/design application. |
| 31 | `02. Neuroscience of Judgment.pptx` | pptx | 479-slide rasterized preservation/compilation archive | Place a short methods-and-claims box before constructed value; integrate distributed valuation into the valuation chapter, prediction error into habits, and mentalizing into communication/negotiation rather than creating a brain-region catalogue. |
| 32 | `03 - Context, Habits and Choice Architecture/00. Choice Architecture.pptx` | pptx | legacy visual-led source; exact-duplicate representative | Move the choice-architecture chapter directly after behavior design; keep governance/ethics as the culminating test. |
| 33 | `03 - Context, Habits and Choice Architecture/05. Habit and Behavior Design.pdf` | pdf | flattened/print lecture export | Habits → wanting/self-control → behavior design; immediately follow with choice architecture so individual and environmental design remain connected. |
| 34 | `03 - Context, Habits and Choice Architecture/06&07. Contextual Influence.pdf` | pdf | flattened/print lecture export | After prospect theory/reference dependence, then framing → priming → fluency, followed by narrator/habits. |
| 35 | `03 - Context, Habits and Choice Architecture/06&07. Contextual Influence.pptx` | pptx | supporting lecture source | After prospect theory/reference dependence, then framing → priming → fluency, followed by narrator/habits. |
| 36 | `03 - Context, Habits and Choice Architecture/06. Framing & Priming.pdf` | pdf | flattened/print lecture export | After prospect theory/reference dependence, then framing → priming → fluency, followed by narrator/habits. |
| 37 | `03 - Context, Habits and Choice Architecture/06. Framing & Priming.pptx` | pptx | supporting lecture source | After prospect theory/reference dependence, then framing → priming → fluency, followed by narrator/habits. |
| 38 | `03 - Context, Habits and Choice Architecture/06. Nudge and Choice Architecture.pdf` | pdf | flattened/print lecture export | Move the choice-architecture chapter directly after behavior design; keep governance/ethics as the culminating test. |
| 39 | `03 - Context, Habits and Choice Architecture/conscious_decisions_vs_habits  -  Repaired.pptx` | pptx | repaired/generated editable teaching source | Habits → wanting/self-control → behavior design; immediately follow with choice architecture so individual and environmental design remain connected. |
| 40 | `03. Two Systems of Thinking.pptx` | pptx | recent 26-slide synthesis; unsafe as citation authority | After attention/prediction/expectation, then transition directly to ecological-fit heuristics. |
| 41 | `04 - Risk, Probability and Prospect Theory/08. Probability Judgment.pdf` | pdf | flattened/print lecture export | After heuristics/biases, expand chapter 12 into two movements: intuitive probability failures, then representation/Bayes/calibration with worked problems and a forecast ledger. |
| 42 | `04 - Risk, Probability and Prospect Theory/08. Probability Judgment.pptx` | pptx | primary detailed legacy lecture deck | After heuristics/biases, expand chapter 12 into two movements: intuitive probability failures, then representation/Bayes/calibration with worked problems and a forecast ledger. |
| 43 | `04 - Risk, Probability and Prospect Theory/09. Risky Decision-Making.pdf` | pdf | flattened/print lecture export | Create a dedicated chapter immediately after probability judgment and before prospect theory: benchmark → measurement → paradoxes/ambiguity → communication and decision hygiene. |
| 44 | `04 - Risk, Probability and Prospect Theory/09. Risky Decision-Making.pptx` | pptx | primary detailed legacy lecture deck | Create a dedicated chapter immediately after probability judgment and before prospect theory: benchmark → measurement → paradoxes/ambiguity → communication and decision hygiene. |
| 45 | `04 - Risk, Probability and Prospect Theory/10. Prospect Theory.pdf` | pdf | flattened/print lecture export | Create a dedicated chapter after risky decision making and before framing/context; let framing then become an application of reference-dependent representation rather than the first exposure to it. |
| 46 | `04 - Risk, Probability and Prospect Theory/10. Prospect Theory.pptx` | pptx | primary detailed legacy lecture deck | Create a dedicated chapter after risky decision making and before framing/context; let framing then become an application of reference-dependent representation rather than the first exposure to it. |
| 47 | `04. Heuristics & Biases.pptx` | pptx | recent 26-slide synthesis; unsafe as citation authority | Two-process thinking → heuristics → affect/availability → resemblance/base rates → story-protecting biases → anchors/frames/priming/fluency. |
| 48 | `05 - Strategic and Social Decisions/11. Behavioral Game Theory.pdf` | pdf | student-facing PDF handout/export | New Part: Strategic and Social Decisions — Strategic Interdependence, then Behavioral Game Theory. |
| 49 | `05 - Strategic and Social Decisions/11. Behavioral Game Theory.pptx` | pptx | legacy editable lecture deck with speaker notes | New Part: Strategic and Social Decisions — Strategic Interdependence, then Behavioral Game Theory. |
| 50 | `05 - Strategic and Social Decisions/11. Strategic Interdependence.pdf` | pdf | student-facing PDF handout/export | chapters/46-strategic-interdependence.qmd in a new Strategic and Social Decisions Part. |
| 51 | `05 - Strategic and Social Decisions/11. Strategic Interdependence.pptx` | pptx | legacy editable lecture deck with speaker notes | chapters/46-strategic-interdependence.qmd in a new Strategic and Social Decisions Part. |
| 52 | `05 - Strategic and Social Decisions/12. Cooperation and Coordination.pdf` | pdf | student-facing PDF handout/export | chapters/48-cooperation-social-preferences.qmd, with one-shot, repeated, and evolutionary mechanisms explicitly separated. |
| 53 | `05 - Strategic and Social Decisions/12. Cooperation and Coordination.pptx` | pptx | legacy editable lecture deck with speaker notes | chapters/48-cooperation-social-preferences.qmd, with one-shot, repeated, and evolutionary mechanisms explicitly separated. |
| 54 | `05 - Strategic and Social Decisions/13. Social Norms.pdf` | pdf | student-facing PDF handout/export | Expand Chapter 23 and cross-reference chapters/48-cooperation-social-preferences.qmd; retain culture/identity applications in Chapter 37. |
| 55 | `05 - Strategic and Social Decisions/13. Social Norms.pptx` | pptx | legacy editable lecture deck with speaker notes | Expand Chapter 23 and cross-reference chapters/48-cooperation-social-preferences.qmd; retain culture/identity applications in Chapter 37. |
| 56 | `05 - Strategic and Social Decisions/13. Social Preferences and Social Norms.pdf` | pdf | combined composite PDF handout | Chapter 48 for social preferences/cooperation; Chapter 23 for expectation-based norms; Chapter 37 for culture/identity. |
| 57 | `05 - Strategic and Social Decisions/13. Social Preferences and Social Norms.pptx` | pptx | combined composite deck/handout | Chapter 48 for social preferences/cooperation; Chapter 23 for expectation-based norms; Chapter 37 for culture/identity. |
| 58 | `05 - Strategic and Social Decisions/13. Social Preferences.pdf` | pdf | student-facing PDF handout/export | chapters/48-cooperation-social-preferences.qmd after repeated games, before social norms/culture. |
| 59 | `05 - Strategic and Social Decisions/13. Social Preferences.pptx` | pptx | legacy editable lecture deck with speaker notes | chapters/48-cooperation-social-preferences.qmd after repeated games, before social norms/culture. |
| 60 | `05 - Strategic and Social Decisions/21. Evolutionary Game Theory.pptx` | pptx | legacy editable lecture deck with speaker notes | Advanced chapter or appendix in Strategic and Social Decisions, after one-shot and repeated games; keep evolutionary dynamics distinct from repeated-game reciprocity. |
| 61 | `05 - Strategic and Social Decisions/22. Evolution of Cooperation.pptx` | pptx | incomplete eight-slide lecture fragment | Short synthesis/box in the evolutionary-games chapter, verified against Nowak (2006) and later evidence. |
| 62 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/EvolutionaryGameTheory.aux` | aux | LaTeX build auxiliary | None; optional reproducibility archive only. |
| 63 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/EvolutionaryGameTheory.bbl` | bbl | generated bibliography | None; optional reproducibility archive only. |
| 64 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/EvolutionaryGameTheory.blg` | blg | BibTeX build log | None; optional reproducibility archive only. |
| 65 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/EvolutionaryGameTheory.log` | log | LaTeX compilation log | None; optional reproducibility archive only. |
| 66 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/EvolutionaryGameTheory.nav` | nav | Beamer navigation artifact | None; optional reproducibility archive only. |
| 67 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/EvolutionaryGameTheory.out` | out | PDF bookmark/navigation artifact | None; optional reproducibility archive only. |
| 68 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/EvolutionaryGameTheory.pdf` | pdf | compiled Beamer PDF derivative | Advanced chapter or appendix in Strategic and Social Decisions, after one-shot and repeated games; keep evolutionary dynamics distinct from repeated-game reciprocity. |
| 69 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/EvolutionaryGameTheory.snm` | snm | empty Beamer build artifact | None; optional reproducibility archive only. |
| 70 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/EvolutionaryGameTheory.synctex.gz` | gz | SyncTeX build artifact | None; optional reproducibility archive only. |
| 71 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/EvolutionaryGameTheory.tex` | tex | editable canonical TeX lecture source | Advanced chapter or appendix in Strategic and Social Decisions, after one-shot and repeated games; keep evolutionary dynamics distinct from repeated-game reciprocity. |
| 72 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/EvolutionaryGameTheory.toc` | toc | Beamer table-of-contents artifact | None; optional reproducibility archive only. |
| 73 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/NetLogo/2by2_game.nlogo` | nlogo | editable NetLogo model source | Advanced evolutionary-games chapter/appendix with independently implemented, versioned, seeded simulations and accessible charts. |
| 74 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/NetLogo/Ethnocentrism.nlogo` | nlogo | editable NetLogo model source | Advanced evolutionary-games chapter/appendix with independently implemented, versioned, seeded simulations and accessible charts. |
| 75 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/NetLogo/Segregation.nlogo` | nlogo | editable NetLogo model source | Advanced evolutionary-games chapter/appendix with independently implemented, versioned, seeded simulations and accessible charts. |
| 76 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/NetLogo/spatial_PD.nlogo` | nlogo | editable NetLogo model source | Advanced evolutionary-games chapter/appendix with independently implemented, versioned, seeded simulations and accessible charts. |
| 77 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/NetLogo/spatial_PD_10.nlogo` | nlogo | editable NetLogo model source | Advanced evolutionary-games chapter/appendix with independently implemented, versioned, seeded simulations and accessible charts. |
| 78 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/NetLogo/spatial_game.nlogo` | nlogo | editable NetLogo model source | Advanced evolutionary-games chapter/appendix with independently implemented, versioned, seeded simulations and accessible charts. |
| 79 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/NetLogo/spatial_game_10.nlogo` | nlogo | editable NetLogo model source | Advanced evolutionary-games chapter/appendix with independently implemented, versioned, seeded simulations and accessible charts. |
| 80 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/.picasa.ini` | ini | Picasa crop/rotation metadata | None. |
| 81 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/.picasaoriginals/.picasa.ini` | ini | Picasa crop/rotation metadata | None. |
| 82 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/.picasaoriginals/PD_200.png` | png | archived pre-crop original | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 83 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/.picasaoriginals/PD_initial.png` | png | archived pre-crop original | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 84 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/.picasaoriginals/schelling.jpg` | jpg | archived pre-crop original | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 85 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/1-s2.0-S0022519307001439-main.pdf` | pdf | copyrighted publisher article PDF | Repeated-versus-evolutionary cooperation box in the advanced strategy chapter. |
| 86 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/1-s2.0-S0022519307001439-main.png` | png | copyrighted publisher-article first-page raster | Repeated-versus-evolutionary cooperation box in the advanced strategy chapter. |
| 87 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/1.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 88 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/2.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 89 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/3.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 90 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/4.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 91 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/5.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 92 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/6.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 93 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/Evolution.jpg` | jpg | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 94 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/PD_100.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 95 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/PD_200i.jpg` | jpg | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 96 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/PD_50o.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 97 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/PD_initial.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 98 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/PD_initial0.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 99 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/PD_initial1.jpg` | jpg | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 100 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/RefereeReport.docx` | docx | blank Word artifact | None. |
| 101 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/beatles1.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 102 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/beatles2.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 103 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/beatles3.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 104 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/darwin.jpg` | jpg | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 105 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/darwin0.jpg` | jpg | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 106 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/ethnocentrism.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 107 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/ethnocentrism0.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 108 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/ethnocentrism_explanation.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 109 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/ethnocentrism_initial.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 110 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/ethnocentrism_initial0.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 111 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/giraffes.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 112 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/hawkdove1.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 113 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/hawkdove2.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 114 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/hawkdove3.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 115 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/neighbors.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 116 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/schelling.jpg` | jpg | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 117 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/segregation_equilibrium.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 118 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/segregation_initial.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 119 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/segregation_update1.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 120 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/staghunt1.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 121 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/staghunt2.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 122 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/staghunt3.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 123 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/staghunt4.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 124 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/strategy_dynamics.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 125 | `05 - Strategic and Social Decisions/Evolutionary Game Theory/img/strategy_dynamics0.png` | png | lecture image asset | Advanced evolutionary-games chapter/appendix, using a recreated accessible figure only. |
| 126 | `05. Habit and Behavior Design.pptx` | pptx | recent 26-slide synthesis; unsafe as citation authority | Habits → wanting/self-control → behavior design; immediately follow with choice architecture so individual and environmental design remain connected. |
| 127 | `06 - Time, Money and Finance/14. Asset Bubbles.pdf` | pdf | student-facing PDF handout/export | chapters/44-asset-bubbles.qmd after behavioral finance; retain a clear investor-level versus market-dynamics boundary. |
| 128 | `06 - Time, Money and Finance/14. Asset Bubbles.pptx` | pptx | legacy editable lecture deck with speaker notes | chapters/44-asset-bubbles.qmd after behavioral finance; retain a clear investor-level versus market-dynamics boundary. |
| 129 | `06 - Time, Money and Finance/15. Investment Decisions.pdf` | pdf | student-facing PDF handout/export | chapters/43-behavioral-finance.qmd; keep investor judgment/anomalies separate from market-level bubble dynamics. |
| 130 | `06 - Time, Money and Finance/15. Investment Decisions.pptx` | pptx | legacy editable lecture deck with speaker notes | chapters/43-behavioral-finance.qmd; keep investor judgment/anomalies separate from market-level bubble dynamics. |
| 131 | `06 - Time, Money and Finance/16. Intertemporal Decision-Making.pdf` | pdf | student-facing PDF handout/export | Expand chapters/38-intertemporal-choice.qmd; move extended peak-end/impact-bias material to Subjective Well-Being with a cross-reference. |
| 132 | `06 - Time, Money and Finance/16. Intertemporal Decision-Making.pptx` | pptx | legacy editable lecture deck with speaker notes | Expand chapters/38-intertemporal-choice.qmd; move extended peak-end/impact-bias material to Subjective Well-Being with a cross-reference. |
| 133 | `06 - Time, Money and Finance/19. Mental Acounting.pdf` | pdf | student-facing PDF handout/export | chapters/42-mental-accounting.qmd; explicitly distinguish mental-account coding/bracketing across decisions from prospect theory's model of a risky choice. |
| 134 | `06 - Time, Money and Finance/19. Mental Acounting.pptx` | pptx | legacy editable lecture deck with speaker notes | chapters/42-mental-accounting.qmd; explicitly distinguish mental-account coding/bracketing across decisions from prospect theory's model of a risky choice. |
| 135 | `06 - Time, Money and Finance/Money and the Mind.pptx` | pptx | legacy composite deck | Mine only unique notes/examples, then route to Chapters 42, 43, and 44. |
| 136 | `07 - Decision from Experience and Operations/0x. Market Experiment.pptx` | pptx | legacy editable lecture deck with speaker notes | Applied box in Behavioral Finance or Decision from Experience, or Appendix C on experimental evidence/market institutions. |
| 137 | `07 - Decision from Experience and Operations/20. Newsvendor problem.pdf` | pdf | PDF lecture source/handout | Applied operations box/appendix after Risky Decision-Making or Decision from Experience; do not make a full chapter unless operations is an explicit scope goal. |
| 138 | `07 - Decision from Experience and Operations/22. Decision making from expereience.pdf` | pdf | PDF lecture source/handout | chapters/41-decisions-from-experience.qmd after Prospect Theory; explicitly separate experienced sampling/feedback from stated-description probability weighting. |
| 139 | `07 - Decision from Experience and Operations/23. Decision from Experience.pptx` | pptx | legacy editable lecture deck with speaker notes | chapters/41-decisions-from-experience.qmd after Prospect Theory; explicitly separate experienced sampling/feedback from stated-description probability weighting. |
| 140 | `08 - Research Methods/17. Conduct Research in Behavioral Economics.pdf` | pdf | visible-slide PDF export / derivative | new appendix: How We Know—Research Design, Causal Inference, and Replication |
| 141 | `08 - Research Methods/17. Conduct Research in Behavioral Economics.pptx` | pptx | canonical editable methods deck | new appendix: How We Know—Research Design, Causal Inference, and Replication; keep a one-page gateway in chapters/35-decision-hygiene.qmd |
| 142 | `08 - Research Methods/18. Formulate Research Questions.pdf` | pdf | visible-slide PDF export / older derivative | new methods appendix section on empirical and literature-review questions; keep ABT material in chapters 26–27 |
| 143 | `08 - Research Methods/18. Formulate Research Questions.pptx` | pptx | canonical editable RQ/ABT deck | new methods appendix sections “From topic to answerable question” and “Empirical versus synthesis questions” |
| 144 | `08 - Research Methods/25. Threats in Running Experiments.pptx` | pptx | canonical editable threats-to-inference deck | new methods appendix: threats to identification, estimands, spillovers, reporting, and reproducibility |
| 145 | `08 - Research Methods/Formulate Research Questions - Thesis.pdf` | pdf | visible-slide PDF export / derivative | new methods appendix/student guide on answerable thesis and review questions |
| 146 | `08 - Research Methods/Formulate Research Questions - Thesis.pptx` | pptx | thesis-oriented variant / near-duplicate | new methods appendix/student guide |
| 147 | `08. Strategic Interdependence.pptx` | pptx | condensed root synthesis/index | chapters/46-strategic-interdependence.qmd in a new Strategic and Social Decisions Part. |
| 148 | `09 - Additional Topics/.DS_Store` | none | macOS administrative artifact | none |
| 149 | `09 - Additional Topics/20. Happiness.pptx` | pptx | mixed legacy deck | split: affective forecasting to chapter 45; finance and EMH/anomalies to chapter 43; bubbles to chapter 44 |
| 150 | `09 - Additional Topics/ABT.pdf` | pdf | legacy ABT handout | chapters 26–27 only |
| 151 | `09 - Additional Topics/Existing Additional Topics/146 Happiness.pdf` | pdf | canonical compact SWB teaching handout | chapters/45-subjective-well-being.qmd in Part V, with evidence versus reflection clearly separated |
| 152 | `09 - Additional Topics/Existing Additional Topics/16. Happiness_presentation.pdf` | pdf | older reveal-build presentation / duplicate | chapters/45-subjective-well-being.qmd |
| 153 | `09 - Additional Topics/Existing Additional Topics/16. SWB_WVS.pdf` | pdf | single-page copied results table | chapters/45-subjective-well-being.qmd |
| 154 | `09 - Additional Topics/Existing Additional Topics/16. SWB_contries.pdf` | pdf | single-page copied country table | chapters/45-subjective-well-being.qmd |
| 155 | `09 - Additional Topics/Existing Additional Topics/18. Cooperation.pdf` | pdf | canonical compact cooperation lecture | primarily chapters/48-cooperation-social-preferences.qmd; theory/setup to chapters 46–47 |
| 156 | `09 - Additional Topics/Existing Additional Topics/18. Cooperation_presentation.pdf` | pdf | older reveal-build presentation / duplicate | chapters/48-cooperation-social-preferences.qmd |
| 157 | `09 - Additional Topics/Existing Additional Topics/18. EvolutionaryGameTheory.pdf` | pdf | legacy theory lecture | chapters/46-strategic-interdependence.qmd and 47-behavioral-game-theory.qmd; optional technical appendix for dynamics/simulation |
| 158 | `09 - Additional Topics/Existing Additional Topics/Behavioral Decision Theory additional.pptx` | pptx | legacy comprehensive teaching compendium | selectively enrich chapters/12, 14, 39, 40, 42, and 43 plus appendices/appendix-a-portable-course-tools.qmd |
| 159 | `09 - Additional Topics/Existing Additional Topics/Newsvendor Experiment.pptx` | pptx | small experimental-results deck | chapters 39 and 41; risk-measure box in new methods appendix |
| 160 | `09 - Additional Topics/Existing Additional Topics/x. Additional Topics.pptx` | pptx | miscellaneous legacy deck | chapters 30, 32, and 34; optional mediation/arbitration box; outsider view remains chapter 35 |
| 161 | `09 - Additional Topics/Mind Magic.pptx` | pptx | mixed neuroscience/self-help deck | at most a short, source-verified network-neuroscience box in chapters 6–7; evidence-bounded well-being material to chapter 45 |
| 162 | `09. Behavioral Finance.pptx` | pptx | condensed root synthesis/index | chapters/43-behavioral-finance.qmd; keep investor judgment/anomalies separate from market-level bubble dynamics. |
| 163 | `11. Behavioral Game Theory.pptx` | pptx | byte-identical duplicate | New Part: Strategic and Social Decisions — Strategic Interdependence, then Behavioral Game Theory. |
| 164 | `11. Probability Judgment.pptx` | pptx | recent 26-slide synthesis; unsafe as citation authority \|\| ADDITIONAL AUDIT: condensed root synthesis/index | After heuristics/biases, expand chapter 12 into two movements: intuitive probability failures, then representation/Bayes/calibration with worked problems and a forecast ledger. \|\| ADDITIONAL AUDIT: Chapters 11-12; avoid creating a duplicate chapter. |
| 165 | `12. Risky Decision Making.pptx` | pptx | recent 26-slide synthesis; unsafe as citation authority \|\| ADDITIONAL AUDIT: condensed root synthesis/index | Create a dedicated chapter immediately after probability judgment and before prospect theory: benchmark → measurement → paradoxes/ambiguity → communication and decision hygiene. \|\| ADDITIONAL AUDIT: chapters/39-risky-decision-making.qmd after Probability Judgment. |
| 166 | `13. Prospect Theory.pptx` | pptx | recent 26-slide synthesis; unsafe as citation authority \|\| ADDITIONAL AUDIT: condensed root synthesis/index | Create a dedicated chapter after risky decision making and before framing/context; let framing then become an application of reference-dependent representation rather than the first exposure to it. \|\| ADDITIONAL AUDIT: chapters/40-prospect-theory.qmd; keep it distinct from mental accounting and from experience-based sampling. |
| 167 | `14. Intertemporal Decision Making.pptx` | pptx | condensed root synthesis/index | Expand chapters/38-intertemporal-choice.qmd; move extended peak-end/impact-bias material to Subjective Well-Being with a cross-reference. |
| 168 | `15. Decision from Experience.pptx` | pptx | condensed root synthesis/index | chapters/41-decisions-from-experience.qmd after Prospect Theory; explicitly separate experienced sampling/feedback from stated-description probability weighting. |
| 169 | `BE01. Decision Process - Complete 2h.pptx` | pptx | complete two-hour teaching version; enrichment source | Chapters 01–03, followed by the narrator/decision-record material later; make the studio cumulative across those chapters. |
| 170 | `BE01. Decision Process - Revised 2h.pptx` | pptx | revised two-hour teaching version; preferred scientific spine | Chapters 01–03, followed by the narrator/decision-record material later; make the studio cumulative across those chapters. |
| 171 | `BE01. Decision Process.pptx` | pptx | legacy long deck with hidden appendix | Chapters 01–03, followed by the narrator/decision-record material later; make the studio cumulative across those chapters. |
| 172 | `BE02. Attention, Prediction, and Expectation - Complete 2h.pptx` | pptx | complete two-hour teaching version; enrichment source | Attention → predictive mind → constructed value → expectation, before two-process thinking and heuristics. |
| 173 | `BE02. Attention_Prediction_Expectation.pptx` | pptx | legacy/integrated teaching version | Attention → predictive mind → constructed value → expectation, before two-process thinking and heuristics. |
| 174 | `BE02. Neuroscience of Decision Making - Revised 2h.pptx` | pptx | revised two-hour teaching version; preferred scientific spine | Place a short methods-and-claims box before constructed value; integrate distributed valuation into the valuation chapter, prediction error into habits, and mentalizing into communication/negotiation rather than creating a brain-region catalogue. |
| 175 | `BE03&04. Heuristics & Biases.pptx` | pptx | legacy/integrated teaching version | Two-process thinking → heuristics → affect/availability → resemblance/base rates → story-protecting biases → anchors/frames/priming/fluency. |
| 176 | `BE03. Limited Attention and Two-Process Thinking - Revised 2h.pptx` | pptx | revised two-hour teaching version; preferred scientific spine | Attention → predictive mind → constructed value → expectation, before two-process thinking and heuristics. |
| 177 | `BE03. Two Systems and Heuristics - Complete 2h.pptx` | pptx | complete two-hour teaching version; enrichment source | After attention/prediction/expectation, then transition directly to ecological-fit heuristics. |
| 178 | `BE04. Biases and Contextual Influence - Complete 2h.pptx` | pptx | complete two-hour teaching version; enrichment source | Chapters 13–17, with evidence-boundary boxes and an end-of-part debiasing/decision-hygiene bridge. |
| 179 | `BE04. Heuristics, Biases, and Contextual Influence - Revised 2h.pptx` | pptx | revised two-hour teaching version; preferred scientific spine | Two-process thinking → heuristics → affect/availability → resemblance/base rates → story-protecting biases → anchors/frames/priming/fluency. |
| 180 | `BE05. Habits and Behavior Design - Complete 2h.pptx` | pptx | complete two-hour teaching version; enrichment source | Habits → wanting/self-control → behavior design; immediately follow with choice architecture so individual and environmental design remain connected. |
| 181 | `BE05. Habits and Behavior Design - Revised 2h.pptx` | pptx | revised two-hour teaching version; preferred scientific spine | Habits → wanting/self-control → behavior design; immediately follow with choice architecture so individual and environmental design remain connected. |
| 182 | `BE05. Habits and Behavior Design.pptx` | pptx | legacy/draft teaching version | Habits → wanting/self-control → behavior design; immediately follow with choice architecture so individual and environmental design remain connected. |
| 183 | `BE06. Choice Architecture.pptx` | pptx | exact duplicate | Move the choice-architecture chapter directly after behavior design; keep governance/ethics as the culminating test. |
| 184 | `BE06. Nudge and Choice Architecture - Complete 2h.pptx` | pptx | complete two-hour teaching version; enrichment source | Move the choice-architecture chapter directly after behavior design; keep governance/ethics as the culminating test. |
| 185 | `BE06. Nudge and Choice Architecture - Revised 2h.pptx` | pptx | revised two-hour teaching version; preferred scientific spine | Move the choice-architecture chapter directly after behavior design; keep governance/ethics as the culminating test. |
| 186 | `BE06. Nudge and Choice Architecture.pptx` | pptx | legacy/draft teaching version | Move the choice-architecture chapter directly after behavior design; keep governance/ethics as the culminating test. |
| 187 | `BE07. Mental Accounting - Complete 2h.pptx` | pptx | modern comprehensive companion deck | chapters/42-mental-accounting.qmd; explicitly distinguish mental-account coding/bracketing across decisions from prospect theory's model of a risky choice. |
| 188 | `BE07. Mental Accounting - Revised 2h.pptx` | pptx | modern revised canonical teaching deck | chapters/42-mental-accounting.qmd; explicitly distinguish mental-account coding/bracketing across decisions from prospect theory's model of a risky choice. |
| 189 | `BE07. Mental Acounting.pptx` | pptx | byte-identical duplicate | chapters/42-mental-accounting.qmd; explicitly distinguish mental-account coding/bracketing across decisions from prospect theory's model of a risky choice. |
| 190 | `BE08. Strategic Interdependence - Complete 2h.pptx` | pptx | modern comprehensive companion deck | chapters/46-strategic-interdependence.qmd in a new Strategic and Social Decisions Part. |
| 191 | `BE08. Strategic Interdependence - Revised 2h.pptx` | pptx | modern revised canonical teaching deck | chapters/46-strategic-interdependence.qmd in a new Strategic and Social Decisions Part. |
| 192 | `BE08. Strategic Interdependence.pptx` | pptx | byte-identical duplicate | chapters/46-strategic-interdependence.qmd in a new Strategic and Social Decisions Part. |
| 193 | `BE09. Behavioral Finance and Investment Decisions - Complete 2h.pptx` | pptx | modern comprehensive companion deck | chapters/43-behavioral-finance.qmd; keep investor judgment/anomalies separate from market-level bubble dynamics. |
| 194 | `BE09. Behavioral Finance and Investment Decisions - Revised 2h.pptx` | pptx | modern revised canonical teaching deck | chapters/43-behavioral-finance.qmd; keep investor judgment/anomalies separate from market-level bubble dynamics. |
| 195 | `BE09. Investment Decisions.pptx` | pptx | byte-identical duplicate | chapters/43-behavioral-finance.qmd; keep investor judgment/anomalies separate from market-level bubble dynamics. |
| 196 | `BE10. Asset Bubbles - Complete 2h.pptx` | pptx | modern comprehensive companion deck | chapters/44-asset-bubbles.qmd after behavioral finance; retain a clear investor-level versus market-dynamics boundary. |
| 197 | `BE10. Asset Bubbles - Revised 2h.pptx` | pptx | modern revised canonical teaching deck | chapters/44-asset-bubbles.qmd after behavioral finance; retain a clear investor-level versus market-dynamics boundary. |
| 198 | `BE10. Asset Bubbles .pptx` | pptx | byte-identical duplicate | chapters/44-asset-bubbles.qmd after behavioral finance; retain a clear investor-level versus market-dynamics boundary. |
| 199 | `DPN2026/DPN01. Decision Process.pdf` | pdf | authoritative current lecture handout | same current chapters; use as sequence/voice QA source |
| 200 | `DPN2026/DPN02. Attention_Prediction_Expectation.pdf` | pdf | authoritative current lecture handout | same chapters, especially active-inference refinements in chapter 6 |
| 201 | `DPN2026/DPN03. Heuristics & Biases.pdf` | pdf | authoritative current lecture handout | same chapters; activity/index cross-links in appendices A–B |
| 202 | `DPN2026/DPN04. Influence & Persuasion.pdf` | pdf | authoritative current lecture handout | same chapters; use as voice and example sequence authority |
| 203 | `DPN2026/DPN05. Distributive Negotiation.pdf` | pdf | authoritative current lecture handout | Part VIII Negotiation (already combines distributive and integrative material) |
| 204 | `DPN2026/DPN06. Integrative Negotiation.pdf` | pdf | authoritative current lecture handout | Part VIII Negotiation plus chapter 37; combine distributive/integrative in one Part as already configured |
| 205 | `DPN2026/DPN07. Communication & Connection.pdf` | pdf | authoritative current lecture handout | same Part IX chapters and appendix tools |
| 206 | `Editable_Active_Inference_Diagram_with_Icons  -  Repaired.pptx` | pptx | single-slide native editable diagram asset \|\| ADDITIONAL AUDIT: single-slide editable source asset | After chapter 06, add a bounded optional toolkit; integrate epistemic action into probability/decision hygiene and negotiation questions. \|\| ADDITIONAL AUDIT: chapters/06-the-predictive-mind.qmd |
| 207 | `FEP_Active_Inference_Behavioral_Economics_Lecture  -  Repaired.pptx` | pptx | broad applied active-inference variant \|\| ADDITIONAL AUDIT: broad alternative teaching deck | After chapter 06, add a bounded optional toolkit; integrate epistemic action into probability/decision hygiene and negotiation questions. \|\| ADDITIONAL AUDIT: chapter 6 only, using the technically more precise 24-slide variant as conceptual authority |
| 208 | `FEP_Active_Inference_Behavioral_Economics_Lecture(1)  -  Repaired.pptx` | pptx | advanced mathematical active-inference variant \|\| ADDITIONAL AUDIT: technically precise alternative deck | After chapter 06, add a bounded optional toolkit; integrate epistemic action into probability/decision hygiene and negotiation questions. \|\| ADDITIONAL AUDIT: chapters/06-the-predictive-mind.qmd; optional equation-light advanced box |
| 209 | `Readings/.DS_Store` | none | macOS administrative artifact | none |
| 210 | `Readings/01 - AI, Prediction and Complexity/AI and Behavioral Economics.pdf` | pdf | published scholarly chapter | short AI prediction/judgment box in chapters/01 or 35; research-method implications in new methods appendix |
| 211 | `Readings/01 - AI, Prediction and Complexity/Impact of ML on economics.pdf` | pdf | published scholarly chapter | new methods appendix section “Prediction is not identification” and a short decision-hygiene box |
| 212 | `Readings/01 - AI, Prediction and Complexity/Impact_ML_on_Econ_Summary.pptx` | pptx | derivative summary deck | new methods appendix |
| 213 | `Readings/01 - AI, Prediction and Complexity/Prediction Judgment and Complexity.pdf` | pdf | published scholarly chapter | chapters/01-the-choice-is-the-tip-of-the-iceberg.qmd and 35-decision-hygiene.qmd |
| 214 | `Readings/01 - AI, Prediction and Complexity/Prediction_Judgment_Complexity_Summary.pptx` | pptx | derivative summary deck | chapters 1 and 35 |
| 215 | `Readings/01 - AI, Prediction and Complexity/The economics of artificial intelligence an agenda.pdf` | pdf | copyrighted edited volume / source repository | use chapters 3, 21, and 24 at the destinations specified in their individual rows |
| 216 | `Readings/01 - AI, Prediction and Complexity/__From Perception to Choice_ Understanding the Dimensions of Decision Making__.docx` | docx | synthetic derivative reading / source-discovery aid | use only as a checklist for perception → choice → uncertainty → time → self/others → intelligence continuity |
| 217 | `Readings/01 - AI, Prediction and Complexity/__From Perception to Choice_ Understanding the Dimensions of Decision Making__.pdf` | pdf | rendered duplicate of synthetic DOCX | none beyond checklist use |
| 218 | `Readings/02 - Research Design and Replication/Choosing the Right Research Question in Behavioral Economics.docx` | docx | synthetic student guide | new methods appendix/student guide: From topic to answerable question |
| 219 | `Readings/02 - Research Design and Replication/Choosing the Right Research Question in Behavioral Economics.pdf` | pdf | rendered duplicate of synthetic DOCX | new methods appendix/student guide |
| 220 | `Readings/02 - Research Design and Replication/Experimental Studies and Replication Failures Across Disciplines.docx` | docx | synthetic replication-crisis survey / lead list | new methods appendix: replication, power, publication bias, protocol heterogeneity, and claim calibration |
| 221 | `Readings/02 - Research Design and Replication/Experimental Studies and Replication Failures Across Disciplines.pdf` | pdf | rendered duplicate of synthetic DOCX | new methods appendix |
| 222 | `Readings/02 - Research Design and Replication/Formulating a Strong Research Question for a Behavioral Economics Literature Review.docx` | docx | synthetic student guide | new methods appendix/student guide: designing an evidence-synthesis question |
| 223 | `Readings/02 - Research Design and Replication/Formulating a Strong Research Question for a Behavioral Economics Literature Review.pdf` | pdf | rendered duplicate of synthetic DOCX | new methods appendix/student guide |
| 224 | `Readings/03 - Priming and Goal Setting/Chapter – Goal Setting and Priming Effects on Behavior.docx` | docx | synthetic literature chapter | chapter 16, one bounded subsection on goal activation, relevance, and timing |
| 225 | `Readings/03 - Priming and Goal Setting/Chapter – Goal Setting and Priming Effects on Behavior.pdf` | pdf | rendered duplicate of synthetic DOCX | chapter 16 only if a nuance is missing |
| 226 | `Readings/03 - Priming and Goal Setting/Priming, Subliminal Messaging, and Positive Thinking_ A Scientific Review and the Replication Crisis.docx` | docx | synthetic replication-aware review / lead list | chapters 16–17; methods appendix only for a replication case box |
| 227 | `Readings/03 - Priming and Goal Setting/Priming, Subliminal Messaging, and Positive Thinking_ A Scientific Review and the Replication Crisis.pdf` | pdf | rendered duplicate of synthetic DOCX | chapters 16–17/methods case box |
| 228 | `Readings/Instructor Notes/Literature.docx` | docx | minimal bibliography note | chapter 14 bibliography |
| 229 | `Readings/Instructor Notes/Replication Crisis References.docx` | docx | bibliographic lead list / rough notes | new methods appendix: a small set of carefully verified replication case studies |

## Disposition summary

- 31: Recreate as a clean, book-native chart/schematic from the stated model/equations; cite the model/source and do not treat the screenshot as empirical data.
- 18: Integrate distinctive, verified concepts/examples; preserve source unchanged.
- 17: Use for page-level visual/order comparison only; prefer editable PPTX or verified modern deck for integration.
- 12: Mine speaker notes, classroom sequence, activities, and unique examples; de-duplicate against root/modern variants and use current revised sources for final claim wording.
- 11: Use to verify visible student sequence and page grouping; ingest concepts from the editable PPTX/modern revised deck and primary sources, not from rasterized journal figures.
- 7: Use as a behavioral specification and provenance source; do not directly redistribute in the book unless the CC BY-NC-SA/commercial-license implications are accepted. Reimplement and validate for publishable figures.
- 6: Replace; do not publish this asset without provenance and permission/license verification.
- 6: Mine richer examples, activities, and citations; use revised version where scientific calibration conflicts.
- 6: Use as the primary teaching spine, supplemented by distinctive verified material from the complete version.
- 5: Exclude from conceptual ingestion after hash-based de-duplication; retain only if the folder structure requires an archival copy.
- 4: Content is readable; compare against underlying legacy/source deck and validate references before integration.
- 4: Use only as a high-level teaching outline after repairing notes and source attributions; validate every claim against originals.
- 4: Exclude.
- 4: Use as a topic checklist and proposed flow only; several slide-level provenance labels/source mappings are unreliable, so do not use it as empirical or bibliographic authority.
- 4: Mine unique examples, activities, notes, and figures; use the Revised deck for the current teaching arc and scientific qualifiers.
- 4: Primary teaching-flow and claim-framing source for the chapter; cross-check every empirical quantity/citation against the cited primary source and mine the Complete deck for omitted examples.
- 3: Mine distinctive prose, synthesis, and DOI bibliography; do not merge wholesale or treat draft statements as verified evidence.
- 3: Primary evidence inventory for examples and progression; verify quantitative claims/citations and redraw rights-sensitive figures.
- 3: Use only as a high-level teaching outline after repairing notes and source attributions; validate every claim against originals. || ADDITIONAL AUDIT: Use as a topic checklist and proposed flow only; several slide-level provenance labels/source mappings are unreliable, so do not use it as empirical or bibliographic authority.
- 2: omit/delete only if the user later authorizes cleanup
- 2: Use only for transitions and any unique combined framing; ingest substantive content from the two component decks to avoid double-counting.
- 2: Exclude; retain only for build provenance.
- 2: Exclude from book ingestion; retain only with the archival image source tree if preservation is desired.
- 2: Exclude from direct book use; superseded/cropped derivative exists. Retain only as source provenance if the lecture archive is preserved.
- 2: use DOCX as lead list; no independent incorporation
- 1: Integrate distinctive, verified concepts/examples; preserve source unchanged. || ADDITIONAL AUDIT: incorporate selectively and redraw natively
- 1: Archive/audit aid only; integrate from editable originals, not from 458 raster slide images.
- 1: Use as the representative copy for content audit; preserve the second path only in the ledger.
- 1: Use only as a pointer to the intended five-rules/kin-selection topic; rebuild from primary literature.
- 1: Retain only in a reproducibility archive; exclude from book ingestion.
- 1: Use to cross-check citations against the TeX, then exclude from prose ingestion as a generated derivative.
- 1: Use to verify the TeX-rendered lecture sequence; ingest equations, structure, and citations from the editable TeX and do not reuse mixed-rights raster assets.
- 1: Exclude; retain only if rebuilding/debugging the TeX project.
- 1: Primary editable authority for equations, payoff matrices, sequence, and citations; retain and mine fully. Rebuild diagrams natively and verify claims against primary sources.
- 1: Exclude as a generated derivative.
- 1: Cite and summarize within copyright limits; exclude the PDF and its figures from the book package.
- 1: Exclude this redundant copyrighted raster from the book package; use the article citation and an independently designed schematic.
- 1: Redraw as a clean accessible SVG explaining same-group/out-group strategies.
- 1: Redraw as accessible SVG with four- and eight-neighbor states clearly distinguished.
- 1: Mine only unique speaker notes/examples, then split them across Mental Accounting, Behavioral Finance, and Asset Bubbles; do not preserve the composite structure.
- 1: use the PPTX as canonical; retain this PDF only as a visual/render check
- 1: incorporate comprehensively but update and bound claims
- 1: use PPTX as canonical; merge only missing RQ guidance
- 1: incorporate RQ logic; deduplicate ABT against chapters 26–27
- 1: incorporate comprehensively with technical review
- 1: use editable PPTX as canonical; no separate book treatment
- 1: merge only thesis-specific material into the main RQ appendix section
- 1: split and rebuild; do not preserve the deck as one chapter
- 1: retain as provenance; add no separate chapter
- 1: incorporate comprehensively after evidence update
- 1: use 146 Happiness.pdf as canonical and discard this from synthesis
- 1: reconstruct from authoritative WVS data or omit
- 1: reconstruct from source data or omit
- 1: incorporate with a current evidence review
- 1: use 18. Cooperation.pdf as canonical
- 1: incorporate core intuition; place equations/simulation details in an optional box or appendix
- 1: mine unique activities and examples; do not import wholesale
- 1: incorporate task concepts only; omit unidentified local results and Raven items
- 1: incorporate AIM/deadline/third-party distinctions selectively; omit admin and stereotypes
- 1: salvage cautious network/value material; omit manifestation and genomic-well-being claims
- 1: Do not integrate twice; retain only as a provenance/path duplicate.
- 1: retain as authoritative progression; reconcile any example-level omissions only
- 1: retain sequence; add only missing conceptual distinctions
- 1: retain progression; update evidence and visual rights
- 1: retain progression; audit each visual and quotation before reuse
- 1: retain as authoritative sequence; reconcile examples/qualifiers
- 1: retain progression; add only missing mediation/arbitration and process details; replace visuals
- 1: retain as authoritative sequence; verify quantitative claims and rights
- 1: Reuse/redraw as an editable conceptual figure after checking labels and accessibility. || ADDITIONAL AUDIT: reuse the conceptual topology, not the slide screenshot
- 1: Optional advanced toolkit; keep applications explicitly hypothetical/testable. || ADDITIONAL AUDIT: use as idea inventory, not as independent evidence
- 1: Optional advanced toolkit; keep applications explicitly hypothetical/testable. || ADDITIONAL AUDIT: incorporate key distinctions and one application; avoid importing full formalism
- 1: omit/delete only if later authorized
- 1: synthesize and cite; no direct reproduction
- 1: synthesize selectively; update methods literature
- 1: use the published chapter, not this summary, as source authority
- 1: incorporate as a concise bridge: prediction does not decide
- 1: use the published chapter as source authority
- 1: cite selectively; do not attempt exhaustive incorporation of this external volume
- 1: source discovery only
- 1: use DOCX only for searchable source discovery
- 1: use as checklist; verify examples against primary evidence
- 1: use DOCX for search; no independent incorporation
- 1: source-discovery lead list only; verify each case
- 1: incorporate concise verified guidance; omit rubric/admin text
- 1: use DOCX as canonical text source; no separate incorporation
- 1: mine moderation ideas only; verify via primary/meta-analytic evidence
- 1: use DOCX for source discovery; no independent incorporation
- 1: use as source map, not as prose authority
- 1: verify bibliography entries; otherwise no prose to add
- 1: use as lead list only
