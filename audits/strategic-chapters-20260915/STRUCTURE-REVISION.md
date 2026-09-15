# Chapters 23–25: structure follow-up — 15 September 2026

This record supersedes the earlier opening and allocation descriptions in OPENING-REVISION.md and REVISION-NOTES.md. It records the author's subsequent request to use unfamiliar people in the meeting scene, postpone payoff matrices until Chapter 24, introduce equilibrium late in Chapter 23, replace Chapter 24's epigraph, and integrate the book's formulaic standalone ethics sections.

## Allocation and narrative

- **23, Strategic Interdependence:** An unfamiliar volunteer has agreed to help the reader leave the city after an earthquake; communication fails before they agree on where and when to meet. The scene establishes shared purpose without assuming knowledge of private preferences. The discussion develops the meeting problem, private face preferences versus rewarded face matching, and the two-thirds guessing game. Learning and limits of strategic inference follow. Nash equilibrium is introduced near the end, before the level-k figure. No payoff matrices or 2×2 games remain in this chapter. Optional cognitive-hierarchy evidence, auction examples, and market institutions are retained.
- **24, Coordination and Focal Points:** Introduces players, actions, strategies, information, timing, and payoffs through the meeting example, then explicitly teaches row/column reading, payoff order, best responses, and pure/mixed equilibrium. It proceeds to focal points, strategic uncertainty, stag hunt, conventions, distribution, and credible coordination. The price-war matrix is an optional research lens. The departmental example and Practice Lab connect the formal tools to decisions.
- **25, Cooperation and Social Preferences:** The opening distinguishes reassurance in a stag hunt from the remaining incentive to withhold help in a Prisoner's Dilemma. Subsequent analysis distinguishes future incentives, reputation, institutions, and social preferences; error repair and population-level explanations remain.

The meeting, equilibrium-boundary, and price-war tables moved from 23 to 24 with their IDs preserved. The redundant departmental matrix-figure invocation in 24 was removed because the introductory meeting matrix and subsequent application now teach its content. Its original asset remains on disk, and its old anchor leads to the application paragraph. The level-k figure moved later within 23. This revision did not redraw figure assets.

## Evidence and quotation

All 53 distinct works in the pre-follow-up Chapters 23–25 remain in their combined references. Rao (2000) moves with the price-war discussion; Nash (1950) is also listed locally in 24. Local reference lists remain alphabetical. The master bibliography contains 912 unique works. The only master-entry formatting change during this follow-up is journal italics for Rao; no work was removed.

Chapter 24's new epigraph begins “People can often concert their intentions or expectations with others…” and comes from Schelling, The Strategy of Conflict (1960), printed p. 57. The exact 23-word sentence was checked against the primary book text: https://www.sackett.net/Strategy-of-Conflict.pdf and https://dokumen.pub/the-strategy-of-conflict-0674840313.html. The quotation distinguishes mutual anticipation from merely choosing what one privately likes.

The verified game rules and numerical examples are retained. In particular, the real-number guessing game specifies at least three players and shared prizes for ties; the 33–22–15 ladder is approximate rather than an exact finite-group best-response calculation. Cognitive-hierarchy sample counts and fitted parameters retain their limits. Chapter 24 retains the distinction between implied coordination rates and realized pairs, the stag-hunt utility assumptions and 8/13 threshold, and the minimum-effort result. Chapter 25 retains the repeated-game sustainability calculation and the distinction between equilibrium support and actual behavior.

## Integrating ethical considerations

Standalone ethics sections were removed from 23–25 and 13 additional canonical chapter sources: 12, 16, 17, 18, 19 (Intertemporal Decision Making), 20 (Mental Accounting), 29, 30, 32, 35, 38, 40, and 41. These are filename prefixes; published Chapters 19 and 20 are reversed relative to those filenames.

Relevant information about costs to outsiders, consent, truthfulness, exclusion, fairness, privacy, and the ability to challenge or leave an arrangement is integrated beside the applicable examples. Repeated generic summaries are condensed. The framing and choice-architecture audit tables are retained. Research ethics and the portable Ethical Audit remain substantive topics in their appropriate places. No standalone ethics heading remains in the configured main chapters; old heading anchors remain as spans.

An independent review checked the integrations. The portfolio discussion now identifies whose returns and losses enter the calculation, and Chapter 40's audit transition now refers to inspecting facts and options along the actual user path. All reference blocks in the additional chapters and Chapter 25 remain byte-identical to their pre-follow-up versions; numeric tokens and working IDs are retained. Chapter 38's tbl-34-1 is an existing legacy span, not an actual table missing a discussion.

## Verification

- Full HTML and EPUB builds succeeded; the canonical EPUB was copied to docs.
- Book QA: 0 errors, 0 warnings. EPUB release QA: 0 errors.
- Reference synchronization passed with 912 unique works; the 53-work preservation comparison and alphabetical local lists passed.
- Source, HTML, and extracted EPUB float-reference checks passed: 62 sources, 116 figures, 148 tables, 0 issues.
- A separate canonical-source scan found no stale links to the moved Chapter 23 sections and no description claiming that 23 teaches matrices or contains the loved-one reunion.
- Headless Chromium checked all three chapters at 1440px and 390px in HTML and extracted EPUB: no page overflow, unresolved references, or missing images. Representative openings, the meeting and price-war matrices, the Prisoner's Dilemma, and the relocated level-k figure were visually inspected. Existing intentionally scrollable wide figures are not claimed to have been redesigned for phones.
- Generated-file permissions were restored after the builds. git diff --check passed. Source and release hashes are in structure-verification-inputs.json.

All edits remain local and uncommitted. Earlier uncommitted changes are preserved.
