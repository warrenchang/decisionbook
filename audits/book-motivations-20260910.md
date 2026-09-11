# Motivation revision — 10 September 2026

Updated the installed `huanren-writing-style` skill before revising the book. Its ABT guidance now requires the expectation, consequential tension, actors’ perspectives, stakes, and resulting question to be explicit in teaching motivations. It calls for verified resistance or disagreement in real cases and natural prose rather than visible ABT labels.

Reviewed all 42 chapter openings and the section/case setups that motivate their concepts. Also reviewed the preface, seven active Part introductions, evidence guide, six appendices, and navigation/reference/about material. Retained strong existing motivations and functional instructions. Revised 53 source files, including all 42 chapters; the net addition is 6,515 words.

Chapter 42 now opens with “why did better predictions provoke opposition?” while preserving the old anchor. It makes residents’ angry opposition to excavation priorities explicit, explains why uninspected households wanted reassurance, and follows the resulting change in city priorities. The opening leads to the question of how forecasts, public objectives, and authority over priorities should fit together. The dedicated Flint section returns to the policy reversal and settlement; the closing returns to the dilemma.

The account was checked against chapter 15 of the supplied *Power and Prediction* EPUB and the existing Webb, Abernethy, and Schwartz (2020) author report. The sources support anger among some residents left waiting and the change in prioritization. The text does not invent a street demonstration or treat all residents as opponents of AI.

## Verification

| Check | Result |
| --- | --- |
| Independent reading of all 42 opening motivations | PASS |
| Independent review of root motivations and Flint source support | PASS |
| Installed skill matches reviewed update | PASS |
| Skill frontmatter/name/description/placeholder checks | PASS with Ruby YAML fallback |
| Original reference blocks, equations, tables, figures, footnotes, and explicit IDs | Preserved |
| Source/HTML QA | PASS: 0 errors, 0 warnings |
| Reference synchronization | PASS: 834 unique references |
| HTML internal links and anchors | PASS: 61 pages |
| Current revised prose in both HTML and EPUB | PASS: 53 changed sources |
| EPUB package/release QA | PASS: 0 errors |
| Final whitespace check | PASS |

Quarto 1.10.18 rebuilt the HTML and EPUB editions. Assets were not edited in this task. Browser preview was not rerun because the local browser URL policy blocks it; no workaround was attempted. Verification used source review, independent editorial review, rendered-text checks, and structural release checks.

The skill’s supplied Python validator could not import PyYAML in either Python runtime. Equivalent YAML and skill-entrypoint checks passed with Ruby, and an independent reader reviewed the guidance itself.

Detailed dispositions are in `book-motivations-20260910-review.md`; check results are in `book-motivations-20260910-checks.json`. Temporary source snapshots, before/after passages, full opening inventory, and build logs are under `/private/tmp/book-motivations/`. Existing user edits were preserved; no commit, push, or publication was performed.
