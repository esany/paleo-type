# Transcription — Reg. Ii 4 Bd. II Knau locus

This directory contains the project-local diplomatic transcription work for the owner-selected Knau passage in Source `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089`, fol. 306v–309r.

The source/file/image/PDF mapping is canonically owned in `corpus/`, especially `corpus/source-data/THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089/crosswalk.tsv`. It is intentionally **not repeated on every transcription row**.

## Research hierarchy

The transcription layer now has an explicit parent → child structure:

```text
transcription/
├── README.md                  # transcription-layer conventions
└── first-reading/
    ├── README.md              # parent: complete Knau first-reading task, fol. 306v–309r
    ├── 306v.tsv               # child: folio-side first-reading detail
    ├── 307r.tsv               # created when inspected
    ├── 307v.tsv               # created when inspected
    ├── 308r.tsv               # created when inspected
    ├── 308v.tsv               # created when inspected
    └── 309r.tsv               # created when inspected
```

`first-reading/README.md` is the **parent overview/state for the complete relevant section**. It owns the ordered child inventory, section-level progress/completion state, current cursor and release gate. It does not duplicate all diplomatic text.

Each folio-side TSV is a child research record containing the actual detailed first-reading observations for that folio.

This preserves both levels: the task remains “independent first reading of fol. 306v–309r”, while inspection and auditability go one level deeper per folio side.

## What the child-row columns mean

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
- archival folio when already fixed by the child file name/context;
- export image number;
- PDF page;
- exact File/derivative identity;
- the generic fact that this pass came from direct inspection;
- the generic pre-collation state.

Those facts remain recoverable from the first-reading parent overview, Project `STATUS.md`, evidence lock, canonical `corpus/` File/crosswalk records and Git history. They should not push the diplomatic reading off-screen by being copied into every row.

## Collation boundary

The independent first-reading children do not carry a mutable `collation_status` column. Before the parent release gate they are, by definition, independent first-reading material. Later comparison/collation belongs in a separate collation layer so that opening a parallel witness does not silently rewrite the provenance or independence of the first-reading records.

## Current state

The parent scope is fol. 306v–309r / images 667–672. Only child `first-reading/306v.tsv` has been entered so far. The next valid cursor is fol. 307r / export image 668. Reg. Ii 5 and legacy G2/Knau material remain blocked as wording evidence until the **complete parent first reading** satisfies the project-local release gate.
