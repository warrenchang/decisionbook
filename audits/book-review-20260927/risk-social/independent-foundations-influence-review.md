# Independent review of the other chapter ranges

Reviewer: risk/social chapter worker, 2026-09-27. This is a bounded, read-only review of the substantive additions in Chapters 01–14 and 30–42 against the current Git baseline. The reviewer did not author these additions. This is not a second complete review of the original chapters or a claim that every cited article was independently re-read. Canonical source files were not edited during this review.

## Finding

No material scientific, attribution, mathematical, or explanatory issue was found in the new prose within this scope. One minor numerical-language correction was sent to the root integrator in Chapter 38. The fee arithmetic is correct, but the sentence “The client gains €100,000 while the adviser loses €9,500” describes the gross sale-price change, not the client's net proceeds if the client pays the fee. Suggested wording: “The sale price rises by €100,000 while the adviser’s fee falls by €9,500.” Under the stated whole-price schedule, net client proceeds rise €109,500. The incentive conclusion is unaffected.

The root integrator applied the suggested wording; the corrected canonical sentence was verified at handoff. No open correction remains from this review.

## Scope actually reviewed

All substantive added paragraphs in the following changed chapters were read, including the surrounding comparison needed to assess the new claim. Chapter-local bibliography additions were checked against the authors' verification records rather than treated as independently replicated metadata.

| Chapters | Additions checked and assessment |
| --- | --- |
| 01 | Testable models and distinctions between explanation and description: clear and appropriately bounded. |
| 03 | Own-name detection, NASA head-up displays and unexpected obstacle, noticing illustration: the small-sample and nonuniversal detection boundaries are present. |
| 04 | Thatcher illusion; fear and ambiguous figures; conditioned hallucinations; infant phoneme discrimination: perceptual interpretation is separated from reporting, voice hearing from treatment need, and learning from irreversible incapacity. |
| 05 | Beer information timing; milkshake and ghrelin; control mindset and chocolate; room attendants and adolescent contrast; arousal reappraisal; aging self-perceptions: different manipulations/populations are not misrepresented as exact replications, endocrine outcomes are distinguished from craving/intake, and observational survival findings are not causal longevity effects. |
| 06 | Incidental valuation, masked incentives and grip force, neural prediction of purchases, name-letter preference: visible incidental stimuli are distinguished from subliminal exposure, neural prediction from causal necessity, and a narrow letter preference from career/partner causation. |
| 07 | Split-brain chicken/claw/snow/shovel example: appropriately presented as a clinical illustration with limits on generalization. |
| 08–10 | Additional reflection problems, seven-letter word subset, authored personality description: solutions and set inclusion are correct; invented teaching text is not presented as a study quotation. |
| 11–13 | Price-first sequencing, enriched-profile selection/rejection and mixed replication, dog/Puma accessibility, associative false-memory list: sequence effects are separated from arbitrary anchoring, replication does not become universal confirmation, and the shortened word list is identified as an adapted illustration. |
| 14 | Compounding independent deadline probabilities and two Monty Hall host protocols: calculations and conditioning are correct for the stated assumptions. |
| 31–32 | Film synchronization and Gettysburg argument structure: shared neural time courses are not equated with agreement, editing is not isolated causally, and retrospective ABT analysis is identified as an interpretive/practitioner framework. |
| 36 | Alternatives, shared software purchase and equal incremental gains, deadline disclosure: declared outside options support the arithmetic; a fairness proposal is not labeled a unique economic solution, and time limits are separated from delay costs. |
| 38 | Whole-price fee cliff versus marginal fee schedule: arithmetic and behavioral incentive are correct; the minor gross/net wording issue above was flagged. |
| 39 | Process versus outcome simulation: duration, student setting and comparison are explicit; mediation analysis is not promoted to experimentally isolated causal mediation. |
| 40 | Search/screening, dating choices, calorie-label position, Copenhagen airport lanes, supermarket goal cues: observational screening and nonrandom field periods are explicit, purchase is not equated with consumption/weight, and calorie-label placement is contingent on the displayed layout and reading direction. |

Chapters 02, 30, 33, 34, 35, 37, 41 and 42 had no substantive additions in the reviewed Git diff. This report does not independently recertify their unchanged content. Appendix changes and the older Chapter 29 preschool passage are outside this review.

## Evidence and arithmetic checks

The chapter authors' claim-level records were read in `../foundations/source-verification.md` and `../influence-design/verification.md`. Those records make access limits explicit; their full-text claims are not extended here. Fresh primary-source spot checks during this independent review covered:

- Powers, Mathys and Corlett (2017): [PubMed primary abstract and figure captions](https://pubmed.ncbi.nlm.nih.gov/28798131/) support the conditioning procedure, voice-hearing comparison, and distinction from treatment need.
- Franssen et al. (2022): [Maastricht University primary article record/abstract](https://cris.maastrichtuniversity.nl/en/publications/effects-of-mindset-on-hormonal-responding-neural-representations-/) supports craving/intake changes alongside absence of the predicted mindset effects on ghrelin/GLP-1. It is not the milkshake-label experiment.
- Jamieson, Nock and Mendes (2012): [primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3410434/) supports randomized reappraisal instructions, cardiovascular response and threat-attention outcomes. Indexed primary text was available; the direct PMC page encountered a challenge. No chronic-stress health conclusion is needed by the chapter.
- Robertson and Lunn (2020): the primary article abstract supports layout-dependent effects and the strongest result for calories just right of price. This is compatible with the chapter's rejection of a universal left-placement rule; it does not establish that the studies used the same menu layout.

Other new studies were assessed against the source verification records and the wording in the chapter. This independent review did not newly obtain every original dataset, paper PDF, or preregistration.

The self-contained examples were independently recomputed:

- Five independent stages at 0.9 success probability each give 0.9^5 = 0.59049. Correlated stages need a different calculation.
- The specified standard Monty Hall host protocol gives 2/3 to switching; an uninformed host who happens to reveal a goat gives 1/2 after conditioning on that event.
- In the three shared-license cases, prices 50, 150 and 250, values 100/200 and the stated separate-purchase alternatives imply equal-incremental-gain payments (25,25), (50,100), and (75,175), respectively.
- At sale prices 2,000,000 and 2,100,000, the whole-price rule pays 20,000 and 10,500; the alternative marginal rule pays 20,500 for the higher price.
- The reflection-task answers (five minutes; day 47) and the seven-letter word subset relation are correct.

Rendering, EPUB production, master-reference synchronization, and link/figure QA remain the root integrator's responsibility. No additional expansion is recommended by this bounded check.
