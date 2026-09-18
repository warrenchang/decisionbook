# Exact two-tone conversion for Chapter 4

> Superseded at the user's request: the earlier AI-generated black-and-white illustration has been restored as the active chapter figure. The exact conversion is retained here as `exact-threshold-30.png`. The chapter footnote again identifies the active pair as corresponding illustrations, not a pixelwise conversion.

The user explicitly requested an exact pixel conversion on 18 September 2026.

The canonical source is `figures/recognition-grayscale-reveal.png`, an AI-generated teaching illustration. It was preserved unchanged. At the time of this experiment, the converted opening figure was written to `figures/recognition-two-tone.png`; the archived converted result is now `exact-threshold-30.png`.

Reproduce with Python and Pillow from the book root:

```sh
python3 scripts/build_recognition_two_tone.py --threshold 30 --output /tmp/recognition-two-tone.png
```

The script converts the source RGB values to Pillow L luminance, then applies one global rule: luminance below 30 becomes 0 (black), otherwise 255 (white). It does not resize, crop, blur, dither, mask, redraw, move, or locally retouch features. Both source and output are 1536 by 1024.

All 1,572,864 output pixels match the threshold rule, with zero mismatches. Only values 0 and 255 occur in the saved image. The source SHA-256 remains unchanged. A second execution reproduced a byte-identical PNG. See `conversion.json` for hashes and counts.

The contact sheets compare thresholds 20, 30, 40, 50, 65, 85, 110, 140, 170, 190, 210, and 230. Threshold 30 was selected to remove continuous contours and reduce large dark regions while retaining landmarks for recognition after the grayscale cue. Recognition difficulty has not been measured; this selection is an editorial judgment. The previous AI redraw is preserved as `previous-ai-redraw.png`.

The chapter's alternative text and provenance footnote were updated. Its delayed reveal remains the final substantive section. Release and destination verification is recorded in the parent `ch04-structure-and-reveal-20260918.md` audit.
