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

The project now distinguishes three different states:

```text
RETRIEVABLE       an authorized tool/path can recover bytes
STAGED            the required evidence object is present in the target work context
VISION-INSPECTABLE the target Source Research context can actually inspect the pixels
```

Historical #84 testing established exact evidence identity and a private attachment retrieval route, but later fresh-context execution showed that this does **not** imply that a new Source Research context already has a staged, vision-inspectable image.

Current state:

```text
exact parent identity / SHA                                  PASS
canonical folio↔image↔PDF mapping                           PASS
reproducible baseline derivation                            PASS
controlled private storage authority                        PASS
private #84 baseline attachments present                    PASS
historical private-attachment retrievability                PASS / evidenced
image 135 staged in the next target #72 context             PENDING — owned by #85/#68
image 135 vision-inspectable in that target #72 context     PENDING — required before #72 resumes
exact parent binary committed + SHA reverified in repo       PENDING — preservation only
```

Do not translate historical retrieval success into `EVIDENCE STAGED` for another chat/context. For visual Source Research the executable gate is the actual evidence object already present and inspectable in that target context.

## Generic gate state

- **G1 — Source and transmission basis secured:** substantially reached for identity, provenance and controlled use; parent-binary preservation remains separately pending.
- **G2 — Principal witness completely and diplomatically represented:** **ACTIVE — not reached.** Checkpoint A, Checkpoint B and the bounded Checkpoint-B Domain Review are complete. Project-local completion of `63r-L05–L11` remains open, and GOV-M4 synthesis has not yet admitted a final implementation.
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
6. **Project-local remaining Source Research:** `63r-L05–L11` is validated physical text without current `135.tsv` coverage. This is research completion, not independent evidence of a system gap.
7. **Specialist review:** not globally triggered; difficult consequential scholarly cases remain consequence-driven.

Positive non-results remain first-class: D001–D011 decision/history semantics are materially useful; unresolved W1–W6, deleted wording, fine localization and hand identity remain scholarly uncertainty/research rather than automatic system defects; no demonstrated target-text consequence follows from 63r show-through.

## Parallel active work

### A. GOV-M4 synthesis — #25 / #64

Use only the three bounded capability candidates above as the G2-specific synthesis input. Determine the smallest adequate representation/enforcement/acceptance fixtures without reopening abstract architecture.

**No Dev implementation is authorized merely by the completed Domain Review.** Existing D-016 / `methodology/maintenance.md` admission remains authoritative for material change.

### B. Project-local 63r completion — #68 → #85 → #72

The next visual Source Research action is blocked only on target-context evidence staging:

```text
#68 evidence-availability owner
→ #85 concrete staging/feasibility task
→ actual image 135 present in target context
→ VISION-INSPECTABLE
→ EVIDENCE STAGED = PASS
→ #72 Source Research resumes directly at 63r-L05
→ complete through 63r-L11
→ persist result
→ return to #64
```

Until #85 demonstrates target-context staging PASS, or image 135 is directly provided to that Source Research conversation, do **not** start another #72 context with instructions to discover/retrieve the image from #84. Evidence discovery/retrieval mechanics are upstream technical work, not Source Research.

### C. Deterministic assurance — #86

#86 owns the planning/falsification of generic work-context assurance: sticky prerequisites, invalidation events, execution cursor, progress/delta checks, circuit breaking, Issue/Handoff contracts, cross-role hard reviews and canonical-state freshness. It is **not** an implemented workflow framework and is not the scholarly NEXT ACTION.

## NEXT ACTION — canonical restart point

There is no remaining #73 execution step for the completed Checkpoint-B fixture.

Run the two admitted parallel paths without conflating them:

1. **#25/#64:** continue bounded GOV-M4 synthesis from the three confirmed capability candidates; do not infer schema or Dev admission.
2. **#85 under #68/#74:** execute capability/feasibility testing for one-shot staging of fol. 63r / image 135 into a fresh Source Research target context. Prefer existing connector mechanics; use a tiny helper only if it materially crosses the real boundary; otherwise record the platform/orchestrator boundary instead of building dead repo infrastructure.
3. **After target-context `EVIDENCE STAGED = PASS`: #72** resumes only the scholarly task `63r-L05–L11`, persists it, and returns to #64.
4. **#86:** consume #85 and the prior loop/STATUS-drift fixtures to determine the smallest generic deterministic assurance actually justified. Do not prebuild a workflow engine.

Exact parent-PDF repository preservation may proceed independently under #68 and must not displace these active paths.

## Human-in-the-loop / authority state

The non-specialist human owner is not required to perform Source Research, Domain Review, repository routing or technical troubleshooting. Human-owner authority remains reserved for research purpose/priorities, unresolved rights/authority facts, new project/scope, consequential publication/use, material implementation admission and Governing Objective amendment.

AI-assisted Source Research and Domain Review remain distinct from independent qualified specialist validation. Technical/CI PASS does not establish scholarly or specialist PASS.

## Restartability test

A fresh capable context must be able to reconstruct without old chat:

- project/source identity and current G2 scope;
- exact evidence identity/provenance and the distinction `retrievable ≠ staged ≠ vision-inspectable`;
- Checkpoint A PASS, Checkpoint B COMPLETE and Domain Review COMPLETE;
- the three bounded GOV-M4 synthesis candidates and the absence of a new REQ-* gap;
- the remaining project-local `63r-L05–L11` task and its #85 staging prerequisite;
- the two parallel active paths and their authority boundaries;
- the exact current NEXT ACTION.

Durable restart pointers:

- Source/File/provenance → `corpus/files.tsv` + Source crosswalk;
- baseline derivation → `research/g2-baseline-provenance.md`;
- Checkpoint A → `research/g2-checkpoint-a-physical-inventory.md`;
- Checkpoint B → `research/g2-checkpoint-b-semantic-loss.md`;
- Domain Review → `research/g2-domain-review-checkpoint-b.md`;
- concrete target-context staging → #85 under #68;
- generic availability workflow → #78;
- work-context/handoff semantics → #77;
- deterministic assurance planning → #86;
- current project cursor → this `STATUS.md`.
