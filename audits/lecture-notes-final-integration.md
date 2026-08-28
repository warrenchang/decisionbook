# Lecture Notes final integration report

**Status: PASS**

All **229** unique paths in the verified Lecture Notes audit have a final disposition. This report must be read with `lecture-notes-coverage.csv`, which preserves the source-level content, rights, duplicate, quantitative-claim, and verification notes.

## What PASS means

PASS means every source path was inventoried, verified, reviewed, and either routed into the book or given an explicit reason for non-reuse. It does not mean that copyrighted figures were copied, that build artifacts became prose, or that unsupported claims were retained. Exact duplicates and derivatives are not counted as additional evidence. Cosmetic modification is not treated as a copyright solution.

The source audit's `gap_status` field records the state of the book before this revision. The final-status and final-destination fields in the CSV below record how those gaps were resolved in the revised book.

## Final handling counts

| Handling | Files |
| --- | ---: |
| `excluded_noncontent` | 16 |
| `incorporated_via_source_family` | 58 |
| `not_reused_rights_or_provenance` | 40 |
| `supporting_duplicate` | 107 |
| `synthesized_no_direct_reproduction` | 3 |
| `verification_lead_only` | 5 |

## Source-family counts

| Source family | Files |
| --- | ---: |
| 01 Foundations — anatomy/predictive evaluation manuscripts | 5 |
| 01 Foundations — decision process | 4 |
| 01 Foundations — introduction to behavioral economics | 2 |
| 01 Foundations — neuroeconomics | 1 |
| 01 Foundations — neuroscience of judgment and decision | 4 |
| 01 Foundations — predictive processing, free energy, and active inference | 1 |
| 01 Foundations — predictive processing, free energy, and active inference \|\| ADDITIONAL AUDIT: Foundations and neuroscience / active inference | 1 |
| 01 Foundations — predictive processing, free energy, and active inference \|\| ADDITIONAL AUDIT: Top-level repaired active-inference assets | 3 |
| 01 Foundations — science of decision making | 3 |
| 01–02 Perception — optical illusions and indirect seeing | 3 |
| 02 Attention — selection, prediction, and expectation | 4 |
| 02 Biases — story protection and contextual judgment | 3 |
| 02 Context — cognitive ease and familiarity | 2 |
| 02 Heuristics and biases — combined lecture | 3 |
| 02 Heuristics — adaptive shortcuts | 2 |
| 02 Heuristics — two-process thinking | 5 |
| 03 Choice architecture and nudge | 6 |
| 03 Context — framing, priming, and contextual influence | 4 |
| 03 Habits and behavior design | 6 |
| 04 Probability judgment | 2 |
| 04 Probability judgment \|\| ADDITIONAL AUDIT: Root synthesis/Probability judgment | 1 |
| 04 Prospect theory and reference-dependent choice | 2 |
| 04 Prospect theory and reference-dependent choice \|\| ADDITIONAL AUDIT: Root synthesis/Prospect theory | 1 |
| 04 Risky decision making | 2 |
| 04 Risky decision making \|\| ADDITIONAL AUDIT: Root synthesis/Risky decision-making | 1 |
| 05/Cooperation and coordination | 2 |
| 05/Evolutionary game theory | 4 |
| 05/Evolutionary game theory/NetLogo models | 7 |
| 05/Evolutionary game theory/TeX build | 9 |
| 05/Evolutionary game theory/images | 44 |
| 05/Evolutionary game theory/research article | 2 |
| 05/Social preferences and norms | 6 |
| 05/Strategic interdependence | 6 |
| 05/Strategic interdependence and behavioral game theory | 3 |
| 06/Asset bubbles | 5 |
| 06/Behavioral finance and investment decisions | 6 |
| 06/Intertemporal choice | 3 |
| 06/Mental accounting | 5 |
| 06/Money and mind composite | 1 |
| 07/Decision from experience | 3 |
| 07/Market experiment | 1 |
| 07/Newsvendor/operations | 1 |
| 08 - Research Methods | 7 |
| 09 - Additional Topics | 1 |
| 09 - Additional Topics / ABT | 1 |
| 09 - Additional Topics / cooperation | 2 |
| 09 - Additional Topics / evolutionary game theory | 1 |
| 09 - Additional Topics / happiness and behavioral finance | 1 |
| 09 - Additional Topics / legacy decision theory | 1 |
| 09 - Additional Topics / negotiation extensions | 1 |
| 09 - Additional Topics / neuroscience and self-help | 1 |
| 09 - Additional Topics / risk elicitation and operations | 1 |
| 09 - Additional Topics / subjective well-being | 4 |
| DPN2026 lecture sequence | 7 |
| Lecture Notes root | 1 |
| Readings | 1 |
| Readings / AI, prediction, and complexity | 8 |
| Readings / instructor notes | 2 |
| Readings / priming and goal setting | 4 |
| Readings / research design and replication | 6 |

## Exact-path evidence

The complete eight-field ledger is `audits/lecture-notes-final-integration.csv`. Each row retains the source SHA-256 and records the final status, mapped book destination, and handling decision.

## Publication rules applied

- Facts, concepts, and numerical results were checked against source authority in proportion to risk.
- Copyrighted journal artwork, commercial images, screenshots, and uncertain-rights photographs were not made reusable merely by cosmetic modification.
- Verifiable results were reconstructed in original tables or diagrams; otherwise the book cites the study without reproducing its figure.
- Local slides labelled only as 'our experiment' were not presented as evidence without an underlying design, sample, data, and analysis.
- Administrative files, empty documents, and software build products remain in the source inventory but do not enter the reader-facing book.
