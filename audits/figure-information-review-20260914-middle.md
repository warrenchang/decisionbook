# Figure information review — middle set (14 September 2026)

## Scope and result

All 39 owned, currently used SVG illustrations were reviewed for whether a reader can identify the central contrast, follow the mechanism, and interpret the conditions or quantities without chapter prose. Nineteen were revised; twenty passed without further source changes. This semantic pass is separate from the earlier removal of redundant text.

Conventional terms, short task instructions, and measurement boundaries were restored where they perform essential explanatory work. Generic titles and repeated summary slogans were not restored. Numerical values, sources, simulation parameters, plotted relationships, and causal connectors were preserved. No QMD, generators, final PNGs, builds, or Git state were edited by this reviewer.

## Verification

Every figure was inspected individually at its native SVG pixel dimensions and on four contact sheets. The 39 SVG files parse; identifiers are unique within each file; the Chrome text-bounds screen found zero elements outside their viewBoxes. Equivalent line geometry in the Asch task is available in the alternative description, with no visible answer banner. The two regression annotations have a pale outline so the unchanged guide line does not interfere with their letters. Final HTML/EPUB placement, phone rendering, and production fallback regeneration remain root responsibilities.

Baseline: `/tmp/figure-information-review-20260914/before/`. Detailed machine-readable results: `/tmp/figure-information-review-20260914/middle-results.json`. Native PNG proofs: `/tmp/figure-information-review-20260914/native-*.png`.

## Caption and alternative-text followups

- Chapter 20: describe the investment bars as **median hypothetical stock allocations**, matching the visible axis and existing caption. Reported to root.
- Chapter 26: keep the Asch social-pressure task in alternative text, together with the line-length information needed for equivalent nonvisual access. Root confirms this treatment. Music Lab alternative text now identifies shown versus hidden download counts.
- The remaining changed labels clarify the same relationships already described by their captions/alternative text; no additional substantive QMD change is necessary.

## Figure ledger

### 1. regression-conditional-shrinkage.svg — REVISED

Purpose: Explain regression toward a conditional mean while retaining the extreme observation and model.

Name regression to the mean beside the worked prediction, making the conventional concept identifiable without an external title. A pale text outline prevents the unchanged vertical prediction guide from crossing the annotation letters.

Native inspection: 900 × 615 pixels. ViewBox: `0 85 900 615` → `0 85 900 615`.

Label changes:

- Added: Regression to the mean

Verification: native view and contact sheet passed; no text-bounds flag.

### 2. monty-hall-protocol.svg — PASS

Purpose: Explain why switching has a two-thirds winning probability under a specified host protocol.

The car/host rule, random tie-break, three stages and both winning probabilities are visible; no missing procedure or condition.

Native inspection: 1200 × 520 pixels. ViewBox: `0 60 1200 520` → `0 60 1200 520`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 3. master-loop-part-3.svg — PASS

Purpose: Preview the part's questions about outcomes, time and life quality.

All three questions and their reading sequence are explicit; a separate heading adds no missing information.

Native inspection: 640 × 436 pixels. ViewBox: `0 62 640 436` → `0 62 640 436`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 4. risky-decision-map.svg — REVISED

Purpose: Distinguish expected value, expected utility and the certainty equivalent; separate risk, ambiguity and process quality.

Spell out certainty equivalent at its plotted value; CE is otherwise undefined in the image.

Native inspection: 1200 × 665 pixels. ViewBox: `0 70 1200 665` → `0 70 1200 665`.

Label changes:

- u(CE) = 5 ⇒ CE = 25 → Certainty equivalent = 25

Verification: native view and contact sheet passed; no text-bounds flag.

### 5. prospect-theory-map.svg — REVISED

Purpose: Connect gains/losses, probability weights and the conditional fourfold risk pattern.

Restore diminishing sensitivity as a named feature with a brief explanation inside the value-function panel.

Native inspection: 1200 × 690 pixels. ViewBox: `0 70 1200 690` → `0 70 1200 690`.

