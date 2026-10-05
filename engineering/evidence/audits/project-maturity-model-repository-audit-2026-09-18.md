# Project maturity model — repository truth/completeness audit — 2026-09-18

Status: **VALID ANALYTICAL / AUDIT EVIDENCE ONLY — NOT AN ACTIVE PROGRAMME CURSOR.** This file is not normative METHOD, not a new gate owner, not a new Project priority, not a schema admission and not authority to change Project state.

**Current programme disposition:** the audit's multidimensional findings remain valid foundations for any future maturity/progress view. Its statement that further work under #225 is supported does **not** make that branch a prerequisite or current next action. See `requirements/human-need-maturity-progress-reconstruction-2026-09-18.md` §18 for the non-blocking disposition.

Repository baseline reviewed: `main@5fe70f641d359e65dd5a85314e01ed810b1c97d6`.

Parent system context: #225.

## 1. Audit question

Audit the proposed maturity model from the 2026-09-18 ChatGPT discussion against the current repository for:

1. **truth** — does the model faithfully represent the current authoritative method, gate semantics, authority boundaries and actual Project state?
2. **completeness** — does it cover the scholarly, epistemic, specialist, data, technical, AI/HITL, human-usability and workflow qualities the repository already requires?
3. **operational safety** — could it be used without laundering technical preparedness into scholarly maturity or gate order into research priority?

The audited proposal separated:

- a P0–P7 process view;
- scholarly quality criteria QF1–QF6;
- technological quality criteria QT1–QT9.

## 2. Repository surface reviewed

The audit freshly reviewed the governing/normative surface:

- `GOVERNING_OBJECTIVE.md`;
- `AGENTS.md`;
- `DECISIONS.md`;
- `MILESTONES.md`;
- all current files under `methodology/`:
  - `historical-source-workflow.md`
  - `research-gates.md`
  - `project-lifecycle.md`
  - `source-and-provenance.md`
  - `evidence-policy.md`
  - `transcription-guidelines.md`
  - `quality-and-learning.md`
  - `workflow.md`
  - `ai-governance.md`
  - `maintenance.md`;
- the complete `requirements/domain-requirements.tsv`: **135 requirements across 13 domains**;
- prior cross-project research-framing/system audits and executable-system concept evidence;
- current `project.yml` + `STATUS.md` for Reg. Ii 3, Reg. Ii 4 Bd. II and Reg. Ii 5;
- current executable context surfaces `tools/project_context.py` and `tools/outcome_context.py`;
- current authority/context regressions, especially `tests/test_outcome_context.py` and `tests/test_governance_ownership.py`.

Requirement-domain inventory reviewed:

| Domain | Count |
|---|---:|
| archival science / diplomatics | 11 |
| palaeography / scribal evidence | 10 |
| historical philology / language history / lexicography | 10 |
| scholarly editing / textual criticism | 10 |
| historical source criticism | 11 |
| source-type/domain history | 10 |
| codicology/material manuscript | 10 |
| onomastics/toponymy | 10 |
| historical metrology/numismatics/accounting | 10 |
| research-data stewardship / GWP | 11 |
| research software/data engineering | 10 |
| AI engineering / HITL | 10 |
| human research usability | 12 |

## 3. Executive verdict

### 3.1 Core idea — correct

The proposal's central correction is **true and strongly supported**:

> Process/activity, scholarly maturity and technical/system quality must not be collapsed into one score.

This is consistent with:

- METHOD distinction between **S1–S9 activities** and **G1–G6 maturity/acceptance states**;
- gate scope/completion semantics;
- GO precedence of scholarship over support infrastructure;
- explicit `CI PASS != scholarly acceptance`;
- explicit `resource_state != task_authority`;
- Project authority and current-target rules.

### 3.2 P0–P7 pipeline — useful as a human view, but not correct as a canonical maturity model

The proposed P0–P7 chain is **not itself a repository-owned pipeline** and is too linear if used as truth.

The current repository says:

- S1–S9 are scholarly activities/methods;
- G1–G6 are maturity states;
- their relationship is typical, **not a rigid waterfall**;
- later evidence may reopen earlier gates;
- some S6/S7 enrichment/interpretation may legitimately occur during earlier source work if epistemic layers remain separate;
- gate state never selects priority;
- Source/File intake can complete with `CORPUS_ONLY / NO_PROJECT_YET`.

