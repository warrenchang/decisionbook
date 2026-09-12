# Consistent chapter openings — 12 September 2026

All 42 chapters now follow: H1/sidebar title → one italic subtitle → epigraph → opening scene without a section heading → Core Idea → Learning goals.

Removed 24 older taglines that had become a second subtitle after the short-title revision. Retained the subtitle specified by the earlier title convention, including Chapter 19’s *Why Later Loses to Now*. Removed 16 introductory section headings and preserved their existing anchors inline. Moved Chapter 36’s first numbered stage below its learning goals, keeping the five-stage structure and its original anchor. Thirty chapter files changed; the other twelve already matched the convention.

All discussion paragraphs and references are unchanged. The removed taglines, former headings, retained anchors, and before/after source hashes are recorded in `changes.json`. The editorial convention is documented in `scripts/README.md`.

## Verification

- All 42 HTML and all 42 EPUB chapter openings have exactly one expected subtitle, no heading between the epigraph and the opening scene, and the correct Core Idea / Learning goals order.
- Legacy opening anchors are present in both formats; Chapter 36 retains all five numbered stages.
- Master bibliography: 849 unique references, synchronized.
- Source and rendered-output QA: PASS, zero errors and warnings.
- HTML link audit: 8,020 local references checked, including 2,886 fragment links; no missing targets or duplicate IDs.
- EPUB package and internal-link QA: PASS, zero errors.
- Desktop and phone HTML previews inspected for Chapters 2, 17, and 36; EPUB previews inspected for Chapters 2 and 17 in Chromium.
- The preceding figure restoration and Figure 2.1 phone layout are preserved byte-for-byte in the source and HTML release.
- `git diff --check`: PASS.

`check-openings.cjs html` checks the built HTML. For `check-openings.cjs epub`, first extract the final EPUB into `$OPENING_CHECK_TEMP/epub/`; the script defaults to this task’s directory under `/private/tmp`. The script requires Playwright and local Chrome. The EPUB visual check uses packaged XHTML in Chromium rather than a native reader.
