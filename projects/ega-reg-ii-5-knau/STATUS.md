# STATUS — Knau benchmark

Last checkpoint: 2026-08-26

## Overall research goal

Produce a source-exact, critically controlled scholarly edition of the Knau passage in `ThHStAW, EGA, Reg. Ii 5, fol. 61v–63r`, with visible uncertainty, traceable editorial decisions, controlled use of comparison witnesses and a human-auditable path from archival source to transcription, analysis and eventual edition.

The authoritative end-to-end scholarly method is `methodology/historical-source-workflow.md`. Detailed diplomatic requirements are in `methodology/transcription-guidelines.md`. Project research gates are in `MILESTONES.md`.

## Method audit checkpoint

A standards/expertise audit on 2026-08-26 found that the repository is already strong in provenance, source-relationship discipline, evidence-layer separation, revision traceability and AI-governance, but that the **diplomatic transcription layer was underspecified** relative to established archival/editorial practice.

The audit is persisted in `methodology/historical-source-workflow.md` and has these binding consequences:

- archival folio/page + editor-assigned physical line reference must become the primary scholarly transcription address; export-image IDs remain provenance/legacy references;
- M2 transcription must preserve folio breaks, physical lineation and source-relevant layout/reading order;
- uncertain positive readings must be distinguishable from illegible/gap material;
- editorial supply/expansion must be distinguishable from written source text;
- additions, deletions, damage and hand shifts must be representable when actually present;
- abbreviation sign and editor-provided expansion must remain separate;
- a human-readable folio/line diplomatic witness view must be derivable from canonical transcription data without a second manually maintained text truth;
- method-compliant AI-assisted work must not be described as independently expert-validated unless a qualified independent review actually occurred.

The existing `132.tsv`–`135.tsv` files are therefore **legacy working transcription data**, not yet the final M2-compliant scholarly representation. Existing readings and revision history remain valuable and must not be discarded.

## Milestone state

- **M1 — Source and transmission basis secured:** substantially reached.
- **M2 — Principal witness completely represented:** **ACTIVE — not reached.** It now includes compliance with the revised diplomatic-transcription requirements above.
- **M3 — Internal palaeographic and notational analysis completed:** not reached.
- **M4 — Existing comparison witnesses/controls independently assessed and collated:** not reached; corresponding Reg. Ii 4 locus is located.
- **M5 — Critically consolidated text state:** not reached.
- **M6 — Scholarly edition produced and quality-controlled:** final goal, not current work.

## Canonical source basis

### Principal witness

`THHSTAW-EGA-REG-II-5-STAT-VIS-00000129` — ThHStAW, EGA, Reg. Ii 5, **Visitation im Amt Ziegenrück**, 1533 context.

Knau locus:

- export image 132 = fol. 61v — Knau begins;
- export image 133 = fol. 62r;
- export image 134 = fol. 62v;
- export image 135 = fol. 63r — Knau closes at top; following entry is outside scope.

Exact digital/folio mapping: `sources/reg-ii-5-00000129-crosswalk.tsv`.

### Existing comparison/control sources

- `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089` — related 1533 Ziegenrück record; corresponding Knau locus at fol. `306v–309r`. Detailed independent transcription/collation remains M4 work.
- `THHSTAW-EGA-REG-II-3-STAT-VIS-00000235` — 1529 Pfarreinkommen record; relevant `Knaw Kirch Einkommen` at fol. `304r`. Comparison/control for economic/notation questions, not automatically a textual witness or same-hand control.
- `THHSTAW-EGA-REG-II-3-STAT-VIS-00000197` — separate earlier 1529 visitation source; no textual-dependence or same-hand claim assumed.

## Existing text checkpoint

The legacy transcription contains useful working readings, but it cannot yet be presented as a complete scholarly diplomatic transcript because physical lineation and several source phenomena were not systematically encoded.

Controlled anchors include:

- `Knawe` heading on fol. 61v — directly reinspected, `observed`;
- closing Knau lines on fol. 63r — directly controlled, `observed`;
- repeated `wolff von` — visually supported; following surname token remains graphematically variant/unresolved;
- arabic `1` visible in economic clauses;
- arabic `80` directly reinspected twice on fol. 62r as numeral form only.

Known text gaps in the legacy representation remain especially:

- fol. 61v: W1–W6 and U1–U2;
- fol. 62r: upper economic/natural-obligation passage plus U3–U5 and variant lines;
- fol. 62v: largest continuous gap, with multi-line paragraph summaries instead of line-level source text.

## Active M2 problem

Before further lexical/palaeographic resolution, the principal witness must be re-inspected as a **document**, not merely as isolated tokens, so that the compliant transcription can preserve the source's actual physical structure and phenomena.

This is a scholarly correction, not a software-development project. Do not design a large abstract schema or migrate line IDs by assumption.

## NEXT ACTION — canonical restart point

Using the original/digital images of Reg. Ii 5 fol. 61v–63r:

1. inspect each folio for physical lineation, reading order and relevant layout (including list/accounting arrangement), headings/marginalia, additions/deletions/corrections, damage/illegibility, abbreviation practice and any evidence of hand shifts;
2. assign editor line references **only from direct physical-line inspection** (`61v:01`, etc. conceptually); do not mechanically convert legacy `132:xx` IDs;
3. map every existing legacy transcription row to its verified folio/physical-line locus where possible, preserving the legacy/export IDs as provenance;
4. identify which source phenomena actually occur and choose the **smallest** compliant structured representation required by `transcription-guidelines.md`;
5. then migrate/extend the principal-witness transcription without discarding prior readings/decisions;
6. produce a derived human-readable diplomatic witness view showing folio breaks and physical line references;
7. complete the remaining visible text representation folio by folio and run the M2 gate.

Do not begin detailed C2 notation analysis, Reg. Ii 4 collation, historical normalization or edition rendering as the controlling task until this M2 source-representation correction is complete.

## Human-in-the-loop state

The user must be able to inspect the current diplomatic text without understanding internal TSV conventions. The future witness view is therefore a scholarly M2 requirement, not a cosmetic feature.

No independent qualified palaeographic expert review of the full Knau transcription has yet been recorded. Method-compliant AI-assisted readings must remain distinguishable from any later independent specialist validation.

## Stop conditions

Mark uncertainty rather than infer when source evidence does not discriminate; distinguish unclear positive reading from illegible/gap material; never add supplied text indistinguishably to the written text; do not claim same hand without palaeographic evidence; do not infer physical line addresses from export numbering; and do not let comparison sources overwrite the principal witness.

## Restartability test

A new capable researcher/agent must be able to determine from the repository:

- which scholarly standards/method govern the work;
- why the legacy transcription is not yet M2-compliant;
- what source phenomena and physical structure must now be directly checked;
- what existing readings remain valid working evidence;
- what the exact next source-inspection action is;
- what has and has not received independent human expert validation.

If any of that requires old chat, the checkpoint is incomplete.