Therefore P-labels may be used only as a derived explanatory/navigation view, never as replacement owners for S/G semantics.

### 3.3 Single “Project maturity” — false / unsafe

A single Project maturity value is incompatible with current METHOD.

Every gate claim is **scope-bound**. One Project may simultaneously contain:

- one locus at G4;
- another Source group with only provenance/crosswalk preparation;
- historical completed work;
- no currently authorized scholarly scope.

Accordingly, maturity belongs to:

```text
Project
+ authorized/evaluated scholarly outcome or target
+ bounded scope/locus/source group
→ gate/activity/quality profile
```

The Project-level view may aggregate those profiles, but may not flatten them into one maturity number.

This is the main reason the earlier description of Reg. Ii 3 sounded falsely “advanced”.

### 3.4 Scholarly QF1–QF6 — directionally useful, materially incomplete

The six proposed scholarly criteria roughly follow G1–G6, but they omit or hide cross-cutting requirements that the repository treats as first-class:

- Human-Owner purpose / Project authority / research framing before gate work;
- evidence status and exact inspection level;
- observation→reading→normalization→identification→interpretation separation;
- independence of corroborating evidence;
- dynamically activated disciplinary adequacy;
- specialist-validation status;
- claim-to-evidence auditability;
- rights/access and target-context inspectability;
- source-relationship/transmission evidence;
- explicit residual uncertainty/evidence ceilings;
- scope-dependent codicological, onomastic, metrological/accounting and source-type-domain requirements;
- publication consequence scaling.

A G-number alone cannot certify those qualities outside the exact gate claim and evaluated scope.

### 3.5 Technological QT1–QT9 — substantially aligned, still incomplete

The proposed QT criteria map well to current GWP/RSE/AI/UX requirements, especially:

- one canonical owner;
- provenance/referential integrity;
- reproducible derived views;
- restartability;
- deterministic checks;
- human usability;
- AI/Human/specialist boundaries;
- reviewability;
- lean/portable architecture.

But a complete system-quality profile must additionally expose:

- **semantic-boundary preservation** across scholarly/technical/human language (D-019 / REQ-GWP-011);
- **evidence readiness versus identity/preservation/reproducibility**;
- **rights/confidentiality/external-AI constraints**;
- **AI provenance** for consequential use;
- **representative evaluation** if scaled AI/HTR becomes a research method;
- **write-class/authority boundaries**;
- **migration/semantic-loss and reversibility checks**;
- **technical assurance vs scholarly adequacy vs specialist validation as separate statuses**;
- **goal alignment / support-drift / outcome-continuity**;
- **fresh-context challengeability**, not only restartability;
- **performance/dependency justification against observed workload**.

## 4. Audit of the proposed P0–P7 process view

| Proposed phase | Repository truth | Audit disposition |
|---|---|---|
| P0 Intake / Routing | Real and strongly owned by source/provenance + intake workflow; may end Corpus-only. File identity, Source identity, evidence access and Project routing are distinct. | **SUPPORTED as derived pre-Project/execution view**, but “complete” must not imply research-ready access or scholarly maturity. |
| P1 Research object / question / bounded scope | Real requirement, but authority/framing is not merely the next technical phase. Project existence/purpose/material priority is Human-owned; candidate directions may be formed before selection. | **SUPPORTED but under-specified.** Must explicitly separate Project purpose, candidate direction, authorized scope/outcome and current work target. |
| P2 S1/S2 → G1 | Typical relation, but G1 has its own evidence-based requirements and is scope-bound. S2 contributes only as relevant. | **PARTIAL.** Do not equate activity completion with gate attainment. |
| P3 S2/S3 → G2 | Typical relation is correct. G2 also requires complete physical representation for the evaluated scope, source phenomena/uncertainty and a human-readable derived witness. | **MOSTLY TRUE, incomplete if reduced to “transcription done”.** |
| P4 S4 → G3 | Strong mapping. G3 means every consequential uncertainty has an internal evidential test or explicit unresolved result, not that every reading is solved. | **TRUE with residual-uncertainty qualification.** |
| P5 S5 → G4 | Strong mapping. Requires independent witness/control establishment, explicit correspondence/divergence and evidence-bounded transmission claims. | **TRUE with witness-independence qualification.** |
| P6 S6+S7+S8 → G5 | Repository gives this as a typical relation, but these are three distinct scholarly operations: enrichment/identification, historical source criticism, and critical consolidation/validation. They may iterate with earlier activities. | **TOO COARSE. Must not become one opaque “consolidation phase”.** |
| P7 S9 → G6 | Typical mapping is correct, but G6 also requires an explicit edition concept, transparent intervention/apparatus policy, quality control, traceability and consequence-scaled review. | **TRUE but incomplete as “render/publication”.** |