Label changes:

- Added: Diminishing sensitivity: changes matter less farther from r.

Verification: native view and contact sheet passed; no text-bounds flag.

### 6. decision-experience-states.svg — PASS

Purpose: Distinguish four information states from description/experience presence.

Both matrix dimensions, all four states, definitions and practical responses are visible.

Native inspection: 1400 × 625 pixels. ViewBox: `0 115 1400 625` → `0 115 1400 625`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 7. experience-rare-event-sampling.svg — REVISED

Purpose: Show how independent sample size affects the chance of missing a rare event.

Identify p on each probability curve, so the displayed formula has a visible parameter key.

Native inspection: 1200 × 635 pixels. ViewBox: `0 52 1200 635` → `0 52 1200 635`.

Label changes:

- 1% event → p = 1%
- 5% event → p = 5%

Verification: native view and contact sheet passed; no text-bounds flag.

### 8. discount-model-crossover.svg — REVISED

Purpose: Compare three discount models and a worked preference reversal.

Use the full quasi-hyperbolic model name, the standard discount-factor axis label, and name present bias/preference reversal in the relevant worked example.

Native inspection: 924 × 1075 pixels. ViewBox: `-12 95 924 1075` → `-12 95 924 1075`.

Label changes:

- Quasi: 1 now; → Quasi-hyperbolic:
- 0.70×0.95ᵗ later → 1 now; 0.70×0.95ᵗ later
- Decision weight, D(t) → Discount factor, D(t)
- One quasi-hyperbolic example: β = .70, δ = .95 → Present bias: β = .70, δ = .95
- Model reverses to €100 now → Preference reverses to €100 now

Verification: native view and contact sheet passed; no text-bounds flag.

### 9. intertemporal-choice.svg — PASS

Purpose: Show why a delayed reward may lose to an immediate one, and corresponding design levers.

Smaller-sooner/larger-later outcomes, uncertainty, future imagery and friction are defined by questions and paired with distinct actions.

Native inspection: 1200 × 580 pixels. ViewBox: `0 120 1200 580` → `0 120 1200 580`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 10. hidden-zero-frame.svg — REVISED

Purpose: Compare an abbreviated payoff display with the same complete outcome streams.

Name the hidden zeros in the complete-stream panel; preserve all option/date/payoff cells.

Native inspection: 800 × 570 pixels. ViewBox: `0 100 800 570` → `0 100 800 570`.

Label changes:

- COMPLETE-STREAM FRAME → COMPLETE STREAM: HIDDEN ZEROS SHOWN

Verification: native view and contact sheet passed; no text-bounds flag.

### 11. mental-accounting-map.svg — REVISED

Purpose: Show how mental grouping and coding of outcomes can influence valuation.

Identify the operations explicitly as mental accounting; the original heading could be read as ordinary bookkeeping.

Native inspection: 1200 × 650 pixels. ViewBox: `0 60 1200 650` → `0 60 1200 650`.

Label changes:

- POSSIBLE ACCOUNTING OPERATIONS → MENTAL ACCOUNTING OPERATIONS

Verification: native view and contact sheet passed; no text-bounds flag.

### 12. mental-accounting-evidence-redraw.svg — REVISED

Purpose: Compare observational disposition-effect evidence with experimentally varied return displays.

Name the disposition effect and identify the stock-allocation responses as hypothetical, retaining the reported medians and source conditions.

Native inspection: 1200 × 630 pixels. ViewBox: `0 95 1200 630` → `0 95 1200 630`.

Label changes:

- Closing winners, keeping losers → Disposition effect: sell winners, hold losers
- Median stock allocation (%) → Median hypothetical stock allocation (%)

Verification: native view and contact sheet passed; no text-bounds flag.

### 13. habit-loop.svg — PASS

Purpose: Represent cue, readiness, action, outcome and learning in a habitual response.

All four elements are defined, learning is labeled, and the nonconscious-impulse qualification remains.

