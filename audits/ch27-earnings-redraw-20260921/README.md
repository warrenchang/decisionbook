# Figure 27.5 redraw — 21 September 2026

Request: reproduce Figure 27.5 in the book's visual style. Only this figure's image reference, caption, and alternative text change in Chapter 27; the rest of the current chapter is preserved.

## Source and evidence boundary

The immutable input is `figures/finance-earnings-drift-evidence.png` (SHA-256 `1a3ac4a128b076e2ccb2ba452165aab135b3489ffe801b8a7600a5db126bb4a4`), extracted previously from slide 20, `ppt/media/image12.png`, in the user's `BE09. Behavioral Finance - election and futures.pptx` lecture. The source is attributed to Rendleman, Jones, and Latané (1982), *Journal of Financial Economics*, 10(3), 269–287, https://doi.org/10.1016/0304-405X(82)90003-4. Publisher metadata/abstract were independently checked; the full publisher PDF was inaccessible (403), and original numerical portfolio observations were not obtained.

The redraw is **approximate graphical digitization**, explicitly disclosed in the caption and alternative text. `digitized-geometry.csv` contains traced graphic segments, **not a recovered daily portfolio dataset**. It must not be used as original data for numerical analysis or inference.

`build_figure.py` traces the center of dark ink runs in adjacent image columns and links touching runs. This preserves the visible crossings, preannouncement divergence, and irregularities without fitting smooth curves. The old announcement marker is removed across an 11-pixel strip; ten short straight bridges reconnect the visible traces across approximately 1.32 days. The script documents the merging of pairs of curves in this strip. It does not infer decile identities where the original lines intersect or merge. All curve segments therefore use one color; the ten endpoint labels retain the ranks explicitly printed in the source. Source axes, labels and ticks are replaced with new typesetting and a sparse grid.

The axis mapping uses source tick centers and piecewise linear calibration for slight scan distortion: x = 120, 303, 1113 pixels for days −20, 0, +90; y = 28, 584, 1144 pixels for +10%, 0%, −10%. The extraction script verifies the input hash before running. Its numerical checks measure geometric agreement in source pixels, not precision of the unavailable portfolio observations. Outside the reconstructed marker strip, 95% of retained source-ink pixels are within one pixel of a traced segment, and 99% are within two pixels.

## Design and reproduction

The new figure uses the book's navy/blue/teal palette, white background, simple sans-serif typography, a horizontal outcome label, subdued horizontal grid, announcement-day reference, and direct endpoint labels. Decile 10 means the most favorable standardized earnings surprises; decile 1 the least favorable. These meanings are stated in the caption.

Run with Python containing NumPy, Pillow, SciPy, and Matplotlib:

```sh
MPLCONFIGDIR=/tmp/ch27-figure-mpl /tmp/ch27-figure-venv/bin/python audits/ch27-earnings-redraw-20260921/build_figure.py
NODE_PATH=/Users/ra25fi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules /Users/ra25fi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node audits/ch27-earnings-redraw-20260921/render_fallback.cjs
```

The canonical output is `figures/finance-earnings-drift-redraw.svg`. The matching PNG fallback is rendered from that final SVG at 180 dpi. `redraw-800.png` and `redraw-390.png` record display-size checks. At 800px all labels are readable and curves are distinct. Fitting all ten paths and labels into 390px makes labels too small, so the existing book's 900px SVG reading pane remains in use on narrow HTML screens. EPUB readers can enlarge the image; native-reader pagination/zoom were not inspected.

## Review and validation

An independent source verifier compared the final redraw with the immutable scan and reviewed the extraction method. It found no blocking fidelity or layout issue, confirmed that crossings and endpoint ordering remain visible, and required the approximation and marker-bridge boundary to be stated. These boundaries are recorded above.

The final SVG is inspected directly and parsed as XML; its title/description, viewBox, ten endpoint labels, and plotting limits are checked. HTML and EPUB are rendered sequentially, then asset bytes, numbering, caption, and alternative text are verified in both outputs. The unchanged source PNG hash and a one-line-only chapter change are checked against `chapter-before.qmd`. Repository checks and delivered hashes are recorded in `validation.json`.

The earlier task's browser policy rejected local-file preview, so no alternate browser route is used for this follow-up. Verification includes source-figure visual inspection at native, 800px and 390px sizes plus rendered HTML/EPUB structure and embedded assets; it does not claim a fresh browser screenshot or native EPUB reader inspection. No commit, push, or external publication is performed.
