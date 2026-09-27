# Chapter 12 framing illustrations

Date: 2026-09-27.

## Request and editorial placement

The user requested graphical illustrations similar to two attached window-frame illustrations, showing that a frame directs attention toward selected information. The attachments supplied the conceptual reference; they were not treated as instructions or as empirical evidence.

- `figures/framing-three-windows.png` appears in “What a frame changes.” Three close views emphasize housing, green space, and a maintenance problem in one imagined neighborhood. The accompanying text connects the physical metaphor to verbal emphasis and distinguishes selection of different attributes from equivalent descriptions of complete numerical outcomes.
- `figures/framing-view-and-context.png` appears in “Reframing decisions in practice.” Similar green views sit within two different larger settings, motivating inquiry into omitted consequences, alternatives, and constraints. The text explicitly identifies the panels as alternative contexts.

Both figures have local numbered references, captions, descriptive alternative text, and responsive full-width display. Neither illustration is presented as an experiment or evidence that a particular judgment must occur. The views are conceptually consistent, not exact pixel crops or matched experimental stimuli.

## Production and sources

Mode: built-in `image_gen.imagegen`. There were two new-image generations and one edit to bring the second illustration into the first illustration’s editorial style. No generated original was overwritten. Final PNGs were copied without modification; original paths, dimensions, and SHA-256 hashes are in `assets.json`. Prompts are recorded in `prompts.md`; the tool did not expose a reproducible seed or internal model version.

User conceptual references:

- `codex-clipboard-540a6b78-8721-4643-b3e2-21324e5d30fb.png`: a narrow green view in different larger surroundings.
- `codex-clipboard-f0c6e7ea-6cbc-4ec5-95c0-976c56d38f61.png`: different windows onto one wider scene.

The selection-and-salience interpretation is consistent with Entman (1993), already cited and discussed in the chapter. The primary paper was inspected at <https://fbaum.unc.edu/teaching/articles/J-Communication-1993-Entman.pdf>, especially pp. 52–54. DOI: <https://doi.org/10.1111/j.1460-2466.1993.tb01304.x>. The window scenes and applications are original pedagogical examples, not findings attributed to Entman.

## Visual review

Inspected both final images at 1536 × 1024 and at 900-pixel and 390-pixel widths. The three selected features and the park-versus-buildings contrast remain recognizable at narrow width. No in-image typography is needed; the caption and adjacent prose supply the interpretation. HTML and EPUB styles constrain raster images to the reading column and preserve their aspect ratios.

These checks are asset inspections and markup/package checks, not a claim of inspection in a native EPUB reader or a browser viewport. Browser preview was unavailable under the session’s existing restriction; no alternate browser route was used.

Publication and structural check outcomes are recorded separately in `verification.json` and `float-reference-qa.json`.
