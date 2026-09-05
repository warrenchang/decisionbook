# Book-wide figure visual audit

**Scope:** all 110 distinct reader-facing visual assets (111 configured source placements) in the book on 5 September 2026.

**Method:** Every asset was reviewed on labeled contact sheets; dense, new, and previously flagged figures were reopened individually. The semantic pass checked whether each colour, curve, symbol, line style, and annotation had one explicit role. All 105 connector-bearing figures were checked programmatically for attachment, visible shaft length, and arrowhead proportion. All 113 rendered HTML placements were loaded at 1440 px and 390 px, and all 112 in-book EPUB placements were extracted and loaded at 768 px and 390 px. Selected figures were captured and inspected at both widths. Wide HTML diagrams use a deliberate horizontal reading pane below 768 px so labels remain readable. The separate cover image was package-validated. EPUB uses PNG fallbacks, while SVG sources are retained for editing. `ADDED` identifies a new asset from the lecture-note visual review; `REVISED` means the current working-tree version changed during the figure-revision programme; `PASS` means it required no visual change. There are no known `BLOCKED` figures.

## Notable corrections

- Rebuilt the master loop and all seven part variants with evenly spaced stages, compact marker-based arrowheads, visible shafts, and consistent highlighting.
- Reintroduced the Chapter 1 normative loop immediately after the rational-choice benchmark, routed feedback to the Judgment boundary, and kept the forward Prediction-to-Valuation relation unambiguous.
- Reworked Figure 1.2 so its unobstructed connectors are straight, its context arrow is correctly coloured, Selection and Interpretation is centred, and every internal Judgment relation is bidirectional.
- Contained the note in Figure 12.2 and rebuilt Figure 13.2 as aligned left and right columns around the central mechanism, eliminating crossings and unreadably small labels.
- Aligned the habit-loop connector and reduced the habit-formation figure to one curve plus the informative 18–254-day range and 66-day median. The separate omission analysis now remains in the caption and prose, where its estimates and boundary conditions can be explained accurately.
- Simplified the urge-wave figure to one curve and five short action labels. Explanatory sentences, caveats, pseudo-legend material, and redundant panels were removed from both Chapter 21 figures.
- Completed a text-light pass across the remaining figures: provenance, methodological qualifiers, and interpretive sentences that did not need to be decoded inside the artwork now appear in captions or prose; essential labels, values, and visual keys remain in the figures.
- Corrected the event-study schematic so the paths coincide before the announcement and visibly diverge only at the event; placed the event label above its line; and used the supplied photograph of an actual €20 note in the efficiency figure.
- Reflowed crowded reward-prediction-error labels and retained its explicit boundary that the drawing is a teaching schematic, not a neural recording.
- Added eight source-safe lecture-inspired figures: a Stroop activity, measurable perceptual-context demonstrations, a choice-blindness switch sequence, an assumed-choice egg menu, a fully specified Monty Hall protocol, an Asch-style line task, a source-verified market-fairness redraw, and a seeded Schelling-style simulation generated from retained code.
- Corrected the new figures after independent scientific review: Monty Hall now declares the host's random tie-break; the Asch caption no longer spoils the task; the perception figure is explanatory rather than a false hidden-answer challenge; the fairness graphic uses descriptive rather than causal cross-vignette headings; and the Schelling figure distinguishes core displayed parameters from generator-level reproducibility.

## Figure ledger

