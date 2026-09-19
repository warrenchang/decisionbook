# Illustrated sensory worlds — 19 September 2026

User request: replace the former Figure 3.3 with an illustration similar to the supplied four-panel animal image.

The new `figures/sensory-worlds-illustrated.png` is a built-in image-generation output copied unchanged into the book. `provenance.json` contains the complete prompt, original output path, primary sources, and scientific checks. `user-style-reference.png` preserves the supplied reference. The original `sensory-windows-partial-world.svg` remains available for comparison.

The four panels depict infrared heat detection in a pit viper, a bee and a schematic ultraviolet floral pattern, infrasonic calls of Asian elephants, and magnetic orientation in a European robin. The bird example follows experiments on European robins rather than transferring a set of navigation cues to a particular ocean crossing. The ultraviolet image explicitly uses false colour. The two small graphs and migration-distance claim from the reference image were omitted.

Chapter 3 supplies the explanations and citations; the caption stays concise. Added primary references: Koski and Ashman (2014), and Wiltschko and Wiltschko (1972). Other relevant sources already present in the chapter were retained. The existing figure anchor `fig-sensory-windows` is reused. Because the earlier throughput figure remains removed, the new image is automatically numbered Figure 3.2.

Both output styles give labeled raster illustrations an 800 px horizontal reading pane on narrow screens. This preserves label legibility; captions and prose remain within the normal text column.

## Verification

Full HTML and EPUB builds passed. Source QA returned zero errors and warnings; the synchronized reference list contains 1,030 entries. EPUB package/navigation QA passed. Float-reference checks covered 62 sources, 96 figures, and 166 tables without issues. The restored figure occurs once at the preserved anchor and is numbered 3.2 in both outputs.

The original generated image and the figure in final HTML and EPUB were visually inspected. Browser checks at 1440/390 px (HTML) and 768/390 px (EPUB) confirmed successful loading, correct captions and alternative text, no page overflow, and a contained 800 px scrollable image on narrow screens. Both edges of the mobile reading panes were inspected. These EPUB display checks use extracted XHTML in Chromium; individual e-reader behavior can vary. `git diff --check` passed. No commit or push was performed.

## Label edit

At the user’s request, the parenthetical “(false colour)” was removed from the illustration using built-in image editing. The explanatory chapter sentence remains. See `label-edit.json` for the edit prompt and record. The revised PNG was copied to the HTML asset location and substituted for its existing image entry in the EPUB; all other EPUB entries were verified byte-identical. EPUB QA passed.
