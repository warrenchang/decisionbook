# Independent review: Social Influence and neighboring chapters

Reviewed 24 September 2026. Scope: revised Chapter 28 and its placement and transitions relative to Chapters 26, 29, and 30. Read-only review of chapter sources; this report does not certify a rendered HTML or EPUB build.

## Assessment

The revised allocation is coherent. Chapter 26 explains norms and conformity; Chapter 28 develops requests, compliance, authority, and failures of collective judgment; Chapter 29 explains how identity and culture change the meaning of social behavior; Chapter 30 focuses on persuasive changes in beliefs and attitudes. Chapter 28 explicitly distinguishes persuasion, compliance, conformity, and obedience, while allowing them to overlap. Its recurring safety-email example gives the later material a common problem to explain. The cue checklist and process safeguards are explicitly practical syntheses, not a unified experimentally validated treatment.

No material numerical or outcome-definition errors were found in the seven newly developed study accounts below. There is no need to dilute their presentation with a generic caveat after every result.

## Actionable findings

1. **New Chapter 26 link can lose its destination in EPUB.** Chapter 26 links to `28-authority-groupthink-and-shared-responsibility.qmd#authority-groupthink-and-shared-responsibility`. The target alias in Chapter 28 is inside a `content-visible unless-format="epub"` block, while the renamed H1 generates a different identifier. Point the new link to `#chapter-28-start`, or preserve the old alias in EPUB as well. The source-level risk should be checked in the final EPUB output.
2. **Chapter 28 still contains seven DOI URLs.** These occur in the Aldag–Fuller, Esser, Fischer, Haslam–Reicher, Mullen, Perry, and Stasser–Titus reference entries. Remove the DOI URLs to follow the user's established reference preference; retain the bibliographic entries.

Two optional, small refinements:

- Introduce the cookie findings as **Worchel and colleagues' first experiment**. The described contrasts are accurate for Experiment 1. Experiment 2 did not show scarcity effects when hypothesis-aware participants were retained, so specifying the first experiment avoids implying uniform confirmation throughout the paper. This does not require a new paragraph or a full replication debate.
- Chapter 28's reciprocity link currently lands inside Chapter 25's collapsed advanced research track (`#outcomes-and-intentions-are-different`). The main-text `#mutual-cooperation-and-reward` section is a more direct destination for readers following the introductory explanation. The current link is not a hard error.

## Study checks

| Study | Verified design and result | Judgment on revised passage |
| --- | --- | --- |
| Langer, Blank, & Chanowitz (1978), Experiment 1 | For the small request, no reason yielded 60% compliance and the circular copying reason 93%; corresponding large-request rates were 24% and 24%. These were permissions to proceed at a copier. | Correct. The passage avoids treating “because” as a universal trigger or the result as attitude change. |
| Regan (1971) | The confederate's favor, an irrelevant favor from the experimenter, and no favor were contrasted. More than one raffle ticket was bought by 58% in the confederate-favor condition and 25% across the pooled controls. The liking manipulation's effect on purchasing did not meet conventional significance. | Correct. The threshold and pooled comparison are identified. “Supports an obligation” is appropriately more cautious than claiming a uniquely identified mediator. |
| Freedman & Fraser (1966), Experiment 2 | The small road-safety-sign condition produced 76.0% agreement to the later large sign (25 participants), compared with 16.7% in the one-contact control (24). A different requester made the later request. | Correct. Small cells are disclosed, and the passage acknowledges multiple possible mechanisms. |
| Cialdini et al. (1975), Experiment 1 | Rejection of a two-hours-per-week, minimum-two-years counseling request preceded the two-hour outing request. Expressed willingness was 50% versus 16.7% for the outing-only control. | Correct. The passage explicitly avoids presenting willingness as attendance. |
| Cialdini et al. (1978), Experiment 1 | A 7 a.m. experiment time was disclosed before or after the initial decision. Attendance was 18/34 (53%) in low-ball and 7/29 (24%) in control. Verbal agreement, a different outcome, was 56% versus 31%. | Correct. Uses attendance rather than confusing it with verbal agreement. |
| Worchel, Lee, & Adewole (1975), Experiment 1 | Two versus ten cookies, and demand-related versus accidental changes in supply, affected desirability/attractiveness ratings. Taste ratings showed no significant effects. Purchases were not measured. | Correct outcome distinction; specifying Experiment 1 would improve precision. |
| Burger et al. (2001) | Three experiments tested brief interaction, mere exposure, and perceived similarity in relation to compliance. | The concise description matches the study scope; it does not claim that warmth invariably defeats judgment. |

The pre-existing Milgram/Burger 2009 discussion appropriately distinguishes the 1963 300/450-volt results from Burger's 150-volt cutoff and retains the interpretive qualifications. The hidden-profile discussion does not mistake collecting initial opinions for pooling distributed evidence. The bystander discussion distinguishes an individual's intervention from the probability that anyone in a crowd acts and distinguishes the early window from the six-minute cutoff.

## Primary sources consulted

- [Langer, Blank, and Chanowitz original article transcript](https://studylib.net/doc/8192259/the-mindlessness-of-ostensibly-thoughtful-action--the-rol...)
- [Regan (1971), original article](https://www.decisionskills.com/uploads/5/1/6/0/5160560/regan_1971_reciprocity.pdf)
- [Freedman and Fraser (1966), original article](https://www.bulidomics.com/w/images/6/6c/Freedman_fraser_footinthedoor_jpsp1966.pdf)
- [Cialdini et al. (1975), original article](https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Influence_Compliance/Cialdini.et.al.Reciprocal.Concessions.Procedure.1975.article.pdf)
- [Cialdini et al. (1978), original article](https://www.bulidomics.com/w/images/1/15/Low-ball_cialdini-cacioppo-bassett-miller_1978.pdf)
- [Worchel et al. (1975), original article](https://www.bulidomics.com/w/images/6/69/Effects-of-supply_worchel-lee-adewole_1975.pdf)
- [Burger et al. (2001), original article](https://citeseerx.ist.psu.edu/document?doi=918456c65c1f26339d2c4a1ceea022680f807208&repid=rep1&type=pdf)

The study-level checks above used primary article text. They do not constitute a systematic review of later replication evidence. Neighboring-chapter placement and links were checked against the current QMD sources; output-level navigation remains part of the parent task's release checks.

## Integration resolution

The coordinating editor corrected both actionable findings, specified the first Worchel experiment, and updated the reciprocity destination. The legacy Chapter 28 anchor is now retained in both HTML and EPUB, also preserving the existing Chapter 27 link. Final output checks are recorded in `verification.json`.
