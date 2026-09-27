# Book-wide lecture-note review — 27 September 2026

## What changed

Read the main exposition of all 42 chapters and Appendices A–G, together with the preface, reading guides, and seven part introductions. Compared the book with the current Behavioral Economics and Decision, Persuasion, and Negotiation lecture decks, then followed selected additional and archival materials where they supplied distinct examples. Implemented revisions in 33 chapters, six appendices, the reading guide, and the concept index. Chapter 29's earlier preschool observation was preserved; it is not counted as a new example from this review.

The revision develops missing comparisons and calculations in their existing conceptual homes. It also qualifies claims, connects related discussions, updates the example and concept indexes, and corrects a portable-tool chapter pointer. It does not add a parallel catalogue of slide summaries. No figure assets were changed; the accepted face and framing illustrations were preserved.

| Book area | Additions or improvements |
| --- | --- |
| Chapters 1–7 | Testable behavioral models; own-name attention and head-up displays; Thatcher configuration, conditioned sound reports and infant speech learning; beer-disclosure timing, milkshake labels, hotel attendants, stress reappraisal and aging; incidental value, masked incentives, purchase prediction and name letters; split-brain explanation. |
| Chapters 8–14 | Worked production/growth reflection questions; nested word categories; an illustrative Barnum profile; price-before-product sequencing; choose/reject framing with a close replication; environmental product cues and false memory; compound project probabilities and two Monty Hall host rules. |
| Chapters 15–22 | Lottery betting records; wetsuit inventory and controlled risk lotteries; possibility/certainty contrasts; prior-gain/loss arithmetic; language and saving with relatedness controls; reward devaluation and habit; classic and modern lottery well-being studies. |
| Chapters 23–29 | Cognitive-hierarchy arithmetic, the €50 auction and acquisition alternatives; complementary platforms and physical standards; a four-person public-goods game, conditional cooperation, warm glow, punishment and antisocial punishment; graffiti and social-feed expression; equity-premium explanations and GameStop; smoke-room bystanders; contradiction and Starbucks-chair comparisons. |
| Chapters 30–42 | Edited-film versus park-footage comparison; Gettysburg/ABT analysis; equal gains above alternatives and deadline disclosure; a fee-schedule cliff; process imagery; dating-site screening, calorie-label placement, Copenhagen Airport paths and shopping cues. |
| Appendix B | Explicit hypothetical reproductive-weight tables for an arms race and hawk–dove invasion, with worked population dynamics. |
| Appendix C | Lucky-golf-ball study versus larger replication attempts; luck reports distinguished from putting performance. |
| Appendix D | Direct response versus strategy method, matching and privacy, incentive compatibility; school-meal selection and noncompliance calculations; baby-bonus anticipation, correcting the lecture's 2014 date to 2004. |
| Appendix E | Working-memory practice versus transfer, with active controls and a meta-analysis. |
| Navigation | 32 new example-index rows; 21 new concept entries and three sharpened entries; learning instructions that ask readers to reconstruct a comparison and vary its assumptions. |

Chapters 2, 18, 30, 33–35, 37, 41 and 42 were reviewed and retained because their relevant mechanisms and examples were already developed. The range ledgers explain these decisions. Retaining a chapter does not certify every historical citation in it anew.

## Evidence and source scope

The read-only inventory covers **345 files**: 170 PPTX, 150 PDF and 25 DOCX, with 23 exact duplicates and 322 unique extractions. The 16,227 units in the unique extractions include background books and readings. **These inventory counts are not claims that every file, page, speaker note, image or linked video was read.** Current decks received the detailed review described in the range ledgers; older variants and background readings received explicitly recorded levels of screening or selective review.

- [Source manifest](source-manifest.json): exact paths, hashes, extraction locations and lengths. Its `visual_review_units` field identifies candidates flagged by extraction; actual visual inspection is documented in the range reports.
- [Foundations review](foundations/README.md): Chapters 1–14, every-slide accounting for eight current decks, archival follow-up, and source-image inspection.
- [Risk and social coverage](risk-social/coverage.csv): Chapters 15–29, lecture ranges, existing coverage, additions and justified omissions.
- [Influence and design review](influence-design/review-notes.md): Chapters 30–42, 69 source-range decisions, primary-source verification and explicit access limits.
- [Methods and book structure](methods-and-book-structure.md): appendix review, research-method lectures, source corrections, evidence checks and evolutionary examples.

