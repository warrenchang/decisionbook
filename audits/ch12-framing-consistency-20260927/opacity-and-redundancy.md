# Chapter 12: visibility and duplicate illustration

- Removed the former Figure 12.4 (`framing-view-and-context.png`) from the chapter. Retained its legacy anchor and replaced the repeated explanation with a brief reference to Figure 12.1.
- Increased imagined-surroundings opacity in Figure 12.1 from 0.36 to 0.72 in the editable SVG assembly generator. The original artwork files are unchanged.
- Updated caption, alternative text and SVG description from “pale” to “lighter.”
- Generator verification: all three 304 × 304 upper/lower framed views remain pixel-identical. A separate decoded-pixel comparison with the committed image confirms that the entire lower scene is unchanged.
- Inspected the final illustration at native size and at 390 pixels wide: city, park and rainy surroundings are more visible while the framed views remain distinct.

Both complete editions rebuilt successfully. Book QA: zero errors and warnings. EPUB QA: zero errors. Float coverage: 107 figures and 164 tables across 62 sources, zero issues. Final HTML and EPUB contain the canonical PNG exactly; Chapter 12 has Figures 12.1–12.3 only. Inspected HTML and extracted EPUB content in the browser at desktop and 390-pixel widths; native e-reader behavior was not separately tested.
