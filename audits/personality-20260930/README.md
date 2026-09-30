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

