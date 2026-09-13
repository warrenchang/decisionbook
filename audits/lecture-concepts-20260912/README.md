# Lecture-to-book coverage revision

The book now distinguishes **expectations changing outcomes** in Chapter 5 from **confirmation and motivated reasoning changing the treatment of evidence** in Chapter 10. Overconfidence was already discussed in Chapter 15, but its name was missing from the explanation and title. It is now a visible organizing topic, with corrected definitions and a practical calibration exercise.

## What changed

| Location | Revision and teaching purpose |
| --- | --- |
| Chapters 5 and 10 | Reciprocal links and a concrete distinction between changing an outcome and selectively testing a belief. Positive illusions and unrealistic optimism remain qualified rather than treated as guarantees of success. |
| Chapter 15 | Explicit overestimation, overplacement, and overprecision; corrected relative-ranking definition; interval-coverage exercise; separate planning-fallacy section; illusion of control with the later challenge to the choice-to-belief mechanism. |
| Chapters 3 and 6 | Task-switching costs; optional network, interoception, and allostasis lenses; common-currency terminology. Neural models remain separate from proven psychological mechanisms. |
| Chapters 7–9 | Explicit introspection, confabulation, dissonance, dual-process, and ecological-rationality terminology; a new dilution-effect explanation. |
| Chapter 11 | Joint/separate evaluation, evaluability, preference reversal, matching, and the prominence hypothesis. These are developed together because they concern how comparisons and response tasks change weight. |
| Chapters 12 and 13 | Explicit misinformation effect; context-dependent memory and encoding specificity. Recall, confidence, and accuracy are kept separate. |
| Chapters 18–22 | Normalization of warning risk; diversification bias versus naive 1/n allocation; positive/negative reinforcement, incentive salience, and urge surfing; explicit affective forecasting. |
| Chapters 25 and 29 | Clearer altruism/inequity distinctions and positive assortment; individualism/collectivism; optional Big Five lens separated from cultural stereotypes. |
| Chapters 30–35 | Foot-in-the-door, door-in-the-face, self-persuasion, Ben Franklin effect, pragmatic inference, and principled negotiation. ABT and narrative-index terminology is distinguished from validated evidence of message quality. |
| Chapters 40–42 | Explicit choice-overload, data-leakage, and algorithm-appreciation terminology within their existing substantive discussions. |
| Appendices A, E, and F | Decision trees; between/within-person and factorial designs; research reactivity, including demand, Hawthorne, John Henry, demoralization, anticipation, and survey effects; HARKing; matching illusion-of-control update in the evidence-status map. |
| Titles and index | All 42 titles reviewed; eight changed in this pass. The preceding concise titles were preserved. The concept index retains its existing entries and adds 56 routes into the revised material. |

See the [complete title review](chapter-titles.md) and [coverage map](coverage-map.csv). The [source-check record](source-checks.md) states which primary articles, abstracts, and methods sources were inspected.

## Course trace examples

Slide/page numbers below are one-based positions in the file; a number printed on a slide can differ.

| Lecture source | Relevant position | Book destination |
| --- | --- | --- |
| BE, `05. Biases.pptx` | Overconfidence sequence, slides 23–42; prominence, slide 115; normalcy bias, slide 124 | Chapters 15, 11, and 18 |
| BE, `08. Probability Judgment.pptx` | Joint/separate evaluation, slide 13; dilution, slide 14 | Chapters 11 and 9 |
| BE, `02. Anatomy of Decision-Making.pptx` | Networks, slides 38–42; interoception, slide 85 | Optional lenses in Chapters 3 and 6 |
| BE, `Neuroeconomics.pptx` | Context-dependent memory, slide 54 | Chapter 13 |
| BE, `19. Mental Acounting.pptx` | Diversification and the 1/n heuristic, slide 51 | Chapter 20 |
| BE, `05. Biases.pptx` | Big Five, slide 86 | Chapter 29's optional personality lens |
| DPN, `DPN04. Influence & Persuasion.pptx` | Self-authored reasons, slide 65; foot-in-the-door, slide 69; Ben Franklin effect, slide 70 | Chapters 30 and 34 |
| BE, `17. Conduct Research in Behavioral Economics.pptx` | Responses to evaluation, slide 33; factorial design, slides 93–94 | Appendix E |

The source inventory records the full paths and checksums, including the Aalborg/Syddansk copies and archived editions.

## What stayed in its existing home

The marshmallow-test evidence belongs primarily in Chapter 19; ego depletion and its replication record belong in Chapter 39 and Appendix F. The Prisoner's Dilemma is worked through in Chapter 25, while beauty-contest unraveling belongs in Chapter 24. Integral emotion and arousal are developed in Chapter 6 before their applications to judgment. Curiosity's information-gap account is developed in Chapter 32. These are not omissions merely because they are absent from another related chapter.

The screen also considered likelihood-ratio notation, the Kelly criterion, experience-weighted attraction, quantal response, and group polarization. It did not establish a separate core-lecture requirement for these additions. Their absence was not filled by inserting extra formal models or investment prescriptions. The decisions and false lexical matches are recorded in [screen-resolutions.json](screen-resolutions.json).

## Method and limits

The audit inventoried **671 source paths**, representing **328 distinct files** after checksum deduplication, from the Behavioral Economics and Decision, Persuasion, and Negotiation note folders in both university storage roots. Current decks, original topic units, archived variants, and supporting documents were included. The extraction produced no file-level errors; it covers text, tables, and available speaker notes, not a fresh visual interpretation of every image-only slide.

A reproducible screen mapped **512 candidate concept–location pairs** to source passages and the canonical chapter bodies. These are not 512 distinct required course concepts, and a keyword hit is not proof of adequate explanation or scientific validity. Chapter outlines, the central concept passages, apparent gaps, and the consequential additions received editorial review. Source matches in the CSV remain retrieval aids; documented false matches and alternative teaching homes are not counted as omissions.

This is a curriculum and placement revision, with targeted scientific verification of additions. It is not a claim that every existing citation in the entire book has been freshly reverified. No new studies were invented, no raw lecture files were edited, and no existing reference entries were removed from the pre-revision source snapshots. New material is integrated into the narrative or optional lenses instead of adding a separate catalog of biases.

The sources, snapshots' hashes, source-level patch, title manifest, and verification reports in this folder make the revision reviewable. The canonical book remains the `.qmd` files; HTML and EPUB are generated from them. No commit or push is part of this revision pass.

## Verification

Both Quarto builds completed. All 42 chapter openings pass in HTML and EPUB: one subtitle, an unheaded opening scene, Core Idea, Learning goals, and retained legacy anchors. The HTML check covered 61 pages, 8,100 local links, and 2,966 local fragments, with no broken targets. All chapter and appendix reference lists are alphabetized; the master bibliography contains 870 entries. EPUB release QA passed. Thirteen selected lecture files retained their original checksums.

Desktop and phone previews were inspected, including the revised titles in Chapters 10, 15, and 42. EPUB previews were checked in a browser; native e-reader applications were not tested. See [verification.json](verification.json), [HTML links](html-links.json), and [EPUB release QA](epub-release-qa.md).
