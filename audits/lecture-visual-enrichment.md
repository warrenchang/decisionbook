# Lecture-note visual enrichment audit

Date: 2026-08-30

## Scope and method

The visual pass covered the complete Behavioral Economics `Lecture Notes` tree rather than only the four legacy decision-course decks. The live inventory contained 91 PowerPoint files (85 unique package hashes), 4,789 embedded-image occurrences representing 1,989 unique image hashes, and 42 loose image files. Hidden slides were retained in the inventory. Every unique embedded image was reviewed through 31 numbered contact sheets; the 42 loose files were reviewed through a separate contact sheet. The earlier occurrence-level audit of 396 images from the legacy decision-course decks remains in `slide-images-reviewed.csv`.

Selection followed four rules:

1. A photograph or illustration must perform a teaching job that prose or an existing figure does not already perform as well.
2. Direct reuse requires author ownership, an open licence, public-domain status, or another documented right. Protected journal artwork and uncertain slide images are not copied or cosmetically altered.
3. Study-result graphics are redrawn only from source-verified facts or data, with task, sample, uncertainty, and inferential boundaries preserved where material.
4. Captions distinguish an engaging illustration from evidence. Personal photographs are not presented as causal demonstrations.

## Added in this pass

| Source occurrence | Rights and treatment | Destination | Teaching function and boundary |
|---|---|---|---|
| `DPN02. Attention_Prediction_Expectation:s39:o1–o3` | Protected source components were not reused. A new vector mark is instantiated identically in number and letter contexts. | `figures/context-b13-demonstration.svg` plus EPUB PNG fallback; Chapter 6 | Gives the reader an immediate B/13 ambiguity demonstration. The figure and prose say that it demonstrates context-sensitive interpretation but does not identify a neural mechanism or measure an effect size. |
| `DPN04. Influence & Persuasion:s9:o1`, SHA-256 `31c371df…` | Author-owned family photograph; directly embedded | `figures/personal-mimicry-crossed-arms.jpg`; Chapter 22 | Makes a shared posture concrete and personal. The caption explicitly states that matching could reflect imitation, a shared situation, instruction, or coincidence; the photograph is not evidence for automatic mimicry. |
| `05. Biases:s73:o1`, SHA-256 `502f1a9a…` | Source-photo provenance unclear; no source pixels reused. A new, unbranded teaching photograph was generated from the underlying interface-simplification idea. | `figures/choice-architecture-simplified-remote.png`; Chapter 36 | Contrasts a control-dense remote with a selectively simplified one. The caption preserves the key boundary: fewer controls are not automatically better if necessary functions disappear. |
| `DPN06. Integrative Negotiation:s35:o1`, SHA-256 `f5f03c87…` | Journal artwork not reused. Exact published values were checked against Sporer and Schwandt (2007), Figure 1, and redrawn in the book's visual system. | `figures/lie-cues-belief-gap.svg` plus EPUB PNG fallback; Chapter 34 | Reproduces all nine observed rows; seven include student and professional belief comparisons, while two missing belief series are marked explicitly. The figure states that association is not individual diagnosis and redirects the reader from demeanor to claim verification. The lecture-slide attribution was corrected to Sporer and Schwandt (2007). |
| `00. Choice Architecture:s12:o1` and duplicates, SHA-256 `44455427…` | Published chart artwork not reused. The exact reciprocal relation `gallons per 100 miles = 100 / MPG` was independently drawn. | `figures/mpg-fuel-use.svg` plus EPUB PNG fallback; Chapter 36 | Makes the MPG illusion numerically visible: 10→20 MPG saves exactly six times as much fuel over 100 miles as 30→40 MPG. The caption identifies this as a mathematical conversion, not an estimated behavioral effect. |

## Added in the complete second review

