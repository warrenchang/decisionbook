# Mathematics and the main reading path

## Scope and editorial decisions

The user requested less mathematics in the main text throughout the book, with formal material placed in mathematical-analysis boxes. All 62 configured sources were reviewed, including all 42 chapters; retired and legacy chapters were excluded. Fourteen chapters needed revision, together with the reading guide and two appendices. Appendix A remains the dedicated mathematical reference and is unchanged.

The main text now explains mechanisms, probability comparisons, model implications, and decision thresholds in words. Numerical examples, empirical findings, assumptions, and qualifications remain available along that reading path. Equations, parameter definitions, detailed calculations, and the methods appendix's existing simulation code are collected in 29 consistently labeled Mathematical analysis boxes: 25 new boxes and four relabeled existing optional boxes. Other established optional research notes remain optional research notes. Necessary numerical labels and notation inside existing diagrams were retained.

Specific changes include:

- Probability rules and Bayes' rule are collected after their verbal explanations. The hiring and screening examples retain their counts and updated probabilities.
- Sampling, regression, forecast scoring, and combined risks retain their practical interpretations. The regression simulation's original data-generating specification and seed moved from its caption into the analysis.
- Expected utility, prospect theory, and discounting introduce the meaning of the models before presenting their functional forms. Numerical model predictions remain explicitly conditional illustrations.
- Coordination and repeated cooperation keep the incentive logic and qualifications in the main explanation; their threshold derivations are optional.
- Market valuation, bargaining surplus, and rain-forecast decision thresholds preserve the worked examples while moving symbolic expressions out of captions, tables, and the main text.
- The methods appendix keeps causal assumptions and the distinction between assignment and receipt visible, with notation and the unchanged teaching code in optional boxes. The portable probability tool links to the Brier-score analysis instead of repeating its formula.

Redundant symbolic statements that already express the same information as the retained prose were translated into words rather than duplicated in another box. Examples include the Palm–3Com sum, the conceptual experience-to-choice chain, the Allais and Ellsberg comparisons, and simple arithmetic already explained by the numerical examples. No empirical dataset, simulation output, reference entry, or scientific interpretation was intentionally changed.

## Verification

The baseline commit, source inventory, rendered mathematics inventory, and heading anchors are recorded alongside this note. `check_reading_layers.py` compares current sources and editions with that baseline. It checks reference blocks, explicit anchors, retained heading destinations, teaching code, box counts, main-text mathematics, and the new EPUB anchors. The before/after counts concern rendered mathematical text; they do not count notation embedded in figures.

HTML and EPUB are built sequentially. Existing book, bibliography, EPUB-release, and float-reference checks are run against the final outputs. `example-arithmetic-qa.json` records 31 recomputed illustrative calculations. These checks do not re-estimate empirical effects or regenerate teaching data.

`check-layout.cjs` inspects all 13 documents containing the labeled boxes in HTML and extracted EPUB XHTML at widths of 1440 and 390 pixels. It tests each HTML expansion control, actual formula typesetting, visible box content, and page overflow. MathJax's required CDN assets are allowed and recorded; unrelated external embeds are blocked. Screenshots sample probability, utility, prospect theory, negotiation, decision thresholds, and causal analysis. EPUB pagination in a native reading application is not tested.

The first EPUB check identified a reading-guide link without a section anchor, which was repaired. Visual inspection also prompted removal of a redundant EPUB frame and separation of stable anchors from Quarto's callout wrappers to avoid duplicate identifiers. Final reports supersede the earlier build logs. Stored logs have trailing whitespace normalized.

## Final result

PASS: all 42 chapters contain no rendered inline or display mathematics outside callouts, compared with 148 inline and 40 display expressions in the baseline. There are 29 labeled mathematical-analysis boxes. The final HTML and EPUB builds, book QA (zero errors and warnings), EPUB-release QA (zero errors), bibliography check (967 references), float-reference QA (62 sources, zero issues), preservation checks, and 31 illustrative arithmetic checks passed. All 52 final browser cases passed, and the revised single-frame EPUB boxes and typeset formulas were visually inspected. Appendix A, the preface, master reference entries, and teaching code are preserved.

The subsequent user follow-up authorized committing and pushing this verified revision.
