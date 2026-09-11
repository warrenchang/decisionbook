# Figure 4.3: learned traffic-signal context

Date: 2026-09-11.

The left panel now contains only the upper lamp's lens on a uniform blue-green field. The right places that identical lens at the same scale and height within a photographic-style vertical traffic signal. Chapter 4 foregrounds the learned expectation of red at the top, adds memory-color evidence, and keeps the distinction between context mechanisms and visual appearance in a footnote.

## Illustration provenance and reconstruction

- Scene: `figures/traffic-light-context-scene.png`, newly generated with the built-in image-generation tool. The supplied slide was not reused as an image asset. The generated scene is an illustration, not a documentary photograph.
- Generation prompt: `audits/traffic-context-imagegen-20260911.txt`.
- Unedited generated PNG SHA-256: `a88a7f5b30aca4a3a4bde91f61cc3279061d9a9eaad9a647ebef6161608b58aa`.
- Editable composition: `figures/traffic-light-color-context.svg`; PNG fallback: `figures/traffic-light-color-context.png`.
- Reconstruction: run `node audits/traffic-context-compose-20260911.cjs` from the repository root, then rasterize the SVG at 1600 × 1640 pixels. The SVG embeds the original scene, so its rendering does not depend on an external image request.
- Lens crop in source coordinates: center (506, 286), radius 149. Both instances reuse the same clipped scene region after an sRGB luminance filter and identical channel transform (slope 0.8, intercept 0.22).
- SVG dimensions: 800 × 820. Lens centers: (198, 231) and (598, 231), radius 74.5. The isolated field is #3aaba8. The contextual scene has a #4bc9b9 overlay at opacity 0.50, applied before the common neutral lens is placed above it.

## Verification

- Compared 67,857 corresponding target-interior pixels: zero differences; every pixel has R = G = B. Edge antialiasing against different surroundings is excluded from this interior comparison.
- Checked 707,471 left-field pixels outside the lens and panel boundary: all equal #3aaba8.
- Inspected the photographic composition at full size and the final stronger-cast composition at 720 and 360 pixels wide. No stray frame or scene details remain in the left field; target placement, panel labels, and crop boundaries are clean.
- Independent scientific and integration review passed. That review inspected the same text and geometry with a preliminary scene-overlay opacity of 0.24. The final opacity of 0.50 was inspected separately; it does not change either target lens.
- Verified Hansen et al. (2006), Witzel et al. (2011), and Valenti and Firestone (2019) against primary publications. Existing illumination and color-constancy references were retained. The laboratory comparison explicitly identifies the unfamiliar control patches.
- Completed full HTML rendering, final Chapter 4 HTML rendering, and EPUB rendering, all with successful exit status.
- Book QA: zero errors and zero warnings. EPUB QA: zero errors. Reference synchronization: 838 unique references. Checked 61 HTML pages for local links and anchors: zero errors.
- Confirmed the revised caption, passage, footnote, and three new references in HTML and EPUB. Figure numbering remains 4.3. The EPUB embeds the final SVG byte for byte. HTML SVG, PNG, and scene copies match their canonical sources.
- Existing figure/table IDs and display mathematics in Chapter 4 are preserved. Final source hashes remained unchanged through rendering and QA. `git diff --check` passed. Existing unrelated user changes were preserved; no commit or push was performed.

Numerical results and hashes are saved in `audits/traffic-context-20260911-checks.json`. These checks establish stimulus construction and output integrity; they are not a human perceptual experiment. The figure invites readers to compare appearance rather than asserting that every viewer will see redness. The photographic scene was chosen to strengthen recognizable object and illumination cues; the relative contribution of learned identity, chromatic context, and inferred illumination is not isolated by this two-panel comparison.
