# Literature-review appendix and validity connections

Revision date: 13 September 2026.

## Scope and reading order

Added **Appendix E, Conducting and Writing a Literature Review**, before the experimental-methods appendix. The methods appendix is now **F** and the research-integrity appendix is **G**. Existing methods and integrity filenames and redirects were retained to preserve their URLs. HTML/EPUB configuration, reading guides, concept index, chapter references, and the lecture-integration report generator follow the new order.

The new appendix follows one question about automatic saving arrangements through scope, search and selection, evidence extraction, thematic synthesis, a defensible gap, and the written argument. It includes four usable tables and a review-plan exercise. It explains that a review can stand alone and that a new experiment is only one possible next step.

Appendix F now connects probability sampling to population generalization, an aspect of **external validity**, and random assignment to the **internal validity** of a causal comparison. The text distinguishes both from guarantees: sampling requires attention to coverage, selection probabilities, and nonresponse; assignment creates comparable groups in expectation, with implementation, attrition, and spillover conditions still relevant. The clinic examples contrast a volunteer RCT with a probability sample whose treatment is selected by staff. The sampling/assignment illustration, caption, alternative text, generator, and PNG companion use the same distinctions. Other methods figures and generated study data were not regenerated.

## Teaching-source provenance

Primary teaching source, read without editing:

`/Users/ra25fi/Library/CloudStorage/OneDrive-SyddanskUniversitet/Teaching/Behavioral Economics/01_Teaching_Materials/Lecture Notes/BE2026/How to Write Your Term Paper - Recording.pptx`

Title: *How to write your term paper: From an interesting puzzle to an evidence-based answer*. Huanren Warren Zhang, University of Southern Denmark, Behavioral Economics, Autumn 2026. All 48 slides and the associated substantive speaker notes were inspected through the presentation XML. This was a text/content adaptation; the deck's visual design was not audited.

SHA-256: `c5ba482dbc7d58d1c32688ba0bb7974219173f6fcd98fb513e977d9061e71be7`.

| Slide positions | Adaptation |
| --- | --- |
| 7–12 | Topic, consequential question, boundaries, and preliminary search |
| 14–17 | Motivation through context, an honest difficulty, and the review's response |
| 19–21 | Distinct section roles and theory that sharpens comparisons |
| 23–25 | Search terms, selection criteria, citation trails, and version records |
| 26–29 | Evidence matrix; design, uncertainty, interpretation, and generalization |
| 31–35 | Thematic synthesis, comparison of outcomes/designs, and qualified conclusions |
| 37–43 | Traceable citations, paraphrase, reverse outlining, and revision |
| 45–46 | A concrete plan for the next review step |

Course-specific page limits, source-count requirements, deadlines, group size, and assessment rules were not transferred. An older research-question guide was consulted for context, but the newer lecture supplied the pedagogical workflow.

## Scientific and bibliographic review

The savings example uses **three deliberately selected teaching studies**, not an exhaustive or current review. Madrian and Shea (2001) supply an employer-policy/cohort comparison; Chetty et al. (2014) distinguish additional saving from account shifts using Danish administrative and quasi-experimental evidence; Blumenstock et al. (2018) randomize contribution defaults and matching among employees who already had accounts. These differences are explicit in the table and synthesis.

Primary-source verification checked these design descriptions and qualitative findings. Review corrections acknowledge the mechanism experiments already in Blumenstock et al.; describe their imprecise displacement measures; and prohibit treating the selected three-paper set as evidence of an unfilled literature gap. The clinic bridge is explicitly conditional and illustrative, with no assertion that its proposed question is currently novel. Madrian and Shea's 2002 erratum concerns a production error in the figures; this revision neither reproduces those figures nor depends on that error.

Methodological sources were checked for the claims used: Pautasso (2013), Snyder (2019), Page et al. (2021), and Stuart et al. (2011). PRISMA is described as reporting guidance, not a review-conduct method or quality certificate. A meta-analysis is distinguished from a systematic review. The author's lecture is identified as unpublished teaching material.

Seven works were added to the synchronized bibliography: Blumenstock et al., Chetty et al., Page et al., Pautasso, Snyder, Stuart et al., and Zhang's lecture. The existing Madrian–Shea entry in Chapter 40 was enriched with the verified DOI and matched to the new appendix to avoid a duplicate. Comparing the master list with HEAD confirmed that all 870 previously listed works remain, with this one bibliographic enrichment and seven additions. The synchronized list now contains **877 unique reference entries**. Reference blocks in new Appendix E and methods Appendix F are alphabetized.

## Verification

- Both complete Quarto builds succeeded: 62 configured sources, 42 chapters, and appendices A–G.
- Source QA: **0 errors, 0 warnings**. Reference synchronization: **PASS, 877 entries**; new Appendix E's seven and methods Appendix F's 17 reference entries are alphabetized.
- HTML navigation: **PASS** across 62 pages, 2,356 main-content local HTML link placements, 685 search destinations, and 126 appendix-labeled links. All sidebars show A–G in order. Report: `literature-review-appendix-20260913-navigation.json`.
- HTML figure checks: **PASS**, 118 placements at desktop and phone widths. Focused inspection checked the new appendix opening, study-comparison table, and revised sampling figure. Tables use the existing contained horizontal reading panes on narrow screens; the sampling figure fits the phone column. DOM checks found no page overflow. Report: `literature-review-appendix-20260913-layout.json`.
- EPUB release QA: **PASS, 0 errors**, including package integrity, all internal links and fragments, all 62 sources, correct A–G navigation, and image alternative text. Initial link failures were corrected with explicit fragments and an HTML-only methods heading anchor before the final rebuild. Report: `../EPUB_QA_REPORT.md`.
- EPUB visual QA: **PASS**, 64 XHTML documents and 116 image placements at 768px and 390px, with no broken images or page overflow. Focused screenshots confirmed readable Appendix E openings, the complete three-study table (Table E.3), and the sampling/assignment diagram (Figure F.2) at both widths. The EPUB study table fits at phone width. Reports: `rendered-epub-figure-qa.json` and `literature-review-appendix-20260913-epub-layout.json`.

Earlier book-wide editorial changes in the working tree were preserved. This revision is local; no commit or push was performed.

## Update: 14 September 2026

At the author's request, removed the unpublished lecture-slide reference and both in-text citations from Appendix E. The instructional material remains, supported where appropriate by its published methodological sources. The synchronized bibliography now contains 876 entries; no published study was removed. The teaching-source record above documents the revision's provenance, rather than a citation retained in the book.
