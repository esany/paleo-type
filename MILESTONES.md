# Milestones — governance and structural-work sequence

## Purpose

This file defines the **work-sequencing semantics** for repository-wide governance, architecture and structural-change issues.

Milestones are a planning/navigation layer. They do **not** define scholarly truth, project research maturity or evidence status.

The scholarly objective, source evidence, project state and G1–G6 research gates remain canonical in their existing repository owners. GitHub milestone metadata should mirror the sequence defined here; it must never replace those records.

## Core rule

Use milestones only for work that has been **explicitly admitted into an active or approved work sequence**.

> **Issue with milestone = scheduled/active phase work.**  
> **Open issue without milestone = backlog/deferred until its own trigger is met.**

An issue does not enter a milestone merely because it exists, is interesting or has a plausible future benefit.

## Research gates are not milestones

Do not mirror `G1–G6` as GitHub Milestones.

`G1–G6` are scholarly maturity requirements defined in `methodology/research-gates.md` and recorded per project in `STATUS.md`. They may advance, regress or remain partially satisfied according to evidence.

The `M1–M4` sequence below is different: it organizes a bounded governance/architecture review and, only if justified, a later implementation decision.

## Required sequence

```text
M1 Governing Objective & Mission Protection
        ↓
M2 Scholarly Domain Architecture Audit
        ↓
M3 AI, Engineering & Human Usability Audit
        ↓
M4 Structural Synthesis & Refactor Decision
        ↓
M5 Approved Structural Refactor   [conditional; create only if M4 authorizes it]
```

A later phase may begin only when the preceding phase has produced enough documented evidence to satisfy its entry condition. Parallel work inside a milestone is allowed where dependencies permit it.

---

## M1 — Governing Objective & Mission Protection

### Purpose
Establish the repository's highest-order scholarly objective, precedence hierarchy and human change authority before any material structural redesign is evaluated.

### Issues
- `#41` — Canonical governing objective and protection against mission drift.

### Entry condition
Immediate. This is P1 and foundational.

### Required outputs
- one canonical, implementation-independent governing-objective artifact;
- explicit precedence from scholarly objective down to technical implementation;
- explicit human-only authority for material mission changes;
- AI anti-drift rules integrated into relevant governance without duplicating the objective;
- assessment and smallest practical GitHub-native protection for mission changes;
- linkage from future structural audit `#25` back to the governing objective.

### Exit condition
M1 is complete only when `#41` satisfies its acceptance criteria and a future AI/researcher can determine the repository's highest-order mission, precedence and change authority without chat.

### What M1 must not do
- freeze current technical architecture;
- constitutionalize TSV, TEI, RiC, GitHub, a model, G1–G6 or the Knau pilot;
- impose approval ceremony on routine source research.

---

## M2 — Scholarly Domain Architecture Audit

### Purpose
Determine the **scholarly and epistemic requirements** that any future structure must satisfy before software or AI architecture is redesigned.

This milestone asks first what excellent early-modern manuscript/source research requires, not what technology should be used.

### Issues

#### Reference-frame refresh — start first
- `#38` — State of the art, standards and expert-knowledge refresh.

#### Domain reviews — may proceed in parallel once #38 has established the relevant current reference frame
- `#26` — Archival science and diplomatics.
- `#27` — Palaeography and scribal evidence.
- `#28` — Historical philology, language history and lexicography.
- `#29` — Scholarly editing and textual criticism.
- `#30` — Historical source criticism.
- `#31` — Source-type and domain history.
- `#32` — Codicology and material manuscript study.
- `#33` — Onomastics and toponymy.
- `#34` — Historical metrology, numismatics and accounting notation.

#### Cross-domain integrity consolidation
- `#35` — Research-data stewardship and Good Research Practice.

### Entry condition
- M1 complete.
- Governing objective is canonical and controls the audit.

### Internal order
1. **#38 first:** establish then-current standards, disciplinary guidance, high-quality practice and experiential-expertise requirements relevant to the proposed review.
2. **#26–#34:** review the current structure against actual source/research needs and the refreshed professional reference frame. These may run in parallel where independent.
3. **#35:** consolidate provenance, reproducibility, responsibility, review status, rights/access and Good Research Practice implications across the domain findings. It may begin earlier, but its final assessment must incorporate material outputs of the domain reviews.

### Required review result per issue
Record one of:
- `adequate` — current structure already supports the requirement;
- `gap` — a demonstrated requirement is not adequately supported;
- `risk` — current support exists but is fragile or likely to fail under the proposed scope;
- `needs evidence` — insufficient project/source evidence exists to justify structural change;
- `not applicable` — justified for the refactor/source scope being reviewed.

### Required outputs
For each material requirement:

`scholarly requirement → evidence/standard/expert practice → current support → gap/risk/no gap → smallest candidate measure`

Also record:
- dependencies and conflicts between disciplinary requirements;
- where independent specialist review is required rather than AI self-assessment;
- requirements that are source-type-specific and must not become generic framework rules;
- areas where the correct decision is explicitly **no structural change**.

### Exit condition
M2 is complete when all relevant domain issues have documented review outcomes, current standards/expert practice have been checked where material, and unresolved requirements are explicit enough for engineering/AI design to be derived rather than guessed.

### What M2 must not do
- select a database, schema, agent architecture, TEI/RiC implementation or UI as its starting point;
- treat a formal standard as proof of scholarly adequacy;
- turn one pilot's needs into universal method without a generalisability test.

---

## M3 — AI, Engineering & Human Usability Audit

### Purpose
Translate the scholarly requirements established in M2 into the **smallest adequate system, AI/Human-in-the-loop and human-auditability requirements**.

M3 is downstream of scholarship. It may not redefine M1 or weaken M2 requirements for implementation convenience.

