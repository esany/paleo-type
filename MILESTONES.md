# Milestones — work sequencing across governance and research

## Purpose

This file defines how GitHub Milestones are used as a **human-readable planning/navigation layer** across different kinds of work in `paleo-type`.

Milestones may organize governance/architecture work **and** project-specific scholarly work. They never become canonical research truth, evidence status or scholarly maturity by themselves.

The canonical owners remain:
- governing scholarly purpose/constraints → repository governance;
- generic G1–G6 scholarly requirements → `methodology/research-gates.md`;
- actual project gate state/gaps/next action → project `STATUS.md`;
- source evidence/readings/decisions → their existing corpus/project records.

GitHub Milestones mirror **what work is being organized toward a target**. They do not decide whether the target has scientifically been reached.

## Three orthogonal GitHub axes

Use GitHub metadata with three separate meanings:

1. **Milestone = target / work phase** — what bounded result or phase the Issue contributes to.
2. **Label = domain / kind** — which scholarly, technical or process domains the Issue concerns.
3. **Issue = discrete work package** — a reviewable task, question, audit or triggered improvement.

Do not use a Milestone as a substitute for domain labels, and do not use labels to encode canonical project status/confidence.

## Core scheduling rule

> **Open Issue with a Milestone = admitted to a planned/active work sequence.**  
> **Open Issue without a Milestone = backlog/deferred until its trigger or scheduling decision admits it.**

This rule applies to Issues, not to all research activity. A project's `STATUS.md` may contain an immediate next research action without creating an Issue when issue tracking adds no value.

Create a research Issue when work is sufficiently discrete, multi-step, collaborative, reviewable, externally blocked, or useful to track independently. Do not create an Issue for every transcription token, reading change or routine source inspection.

## Milestone families

Milestone families separate work domains that have different target semantics.

Current families:

- `GOV-*` — repository governance / architecture / structural-review work;
- `<project> / G*` — project-specific scholarly work contributing to a generic G1–G6 gate.

Additional families may be introduced only when they represent a genuinely different recurring work-sequencing need. Do not create a family merely to categorize Issues; use labels for that.

---

# Family A — Governance / architecture milestones (`GOV-*`)

These milestones organize bounded work **on the research system itself**. They are globally repository-scoped and follow an evidence-derived sequence.

## Required sequence

```text
GOV-M1 Governing Objective & Mission Protection
        ↓
GOV-M2 Scholarly Domain Architecture Audit
        ↓
GOV-M3 AI, Engineering & Human Usability Audit
        ↓
GOV-M4 Structural Synthesis & Refactor Decision
        ↓
GOV-M5 Approved Structural Refactor   [conditional]
```

A later phase may begin only when the preceding phase has produced enough evidence to satisfy its entry condition. Parallel work inside a phase is allowed where dependencies permit it.

## GOV-M1 — Governing Objective & Mission Protection

### Purpose
Establish the repository's highest-order scholarly objective, precedence hierarchy and human change authority before material structural redesign is evaluated.

### Issues
- `#41` — Canonical governing objective and protection against mission drift.

### Entry condition
Immediate. This is P1 and foundational.

### Required outputs
- one canonical, implementation-independent governing-objective artifact;
- explicit precedence from scholarly objective down to technical implementation;
- explicit human authority for material mission changes;
- AI anti-drift rules without duplicating the objective;
- assessment and smallest practical GitHub-native protection for mission changes;
- linkage from `#25` back to the governing objective.

### Exit condition
`#41` satisfies its acceptance criteria and another capable researcher/AI can identify mission, precedence and change authority without chat.

### Must not
- freeze current technical architecture;
- constitutionalize TSV, TEI, RiC, GitHub, a model, G1–G6 or the Knau pilot;
- impose approval ceremony on routine source research.

## GOV-M2 — Scholarly Domain Architecture Audit

### Purpose
Determine the scholarly and epistemic requirements any future structure must satisfy **before** software/AI architecture is redesigned.

### Issues

Reference-frame refresh — start first:
- `#38` — State of the art, standards and expert-knowledge refresh.

Domain reviews — then/parallel:
- `#26` — Archival science and diplomatics.
- `#27` — Palaeography and scribal evidence.
- `#28` — Historical philology, language history and lexicography.
- `#29` — Scholarly editing and textual criticism.
- `#30` — Historical source criticism.
- `#31` — Source-type and domain history.
- `#32` — Codicology and material manuscript study.
- `#33` — Onomastics and toponymy.
- `#34` — Historical metrology, numismatics and accounting notation.

Cross-domain integrity consolidation:
- `#35` — Research-data stewardship and Good Research Practice.

### Entry condition
- GOV-M1 complete;
- governing objective canonical and controlling the audit.

