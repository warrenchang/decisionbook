# Sources and construction boundaries

## Cold-water protocol

- Primary publisher abstract: [Kahneman et al. (1993)](https://journals.sagepub.com/doi/10.1111/j.1467-9280.1993.tb00589.x).
- [University-hosted copy of the published paper](https://www.ius.uzh.ch/dam/jcr%3A5ae9adc9-61ec-4174-b37c-4b752f36c23b/Kahnemann%20et%20al.%20-%20When%20More%20Pain%20is%20Preferred%20to%20Less%20%281993%29.pdf), pp.402–403, checked 2026-09-25.
- Protocol: 60 seconds at nominal14°C; longer version adds30 seconds while warming toward15°C. Durations control strip lengths; neither bar height nor color measures pain.
- Result:22 of32 analyzed male students chose the long trial. Three participants were replaced: one technical exclusion, two inconsistent-choice exclusions. Order and hand were counterbalanced. Actual repeat exposure was not administered.
- Graphic depicts a protocol and reported choice, not a measured pain trajectory. No patient outcomes or population prevalence inferred.

## Stag-hunt belief threshold

- Source: existing illustrative utility-payoff matrix `tbl-stag-hunt` in Chapter24 and its accompanying mathematical analysis; Skyrms(2004) supplies the general game-theoretic context.
- With probability `p` that the other player chooses Stag, `E(Stag)=15p+2(1-p)=2+13p`; `E(Hare)=10`.
- Exact intersection:`p=8/13`; label rounds to61.5%. At50%, payoffs are8.5 and10. The generator asserts these relationships.
- Lines show calculated expected utility payoffs, not estimated beliefs, frequencies, or measured behavior. Their shape depends entirely on the displayed illustrative matrix.

## Reproduction and verification

1. `python3 scripts/build_coordination_experience_figures.py`
2. `node scripts/render_svg_png_fallbacks.cjs figures/cold-water-better-ending.svg figures/stag-hunt-belief-payoffs.svg` with Playwright available.
3. `node audits/visual-readability-20260925/check-coordination-experience.cjs`

PNG fallbacks were generated from the final SVGs. Both figures were visually inspected at native size and350px width; label bounds were checked at760px and350px. Minimum rendered font at350px is12.89px. Both have direct labels and survive monochrome interpretation. Full HTML/EPUB destination checks belong to the parent task's final build.
