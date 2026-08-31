# STATUS — ThHStAW, EGA, Reg. Ii 5

Last checkpoint: 2026-08-31

## Historical project root

This project is anchored to the historically independent source structure `ACT-THHSTAW-EGA-REG-II-5` — *Registratur für die Superintendenz Neustadt an der Orla (Auszug)* — via `project.yml: project_source_id`.

The current Knau work is a bounded research scope inside that project root; it does not define the project boundary. The project root is a structural anchor, not a selector of current research priority.

Generic scholarly method is defined in `../../methodology/historical-source-workflow.md`; reusable maturity requirements are in `../../methodology/research-gates.md`; diplomatic requirements are in `../../methodology/transcription-guidelines.md`.

## Research purpose and active scope

Produce a source-exact, critically controlled scholarly edition and historical understanding of the relevant material within Reg. Ii 5 while using separately preserved related witnesses and controls where the research requires them.

**Owner-grounded priority correction, 2026-08-31:** the original comparison-material strand began from the supplied Reg. Ii 4 Bd. II material. Later Reg. Ii 5 uploads were repeatedly requested by the assistant to establish exact provenance and to execute the bounded G2/architecture fixture. Those later valid Reg. Ii 5 evidence tasks do **not** themselves evidence an owner-approved replacement of the comparison strand as the current scholarly priority.

The current scholarly work target is therefore the already inspected Reg. Ii 4 Bd. II Knau locus, fol. 306v–309r / export images 667–672, for detailed local comparison/collation against the completed Reg. Ii 5 principal locus fol. 61v–63r. Preserve both witnesses independently. Reg. Ii 5 remains the internal principal witness and valid completed G2 fixture; Reg. Ii 4 remains an external comparison source. Current work priority does not alter either research function.

## Sources used

The project uses four canonical protocol/source records. Structural membership is derived from `corpus/relationships.tsv` `part_of` relations, not from project roles or current work priority.

- **internal / principal** — `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`: *Visitation im Amt Ziegenrück*, fol. 55v–66v, structurally inside `ACT-THHSTAW-EGA-REG-II-5`. Principal Knau locus: fol. 61v–63r / export images 132–135.
- **external / comparison** — `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089`: *Visitation im Amt Ziegenrück*, fol. 294r–313r, structurally inside `ACT-THHSTAW-EGA-REG-II-4-BD-II`. Corresponding Knau locus: fol. 306v–309r / export images 667–672. This is the current scholarly work target without becoming the principal witness.
- **external / context** — `THHSTAW-EGA-REG-II-3-PROT-NEUSTADT-41R-63V`: *Visitation in Neustadt an der Orla*, fol. 41r–63v, structurally inside `ACT-THHSTAW-EGA-REG-II-3`.
- **external / control** — `THHSTAW-EGA-REG-II-3-STAT-VIS-00000235`: *Pfarreinkommen Gössitz, Knau (mit Laskau, Bahren), Liebschütz (mit Liebengrün)*, fol. 303r–306r, structurally inside the same Reg. Ii 3 act.

## Digital addressing / provenance state

For the principal Reg. Ii 5 source, folio↔export-image↔PDF-page mapping is canonical. Stable per-image URNs are **not established** and must not be inferred. Directly observed provider derivative/TIFF labels for the active slice are recorded in the Source crosswalk. The exact parent File is `FILE-REG-II-5-00000129-EXCERPT`; provider file object `stat_file_00000033` remains distinct from Source/provider record `stat_visitation_00000129`.

For the Reg. Ii 4 Bd. II comparison source, the corresponding Knau locus has already been located at fol. 306v–309r / export images 667–672 from the uploaded archive export and is recorded in `research/source-audit.tsv` R002. Its detailed local collation remains the current scholarly action.

For the completed Reg. Ii 5 G2 slice, the exact parent File was SHA-256 verified and unprocessed baselines for fol. 61v–63r were reproduced from canonical PDF pages 14–17 using the persisted Poppler recipe. Durable derivation/recovery provenance is recorded in `research/g2-baseline-provenance.md`.