### Internal order
1. `#38` establishes then-current standards, disciplinary guidance, high-quality practice and experiential-expertise requirements.
2. `#26–#34` test actual source/research requirements against the current structure.
3. `#35` consolidates provenance, reproducibility, responsibility/review status, rights/access and Good Research Practice implications.

### Required result per domain Issue
Record one of:
- `adequate`;
- `gap`;
- `risk`;
- `needs evidence`;
- `not applicable`.

Each material finding should be traceable as:

`scholarly requirement → evidence/standard/expert practice → current support → gap/risk/no gap → smallest candidate measure`

### Exit condition
Relevant domain Issues have documented outcomes, current standards/expert practice were checked where material, and unresolved requirements are explicit enough for engineering/AI decisions to be derived rather than guessed.

### Must not
- start from a database, schema, agent architecture, TEI/RiC implementation or UI;
- treat a formal standard as proof of scholarly adequacy;
- generalize one pilot's needs without a generalisability test.

## GOV-M3 — AI, Engineering & Human Usability Audit

### Purpose
Translate GOV-M2 scholarly requirements into the smallest adequate software/data, AI/Human-in-the-loop and human-auditability requirements.

### Issues
- `#36` — Research software and data engineering.
- `#37` — AI engineering and Human-in-the-loop.
- `#39` — Human research usability and transparency.

### Entry condition
- GOV-M1 complete;
- GOV-M2 sufficiently complete to identify material scholarly requirements.

### Required outputs
- every technical/AI proposal mapped to an upstream scholarly requirement or observed failure mode;
- deterministic invariants distinguished from epistemic/specialist judgement;
- Human-in-the-loop responsibility model;
- independent-expert escalation implications;
- smallest viable alternatives, including no technical change;
- migration/test requirements where canonical structures would change;
- human-readable review/output requirements;
- explicit maintenance/complexity cost versus research benefit.

Human usability is an acceptance test for engineering/AI design, not a later cosmetic layer.

### Exit condition
Engineering, AI and human-usability findings are mutually consistent and every proposed measure has an upstream scholarly justification plus simpler/no-change alternatives.

## GOV-M4 — Structural Synthesis & Refactor Decision

### Purpose
Synthesize GOV-M1–M3 and decide whether any repository restructuring is justified.

### Issue
- `#25` — Future structural audit: transdisciplinary scholarly architecture.

### Entry condition
- GOV-M1 complete;
- relevant GOV-M2 reviews complete;
- GOV-M3 complete for the requirements under consideration.

### Required synthesis

`requirement → current support → evidence → gap/risk → proposed action/no action`

Also include cross-domain conflicts/dependencies, observed failure modes, smallest viable alternatives, migration/loss analysis where relevant, HITL/expert implications and maintenance cost.

### Permitted decisions
1. **No refactor** — current structure is adequate.
2. **Targeted changes** — bounded demonstrated gaps justify changes.
3. **Material structural refactor** — multiple demonstrated requirements justify a cohesive migration.

`No refactor` is a successful audit outcome.

### Exit condition
`#25` records the chosen outcome and bounded scope; rejected consequential alternatives remain understandable.

## GOV-M5 — Approved Structural Refactor — conditional

Do **not** create/populate this milestone in advance.

Create it only if GOV-M4 explicitly authorizes implementation. Existing backlog Issues enter GOV-M5 only when their own trigger is demonstrated **and** `#25` selects them as part of the approved solution.

---

# Family B — Project scholarly milestones (`<project> / G*`)

## Purpose

A project may use GitHub Milestones to group **scholarly Issues that contribute to a generic G1–G6 research gate**.

This is a navigation/work-planning mirror only:

> **GitHub gate milestone = planned work contributing to a gate.**  
> **Project `STATUS.md` = evidence-based decision about whether the gate is reached/active/reopened.**

Completing or closing a GitHub gate milestone does **not** automatically complete the scholarly gate.

## Canonical gate source

Never copy the G1–G6 requirements into GitHub Milestone descriptions or project files as a competing definition. The authoritative requirements remain in `methodology/research-gates.md`.

Milestone descriptions should link/refer to the generic gate and state only project-specific scope/intent.

## Naming convention

Use:

`<project-id> / G<n> — <short generic gate name>`

For the current pilot:

1. `ega-reg-ii-5-knau / G1 — Source and transmission basis`
2. `ega-reg-ii-5-knau / G2 — Diplomatic representation`
3. `ega-reg-ii-5-knau / G3 — Internal palaeographic analysis`
4. `ega-reg-ii-5-knau / G4 — Controlled witness comparison`
5. `ega-reg-ii-5-knau / G5 — Critical consolidation and validation`
6. `ega-reg-ii-5-knau / G6 — Scholarly edition`

