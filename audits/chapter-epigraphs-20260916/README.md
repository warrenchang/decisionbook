# Chapter-opening quotation revision — 16 September 2026

Reviewed all 42 chapter epigraphs. Replaced 35 technical or less accessible quotations with short quotations from recognizable writers, public figures, and scientists speaking to general audiences. Retained seven existing quotations. No selected epigraph is an excerpt from an academic paper.

The changes touch 38 chapter-opening blocks: 35 replacement quotations, two updated source links (Chapters 3 and 36), and one revised attribution identifying Feynman's 1974 commencement address (Chapter 32). All source text outside those blocks is identical to the saved baseline, including chapter titles, examples, references, and cross-reference identifiers. Removed the obsolete Chapter 7 exception from the epigraph QA rule because its former research-abstract quotation is gone.

- [Quotation guide](quotation-guide.md): all 42 quotations and linked sources.
- [Selection record](epigraph-selections.json): exact before/after blocks, source metadata, and topic-fit rationale.
- [Source notes](source-verification-notes.md): verification method and bibliographic details.

## Verification

| Check | Result |
| --- | --- |
| HTML build, followed by EPUB build | PASS; builds ran sequentially |
| General Quarto book QA | PASS; 0 errors, 0 warnings |
| EPUB package, navigation, content, and internal links | PASS |
| Exact epigraph text in all 42 HTML chapters and all 42 EPUB chapters | PASS |
| Text outside epigraphs in all 62 configured source documents | Unchanged |
| Existing HTML identifiers | Preserved; no duplicate identifiers |
| Search index | Unchanged; epigraphs were not indexed in the baseline |
| Quotation length | At most 21 words each |
| Layout checks | PASS for 12 format/chapter/viewport combinations |

Layout checks cover HTML Chapters 1, 22, 27, and 29 and EPUB Chapters 27 and 29 at 1440- and 390-pixel widths. They check quotation text, placement below the title, and horizontal containment. Visual inspection of the saved desktop Chapter 1, mobile Chapters 22 and 29, and mobile EPUB Chapter 27 screenshots confirmed readable quotation and attribution wrapping. EPUB screenshots show extracted XHTML in Chrome; they do not test native-reader pagination.

The first draft of the task-specific checker incorrectly expected epigraphs in the search index. A comparison with the baseline commit established that none of the old epigraphs was indexed and that the regenerated index was byte-identical. The check now verifies preservation of the existing search content.

## Reproduction

From the repository root, run these commands in order:

```sh
quarto render --profile html
quarto render --profile epub
python3 scripts/qa_quarto_book.py
python3 scripts/qa_epub_release.py
python3 audits/chapter-epigraphs-20260916/check_epigraphs.py
```

The EPUB post-render hook copies the finished package to `docs/Decision-in-the-Making.epub`. `render-html.log`, `render-epub.log`, `qa-quarto.log`, `epigraph-qa.json`, and `layout-qa.json` record this run. Root `QA_REPORT.md` and `EPUB_QA_REPORT.md` contain the general release checks.

For the saved layout procedure, extract the released EPUB to `/private/tmp/book-epigraphs-epub-20260916/`, preserving its directory structure, then run `check-layout.cjs` with Node and Playwright available. The script uses the installed Google Chrome binary and blocks external requests. `epub-layout-targets.json` identifies the extracted chapters. Baseline source content, identifiers, search digest, and commit are saved alongside the checks.

This revision was not committed or pushed.
