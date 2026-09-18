# Chapter 4: structure and delayed recognition reveal

**Current image choice:** The user subsequently preferred the earlier black-and-white illustration. It has been restored byte-for-byte, with its original provenance footnote. The revised chapter structure and final reveal are retained. Exact-conversion records below document the superseded variant.

## Scope

The request named Chapter 20, but its topic, figure numbers 4.2/4.3, and the displayed chapter identify Chapter 4, *The Predictive Mind*. This interpretation was stated before editing. Chapter 20 was not changed in this revision.

## Editorial sequence

1. Inspect the ambiguous two-tone image and record an interpretation.
2. Explain internal models, prior knowledge, and context using the unresolved image and a dim kitchen.
3. Show context selecting interpretations: B/13, duck/rabbit, equal measurable targets, familiar color, and hollow faces.
4. Explain learning through the restored-sight case.
5. Distinguish perceptual prediction from decision forecasts, then explain error and precision.
6. Extend the account to thirst and learned bodily cues.
7. Discuss model correction, the optional AI analogy, and practice.
8. Give references, then finish with the grayscale reveal and a return to the unchanged opening image.

All 40 chapter reference entries and all existing cross-reference anchors were preserved. The revised explanation treats internal models as learned relationships and expectations, without claiming that contexts retrieve literal complete pictures stored in the brain. Clark (2013) and Dolan et al. (1997), already cited in the chapter, were checked against primary-source records. Different context effects are not asserted to have one established neural mechanism.

The reveal is now an ordinary final section, not a collapsed callout. HTML print CSS and EPUB CSS request a new page before `recognition-reveal`. Figure numbering is generated from the new sequence, so the former Figures 4.2/4.3 no longer keep those numbers.

## Image provenance finding and completed replacement

The existing two-tone asset is a separate AI simplification of the grayscale illustration, not a pixelwise threshold conversion. Both are 1536 by 1024. Read-only comparison against global luminance thresholds found that even the best matching threshold (70) leaves approximately 12.11% of pixels different from the existing asset. This supports the user's concern about altered details. The source footnote already disclosed this distinction.

After the user explicitly selected exact pixel conversion, `scripts/build_recognition_two_tone.py` was used to replace the opening asset. The final threshold is 30: Pillow L luminance below 30 becomes black, otherwise white. All 1,572,864 pixels were checked against this rule with zero mismatches. Source size (1536 by 1024), coordinates, and the grayscale source file are unchanged. The old AI redraw is preserved under `audits/ch04-exact-pixel-conversion-20260918/previous-ai-redraw.png`.

Twelve thresholds spanning 20 to 230 were visually compared. Threshold 30 reduces continuous contours and dark regions while retaining fragments that can be matched after the reveal. Its black fraction is 6.84%. This is an editorial choice, not an experimentally established optimum. The chapter's image description and provenance footnote now reflect the exact conversion. Reproduction metadata and verification are recorded in `audits/ch04-exact-pixel-conversion-20260918/conversion.json`.

Recognition difficulty has not been measured in readers. Neither the existing image nor a possible replacement should be described as having a validated recognition rate.

## Verification

- Source: all existing anchors preserved and all 40 reference entries unchanged.
- Full HTML render, final Chapter 4 HTML render, and final EPUB render completed successfully.
- Chapter 4 structural checks passed: opening image is first, reveal is the last substantive section, the grayscale image appears once, both figures have local prose links, and the subject is not named before the reveal. Ordinary endnotes follow the final section.
- Final EPUB package QA passed with zero errors. Both packaged image files match the canonical source assets by hash, and the EPUB includes `break-before: page` for the reveal.
- Visually inspected the opening and reveal in HTML at 1280 and 390 pixel viewports, and in the extracted EPUB chapter at 768 and 390 pixel widths. Images retain proportions, captions fit, and no horizontal overflow was detected at the narrow width. The EPUB inspection used a browser rendering of a byte-identical HTML copy of the packaged XHTML and its packaged CSS; this does not validate native-reader pagination.
- HTML figure sequence is 4.1 (opening), 4.2 (B/13), 4.3 (duck/rabbit), 4.4 (equal targets), 4.5 (traffic light), 4.6 (hollow-face animation), 4.7 (predictive processing), 4.8 (reveal). EPUB omits the animated figure and numbers its final reveal 4.7.
- The earlier structure check reported 12 unresolved citations in concurrently edited Chapters 35–38, with no Chapter 4 issue. Those unrelated edits were preserved. After the concurrent task finished its rebuild, the exact-conversion follow-up passed whole-book QA with zero errors and zero warnings.
- `git diff --check` passed.
- Native EPUB pagination and a physical print proof: not inspected.

## Exact-conversion follow-up verification

- User selected exact pixel conversion; the image replacement is complete.
- All 1,572,864 pixels satisfy the threshold-30 rule with zero mismatches; the source hash is unchanged. A second script execution produced a byte-identical PNG.
- Inspected the corrected figure in HTML at 1280 and 390 pixels and in the packaged EPUB chapter at 768 and 390 pixels. Both keep the image's proportions and caption, with no horizontal overflow at narrow widths.
- The EPUB build and package QA passed, and its image bytes match the canonical corrected PNG. The new provenance note is present and the reveal remains the final substantive section.
- A concurrent full HTML build temporarily removed the shared `docs/` output after the first package QA passed. After that build completed, final whole-book QA passed with zero errors and zero warnings, EPUB package QA passed with zero errors, and `git diff --check` passed. Final HTML and released EPUB both contain the verified exact image bytes, corrected provenance, and the delayed reveal.

## User-requested restoration

The user preferred the earlier black-and-white image. Restored its saved PNG byte-for-byte in the source, rebuilt HTML and EPUB, and verified matching image bytes in both outputs. Restored the earlier alternative text and the footnote explaining that the images are corresponding generated illustrations rather than a pixelwise conversion. The revised chapter structure and end reveal remain in place. The superseded threshold-30 image is retained in the conversion audit directory. Both whole-book QA and EPUB package QA passed after the restoration.
