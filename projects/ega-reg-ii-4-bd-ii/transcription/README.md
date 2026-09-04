# Transcription — Reg. Ii 4 Bd. II Knau locus

This directory contains the project-local diplomatic transcription work for the owner-selected Knau passage in Source `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089`, fol. 306v–309r.

The source/file/image/PDF mapping is canonically owned in `corpus/`, especially `corpus/source-data/THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089/crosswalk.tsv`. It is intentionally **not repeated on every transcription row**.

## First-reading files

Independent first readings are stored one archival folio per file under `first-reading/`:

- `first-reading/306v.tsv` — current source-exact first-reading draft for fol. 306v / export image 667.
- further files are added only when that folio has actually been inspected.

This avoids a range-named file appearing complete before the full range has been read.

## What the row columns mean

The first columns are ordered for human inspection:

1. `reading_order` — order in which the source unit is read on the folio.
2. `diplomatic_reading` — the actual current diplomatic reading; this is the main scholarly content.
3. `line_ref` — editor-assigned physical line/reference address within the folio.
4. `region` — source/layout structure when it affects reading or interpretation.
5. `source_phenomena` — visible source phenomena such as abbreviation, uncertainty, divider, possible deletion/addition, etc.
6. `research_status` — current epistemic state of the reading (`observed`, `working`, `unresolved`, etc.).
7. `alternatives` — graphically viable competing readings.
8. `abbreviation_layer` — separate editorial information about an abbreviation when needed; never silently substitutes the written form.
9. `editorial_supply` — explicit editorial supply only when present.
10. `evidence_note` — only the consequential local reason/evidence needed to understand an uncertainty or decision.

These are the values that can materially change as source inspection improves. Git history records those revisions.

## What is metadata and therefore not repeated per row

The following are stable scope/provenance metadata for a folio rather than changing scholarly row content:

- canonical Source ID;
- archival folio when already fixed by the file name/context;
- export image number;
- PDF page;
- exact File/derivative identity;
- the generic fact that this pass came from direct inspection;
- the generic pre-collation state.

Those facts remain recoverable from the Project `STATUS.md`, the evidence lock, canonical `corpus/` File/crosswalk records and Git history. They should not push the diplomatic reading off-screen by being copied into every row.

## Collation boundary

The independent first-reading files do not carry a mutable `collation_status` column. Before the release gate they are, by definition, independent first-reading material. Later comparison/collation belongs in a separate collation layer so that opening a parallel witness does not silently rewrite the provenance or independence of the first-reading table.

## Current state

Only fol. 306v has been entered so far. The next valid cursor is fol. 307r / export image 668. Reg. Ii 5 and legacy G2/Knau material remain blocked as wording evidence until the full fol. 306v–309r independent first reading satisfies the project-local release gate.
