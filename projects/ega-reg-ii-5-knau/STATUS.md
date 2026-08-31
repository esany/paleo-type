# STATUS — ThHStAW, EGA, Reg. Ii 5

Last checkpoint: 2026-08-31

## Historical project root

This project is anchored to the historically independent source structure `ACT-THHSTAW-EGA-REG-II-5` — *Registratur für die Superintendenz Neustadt an der Orla (Auszug)* — via `project.yml: project_source_id`.

The current Knau work is a bounded research scope inside that project root; it does not define the project boundary.

Generic scholarly method is defined in `../../methodology/historical-source-workflow.md`; reusable maturity requirements are in `../../methodology/research-gates.md`; diplomatic requirements are in `../../methodology/transcription-guidelines.md`.

## Research purpose and active scope

Produce a source-exact, critically controlled scholarly edition and historical understanding of the relevant material within Reg. Ii 5. The active diplomatic focus is the Knau passage at fol. 61v–63r inside the Ziegenrück protocol fol. 55v–66v.

## Sources used

The project uses four canonical protocol/source records. Structural membership is derived from `corpus/relationships.tsv` `part_of` relations, not from project roles.

- **internal / principal** — `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`: *Visitation im Amt Ziegenrück*, fol. 55v–66v, structurally inside `ACT-THHSTAW-EGA-REG-II-5`. Principal Knau locus: fol. 61v–63r / export images 132–135.
- **external / comparison** — `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089`: *Visitation im Amt Ziegenrück*, fol. 294r–313r, structurally inside `ACT-THHSTAW-EGA-REG-II-4-BD-II`. Corresponding Knau locus: fol. 306v–309r / export images 667–672.
- **external / context** — `THHSTAW-EGA-REG-II-3-PROT-NEUSTADT-41R-63V`: *Visitation in Neustadt an der Orla*, fol. 41r–63v, structurally inside `ACT-THHSTAW-EGA-REG-II-3`.
- **external / control** — `THHSTAW-EGA-REG-II-3-STAT-VIS-00000235`: *Pfarreinkommen Gössitz, Knau (mit Laskau, Bahren), Liebschütz (mit Liebengrün)*, fol. 303r–306r, structurally inside the same Reg. Ii 3 act.

## Digital addressing / provenance state

For the principal Reg. Ii 5 source, folio↔export-image↔PDF-page mapping is canonical. Stable per-image URNs are **not established** and must not be inferred. Directly observed provider derivative/TIFF labels for the active slice are recorded in the Source crosswalk. The exact parent File is `FILE-REG-II-5-00000129-EXCERPT`; provider file object `stat_file_00000033` remains distinct from Source/provider record `stat_visitation_00000129`.

For the active G2 slice, the exact parent File was SHA-256 verified and unprocessed baselines for fol. 61v–63r were reproduced from canonical PDF pages 14–17 using the persisted Poppler recipe. Durable derivation/recovery provenance is recorded in `research/g2-baseline-provenance.md`.

The canonical private-repository target for the exact parent remains:

`corpus/source-files/THHSTAW-EGA-REG-II-5-STAT-VIS-00000129/original/1a03ea95927-120-143.pdf`

The exact parent binary is not yet verified present there; repository preservation remains separate from active evidence staging.

## Evidence availability state

The project distinguishes atomic evidence states from the derived execution gate:

```text
RETRIEVABLE          an authorized tool/path can recover bytes
STAGED                the required evidence object is present in the target work context
VISION-INSPECTABLE    the target Source Research context can actually inspect the pixels
VISUAL EVIDENCE READY = STAGED + VISION-INSPECTABLE for the same object in the same target context
```

Historical #84 testing established exact evidence identity and a private attachment retrieval route, but that did not imply that a later Source Research context already had a staged, vision-inspectable image. The subsequent bounded #72 execution received image 135 directly in its target context and actually inspected the manuscript pixels.

Current state:

```text
exact parent identity / SHA                                  PASS
canonical folio↔image↔PDF mapping                           PASS
reproducible baseline derivation                            PASS
controlled private storage authority                        PASS
private #84 baseline attachments present                    PASS
historical private-attachment retrievability                PASS / evidenced
image 135 STAGED in the completed #72 target context        PASS — context-bound
image 135 VISION-INSPECTABLE in that #72 target context     PASS — actual pixel inspection
VISUAL EVIDENCE READY for the completed #72 execution       PASS — context-bound
exact parent binary committed + SHA reverified in repo       PENDING — preservation only
```

These target-context PASS states certify the completed #72 execution only. They must not be inherited automatically by a future chat/context without a new target-context check.

## Generic gate state

- **G1 — Source and transmission basis secured:** substantially reached for identity, provenance and controlled use; parent-binary preservation remains separately pending.
- **G2 — Principal witness completely and diplomatically represented:** **ACTIVE — not reached.** Checkpoint A, Checkpoint B, the bounded Checkpoint-B Domain Review and the project-local `63r-L05–L11` completion are complete. GOV-M4 synthesis has not yet admitted a final implementation, and this status does not independently assert that all remaining G2 exit conditions are satisfied.
- **G3 — Internal palaeographic and notational analysis completed:** not reached.
- **G4 — Comparison witnesses/controls independently assessed and collated:** not reached.
- **G5 — Critically consolidated and proportionally validated text state:** not reached.
- **G6 — Scholarly edition produced and quality-controlled:** final goal, not reached.

## G2 evidence / review state

