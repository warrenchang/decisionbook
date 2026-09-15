# Chapters 23–25: allocation and revision record

Latest follow-up: [STRUCTURE-REVISION.md](STRUCTURE-REVISION.md) records the subsequent stranger-based opening, revised chapter allocation, and integration of ethics sections.

Date: 15 September 2026  
Baseline: `343f02890ca2f1efaef85f6d5380dbe6615f33ac`  
Scope: canonical Chapters 23–25, their navigation and incoming links, one coordination figure, the master bibliography, and generated HTML/EPUB. No commit or push was requested for this revision.

## The allocation

| Chapter | Title | Main question and sequence |
| --- | --- | --- |
| 23 | Strategic Interdependence | How does the value of my choice depend on others? The Odense meeting game introduces game specification, expected payoffs, best responses, and Nash equilibrium. The portrait task separates preference from prediction. The two-thirds guessing game develops recursive expectations, equilibrium, limited strategic depth, and learning. |
| 24 | Coordination and Focal Points | How do people select and act on compatible plans? A dispute over reporting standards develops focal points, common expectations, strategic uncertainty, payoff and risk dominance, conventions, distributional disagreement, complementary roles, communication, and credible commitment. |
| 25 | Cooperation and Social Preferences | Why contribute when holding back can pay? Colleagues sharing working notes introduce the Prisoner's Dilemma, future incentives, reciprocity and repair, reputation and rules, fairness, and social obligations. An optional research lens brings together the population models. |

Chapter 23 supplies the analytical language through the three lecture examples. Chapter 24 examines selection among compatible outcomes. Chapter 25 examines the further obstacle that someone can gain by departing from an agreement even while others honor it. This distinction links the chapters without treating coordination and cooperation as interchangeable problems.

## Disposition of existing material

- The level-k figure, cognitive-hierarchy model and eight-row evidence table, neural evidence, and individual-learning discussion moved from 24 to 23. The model and detailed evidence remain in a Research Lens; the central distinction between reasoning and prediction stays in the main text.
- Focality, the stag-hunt calculation, conventions and the QWERTY dispute, bargaining over compatible outcomes, complementary roles, and commitment moved from 23 to 24. The two departments now provide a sustained example.
- The old three-lenses figure/table, strategy-diffusion diagnostic, and evolutionary/spatial material moved from 24 into 25's optional research track. The five cooperation mechanisms remain, with their distinct transmission assumptions.
- The price-war matrix, competitive escalation, winner's curse, and market-institution comparison remain available in 23's optional material. The Ford price-promise account moves with commitment to 24 and now cites contemporary reporting directly.
- The generic strategic-situation diagram was replaced with a concrete matrix showing compatible and incompatible reporting standards. The related table now compares coordination obstacles at the same conceptual level. Broad game distinctions are explained through the actual games across the three chapters.
- Part IV, the concept index, the index of major examples, and Chapter 27's beauty-contest link were updated. Existing chapter filenames remain stable, while Chapter 24's visible title changes. Links to relocated material point to its new chapter. Two callout anchors were placed outside the callout headings so EPUB export retains them.

## Scientific checks and corrected interpretations

