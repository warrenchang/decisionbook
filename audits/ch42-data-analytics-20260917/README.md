# Chapter 42: data availability, computation, and analytical purposes

Date: 2026-09-17

The user requested integration of the messages of three supplied figures into the final chapter, with a coherent discussion of growing data availability, cheaper computation, and different uses of analysis. The screenshots were treated as reference content. Their embedded labels were not instructions.

## Coverage and scientific decisions

| Supplied figure | Integration | Qualification |
| --- | --- | --- |
| Descriptive, diagnostic, predictive, and prescriptive analytics | New “Four questions data analysis can answer” section and Table 42.1; all four purposes use Flint as a common setting. The tool table, evaluation section, practice canvas, and conclusion now follow these distinctions. | Diagnostic breakdowns can suggest explanations without identifying causes. Prediction includes unobserved present facts. Prescription needs objectives and constraints, plus causal evidence where actions change outcomes. Value and difficulty are not universally ordered across the four purposes. |
| Data volume growing from 4.4 to 44 to 180 zettabytes | New “More data and cheaper computation” section explains digital records, reuse, affordability, and the verified IDC comparison: 4.4 zettabytes estimated for 2013 and 44 forecast for 2020. | The 2020 value is explicitly a forecast made in 2014. The measure includes created and copied data, including transient data. The screenshot's 180-zettabyte endpoint was not reproduced because its forecast provenance was not established. No screenshot point is presented as a current observed total. |
| Falling image-classification error and a human reference line | New historical ImageNet subsection explains the fall from 28.2% top-five error in 2010 to the winning ensemble's 3.57% in 2015. | The human reference is annotator- and task-specific. A footnote gives sample sizes and notes changing early challenge categories. Benchmark progress demonstrates capability, not the cost of computation or universal human-level vision. |

The computation discussion uses the chapter's existing Stanford AI Index comparison, moved earlier and explained: US$20 to US$0.07 per million tokens between November 2022 and October 2024 for approximately GPT-3.5-level MMLU performance. It distinguishes inference from training and the price of computation from the full cost of collecting, checking, and acting on evidence.

## Verified primary sources

- IDC (2014), executive summary: https://idcclients.cycloneinteractive.net/emc-digital-universe-iview-2014/executive-summary.htm
- INFORMS analytics framework: https://www.informs.org/Professional-Development/INFORMS-Analytics-Framework/Explore
- Stanford AI Index 2025: https://hai.stanford.edu/ai-index/2025-ai-index-report and https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf
- Russakovsky et al. (2015), ImageNet benchmark methods and historical/human comparisons: https://arxiv.org/pdf/1409.0575
- He et al. (2016), residual networks and 2015 result: https://arxiv.org/pdf/1512.03385 and https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html
- Bertsimas and Kallus (2020), prediction and prescription: https://pubsonline.informs.org/doi/10.1287/mnsc.2018.3253 (online publication 2019; journal issue March 2020).

Five references were added to the chapter and synchronized to the book bibliography. All 21 original chapter references and existing explicit anchors were retained. The two existing SVGs were not edited. The whole-book recap was moved near the end, before the practice lab, to give the main discussion a continuous progression from opportunity to analytical question, tool, action, and evaluation.

## Verification

- `quarto render --profile html`: completed successfully.
- `quarto render --profile epub`: completed successfully.
- `python3 scripts/qa_quarto_book.py`: PASS, zero errors and zero warnings.
- `python3 scripts/qa_epub_release.py`: PASS, zero errors.
- `python3 scripts/sync_references.py --check`: PASS, 974 unique references.
- Source float checks: PASS; see `float-source-qa.json`.
- Existing references, explicit anchors, arithmetic, and unchanged figure hashes: see `source-checks.json`.
- Visual inspection: Table 42.1 in HTML at 1280px and 390px, and in extracted EPUB content at the same widths; HTML tool table and practice canvas at desktop width; a retained EPUB figure at desktop width. No text overlap or page-level horizontal overflow was observed in the narrow table checks. Both existing images loaded in both formats. The existing wider HTML tables retain horizontal scrolling on narrow screens.
- EPUB visual inspection used a byte-identical `.html` copy of the extracted chapter XHTML, with its packaged CSS and assets, because the browser did not open the `.xhtml` URL. This was a browser rendering check, not an Apple Books device test. The actual EPUB was checked separately by the release QA script.

`chapter-before.qmd` preserves the pre-edit source. `attachments.json` records the three input paths and hashes. Changes are local; no commit, push, or external publication was performed.
