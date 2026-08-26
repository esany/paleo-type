# STATUS — Knau benchmark

Last checkpoint: 2026-08-26

## Overall research goal

Produce a source-exact, critically controlled scholarly edition of the Knau passage in `ThHStAW, EGA, Reg. Ii 5, fol. 61v–63r`, with visible uncertainty, traceable editorial decisions, controlled use of comparison witnesses and a human-auditable path from archival source to transcription, analysis and eventual edition.

Generic scholarly method is defined in `../../methodology/historical-source-workflow.md`; reusable maturity requirements are in `../../methodology/research-gates.md`; diplomatic requirements are in `../../methodology/transcription-guidelines.md`.

This is a `research-scope` project. Source-unit projects own reusable source-local mapping; research relations are recorded in `../relationships.tsv`; historical/source relations remain canonical in `../../corpus/relationships.tsv`.

## Generic gate state

- **G1 — Source and transmission basis secured:** substantially reached.
- **G2 — Principal witness completely and diplomatically represented:** **ACTIVE — not reached.**
- **G3 — Internal palaeographic and notational analysis completed:** not reached.
- **G4 — Comparison witnesses/controls independently assessed and collated:** not reached.
- **G5 — Critically consolidated and proportionally validated text state:** not reached.
- **G6 — Scholarly edition produced and quality-controlled:** final goal, not reached.

## Canonical source basis

Principal witness: `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`, Knau locus fol. 61v–63r / export images 132–135. Reusable source-local digital/folio mapping is owned by `../ega-reg-ii-5-00000129/sources/crosswalk.tsv`.

Project relations:
- `scopes-source-unit` → `ega-reg-ii-5-00000129`;
- `compares-with` → `ega-reg-ii-4-bd-ii-00000089`;
- `uses-as-control` → `ega-reg-ii-3-00000235`;
- `uses-as-context` → `ega-reg-ii-3-00000197`.

These are research-organisational relations only. They do not create source dependence, same-hand status or textual equivalence.

## Existing text checkpoint

The existing `transcription/132.tsv`–`135.tsv` files are legacy working transcription data, not yet the final G2-compliant representation. Controlled anchors include `Knawe` on fol. 61v, closing Knau lines on fol. 63r, repeated `wolff von`, arabic `1`, and twice-reinspected arabic `80` on fol. 62r. Known representation gaps remain especially W1–W6/U1–U2 on 61v, the upper economic passage/U3–U5 on 62r, and substantial multi-line gaps on 62v.

## Active G2 project gaps

1. direct folio-by-folio inspection of physical lineation and reading order on 61v–63r;
2. source-specific layout/material description sufficient to preserve list/accounting/spatial meaning;
3. verified mapping from legacy `132–135` working rows to archival folio/physical-line addresses where possible;
4. explicit classification of source phenomena actually present;
5. minimal compliant migration/extension without discarding prior readings/decisions;
6. derived human-readable diplomatic witness view;
7. full representation-completeness check across fol. 61v–63r.

G2 does **not** require every difficult token to be resolved.

## NEXT ACTION — canonical restart point

Using Reg. Ii 5 fol. 61v–63r and the source-unit crosswalk:
1. inspect each folio for physical lineation, reading order, layout, headings/marginalia, corrections, damage/illegibility, abbreviations and any evidenced hand shifts;
2. assign editor line references only from direct physical inspection;
3. map legacy rows to verified folio/physical-line loci while retaining export IDs as provenance;
4. choose the smallest structured representation required by the generic transcription guideline;
5. migrate/extend the principal-witness transcription;
6. produce the derived human-readable diplomatic witness view;
7. run the generic G2 gate.

Do not let comparison-source work displace this active G2 task.

## Human-in-the-loop state

The user must be able to inspect the current diplomatic text without understanding internal TSV conventions. No independent qualified palaeographic expert review of the full Knau transcription has yet been recorded.

## Restartability test

A new capable researcher/agent must be able to determine from repository + sources: active gate, exact source locus, source-unit project and crosswalk, project relations, remaining G2 gaps, current text evidence and next action without old chat.
