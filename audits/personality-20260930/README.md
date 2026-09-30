# Personality integration — 30 September 2026

## Editorial placement

- Chapter 29: promote the short Big Five note into the main reading path; preserve its existing anchor. Distinguish traits, situations, culture, and identity; develop repeated-observation and replication evidence before the ReGPC findings and decision applications.
- Appendix B: explain quantities and causal designs without repeating the Chapter 29 study summary.
- Chapter 39: connect personality-change evidence to the existing student-writing case and to assessment across occasions.
- Chapter 10: link the Barnum example to measured personality evidence. Update concept and example indexes, chapter references, and the generated master references.
- No new figure: the five-domain comparison benefits from a short table; no plot is needed to restate the study summaries. Table questions are explicitly book applications, not validated test items.

## Source verification record

Primary published papers or author/institution-hosted versions were checked. No preprint numbers substituted for the 2026 Nature version. This ledger identifies the passages used; the book contains the evidence synthesis.

| Source | Primary source inspected | Relevant sections | Use and interpretation check |
| --- | --- | --- | --- |
| Schwaba et al. (2026) | https://www.nature.com/articles/s41586-026-10992-9 | Population meta-analysis; SNP heritability; polygenic prediction; familial confounding; Mendelian randomization; Discussion | Discovery markers, population estimates, prediction, and causal inference kept distinct. Advance online publication metadata confirmed; no invented volume or pages. |
| Soto & John (2017) | https://www.colby.edu/wp-content/uploads/2013/08/Soto_John_2017.pdf | Domain/facet structure and instrument development | Definitions only; no questionnaire items reproduced. |
| Fleeson (2001) | https://personality-project.org/revelle/syllabi/classreadings/fleeson.2001.pdf | Three experience-sampling studies and Discussion; indexed published text | State variation and aggregate stability; scope tied to sampled weeks. No unverified sample count added. |
| Soto (2019) | https://www.colby.edu/wp-content/uploads/2019/05/Soto_2019.pdf | Methods; Results; limitations p.725 | Replication evidence explicitly identified as cross-sectional self-report. |
| Howe et al. (2022) | https://findresearcher.sdu.dk/ws/portalfiles/portal/204196614/Howe_2022_Within_sibship_genome_wide_associat.pdf | Introduction; within-sibship/population comparison | Method comparison; direct genetic effects not equated with environmentally unmediated effects. |
| Davies et al. (2018) | https://research-information.bristol.ac.uk/files/162966737/bmj.k601.full.pdf | Assumptions; pleiotropy; intervention interpretation | Genetic correlation separated from causal inference; lifetime genetic contrasts distinguished from interventions. |
| Stieger et al. (2021) | https://doi.org/10.1073/pnas.2017548118 | Indexed published Methods and Results, including participant flow and follow-up | Immediate versus delayed access, unequal wait/intervention duration, attrition and observer ratings retained. No within-person effect size represented as a randomized contrast. |

## Verification

Source and citation QA and source float checks passed after the initial edit. Independent source and teaching reviews found no major scientific errors. Two requested corrections were implemented: delayed access described as an offer rather than universal receipt, and trait change distinguished from downstream health or work benefits. 

Completed verification:

- `quarto render --profile html` and `quarto render --profile epub`: both completed successfully; staged and released EPUB synchronized.
- `python3 scripts/sync_references.py --check`: 1,260 unique references, synchronized.
- `python3 scripts/qa_quarto_book.py`: 0 errors, 0 warnings after the HTML render finished. An intermediate check during rendering saw temporarily unavailable generated pages; the completed-build check supersedes it.
- `python3 scripts/build_practice.py --check`: all generated practice sources current.
- `python3 scripts/qa_practice.py --rendered`: 280 questions, 49 sets; HTML and EPUB checks passed.
- `python3 scripts/qa_epub_release.py`: 0 errors.
- `python3 scripts/qa_float_references.py --rendered --epub-dir <fresh-extracted-EPUB>/EPUB`: 69 sources, 107 figures, 169 tables, 0 issues. Saved as `float-reference-qa.json` here.
- All three new/expanded section anchors appear exactly once in the EPUB.
- Browser inspection: Table 29.1 was readable at the default 1280-by-720 viewport, with no clipped cells or overlapping text. Followed Chapter 29 → Appendix B → Chapter 39 and verified the corrected delayed-access wording in the rendered page.
- Restored the pre-existing executable mode on `docs/parts/part-1.html` after Quarto regenerated it; no content was hand-edited in generated HTML.
- `git diff --check`: passed.

Changes remain local; no commit or push was requested for this revision.

## Follow-up: Hardy, Little, and personality development

Added after the earlier revision was committed as `8fb8c50`, in response to the request to discuss both books in Chapter 29. The two new subsections distinguish choosing a future self, lasting trait change, and purposeful departures from usual behavior. They reuse the student and meeting applications, link to Chapter 39's existing intervention discussion, and add concept/example index routes. Six references were added to the chapter and synchronized master bibliography. No new figure or assessment item was needed for this prose extension.

### Sources and inference boundaries

Book themes were checked against publisher descriptions and authors' own explanations; this record does not claim a cover-to-cover reading of either book. Study claims use published papers and author-hosted copies.