Native inspection: 640 × 595 pixels. ViewBox: `0 45 640 595` → `0 45 640 595`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 14. habit-formation-curve.svg — PASS

Purpose: Separate a schematic increase in automaticity from observed modeled formation times.

Illustrative shape, axes, plateau, source, 95-percent criterion and range/median are visible.

Native inspection: 760 × 770 pixels. ViewBox: `0 125 760 770` → `0 125 760 770`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 15. wanting-liking.svg — REVISED

Purpose: Distinguish motivation to obtain a reward from the pleasure it brings.

Give wanting and liking parallel labels and define liking as experienced pleasure, separating subsequent regret from pleasure itself.

Native inspection: 1200 × 475 pixels. ViewBox: `0 145 1200 475` → `0 145 1200 475`.

Label changes:

- Experienced outcome → Liking
- liking may be brief, weak,or followed by regret → experienced pleasure / may be brief or weak; / regret can follow

Verification: native view and contact sheet passed; no text-bounds flag.

### 16. reward-prediction-error-shift.svg — REVISED

Purpose: Show unexpected, predicted and omitted rewards, then distinguish a separate application hypothesis.

Name reward prediction errors above their three panels; the removed generic heading had contained the only visible occurrence of the concept. The learned-cue panel names the response shift, without implying that the cue delivers the reward.

Native inspection: 1200 × 525 pixels. ViewBox: `0 60 1200 525` → `0 60 1200 525`.

Label changes:

- CLASSIC PATTERNS → REWARD PREDICTION ERRORS
- prediction moves earlier → response shifts to cue

Verification: native view and contact sheet passed; no text-bounds flag.

### 17. urge-wave-observation.svg — REVISED

Purpose: Show one possible urge trajectory and a separate optional observation practice.

Name BRAIN beside its five expanded prompts while retaining the non-timetable qualification.

Native inspection: 760 × 780 pixels. ViewBox: `0 170 760 780` → `0 170 760 780`.

Label changes:

- An optional observation practice → BRAIN: an optional practice

Verification: native view and contact sheet passed; no text-bounds flag.

### 18. subjective-well-being-six-lenses.svg — PASS

Purpose: Distinguish six ways to assess a decision and its relation to life quality.

Every lens has a short definition and temporal position; the no-master-measure boundary remains.

Native inspection: 1200 × 630 pixels. ViewBox: `0 100 1200 630` → `0 100 1200 630`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 19. income-wellbeing-evidence-synthesis.svg — REVISED

Purpose: Compare income/well-being findings across measures and parts of the distribution.

Make the schematic—not fitted—status of all three curves visible in the image itself. The horizontal axes now identify household rather than individual income and its annual period.

Native inspection: 1200 × 585 pixels. ViewBox: `0 95 1200 545` → `0 95 1200 585`.

Label changes:

- Added: Schematic study summaries: curves show patterns, not fitted estimates.
- log income (three panels) → log annual household income (three panels)

Verification: native view and contact sheet passed; no text-bounds flag.

### 20. master-loop-part-4.svg — PASS

Purpose: Preview questions about strategic dependence, cooperation and collective outcomes.

Three explicit questions and their sequence are sufficient for a part route.

Native inspection: 640 × 436 pixels. ViewBox: `0 62 640 436` → `0 62 640 436`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 21. strategic-situation-diagnostic.svg — PASS

Purpose: Distinguish overlapping payoff patterns before selecting strategic actions.

Four conventional archetypes have short definitions and diagnostic questions, followed by a game audit and design options.

Native inspection: 1200 × 650 pixels. ViewBox: `0 95 1200 650` → `0 95 1200 650`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 22. three-lenses-strategic-behavior.svg — PASS

Purpose: Compare equilibrium, bounded reasoning and population dynamics.

Each named lens identifies its mechanisms and question, with shared game specification and conditional-prediction boundary.

Native inspection: 1200 × 580 pixels. ViewBox: `0 95 1200 580` → `0 95 1200 580`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 23. level-k-reasoning-ladder.svg — REVISED

