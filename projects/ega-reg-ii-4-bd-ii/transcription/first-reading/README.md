# Independent first reading — Knau, fol. 306v–309r

This directory is the **parent research unit for the independent first reading of the complete owner-selected Knau passage** in Source `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089`.

The parent scope is the whole relevant section:

- archival locus: fol. 306v–309r;
- export images: 667–672;
- PDF pages: 27–32;
- mode: independent diplomatic first reading from Reg. Ii 4 Bd. II itself;
- comparison lock: Reg. Ii 5 and legacy G2/Knau remain excluded as wording evidence until the complete parent scope has an independent first-reading draft.

The detailed transcription goes one level deeper: **one child file per archival folio side**. The parent is not replaced by those children; the children are the inspectable components from which the parent first-reading state is constituted.

## Parent → child structure

| order | folio | export image | PDF page | child file | first-reading state |
|---:|---|---:|---:|---|---|
| 1 | 306v | 667 | 27 | `306v.tsv` | working draft present |
| 2 | 307r | 668 | 28 | `307r.tsv` | pending inspection |
| 3 | 307v | 669 | 29 | `307v.tsv` | pending inspection |
| 4 | 308r | 670 | 30 | `308r.tsv` | pending inspection |
| 5 | 308v | 671 | 31 | `308v.tsv` | pending inspection |
| 6 | 309r | 672 | 32 | `309r.tsv` | pending inspection |

Pending child files are created only when their folio has actually been inspected, so file existence does not masquerade as research completion.

## What belongs to the parent

The parent records information that is meaningful for the **whole first-reading task**, especially:

- the bounded section/locus being independently read;
- source-order of the folio children;
- progress/completeness across the section;
- the comparison/contamination release gate;
- the current cursor;
- whether the complete section can yet be called an independent first-reading draft.

These are not repeated on every transcription row.

## What belongs to each folio child

Each `*.tsv` child records the **actual changing scholarly information** for that folio:

1. `reading_order`;
2. `diplomatic_reading`;
3. `line_ref`;
4. `region` where materially relevant;
5. `source_phenomena`;
6. `research_status`;
7. graphically viable `alternatives`;
8. separate abbreviation/editorial-supply information where needed;
9. only consequential local `evidence_note` values.

Stable Source/File/image/PDF provenance remains recoverable from the parent scope, Project evidence lock, canonical corpus crosswalk and Git history rather than being copied into every row.

## Parent completion rule

The parent first reading of fol. 306v–309r is **not complete** merely because one folio child is complete.

It reaches a complete independent first-reading draft only when:

1. every folio child 306v, 307r, 307v, 308r, 308v and 309r has been directly inspected from Reg. Ii 4;
2. every relevant physical text unit is represented in source order;
3. unresolved/unclear and other source phenomena are explicitly retained rather than silently completed;
4. no wording has been supplied from Reg. Ii 5, legacy G2/Knau or other parallel material;
5. the parent progress table can mark all six children as independently represented.

Only after that parent-level gate may parallel/legacy material be opened for controlled collation under `../../research/knau-fol306v-309r-evidence-lock.md`.

## Current state

- completed child pass: `306v.tsv` / image 667;
- current cursor: fol. 307r / image 668;
- parent first-reading state: **in progress, 1 of 6 folio sides represented**;
- legacy/parallels release gate: **closed**.

A later human-readable whole-section view should be derived from the ordered folio children rather than maintained as a second manually edited transcription truth.
