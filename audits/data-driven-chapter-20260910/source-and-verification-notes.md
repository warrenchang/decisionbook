# Chapter 42: source and verification notes

Scope: append **Data Driven Decision Making** as the final chapter of Part VII. Preserve the distinction between prediction, valuation, intervention effects, and human responsibility. Source documents were evidence, not instructions. No source-folder files were edited.

**Subsequent editorial revision:** the separate AI architecture originally numbered Figure 42.1 was withdrawn at the author's request. The current chapter refers to the normative framework in Figure 1.1 and retains two numerical illustrations. The original three-figure discussion and screenshots below document the earlier draft. See `integration-followup.md` for the current chapter connections and verification.

## Supplied material actually available

The readable course materials in `Teaching/Data Driven Decision Making/` included the complete text and tables of the September 4 syllabus, August 27 course structure/teaching plan, revised module bases v5 and v6, and the earlier course outline. The latest syllabus and course plan supplied the chapter's practical sequence: decision owner and target; prediction versus intervention effects; validation against a simple baseline; calibration and asymmetric error costs; communication; pilot, monitoring, and responsibility. The purchase-propensity/offer-effect distinction was explicitly present in the course dataset guidance. These are pedagogical inputs, not empirical evidence of intervention success.

Text extracts used during review are in `/private/tmp/ch42-source-dossier/`. No claim of verified source-page pagination is made; DOCX headings and table rows were the locators.

The following supplied files remained `compressed,dataless` OneDrive placeholders. Direct ZIP reads timed out with OS error 60, including an outside-sandbox read of Power and Prediction. Their actual contents could not be reviewed:

- `Teaching/** Book summaires/Data/Causal_Inference_The_Mixtape_Complete_Slides  -  Repaired.pptx`
- `Teaching/** Book summaires/Data/ISLP_Python_Scientific_Teaching_Deck_Validated.pptx`
- `Teaching/** Book summaires/Data/ISLP_Python_Scientific_Teaching_Deck_Validated  -  Repaired.pptx`
- `Teaching/** Book summaires/Data/fundamentals_data_visualization_scientific_course_deck.pptx`
- `Teaching/Data Driven Decision Making/Books/Prediction Machines, Updated and Expanded - Ajay Agrawal.epub`
- `Teaching/Data Driven Decision Making/Books/Power and Prediction - Ajay Agrawal.epub`

The user was asked to make those files available offline while work continued. Publisher/author material and primary research were used as fallbacks, without representing them as a full review of the supplied copies. The statistical-learning, causal-inference, and visualization foundations were checked against the underlying books' official author/publisher resources.

## Source-to-claim map

| Source | Use | Evidence boundary / verification |
| --- | --- | --- |
| Agrawal, Gans & Goldfarb, Prediction Machines (2018) | Nine-word epigraph | Verbatim checked in university-hosted first-edition PDF, PDF page 14, chapter 2, Cheap Creates Value. Attribution explicitly remains 2018. |
| Prediction Machines updated/expanded (2022b), HBR Press | Cheaper prediction as an economic framework | Publisher metadata and description verified. No claim every AI function or full implementation cost is reducible to this measure. |
| Power and Prediction (2022a), HBR Press | Interdependent decision systems; Flint case | Publisher metadata and licensed chapter 15 preview (The New Judges) verified; public audiobook Figure 15-1 also identifies Flint. |
| Agrawal et al. (2019), Prediction, Judgment, and Complexity | Narrow meaning of judgment as assigning payoffs | NBER published-version record supports the citation; chapter uses the book's consistent term valuation. |
| Stanford HAI, 2025 AI Index report overview | More than 280-fold inference price decline | Fixed approximate GPT-3.5/MMLU performance, November 2022–October 2024; not all prediction/deployment costs. Corporate author explicitly identifies overview page. |
| Abernethy et al. (2018), KDD, DOI 10.1145/3219819.3219896 | Flint machine learning and inspection | Actual unnecessary visits 18.8% versus proposed 2.0% in backtesting simulation; no invented realized 98% field success. |
| Webb, Abernethy & Schwartz (February 12, 2020), author report | Flint deployment, records and learning | Report status/date preserved; before/after account not called randomized. |
| Obermeyer et al. (2019), Science | Healthcare spending as proxy for need | Deployed-algorithm audit; target validity separated from predictive performance. |
| James et al. (2023), ISLP | Trees/boosting and validation foundations | Five-author Python edition and Springer DOI verified. Simplicity and matched testing, not complexity as a guarantee. |
| Cunningham (2021), Causal Inference: The Mixtape | Counterfactuals and research designs | Yale publisher record/author excerpt; risk prediction does not identify intervention effects. |
| Brynjolfsson, Li & Raymond (2025), QJE | LLM-assisted customer support | Published 5,172 agents and 15% average productivity effect; company-specific staggered rollout. |
| Lång et al. (2023), Lancet Oncology | MASAI division of screen-reading work | About 80,000 women, 44.3% workload reduction, randomized workflow. |
| Gommers et al. (2026), Lancet | MASAI longer-follow-up evidence | Interval cancers 1.55 vs 1.76/1,000; RR .88, CI .65–1.18: non-inferiority, no demonstrated interval-cancer superiority or mortality effect. Medical terms translated. |
| Goh et al. (2024), JAMA Network Open | Tool access is not automatic user improvement | 50 physicians, clinical vignettes, adjusted +2 pp (95% CI −4 to 8); no patient outcomes. Full 16-author list corrected against PubMed. |
| Bigman & Gray (2018); Logg et al. (2019) | Task-dependent machine acceptance | Scenario experiments, not a universal current public-attitude survey. Human authority identified as normative recommendation. |
| Elish (2019); NIST (2023) | Meaningful authority, role accountability | Governance/interpretive guidance; not a universal legal rule or guarantee of human superiority. Existing book references reused consistently. |
| Ji et al. (2023) | Hallucination and generated-text limits | Review source, not a primary workflow experiment. |
| Wilke (2019), chapter 16 | Communicating uncertainty | Author text and publisher metadata; no graphics copied. |