| Evidence or calculation | Verified treatment |
| --- | --- |
| Meeting matrix | Illustrative payoffs are explicitly labeled. A 70% belief gives 35 versus 15 expected units. Two pure equilibria and the independent equal-randomization equilibrium are distinguished from successful coordination. |
| Guessing game | Real choices in [0,100], at least three players, closest to two-thirds of the mean, fixed prize shared in a tie. The 50→33→22→15 ladder is an approximation, not an exact finite-group best-response calculation. All-zero equilibrium and iterated elimination of weakly dominated high actions are explained separately. |
| Camerer, Ho, and Chong (2004), Table II | All eight rows retained. “Group size” corrected to “Sample size”: some rows pool multiple playing groups. Fitted tau values match observed means and are not presented as independent prediction tests. Occupational comparisons do not identify causal effects. |
| Crawford, Gneezy, and Rottenstreich (2008) | The 64% versus 38% coordination rates are implied by choice frequencies, not observed pair-success rates. The small payoff asymmetry and participant counts are stated. |
| Van Huyck, Battalio, and Beil (1990) | In the seven large-group experiments, the minimum reached one within four rounds. The text does not claim that every participant immediately chose one. |
| Stag hunt | Given the displayed payoffs, choosing stag requires belief p > 8/13. At equal beliefs, expected stag payoff is 8.5 against hare's 10. Risk dominance is distinguished from individual risk aversion. |
| Charness (2000) | Costless messages sent before action improved efficient coordination; communication timing matters. No invented percentage is supplied. |
| Ford price promise | Contemporary trade reporting supports the promise and reported postponement of purchases. The strategic explanation is an interpretation of incentives, not an identified causal effect. Rao et al. (2000) remains in the price-competition discussion. |
| Repeated Prisoner's Dilemma | Under the stated grim-trigger strategies and observation assumptions, continuation weight 1/2 gives 8 versus 8; weight 3/4 gives 16 versus 12. Sustainability in equilibrium does not guarantee that participants cooperate. |
| Social preferences and population models | Existing study values and qualifications remain. Observable choices do not uniquely reveal motives; individual learning, imitation, selection, and population outcomes are distinguished. |

Primary verification used Nagel (1995), Camerer et al. (2004), the original coordination papers, and the sources cited in the revised chapters. Separate agent reviews covered source accuracy, coordination, and cooperation; the final cross-chapter reading found no substantive routing or transition error.

## References

All 47 distinct works in the original three chapters are retained, with 53 distinct works after revision. The three chapter lists contain 14, 9, and 32 entries respectively; works shared across chapters appear in each relevant list. All three lists are alphabetical. Six works were added: Keynes (1936); Crawford et al. (2008); Van Huyck et al. (1990); Charness (2000); and the two contemporary Motor Trader reports (1999a, 1999b). The synchronized book bibliography contains 912 unique entries.

`reference-preservation.json` records the original and new chapter locations of every prior reference. `calculations.json` records the numerical checks. No unpublished lecture slides are cited.

## Verification

- Full HTML and EPUB renders completed successfully. Both contain the revised chapter titles and allocation.
- `scripts/qa_quarto_book.py`: PASS, zero errors and zero warnings.
- `scripts/qa_epub_release.py`: PASS, including all internal links/fragments, packaged images, navigation, and valid XHTML.
- `scripts/qa_float_references.py --rendered --epub-dir <extracted-EPUB>`: PASS across 62 sources, 117 figures, and 148 tables; every float has a local prose reference in source and rendered HTML/EPUB. The revised three chapters contain 7 figures and 13 tables.
- `scripts/sync_references.py --check`: PASS, 912 unique book references. All three revised chapter lists are alphabetical, and the 47 original works are retained.
- Final HTML and extracted-EPUB pages were opened at 1440px and 390px widths: six page/viewport combinations for each format, no failed image loads, unresolved cross-references, or whole-page horizontal overflow. Rendered chapter openings, figures, and revised tables were visually inspected. The new coordination figure fits the narrow page; existing wide diagrams and tables retain their scroll containers. This is browser inspection of EPUB XHTML, not a test of every e-reader application.
- Corrected two payoff-table headers whose backslash separator was consumed by Markdown.
- Restored original permissions on generated files after rendering; unrelated source content is unchanged.
- `git diff --check`: PASS. Work remains local and uncommitted.

The two layout JSON files record the final viewport checks. The new coordination figure's narrow HTML and EPUB screenshots are retained here. `verification-inputs.json` records source and artifact hashes for this revision.


## Subsequent opening revision

The author subsequently requested a more relatable opening for Chapter 23. See [the follow-up record](OPENING-REVISION.md) for the earthquake reunion scene and its verification; `opening-verification-inputs.json` records the resulting versions.
