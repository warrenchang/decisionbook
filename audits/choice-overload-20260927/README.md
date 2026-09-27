# Choice overload, contrast, and indecision

Requested scope: connect choice overload (overchoice), the contrast principle, and decoy effects coherently in the book. Chapter 40 already contained the jam study and the 2010 and 2015 meta-analyses. Those findings remain; Chapter 11 supplies the comparison mechanisms.

## Verified additions

| Source | Design and evidence inspected | Use and boundary |
| --- | --- | --- |
| Simonson, I., & Tversky, A. (1992). Choice in context: Tradeoff contrast and extremeness aversion. *Journal of Marketing Research, 29*(3), 281–295. [DOI](https://doi.org/10.1177/002224379202900301) | Primary paper, especially pp. 281–284: consumer comparisons with fixed target alternatives and varied surrounding or preceding trade-offs. | Chapter 11 distinguishes contrast, compromise, and asymmetric dominance. The wine prices are a hypothetical illustration. |
| Dhar, R., & Simonson, I. (2003). The effect of forced choice on choice. *Journal of Marketing Research, 40*(2), 146–160. [DOI](https://doi.org/10.1509/jmkr.40.2.146.19229) | Study 2, pp. 151–152, Table 3: 322 science-museum visitors across conditions; microwave no-choice shares 32% and 18%, target shares 22% and 48%, without and with the decoy. | Chapter 40 uses stated choices from small menus as evidence about deferral. It separates this outcome from welfare and from effectiveness in large assortments. |

The existing overload synthesis was checked against Chernev, Böckenholt, and Goodman (2015), [author PDF](https://chernev.com/wp-content/uploads/2017/02/ChoiceOverload_JCP_2015.pdf). Its [corrigendum](https://doi.org/10.1016/j.jcps.2015.07.001) corrects regression-statistic notation on p. 348; the book does not reproduce those statistics.

Primary full texts inspected: [Simonson and Tversky](https://cognition.aau.at/bg/BA/Simon%20%26%20tversky%2C%201992.pdf) and [Dhar and Simonson, author-hosted file](https://spinup-000d1a-wp-offload-media.s3.amazonaws.com/faculty/wp-content/uploads/sites/48/2019/06/TheEffectofForcedChoiceonChoice.pdf).

The phone plans are explicitly hypothetical. With common coverage and contract terms, B offers more data than C at the same price; A trades a lower price for less data. The 80 GB and 6 GB cases make the dependence on user needs explicit. Practical recommendations are design proposals to test, not additional reported experimental results.

The concept index adds contrast and overchoice routes. The example index links the new application. Existing references, anchors, figures, practice questions, and earlier edits are preserved.

## Verification

- Full HTML and EPUB renders completed. A subsequent targeted HTML render repaired five unresolved Chapter 30 float references produced by the full build; its source was unchanged.
- `qa_quarto_book.py`: 0 errors, 0 warnings.
- `sync_references.py --check`: 1,250 unique references; all 1,248 previous entries retained, two added.
- `qa_epub_release.py`: 0 errors; published and staged EPUBs synchronized.
- `qa_float_references.py --rendered --epub-dir ...`: 69 sources, 107 figures, 168 tables, 0 issues.
- `qa_practice.py --rendered`: all 280 questions across 49 sets retained in HTML and EPUB; `build_practice.py --check` found no stale outputs.
- New HTML/EPUB anchors, index routes, search text, numerical findings, and hypothetical examples checked. Existing source anchors retained.
- Browser inspection confirmed readable prose in the default viewport and navigation between the Chapter 11 and Chapter 40 passages. No new figures were needed.
