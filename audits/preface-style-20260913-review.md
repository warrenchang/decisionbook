# Revision using the preface as the writing standard

Date: 13 September 2026

Baseline: `ae477ccab98e4c8012240a28ec3699d4f21080e2`

## Scope and editorial standard

Reviewed the 61 sources included in the published book: the preface and two reading guides, seven part introductions, all 42 chapters, six appendices, the reference list, concept index, and About page. Revised 59 source files. The accepted preface remains the calibration example and is unchanged; the consolidated reference list is also unchanged. Historical chapters and unused part pages were excluded from the publication pass.

The revision follows the user's preface feedback: make the decision and its stakes visible; establish what each sentence refers to; let a question create the need for a concept; connect explanation, evidence, and practical use; and vary sentence length without turning the prose into a succession of short declarations. A paragraph that already served these purposes was retained.

The local `huanren-writing-style` skill now contains a reusable section on narrative coherence. A linked `references/decision-book.md` records the book-specific decisions about the preface, the decision map, connection and negotiation, terminology, titles, figures, and publication checks. The general skill keeps these project conventions separate from instructions for unrelated writing. Skill validation passed.

## What changed

- **Openings and transitions:** Concrete situations now lead more clearly into the chapter's question. Later sections explain why the next distinction matters to that situation instead of introducing another list of terms.
- **Explanations:** Clarified ambiguous pronouns, implied comparisons, premature technical language, and repeated definitions. Retained technical vocabulary where the chapter develops and uses it.
- **Evidence and application:** Distinguished reported findings from hypothetical examples and proposed interventions. A successful story, changed choice, or later outcome does not by itself establish the mechanism that produced it.
- **Practical work:** Exercises now specify an intelligible comparison or next action. For example, one forecast outcome cannot diagnose calibration; a relevant emotion need not change an objective consequence; and already-spent money is not necessarily unrecoverable.
- **Connections across topics:** Strengthened the progression from individual judgment to shared information, communication, conflict, value creation, agreement design, and later evaluation. The hiring case and decision map are used where they help, rather than inserted mechanically everywhere.
- **Part introductions and appendices:** Clarified the reading route and the purpose of each tool. Reduced duplicated interpretation in the simulated-study appendix while retaining the result itself, its uncertainty, and its limitations.

## Chapter-level records

Each chapter editor read the complete assigned chapters, including optional material, tables, captions, alt text, exercises, closings, and references. A different editor then reviewed the changes and relevant context for introduced scientific or logical errors.

- [Chapters 1–14](preface-style-20260913-ch01-14.md)
- [Chapters 15–28](preface-style-20260913-ch15-28.md)
- [Chapters 29–42](preface-style-20260913-ch29-42.md)

The independent integration review corrected the cue-audit distinction in Chapter 6, the monetary-outcome condition and acquisition-utility/sunk-cost distinctions in Appendix C, and the historical meaning of exaptation in Appendix B. Chapter 9's figure alt text now describes combining a prior with the comparative likelihood of evidence, avoiding an unintended statistical-independence claim. Chapter 31's reference to the comment Sara receives was checked against the opening scene.

## Illustrations

Reviewed the title, description, and text of all 109 SVGs referenced by the configured sources. Reviewed ten contact sheets of the configured figure assets for broad composition, and inspected all five edited figures at full size. Contact sheets do not certify small-text legibility or exact connector geometry.

Five SVGs and their PNG companions were updated:

| Figure | Revision |
|---|---|
| `communication-grounding` | Checking and repair seek sufficient understanding and invite another check; they do not guarantee it. Updated the corresponding caption and generator text. |
| `cooperation-architecture` | Ask readers to test relevant supports and their failure conditions instead of promising that the architecture works. |
| `norm-message-diagnostic` | A description of what others do can imply approval; the text no longer asserts that every norm message necessarily states both. |
| `prospect-theory-map` | Identify the curves as illustrative and the risk pattern as dependent on model parameters. |
| `story-evidence-braid` | Correct a punctuation error in the accessible description. |

Existing geometry was retained. Both older Chapter 1 SVGs and their PNG companions are byte-for-byte unchanged. The accepted decision map remains consistent with **Choose & commit**, and Chapter 21 no longer describes a separate Act node or a mandatory sequence through all functions.

## Scientific-content preservation

The [preservation manifest](preface-style-20260913-preservation.json) compares every configured source with the baseline. All original reference blocks, displayed equations, explicit IDs, and figure-path sequences are retained. The consolidated bibliography still contains **870 unique chapter-and-appendix references**, and the reference synchronization check passes.

No study or bibliography entry was removed in this pass. Where repeated exposition was condensed, the finding and its supporting reference remain. Numerical checks by the chapter editors found no deleted empirical number; deleted numerical tokens were arbitrary scene timestamps or repeated chapter-number mentions. Interpretive changes are documented in the chapter records and above.

This was a complete editorial and internal-consistency review, not a fresh independent verification of every primary source or external website. Existing uncertainty statements, evidence-status notices, and reported limitations were preserved; they should not be mistaken for a new literature search dated today.

## Build and delivery verification

| Check | Final result |
|---|---|
| Updated writing skill | Validator reports `Skill is valid!`; [file hashes](preface-style-20260913-skill.json) recorded. |
| Full HTML and EPUB builds | Completed successfully. Targeted HTML renders incorporate the final Chapter 6 and Chapter 33 integration corrections. |
| Source preservation | All 61 configured files checked against the baseline; no failed preservation check. |
| Bibliography synchronization | 870 unique references; exact chapter-and-appendix union passes. |
| Canonical book QA | Zero errors and zero warnings, including citation, source-link, figure metadata, fallback, and connector checks. See [QA report](../QA_REPORT.md). |
| EPUB release QA | Zero errors; staged and released files match; all internal content links and fragments resolve. See [EPUB report](../EPUB_QA_REPORT.md). |
| HTML navigation | 675 search targets resolve. The independent review checked 2,455 main-content links, including 2,324 local links, with no broken targets. All 42 chapter titles and single italic subtitles match source. See [navigation record](preface-style-20260913-html-navigation.json). |
| HTML display | 61 pages and 118 figure placements checked at desktop and phone widths; zero issues. See [rendered-figure record](rendered-figure-qa.json). |
| EPUB display | 63 XHTML documents and 116 figure placements checked at 768px and 390px in Chromium; zero issues. See [EPUB figure record](rendered-epub-figure-qa.json). |
| Updated figure assets | All five edited SVGs match both the HTML assets and the SVGs embedded in the released EPUB; corresponding source PNG companions were regenerated. |

The EPUB link check caught one newly added Chapter 6 forward link that had not converted from `.qmd` to an EPUB destination. Adding the existing Chapter 19 start anchor fixed it; the rebuilt release passes the complete internal-link check.

The HTML and EPUB outputs are ready for review. Changes remain local and uncommitted; nothing was pushed.
