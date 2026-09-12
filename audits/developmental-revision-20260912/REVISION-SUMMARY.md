# Revised edition — 12 September 2026

The revised local edition incorporates the developmental review's verified scientific corrections and its central editorial direction across all 42 chapters, seven part openers, front matter, and supporting appendices. The edits preserve varied sentence rhythm, scientific qualifications, and the established chapter structure. They make findings concrete before explaining their limits, introduce fewer concepts at once, and connect related discussions instead of repeating them.

Source baseline: `227f62ed57dedc46b6c1d3bef2ed67b4e3612d3b`. The six supplied review files are preserved unchanged. This is a local revision; no commit, push, or external publication was performed.

## What changed

### Scientific accuracy and usable evidence

- Corrected Chapter 15's impossible union probability. The three risks imply a combined probability between 20% and 45%; independence would give 38.8%. A component delay and a missed final deadline after schedule slack are explicitly different outcomes.
- Corrected the Iowa Gambling Task's 1994 introduction versus the 1997 anticipatory-response report, the Stanovich mechanism attribution, Miller and Ross's skeptical argument, and the endowment-effect chapter pointer.
- Separated choice overload's near-zero meta-analytic average from its conditional moderators; distinguished marshmallow-task reliability experiments from the attenuated longitudinal association.
- Rewrote Chapter 31 around what Small and colleagues actually found: adding statistics reduced donations relative to the identifiable-person condition. Immediate generosity and informed assistance are distinct goals; separating or sequencing information is a proposal to test, not an established remedy.
- Added procedures, denominators, and published comparisons where they make the result intelligible: Milgram, Asch, bystander helping, the outbreak problem, anchoring, question wording, dissonance, mental accounting, negotiation behavior, and checklists. The relevant qualifications remain adjacent.
- Added worked calculations in Chapters 16 and 17, clearly separating model implications from observed choices.
- Corrected additional citation/claim mismatches encountered in communication, persuasion, negotiation, and smartphone discussions. Chapter-specific source records identify the papers and the limits of verification.

The independent propagation check covered all twenty cases in Appendix F's two evidence maps against the claims actually made in the 42 chapters. Eleven cases remain appendix-only; their presence in the map does not require adding them to chapters. The nine cases used in the chapters now carry the relevant qualification or update.

### Organization and reader involvement

- Made Chapter 1's six examples visible in sequence, with a consistent heading hierarchy.
- Placed the five comparison tables and Chapter 1's commercial examples in the visible reading route. Optional research depth remains optional.
- Consolidated Maslow/Kenrick in Appendix B, the outbreak demonstration in Chapter 12 with its model in Chapter 17, choice overload in Chapter 40, and repeated psychological-safety explanations through purposeful references to Chapter 28. Removed a duplicate negotiation priority table while preserving its legacy anchor and linking the developed tool.
- Added substantive outbound chapter links throughout the book. On a consistent source count, explicit links between numbered chapters increased from 66 to 144; all 42 chapters now have at least one. This count excludes navigation, appendix links, and prose-only pointers.
- Replaced the seven generic part captions with the questions each part develops, and corrected running-case promises to match the cases readers actually encounter.
- Added concise applications concerning designed digital attention, moral judgment, and decisions under time pressure; clarified forecasting terminology without creating extra survey chapters.
- Rendered Appendix C's existing taxonomy as 12 core tools, 3 quick checks, and 15 specialized extensions, with explicit text labels as well as color. Five existing commitment-before-reveal exercises now have a consistent “Predict first” label.
- Strengthened the preface's practical promise: locate the decision function involved, distinguish competing explanations, and choose a check that could change the diagnosis.

### Figures and captions

Eleven priority diagrams were recomposed on a 760-unit canvas with readable type, deliberate connector geometry, and compact layouts: the two Chapter 1 decision diagrams, heuristic substitution, context mechanisms, fluency, habit formation, urge observation, the silence diagnostic, communication grounding, conversation needs, and the digital action-cue illustration. The communication-calibration chart was separately corrected to distinguish sender forecasts from receivers' later confidence and to label approximate values honestly.

The layout now uses an explicit `phone-fit` class shared by HTML and EPUB instead of a filename allowlist. It covers 41 placements of 40 compact SVG assets, including the previously compact diagrams. Captions and alternative text were reconciled with the drawings; the digital advertisements are explicitly illustrative rather than the original test stimuli. All eleven new compact diagrams have deterministic source generation and PNG fallbacks.

**Visual scope:** this edition does not claim to have redrawn all 80 figures proposed in the review. The other 69 referenced SVG assets retain their existing composition and, where necessary, a contained horizontal reading pane. Their loading, alternative text, and page containment were checked; their retained artwork received a contact-sheet review. The more detailed independent inspection applies to the twelve changed figures. A complete portrait conversion of the remaining wide artwork is a separate design pass, not a completed result of this revision.

## References and information preservation

The bibliography contains **849 distinct works, up from 838**, with **11 added and none removed at book level**. Three chapter-local references—Bridgman et al. (2019), Kesebir et al. (2010), and Peterson and Park (2010)—now accompany their fuller discussion in Appendix B. They remain in the master bibliography. Tversky and Kahneman (1981) citation variants were merged and enriched with the DOI, rather than treated as separate works.

The reference sorter now compares author-name sequences, then dates and titles; punctuation such as `&` no longer puts coauthors in the wrong order. All chapter and appendix lists, including the habit chapter, and the master bibliography were reordered without changing their reference bodies.

Some material was shortened: a secondary Gandhi anchoring illustration, repeated definitions, duplicate tables, and repeated presentations of the same experiment. The fuller treatment or distinct application remains where the surrounding chapter needs it. This is an editorial consolidation, not a claim that every original sentence remains.

## Recommendations adapted or rejected

- Preserved working legacy table and section IDs. Their strings do not determine Quarto's displayed numbering; wholesale renaming would create unnecessary link risk. No original explicit anchor was lost.
- Kept the existing Core Idea sections in Chapters 20, 22, and 27, and the existing natural-frequency figure in Chapter 14. The proposed additions would duplicate material already present.
- Corrected the review's proposed Milgram wording: all forty reached 300 V, five stopped there, and twenty-six reached 450 V. “All went past 300” would introduce an error. Burger's later stopping protocol is described separately.
- Kept the outbreak demonstration in Chapter 12, where the reader makes the framing choice, and used Chapter 17 for the formal model.
- Retained Chapter 42's final-paper sample of 5,172 agents; the contrary suggested correction was not supported.
- Did not treat 824 findings, numerical density, color counts, or the presence of a qualification as automatic editing targets. Study numbers were added when verified and useful, not to meet a quota.

## Verification and records

The final verification record is `VERIFICATION.md`; machine-readable reports and hashes accompany it. It distinguishes source/package checks, browser geometry checks, and actual visual inspection. Browser rendering of extracted EPUB XHTML tests reflow and content; it does not certify every native EPUB reader.

Detailed chapter edits and primary-source checks: `chapters-01-14.md`, `chapters-15-28.md`, and `chapters-29-42.md`. Independent checks: `evidence-propagation-check.md`, `reference-preservation-check.md`, `independent-figure-review.md`, and `reading-route-qa.md`. Figure inventory, dimensions, and revision counts are reproducible from the scripts in this directory and `scripts/build_reading_figures.py`.
