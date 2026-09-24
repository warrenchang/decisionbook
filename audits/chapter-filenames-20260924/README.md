# Chapter filename update · 24 September 2026

All 42 canonical chapter filenames now follow the current chapter number and H1 title. Thirty-eight were renamed; four already matched. Chapters 19 and 20 now have filename numbers consistent with the established reading order: Mental Accounting, then Intertemporal Decision Making.

Active book links, HTML/EPUB configurations, the concept index, and current QA script paths were updated. Chapter text and section identifiers were preserved; only file paths and redirect aliases changed. Existing staged changes were left untouched. Historical audit records and the earlier one-time migration script retain their original paths.

Quarto aliases retain every former published chapter URL, including earlier aliases, and carry section fragments forward. The complete old-to-new map is in [mapping.json](mapping.json).

## Current chapter files

| Chapter | Title | Source |
| ---: | --- | --- |
| 1 | Understanding Decision Making | [01-understanding-decision-making.qmd](../../chapters/01-understanding-decision-making.qmd) |
| 2 | Structuring a Decision | [02-structuring-a-decision.qmd](../../chapters/02-structuring-a-decision.qmd) |
| 3 | Limited Attention | [03-limited-attention.qmd](../../chapters/03-limited-attention.qmd) |
| 4 | Predictive Mind | [04-predictive-mind.qmd](../../chapters/04-predictive-mind.qmd) |
| 5 | Expectations | [05-expectations.qmd](../../chapters/05-expectations.qmd) |
| 6 | Valuation | [06-valuation.qmd](../../chapters/06-valuation.qmd) |
| 7 | Narrator After Choice | [07-narrator-after-choice.qmd](../../chapters/07-narrator-after-choice.qmd) |
| 8 | Intuition and Deliberation | [08-intuition-and-deliberation.qmd](../../chapters/08-intuition-and-deliberation.qmd) |
| 9 | Availability, Affect, and Representativeness | [09-availability-affect-and-representativeness.qmd](../../chapters/09-availability-affect-and-representativeness.qmd) |
| 10 | Confirmation Bias and Motivated Reasoning | [10-confirmation-bias-and-motivated-reasoning.qmd](../../chapters/10-confirmation-bias-and-motivated-reasoning.qmd) |
| 11 | Anchors, Halos, and Decoys | [11-anchors-halos-and-decoys.qmd](../../chapters/11-anchors-halos-and-decoys.qmd) |
| 12 | Framing | [12-framing.qmd](../../chapters/12-framing.qmd) |
| 13 | Priming, Fluency, and Familiarity | [13-priming-fluency-and-familiarity.qmd](../../chapters/13-priming-fluency-and-familiarity.qmd) |
| 14 | Base Rates and Updating | [14-base-rates-and-updating.qmd](../../chapters/14-base-rates-and-updating.qmd) |
| 15 | Randomness and Overconfidence | [15-randomness-and-overconfidence.qmd](../../chapters/15-randomness-and-overconfidence.qmd) |
| 16 | Risky Decision Making | [16-risky-decision-making.qmd](../../chapters/16-risky-decision-making.qmd) |
| 17 | Prospect Theory | [17-prospect-theory.qmd](../../chapters/17-prospect-theory.qmd) |
| 18 | Decisions From Experience | [18-decisions-from-experience.qmd](../../chapters/18-decisions-from-experience.qmd) |
| 19 | Mental Accounting | [19-mental-accounting.qmd](../../chapters/19-mental-accounting.qmd) |
| 20 | Intertemporal Decision Making | [20-intertemporal-decision-making.qmd](../../chapters/20-intertemporal-decision-making.qmd) |
| 21 | Habits, Wanting, and Self-Control | [21-habits-wanting-and-self-control.qmd](../../chapters/21-habits-wanting-and-self-control.qmd) |
| 22 | Deciding for a Better Life | [22-deciding-for-a-better-life.qmd](../../chapters/22-deciding-for-a-better-life.qmd) |
| 23 | Strategic Interdependence | [23-strategic-interdependence.qmd](../../chapters/23-strategic-interdependence.qmd) |
| 24 | Coordination and Focal Points | [24-coordination-and-focal-points.qmd](../../chapters/24-coordination-and-focal-points.qmd) |
| 25 | Cooperation and Social Preferences | [25-cooperation-and-social-preferences.qmd](../../chapters/25-cooperation-and-social-preferences.qmd) |
| 26 | Social Norms and Conformity | [26-social-norms-and-conformity.qmd](../../chapters/26-social-norms-and-conformity.qmd) |
| 27 | Markets, Mispricing, and Bubbles | [27-markets-mispricing-and-bubbles.qmd](../../chapters/27-markets-mispricing-and-bubbles.qmd) |
| 28 | Social Influence | [28-social-influence.qmd](../../chapters/28-social-influence.qmd) |
| 29 | Culture and Identity | [29-culture-and-identity.qmd](../../chapters/29-culture-and-identity.qmd) |
| 30 | Persuasion | [30-persuasion.qmd](../../chapters/30-persuasion.qmd) |
| 31 | Storytelling | [31-storytelling.qmd](../../chapters/31-storytelling.qmd) |
| 32 | Message Design | [32-message-design.qmd](../../chapters/32-message-design.qmd) |
| 33 | Communication | [33-communication.qmd](../../chapters/33-communication.qmd) |
| 34 | Connection and Repair | [34-connection-and-repair.qmd](../../chapters/34-connection-and-repair.qmd) |
| 35 | Negotiation as Joint Decision Design | [35-negotiation-as-joint-decision-design.qmd](../../chapters/35-negotiation-as-joint-decision-design.qmd) |
| 36 | Distributive Negotiation | [36-distributive-negotiation.qmd](../../chapters/36-distributive-negotiation.qmd) |
| 37 | Integrative Negotiation | [37-integrative-negotiation.qmd](../../chapters/37-integrative-negotiation.qmd) |
| 38 | Designing Better Agreements | [38-designing-better-agreements.qmd](../../chapters/38-designing-better-agreements.qmd) |
| 39 | Behavior Design | [39-behavior-design.qmd](../../chapters/39-behavior-design.qmd) |
| 40 | Choice Architecture | [40-choice-architecture.qmd](../../chapters/40-choice-architecture.qmd) |
| 41 | Decision Hygiene | [41-decision-hygiene.qmd](../../chapters/41-decision-hygiene.qmd) |
| 42 | Deciding With Data and AI | [42-deciding-with-data-and-ai.qmd](../../chapters/42-deciding-with-data-and-ai.qmd) |

## Checks

The final checks are recorded in [validation.json](validation.json). They cover filename/title consistency, preservation of chapter content and anchors, references, generated navigation and search, old-URL redirects, internal links, and the EPUB release.

For future title changes, `python3 scripts/sync_chapter_filenames.py` previews the proposed updates; `--apply` makes them. A second run after this update reports zero remaining changes.

No commit or push was performed.
