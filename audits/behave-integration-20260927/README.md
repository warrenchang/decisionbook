# Behave material integration — 27 September 2026

All 18 supplied PDFs were reviewed through complete OCR transcriptions. The source manifest records the original filenames, absolute paths, SHA256 hashes, page counts, and extraction quality. The 36 scanned pages were covered by 238 contiguous tiles. Source hashes were unchanged after extraction. The original PDFs and the prior fly/implicit-knowledge revision were preserved.

OCR is a discovery aid: it contains occasional character omissions and substitutions. Precise new study claims and bibliographic details were checked against published sources. Full OCR and image tiles remain in ignored scratch storage; only compact provenance and editorial records are included here.

## Where the material went

The revision adds or extends passages in Chapters 1, 6, 7, 8, 20, 25, 29, and 34, plus Appendix B. Existing discussions of dopamine, punishment, repeated cooperation, group identity, conformity, rationalization, and replication were retained and used as the main homes for overlapping topics. The concept index provides direct links to the new discussions.

| Source | Main subject | Book destination | Detailed ledger |
|---|---|---|---|
| jy1021 | Causal history and explanatory levels | Ch1; Appendix B | [Topic and source record](causal-genetic-agency.md) |
| jy1022 | Brain organization, emotion, and control | Ch6; existing Ch3/8/21 | [Topic and source record](neuro-development.md) |
| jy1023 | Unconscious influences, cues, bodily states | Ch6; existing Ch3/8/13/21 | [Topic and source record](neuro-development.md) |
| jy1024 | Hormones, attachment, and social context | Ch6; Ch25 links | [Topic and source record](neuro-development.md) |
| jy1028 | Adolescence and peer contexts | Ch20 | [Topic and source record](neuro-development.md) |
| jy1029 | Childhood conditions, adversity, and SES | Ch20; Appendix B | [Topic and source record](neuro-development.md) |
| jy1030 | Gene–environment relations and heritability | Appendix B | [Topic and source record](causal-genetic-agency.md) |
| jy1104 | Cultural history and variation | Ch29 | [Topic and source record](culture-evolution.md) |
| jy1105 | Evolution, kinship, and explanatory limits | Appendix B; existing Ch25 | [Topic and source record](culture-evolution.md) |
| jy1106 | Group identity, stereotypes, and category salience | Ch29/25; Appendix B distinctions | [Topic and source record](culture-evolution.md) |
| jy1108 | First-half recap | Merged into the corresponding main topics | [Topic and source record](causal-genetic-agency.md) |
| jy1111 | Rank, stress, control, dominance, prestige | Ch29 | [Topic and source record](culture-evolution.md) |
| jy1112 | Moral intuition, deliberation, early social evaluation | Ch8/25 | [Topic and source record](moral-social.md) |
| jy1113 | Empathy, compassion, distress, and helping | Ch34 | [Topic and source record](moral-social.md) |
| jy1114 | Symbols, dehumanization, sacred values | Ch7/25/29; existing replication cautions | [Topic and source record](moral-social.md) |
| jy1118 | Free will, neural precursors, and responsibility | Appendix B; Ch8 link | [Topic and source record](causal-genetic-agency.md) |
| jy1119 | Plasticity, social transmission, and hope | Ch29/34; existing Ch25 cooperation | [Topic and source record](moral-social.md) |
| jy1122 | Second-half recap | Merged into the corresponding main topics | [Topic and source record](causal-genetic-agency.md) |

The four detailed ledgers cover substantive claims, illustrative stories, reader comments, duplicates, and administrative material. Each records whether the content was added, merged with existing coverage, corrected, or omitted. [Source manifest](source-manifest.json) resolves each source ID to the supplied PDF.

## Scientific corrections and boundaries

- Interacting neural systems replace a literal triune-brain hierarchy; regional activation is not a unique emotion or a direct neurotransmitter measurement.
- Hormonal interventions are tied to specific tasks, populations, and relationships; attachment does not reduce to one receptor or chemical.
- Adolescent development has no universal age-25 finish line; childhood brain associations and randomized changes in care support different conclusions.
- Heritability describes population variation. Genetic influence is compatible with environmental change; rat epigenetic findings do not establish inherited human trauma.
- Moral intuition and reflection are not equivalent to competing ethical schools. Infant helper preferences are presented alongside the large preregistered replication.
- Shared distress, understanding, compassion, and costly helping are distinguished; post-randomization exclusions and training-order limits are explicit.
- Cultural histories and rank/stress associations do not establish national or biological destiny. The baboon example concerns social transmission with important observational limits.
- Libet used EEG and a movement-timing task. Alternative readiness-potential models and deliberate-choice evidence qualify broad free-will claims.
- Unsupported priming techniques, deterministic class/parenting stereotypes, firing-rate/PTSD narratives, and claims that science has fully explained human behavior were not imported. Philosophical positions remain attributed.

## Review and release checks

The [independent scientific review](independent-review.md) found no remaining blocker after the listed precision corrections. A separate preservation/coherence pass confirmed the prior anchors, figures, and implicit-knowledge passage remained intact.

Both editions were rebuilt and verified:

- Book QA: **0 errors, 0 warnings** across 42 chapters.
- EPUB release QA: **0 errors**, with seven Parts and 42 numbered chapters.
- Float references: **0 issues** across 62 sources, 108 figures, and 164 tables.
- Master bibliography: synchronized, **1,186 unique references** in the checked shared checkout.
- Integration-specific checks: all **19 new anchors** present exactly once in the relevant HTML and in the EPUB; all **18 source PDF hashes unchanged**; the prior implicit-knowledge passage unchanged.
- `git diff --check`: passed.
- Representative desktop browser checks covered Chapters 20 and 34 and Appendix B, including opening the agency research note. This was not an exhaustive visual audit of every page or viewport.

[Machine-readable integration results](verification.json) record source/output hashes and preservation checks; [release results](release-checks.json) record commands, counts, visual scope, and the final build snapshot. Re-run `python3 audits/behave-integration-20260927/verify_integration.py` after rebuilding to check these additions. Task-start snapshots and source PDFs are checked when available locally.

Other tasks were editing this same checkout. Their additions were preserved and affected HTML pages refreshed before the final EPUB build. The book-wide counts include those concurrent edits and should not be read as additions from the Behave materials alone.

Changes remain local to this checkout. No commit, push, or external publication is part of this integration.
