# Relocate the lie-detection discussion

The general evidence and figure now appear in Chapter 33, immediately after
“When intention feels visible,” under “Why demeanor is a poor guide to lying.”
The passage uses the chapter's deadline misunderstanding to connect ambiguous
behavior, suspicions of dishonesty, checking records, and perspective-getting.
The learning goals and transition into “Ask rather than merely imagine” were
revised to match that progression.

Chapter 38 retains strategic disclosure, omission and paltering, the distinction
between privacy and deception, the four claim-verification questions, and the
Schweitzer–Croson findings on direct questions. Its subsection is now titled
“Verify consequential claims,” with its existing anchor preserved. A forecast
and capacity-confirmation example connects verification to the chapter's
supplier dispute and operating rules. Reciprocal links connect the general
evidence in Chapter 33 with this application in Chapter 38.

Chapter 34's opening and its existing link to Chapter 33 were reviewed. Its
progression from an unsupported accusation to understanding and relationship
repair remains consistent with the revised communication chapter; no edit to
Chapter 34 was needed.

The figure, its caption, alternative text, and numerical results were retained.
Five reference entries moved from Chapter 38 to Chapter 33: Bond and DePaulo,
Köhnken, Sporer and Schwandt, Vrij and colleagues, and Zuckerman and colleagues.
The union of chapter references and the master bibliography are unchanged.
The concept-index entries for deception, information verification, and lie
detection now identify the separate evidence and application sections.

This was an editorial relocation of existing evidence, not a new literature
review or reanalysis. No figure data or scientific interpretation was changed.

Records:

- `ch33-before.qmd`, `ch38-before.qmd`, and `concept-index-before.qmd` preserve
  the source state before this request.
- `source-check.json` records preservation of the references, figure markup,
  sample sizes and accuracy figures, application, and links.
- `float-source-qa.json` records source figure and table reference checks.
- `check-layout.cjs` inspects the actual HTML and extracted EPUB sections at
  desktop and phone widths, including the figure's existing horizontal reading
  pane on phones. It writes screenshots and `layout-check.json`.

HTML and EPUB builds are run sequentially. EPUB visual inspection uses the
packaged XHTML and image in Chrome; it does not test every native EPUB reader.

Completed validation: both builds succeeded. Book QA reported zero errors and
zero warnings; EPUB QA reported zero errors; source, HTML, and EPUB float
checks reported zero issues. Eight desktop/phone section layouts were checked
and the rendered text and figure were inspected. The moved figure is numbered
33.4 in both editions and is absent from Chapter 38. The search index now
locates the evidence in Chapter 33, with no stale Chapter 38 evidence entry.

No files were staged, committed, or pushed for this request.