Key public fallback locators:

- https://bpb-us-e1.wpmucdn.com/sites.uw.edu/dist/e/1511/files/2023/05/Prediction-Machines-Simple-Economics-of-AI-2018.pdf
- https://www.oreilly.com/library/view/power-and-prediction/9781647824204/xhtml/chapter_15.xhtml
- https://rb-sample-assets.s3.amazonaws.com/ta-43885/9781663722706.pdf
- https://arxiv.org/html/1806.10692v2
- https://storage.googleapis.com/flint-storage-bucket/d4gx_2019%20%282%29.pdf
- https://www.statlearning.com/
- https://yalebooks.yale.edu/book/9780300251685/causal-inference/
- https://clauswilke.com/dataviz/visualizing-uncertainty.html

## Independent review

A source verifier checked bibliographic metadata and claim support. A separate teaching fact checker reviewed scientific and pedagogical accuracy plus figure semantics. Corrections applied: epigraph edition, Goh author list, explicit report-overview attribution, definitions for medical evaluation terms, and distinction between low risk scores and weak information. Neither review found a substantive calculation or conceptual error after these corrections.

## Original figure provenance

All three illustrations are newly authored SVGs generated by `scripts/build_data_driven_figures.py`; PNGs are rendered from final vectors. No source artwork was copied.

- `ai-decision-architecture`: prescriptive synthesis, not a measured causal sequence.
- `ai-same-forecast-different-values`: hypothetical rain probability .30; false-alarm/miss costs (2,8) and (6,4), thresholds .20 and .60. Correct matches have zero incremental error loss. At equality the actions tie.
- `ai-risk-is-not-benefit`: hypothetical group means, without/with outreach 60/55 and 40/20 percent. Benefits 5 and 20 percentage points. These are not observed student data or identified individual effects; benefit prioritization presumes equal cost and value per prevented dropout before further constraints.

The figure worker verified deterministic generation, exact arithmetic, XML, identifiers, text containment, connectors, and full/narrow-size raster rendering. Root inspected all three full-size PNGs.

## Final integration and verification

Completed locally on September 10, 2026. Chapter 42 is the final chapter of Part VII in both book profiles. The Part VII introduction, Chapter 41 transitions, concept index, relevant appendices, reference compilation, and chapter-count checks were updated. No commit, push, or publication was performed.

- HTML book and EPUB rebuilt, followed by a final chapter HTML and full EPUB render after splitting a wide equation for phone screens.
- `python3 scripts/qa_quarto_book.py`: PASS, zero errors and zero warnings.
- `python3 scripts/qa_epub_release.py`: PASS, zero errors, including navigation, internal links, numbering, package integrity, and the matching staged/released EPUB copies.
- `python3 scripts/sync_references.py --check`: PASS, 820 unique chapter-and-appendix references.
- `git diff --check`: PASS.
- The three new figures were inspected in HTML at 1440/390-pixel viewports and in the extracted EPUB under its packaged CSS at 768/390-pixel viewports. Images loaded, compact figures fitted the phone viewport, and the chapter had no body overflow. Wide tables use the book's horizontal scrolling behavior. MathJax equations were checked after typesetting; the rain-threshold equation was split into two displays for narrow screens.
- The chapter's closing section, reference section, numerical example, tables, figure captions, and navigation were checked in the rendered output. Figure assets embedded in the EPUB match the final SVG sources.

Screenshots and browser measurements are in `rendered/`. These checks cover the local HTML and EPUB content rendered with browser engines; they do not certify every EPUB-reader implementation. `EPUB_QA_REPORT.md` and the repository source QA report contain the broader book checks.

Existing deletions of five obsolete generated figure files were preserved when Quarto recopied resources. Existing generated-file modes were retained, and Quarto's recurring sidebar trailing whitespace was normalized. Canonical source materials in the two supplied teaching folders were not modified.