Additional lifecycle truth absent from P0–P7:

- gates can be reopened;
- Projects can become inactive/closed yet remain provenance packages;
- evidence/resource changes can affect one action without reprioritizing the Project;
- local support/technical work is not a scholarly phase;
- a valid terminal outcome may be a bounded evidence ceiling or specialist/authority dependency, not progression to the next gate.

## 5. Audit of proposed scholarly-quality criteria

### QF1 Provenance/source basis

**Truth:** strongly supported by G1, archival requirements, source/provenance and evidence policy.

**Missing:** Project authority and evaluated investigation scope; exact inspection/evidence status; Source relationships; rights/preservation/access distinctions; completeness/search boundaries.

**Disposition:** retain only as a **scope-specific Source/Evidence Basis** dimension, not general Project maturity.

### QF2 Representation completeness

**Truth:** strongly supported by G2 and transcription guidelines.

**Missing:** physical/documentary structure, reading order, source phenomena, uncertainty/intervention visibility, human-readable derived view, no hidden normalization.

**Disposition:** retain with full G2 semantics.

### QF3 Internal evidence analysis

**Truth:** strongly supported by G3/S4.

**Missing if too compressed:** exact palaeographic anchors; distinction of same Source vs same hand; philological evidence after graphematic stabilization; special notation/sign systems; alternatives/rejected readings; explicit specialist trigger.

**Disposition:** retain but treat as **internal-analysis adequacy**, not reading-resolution percentage.

### QF4 Controlled comparison

**Truth:** strongly supported by G4/S5.

**Missing:** witness independence, exact relationship/correspondence claim status, non-copying of clearer witness into principal witness, genuine independence of corroboration.

**Disposition:** retain with textual-critical/source-critical independence criteria.

### QF5 Critical consolidation

**Truth:** G5 exists and is central.

**Problem:** one QF5 bucket hides S6, S7 and S8:
- normalized/identified/enriched claims;
- historical source criticism and interpretation;
- consolidation, adversarial falsification, provenance/decision audit and validation.

**Disposition:** split the quality view even if gate remains G5. G5 is the acceptance state; S6/S7/S8 coverage must remain visible underneath it.

### QF6 Edition/usability

**Truth:** G6/S9.

**Missing:** edition concept before final rendering; intended audience/purpose; intervention/apparatus conventions; source/transmission note; publication/data/preservation/interoperability requirements; independent review proportional to consequence.

**Disposition:** retain with full G6/S9 acceptance.

## 6. Missing scholarly quality dimensions not safely represented by QF1–QF6

A complete maturity/quality profile needs cross-cutting dimensions in addition to gate state.

### SQ-A — Authority / research framing

Questions:

- Does the Project exist by Human authority?
- What is the Project purpose/research object?
- Is there an authorized current outcome/scope?
- Is there only a candidate research direction?
- Is there a current bounded research question/work target?

This must be visible **before** gate interpretation.

### SQ-B — Epistemic integrity

Minimum checks from GO/quality/evidence:

- evidence actually inspected at the level claimed;
- claim-layer separation preserved;
- uncertainty remains valid;
- corroboration independence assessed;
- AI/model output not treated as evidence;
- changed durable truth persisted.

### SQ-C — Disciplinary adequacy / competence activation

The repository has 9 scholarly/specialist domain families beyond generic editing/source work. Applicability is source/question/claim-relative.

A profile must answer not “were all disciplines used?” but:

> Were all **applicable** disciplinary requirements activated, and were irrelevant ones correctly not activated?

### SQ-D — Specialist / validation state

Keep distinct:

- AI-assisted/method-compliant;
- scholarly adequacy review;
- qualified specialist validation;
- Human-Owner acceptance where governance requires it.