Purpose: Explain successive levels of reasoning in a two-thirds guessing game.

State the 0–100 choice range and two-thirds-of-group-mean target; the ladder otherwise lacks its game rule.

Native inspection: 1200 × 395 pixels. ViewBox: `0 145 1200 345` → `0 95 1200 395`.

Label changes:

- Added: Choose a number from 0 to 100; aim for ⅔ of the group mean.
- Added: None

Verification: native view and contact sheet passed; no text-bounds flag.

### 24. cooperation-architecture.svg — PASS

Purpose: Compare five supports for cooperation and their limitations.

Each support is named and illustrated by mechanisms; the private/joint incentive conflict and relevant audit conditions remain visible.

Native inspection: 1200 × 650 pixels. ViewBox: `0 95 1200 650` → `0 95 1200 650`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 25. watched-eyes-evidence-update.svg — PASS

Purpose: Compare a memorable field-study effect with later cumulative evidence.

The two cue conditions, ten-week sequence, normalized outcome, ratio, study sources and later no-reliable-overall-effect result are all visible.

Native inspection: 1440 × 550 pixels. ViewBox: `0 110 1440 550` → `0 110 1440 550`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 26. social-preference-games-redraw.svg — REVISED

Purpose: Compare how rejection, giving/taking rights and participation options change the meaning of giving.

Replace unexplained sorting out with the concrete option to avoid the game.

Native inspection: 1200 × 580 pixels. ViewBox: `0 105 1200 580` → `0 105 1200 580`.

Label changes:

- or sorting out is available → or avoiding the game is allowed

Verification: native view and contact sheet passed; no text-bounds flag.

### 27. fairness-entitlements-redraw.svg — PASS

Purpose: Compare fairness judgments across market-price scenarios and reference points.

Each scenario includes the monetary change, independent sample size, response percentage and historical sample provenance.

Native inspection: 1200 × 645 pixels. ViewBox: `0 60 1200 645` → `0 60 1200 645`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 28. asch-line-comparison.svg — REVISED

Purpose: Invite a line judgment, then distinguish private belief from a public answer under group pressure.

Restore the social-pressure manipulation as a concise follow-up task; no correct answer is revealed. SVG alternative description preserves all line lengths for equivalent nonvisual access; no visible answer is disclosed.

Native inspection: 1200 × 580 pixels. ViewBox: `0 25 1200 460` → `0 25 1200 580`.

Label changes:

- Added: After choosing, imagine everyone before you answered B.
- Added: Would that change your belief, your public answer, or both?
- Added: None

Verification: native view and contact sheet passed; no text-bounds flag.

### 29. norm-message-diagnostic.svg — PASS

Purpose: Distinguish descriptive norms from approval claims and check their potential harms.

Both norms are defined, decision branches are explicit, and the backfire test retains its essential conditions.

Native inspection: 1200 × 600 pixels. ViewBox: `0 110 1200 600` → `0 110 1200 600`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 30. social-pathways.svg — PASS

Purpose: Distinguish informational learning from public conformity driven by approval or sanctions.

Parallel routes define the mechanisms, distinguish private belief from public response, show feedback and preserve the independence safeguard.

Native inspection: 1200 × 770 pixels. ViewBox: `0 40 1200 770` → `0 40 1200 770`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 31. cultural-market-study-redraw.svg — REVISED

Purpose: Compare variability in song popularity with and without social information.

Name song popularity as the outcome and define the social versus independent conditions by whether download counts were shown.

Native inspection: 1200 × 630 pixels. ViewBox: `0 90 1200 630` → `0 90 1200 630`.

Label changes:

- How much did the worlds diverge? → Music Lab: variation in song popularity
- 1  Social worlds → 1  Social worlds see download counts
- 2  Independent benchmark → 2  No download counts shown

Verification: native view and contact sheet passed; no text-bounds flag.

### 32. social-learning-culture.svg — PASS

