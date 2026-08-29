# New-Chapter Image Integration Report

**Audit date:** August 29, 2026  
**Scope:** the lecture materials supporting risky choice, prospect theory, intertemporal choice, decisions from experience, mental accounting, strategic interdependence, behavioral finance, asset bubbles, social preferences, and subjective well-being.

## What was reviewed

The review covered every rendered slide in nine editable lecture decks and all 46 pages of the subjective-well-being PDF. The editable decks contained 275 visual occurrences representing 241 unique embedded-image hashes. Contact sheets were inspected for conceptual importance, legibility, source status, duplication, and fit with the current chapters.

An image was added only when it did at least one of the following:

- made a central mechanism easier to understand than prose alone;
- preserved an important lecture example;
- made a study design or inferential boundary visible;
- or re-expressed a quantitative journal result whose values could be checked against the chapter's cited source.

Copyrighted photographs, screenshots, journal artwork, maps, cartoons, video frames, and banknote images were not treated as reusable merely because they appeared in a lecture file. Cosmetic modification was not used as a copyright workaround.

## Figures added

| Figure asset | Chapter and placement | Treatment | Evidence boundary |
| --- | --- | --- | --- |
| `finance-euro-efficiency` | Behavioral Finance, “The €20 note and three meanings of efficiency” | Original composite using the photograph supplied for this book | Shows an actual €20 note left on the ground while separating rapid incorporation, no-free-lunch, and fundamental-value claims. |
| `finance-event-study-drift` | Behavioral Finance, event studies | Original method schematic derived from the cited event-study and earnings-drift literature | Curves explain the design logic and are explicitly not digitized effect-size estimates. |
| `experience-rare-event-sampling` | Decisions from Experience, small samples | Original mathematical visualization of $(1-p)^n$ | Assumes independent sampling; the caption names selection, dependence, censoring, and memory as departures. |
| `mental-accounting-evidence-redraw` | Mental Accounting, disposition effect and myopic loss aversion | Original redraw of reported values from Odean (1998) and Benartzi and Thaler (1999) | Displays the 3.41-percentage-point comparison and 40%/90% allocations without copying either published figure; context and alternative mechanisms remain visible. |
| `bubble-trader-strategies-redraw` | Asset Bubbles, trader heterogeneity | Original redraw of the Haruvy and Noussair (2006) classification | Shares describe one experiment and classification rule, not fixed investor types or population proportions. |
| `level-k-reasoning-ladder` | Behavioral Game Theory, limited strategic depth | Original theoretical diagram based on Nagel (1995) | The numerical ladder is not used to infer a person's reasoning depth from one choice. |
| `social-preference-games-redraw` | Cooperation and Social Preferences, ultimatum and dictator games | Original design comparison plus redraw of historical result ranges | Ranges are bounded by population, stakes, anonymity, entitlement, repetition, culture, and procedure. |
| `income-wellbeing-evidence-synthesis` | Subjective Well-Being, income | Original synthesis of the 2010, 2021, and 2023 analyses | Curves are explicitly illustrative; the figure rejects a universal magic income threshold. |

Every SVG also has a high-resolution PNG companion for formats or readers that require raster output. The current EPUB embeds the standards-compliant SVG assets directly. Each insertion has a substantive caption, alternative text, an in-text interpretation, and a source or derivation boundary.

## Verification

- All eight SVG files parse as valid XML.
- All eight PNG companions were regenerated at 1,800 pixels wide.
- The figure-connector audit passes across all 76 chapter figures.
- The eight figures were rendered inside their actual HTML chapters at an 820-pixel content width and visually inspected as a contact sheet; text remains legible, boxes and charts are evenly spaced, and connectors terminate correctly.
- Full HTML and EPUB builds completed successfully after insertion.
- EPUB package QA confirmed that all eight figure references resolve to embedded media assets and that the compact Part/chapter navigation remains valid.
