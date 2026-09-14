# Table consistency audit: front matter and Chapters 1–22

Date: 14 September 2026

## Scope and criterion

Inspected all 45 source tables in canonical Chapters 1–22, configured front matter and Parts I–III, including Markdown tables, the raw HTML row-group table in Chapter 5, and tables inside callouts. Counts matched the previously rendered HTML tables in each of the 22 files containing tables. Excluded retired chapters and audit copies.

The criterion is what each table claims to compare. A taxonomy must keep peer concepts at the same level; an example belongs in an example column or prose. A workflow, glossary, evidence comparison or diagnostic audit may legitimately compare different practical roles when that purpose is explicit. Overlapping constructs are not automatically a categorical error.

Final result: 35 PASS and 10 REVISED. This worker revised seven tables; the coordinating editor revised the Chapter 8, 9 and 15 tables, and the final integration review confirmed those fixes.

## Table-by-table inventory

| File | Table ID or local title | Status | Assessment |
| --- | --- | --- | --- |
| `how-to-use-this-book.qmd` | `tbl-long-form-journey` | PASS | Four reading focuses mapped to the corresponding parts; this is a navigation table, not a taxonomy of psychological mechanisms. |
| `how-to-use-this-book.qmd` | `tbl-navigation-vocabulary` | PASS | Explicit glossary of terms. Verbs and the noun expectation are legitimate glossary entries rather than asserted peer stages. |
| `how-to-use-this-book.qmd` | `Reading routes (unlabelled)` | PASS | Reading routes compare reader interests and suitable routes; no claim that these are mutually exclusive scientific categories. |
| `chapters/01-how-decisions-should-be-made-and-how-they-actually-are.qmd` | `tbl-three-questions` | PASS | Normative, descriptive and prescriptive perspectives are parallel questions with matching success criteria. |
| `chapters/01-how-decisions-should-be-made-and-how-they-actually-are.qmd` | `tbl-seven-context-examples` | PASS | All rows are explicitly examples; evidence types occupy their own column. Kept the working historical anchor. |
| `chapters/01-how-decisions-should-be-made-and-how-they-actually-are.qmd` | `tbl-hiring-loop` | PASS | Parallel decision functions, each with its own failure and response; implementations remain in the response column. |
| `chapters/02-building-a-better-decision-alternatives-opportunity-cost-information-and-robustness.qmd` | `tbl-prediction-value` | PASS | Alternative actions occupy rows, predictions and values occupy distinct columns, including the status quo or delay. |
| `chapters/02-building-a-better-decision-alternatives-opportunity-cost-information-and-robustness.qmd` | `tbl-information-decision-branches` | PASS | Explicit practical test examples with matching results and conditional decision value; examples are not labelled information mechanisms. |
| `chapters/02-building-a-better-decision-alternatives-opportunity-cost-information-and-robustness.qmd` | `tbl-proportionate-analysis` | PASS | Decision features use paired ends of the same dimension to compare the needed structure. |
| `chapters/03-attention-what-becomes-evidence.qmd` | `tbl-attention-architecture` | REVISED | Changed Time pressure to Time allocation so all row labels are choices an organizer can make. The row explains how tight deadlines affect evidence inspection. |
| `chapters/03-attention-what-becomes-evidence.qmd` | `tbl-05-1` | PASS | All rows identify attention or interpretation failures, followed by a mechanism and a possible response. |
| `chapters/04-the-predictive-mind-perception-is-inference.qmd` | `tbl-two-meanings-prediction` | PASS | Compares two uses of prediction at the same semantic level; does not treat perception as an example of forecasting. |
| `chapters/05-expectations-when-predictions-become-causes.qmd` | `tbl-consequence-forecast` | PASS | All rows are fields of a forecast, with an explicitly separate example column. A workflow need not be a taxonomy of mechanisms. |
| `chapters/05-expectations-when-predictions-become-causes.qmd` | `tbl-self-fulfilling-self-defeating` | PASS | Raw HTML: self-fulfilling and self-defeating forecasts form the row groups; the two examples within each group are explicitly nested and labelled examples. |
| `chapters/05-expectations-when-predictions-become-causes.qmd` | `tbl-08-expectation-pathways` | REVISED | Narrowed generic Behavior to the person’s behavior and Interpersonal response to other people’s responses, so the former does not silently contain the latter. Caption makes overlapping causal routes explicit. |
| `chapters/05-expectations-when-predictions-become-causes.qmd` | `tbl-08-1` | PASS | Parallel application domains with pathway and ethical-condition columns; not an asserted taxonomy of mechanisms. |
| `chapters/06-valuation-how-options-become-worth-choosing.qmd` | `tbl-automatic-evaluation-stages` | PASS | Explicit stages/appraisals in a practical process comparison, with matching questions and inputs. |
| `chapters/06-valuation-how-options-become-worth-choosing.qmd` | `tbl-value-is-not-one-thing` | PASS | Explicitly contrasts related constructs that can diverge; it does not label habit strength as a fourth kind of pleasure or value. |
| `chapters/06-valuation-how-options-become-worth-choosing.qmd` | `tbl-contextual-cues-and-waiting` | REVISED | Recast all rows as testable claims with evidence and limits. Physiological or neural cue reactivity is no longer labelled as a peer causal explanation of impatient choice. Retained all four scientific distinctions and all surrounding studies. |
| `chapters/06-valuation-how-options-become-worth-choosing.qmd` | `tbl-07-1` | PASS | Parallel diagnostic questions; constructs and possible mistakes occupy separate columns. |
| `chapters/07-the-narrator-after-choice-why-reasons-are-not-always-causes.qmd` | `tbl-rationalization-detector` | PASS | Parallel diagnostic questions; specific biases and incentives are the potential targets rather than the row taxonomy. |
| `chapters/07-the-narrator-after-choice-why-reasons-are-not-always-causes.qmd` | `tbl-process-outcome-review` | PASS | A complete two-by-two crossing of process and outcome quality, with conditional review advice. |
| `chapters/08-fast-and-frugal-thinking.qmd` | `tbl-04-1` | REVISED | Coordinating editor added shared dimensions for System 1 and System 2: cognitive demands, typical speed and effort, contributions, and sources of error. Final source inspection confirms both columns answer the same question in each row. |
| `chapters/09-what-feels-likely-availability-affect-and-resemblance.qmd` | `tbl-10-1` | REVISED | Coordinating editor removed Personal example as a peer heuristic. The table now compares affect, availability and representativeness; the nearby discussion and availability row retain the need to compare a memorable case with the relevant wider record. |
| `chapters/10-beliefs-that-defend-themselves.qmd` | `tbl-13-1` | REVISED | Used the chapter’s standard term Fundamental attribution error in the row. Replaced the caption implying every listed risk protects a preferred belief with Risks in searching, interpreting, and explaining evidence; the surrounding chapter already distinguishes motivational from informational explanations. |
| `chapters/11-when-context-rewrites-comparison.qmd` | `tbl-14-1` | REVISED | All rows now name observed effects: anchoring, halo/horn, attraction and preference reversal. Moved evaluation mode and response task into the context column. Decoy/context no longer combines a specific manipulation with its broader category. |
| `chapters/12-framing-when-the-same-facts-become-different-decisions.qmd` | `tbl-disease-framing` | PASS | The two rows are complementary descriptions of identical programs; probabilities, totals and sure/risky columns align. |
| `chapters/12-framing-when-the-same-facts-become-different-decisions.qmd` | `tbl-15-1` | PASS | Each row specifies what a frame makes focal and its appropriate safeguard; question and causal frames are broad framing operations, not individual examples masquerading as a peer heuristic. |
| `chapters/13-accessibility-familiarity-and-ease.qmd` | `tbl-16-1` | REVISED | Rewrote every first-column entry as an empirical claim. Research domains, named phenomena and a specific failed intervention are no longer mixed as if they were parallel conceptual categories. Evidence strengths and boundaries remain explicit. |
| `chapters/15-samples-randomness-regression-and-calibration.qmd` | `tbl-confidence-calibration` | REVISED | Coordinating editor retained three forms of overconfidence: overestimation, overplacement and overprecision. Planning fallacy appears in its own subsection as an application that can involve optimistic estimates and overprecision, rather than exclusively overestimation or a fourth peer form. |
| `chapters/15-samples-randomness-regression-and-calibration.qmd` | `tbl-probability-forecast-ledger` | PASS | Parallel record fields with examples or instructions appropriate to each field. |
| `chapters/16-risky-decision-making-a-probability-is-not-yet-a-feeling.qmd` | `tbl-risk-elicitation` | REVISED | Renamed the outcome Certainty equivalent to the method Certainty-equivalent elicitation. Corrected the bomb task’s output from a continuous stopping point to a discrete number of boxes; retained the method comparison and limitations. |
| `chapters/17-prospect-theory-gains-and-losses-begin-at-a-reference-point.qmd` | `tbl-prospect-fourfold` | PASS | Complete gain/loss by high/low probability comparison; behavioral examples remain within the corresponding cell, and the preceding text qualifies the parameter-dependent pattern. |
| `chapters/18-decisions-from-experience-when-rare-events-are-not-encountered.qmd` | `tbl-experience-states` | PASS | Exhaustive two-by-two information states, with a corresponding danger and response in each row. |
| `chapters/18-decisions-from-experience-when-rare-events-are-not-encountered.qmd` | `tbl-process-outcome` | PASS | Complete process-quality by outcome-quality comparison, consistent with the Chapter 7 table. |
| `chapters/19-intertemporal-decision-making-why-later-loses-to-now.qmd` | `tbl-22-delay-mechanisms` | PASS | Parallel possible influences on intertemporal choice; illustrative cases occupy the Example column. |
| `chapters/19-intertemporal-decision-making-why-later-loses-to-now.qmd` | `tbl-most-discounting` | PASS | Explicit teaching mnemonic for inspecting four attributes/representations; does not classify four mutually exclusive types of impatience. |
| `chapters/19-intertemporal-decision-making-why-later-loses-to-now.qmd` | `tbl-discount-identification` | PASS | Explicit comparison of possible components of an observed discount estimate, with distinct identification problem and design response. |
| `chapters/19-intertemporal-decision-making-why-later-loses-to-now.qmd` | `tbl-intertemporal-time-stream` | PASS | Parallel before/during/after parts of an outcome stream; questions and records align across rows. |
| `chapters/20-mental-accounting-money-is-fungible-minds-label-it.qmd` | `tbl-mental-budgets` | PASS | Prior-purchase conditions share one clearly specified percentage scale and denominator; new-purchase outcomes occupy columns. No reported data changed. |
| `chapters/20-mental-accounting-money-is-fungible-minds-label-it.qmd` | `tbl-mental-accounting-audit` | PASS | Parallel audit questions about a representation; it does not mistake a particular purchase for a mechanism. |
| `chapters/21-habits-wanting-and-self-control.qmd` | `tbl-20-brain` | PASS | BRAIN is explicitly an optional practice sequence, not a scientific classification. Each step has a prompt; no revision needed on category grounds. |
| `chapters/22-deciding-for-a-better-life-satisfaction-connection-and-meaning.qmd` | `tbl-well-being-targets` | PASS | Explicitly compares measurement targets and their limitations, not subtypes of one happiness measure. Predicted, chosen, experienced and retrospective targets remain distinguishable. |
| `chapters/22-deciding-for-a-better-life-satisfaction-connection-and-meaning.qmd` | `tbl-relational-well-being` | PASS | Four related relational constructs, each with a diagnostic question and a separate limitation; no example is promoted to a construct. |
| `chapters/22-deciding-for-a-better-life-satisfaction-connection-and-meaning.qmd` | `tbl-well-being-decision-audit` | PASS | Four practical fields compare a prospective question with a retrospective check on the same field. |

