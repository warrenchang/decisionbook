# Foundations review, 27 September 2026

Owner: foundations worker. Canonical Chapters 01–14 were read in full, including learning goals, examples, research lenses, practice labs and chapter references. Edits are confined to 13 chapter files and this audit folder; Chapter 02 was deliberately unchanged. No generated output, existing figure asset, master reference list, configuration, index, commit or push was changed by this worker. Root owns book-wide integration and rendering.

## Actual source coverage

- **488 slides across eight current decks:** BE2026 BE01–BE05 and the full DPN2026 Decision Process, Attention and Prediction, and Heuristics and Biases decks. Ordered visible text and the actual slide-linked speaker notes were read. `current-slide-coverage.csv` accounts for every slide exactly once in 86 grouped rows and maps substantive topics to explicit book anchors.
- **1,129 slides across 15 archival/additional decks:** ordered topic inventories were screened, with selected relevant passages subsequently read in full. This is narrower than reading every archived speaker note. `archival-review.md` records deck scope, selected examples, destinations and exclusions. It must not be described as a full archival-deck read.
- Three BE-folder DPN copies were compared at the normalized slide-text-plus-notes level against the DPN-course versions. Decision Process had 82 of 84 equal slides; the museum/Mars order differed at 25–26. Attention and Prediction had 91 of 91 equal slides. Heuristics and Biases had 78 of 79 equal slides in the shorter copy; the full copy adds a Derren Brown slide near the beginning and changes the Stroop text. These copies are not additional independent evidence.
- The authoritative root manifest contains 345 source files, including readings, background books, other chapter topics and duplicates. This worker does **not** claim to have read all 345. `source-scope.csv` gives exact IDs, paths, hashes, lengths and review depth for this worker's selected scope.
- A report from the social worker about DPN Social Influence slides 16–36 was considered a cross-range lead, not independently counted as a full deck read. Attribution and self-serving beliefs are already in Chapter 10; interpersonal expectations in Chapter 05; new aging discussion covers the longitudinal association. Stereotype material remains with the identity owner. The 2025 loneliness-belief article was not added: it would require a separate developed social-connection discussion and was not necessary for the chapter's now concrete causal comparisons.

## Visual source inspection

Inspected 34 embedded source images in three temporary contact sheets: BE03 slides 11–17 and 21; DPN Attention/Prediction 27–33, 41 and 66; BE02 21 and 25. These included face-contrast stimuli, the Thatcher configuration, hollow face, illumination/traffic-light and checker/cube illusions, footprint shading, the squirrel/alligator and other affect-ambiguous figures, the dress, a name-letter graph and a BBC brain still. This was **static embedded-asset inspection**, not complete slide rendering, playback of animations/videos, or a claim of book-wide visual QA. No source image was imported into the book. Existing book figures were preserved.

## Main improvements

The revisions develop examples through a comparison that identifies what changed: own-name noticing and shadowing errors; tracking versus unexpected obstacles with head-up displays; upside-down versus upright face configurations; language-specific infant discrimination; tones present versus absent after conditioning; ingredient disclosure before versus after tasting; food labels versus measured hormonal/behavioral outcomes; reappraising the same bodily arousal; visible incidental evaluation versus masked incentives; product before price versus price before product; choosing versus rejecting; related presented words versus an unpresented lure; and an informed versus uninformed Monty Hall host.

The added studies are not treated as a catalogue of effects. Small studies are grouped in optional lenses when appropriate, contrasting studies and the close choose/reject replication are included, clinical and neural findings retain their design boundaries, and established everyday examples remain in place. The original fly/System 1 anecdote, choice-blindness faces, framing surroundings and earlier Behave integration were preserved.

## Verification and limitations

- Ledger slide coverage and all ledger target anchors were checked programmatically; see `coverage-checks.txt`.
- New quantitative statements and new references were checked against primary papers or primary repository metadata; see `source-verification.md`. The NASA PDF, rather than incomplete catalog metadata, supplied the third author.
- `git diff --check` passed for Chapters 01–14 after edits. Added explicit anchors are unique. New internal crosslinks resolve to the intended chapter/anchor.
- Probability examples were independently enumerated: five independent 0.9 stages succeed with 0.59049 probability; informed-host Monty Hall switching wins 2/3; an uninformed random host conditional on revealing a goat yields 1/2.
- This worker did not run Quarto, evaluate generated HTML/EPUB, re-test unrelated code, or verify every pre-existing reference. Root completes integrated rendering and QA.
