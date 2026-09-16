# Chapter 25: robot cues and the reward of cooperation

The user requested removal of “Can an image of eyes create reputation?” and asked about robot eyes and dopamine during mutual cooperation. The honesty-box section and its chapter-only Bateson reference were removed. The existing appendix evidence case remains. Old section anchors are retained for incoming links; the concept index points to the replacement robot paragraph.

Kismet is discussed briefly within reputation. Mutual cooperation and reward processing precedes punishment, linking the positive and retaliatory sides of social valuation. The preceding ingroup-identity revision is preserved.

## Primary-source verification, 16 September 2026

- [Burnham and Hare (2007), full text](https://evolutionaryanthropology.duke.edu/sites/evolutionaryanthropology.duke.edu/files/site-images/Burnham%20and%20Hare_%202007_%20Engineering%20human%20cooperation-does%20involuntary%20neural%20activation%20increase%20public%20goods%20contributions.pdf): methods pp. 95–98 and Table 1. Screen images, not a physically present robot; no eyes-only control. The outcome is contribution amount.
- [Northover et al. (2017), full text](https://www.aggression-irlab.com/wp-content/uploads/2019/08/ArtificialSurveillanceCuesAndGenerosity2017.pdf): both meta-analyses include Burnham and Hare (Tables 3–4). The broader evidence qualifies the positive study.
- [Rilling et al. (2002), full text](https://is.muni.cz/el/1451/jaro2008/bp209/um/Neural_Basis_for_Social_Cooperation.pdf): methods and Table 4/Figure 5. The contrast is mutual cooperation versus the average of the other three outcomes. BOLD was measured; dopamine release was not.

Two references were added to Chapter 25 and the master bibliography. Bateson remains in the master bibliography because the appendix still cites it. The dopamine, artificial-surveillance, and watching-eyes index entries were updated.

## Checks

Builds are sequential: `quarto render --profile html`, then `quarto render --profile epub`. Release checks use `scripts/qa_quarto_book.py`, `scripts/qa_epub_release.py`, `scripts/sync_references.py --check`, and `scripts/qa_float_references.py` on source, HTML, and extracted EPUB. The layout script uses the bundled Node/Playwright runtime and installed Chrome, with network requests blocked.

EPUB layout is inspected as extracted XHTML in Chromium; native-reader pagination is not tested. Before-files and build/check outputs are retained in this directory.

Final verification passed: HTML release QA had zero errors and warnings; EPUB release QA had zero errors; figure/table checks passed across 62 sources. The 967-reference master bibliography matches its source union. Both new concept links resolve in HTML and EPUB, the removed title is absent from Chapter 25 search results, and all four format/viewport layout checks passed. Visual inspection confirmed readable paragraphs and transitions. The earlier ingroup section is unchanged. Build-log trailing whitespace was normalized for storage.
