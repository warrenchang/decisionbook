# Visual verification

All four new figures were inspected in the generated HTML at viewport widths of 390 and 1280 CSS pixels, and in extracted EPUB XHTML at 390 and 768 pixels: sixteen rendered screenshots in this folder. Inspection covered text legibility, data labels, axes, captions, clipping, overlap, and fit within the reading column.

The phone versions fit without horizontal scrolling. SVGs use explicit font fallbacks and larger labels; EPUB images are packaged PNG equivalents. Numerical values and caption interpretations were checked separately against primary sources.

`render-offline.cjs` embeds the generated document's local styles and images, disables scripts, and blocks network access before rendering it in a browser. `rendered-geometry.json` and `epub-rendered-geometry.json` record actual image widths and successful image loading. This verifies the generated HTML/XHTML layout; it does not claim testing in every commercial EPUB reader.

The final EPUB rebuild changes only the evidence guide's Chapter 40 link. The four illustrated chapter documents and their image assets are compared with the visually checked extraction in the final validation record.