The canonical private-repository target for the exact Reg. Ii 5 parent remains:

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

Historical #84 testing established exact Reg. Ii 5 evidence identity and a private attachment retrieval route, but that did not imply that a later Source Research context already had a staged, vision-inspectable image. The subsequent bounded #72 execution received image 135 directly in its target context and actually inspected the manuscript pixels.

Current Reg. Ii 5 staging state:

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

These target-context PASS states certify the completed #72 execution only. They must not be inherited automatically by a future chat/context without a new target-context check. They also do not determine which Source is the current scholarly work target.

## Generic gate state

- **G1 — Source and transmission basis secured:** substantially reached for identity, provenance and controlled use; parent-binary preservation remains separately pending.
- **G2 — Principal witness completely and diplomatically represented:** **ACTIVE — not reached.** Checkpoint A, Checkpoint B, the bounded Checkpoint-B Domain Review and the project-local `63r-L05–L11` completion are complete. GOV-M4 synthesis has not yet admitted a final implementation, and this status does not independently assert that all remaining G2 exit conditions are satisfied.
- **G3 — Internal palaeographic and notational analysis completed:** not reached.
- **G4 — Comparison witnesses/controls independently assessed and collated:** not reached. Reg. Ii 4 Bd. II is already independently identified/inspected and its corresponding Knau locus is localized; detailed local collation is the current scholarly work target.
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

## Comparison-source state — Reg. Ii 4 Bd. II

`research/source-audit.tsv` R002 records the Reg. Ii 4 Bd. II Ziegenrück protocol as inspected primary comparison material. Its Knau locus at fol. 306v–309r / export images 667–672 was located and compared structurally with Reg. Ii 5 fol. 61v–63r. The established claim is structural/textual correspondence; verbatim copying, complete line-level equivalence and transferability of individual readings remain explicitly unproven.

The persisted R002 next step is therefore authoritative for the current comparison strand:

> Perform detailed local collation of 306v–309r against Reg. Ii 5, 61v–63r while preserving each witness independently.

This work must not overwrite Reg. Ii 5 readings from a clearer comparison witness. It advances the comparison strand rather than changing Source identity or project root.

## Parallel active work

### A. Scholarly comparison — current work target

Proceed with bounded detailed local comparison/collation of Reg. Ii 4 Bd. II fol. 306v–309r / images 667–672 against Reg. Ii 5 fol. 61v–63r, following `research/source-audit.tsv` R002. Begin from the Reg. Ii 4 witness independently; preserve its own lineation/readings/uncertainty before using correspondences.

### B. GOV-M4 synthesis — #25 / #64, parallel support track

Use only the three bounded capability candidates above as the G2-specific synthesis input. Determine the smallest adequate representation/enforcement/acceptance fixtures without reopening abstract architecture.

**No Dev implementation is authorized merely by the completed Domain Review or by the completed `63r-L05–L11` transcription.** Existing D-016 / `methodology/maintenance.md` admission remains authoritative for material change. This architecture/support track must not displace the owner-grounded scholarly comparison target.

### C. Project-local 63r completion — COMPLETE / returned to #64

The prior staging path `#68 → #85 → #72` produced its intended execution result for this fixture: image 135 was present and visually inspectable in the target Source Research context, `63r-L05–L11` was directly inspected, and the seven-line diplomatic first pass is persisted in `transcription/135.tsv`.

Do not restart #72 merely to repeat this completed task. The three `working` readings remain valid research states. Escalate only if a later consequential use requires stronger adjudication.

### D. Deterministic assurance — #86, parallel support track

#86 owns planning/falsification of generic work-context assurance. It must now also consume the demonstrated priority-routing failure: a fresh/restartable and internally consistent canonical state can still be wrong if its current work target was inferred without owner-grounded authority. #86 is not the scholarly NEXT ACTION and does not authorize a workflow engine.

## NEXT ACTION — canonical restart point