### Issues
- `#36` — Research software and data engineering.
- `#37` — AI engineering and Human-in-the-loop.
- `#39` — Human research usability and transparency.

### Entry condition
- M1 complete.
- M2 domain findings sufficiently complete to identify the material scholarly requirements that engineering/AI decisions must serve.

### Internal order
`#36`, `#37` and `#39` should inform one another rather than operate as isolated silos:

1. **#36** evaluates representation, integrity, validation, migration, generated views, dependencies and automation against demonstrated scholarly needs.
2. **#37** evaluates context routing, deterministic vs model judgement, AI provenance/evaluation, Human-in-the-loop roles and specialist escalation against the same requirements.
3. **#39** tests the combined result from the human side: can a non-specialist owner understand source/result/uncertainty/validation, and can a specialist audit exact evidence without trusting an AI summary?

Human usability is an acceptance test for #36/#37, not a later cosmetic layer.

### Required outputs
- mapping from every proposed technical/AI component to an explicit M2 scholarly requirement or observed failure mode;
- distinction between deterministic invariants and epistemic/specialist judgements;
- Human-in-the-loop responsibility model;
- independent-expert validation/escalation implications;
- smallest viable technical alternatives, including retaining current file-based architecture;
- migration/test requirements if canonical data structures would change;
- human-readable review/output requirements;
- explicit complexity/maintenance cost versus research benefit.

### Exit condition
M3 is complete when engineering, AI and human-usability findings are mutually consistent and each proposed structural measure is traceable to an upstream scholarly requirement, with simpler/no-change alternatives assessed.

### What M3 must not do
- introduce multi-agent systems, vector databases, knowledge graphs, applications, CI/CD or other patterns because they are fashionable/normal engineering practice;
- use user confirmation as substitute specialist review;
- treat model agreement as independent validation;
- create a second human-facing research truth store.

---

## M4 — Structural Synthesis & Refactor Decision

### Purpose
Synthesize M1–M3 and make an explicit evidence-based decision about whether the repository should be restructured at all.

### Issue
- `#25` — Future structural audit: transdisciplinary scholarly architecture.

### Entry condition
- M1 completed.
- Relevant M2 reviews completed.
- M3 completed for the requirements under consideration.

### Required synthesis
Produce the matrix required by `#25`:

`requirement → current support → evidence → gap/risk → proposed action/no action`

Also include:
- cross-domain conflicts/dependencies;
- observed failure modes being solved;
- smallest viable alternatives;
- representative source-data migration/loss analysis where applicable;
- Human-in-the-loop and independent-specialist implications;
- deterministic validation requirements where justified;
- research and maintenance cost of each candidate architecture.

### Permitted decisions
M4 must explicitly choose one of three outcomes:

1. **No refactor** — current structure adequately satisfies the demonstrated requirements; close/supersede unnecessary proposals.
2. **Targeted changes** — only specific bounded gaps justify implementation.
3. **Material structural refactor** — multiple demonstrated requirements justify a cohesive migration.

`No refactor` is a successful audit outcome, not a failure to deliver.

### Exit condition
- #25 records the chosen outcome and rationale.
- Approved implementation scope is explicit and bounded.
- Rejected alternatives are recorded where consequential.
- No implementation work is implied merely by the existence of backlog issues.

---

## M5 — Approved Structural Refactor — conditional

**Do not create or populate this milestone in advance.**

Create M5 only if M4 explicitly authorizes targeted or material implementation.

Its issues must be the concrete implementation tasks approved by #25. Existing backlog issues move into M5 only when both conditions are true:
1. their own trigger has been demonstrated; and
2. M4 explicitly selects them as part of the approved solution.

M5 is implementation, not another opportunity to expand scope.

---

## Backlog — no milestone

Open issues without a milestone are intentionally deferred. Their existence preserves options/rationale; it does not authorize work.

Current examples include:
- `#1` TEI P5 export layer;
- `#2` formal RiC mapping;
- `#3` HTR evaluation and training gate;
- `#4` corpus discovery/import automation;
- `#6` corpus-level entity authority reconciliation;
- `#11` machine-readable schema validation;
- `#12` corpus discovery coverage audit;
- `#13` structured bibliography integration;
- `#22` manuscript-hand registry.

A backlog issue enters a milestone only when its documented trigger is actually met or when a governing audit explicitly admits it to a bounded work phase.

If a trigger becomes obsolete, impossible or superseded, close/update the issue rather than carrying it indefinitely.

## Milestone-assignment rules

- A milestone assignment means **planned sequence**, not scholarly status or confidence.
- Do not use due dates unless a real external deadline exists.
- Do not assign an issue to a milestone merely to make the backlog look tidy.
- Keep only one active structural/governance phase when practical; limited overlap is allowed where dependencies are explicit.
- If an issue's trigger is no longer met, remove/defer it rather than forcing milestone completion.
- Closing a milestone requires its exit condition, not simply all issue checkboxes being mechanically closed.
- New structural issues must identify which upstream scholarly requirement they serve before entering M2–M5.

## GitHub milestone names

When mirrored in GitHub, use these exact names:

1. `M1 — Governing Objective & Mission Protection`
2. `M2 — Scholarly Domain Architecture Audit`
3. `M3 — AI, Engineering & Human Usability Audit`
4. `M4 — Structural Synthesis & Refactor Decision`
5. `M5 — Approved Structural Refactor` — create only after M4 authorizes implementation.

## Human reading rule

A visitor should be able to interpret the Issues view as follows:

- **Milestone M1–M4:** this work is admitted to the current governance/architecture sequence.
- **No milestone:** backlog/deferred until trigger.
- **Project `STATUS.md`:** actual current research state and G1–G6 maturity.

Never infer research progress from GitHub milestone completion.