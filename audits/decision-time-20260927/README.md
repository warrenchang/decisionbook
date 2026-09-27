# Decision-time allocation: source and editorial record

## Verified source

Oud, B., Krajbich, I., Miller, K., Cheong, J. H., Botvinick, M., & Fehr, E. (2016). Irrational time allocation in decision-making. *Proceedings of the Royal Society B: Biological Sciences, 283*(1822), 20151439. https://doi.org/10.1098/rspb.2015.1439

Full text inspected on 27 September 2026 in the [University of Zurich author-hosted publication](https://www.econ.uzh.ch/dam/jcr:87b30249-c261-4f0d-b21d-affa7c90f45f/Irrational%20time%20allocation%20in%20decision-making.pdf). Bibliographic details also matched [PubMed PMID 26763695](https://pubmed.ncbi.nlm.nih.gov/26763695/). The study directly matches the requested comparison between small outcome differences and inefficient time allocation.

| Claim checked | Primary-source location | Editorial treatment |
| --- | --- | --- |
| Food task, sample, block size, time budget, and random completion | Methods, pp. 2–3 | Describe incentives so the opportunity cost is explicit. |
| Longer comparisons for closer valuations | Results and Figure 2, pp. 4–5 | Treat this pattern as descriptive; the deadline intervention provides the test of inefficiency. |
| Individually calibrated deadlines improve performance | Methods and Results, pp. 3–5 | Distinguish valuation-based food surplus from monetary earnings in the perceptual task. |
| Perceptual sample | Methods, p. 3 | Report 40 analyzed participants, after two exclusions from 42 recruited. |
| Interpretation | Introduction, p. 2; Discussion, pp. 5–7 | Explain allocation across a fixed time budget; do not infer that every valuable decision needed a longer response. |

The lunch and cancellation-clause examples are constructed applications. Their purpose is to distinguish known near-equivalence from uncertainty about consequential differences. No new data analysis or numerical effect estimates were produced.

## Placement

The developed account follows confidence-guided information gathering in Chapter 8's metacognition section, at `how-much-time-is-a-decision-worth`. Chapter 41 adds a practical cross-reference within proportionate decision process. The concept index and example index route readers to the developed account; the chapter reference is synchronized into the master bibliography.

## Verification

- Full HTML and EPUB renders completed successfully. The new Chapter 8 passage was inspected in the browser at its direct anchor.
- `python3 scripts/qa_quarto_book.py`: 0 errors, 0 warnings.
- `python3 scripts/sync_references.py --check`: 1,251 unique references; all 1,250 previous entries retained.
- `python3 scripts/qa_epub_release.py`: 0 errors.
- `python3 scripts/qa_float_references.py --rendered --epub-dir /private/tmp/decision-time-epub-tle3nwma/EPUB --output /private/tmp/decision-time-float-final.json`: 69 sources, 107 figures, 168 tables, 0 issues.
- `python3 scripts/qa_practice.py --rendered`: 280 questions in 49 sets; all 49 HTML sets and 280 EPUB questions with 49 answer sections retained.
- Existing anchors in the four edited content/index sources were preserved. `render-checks.json` records the new HTML/EPUB anchor, incoming links, search entry, study text, and identical staged/release EPUB bytes.
- `git diff --check` passed; no file-mode changes remain. No commit or push was performed.