Create only the project Milestones that are useful for actual Issue-based work; do not pre-create all six merely for completeness.

## Assignment rule

Assign a scholarly Issue to a project gate Milestone when:
- the Issue is a discrete work package rather than ordinary line-by-line research activity;
- completing it materially contributes to that gate's requirements;
- the project has deliberately scheduled it rather than merely preserving it as a future option.

Examples:
- rebuilding the principal witness into a complete physical-line diplomatic representation → project G2;
- a bounded internal notation/grapheme concordance needed to test consequential readings → project G3;
- independent transcription/collation of a comparison witness → project G4;
- adversarial validation/review packet for consequential readings → project G5;
- edition/export package after G5 → project G6.

An Issue may support more than one gate. Assign it to the **primary immediate target** and use labels/body links to expose secondary relevance. Do not create duplicate Issues only to place the same work in multiple Milestones.

## Gate milestone lifecycle

- **Open milestone:** project has scheduled Issue-based work toward that gate.
- **Closed milestone:** the planned Issue set for that pass is complete/replanned; this is not by itself a gate claim.
- **Gate reached:** only project `STATUS.md`, using `research-gates.md`, may state this.
- **Gate reopened:** reopen/create a bounded GitHub milestone only if new Issue-based work actually benefits from tracking; always update `STATUS.md` first for the scholarly state.

If all scheduled Issues are closed but a gate remains scientifically unmet, `STATUS.md` remains `active/not reached/reopened`; create further Issues only for demonstrated remaining work that benefits from issue tracking.

## Current pilot use

The current Knau project is at G2 according to project `STATUS.md`. If its current G2 work is represented as discrete Issues, those Issues should target:

`ega-reg-ii-5-knau / G2 — Diplomatic representation`

Do not infer G2 completion from the Milestone's progress bar.

---

# Labels — orthogonal domain classification

Milestones answer **toward what target/phase?** Labels answer **what kind/domain of work is this?**

Prefer a small reusable label vocabulary when available, for example domain/topic families such as:
- archival/diplomatics;
- palaeography;
- editing/textual criticism;
- source criticism/history;
- philology;
- codicology;
- entities/onomastics;
- metrology/numismatics;
- research data/GWP;
- AI/HITL;
- software/data engineering;
- documentation/navigation.

Do not encode source truth, reading confidence, gate state or canonical identity in labels.

Because one GitHub Issue has one Milestone but can have multiple labels, cross-disciplinary work belongs in one target Milestone with all relevant domain labels.

---

# Backlog — no milestone

Open Issues without a Milestone are intentionally unscheduled/deferred. Their existence preserves a question, option or trigger; it does not authorize work.

Current examples include trigger-based future options such as:
- `#1` TEI P5 export layer;
- `#2` formal RiC mapping;
- `#3` HTR evaluation and training gate;
- `#4` corpus discovery/import automation;
- `#6` corpus-level entity authority reconciliation;
- `#11` machine-readable schema validation;
- `#12` corpus discovery coverage audit;
- `#13` structured bibliography integration;
- `#22` manuscript-hand registry.

A backlog Issue enters a Milestone only when its documented trigger fires or a deliberate planning/audit decision admits it to a bounded work phase.

If a trigger becomes obsolete, impossible or superseded, close/update the Issue rather than carrying it indefinitely.

---

# Milestone assignment and maintenance rules

- No calendar due date unless a real external deadline exists.
- Do not assign an Issue merely to make the backlog look tidy.
- Do not infer evidence confidence or scholarly completion from a progress bar.
- Governance and project-research Milestones may coexist because they organize different work families.
- Keep naming prefixes explicit so Milestone families cannot be confused.
- Use labels for domains; use Milestones for targets/phases.
- When a project changes scholarly gate state, update `STATUS.md` first; then review whether GitHub Issue/Milestone assignments should change.
- When a governance phase changes, update the relevant Issues/Milestone; do not alter project gate state unless evidence changed.
- Closing a Milestone requires completion/replanning of its admitted work, not a claim that every broader problem is solved.

## GitHub-native creation limitation

If tooling cannot create GitHub Milestone objects directly, this file remains the canonical **planning semantics and naming convention**, but it does not pretend the UI objects exist. Create/assign native Milestones only through a supported GitHub interface and keep them consistent with these rules.

## Human reading rule

A visitor should be able to interpret GitHub as follows:

- `GOV-*` Milestone → admitted repository-governance/architecture work;
- `<project> / G*` Milestone → admitted scholarly Issue work toward that project's gate;
- labels → affected domain(s)/kind of work;
- no Milestone → backlog/deferred;
- project `STATUS.md` → actual scientific gate state and next action;
- repository/source records → canonical evidence and research truth.

GitHub metadata makes the work legible. It never decides what the sources prove.