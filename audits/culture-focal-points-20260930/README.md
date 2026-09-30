# Culture, focal points, and the elevator photograph — 30 September 2026

## Scope and provenance

- Added the user-supplied photograph unchanged to Chapter 29's existing hotel-number anecdote. Caption and alternative text describe visible numbering; no hotel, location, date, photographer, or explanation of management's intent was inferred.
- Source: `/var/folders/wb/4y_xzcwn6yv3xkmnrynw_hqm0000gp/T/codex-clipboard-1c3e2b3d-625d-4e81-8852-520c6388e4a9.png`.
- Book asset: `figures/hotel-elevator-numbering-photo.png`; original dimensions 193 × 288 pixels. SHA-256: `72177539d6bb852ed5489ba3946ae58ac6c7e1a1d85da4750aae3cedc945eb6f`. No image generation, sharpening, or alteration of the numbers. The source's limited resolution remains visible when enlarged.
- The visible panel includes 14 and omits 13. The wider first-person observation about 4, 13, and 14 remains separate from what this particular photograph shows.
- Added reciprocal Chapter 24/29 links. Chapter 29 distinguishes preference for or avoidance of a number from coordination through mutually anticipated salience; its number-matching scenario is hypothetical. Chapter 24 retains the main explanation of focality and adds the empirical comparison below.

## Source check

Jackson, M. O., & Xing, Y. (2014). Culture-dependent strategies in coordination games. *PNAS, 111*(Suppl. 3), 10889–10896. https://doi.org/10.1073/pnas.1400826111

Primary source: https://web.stanford.edu/~jacksonm/Jackson-Xing-CultureAndCoordination-PNAS-2014.pdf

Checked the published Methods, Fig. 2, and Discussion. The book describes the matching payoffs and residence-associated choice differences. Residence was measured; the account does not identify a causal cultural mechanism or claim national representativeness. No realized equilibrium is inferred merely from an individual's color choice.

## Verification

- Full HTML and EPUB builds completed. After correcting the initial oversized photo, regenerated Chapter 29 HTML; regenerated the example index after arranging its new rows in chapter order.
- HTML source/link/citation QA: 0 errors, 0 warnings. Master references synchronized at 1,267 entries. EPUB release QA: 0 errors. Practice QA passed for 280 questions and 49 sets.
- Figure/table coverage: 69 sources, 108 figures, 169 tables, 0 issues; see `float-reference-qa.json`.
- Photo bytes match the supplied source, HTML asset, and EPUB-embedded image. EPUB caption, alternative text, 280-pixel sizing rule, and unique figure/section anchors verified.
- Browser navigation followed Chapter 29 → Chapter 24 → Chapter 29 successfully. Temporary viewport changes were reset and the preview tab closed.
- Restored the existing executable mode on `docs/parts/part-1.html` after rendering. No commit or push.

| Figure | HTML desktop (1280 × 720) | HTML narrow (390 × 844) | EPUB |
| --- | --- | --- | --- |
| 29.2, elevator numbering | PASS after size correction; image 280 × 417 CSS pixels, caption visible, numbering legible within the supplied resolution | PASS for width/containment and caption wrapping; same 280-pixel width | Structural/image checks PASS. Direct visual preview of extracted XHTML was blocked by the in-app browser; no claim of native EPUB-reader visual verification. |

## Follow-up: preserve native photo size

The user subsequently reported blur relative to the original. The replacement upload (`codex-clipboard-3c281449-589f-4125-81a2-268ceeb351cc.png`) has the same SHA-256 as the original and book asset. The earlier 280-pixel display still enlarged a 193-pixel-wide source. Changed the chapter's width attribute and inline style, and the EPUB's figure-specific CSS, to 193 pixels. No image pixels were modified.

The regenerated HTML was visually inspected at desktop and 390 × 844 narrow viewport sizes. In both cases the image element measured 193 × 287 CSS pixels including the theme's border, with intrinsic dimensions 193 × 288. The photograph and caption fit without horizontal clipping; the image is no longer enlarged. The viewport was reset and the temporary tab closed. Source QA passed with 0 errors and 0 warnings. This follow-up supersedes the 280-pixel sizing assessment above.

The EPUB rebuild completed and release QA passed with 0 errors. The packaged figure has a 193-pixel width attribute, inline style, and scoped CSS rule. Both the HTML image asset and EPUB-embedded image match the original bytes. EPUB verification remains structural rather than native-reader visual verification.