| Source | Primary source inspected | Design and use | Boundary retained |
| --- | --- | --- | --- |
| Hardy (2020), *Personality Isn't Permanent* | [Publisher description and metadata](https://www.penguinrandomhouse.com/books/607021/personality-isnt-permanent-by-benjamin-hardy-phd/); [author interview transcript](https://thementee.com/s4e4/) | Future-self goals, identity, relationships, and environment as a prescription for development | Attributed as Hardy's proposal; no claim that his complete program was experimentally validated. Clinical claims in marketing copy were not imported. |
| Little (2014), *Me, Myself, and Us* | [Publisher's original ebook metadata](https://www.hachettebookgroup.com/titles/brian-r-little-phd/me-myself-and-us/9781586489687/); author's conceptual article below | Traits alongside personal projects and flexible action | Uses the original PublicAffairs 2014 publication, not the later paperback date. |
| Little (2008) | [Author-hosted article](https://www.brianrlittle.com/articles/%EF%BF%BCpersonal-projects-and-free-traits/), especially free traits and restorative niches | Conceptual account of acting outside usual tendencies for valued projects | Recovery settings are presented as a proposal, not an experimentally established universal need of introverts. |
| Bleidorn et al. (2022) | [Published abstract and metadata](https://pubmed.ncbi.nlm.nih.gov/35834197/); [publisher supplement](https://supp.apa.org/psycarticles/supplemental/bul0000365/bul0000365_supp.html) | Meta-analysis: 189 longitudinal samples for rank-order stability (N = 178,503), 276 for mean-level change (N = 242,542) | Relative standing distinguished from average levels; observational developmental patterns do not establish effects of intentional change. |
| Hudson et al. (2019) | [Author-hosted published article](https://www.nathanwhudson.com/vita/pdf/Hudson%20et%20al.,%202019a.pdf), Table 2 p.845, Discussion and limitations pp.849–850 | 15-week student study; 377 initial participants, declining participation; self-reported challenge completion and traits | Completion was not randomized. Positive completion-by-time associations for extraversion, conscientiousness, and emotional stability; inconclusive agreeableness and negative openness association retained. No claim that merely choosing a goal causes change. |
| Jacques-Hamilton et al. (2019) | [Author-hosted article](https://jessiesun.me/publication/jacques-hamilton-2019/jacques-hamilton-2019.pdf), Methods and Tables 2, 6–7 | One-week randomized trial, n = 147, act-extraverted instructions versus active control | All book comparisons use the randomized active control, not the additional 76 archival participants. Overall positive-affect/authenticity gains distinguished from moderation: momentary tiredness/negative affect and retrospective authenticity costs in different low-extraversion ranges. No durable trait-change or restorative-niche claim. |

Independent source reviewers checked both groups of studies and all six reference entries. A teaching reviewer checked the narrative and applications. Implemented corrections: explicitly define free traits as departures from usual tendencies; avoid confusing assertiveness with sociability; retain the negative openness result; avoid implying uniform costs for introverts. The behavioral examples and practical synthesis are textbook applications, not reported treatment effects.

### Follow-up verification

- Full HTML and EPUB renders completed successfully. The released EPUB was synchronized with the newly rendered staged file; release QA reported 0 errors.
- Source/citation QA: 0 errors and 0 warnings. Master references: 1,266 unique entries, synchronized. Practice sources current; rendered practice QA passed for 280 questions and 49 sets.
- Rendered HTML and freshly extracted EPUB float checks: 69 sources, 107 figures, 169 tables, 0 issues.
- Both new section anchors occur exactly once in each format; both book titles and the corrected openness result appear in the released EPUB. Existing personality/genetics/self-construal anchors remain present in HTML.
- Browser inspection at 1280 × 720 confirmed readable paragraphs and headings in both new sections and working table-of-contents navigation. The temporary inspection tab was closed.
- Restored existing file modes on two HTML files changed by rendering. `git diff --check` passed. No commit or push was made for this follow-up.

## Title follow-up

Renamed Chapter 29 to **Personality, Culture, and Identity** to reflect its expanded scope. Updated chapter-name cross-references and the assessment blueprint title. Following the repository's filename convention, migrated the canonical source to `chapters/29-personality-culture-and-identity.qmd`, updated active links, and retained the old HTML URL as a redirect alias. The chapter's section anchors and subtitle were retained.

Verification: full HTML and EPUB renders completed; source/link/citation QA and EPUB release QA passed with no errors. Rendered practice checks passed for 280 questions and 49 sets. Confirmed the new title in HTML navigation/search and EPUB contents/heading, plus preserved personality section anchors. Browser inspection confirmed that the old URL retains its section fragment through the redirect and that the new title fits the chapter heading and sidebar. Filename synchronization and reference synchronization checks passed; `git diff --check` passed. No commit or push was made.

Final wording, at the author's request: **Culture, Personality, and Identity**, with canonical source `chapters/29-culture-personality-and-identity.qmd`. Both former HTML filenames redirect to the current chapter. Rebuilt HTML and EPUB after reordering; source/link/reference, rendered practice, and EPUB release checks passed. Verified the final title in HTML headings/navigation/search and EPUB headings/contents, and preserved the personality section anchors.
