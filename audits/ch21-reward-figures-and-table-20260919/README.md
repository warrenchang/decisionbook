# Chapter 21: reward figures and wanting–liking comparison

## Requested revision

Move the former Figures 21.5 and 21.6 from a collapsed research note into the main text. Replace the former Figure 21.3 with a table based on BE06, including the neural foundations of wanting and liking. Preserve the earlier goal-directed behavior / habitual behavior wording already present in the working tree.

## Source and editorial decisions

- The source excerpts and SHA-256 hash in `lecture-source-excerpts.json` identify the current SDU BE06 PowerPoint. Slide 11 provides the wanting–liking comparison; slides 12 and 45 describe dopamine's motivational and learning roles. The corresponding PDF comparison on page 11 was visually inspected. The PDF export has 33 pages and the current PowerPoint has 60 slides, so the editable presentation was also read.
- The new Table 21.1 compares the question, measurement, dopamine, brain circuitry, opioid/endocannabinoid signaling, and bedtime example. Two columns keep both concepts visible on a phone. It distinguishes animal taste-reactivity measures from human pleasure reports.
- The former Figure 21.3 is replaced by `tbl-wanting-liking`; its old `fig-wanting-liking` fragment remains as an invisible bookmark alias. The unused illustration files remain available to legacy material.
- Former Figure 21.5 (`fig-reward-prediction-error-shift`) is now Figure 21.3, immediately after the main explanation of reward prediction error. Former Figure 21.6 (`fig-reward-uncertainty-comparison`) is now Figure 21.4, in the main discussion of uncertain rewards. Neither figure is inside a collapsible callout.
- The former urge-wave Figure 21.4 becomes Figure 21.5. The BRAIN table becomes Table 21.2. Quarto regenerates linked numbers throughout the book.
- The emptied dopamine research note is removed. Its relevant explanations are integrated beside the figures, and its Schultz video is retained in the existing delay-and-effort research lens.

## Evidence supporting the neural comparison

- Berridge & Robinson (1998), doi:10.1016/S0165-0173(98)00019-8: severe dopamine depletion disrupted spontaneous feeding while taste-reactivity patterns remained. The paper combines a review with original depletion experiments. Retain the narrower finding; do not infer that dopamine has no learning role.
- Peciña & Berridge (2005), doi:10.1523/JNEUROSCI.2329-05.2005: mu-opioid stimulation increased intake widely across rat accumbens medial shell, but enhanced positive sucrose reactions in a localized hotspot. The same chemical signal can have different effects across sites.
- Smith & Berridge (2007), doi:10.1523/JNEUROSCI.4205-06.2007: opioid enhancement of sweet liking involved interacting accumbens and posterior ventral-pallidum hotspots; effects on eating had different circuit requirements.
- Mahler, Smith, & Berridge (2007), doi:10.1038/sj.npp.1301376: anandamide in a rat accumbens-shell hotspot enhanced positive sucrose reactions and eating. This supports an endocannabinoid role without assigning all pleasure to a single transmitter.
- The three new references were verified against author-hosted primary papers and added to Chapter 21 and the synchronized master references.

## Verification

The final source, HTML, EPUB, cross-reference, and visual results are recorded alongside this note. Screenshots distinguish HTML desktop/phone and EPUB reading widths. EPUB screenshots inspect the extracted release XHTML in Chromium, not every possible e-reader implementation.

The first HTML inspection showed centered table prose. Both columns were changed to left alignment for easier reading, and both publication formats were rebuilt before final verification.

Final results: source QA passed with zero errors/warnings; all 1,026 references synchronized; EPUB release QA passed; the 62-source float audit found 116 figures and 166 tables with no issues. All three revised items were visually inspected in HTML at 1280/390 pixels and EPUB at 768/390 pixels. The table requires no horizontal scrolling, and both figures remain outside callouts. The previous terminology edits are preserved. No commit or push was performed.
