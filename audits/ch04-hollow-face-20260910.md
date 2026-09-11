# Chapter 4: hollow-face illusion and online media

## Content and attribution

Added a subsection after the duck–rabbit discussion, with a short observation exercise, a responsive Wikimedia video embed, a link to the supplied interactive 3D model, and an entry in Appendix D. The explanation distinguishes concavity from its convex appearance and discusses familiarity, lighting, and binocular information without claiming a unique mechanism.

The two new experimental references are Hill and Bruce (1993), DOI 10.1068/p220887, and Hill and Johnston (2007), DOI 10.1068/p5523. An independent source verifier checked the final prose and bibliographic details and found no material issue. The connection to decision-making is presented as a teaching inference.

The video page identifies Co as author, Iljsdf as uploader, July 31, 2026 as date, and CC BY-SA 4.0 as license. It is embedded unchanged, with visible credit, source link, and license link. The comparison surface is described as part of a demonstration; the uploader's stronger claim that the comparison isolates face-specific prior knowledge was not adopted.

The model page credits Wael Tsar's mesh and cmglee's recentering, symmetrizing, and STL conversion, under CC BY 4.0. Both are credited beside the model link. No remote media was copied into the repository.

## Format behavior

The iframe has an explicit closing tag, accessible title and description, lazy loading, fullscreen support, and the supplied player URL. Its 640 × 1280 native ratio is preserved with a maximum rendered width of 360 pixels, bounded by its reading column. The source explicitly excludes the player from EPUB; the description, source link, model link, and credits remain in both formats.

An initial `when-format="html"` condition also matched Quarto's EPUB output and exposed invalid raw iframe markup to the XHTML parser. The format gate was changed to `unless-format="epub"`, following the book's existing format-specific convention, and the EPUB was rebuilt.

## Verification scope

The Wikimedia embed player was opened and played on its original site in the in-app browser. The supplied 3D Viewer URL loaded the named model and displayed its geometry. The book's automated whole-book HTML figure check completed with 117 placements at desktop and mobile widths, with 0 issues.

The subsequent focused local chapter preview was blocked by the browser URL policy. That block was respected; a focused local player/layout check was not performed through another browser surface. Final media integration checks use generated-file inspection. No claim is made that local embedded playback or the new section's final visual layout was verified interactively.

Final checks passed after rebuilding the corrected EPUB and refreshing the HTML chapter:

- Reference synchronization: 834 unique entries.
- Source/HTML QA: 0 errors and 0 warnings; EPUB release QA: 0 errors.
- Generated HTML contains exactly the supplied player URL, an accessible title and description, lazy loading, and proportional CSS sizing.
- EPUB excludes the player and its wrapper. Both formats retain the description, the video/model links, author credits, and license links.
- Narrative text matches between HTML and EPUB. Both experimental references are present in both editions.
- Appendix D's new subsection link resolves in both formats.
- The EPUB archive passes its integrity check, and staged/distributed copies match.

Focused file checks are recorded in `ch04-hollow-face-file-checks-20260910.json`. Build logs and temporary verification scripts are in `/private/tmp/ch04-hollow-face/`.
