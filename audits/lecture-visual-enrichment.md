# Lecture-note visual enrichment audit

Date: 2026-08-30

## Scope and method

The visual pass covered the complete Behavioral Economics `Lecture Notes` tree rather than only the four legacy decision-course decks. The inventory contained 91 PowerPoint files (85 unique package hashes), 3,651 embedded-image occurrences representing 1,981 unique image hashes, and 42 loose image files. Hidden slides were retained in the inventory. Every unique embedded image was reviewed through 31 numbered contact sheets; the 42 loose files were reviewed through a separate contact sheet. The earlier occurrence-level audit of 396 images from the legacy DPN decks remains in `slide-images-reviewed.csv`.

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

## Already present and retained

- The author's photograph of his daughter counting on her fingers remains in Chapter 4 because it makes the transition from effortful rule-guided processing to practised automaticity memorable.
- The author's €20-note photograph remains in the behavioral-finance chapter because it anchors three distinct efficiency claims in one concrete observation.
- Existing book-native diagrams and source-verified study redraws remain the preferred treatment where the slide image was protected, visually cluttered, or already represented more accurately in the book.

## Deliberately excluded after review

- The fish-feeding sign, nearby visitors, and preschool-door photographs were not used. Their meanings are ambiguous, identifiable people or settings are visible, and the caveats needed to avoid overclaiming would outweigh their teaching value.
- Film stills, advertisements, commercial interfaces, book covers, publisher graphics, memes, logos, and stock photographs were not redistributed when reuse rights were not established.
- The 42 loose evolutionary-game images were not inserted. Most are unlabelled simulation snapshots or third-party portraits/graphics; without documented parameters, seed, run history, and licence, they would be neither reproducible evidence nor safe decoration.
- A beauty-contest distribution was not added because the existing ladder and empirical comparison already teach the mechanism, and exact published bin frequencies were not recovered in this pass.
- The Ariely–Wertenbroch deadline-result chart was not added because the source data are subject to an integrity/retraction concern. The book should not turn that result into a visual anchor.

## Withheld pending evidence

The current `DPN07. Communication & Connection.pptx`, slide 5, object `Picture 10` (SHA prefix `581e55fb…`) contains a before/after conversation-rating chart not represented in the legacy ledger. It has no recoverable source, sample description, measure definition, uncertainty, or underlying data in the deck. It is therefore withheld from the book and must not be described as evidence unless those items are recovered and verified. A future version should redraw it rather than reuse the slide artwork.

## Reproducibility notes

- The SVG source and PNG fallback for the lie-cue figure are both retained in `figures/`.
- Source-image hashes and dispositions remain traceable through `slide-images-reviewed.csv` and `lecture-notes-final-integration.csv`.
- The generated remote is a new original replacement. Its final SHA-256 is `ba46447fecb81cd72433ded756438fac1203bc2e95adde40359ce7a3f5092e89`.
- No original lecture-note file was modified.