No generic PASS may collapse these.

### SQ-E — Outcome usefulness / evidence ceiling

The profile must express:

- usable result achieved for intended outcome;
- valid work remains;
- bounded evidence ceiling;
- specialist dependency;
- Human-authority decision required.

This is not identical to gate state.

## 7. Complete system/technology quality profile required by the repo

Rather than a single “technology maturity”, the current requirements support at least these cross-cutting assurance families.

### TQ-A — Canonical ownership / data integrity

Owners: GWP/RSE/Source Contract.

Checks:
- one durable fact/state owner;
- derived views explicitly derived/rebuildable;
- stable IDs/references;
- no parallel manual truth;
- migration preserves semantics/history.

### TQ-B — Provenance / reproducibility / evidence access

Checks:
- exact Source/File/locus recoverable;
- checksum and mappings;
- preservation/reproducibility distinguished from target-context inspectability;
- rights/access state explicit;
- transformations/derivatives retain parent provenance.

### TQ-C — Deterministic assurance / software quality

Checks:
- stable failure classes executable where justified;
- transformations tested/reversible enough;
- components trace to demonstrated scholarly requirements/failures;
- dependencies/performance proportional to observed workload;
- technical PASS declares its certification boundary.

### TQ-D — AI/HITL integrity

Checks:
- complete applicable context assembled;
- AI output ≠ evidence/independent validation;
- consequential AI provenance;
- write/authority class visible;
- unresolved alternatives preserved;
- scaled AI/HTR evaluated on representative source tasks if triggered.

### TQ-E — Human usability / auditability

Checks:
- source/result/locus reachable without repository expertise;
- human-readable source-order witness;
- uncertainty/intervention visible;
- drill-down result→evidence→decision;
- specialist review status visible;
- Human Owner not used as repository operator/substitute specialist;
- consequential actions explainable/challengeable in ordinary language.

### TQ-F — Semantic-boundary integrity

Checks:
- domain↔domain / Domain↔Dev / machine↔human / language translation preserves owning meaning;
- technical `PASS/complete/status/owner/source/evidence` words do not acquire stronger scholarly meaning;
- unresolved/non-lossless mapping remains unresolved.

### TQ-G — Workflow / restart / goal alignment

Checks:
- current work target has authority;
- resource state does not create roadmap authority;
- sticky prerequisites invalidate only on evidence;
- support work does not displace first scholarly action;
- local PASS remains local;
- repair returns to higher outcome cursor;
- fresh context reconstructs role/stage/cursor/evidence/next legitimate decision;
- no-progress loops terminate/redirect.

### TQ-H — Responsible access / platform constraints

Checks:
- rights/licensing/confidentiality/sensitive-data constraints;
- external-AI use compatible with authority;
- public repository visibility ≠ redistribution authority;
- preservation/storage state does not imply legal permission.

## 8. Corrected maturity model supported by the repository

The audit supports a **multi-layer profile**, not one ladder/score.

### Layer 1 — Project authority / framing state

Recommended derived meanings, not new canonical enum:

```text
PROJECT EXISTS?              yes | no
PROJECT PURPOSE              canonical owner reference
CURRENT AUTHORIZED OUTCOME   present | absent | Human decision required
CURRENT BOUNDED SCOPE        present | absent
CURRENT RESEARCH QUESTION    present | candidate-only | absent
CURRENT WORK TARGET          authorized | absent
```

Candidate directions may be generated under the narrow pre-priority framing rule, but they do not become scope/NEXT ACTION.

### Layer 2 — Evidence / resource readiness

Keep separate:

```text
identity established
provenance established
exact File established
crosswalk/locus established
preservation/bytes state
retrievable now
staged now
vision/source-inspectable now
rights/authority state
```

These are prerequisites/resources, not scholarly maturity.

### Layer 3 — Scholarly activity coverage

Use the canonical S1–S9 activities directly.

For each applicable activity, a derived profile may expose:

```text
not activated
active
sufficient for current gate/outcome
residual uncertainty explicit
specialist dependency
reopened
not applicable to current question
```

These are explanatory meanings; no new status vocabulary should become canonical without separate admission.

### Layer 4 — Scholarly maturity

Use canonical G1–G6 **per evaluated scope**:

```text
<scope A>: G1 reached / G2 reached / G3 ... / G4 ... / G5 ... / G6 ...
<scope B>: not evaluated
```

Never flatten to one Project G-number unless only one explicitly declared evaluated scope exists and the aggregation meaning is unambiguous.

### Layer 5 — Cross-cutting quality/assurance profile

Expose separately:

```text
EPISTEMIC INTEGRITY
DISCIPLINARY ADEQUACY
SPECIALIST VALIDATION
DATA/PROVENANCE/REPRODUCIBILITY
TECHNICAL ASSURANCE
AI/HITL INTEGRITY
HUMAN USABILITY/AUDITABILITY
SEMANTIC-BOUNDARY INTEGRITY
WORKFLOW/RESTART/GOAL ALIGNMENT
RIGHTS/ACCESS RESPONSIBILITY
```

Not every dimension needs a numeric score. Evidence-bearing state + exact gap is more faithful than pseudo-precision.

### Layer 6 — Candidate transitions / next outcomes

Derive **options**, not priority.

Each candidate should state:

- desired outcome it would serve;
- current evaluated scope or required new scope;
- unmet gate/requirement(s);
- applicable competence(s);
- evidence/resource prerequisites;
- specialist/Human decision boundary;
- likely scholarly value;
- evidence ceiling/falsifier;
- whether it is compatible with current Project purpose.

If no current scope is authorized, the system may form evidence-grounded candidate directions **only when a real direction decision is needed**, under the pre-priority framing rule. It must not auto-rank or activate them.

## 9. Project sanity check

### 9.1 Reg. Ii 3

Repository truth:

- Human-defined act-level Project exists.
- Two internal Source groups and exact File/provenance/crosswalk state are substantially documented.
- `source-uses.tsv` is intentionally empty.
- no owner-selected bounded scholarly target is active;
- no current G1–G6 progression/claim is asserted;
- no current manuscript/source-research NEXT ACTION is recorded.

Correct maturity reading:

```text
PROJECT AUTHORITY: established
CURRENT SCHOLARLY OUTCOME/SCOPE: absent
CORPUS/INTAKE PREPARATION: substantial for known Source/File mappings
CURRENT SCHOLARLY ACTIVITY: not activated
G1–G6: NOT EVALUATED for a current bounded research target
SCIENTIFIC MATURITY: cannot be promoted from crosswalk/File readiness
```

Important correction to the earlier ChatGPT model:

> Reg. Ii 3 is **not “scientifically mature but idle.”** It is structurally/provenance-prepared in several respects while current bounded scholarly research is essentially unactivated.

Even “technical preparation complete” would be too strong if it implied current research-ready access: the repository explicitly distinguishes identity/preservation/reproducibility from current-context inspectability.

### 9.2 Reg. Ii 4 Bd. II

Repository truth for the historical bounded Knau scope fol. 306v–309r:

- G1 reached;
- G2 reached;
- G3 reached at current internal evidence level;
- G4 reached against Reg. Ii 5 fol. 61v–63r;
- residual readings/signs explicitly unresolved;
- G5 not reached;
- G6 not reached;
- no current owner-selected active scholarly scope.

Correct profile:

```text
PROJECT AUTHORITY: established
CURRENT ACTIVE SCOPE: absent
HISTORICAL EVALUATED SCOPE: fol. 306v–309r
MATURITY OF THAT SCOPE: G1–G4 reached; G5/G6 not reached
RESIDUAL UNCERTAINTY: explicit
NEXT PRIORITY: not derivable from gate order
```

### 9.3 Reg. Ii 5

Repository truth for bounded fol. 61v–63r:

- G1 reached;
- G2 reached;
- G3 reached at current internal evidence level;
- G4 reached against Reg. Ii 4;
- substantial completed source-understanding and relation/function work;
- local result includes `SCHOLARLY DELTA + BOUNDED SCHOLARLY EVIDENCE CEILING`;
- G5/G6 not reached;
- no current owner-selected active scholarly scope;
- legacy diplomatic material remains explicitly non-canonical/recovery-only.

Correct profile:

```text
PROJECT AUTHORITY: established
CURRENT ACTIVE SCOPE: absent
HISTORICAL EVALUATED SCOPE: fol. 61v–63r
MATURITY OF THAT SCOPE: G1–G4 reached; G5/G6 not reached
LOCAL EVIDENCE CEILINGS: explicit
LEGACY-PROVENANCE CAVEAT: explicit
NEXT PRIORITY: not derivable from unresolved items or G5 availability
```

## 10. Executable support audit

### Already executable / deterministic

Current repository can already derive or validate substantial parts of Layers 1–2 and system assurance:

- Source/File/Project structure and referential integrity;
- exact File/checksum/provenance relationships;
- Source ancestry/internal/external status after Project selection;
- Project context assembly;
- explicit no-Project state;
- explicit canonical “no owner-selected current outcome” state;
- selected Requirement metadata including domain/validation/specialist trigger;
- deterministic negative rule: no automatic NEXT ACTION;
- local technical/task PASS cannot become whole-outcome completion;
- broad regression assurance over known failure classes.

### Not currently generic/executable

There is currently **no generic maturity-profile compiler** that safely derives:

- structured current S1–S9 coverage;
- structured G1–G6 profile from heterogeneous Project STATUS owners;
- outcome-specific unmet requirements;
- full cross-cutting quality/assurance profile;
- candidate next scholarly directions from maturity/evidence without inventing priority.

`tools/outcome_context.py` intentionally requires Requirement IDs to be selected upstream and does not infer open applicability or scholarly maturity.

This means the corrected model is **repository-supported conceptually**, but not yet operationally available as a deterministic portfolio view.

## 11. Completeness verdict on the original proposal

| Part | Truth | Completeness | Safe to operationalize unchanged? |
|---|---|---|---|
| separate process / scholarly / technical dimensions | strong | medium | **No — needs scope/authority/quality layers** |
| P0–P7 process ladder | medium | low-medium | **No** |
| QF1–QF6 | medium-high mapping to gates | medium | **No — misses cross-cutting epistemic/domain/specialist dimensions** |
| QT1–QT9 | high directional fit | medium-high | **No — misses semantic, AI provenance/eval, access, workflow-certification boundaries** |
| one Project maturity statement | low / unsafe | low | **No** |
| scope-specific G1–G6 maturity | strong | high within gate semantics | **Yes, if exact scope remains visible** |
| maturity-derived next-step candidates | conceptually supported | partial operational support | **Yes only as proposals, with authority boundary and no auto-priority** |

## 12. Audit conclusion

The repository already contains a much more rigorous maturity theory than the earlier conversational model implied.

The correct system abstraction is not:

```text
Project → one phase → one maturity score → next step
```

It is:

```text
PROJECT AUTHORITY / PURPOSE
        ↓
CURRENT OUTCOME / SCOPE AUTHORITY
        ↓
EVIDENCE + RESOURCE READINESS
        ↓
APPLICABLE S1–S9 ACTIVITY COVERAGE
        ↓
SCOPE-BOUND G1–G6 MATURITY
        +
CROSS-CUTTING SCHOLARLY / SPECIALIST / DATA / TECHNICAL / AI / UX / WORKFLOW QUALITY
        ↓
OUTCOME-SPECIFIC UNMET REQUIREMENTS
        ↓
CANDIDATE TRANSITIONS / DIRECTIONS
        ↓
Human selection only where purpose/priority is genuinely non-derivable
```

### Main correction

**Infrastructure maturity must never visually or numerically compensate for absent scholarly maturity.**

Reg. Ii 3 is the decisive fixture: substantial Source/File/crosswalk/restart preparation coexists with **no currently activated bounded scholarly target and no G1–G6 maturity claim**.

### Main completeness addition

A faithful Project portfolio view must make at least four things simultaneously visible:

1. **authority/framing state**;
2. **scope-specific scholarly maturity**;
3. **cross-cutting quality/assurance state**;
4. **candidate next outcomes/transitions without implied authorization**.

### System consequence

The audit supports further work under #225 on a **derived, scope-bound Project Maturity Profile**, but **not** by simply adding P0–P7 or a numeric maturity score to C1R.

Before implementation, the exact derived semantics must be reconciled against existing STATUS/gate owners and the D-016 boundary. In particular, a future design must decide whether safe maturity derivation can be achieved from current canonical owners or whether any stable machine-readable gate/profile representation is genuinely warranted. This audit does not make that material design decision.