The current scholarly cursor is no longer Reg. Ii 5 evidence acquisition or repetition of #72. It is the comparison strand that was already present and inspected before the later Reg. Ii 5 support work became dominant.

1. **Source Research / comparison:** work independently through Reg. Ii 4 Bd. II Knau fol. 306v–309r / export images 667–672 and perform detailed local collation against Reg. Ii 5 fol. 61v–63r. Preserve witness independence and record agreements/divergences without copying Reg. Ii 4 readings into the Reg. Ii 5 diplomatic text.
2. **#64 / #25, parallel:** consume the completed Reg. Ii 5 G2 fixture for bounded GOV-M4 synthesis; do not let this support/architecture track redefine the current scholarly source target or infer Dev admission.
3. **Consequence-driven scholarly review only if triggered:** if `63r-L10 xlvij` is later used as chronological evidence, first obtain bounded Senior Scholarly Review of the graphematic reading; do not infer `1547` or another normalized year from the current working transcription alone.
4. **#86, parallel:** treat the Reg. Ii 4/Reg. Ii 5 history as an authority-validity fixture: correct File/Source identity + fresh canonical state does not certify correct research priority.

Exact parent-PDF repository preservation may proceed independently under #68 and must not displace the scholarly comparison path.

## Human-in-the-loop / authority state

The non-specialist human owner is not required to perform Source Research, Domain Review, repository routing or technical troubleshooting. Human-owner authority remains reserved for research purpose/priorities, unresolved rights/authority facts, new project/scope, consequential publication/use, material implementation admission and Governing Objective amendment.

The 2026-08-31 owner clarification is now the explicit authority basis for restoring the Reg. Ii 4 comparison strand as current work target. This does not reclassify Reg. Ii 4 as principal and does not invalidate correctly performed Reg. Ii 5 research.

AI-assisted Source Research and Domain Review remain distinct from independent qualified specialist validation. Technical/CI PASS does not establish scholarly, specialist or priority-authority PASS.

## Restartability test

A fresh capable context must be able to reconstruct without old chat:

- project/source identity and structural root;
- the distinction between Source/File identity, structural status, research function and current work priority;
- Reg. Ii 5 remains the internal principal witness and completed G2 fixture;
- Reg. Ii 4 Bd. II remains the external comparison Source and is the current scholarly work target at fol. 306v–309r / images 667–672;
- why the current comparison target was restored: later assistant-requested Reg. Ii 5 support work was valid but did not itself authorize a priority change;
- exact Reg. Ii 5 evidence identity/provenance and the distinction `retrievable ≠ staged ≠ vision-inspectable`, plus the derived `VISUAL EVIDENCE READY` gate;
- Checkpoint A PASS, Checkpoint B COMPLETE and Domain Review COMPLETE;
- the three bounded GOV-M4 synthesis candidates and the absence of a new REQ-* gap;
- project-local `63r-L05–L11` Source Research COMPLETE with its three retained `working` readings;
- the current Reg. Ii 4 detailed-collation cursor and the parallel subordinate #64/#25 and #86 tracks.

Durable restart pointers:

- Source/File/provenance → `corpus/files.tsv` + Source crosswalks;
- Reg. Ii 4 comparison status/current scholarly next step → `research/source-audit.tsv` R002;
- Reg. Ii 5 baseline derivation → `research/g2-baseline-provenance.md`;
- Checkpoint A → `research/g2-checkpoint-a-physical-inventory.md`;
- Checkpoint B → `research/g2-checkpoint-b-semantic-loss.md`;
- Domain Review → `research/g2-domain-review-checkpoint-b.md`;
- completed image-135 diplomatic coverage → `transcription/135.tsv`;
- priority-routing correction → `LEARNINGS.md` L012 + `project.yml: active_scope` + this `STATUS.md`;
- concrete target-context staging fixture → #85 under #68;
- generic intake/routing workflow → #69;
- work-context/handoff semantics → #77;
- deterministic assurance planning → #86;
- current project cursor → this `STATUS.md`.
