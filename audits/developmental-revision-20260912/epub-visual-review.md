# Bounded EPUB visual review

Date: 12 September 2026.

**Result:** all twelve supplied captures of the six assigned figures passed this visual check. No substantive clipping, text-containment, arrow-attachment, caption-placement, or caption-meaning issue was found.

## Actual scope

Applied the `diagram-figure-quality` skill to individual captures in `/private/tmp/decision-book-developmental-epub-qa`. Each image was opened and inspected individually at its original pixel resolution. The two sizes are the supplied 768-pixel viewport and mobile render, with the cropped figure-and-caption image dimensions listed below.

These are **Chromium renders of extracted EPUB XHTML**, not screenshots from native Apple Books or another dedicated EPUB reader. The review covers the six specified figures and their visible captions; it does not establish that every figure in the book has been visually inspected, or that pagination, fonts, or SVG behavior will be identical in all reading systems. Package/link validation and all-placement geometry checks belong to the separate integration pass.

The integrating agent identified these captures as using the current graphic/style versions, with the final EPUB refresh changing an evidence link rather than these figures. No source, SVG, CSS, or EPUB package was changed during this visual check.

## Figure ledger

| Capture stem | Desktop crop | Mobile crop | Disposition and observed details |
| --- | --- | --- | --- |
| `epub-normative-decision-loop` | 752 × 1198 px | 374 × 650 px | **PASS.** Heading, five functional boxes, judgment enclosure, and feedback label remain readable. Downward arrowheads meet their boxes; the return arrow enters the judgment boundary without overlapping a label. The figure explicitly presents an analytical benchmark and allows actual judgment to move back and forth. The caption is left-aligned below the figure, fits its width, and describes those relations. |
| `epub-behavioral-decision-loop` | 752 × 1284 px | 374 × 700 px | **PASS.** The denser layout remains legible at mobile width, including the internal-state examples and the reciprocal links within judgment. Arrowheads and visible shafts remain distinguishable; connectors terminate at the intended boxes or enclosure. The long feedback route is contained within the image and points back to internal state. The caption describes interacting functions and model updating, consistent with the diagram's warning against reading it as a fixed mental sequence. |
| `epub-habit-formation` | 752 × 961 px | 374 × 532 px | **PASS.** Both axes, the plateau label, schematic curve, and numerical summary are readable and unclipped. No arrowheads are required in this chart. The image labels the curve illustrative; the caption identifies modeled time to 95% of the plateau, the 18–254-day range, median 66 days, and well-fitted cases. It does not convert the median into a universal deadline. |
| `epub-urge-wave-observation` | 733 × 986 px | 355 × 503 px | **PASS.** The axis labels and rounded curve fit, and the observation-practice text stays inside its box with padding. At the narrower crop, the final instruction wraps onto a second line without clipping. The title, warning that urges can persist or return, and caption all identify a possible schematic pattern rather than a guaranteed timetable. |
| `epub-digital-arrow` | 752 × 1175 px | 374 × 663 px | **PASS.** Both hotel panels, the separate bundled-redesign stage, connector arrows, and button cue remain clear. Text does not collide with the button. The visible evidence qualification and caption state that the bundle does not isolate the arrow's effect or establish better choices. The caption also identifies the advertisements as illustrative rather than the original test stimuli. |
| `epub-figure-13-2` | 752 × 1070 px | 374 × 569 px | **PASS.** This is the processing-ease figure, “When ease becomes evidence.” The four vertically arranged boxes and connecting arrows remain readable and aligned. The dashed route to the inference check is visually distinct. “Possible sources” and “Possible judgments,” together with the evidence-check questions, avoid presenting fluent processing as validation. The caption describes the same possible effects. |

For each stem, the exact files inspected were `<stem>.png` and `<stem>-mobile.png`; the final pair is indeed `epub-figure-13-2.png` and `epub-figure-13-2-mobile.png`.

## Limits of the pass

Type readability was judged from the supplied original-resolution captures, not inferred solely from SVG font-size attributes. Small arrowheads in the denser mobile decision diagram remain visible, but native-reader testing and any reader-specific minimum-font settings were outside this pass. The study numbers were checked here for agreement between diagram and caption; this was not a new primary-source audit of those studies.

No corrective action was requested for these twelve captures. `git diff --check` passed for this audit note.
