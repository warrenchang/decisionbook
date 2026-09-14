# Independent semantic review of three root-owned figures

Reviewed the current SVGs, their individual canonical PNGs, associated generator functions, and relevant appendix captions/alternative text. This was a read-only review of production files; no SVG, generator, QMD, or PNG was changed by the reviewer. Final HTML/EPUB and narrow-reader layout remain the root agent’s checks.

## F.3: participant-flow-threats — PASS

The figure is independently informative. Noncompliance explicitly distinguishes treatment assigned from treatment received, including treatment nonreceipt and control crossover. Attrition separately concerns missing outcomes after loss to follow-up and states the conditional possibility that observed groups cease to be comparable. Spillovers/interference are drawn as one person’s treatment affecting another person’s outcome; they are not depicted as failure to take treatment or failure to observe outcomes. There are no connecting arrows between the three panels that could imply a mandatory sequence.

The ITT panel correctly compares outcomes by original assignment and explicitly says that this alone does not resolve attrition or spillovers. That preserves the distinction between an analysis principle and the additional assumptions needed when outcomes are missing or units affect each other. The definitions agree with the [CONSORT 2025 explanation](https://www.bmj.com/content/389/bmj-2024-081124) and the interference definition in [Hudgens and Halloran (2008)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2600548/). The visible qualifications “may” and “can” appropriately avoid treating every noncompliant or incomplete trial as necessarily biased.

Native PNG inspection: the panel headings, explanations, and ITT limitation are legible; all text fits; connectors meet their nodes; the panels are clearly separate. The current generator output reproduces the SVG exactly (ignoring terminal whitespace). Caption and alternative text describe the four-panel design accurately. No correction requested.

## selected-evidence-pipeline — PASS

Stage 4 now explicitly identifies analysis and reporting, while stage 5 identifies publication. Their questions distinguish selection among analyses/results from selection in what reaches readers. Earlier question, design, and data stages retain their separate questions. The sequence is clear without chapter prose, text fits the panels, and connectors attach. Generator output exactly reproduces the SVG (ignoring terminal whitespace); current alternative text matches. No correction requested.

## schelling-emergence — PASS

The statistic is identified as a mean same-group-neighbor share, and the added sweep/occupied-neighbor explanation makes the sequence interpretable without the appendix prose. The figure remains explicitly one teaching run, retains the one-third local threshold, seed, group/vacancy key, move counts, and unchanged grids.

Read-only reconstruction from the generator produces moves [36, 6, 2, 0], with 38 vacancies and 107 agents per group in all three displayed grids. Mean shares are 0.4834279, 0.6377281, and 0.6805352, matching 0.48, 0.64, and 0.68. All 759 circle attribute sets match the semantic-review before snapshot, so the added explanation did not alter the illustrated population or positions. Generator output exactly reproduces the SVG (ignoring terminal whitespace). Native PNG inspection finds no clipping, label overlap, or missing legend. No correction requested.

## Reviewed production versions

- `figures/participant-flow-threats.svg`: SHA-256 `8a7bdeb0e50733d9eca31bfee0df60d057e61eba0973558a65a6b32c65e9e6df`
- `figures/participant-flow-threats.png`: SHA-256 `11a56bbbdd996b8f76032e1e0a968508b232ce2f394b4cca8729e7710831b81c`
- `figures/selected-evidence-pipeline.svg`: SHA-256 `949c01b066b7dcd9beb34444e6a694d77ef47e50099b4b6a150e06e5a43681cb`
- `figures/selected-evidence-pipeline.png`: SHA-256 `30c64c75e7e7a37fa7329793a3e51f50feb4e30362acca5712a3345c2a2f4c3d`
- `figures/schelling-emergence.svg`: SHA-256 `492821ff5bac4240d5d7327239852453236bfbbe54bd7e2bb606b5c8fc548bf7`
- `figures/schelling-emergence.png`: SHA-256 `5668fd38fb58e87fa82ca3ca06ca2b07985f2c2ebcb46054172d08246d45a841`

## Final regenerated contact-sheet overview — PASS

Inspected `/tmp/figure-information-review-20260914/final-contact/figures-06.png` through `figures-10.png` after all 46 changed figures were regenerated. These five sheets contain 54 assets, including the final added labels in all late figures and the redesigned F.3. No missing content, text collisions, clipping, or newly unbalanced spacing was apparent. The larger agreement-tool cards and both AI figures show the final clarifications. This overview supplements the individual native inspections above; it does not replace destination/phone checks. No production asset changes were made during this check.