| Lecture-note idea | Rights, evidence, and reconstruction | Destination | Teaching function and boundary |
|---|---|---|---|
| Stroop colour–word activity | The protected slide graphics and unverified classroom histogram were not reused. A new accessible vector activity was drawn from the standard task logic. | `figures/stroop-interference-lab.svg` plus PNG fallback; Chapter 4 | Lets readers experience how a practised reading response competes with the instructed ink-colour response. It is explicitly not an ability test or an estimate of a universal effect size. |
| Context-dependent perceptual comparisons | No lecture pixels were reused. Three measurable, book-native demonstrations were constructed with identical target geometry or luminance within each comparison. | `figures/perception-context-lab.svg` plus PNG fallback; Chapter 6 | Makes context-sensitive appearance inspectable and correctable by measurement without claiming one neural mechanism. |
| Choice-blindness switch sequence | The published face photographs and lecture screenshot were not copied. A generic abstract-card sequence was newly drawn. | `figures/choice-blindness-swap.svg` plus PNG fallback; Chapter 18 | Exposes the experimental intervention that separates the selected item from the item later explained. The caption and figure retain the boundary that many switches are detected. |
| “One egg or two?” assumed-choice question | New vector illustration based on the author's personal teaching example. | `figures/assumed-choice-eggs.svg` plus PNG fallback; Chapter 15 | Shows that a question can change the displayed option set and implied commitment, not merely reword equivalent facts. |
| Monty Hall protocol | New diagram derived from the standard probability structure; no game-show or lecture artwork was reused. | `figures/monty-hall-protocol.svg` plus PNG fallback; Chapter 12 | Keeps the host's constrained information rule and uniform random tie-break visible. It states that a different host protocol changes the inference. |
| Asch-style line-comparison task | The experimental photographs and slide imagery were not copied. A new, exactly measurable line task was drawn. | `figures/asch-line-comparison.svg` plus PNG fallback; Chapter 22 | Lets the reader separate private belief updating from the public cost of dissent instead of treating conformity as one mechanism. |
| Market-fairness vignette contrasts | Journal and slide artwork were not reused. Exact values were checked against Kahneman, Knetsch, and Thaler (1986): 82% (N=107), 21% (N=101), 71% (N=130), and 42% (N=123). | `figures/fairness-entitlements-redraw.svg` plus PNG fallback; Chapter 48 | Compares cost pass-through with opportunistic price changes and a surcharge with withdrawal of an equivalent discount. Separate 1984–85 Canadian samples are identified; the chart is descriptive, not a universal or normative fairness rule. |
| Schelling-style spatial sorting | Parameter-free lecture screenshots were replaced by an executable teaching model. The generator records grid, group counts, vacancy rate, neighbourhood, minimum same-group share, isolated-agent handling, sequential schedule, eligible-vacancy rule, pseudorandom implementation, seed, sweeps, moves, and outcome measure. | `scripts/build_schelling_sequence.py`; `figures/schelling-emergence.svg` plus PNG fallback; Chapter 47 | Shows how declared local rules can produce more aggregate sorting in one reproducible run. It does not infer motives or identify the cause of segregation in a real city. |

## Already present and retained

- The author's photograph of his daughter counting on her fingers remains in Chapter 4 because it makes the transition from effortful rule-guided processing to practised automaticity memorable.
- The author's €20-note photograph remains in the behavioral-finance chapter because it anchors three distinct efficiency claims in one concrete observation.
- Existing book-native diagrams and source-verified study redraws remain the preferred treatment where the slide image was protected, visually cluttered, or already represented more accurately in the book.

## Deliberately excluded after review

- The fish-feeding sign, nearby visitors, and preschool-door photographs were not used. Their meanings are ambiguous, identifiable people or settings are visible, and the caveats needed to avoid overclaiming would outweigh their teaching value.
- Film stills, advertisements, commercial interfaces, book covers, publisher graphics, memes, logos, and stock photographs were not redistributed when reuse rights were not established.
- The 42 loose evolutionary-game images were not inserted. Most are unlabelled simulation snapshots or third-party portraits/graphics; without documented parameters, seed, run history, and licence, they would be neither reproducible evidence nor safe decoration. Their strongest teaching idea is now represented by the declared and reproducible Schelling sequence.
- A beauty-contest distribution was not added because the existing ladder and empirical comparison already teach the mechanism, and exact published bin frequencies were not recovered in this pass.
- The Ariely–Wertenbroch deadline-result chart was not added because the source data are subject to an integrity/retraction concern. The book should not turn that result into a visual anchor.

## Withheld pending evidence

The current `DPN07. Communication & Connection.pptx`, slide 5, object `Picture 10` (SHA prefix `581e55fb…`) contains a before/after conversation-rating chart not represented in the legacy ledger. It has no recoverable source, sample description, measure definition, uncertainty, or underlying data in the deck. It is therefore withheld from the book and must not be described as evidence unless those items are recovered and verified. A future version should redraw it rather than reuse the slide artwork.

## Reproducibility notes

- SVG sources and PNG fallbacks are retained for every new vector figure in `figures/`.
- Source-image hashes and dispositions remain traceable through `slide-images-reviewed.csv` and `lecture-notes-final-integration.csv`.
- The generated remote is a new original replacement. Its final SHA-256 is `ba46447fecb81cd72433ded756438fac1203bc2e95adde40359ce7a3f5092e89`.
- `scripts/build_schelling_sequence.py` regenerates the spatial-sorting figure deterministically with seed `20260830`; the illustrated run reaches a no-move sweep after four sweeps and raises average same-group-neighbour share from 0.48 to 0.68.
- Source-level geometry QA passes for all 94 configured SVG figures. The rendered-book pass loads all 102 HTML figure placements at desktop and phone widths and all 101 EPUB placements at 768 px and 390 px with no broken images or page overflow. The eight additions were captured and visually inspected in both formats.
- No original lecture-note file was modified.
