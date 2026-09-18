# Internal models and bodily prediction — 18 September 2026

## Scope and sources

Chapter 4 adds a two-tone recognition exercise, anticipatory thirst regulation, and the author's supplied toilet-cue anecdote. Chapter 5 adds the requested post-deadline illness example and a cross-reference to Chapter 4. Existing edits to Figure 4.1 are preserved.

| Claim | Verified primary source | Boundary retained in the text |
| --- | --- | --- |
| A grayscale cue can improve subsequent recognition of a degraded image | Dolan et al. (1997), https://doi.org/10.1038/39309 | The generated pair is an illustration; no recognition rate is claimed for it. It does not uniquely establish predictive-processing theory. |
| Human thirst can fall within minutes of intake, with effects depending on volume | Williams et al. (1989), https://doi.org/10.1152/ajpregu.1989.257.4.R762 | Small experiment, six volunteers; no universal immediate disappearance of thirst or claim that hydration is already complete. |
| Drinking rapidly suppresses thirst-related neural activity before blood measures recover | Zimmerman et al. (2016), https://doi.org/10.1038/nature18950 | Mouse experiments explicitly identified as such. |
| Gut signals about ingested fluid help control continued thirst satiation | Zimmerman et al. (2019), https://doi.org/10.1038/s41586-019-1066-x | Anticipatory physiological regulation is distinguished from a conscious forecast. |
| Personalized situational cues can alter bladder sensation and activity | Clarkson et al. (2020), https://doi.org/10.1002/nau.24524 | Twelve women with situational urgency incontinence; not generalized as the established mechanism of the author's anecdote. |
| Some people report illness during weekends or vacations following work | Vingerhoets et al. (2002), https://doi.org/10.1159/000065992 | Exploratory self-report evidence; no proof that expectation causes infection or that illness is postponed by responsibility. Alternatives are framed as hypotheses. |

The 2022 neuroimaging cue paper was examined during research but is not used as the main evidence: its full-text search record reports that neural differences did not survive correction for multiple comparisons. The earlier controlled cue study directly supports the narrower claim used here.

## Figure provenance

Built-in image generation was used, with an original grayscale scene followed by an image edit. The selected two-tone image is a generative tonal simplification, not a reproducible pixelwise threshold operation; this limitation is disclosed in the chapter footnote. The important invariant in the teaching exercise is that the first image remains identical when the reader returns to it. The pair has not been behaviorally validated.

- Source scene: `figures/recognition-grayscale-reveal.png`, copied unchanged from `exec-2eeef2be-b901-4fc4-81c8-67004913d27d.png`.
- Selected simplification: `figures/recognition-two-tone.png`, copied unchanged from `exec-9bf62e41-6d70-4e1a-ba17-59ece231ae7d.png`.
- An earlier simplification, `exec-bf7fa51d-5ac5-475c-8133-6aad469aca15.png`, was rejected because its continuous outer contour made the subject too obvious.
- Supplied reference screenshots were not modified or inserted in the book.

### Final source prompt

Use case: scientific-educational. Asset type: original grayscale source illustration for a textbook recognition demonstration. Create a photorealistic grayscale photograph of a Dalmatian dog resting in dappled shade, its head seen in three-quarter profile facing left, nose near the center-left, head occupying the upper right, shoulder and curled body filling the lower half. Close crop, 3:2 landscape. The dog is unmistakable when continuous gray shading is present. Its black spots, dark ear, eye and nose should be irregular natural shapes. Behind it are soft irregular patches of dark foliage and light ground; the illumination and background should break up the outline, without a continuous silhouette around the dog. This image will be shown after an ambiguous black/white rendition to let readers recognize how patches organize into a dog. Favor 25–45 broad spots and shadows over fine speckle. Natural anatomy and photographic texture, no collar, no people, no text, no border, no watermark. Entire image neutral grayscale, no color. Make a new composition, not a copy of any known photograph.

### Selected two-tone edit prompt

Use case: scientific-educational. Edit target: the attached grayscale Dalmatian scene. Create a genuinely ambiguous Mooney-style two-tone version by removing intermediate gray tones. Keep ONLY the DARKEST areas black (imagine a low cutoff near 55 out of 255); almost ALL midgray areas and white fur become PURE WHITE. In particular the gray background to the LEFT of the face and around the nose becomes WHITE so that the face outline DISAPPEARS into the surrounding white. The narrow dark upper background and black ear may join as one black field. Do not preserve the continuous outline of the head or body. Preserve recognizable LANDMARK POSITIONS exactly: eye patch, nose patch, ear, coat spots, neck patches in the same places as the source. Eye and nose are irregular black patches, without small highlights or detail. Flatten fur detail to smooth broad solid blobs; no tiny speckle, no shading, no hatching. It should look like disconnected black islands on a mostly white field plus some dark regions at top/right; no outlined dog silhouette. This is a perceptual-learning puzzle intended to be hard to recognize BEFORE the viewer sees the grayscale source. Keep the exact composition, crop and proportions of the source. No new objects, no text, no border. Landscape 3:2.

## Verification

Status: REVISED and verified within the limits below.

- Full HTML build completed, followed by a full EPUB build and a final EPUB rebuild for the reveal page break. The master bibliography contains 980 unique entries and passes synchronization checks.
- Book QA: zero errors and zero warnings. Final EPUB QA: zero errors. `git diff --check` passes. Both new interchapter links have explicit target anchors.
- Both images are 1536 × 1024 PNGs. Source, generated HTML and final EPUB copies are byte-identical. Two-tone SHA-256: `e5a46b7a2c0c5c51422f81a744e5380c3072b1d47ee9418143496b41ff4a1163`; grayscale SHA-256: `b59049ac8a4d055916a8c6cc50a0d38b1d64e524efa3f7a7ce5bf87a0ca55039`.
- Inspected both images in HTML at 1280 × 720 and 390 × 844. Verified the reveal is initially collapsed, opens to Figure 4.3, and closes so the reader can return to unchanged Figure 4.2. Phone image widths are approximately 331 px and 309 px, without horizontal image scrolling. Reviewed the rendered thirst section and Chapter 5 illness passage.
- Inspected both images in the extracted EPUB chapter at 768 × 1024 and 390 × 844. Phone image widths are approximately 374 px and 354 px. These checks used a byte-identical HTML copy of extracted XHTML with packaged CSS/assets in a browser, not a dedicated EPUB application.
- Added a targeted EPUB page break before `#recognition-reveal` and verified both modern and legacy page-break declarations in the final package. Paginated reader behavior was not directly tested; continuous-scrolling readers can still show both images, so the text instructs readers to avoid the reveal until ready and to cover it afterward.
- The full HTML build produced attribute-order-only changes in chapters 8 and 37. Confirmed equivalence with an HTML event comparison and restored their original attribute order. The HTML version date advances to 18 September 2026.
