# Figure F.2: simplify sampling and assignment

14 September 2026. User requested the original branching arrangement, removal of redundant diagram text, and validity labels outside the procedure boxes.

## Revision

- Removed the visible heading, footer, and extra note beside “Not in evaluation.”
- Retained exactly seven study-flow boxes: target population; random sampling; evaluation sample; not in evaluation; random assignment; treatment group; control group.
- Moved “External validity” and “Internal validity” into unboxed side annotations. Horizontal arrows link each annotation to its corresponding procedure; they do not represent participant movement.
- Retained the original two forks. Only the evaluation sample proceeds to random assignment; people outside evaluation are not controls.
- Shortened the caption to the two distinct inferences supported. The surrounding validity discussion and every reference remain unchanged.
- Regenerated SVG and matching PNG from the edited function in `scripts/build_methods_appendix_figures.py`, without regenerating other figures.

## Verification

Independent semantic review passed. Source-size and 330-pixel browser checks found no text containment or label-attachment issues; smallest text at 330 pixels is 13.89 pixels. Diagram labels, branch destinations, and annotation positions were visually inspected.

The connector audit previously assumed every arrow had to meet a box. Its explicit free-endpoint list now records the two intentionally unboxed annotation tips. Separate browser checks verify each tip is 20 pixels before its label and aligned within its text height. Participant-flow arrows retain ordinary box-boundary checks. Source QA passes with zero errors and zero warnings.

Figure F.2 was checked in the HTML chapter at desktop and phone widths. The final EPUB passes release QA with zero errors. Figure F.2 also passes tablet (768px) and phone (390px) display checks, with correct numbering, caption placement, loaded image, and no body or figure overflow. The phone rendering was visually inspected. Destination records: `sampling-figure-cleanup-20260914-destinations.json`; source bounds: `sampling-figure-cleanup-20260914-bounds.json`. No chapter body text or existing reference was removed, and no commit or push was requested.