Purpose: Show contributors to cumulative culture while allowing error to accumulate.

The five contributors have concrete examples; transmission/retention and both useful/error outcomes remain explicit.

Native inspection: 1200 × 545 pixels. ViewBox: `0 105 1200 545` → `0 105 1200 545`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 33. mimicry-study-redraw.svg — REVISED

Purpose: Compare participants' face rubbing and foot shaking by a partner's mannerism.

Name behavioral mimicry in the chart panel while retaining outcome units, source/N and unequal strength of the two contrasts.

Native inspection: 810 × 595 pixels. ViewBox: `15 55 810 595` → `15 55 810 595`.

Label changes:

- Participant behavior by interaction partner’s mannerism → Behavioral mimicry: actions by partner condition

Verification: native view and contact sheet passed; no text-bounds flag.

### 34. finance-euro-efficiency.svg — PASS

Purpose: Separate three market-efficiency claims prompted by the banknote illustration.

All three claims are defined, risk/cost qualifications are explicit, and the nonimplication between the weaker and stronger claims remains.

Native inspection: 1200 × 580 pixels. ViewBox: `0 120 1200 580` → `0 120 1200 580`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 35. behavioral-finance-audit.svg — REVISED

Purpose: Explain why a return anomaly cannot by itself distinguish market inefficiency from a faulty return model.

Name and briefly define the joint-hypothesis problem inside the diagnostic panel.

Native inspection: 1200 × 625 pixels. ViewBox: `0 100 1200 625` → `0 100 1200 625`.

Label changes:

- JOINT-TEST AUDIT → JOINT-HYPOTHESIS PROBLEM
- Which explanation survives? → Market efficiency and the return model

Verification: native view and contact sheet passed; no text-bounds flag.

### 36. asset-bubble-feedback.svg — PASS

Purpose: Show a possible reinforcing price/expectation/buying loop and its moderators.

Mechanism, fundamentals, optional financing and possible brakes are defined without claiming every rising market is a bubble.

Native inspection: 1200 × 635 pixels. ViewBox: `0 115 1200 635` → `0 115 1200 635`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 37. bubble-trader-strategies-redraw.svg — PASS

Purpose: Report four rule-based trader classifications and their different motivations.

All classifications, percentages, interpretations, source, denominator and classification limits are visible.

Native inspection: 1200 × 655 pixels. ViewBox: `0 55 1200 655` → `0 55 1200 655`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

### 38. finance-event-study-drift.svg — REVISED

Purpose: Explain event windows, abnormal returns and post-event drift without presenting empirical estimates.

Mark the return panel as schematic and define its vertical quantity as cumulative observed minus expected return.

Native inspection: 1200 × 550 pixels. ViewBox: `0 175 1200 550` → `0 175 1200 550`.

Label changes:

- Cumulative abnormal return → Schematic cumulative abnormal return
- Added: Cumulative observed − expected return

Verification: native view and contact sheet passed; no text-bounds flag.

### 39. silence-mechanism-diagnostic.svg — PASS

Purpose: Distinguish five reasons a group may lose information, dissent or responsibility.

Every named mechanism has a diagnostic question and a matched safeguard; neither a generic heading nor a slogan supplies missing content.

Native inspection: 760 × 1005 pixels. ViewBox: `0 185 760 1005` → `0 185 760 1005`.

Existing terms, definitions, task conditions, and boundaries are sufficient; source is byte-identical to this pass’s baseline.

Verification: native view and contact sheet passed; no text-bounds flag.

## Final canonical PNG overview

PASS — Inspected final contact sheets `figures-01.png` through `figures-05.png` in `/tmp/figure-information-review-20260914/final-contact/` after canonical fallback regeneration. No new missing content, text collision, or spacing defect is apparent in the figures. The contact sheet truncates one exceptionally long filename outside its thumbnail; this is an audit-sheet label only, not book figure content. Existing individual native-size inspections remain applicable. No SVG source was changed during this final overview.
