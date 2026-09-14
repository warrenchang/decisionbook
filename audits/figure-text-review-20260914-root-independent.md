# Independent review of seven root-owned figures

Reviewed against `/tmp/figure-text-review-20260914/before`. Read the current SVGs and related generator diffs; inspected each current PNG individually. No SVG, script, QMD, or PNG was changed during this review.

## Result

PASS for scientific preservation and current figure appearance. The one minor alt-text discrepancy found during review has been corrected and rechecked; no plotted data or essential qualification was lost.

| Figure | Result | Evidence |
| --- | --- | --- |
| master-loop.svg | PASS — PNG 1050×1250 inspected | All seven input/function nodes and five feedback targets retained. The enclosing people/institutions/design frame remains. Removed recurrence/overlap prose is still explicit in the caption, nearby paragraph, and accessible description. No direct feedback arrow to current inputs was introduced. |
| random-sampling-vs-assignment.svg | PASS — PNG 1140×1260 inspected | Assignment center x=240. Treatment/control centers x=125 and x=355, exactly 115 units to either side; both group boxes are 200×102 at y=718. The junction is x=240, y=684 and branch endpoints attach to the group tops. External/internal validity groups contain text only and remain beside the procedure boxes. Population/sample/not-in-evaluation/control distinctions preserved; generalization and causal-inference boundaries remain in the caption/body. |
| claim-to-design-pipeline.svg | PASS — PNG 1050×1020 inspected | All five stage labels and questions are identical. Only the outer heading was removed and stages translated upward; their order and connectors remain unchanged. |
| selected-evidence-pipeline.svg | PASS — PNG 1050×1020 inspected | All five stage labels and selection questions are identical. Only the heading and surrounding space were removed; no evidence-selection stage was lost. |
| participant-flow-threats.svg | PASS — PNG 1140×1016 inspected | Both assignment branches still distinguish receipt, observation, and comparison as assigned. The removed interference/reminder prose remains in the caption, accessible description, and appendix discussion. Original assignment is not replaced by treatment received. |
| selected-literature-simulation.svg | PASS — PNG 1038×954 inspected | All 68 SVG path attribute dictionaries are identical to the snapshot, including the histogram data geometry. N=2,000, selected N=328, means .202/.490, true effect .20 SD, shared axes, and two-sided p<.05 gate all remain. Repeated dashed-line keys were consolidated with the teaching-simulation qualifier; denominators remain in the caption/description. Generator changes affect labels and crop only, not sampling, selection, means, histogram bins, or weights. |
| schelling-emergence.svg | PASS — PNG 2100×840 inspected | All 759 circle attribute dictionaries are identical, preserving every agent/vacancy position and legend marker. Seed 20260830, one-run qualifier, one-third threshold, three states, 36/44 moves, four sweeps, and .48/.64/.68 summaries remain. All simulation functions are AST-identical; only rendering title/crop changed. |

## Resolved editorial follow-up

The participant-flow alt text previously referred to a deleted reminder about effects between groups. The parent corrected it to “and retains the original assignment labels for analysis.” I reread the current QMD and verified this wording. Its visible caption still preserves missing-outcome and interference qualifications. No open finding remains.

## Final contact-sheet check

Inspected final contact sheets `figures-06.png` through `figures-10.png` in `/tmp/figure-text-review-20260914/final-contact`, covering 54 displayed assets. No missing content, empty deleted-panel shell, conspicuous clipping, or newly excessive outer whitespace was apparent. The short explanatory panel beside the lie-cue plot is intentionally smaller than the plot; its remaining open area does not omit data. Previously reviewed late figures, appendix pipelines, F.2, and both simulations remain visually consistent with their individually inspected versions. This overview check supplements individual inspection; it does not independently certify small text at phone width.

## Generator and verification boundary

Inspected `build_master_loop_figures.py`, `build_methods_appendix_figures.py`, `build_schelling_sequence.py`, and the coordinate exception in `qa_figure_connectors.py`. F.2 annotation coordinates and symmetry match their generator definitions. Selection-simulation calculation code is unchanged before the plotting section. Schelling `neighbors`, `same_share`, `segregation_index`, `run`, and `panel` are unchanged; its figure change is restricted to a heading and crop.

This was a read-only source and individual-PNG review. The parent is responsible for generator execution checks, final HTML/EPUB builds, and destination/phone verification. No claim is made here that a PNG-only inspection verifies those final destinations.
