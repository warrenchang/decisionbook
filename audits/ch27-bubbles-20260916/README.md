# Chapter 27: bubbles expansion, 16 September 2026

The canonical source is `chapters/27-markets-mispricing-and-bubbles.qmd`.

## Scope and source provenance

The principal coverage target is the 63-slide BE2026 `BE10. Asset Bubbles.pptx`, including its 15 hidden slides, notes, and substantive embedded charts/tables. The older `14. Asset Bubbles.pptx` was compared for historical content. `BE09. Behavioral Finance.pptx` was inspected for context; this revision expands the bubbles material and preserves the existing finance discussion rather than attempting a separate full revision of the finance lecture.

`sources.json` records exact source paths and SHA-256 hashes. The corresponding AAU and SDU copies matched for all three files. No lecture source was edited. `slide-coverage.csv` maps every slide of the principal deck to its chapter destination or explains why administrative, decorative, duplicate, or unsupported material was not copied. Important concepts and study findings are integrated in prose; slides are not reproduced verbatim.

## Editorial and scientific decisions

- All historical episodes on the lecture timeline are represented, with fuller accounts of tulipmania, South Sea/Newton, Mississippi, 1929, dot-com, housing, and 1987. Asset booms, credit booms, crashes, and systemic crises remain distinct.
- Goldgar's archival account qualifies tulipmania legends. Extreme price-to-income anecdotes and the source's unverified tulip-index reconstruction are not presented as measured representative data.
- Odlyzko's primary reconstruction supports Newton's early sale, later repurchase and losses, but not bankruptcy or a single exact loss figure. The famous quotation and modern-pound conversion are not repeated.
- P/E is not a literal payback period, and equity valuation uses an appropriate required return. Terminal valuation, the growth-rate sensitivity example, the known expected-dividend benchmark, and risk aversion are distinguished.
- The 2000 survey result concerns respondents, not the whole population or proven trading behavior. Broad NASDAQ and the study's internet-stock portfolio are distinguished.
- Historical graphs are interpreted without pretending to recover their underlying observations. Comparisons of international crashes require consistent windows and currencies.
- The experimental section includes the baseline parameters, double-auction mechanics, 304-trader market, overlapping generations, flat fundamentals, cash, borrowing, dividend timing, short selling, no-resale and alternative-activity interventions, forecasts, strategies, lottery payoffs, CRT, earned money, gender/context, and testosterone intervention.
- The two seven-dollar flat-value examples change both dividends and interest. They are not described as a clean manipulation of initial cash.
- Gender comparisons and administered testosterone answer different questions. Country and CRT comparisons do not independently identify causal cultural or training effects.
- Classroom screenshots and a six-period result placeholder become a reproducible debrief exercise; no class outcomes are invented.
- Existing artwork and its numbering are retained. Two editable Markdown tables add the historical comparison and experimental intervention comparison, each discussed locally.

## Source checks

Primary/research-source checks included Goldgar's publisher account; Odlyzko's 2020 author manuscript; Velde's Chicago Fed working-paper summary; Ofek and Richardson's author-hosted paper; Shiller's Yale survey explanation; Federal Reserve History accounts of 1929, 1987, Latin American debt and the Great Recession; and the experiment articles/publisher or author-institution abstracts. Links are in the chapter bibliography. Some publisher full texts were unavailable; no claim is made to have independently reanalyzed their data.

`numerical-checks.json` records recomputed dividend expectations, growth-model values, flat-value finite-horizon identities, and the existing NASDAQ percentages. `float-source-qa.json` records the source figure/table reference check.

## Validation

- Full HTML book rendered, followed by a final Chapter 27 HTML render after the last wording change; the EPUB was rebuilt from the final source.
- `python3 audits/ch27-bubbles-20260916/verify_chapter.py`: PASS. All 63 slide numbers are mapped (15 hidden), chapter floats have local prose references, HTML and EPUB include the final historical and experimental additions, and all 57 chapter references have resolved author-year correspondence. `chapter-validation.json` records the tested source/output hashes.
- `python3 scripts/sync_references.py --check`: PASS; the shared master bibliography is synchronized. Its total can change as other tasks revise other chapters.
- `python3 scripts/qa_epub_release.py`: PASS, zero package/navigation/content errors after the final build.
- `python3 scripts/qa_quarto_book.py`: six book-wide errors, all outside Chapter 27. They concern unresolved table references in six appendix HTML pages (Appendix B: 9; literature review: 5; evidence methods: 14; evidence failures: 7; portable tools: 4; course examples: 3). Chapter 27 itself has no unresolved float or author-year references. These unrelated appendix sources were not edited for this request.
- Browser visual inspection at the normal desktop viewport confirmed readable historical and experimental comparison tables and correctly rendered flat-fundamental-value mathematics. This was a targeted inspection, not a new whole-book visual audit.

Other tasks were changing the shared book during this revision. The validation records the tested files, not a promise that subsequent workspace edits preserve these results. No commit, push, or external publication was performed by this task.
