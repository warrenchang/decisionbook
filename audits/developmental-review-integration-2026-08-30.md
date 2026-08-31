# Developmental-review integration audit

Date: 30 August 2026

Source reviewed: `Decision_in_the_Making_developmental_review.md`

## Scope and decision rule

The review was treated as editorial evidence rather than as an instruction set. Suggestions for Chapters 1 and 2 were excluded at the author's request. A suggestion was adopted when it clarified the book's causal spine, reduced duplicated teaching, improved the separation of core and advanced material, strengthened an evidence boundary, or repaired production quality without contradicting an already approved authorial decision.

## Adopted across the book

- Made the long-form journey explicit: **Choice within a mind → Influence across minds → Agreement between interdependent minds → Designing better loops**.
- Retained one canonical decision loop and added stable definitions of interpretation, prediction, expectation, and valuation.
- Clarified the reading layers: Core Narrative, Research Lens, Applied Module, Practice Lab, Evidence Boundary, and optional Research Companion.
- Standardized evidence boundaries around **Claim → Boundary → Alternative → Update**.
- Added a recurring six-question ethical audit to the reading guide and portable tools.
- Added a recurring-case map so hiring, supplier, conversation, negotiation, and choice-path cases accumulate rather than restart.
- Added publication, version, subject, rights, accessibility, and stable-identifier metadata for the EPUB workflow.
- Strengthened package QA to check EPUB metadata, internal links and fragments, and image alternative text.
- Added a complete, reproducible simulated study to Appendix C, including question, preregistered design, estimand, code, generated result, bounded interpretation, and preservation record.
- Removed course-platform word-limit artifacts from the canonical chapters and research appendices in scope.
- Reconciled Appendix B after consolidation: removed stale example ownership, assigned each retained video a primary conceptual owner, and made optional video lessons recoverable without the original clip.

## Adopted in Chapters 3–15

- Kept attention at the beginning of the decision process and reduced secondary detours.
- Distinguished sensory prediction in predictive-processing theories from predictive judgment about future consequences.
- Rebuilt the expectations chapter so an ordinary, testable forecast precedes the special case in which an expectation changes its own outcome.
- Placed that consequence-forecast chapter before valuation, so Part I now follows **Notice and interpret → Construct options → Predict → Value → Choose and act → Learn** without a chapter-order contradiction. Chapter 5 and Chapter 6 source/output names were updated, with aliases retained for their former URLs.
- Reduced repeated affect, availability, belief-protection, and calibration explanations.
- Assigned overconfidence, the outside view, planning fallacy, regression, and calibration to Chapter 15 as their primary home.
- Expanded the worked Bayesian instruction while keeping puzzles subordinate to natural-frequency reasoning.

## Adopted in Chapters 16–29

- Separated core risk and prospect-theory models from advanced elicitation, neuroscience, and related-but-not-entailed phenomena.
- Kept decisions from experience centered on the encountered distribution and sampling policy.
- Simplified intertemporal choice and mental accounting around their recurring diagnostic tools.
- Marked clinical addiction material and evolutionary or spatial game models as advanced Research Lenses.
- Reorganized cooperation into mechanisms that sustain cooperation and preferences that shape social value.
- Gave social norms and conformity a clear primary home before markets, authority and groupthink, and culture and identity.
- Marked markets, mispricing, and bubbles as an Applied Module while preserving its strategic and social role.
- Preserved well-being as the bridge from predicted value to experienced, remembered, evaluated, relational, and meaningful outcomes.

## Adopted in Chapters 30–41

- Sharpened the progression from persuasion to story, evidence-aligned message, communication, connection, and repair.
- Distinguished craft sources from causal evidence and bounded neuroscience claims about narrative.
- Reduced negotiation duplication and clarified the sequence: map the joint decision, prepare and claim value, create value, then design an implementable agreement.
- Moved mediation, arbitration, and related specialist processes into a Research Lens rather than allowing them to interrupt the core negotiation path.
- Clarified the division of labor among behavior design, choice architecture, and decision hygiene.
- Condensed AI material into an accountable-decision Research Lens that keeps prediction, valuation, intervention choice, and responsibility separate.

## Adapted rather than adopted literally

- The seven-part structure was retained. The review's three large movements were added above it without global renumbering. The one sequence correction—forecasting before valuation—was confined to Chapters 5 and 6 and protected by URL aliases.
- The canonical loop retains the author's approved combined **choose, commit, and act** function and separate prediction and valuation functions. The loop is presented as recursive rather than a validated universal stage order.
- Specialized content was layered in place rather than removed wholesale or moved to a separate product. This preserves scientific depth while letting a first-time reader follow the core narrative.
- Chapter 25 remains one chapter with two visible movements rather than being split and renumbered.
- Markets and bubbles remain in the strategic and social part as an optional applied synthesis rather than being removed from the book.
- Chapter 35 remains a deliberately short gateway; the substance resides in Chapters 36–38 rather than being repeated.

## Deferred or rejected

- No Chapter 1 or Chapter 2 changes were made from this developmental review.
- The author-approved preface was not shortened or structurally replaced.
- The author's dual Aalborg University Business School and University of Southern Denmark affiliation was preserved.
- A full migration from chapter-level reference lists to a different citation architecture was deferred. The current design keeps local traceability and a synchronized master union; a partial migration would create more inconsistency than it removes.
- Chapter splits and global renumbering that would break established course mappings and links were not adopted where layering or cross-reference changes solved the underlying problem.
- The review's package findings were treated as a dated snapshot. Current sources are re-audited after rendering rather than assuming that reported broken links, empty headings, or missing captions still exist.

## Verification completed

- Regenerated the synchronized master reference union and rendered the complete HTML and EPUB editions on 30 August 2026.
- Source/book QA: **PASS**, with 0 errors and 0 warnings.
- EPUB package QA: **PASS**, including ZIP integrity, compact Part-to-Chapter navigation, all internal links and fragments, chapter numbering, tables, metadata, MathML, alternative text, and required-content checks.
- Connector geometry QA: **PASS** for 105 reader-facing figures.
- Rendered HTML QA: **PASS** for 113 figure placements at 1,440-pixel desktop and 390-pixel phone widths, with no loading, containment, caption, or horizontal-overflow issues.
- Rendered EPUB QA: **PASS** for 112 figure placements at 768-pixel tablet and 390-pixel phone widths, with no broken images or horizontal-overflow issues. Long inline mathematics and code blocks use bounded horizontal scrolling when a reader viewport is narrower than the content.
- `git diff --check`: **PASS**.

These checks validate the generated artifacts in Chromium at the tested widths; they do not establish identical rendering in every EPUB application.
