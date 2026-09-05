# Transcription — Reg. Ii 4 Bd. II Knau locus

This directory contains the project-local diplomatic transcription work for the owner-selected Knau passage in Source `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089`, fol. 306v–309r.

This README owns **transcription-layer conventions and navigation only**. It does not own Project scope, current progress, execution cursor, gate state or release authority.

Canonical/operational owners remain:

- `../project.yml` — Project definition and current bounded scope;
- `../STATUS.md` — current Project restart/gate/cursor state;
- `../research/knau-fol306v-309r-evidence-lock.md` — immediate evidence, internal-comparison and external-release rules for this bounded task;
- `../research/knau-fol306v-309r-contamination-matrix.tsv` — allowed/forbidden evidence-use classes;
- `corpus/`, especially the Source crosswalk — canonical Source/File/image/PDF mapping;
- folio-local `first-reading/*.tsv` files — actual changing diplomatic first-reading observations.

## Storage/work partition

The first-reading data are partitioned one archival folio side per file:

```text
transcription/
├── README.md                  # transcription-layer conventions/navigation
└── first-reading/
    ├── README.md              # navigation for folio-local first-reading partitions
    ├── 306v.tsv
    ├── 307r.tsv               # created when inspected
    ├── 307v.tsv               # created when inspected
    ├── 308r.tsv               # created when inspected
    ├── 308v.tsv               # created when inspected
    └── 309r.tsv               # created when inspected
```

This filesystem layout is a storage/audit partition, **not a scholarly parent→child ontology**. The scholarly object is already bounded by the Project + Source + locus/task. A directory or overview file does not become a second owner of that Project state.

Each folio-side TSV contains the actual detailed first-reading observations for that folio. File existence must not be treated as a substitute for canonical progress/gate state.

## What the folio-row columns mean

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

## Internal Reg. Ii 4 comparison evidence

Source-order remains the persistence/traversal order, but the same Reg. Ii 4 witness is not artificially page-isolated during palaeographic recognition.

For a difficult locus, inspect and localize the target graph/sign first. If a directly inspected internal Reg. Ii 4 comparison anchor materially supports, rejects or fails to decide a consequential reading, `evidence_note` may record the exact anchor and concise discriminating reason. The target graph remains primary evidence; expected wording, semantic plausibility and unproven same-hand assumptions do not supply graphemes.

Do not create a general palaeography/survey registry merely because broader direct inspection occurred. Persist only comparison evidence that materially affects a research decision unless repeated reuse later demonstrates a separate need.

Detailed execution and contamination rules live in the project evidence lock and contamination matrix rather than being duplicated here.

## What is stable metadata and therefore not repeated per row

The following are stable scope/provenance metadata rather than changing scholarly row content:

- canonical Source ID;
- archival folio when fixed by the file path/context;
- export image number;
- PDF page;
- exact File/derivative identity;
- the generic fact that this pass came from direct inspection;
- the generic first-reading/pre-collation stage.

Those facts remain recoverable from Project/corpus/evidence owners and Git history. They should not push the diplomatic reading off-screen by being copied into every row.

## Collation boundary

The independent first-reading files do not carry a mutable `collation_status` column. External comparison/collation is released only by the project-local evidence lock after the current independent representation/G2/internal-adjudication sequence is satisfied.

Later collation belongs in a separate comparison layer so that opening a parallel witness cannot silently rewrite first-reading provenance or turn another witness into wording authority.

## Progress and restart state

Do not maintain current progress, current cursor, completion count or release-gate state in this README. Resolve those volatile facts from `../STATUS.md` and the project-local evidence lock. This keeps the transcription documentation stable while the scholarly work advances.
