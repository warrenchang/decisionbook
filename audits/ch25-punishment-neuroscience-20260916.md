# Chapter 25: anticipated reward from punishment

## Editorial scope

Added “Why punishment can feel rewarding” to the main social-preferences discussion, following the dictator-game comparison. Replaced the optional notes' duplicate study summary with a link to the new section. Added Carlsmith et al. to the chapter references and synchronized the master bibliography. No figures or data changed.

## Primary-source checks

Full bibliographic details appear in the chapter. Primary papers and indexed metadata were checked on 2026-09-16.

| Source | Design and evidence relevant to the addition | Interpretation boundary |
| --- | --- | --- |
| de Quervain et al. (2004), *Science*, 305(5688), 1254–1258; [DOI](https://doi.org/10.1126/science.1100735); [author-hosted paper](https://www.econ.uzh.ch/dam/jcr:ffffffff-9758-127f-0000-000015633e5e/Altruistic_Punishment.pdf); [PubMed](https://pubmed.ncbi.nlm.nih.gov/15333831/) | Within-person trust-game conditions; PET during deliberation. Fifteen men recruited, 14 trusting participants analyzed. Effective/symbolic contrast and caudate–punishment-cost association support anticipated reward. | No direct identification of pleasure or causal neural mediation; narrow sample. See pp. 1254–1257, especially Figure 3. |
| Carlsmith, Wilson, and Gilbert (2008), *Journal of Personality and Social Psychology*, 95(6), 1316–1324; [DOI](https://doi.org/10.1037/a0012165); [author-hosted paper](https://dtg.sites.fas.harvard.edu/CARLSMITH%2C%20WILSON%2C%20%26%20GILBERT%20%282008%29.pdf); [PubMed](https://pubmed.ncbi.nlm.nih.gov/19025285/) | Student laboratory experiments with simulated partners, randomized punishment opportunities, affect forecasts, mood, and rumination measures. Studies 1 and 3 compare opportunity and no-opportunity groups; most eligible participants punished. | Opportunity assignment is distinguished from self-selected punishment. Rumination evidence is suggestive of a mechanism, not independently randomized mediation. Results do not establish universal negative effects. |

## Synthesis and remaining boundary

The two papers address different stages: valuing a prospective sanction and evaluating its emotional aftermath. They are complementary rather than a direct replication or refutation. The chapter connects this distinction to its existing account of valuation and reverse inference in Chapter 6, then returns to the cooperation problem. The practical recommendation to assess repair of cooperation is an application, not an outcome established by these studies.

This is a focused addition about historical evidence, not a systematic review or a claim about the latest consensus. No further search is needed for these bounded claims. General claims about demographic differences, long-term emotional effects, or improved cooperation would require additional evidence.

## Verification

- Full HTML render completed; Chapter 25 was rendered again after the final wording refinement.
- Full EPUB render completed, with the release copied to `docs/Decision-in-the-Making.epub`.
- `python3 scripts/qa_quarto_book.py`: PASS, 0 errors and 0 warnings.
- `python3 scripts/qa_epub_release.py`: PASS, 0 errors.
- `python3 scripts/sync_references.py --check` and `git diff --check`: PASS.
- Confirmed the final subsection and opportunity-assignment wording in both HTML and EPUB (`EPUB/text/ch032.xhtml`).
- Visually inspected the subsection in the browser: readable paragraphs, emphasis, navigation entry, and Chapter 6 link; no observed overlap or clipping.
- Concurrent Chapter 8 source edits were preserved; the rebuilt editions incorporate the shared working tree. No commit, push, or external publication was performed.
