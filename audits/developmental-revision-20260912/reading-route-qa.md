# Rendered reading-route QA

Run: 2026-09-12T19:13:41.902Z. Phase: final-refreshed-html. Automated status: **PASS**. Independent visual review: **PASS**.

Scope: eleven revised SVGs at desktop 1440 × 1000 and mobile 390 × 844; six core comparison sections on fresh page loads; all thirty Appendix C tool levels at both widths. Optional notes were opened only when needed to inspect their figures.

| Figure | Viewport | Image width | Minimum non-title font | Phone-fit |
| --- | --- | ---: | ---: | --- |
| decision-loop | desktop | 820.0px | 14.84px | true |
| decision-making-according-to-behavioral-evidence | desktop | 820.0px | 14.00px | true |
| urge-wave-observation | desktop | 798.7px | 18.60px | true |
| habit-formation-curve | desktop | 820.0px | 18.67px | true |
| digital-arrow-affordance | desktop | 820.0px | 15.36px | true |
| heuristic-substitution | desktop | 820.0px | 18.47px | true |
| context-mechanisms | desktop | 820.0px | 16.69px | true |
| fluency-pathway | desktop | 820.0px | 16.69px | true |
| communication-grounding | desktop | 820.0px | 17.36px | true |
| conversation-needs-map | desktop | 820.0px | 14.47px | true |
| silence-mechanism-diagnostic | desktop | 820.0px | 30.18px | true |
| decision-loop | mobile | 330.5px | 12.15px | true |
| decision-making-according-to-behavioral-evidence | mobile | 330.5px | 12.15px | true |
| urge-wave-observation | mobile | 309.2px | 12.19px | true |
| habit-formation-curve | mobile | 330.5px | 12.16px | true |
| digital-arrow-affordance | mobile | 330.5px | 12.15px | true |
| heuristic-substitution | mobile | 330.5px | 12.16px | true |
| context-mechanisms | mobile | 330.5px | 12.16px | true |
| fluency-pathway | mobile | 330.5px | 12.16px | true |
| communication-grounding | mobile | 330.5px | 12.16px | true |
| conversation-needs-map | mobile | 330.5px | 12.15px | true |
| silence-mechanism-diagnostic | mobile | 330.5px | 12.15px | true |

## Automated issues

None.

## Warnings

None.

Screenshots: /private/tmp/decision-book-reading-route. Detailed measurements, default visibility, and per-tool labels are in reading-route-qa.json.

## Limits

This focused check does not certify all historical book figures, every page, or EPUB display. Figure font sizes are estimated from browser-computed SVG text and the measured contain scale, including desktop height constraints. Screenshot inspection is recorded below.


## Final visual review

All 22 final refreshed-HTML figure screenshots were inspected individually, including their captions. There is no cropped figure text, overflowing label, unintended arrow/text collision, or clipped caption in this scope. All eleven mobile figures fit the reading column without horizontal figure scrolling. The minimum non-title text sizes range from 12.15 to 12.19 CSS px on mobile and from 14.00 to 30.18 CSS px on desktop. The estimate accounts for the desktop 620px height limit and `object-fit: contain`, rather than assuming the image element's full width is painted.

The final screenshots preserve the semantic corrections recorded in `independent-figure-review.md`: judgment as a whole connects to choice; observation prompts are separate from the illustrative urge curve; and modeled Lally estimates are clearly separated from the schematic habit curve. The five silence pathways remain distinct and legible.

All six core comparison sections are visible on fresh page loads at both widths (12 checks). Chapter 1's commercial examples are now ordinary visible content; the other five comparison bodies are expanded. This verification precedes any opening of optional notes for figure inspection.

All thirty Appendix C tools show the assigned textual level at both widths (60 checks): 12 Core tools, 3 Quick checks, and 15 Specialized extensions. Their borders are now respectively blue `rgb(37, 103, 143)`, teal `rgb(43, 122, 120)`, and purple `rgb(111, 93, 155)`. One representative of each level was visually inspected at both widths (six additional screenshots). The decision-journal table retains local horizontal scrolling on mobile: a follow-up DOM check measured table client width 309px, scroll width 365px, and `overflow-x:auto`, with no overflow of the containing tool box or page. This table behavior is separate from the eleven phone-fitting figures.

Initial rendered inspection caught undersized text in the habit and conversation figures caused by their inline widths, the urge figure inside a padded callout, and the heuristic footer. It also caught overridden tool-level border colors. The parent corrected source widths, the affected SVG font sizes/wrapping, and CSS specificity; this final refreshed-HTML run verifies those corrections.

Screenshot crops hide fixed navigation overlays only, so a sticky navigation bar does not cover the top of an element capture. The actual figure and reading-column layout are unchanged. Optional notes were opened only to inspect their figures. This is a local Chrome HTML check; EPUB, other browsers, and the remaining historical figures belong to separate QA.

## Reproduce

From the repository root, run:

```sh
NODE_PATH=/Users/ra25fi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules READING_ROUTE_PHASE=final-refreshed-html /Users/ra25fi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node audits/developmental-revision-20260912/qa-reading-route.cjs
```

The script generates measurements and screenshot captures. Each rerun deliberately resets the manual visual-review status to pending; a script run alone cannot certify that a reviewer inspected its new images.
