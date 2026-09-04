# Reg. Ii 4 Bd. II Knau fol. 306v-309r — evidence lock and contamination control

Created: 2026-09-04

## Authority and scope

This project-local file records the execution lock for the owner-selected current task in `projects/ega-reg-ii-4-bd-ii/STATUS.md` and `project.yml`.

It does not create a new Project, Source, Project->Source use, research priority or textual-dependence claim. It only constrains how the already-authorized Reg. Ii 4 Bd. II Knau first reading is executed and later checked.

Current bounded target:

- Project: `ega-reg-ii-4-bd-ii`
- Source: `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089`
- Historical locus: Knau passage, fol. 306v-309r
- Digital locus: export images 667-672 / PDF pages 27-32
- Start cursor: fol. 306v / export image 667
- Mode: independent diplomatic first reading from Reg. Ii 4 Bd. II itself

## Evidence state for the active work context

Canonical repository state already records the exact inspected export as `FILE-REG-II-4-II-00000089-EXPORT` and the crosswalk fol. 306v-309r <-> export images 667-672 <-> PDF pages 27-32.

The 2026-09-03/04 active target context additionally had the uploaded PDF `1533-Visitationsprotokoll-Ziegenrueck-ThHStAW, EGA, Reg. Ii 4 Bd. II-294r-313r.pdf` visually inspectable. Its relevant visible pages show:

| folio | PDF page | export image |
|---|---:|---:|
| fol. 306v | 27 | 667 |
| fol. 307r | 28 | 668 |
| fol. 307v | 29 | 669 |
| fol. 308r | 30 | 670 |
| fol. 308v | 31 | 671 |
| fol. 309r | 32 | 672 |

This is a target-context visual-evidence PASS for the current session only. If the work context changes, staging and pixel-inspectability must be re-established for the same evidence object instead of relying on this prose.

## Contamination lock

The following separation is mandatory until a complete independent Reg. Ii 4 first-reading draft exists for fol. 306v-309r.

| Material | Status before independent first reading | Allowed use | Forbidden use |
|---|---|---|---|
| Reg. Ii 4 Bd. II, Source `...00000089`, images 667-672 | Primary evidence | visual inspection, physical-line inventory, diplomatic reading, uncertainty marking | none |
| Reg. Ii 5 Ziegenrück material | quarantined parallel/legacy material | method warning, later controlled collation | wording source, line mapping, grapheme supply, same-hand assumption |
| Legacy G2/Knau files and old TSV/apparatus/palaeography | contaminated until Source/File/locus attribution is re-established | recovery/checking after release gate | promotion as Reg. Ii 4 reading, silent import, automatic witness attribution |
| Prior chat draft of image 667 | unadjudicated local draft | cursor memory and risk signal only | canonical line text unless each row is reinspected against image 667 |
| Early-modern visitation/domain knowledge | contextual hypothesis/control | generate questions, rank alternatives after graphical inspection | replace unread graphemes, normalize diplomatic spelling, infer names/amounts |

## Release gate for legacy/parallels

Legacy Knau/G2 or Reg. Ii 5 material may be opened for textual comparison only after all of the following are true:

1. fol. 306v-309r has a complete independent Reg. Ii 4 first-reading draft in source order;
2. every unresolved, unclear, damaged, supplied, deleted, added or otherwise non-ordinary locus is explicitly marked;
3. physical line references are stable enough to cite and compare;
4. the comparison record identifies itself as collation/checking, not as original first reading;
5. any promoted correction explains the inspected Reg. Ii 4 graphical basis and does not rely on parallel wording alone.

If these conditions are not met, the correct action is to continue Reg. Ii 4 inspection, not to consult clearer or older material.

## First-reading row requirements

Each future transcription row must preserve at least:

- canonical `source_id`;
- folio/page;
- export image and PDF page as provenance/crosswalk values;
- editor-assigned physical line reference;
- reading order and region where relevant;
- diplomatic written reading;
- source phenomena separate from research confidence;
- research status and graphically viable alternatives;
- abbreviation/editorial supply only as separate information where needed;
- evidence note for consequential uncertainty or revision;
- collation status showing `not_collated` until the release gate has been passed.

A fluent full line with hidden uncertainty is worse than a narrower visible unresolved span.

## Current execution cursor

Next executable action:

> Reinspect fol. 306v / image 667 from the Reg. Ii 4 PDF and build the physical-line first-reading rows from the image itself. Do not populate rows from legacy material or from the unadjudicated chat draft.

After image 667 is line-adjudicated, continue in source order through images 668-672.

## Invalidation triggers

Re-run the evidence prerequisite if:

- the active work context no longer has the uploaded PDF or render/crop set;
- the inspected image does not match `FILE-REG-II-4-II-00000089-EXPORT` / image 667-672;
- a later corpus/crosswalk correction changes the folio/image/PDF-page mapping;
- visual inspectability fails or a different derivative is substituted.

New model uncertainty alone is not an invalidation trigger. It should narrow the unresolved locus or trigger qualified review, not send the work back into retrieval/governance loops.
