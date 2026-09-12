# Integration corrections

These notes resolve findings raised during independent checks. The reviewers' earlier reports remain records of the snapshots they inspected.

- Appendix F propagation: added “mainly involving hypothetical choices” to Chapter 2's opportunity-cost meta-analysis sentence.
- Prediction exercises: Chapter 10 now tells the reader to see the initial puzzle, pause, record a rule and discriminating test, then continue. Chapter 26's general application remains but is no longer labeled “Predict first.” Five correctly sequenced prediction callouts retain the label.
- Captions: Chapter 34 describes three cards rather than a branching diagram. Chapter 40 identifies the generic hotel advertisements as illustrations rather than original test stimuli and retains the bundled-intervention boundary.
- Legacy links: preserved the removed Chapter 38 table's `tbl-34-1` anchor at its replacement pointer, as already done for Chapter 6's consolidated table.
- Figures: communication-calibration arrows reach the destination boxes. New conceptual-diagram markers were reduced from 12 to 8 source units for a 3-unit stroke. The digital redesign description has a visible box and connected boundary endpoints.
- Mobile rendering: removed the 92% and 90% figure-container reductions in the habit-formation and conversation-needs figures. Increased the urge figure's body/axis type to 30 source units and wrapped the final observation prompt; raised the heuristic-substitution footer to 28. The independent check measures actual contained-image scaling, including desktop max-height constraints.
- Tool styles: strengthened selector specificity so the three level colors and prediction cue survive Quarto's default callout rules. The level names remain explicit text, not color-only coding. Applied corresponding reading cues and the compact figure class to EPUB styling.
- Reference hygiene: merged the enriched Tversky–Kahneman 1981 citation across Chapters 12, 17, and 20. Changed sorting to compare author-name sequences rather than punctuation-bearing strings; independent audit confirms the habit chapter and all other lists.
- Cross-format chapter entry links: source-level chapter-title fragments can disappear from HTML because Quarto removes the title heading from the body. Some bare-file links also remained unresolved in EPUB. Each chapter now has a stable `chapter-NN-start` ID on its existing epigraph block; affected title links and bare chapter pointers target these IDs. No visible text was added by this correction.
- QA maintenance: updated the rendered-image inventory from a stale 117 to the source-supported 118 placements (116 Markdown images, one raw HTML GIF, and Quarto's preface cover). Updated two literal-phrase assertions to match the revised, scientifically equivalent captions. These were distinct from the real link, font, and connector failures, which were corrected in the book itself.

The EPUB edition metadata was advanced to `2026.09.12`; its stable publication identifier is preserved. Final browser and package results are recorded separately in `VERIFICATION.md`.