## Files checked with no tables

The following configured files contain no Markdown or raw HTML tables: `index.qmd`, `how-to-read-evidence.qmd`, `about.qmd`, `concept-index.qmd`, `references.qmd`, `parts/part-1.qmd`, `parts/part-2.qmd`, `parts/part-3.qmd`, and Chapter 14 (`chapters/14-base-rates-conditional-probability-and-bayesian-updating.qmd`).

## Evidence and preservation

- All chapter reference blocks and all existing table anchors in the seven edited files match their pre-task content. No studies, reported numbers, reference entries, figures or source data were removed.
- The Chapter 6 change separates observation from causal mechanism; all arousal, subjective-time, generalized-wanting and process-model studies remain in the surrounding discussion.
- The Chapter 11 revision uses effects already defined and sourced in that chapter, including its explicit account of preference reversal.
- The Chapter 13 table restates the claims and qualifications already developed in its source paragraphs; it does not add an unverified effect.
- The bomb task’s discrete number-of-boxes measure was checked against the authors’ paper abstract in the [University of Milan repository](https://air.unimi.it/handle/2434/224581) and the [IZA working-paper record](https://www.iza.org/publications/dp/6710/the-bomb-risk-elicitation-task). The existing published Crosetto and Filippin (2013) reference is retained.
- Source whitespace checks passed for the seven edited chapters. Full rebuilding and final rendered checks belong to the coordinating editor.

## Final integration review

A second source review checked the seven early-worker files, the thirteen late-worker files, and the coordinating editor’s Chapter 8, 9, 15 and 39 fixes. The revised tables consistently distinguish scientific categories from examples, measurement conditions, design choices, and evaluation tasks. No new table-level semantic problem was found in these changes.

A fresh census of the 62 configured source files found **146 tables in 48 files: 145 Markdown tables and one raw HTML table**. The early inventory covers 45 and the late inventory covers 101. Matching each table by source file and ID, with an explicit match for the two unnumbered tables, found **no omissions or duplicate coverage**. The combined final disposition is **34 revised and 112 passed**. The sole raw HTML table is Chapter 5’s self-fulfilling/self-defeating comparison, whose grouped example rows preserve the distinction between forecast type and illustration.

Preservation was rechecked against the complete pre-task snapshot at `/tmp/standard-terms-tables-20260914/before`, including the already revised Appendix F. Reference blocks are unchanged and all prior explicit anchors remain in the twenty worker-edited files. The four additional coordinating-editor files likewise retain all original references and explicit anchors; Chapter 8 adds one reference and Chapter 15 adds five. This verification does not overwrite or replace the earlier Appendix F work.

The Chapter 39 framework table now identifies each component as belonging to COM-B or B=MAP. Its digital-loop table contains four loop features, while the separate paragraph supplies the evaluation and welfare check. Both requested distinctions are present in the final source. No manuscript edits, reference synchronization, builds, commits or pushes were performed during this final integration review.
