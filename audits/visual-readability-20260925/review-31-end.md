# Readability review: Chapters 31–42 and supporting material

Reviewed the canonical reading route in `_quarto-html.yml`, the section/float inventory, existing captions and table structures, and the explanatory passages around candidate comparisons. This is a **source-level opportunity review**, not a visual certification of every existing illustration. Existing assets were not changed or marked visually passed. The new Chapter 38 illustration was separately rendered and inspected as recorded below.

## Selection and change

**Implemented:** Chapter 38, “Check effort, liquidity, and risk” (`#mpharm-incentives`). The MPharm table compares expected gains under different subjective forecasts, while the following prose asks whether a contract preserves incentives in the two eventual states. A separate two-panel horizontal bar chart makes this second comparison visible. Package D leaves MPharm $30m in either state; package E leaves $18m without approval and $38m with approval. The figure makes no empirical claim and deducts no unmodeled effort cost. One existing closing sentence was replaced with a substantive figure/table cross-reference; no section was added.

**Considered but not added:** Chapter 35's Rackham comparisons (planning/common ground, asking questions, and defending/attacking). These observations concern different coded behaviors and, for planning, a different denominator. A new plot would need careful separation and offers less additional explanatory value than the contract-state comparison. The paragraph already gives the published contrasts and observational boundary.

**Rejected quadrant conversion:** Chapter 34's four honesty responses are not a two-by-two factorial classification: nice silence and protective white lies can occupy similar positions on an invented honesty/warmth axis. A quadrant would impose an unsupported structure on a useful prose comparison.

## Source-review ledger

“Retain” below means no additional graphic selected from the source review; it is not a rendered visual-QA result.

| Canonical source | Decision and reason |
| --- | --- |
| `chapters/31-storytelling.qmd` | Retain. Donation study already has a direct comparative plot; mechanism table compares overlapping families that should not be plotted as independent axes. |
| `chapters/32-message-design.qmd` | Retain. Claim–evidence mappings and drafting prompts serve as lookup tables; turning them into a workflow graphic would repeat their text. |
| `chapters/33-communication.qmd` | Retain. Existing communication-calibration and lie-cue figures already expose the most useful quantitative comparisons; grounding diagrams cover the interaction. |
| `chapters/34-connection.qmd` | Retain. Intent–behavior–impact and repair are already visualized; honesty rows do not support a scientifically clean quadrant. |
| `chapters/35-negotiation-as-joint-decision-making.qmd` | Retain. Negotiation architecture already maps the relation between parties; observation-study percentages remain concise in prose with their limitations. |
| `chapters/36-distributive-negotiation.qmd` | Retain. Existing ZOPA and first-offer information matrix already encode interval and two-dimensional relations. |
| `chapters/37-integrative-negotiation.qmd` | Retain. Existing two-issue Camp David map and Pareto plot explain the geometric relationships; package tables retain exact issue values. |
| `chapters/38-designing-better-agreements.qmd` | **Revised.** Added `contract-state-payoffs.svg/png`; explains the difference between expected gains and incentives in realized approval states. |
| `chapters/39-behavior-design.qmd` | Retain. Vaccination study already has a plot and the behavior-design process already has a diagram. B=MAP here has a different meaning of ability from elaboration in Chapter 30. |
| `chapters/40-choice-architecture.qmd` | Retain. Fuel-use conversion, simplified remote, and action cue already show relationships better than prose alone. Nudge-study averages are qualified in text; avoid treating unlike literatures as randomized conditions. |
| `chapters/41-decision-hygiene.qmd` | Retain. Bias/noise targets, process/outcome quadrant, and judgment pipeline already cover the strongest visual opportunities. |
| `chapters/42-deciding-with-data-and-ai.qmd` | Retain. Existing plots separate forecast from action threshold and baseline risk from treatment benefit. Avoid a simple model/physician/assisted bar chart that obscures different evaluation conditions. |
| `parts/part-1.qmd` through `parts/part-7.qmd` | Retain all seven. Short narrative bridges and three questions establish the route; additional route diagrams would repeat the prose. Existing empty legacy figure anchors are retained. |
| `index.qmd` | Retain. Existing decision map provides the central visual; opening story and contrasts need no additional graphic. |
| `how-to-use-this-book.qmd` | Retain. Reading-route and vocabulary tables are navigational lookup material. |
| `how-to-read-evidence.qmd` | Retain. Comparison, denominator, inference, and generalization are developed through short examples; a new checklist diagram would add no relationship. |
| `appendices/appendix-a-rational-choice-and-decision-analysis.qmd` | Retain. Formal derivations already link to the book's worked examples. An illustrative graph would require selecting new arbitrary parameters; no compelling addition selected in this pass. |
| `appendices/appendix-b-evolutionary-explanations-of-value-choice-and-rationality.qmd` | Retain. Tinbergen's four questions are explicitly distinguished, and the source-qualified Schelling simulation is already visualized. Other tables compare frameworks and evidence rather than independent coordinates. |
| `appendices/appendix-literature-review.qmd` | Retain. Evidence matrices are meant to preserve design and inferential differences; pooling heterogeneous positive-thinking studies into a plot would conceal them. |
| `appendices/appendix-e-how-behavioral-evidence-is-built.qmd` | Retain. Claim-to-design, sampling/assignment, and participant-flow threats already have dedicated diagrams. |
| `appendices/appendix-f-when-evidence-breaks.qmd` | Retain. Evidence selection is visualized as a process and a simulated selection comparison; evidence-status tables function as references. |
| `appendices/appendix-c-portable-course-tools.qmd` | Retain. Standalone worksheets and task-to-tool mappings need explicit fields, not additional schematic diagrams. |
| `appendices/appendix-d-index-of-major-course-examples.qmd` | Retain. Case and media indexes are lookup tables. |
| `references.qmd`, `concept-index.qmd`, `about.qmd` | Retain. Bibliography, index, and publication/author matter; no comparison diagram needed. |

## New-figure verification ledger

| Figure | Status | Size inspected | Verification |
| --- | --- | --- | --- |
| `figures/contract-state-payoffs.svg` | **REVISED** | Native 760×680; narrow 350×314 CSS pixels | Both rendered images inspected. Direct labels and axes fit; minimum essential label size is 14.74 CSS px at 350 px. Grid lines behind value labels were cleared and both sizes reopened. SVG XML parses and no text bounding boxes cross the viewBox. |
| `figures/contract-state-payoffs.png` | **REVISED** | 1140×1020 PNG fallback | Generated by browser rasterization of the final SVG, then opened. Arithmetic and state labels match the source. Final book HTML/EPUB integration is verified by the coordinating agent's release checks. |

Reproduction: `python3 scripts/build_contract_state_figure.py`, followed by `node scripts/render_svg_png_fallbacks.cjs figures/contract-state-payoffs.svg`. `check-contract-figure.cjs` records native/narrow bounds and produces the two inspected screenshots. `contract-state-data.json` records the illustrative terms and calculated payoffs; these are not observations or reconstructed participant data.