New empirical claims were checked against primary papers, official reports, or primary article abstracts and metadata. Where full text was unavailable, the claim was confined to material actually inspected and the limit recorded. All new local references were merged into the master bibliography, which now contains **1,248 unique entries**, 56 more than at the start of this review. This is bibliographic synchronization, not an independent re-verification of every pre-existing work.

Claims about individual motives, hormonal mechanisms, neural pleasure, national character and long-term health are bounded by the designs. Observational associations remain observational. Contrasting studies and replication outcomes accompany several memorable older examples. New payoff and contract calculations are labeled hypothetical; no invented values are reported as empirical findings. Administrative instructions, unverified historical numbers, redundant anecdotes and proprietary role briefs were not reproduced.

## Reproducibility and verification

`extract_sources.py` preserves the extraction procedure, including PowerPoint presentation order and actual slide-to-notes relationships. Source files remained immutable: [source-integrity-check.json](source-integrity-check.json) reports 345 checked and zero changes. Scratch extracted text is deliberately outside the repository.

Run `python3 audits/book-review-20260927/check_worked_examples.py` to reproduce the new school-meal, evolutionary, probability, inventory, lottery, game and fee calculations. Results are in [worked-example-checks.json](worked-example-checks.json). The numbers are teaching examples, not statistical results.

Independent reviewers checked additions outside their own authorship ranges: [Chapters 15–29](foundations/independent-risk-social-review.md), [Chapters 1–14 and 30–42](risk-social/independent-foundations-influence-review.md), and [Appendices B–E](influence-design/independent-appendix-review.md). No material issue remained. Two precision edits were implemented: distinguish the constant marginal incentive to withhold a public-good token from the level of earnings, and describe the fee-cliff example's increase in gross sale price separately from net proceeds. This is a targeted scientific and editorial review, not a replication of the original studies.

## Final validation

| Check | Result |
| --- | --- |
| Full HTML build, followed by targeted renders for the final wording and anchor repairs | Pass; 62 configured pages. |
| Full final EPUB build | Pass; released file is newer than all source/build inputs and matches the staged release. |
| Canonical source QA | Pass; zero errors, zero warnings, zero unresolved author–year citations. |
| Master-reference union | Pass; 1,248 unique references. |
| HTML file and fragment links | Pass; 7,850 local links checked, zero issues. |
| EPUB structure, resources, navigation and every internal content link | Pass; zero issues in the release QA report. |
| Source/HTML/EPUB float references | Pass; 107 figures and 168 tables, zero issues. Four tables were added in this review. |
| Worked calculations | Pass; reproducible exact-fraction checks and independent review. |
| Source-file integrity | Pass; 345 source files checked, zero changes. |
| Whitespace and file modes | `git diff --check` passed; no file-mode changes. |

Representative visual inspection covered the new software-sharing table on a 1280-pixel desktop and a 390 × 844 phone viewport, expanded evolutionary and noncompliance notes on mobile, and the actual EPUB software/noncompliance pages with their packaged styles. The school-meal headers were shortened after the first mobile inspection; all values remain readable without page-level overflow. EPUB preview pages were byte-identical to the final release. This was a browser preview of EPUB XHTML, not a test in every native e-reader. No complete screenshot audit of all existing figures is claimed.

Link checking caught and repaired five initially broken EPUB links, then two HTML-only targets: the new guide now links to stable section anchors in the tools and example index; the former menu-section anchor is preserved; and the newsvendor anchor sits outside a callout heading so it survives both formats. The final checks above were rerun after those repairs.

Machine-readable evidence: [build verification](build-verification.json), [HTML links](html-link-check.json), [float references](float-reference-qa.json), and [worked examples](worked-example-checks.json). The repository-level [source QA](../../QA_REPORT.md), [citation audit](../../CITATION_AUDIT.md), and [EPUB QA](../../EPUB_QA_REPORT.md) describe the final artifacts.

All changes are local and reviewable. No commit or push was performed for this editing task; earlier user edits remain preserved.