| Figure asset | Status | Size inspected | Result |
|---|---|---|---|
| `master-loop.png` | REVISED | 100% fallback | Shared influence rail, separate prediction and valuation, combined choice–commitment–action, spacing, and markers verified; QA pass. |
| `master-loop-part-1.png` | REVISED | 100% fallback | Shared influence rail, revised stage grouping, shafts, markers, and highlight verified; QA pass. |
| `decision-loop.png` | REVISED | 100% fallback; HTML desktop/mobile; EPUB 768/390 | Normative flow, one-way Prediction-to-Valuation relation, connector attachment, and feedback path to the Judgment boundary verified; QA pass. |
| `decision-making-according-to-behavioral-evidence.png` | REVISED | 100% fallback; HTML desktop/mobile; EPUB 768/390 | Straight/aligned connectors, bidirectional Judgment relations, and feedback path to the internal model verified; QA pass. |
| `option-information-portrait.png` | REVISED | Contact sheet; 100% fallback | Connector and spacing corrections verified; QA pass. |
| `attention-bottleneck.png` | REVISED | Contact sheet; 100% fallback | Text sizing and visual hierarchy corrected; QA pass. |
| `attention-filter.png` | REVISED | Contact sheet; 100% fallback | Alignment and connector geometry corrected; QA pass. |
| `judgment-and-decision-making-according-to-predictive-processing.png` | REVISED | Contact sheet; 100% fallback | Reflowed to aligned columns; crossings and small type removed; QA pass. |
| `valuation.png` | PASS | Contact sheet; 100% fallback | Text containment and relationships verified. |
| `expectation-loop.png` | REVISED | Contact sheet; 100% fallback | Loop geometry, text sizing, and connector attachment corrected; QA pass. |
| `narrator-learning.png` | PASS | Contact sheet; 100% fallback | Geometry, labels, and hierarchy verified. |
| `master-loop-part-2.png` | REVISED | 100% fallback | Shared influence rail, revised stage grouping, shafts, markers, and highlight verified; QA pass. |
| `heuristic-substitution.png` | PASS | Contact sheet; 100% fallback | Geometry and text containment verified. |
| `fast-slow.png` | PASS | Contact sheet; 100% fallback | Bidirectional relation and labels verified. |
| `daughter-finger-counting.png` | PASS | Contact sheet; 100% source | Crop, resolution, and page fit verified. |
| `affect-panda-sea-star.png` | PASS | Contact sheet; 100% source | Image framing and legibility verified. |
| `affect-availability.png` | REVISED | Contact sheet; 100% fallback | Text, spacing, and connectors corrected; QA pass. |
| `prototype-probability.png` | REVISED | Contact sheet; 100% fallback | Comparison structure and connector geometry corrected; QA pass. |
| `belief-protection-loop.png` | PASS | Contact sheet; 100% fallback | Loop and text containment verified. |
| `anchor-decoy.png` | REVISED | Contact sheet; 100% fallback | Arrowhead scale and connector alignment corrected; QA pass. |
| `context-mechanisms.png` | PASS | Contact sheet; 100% fallback | Alignment, type, and hierarchy verified. |
| `wording-memory-study-redraw.png` | REVISED | Contact sheet; 100% fallback | Overflow removed and study-result presentation clarified; QA pass. |
| `priming-pathway.png` | PASS | Contact sheet; 100% fallback | Flow and evidence boundary verified. |
| `fluency-pathway.png` | REVISED | Contact sheet; 100% fallback | Text containment, arrow sizing, and spacing corrected; QA pass. |
| `probability-judgment-map.png` | REVISED | Contact sheet; 100% fallback | Denominator tree, feedback loop, and type scale corrected; QA pass. |
| `master-loop-part-3.png` | REVISED | 100% fallback | Shared influence rail, revised stage grouping, shafts, markers, and highlight verified; QA pass. |
| `risky-decision-map.png` | REVISED | Contact sheet; 100% fallback | Arrowheads, labels, and decision path corrected; QA pass. |
| `prospect-theory-map.png` | REVISED | Contact sheet; 100% fallback | Curves, reference point, and labels corrected; QA pass. |
| `decision-experience-states.png` | REVISED | Contact sheet; 100% fallback | State layout and connectors corrected; QA pass. |
| `experience-rare-event-sampling.png` | REVISED | Contact sheet; 100% fallback | Sampling path and type hierarchy corrected; QA pass. |
| `intertemporal-choice.png` | REVISED | Contact sheet; 100% fallback | Timeline, labels, and connector scale corrected; QA pass. |
| `habit-loop.png` | REVISED | Contact sheet; 100% fallback | Middle connector aligned to adjacent shaft; QA pass. |
| `habit-formation-curve.png` | REVISED | Source and fallback; HTML desktop/mobile; EPUB 768/390 | Reduced to one curve and one numeric range: 18–254 days, median 66; omission details moved to prose; QA pass. |
| `reward-prediction-error-shift.png` | REVISED | Contact sheet; 100% fallback | Marker size and crowded cue/reward labels corrected; evidence boundary retained; QA pass. |
| `wanting-liking.png` | REVISED | Contact sheet; 100% fallback | Label scale and relationship layout corrected; QA pass. |
| `urge-wave-observation.png` | REVISED | Source and fallback; HTML desktop/mobile; EPUB 768/390 | Reduced to one curve and five short BRAIN labels; explanatory boxes and meta-commentary removed; QA pass. |
| `mental-accounting-map.png` | REVISED | Contact sheet; 100% fallback | Layout, arrows, and text scale corrected; QA pass. |
| `mental-accounting-evidence-redraw.png` | REVISED | Contact sheet; 100% fallback | Study-result redraw and labels clarified; QA pass. |
| `subjective-well-being-six-lenses.png` | REVISED | Contact sheet; 100% fallback | Six-panel spacing and type hierarchy corrected; QA pass. |
| `income-wellbeing-evidence-synthesis.png` | REVISED | Contact sheet; 100% fallback | Curves, labels, and evidence boundary corrected; QA pass. |
| `master-loop-part-4.png` | REVISED | 100% fallback | Shared influence rail, revised stage grouping, shafts, markers, and highlight verified; QA pass. |
| `strategic-situation-diagnostic.png` | REVISED | Contact sheet; 100% fallback | Decision path and type scale corrected; QA pass. |
| `three-lenses-strategic-behavior.png` | REVISED | Contact sheet; 100% fallback | Three-column alignment and labels corrected; QA pass. |
| `level-k-reasoning-ladder.png` | REVISED | Contact sheet; 100% fallback | Ladder alignment, spacing, and marker scale corrected; QA pass. |
| `cooperation-architecture.png` | REVISED | Contact sheet; 100% fallback | Mechanism lanes and connectors corrected; QA pass. |
| `social-preference-games-redraw.png` | REVISED | Contact sheet; 100% fallback | Study-result panels and labels clarified; QA pass. |
| `social-learning-culture.png` | REVISED | Contact sheet; HTML desktop/mobile; EPUB 768/390; 100% fallback | Five contributors now use separate straight ports; crossing connectors removed; QA pass. |
| `mimicry-study-redraw.png` | REVISED | Contact sheet; 100% fallback | Study-result redraw and evidence boundary clarified; QA pass. |
| `norm-message-diagnostic.png` | REVISED | Contact sheet; HTML desktop/mobile; EPUB 768/390; 100% fallback | Question, norm, decision, and backfire boxes widened; all labels contained; QA pass. |
| `social-pathways.png` | REVISED | Contact sheet; HTML desktop/mobile; EPUB 768/390; 100% fallback | Parallel route lanes, straight vertical connectors, external feedback route, and larger support type remove crossings and text overlap; QA pass. |
| `cultural-market-study-redraw.png` | REVISED | Contact sheet; 100% fallback | Study-result redraw, scales, and labels clarified; QA pass. |
| `finance-euro-efficiency.png` | REVISED | Contact sheet; 100% fallback | Supplied €20-note photograph integrated; claims and spacing clarified; QA pass. |
| `behavioral-finance-audit.png` | REVISED | Contact sheet; 100% fallback | Audit flow and text scale corrected; QA pass. |
| `finance-event-study-drift.png` | REVISED | Contact sheet; 100% fallback | Pre-event paths now coincide and divergence begins at the event; QA pass. |
| `asset-bubble-feedback.png` | REVISED | Contact sheet; 100% fallback | Feedback curve, markers, and labels corrected; QA pass. |
| `bubble-trader-strategies-redraw.png` | REVISED | Contact sheet; 100% fallback | Strategy comparison and study-result labels clarified; QA pass. |
| `culture-meaning-map.png` | REVISED | Contact sheet; 100% fallback | Meaning-audit layout and connector scale corrected; QA pass. |
| `culture-triad-monkey-panda-banana.png` | PASS | Contact sheet; 100% source | Illustration framing, resolution, and page fit verified. |
| `culture-honor-study-redraw.png` | REVISED | Contact sheet; 100% fallback | Study-result redraw, comparison labels, and evidence boundary clarified; QA pass. |
| `master-loop-part-5.png` | REVISED | 100% fallback | Shared influence rail, revised stage grouping, shafts, markers, and highlight verified; QA pass. |
| `persuasion-update.png` | REVISED | Contact sheet; 100% fallback | Model-update flow and type hierarchy corrected; QA pass. |
| `story-update.png` | REVISED | Contact sheet; 100% fallback | Connector geometry and text scale corrected; QA pass. |
| `story-evidence-braid.png` | REVISED | Contact sheet; 100% fallback | Braid paths, labels, and evidence relation corrected; QA pass. |
| `communication-iceberg.png` | REVISED | Contact sheet; 100% fallback | Layer spacing and labels corrected; QA pass. |
| `communication-grounding.png` | REVISED | Contact sheet; 100% fallback | Grounding loop and text containment corrected; QA pass. |
| `communication-calibration-evidence.png` | REVISED | Contact sheet; 100% fallback | Meta-text removed, labels shortened, and every label contained; QA pass. |
| `conversation-needs-map.png` | REVISED | Contact sheet; 100% fallback | Column alignment, spacing, and labels corrected; QA pass. |
| `conversation-repair.png` | REVISED | Contact sheet; 100% fallback | Repair sequence and connector geometry corrected; QA pass. |
| `intent-behavior-impact-cycle.png` | REVISED | Contact sheet; 100% fallback | Cycle geometry and text hierarchy corrected; QA pass. |
| `master-loop-part-6.png` | REVISED | 100% fallback | Shared influence rail, revised stage grouping, shafts, markers, and highlight verified; QA pass. |
| `negotiation-architecture.png` | REVISED | Contact sheet; 100% fallback | Process phases, connectors, and type scale corrected; QA pass. |
| `zopa.png` | REVISED | Contact sheet; 100% fallback | Range geometry, labels, and alignment corrected; QA pass. |
| `first-offer-information-matrix.png` | REVISED | Contact sheet; 100% fallback | Matrix spacing and label legibility corrected; QA pass. |
| `pareto.png` | REVISED | Contact sheet; 100% fallback | Frontier curve and annotations corrected; QA pass. |
| `agreement-design.png` | REVISED | Contact sheet; 100% fallback | Agreement sequence and connector scale corrected; QA pass. |
| `master-loop-part-7.png` | REVISED | 100% fallback | Shared influence rail, revised stage grouping, shafts, markers, and highlight verified; QA pass. |
| `behavior-design.png` | REVISED | Contact sheet; 100% fallback | Behavior path, markers, and type hierarchy corrected; QA pass. |
| `choice-architecture.png` | REVISED | Contact sheet; 100% fallback | Choice path and visual hierarchy corrected; QA pass. |
| `bias-and-noise.png` | REVISED | Contact sheet; 100% fallback | Comparison layout and labels corrected; QA pass. |
| `structured-judgment-pipeline.png` | REVISED | Contact sheet; 100% fallback | Pipeline geometry and text scale corrected; QA pass. |
| `decision-audit.png` | REVISED | Contact sheet; 100% fallback | Audit sequence, arrowheads, and type scale corrected; QA pass. |
| `claim-to-design-pipeline.png` | REVISED | Contact sheet; 100% fallback | Claim/design flow and evidence boundary corrected; QA pass. |
| `selected-evidence-pipeline.png` | REVISED | Contact sheet; 100% fallback | Evidence pipeline spacing, hierarchy, and labels corrected; QA pass. |
| `huanren-warren-zhang-profile.png` | PASS | Contact sheet; 100% source | Crop, resolution, and about-page fit verified. |
| `stroop-interference-lab.png` | ADDED | Contact sheet; source and fallback; HTML desktop/mobile; EPUB 768/390 | Colour words and ink colours are contained, high-contrast, and readable; the boundary note avoids treating the activity as an ability test or effect-size estimate; QA pass. |
| `perception-context-lab.png` | ADDED | Contact sheet; source and fallback; HTML desktop/mobile; EPUB 768/390 | Three physically controlled comparisons are aligned and measurable; support text enlarged and challenge wording removed; QA pass. |
| `choice-blindness-swap.png` | ADDED | Contact sheet; source and fallback; HTML desktop/mobile; EPUB 768/390 | Bidirectional swap connector attaches to both cards; labels are contained; the figure preserves partial detection and bounded introspection; QA pass. |
| `assumed-choice-eggs.png` | ADDED | Contact sheet; source and fallback; HTML desktop/mobile; EPUB 768/390 | Two menus use balanced panels and visible option sets; egg art does not obscure labels; refusal and implied commitment are distinguished; QA pass. |
| `monty-hall-protocol.png` | ADDED | Contact sheet; source and fallback; HTML desktop/mobile; EPUB 768/390 | Long enough arrow shafts attach to panel boundaries; all support text was enlarged; host knowledge, mandatory reveal and offer, and random tie-breaking are visible; QA pass. |
| `asch-line-comparison.png` | ADDED | Contact sheet; source and fallback; HTML desktop/mobile; EPUB 768/390 | Lines are precisely drawn, labels are legible, and the visible caption preserves the activity before asking about public pressure; QA pass. |
| `fairness-entitlements-redraw.png` | ADDED | Contact sheet; source and fallback; HTML desktop/mobile; EPUB 768/390 | Exact source values and sample sizes are legible; headings are descriptive; historical, separate-sample, and nonnormative boundaries are visible; QA pass. |
| `schelling-emergence.png` | ADDED | Contact sheet; source and fallback; HTML desktop/mobile; EPUB 768/390 | Three panels preserve identical population counts; connectors attach cleanly; parameter text was enlarged and reflowed; generator-level schedule and randomness are declared; QA pass. |
| `camp-david-two-issue-map.png` | REVISED | Contact sheet; source and fallback | Redundant boundary box removed; issue map and package relationship verified; QA pass. |
| `choice-architecture-simplified-remote.png` | PASS | Contact sheet; source and fallback | Simplified remote-control comparison is legible and its choice-design contrast is explicit; QA pass. |
| `context-b13-demonstration.png` | PASS | Contact sheet; HTML desktop/mobile; EPUB 768/390 | Identical central symbols and contextual cues are clearly distinguished; no false hidden-answer implication; QA pass. |
| `digital-arrow-affordance.png` | PASS | Contact sheet; HTML desktop/mobile; EPUB 768/390 | Directional cue is visually salient without implying stronger evidence than the example supports; QA pass. |
| `discount-model-crossover.png` | PASS | Contact sheet; source and fallback | Discount curves, crossover, axes, and model labels are distinct and readable; QA pass. |
| `economist-subscription-decoy.png` | PASS | Contact sheet; HTML desktop/mobile; EPUB 768/390 | Three offers and the dominated comparison are visibly separated; QA pass. |
| `hidden-zero-frame.png` | PASS | Contact sheet; source and fallback | Equivalent totals and the hidden-zero contrast are contained and legible; QA pass. |
| `lie-cues-belief-gap.png` | PASS | Contact sheet; HTML desktop/mobile; EPUB 768/390 | Belief–evidence gap, uncertainty, and the absence of a reliable single cue are explicit; QA pass. |
| `model-underdetermination.png` | PASS | Contact sheet; source and fallback | Multiple mechanisms leading to the same observation are visually distinct; QA pass. |
| `mpg-fuel-use.png` | PASS | Contact sheet; HTML desktop/mobile; EPUB 768/390 | Nonlinear mapping and comparison quantities are labelled and readable; QA pass. |
| `overlapping-motive-systems.png` | PASS | Contact sheet; source and fallback | Nested triangular systems use equal type size and spacing; the caption prevents interpretation as a rigid hierarchy; QA pass. |
| `participant-flow-threats.png` | PASS | Contact sheet; source and fallback | Recruitment, allocation, attrition, and analysis threats are separated without crossed connectors; QA pass. |
| `personal-mimicry-crossed-arms.png` | PASS | Contact sheet; 100% source | Crop, resolution, and contextual placement verified. |
| `random-sampling-vs-assignment.png` | PASS | Contact sheet; source and fallback | Population generalization and causal assignment paths are visually separated; QA pass. |
| `selected-literature-simulation.png` | PASS | Contact sheet; source and fallback | Literature-to-simulation relation and evidence boundary are explicit; QA pass. |
| `sensory-windows-partial-world.png` | PASS | Contact sheet; source and fallback | Partial-observation metaphor, labels, and visual hierarchy verified; QA pass. |
| `silence-mechanism-diagnostic.png` | PASS | Contact sheet; source and fallback | Competing meanings of silence are aligned and visibly treated as hypotheses; QA pass. |
| `watched-eyes-evidence-update.png` | PASS | Contact sheet; HTML desktop/mobile; EPUB 768/390 | Effect estimate, uncertainty, and updated evidence boundary are visibly distinguished; QA pass. |
