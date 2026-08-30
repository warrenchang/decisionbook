# Deleted-Text Reconciliation

**Audit date:** August 30, 2026  
**Comparison baseline:** commit `73c2111`, the last canonical 48-chapter version before consolidation  
**Current architecture:** seven parts and 41 canonical chapters

## What counts as a deletion

The large set of deleted chapter paths shown by Git is mostly a filename migration. The canonical source and rendered chapter files were renamed so that each filename begins with its current chapter number and title. Those delete/add pairs do not represent lost prose.

The substantive audit therefore compared the current 41-chapter manuscript with every chapter in the 48-chapter baseline. It also checked the eight `chapters/retired-*.qmd` sources retained after chapter mergers. The comparison classified earlier text into four groups:

1. **Retained or rewritten:** the mechanism, evidence, example, or tool remains in the same conceptual location.
2. **Relocated:** the material survives where it now fits the causal sequence better.
3. **Selectively restored:** a distinct and useful item had disappeared during consolidation and has now returned in a shorter, better-bounded form.
4. **Intentionally omitted:** repetition, generic exercises, weakly supported anecdotes, long application tours, or technical detail that did not earn its interruption remain outside the canonical narrative.

## Standalone chapters that became mergers

Eight former standalone chapters remain in the repository as retired source files. Their substantive destinations are documented in `excluded-chapters-consolidation-audit.md`:

| Former standalone material | Current destination |
| --- | --- |
| Opportunity cost, information, and better options | Chapter 2 |
| The adaptive toolbox | Chapter 8 |
| Resemblance and probability | Chapters 9, 14, and 15 |
| Fluency, familiarity, and truth | Chapter 13 |
| Wanting, craving, and self-control | Chapter 21 |
| Conformity, norms, and social proof | Chapter 26 |
| Bargaining anchors, concessions, and tactics | Chapter 36 and Appendix A |
| Asset bubbles | Chapter 27 |

These chapter titles disappeared from the table of contents; their central content did not.

## Important relocations

Several passages that look deleted when chapters are compared one by one now appear elsewhere:

- attribution and self-serving explanation moved from the former social-learning chapter to Chapter 10, where belief-protective interpretation is developed;
- planning fallacy and outside-view forecasting moved into Chapter 10 and Chapter 41, while sunk cost and escalation moved into Chapters 20 and 23;
- identity salience moved from priming into Chapters 6 and 29;
- probability axioms, natural frequencies, dilution, sampling error, regression, and calibration were divided between Chapters 14 and 15;
- habit diagnosis, wanting versus liking, and self-control were combined in Chapter 21, while intervention design moved to Chapter 39;
- social learning, social proof, descriptive and injunctive norms, conformity, pluralistic ignorance, and cascades were combined in Chapter 26;
- mediation, arbitration, cultural differences in negotiation, and claim verification now receive fuller treatment in Chapter 38;
- finance and bubble material was combined in Chapter 27 and placed after strategic interaction and social learning, whose mechanisms it applies;
- the health and welfare consequences of connection moved to Chapter 22, while conversational grounding and repair remain in Chapters 33 and 34.

## Material selectively restored in this pass

The audit found several compact items whose explanatory or teaching value was not fully replaced by the consolidated text:

| Restored item | Destination | Why it earns space |
| --- | --- | --- |
| A visible decision branch for the value of information | Chapter 2 | Converts an abstract principle into the question: what possible result would change action? |
| Recognition-primed expert intuition | Chapter 8 | Explains how learned pattern recognition can retrieve and mentally test a workable action without treating intuition as magic. |
| Arithmetic average versus multiplicative ruin | Chapter 16 | Distinguishes expected return, expected terminal wealth, a typical compounded path, drawdown, and ruin. |
| A bounded comparison of historical market anomalies | Chapter 27 | Preserves competing behavioral, risk, friction, and data-mining accounts without restoring a long finance survey. |
| Identity-safe teaching | Chapter 29 | Shows how difficulty can communicate either investment or exclusion while keeping structural access and context visible. |
| An influence-cue signal audit | Chapter 30 | Restores reciprocity, commitment, scarcity, liking, unity, reason-giving, social proof, and authority as conditional signals rather than behavioral buttons. |
| Shared reality | Chapter 33 | Defines the perceived common ground that communication can create without confusing agreement with truth. |
| Errors in social forecasts | Chapter 34 | Connects prediction to conversation by showing that people can underestimate the benefits of contact and how much partners liked them. |
| Reciprocal, responsive self-disclosure | Chapter 34 | Restores the evidence-based distinction between appropriately paced disclosure and disclosure used as an intimacy technique. |
| Watching-eyes evidence update | Appendix D | Turns a memorable field finding and its later meta-analytic update into a concrete lesson in cumulative evidence. |

## Material that remains omitted

The following removals improve the book and were not reversed:

- repeated Core Idea, Key Ideas, generic question banks, and duplicate Experience–Explain–Apply instructions;
- long domain-by-domain tours that repeated the same persuasion, storytelling, culture, negotiation, or choice-design mechanism;
- the long influence-trigger catalogue: the diagnostic table returns, but not a promise that each label is a universal compliance technique;
- the mother-turkey analogy and broad unconscious social-priming claims, which would overstate how directly such demonstrations transfer to human decisions;
- the Roosevelt campaign anecdote and other historical stories whose documentation was too uncertain for the role assigned to them;
- duplicate orange, mismatched-shoes, and Camp David negotiation examples once the supplier case became the running case;
- long technical-analysis and bubble-history tours that would interrupt the strategic and social mechanism of Chapter 27;
- exact evolutionary-game derivations and extended spatial-model tours already represented by a bounded Research Lens in Chapter 24;
- an extended clinical-addiction survey whose key wanting, learning, context, and recovery distinctions already survive in Chapter 21;
- repeated worked applications where one developed case now carries the mechanism more clearly.

## Editorial rule

Earlier wording was not restored merely because it once appeared in the manuscript. A passage returned only when it supplied a distinct mechanism, discriminating example, evidence boundary, or reusable tool that the current book otherwise lacked. The result remains a consolidation rather than a reconstruction of the 48-chapter catalogue.