1. **Checkpoint A — PASS.** Durable physical/source-order fixture: `research/g2-checkpoint-a-physical-inventory.md`.
2. **Checkpoint B — COMPLETE.** Durable Source Research fixture: `research/g2-checkpoint-b-semantic-loss.md`. Exactness remains `partial`, `ambiguous` or `unresolved` where the evidence does not support a stronger claim.
3. **Checkpoint-B Domain Review — COMPLETE.** Durable review fixture: `research/g2-domain-review-checkpoint-b.md`, commit `be003d0cf554e94e322f36b2434cd86c3856cc4b`.
4. **New generic requirement gap — NONE.** #73 found that the demonstrated losses instantiate existing requirements.
5. **GOV-M4 synthesis input — exactly three bounded reusable capability candidates:**
   - canonical physical Source-unit/locus addressing independent of legacy row IDs;
   - lossless preservation of materially relevant source-order/spatial association;
   - explicit representation of confirmed source phenomena/interventions distinct from read/editorial text.
6. **Project-local `63r-L05–L11` Source Research — COMPLETE.** Direct visual inspection of image 135 supplied diplomatic coverage for all seven physical lines in `transcription/135.tsv`, commit `74ff4be9266e791bdb2ef4a925f6b51a03455a7a`. `63r-L05`, `L09` and `L10` remain `working`; the open points are `Beuelh` (especially final `lh`), `fellig`, and exact graphematic security of `xlvij`. No chronological normalization or identification was performed.
7. **Senior/specialist review:** not globally triggered. If `63r-L10 xlvij` later becomes consequential as a chronological claim, route that exact graphematic reading for bounded Senior Scholarly Review before interpreting it as a year; no such interpretation is currently canonical.

Positive non-results remain first-class: D001–D011 decision/history semantics are materially useful; unresolved W1–W6, deleted wording, fine localization and hand identity remain scholarly uncertainty/research rather than automatic system defects; no demonstrated target-text consequence follows from 63r show-through.

## Parallel active work

### A. GOV-M4 synthesis — #25 / #64

Use only the three bounded capability candidates above as the G2-specific synthesis input. Determine the smallest adequate representation/enforcement/acceptance fixtures without reopening abstract architecture.

**No Dev implementation is authorized merely by the completed Domain Review or by the completed `63r-L05–L11` transcription.** Existing D-016 / `methodology/maintenance.md` admission remains authoritative for material change.

### B. Project-local 63r completion — COMPLETE / return to #64

The prior staging path `#68 → #85 → #72` has now produced its intended execution result for this fixture: image 135 was present and visually inspectable in the target Source Research context, `63r-L05–L11` was directly inspected, and the seven-line diplomatic first pass is persisted in `transcription/135.tsv`.

Do not restart #72 merely to repeat this completed task. The three `working` readings remain valid research states. Escalate only if a later consequential use requires stronger adjudication.

### C. Deterministic assurance — #86

#86 owns the planning/falsification of generic work-context assurance: sticky prerequisites, invalidation events, execution cursor, progress/delta checks, circuit breaking, Issue/Handoff contracts, cross-role hard reviews and canonical-state freshness. The completed #85→#72 target-context fixture may now be consumed as evidence. #86 is not the scholarly NEXT ACTION and does not authorize a workflow engine.

## NEXT ACTION — canonical restart point

There is no remaining #73 execution step for the completed Checkpoint-B fixture and no remaining `63r-L05–L11` execution step for #72.

Current paths:

1. **#64 / #25:** consume the completed project-local 63r return and continue bounded GOV-M4 synthesis from the three confirmed capability candidates; do not infer schema or Dev admission.
2. **Consequence-driven scholarly review only if triggered:** if `63r-L10 xlvij` is later used as chronological evidence, first obtain bounded Senior Scholarly Review of the graphematic reading; do not infer `1547` or another normalized year from the current working transcription alone.
3. **#86:** consume the completed target-context staging/execution fixture together with the prior loop/STATUS-drift fixtures to test the smallest generic deterministic assurance actually justified. Do not prebuild a workflow engine.

Exact parent-PDF repository preservation may proceed independently under #68 and must not displace these active paths.

## Human-in-the-loop / authority state

The non-specialist human owner is not required to perform Source Research, Domain Review, repository routing or technical troubleshooting. Human-owner authority remains reserved for research purpose/priorities, unresolved rights/authority facts, new project/scope, consequential publication/use, material implementation admission and Governing Objective amendment.

AI-assisted Source Research and Domain Review remain distinct from independent qualified specialist validation. Technical/CI PASS does not establish scholarly or specialist PASS.

## Restartability test

A fresh capable context must be able to reconstruct without old chat:

- project/source identity and current G2 scope;
- exact evidence identity/provenance and the distinction `retrievable ≠ staged ≠ vision-inspectable`, plus the derived `VISUAL EVIDENCE READY` gate;
- Checkpoint A PASS, Checkpoint B COMPLETE and Domain Review COMPLETE;
- the three bounded GOV-M4 synthesis candidates and the absence of a new REQ-* gap;
- project-local `63r-L05–L11` Source Research COMPLETE with its three retained `working` readings;
- the fact that the successful image-135 staging/vision PASS was context-bound to the completed #72 execution and must not be generalized to future contexts;
- the current #64/#25 synthesis path and consequence-driven scholarly-review trigger;
- the exact current NEXT ACTION.

Durable restart pointers:

- Source/File/provenance → `corpus/files.tsv` + Source crosswalk;
- baseline derivation → `research/g2-baseline-provenance.md`;
- Checkpoint A → `research/g2-checkpoint-a-physical-inventory.md`;
- Checkpoint B → `research/g2-checkpoint-b-semantic-loss.md`;
- Domain Review → `research/g2-domain-review-checkpoint-b.md`;
- completed image-135 diplomatic coverage → `transcription/135.tsv`;
- concrete target-context staging fixture → #85 under #68;
- generic availability workflow → #78;
- work-context/handoff semantics → #77;
- deterministic assurance planning → #86;
- current project cursor → this `STATUS.md`.
