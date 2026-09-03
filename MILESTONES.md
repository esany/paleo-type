# Milestones — GitHub work-planning semantics

## Purpose

GitHub Milestones are a **human-readable planning/navigation layer**. They group discrete Issues toward a bounded target or phase. They are not canonical research truth, evidence status, scholarly maturity, Project purpose, current research priority or implementation authority.

Canonical owners remain elsewhere:

- scholarly purpose/precedence → `GOVERNING_OBJECTIVE.md`;
- material research-system admission → `methodology/maintenance.md`;
- generic G1–G6 requirements → `methodology/research-gates.md`;
- Project purpose/scope → Project `project.yml`;
- actual Project gate/restart state and authorized `NEXT ACTION` when one exists → Project `STATUS.md`;
- Source/File/research evidence → their canonical Corpus/Project owners.

## Admission vocabulary

In this file, an Issue being **scheduled/admitted to a Milestone** means only that it has entered a GitHub work sequence.

It does **not** mean:

- D-016 material implementation admission;
- Human Owner authorization of a Project or research priority;
- scholarly gate attainment;
- evidence acceptance;
- merge/release authority.

Where material research-system change is involved, the separate D-016 admission state in `methodology/maintenance.md` must already be satisfied before implementation begins.

## Three orthogonal GitHub axes

1. **Milestone = target / work phase** — what bounded result or phase an Issue contributes to.
2. **Label = domain / kind** — which scholarly, technical or process domains the Issue concerns.
3. **Issue = discrete work package** — a reviewable task, question, audit or triggered improvement.

Do not encode canonical Project status, source truth, reading confidence or owner authority in GitHub metadata.

## Scheduling rule

> **Open Issue with a Milestone = scheduled in that GitHub work sequence.**  
> **Open Issue without a Milestone = unscheduled/backlog.**

This rule applies to Issues, not to all research activity. A Project `STATUS.md` may contain an authorized immediate scholarly action without creating an Issue when issue tracking adds no value.

Create an Issue when work is sufficiently discrete, multi-step, collaborative, reviewable, externally blocked or useful to track independently. Do not create one for every line reading, transcription correction or routine source inspection.

## Milestone families

### `GOV-*` — repository governance / architecture

Use for bounded work on the research system itself.

The established family is:

```text
GOV-M1 Governing Objective & Mission Protection
GOV-M2 Scholarly Domain Architecture Audit
GOV-M3 AI, Engineering & Human Usability Audit
GOV-M4 Structural Synthesis & Refactor Decision
GOV-M5 Approved Structural Refactor [conditional]
```

These names preserve planning lineage. Detailed phase evidence, decisions and acceptance state belong in the owning Issues/PRs, not copied here.

`GOV-M5` is conditional: use it only for implementation explicitly admitted by the relevant owner/governance path. A GOV Milestone does not itself provide that admission.

### `<project> / G*` — Project scholarly work

Use to group discrete scholarly Issues contributing to a generic G1–G6 gate.

The Milestone is a planning mirror only:

> **GitHub gate Milestone = scheduled Issue work contributing to a gate.**  
> **Project `STATUS.md` = evidence-based statement of actual Project gate/restart state.**

Closing the Milestone does not complete the scholarly gate. Reopening or creating one does not change Project priority.

## Canonical gate source

Never copy G1–G6 requirements into Milestone descriptions or Project files as a competing definition. The authoritative requirements remain in `methodology/research-gates.md`.

Milestone descriptions should reference the relevant generic gate and contain only planning scope needed to understand the scheduled Issue set.

## Naming convention

Use:

`<project-id> / G<n> — <short generic gate name>`

Stable generic gate names are:

1. `G1 — Source and transmission basis`
2. `G2 — Diplomatic representation`
3. `G3 — Internal palaeographic analysis`
4. `G4 — Controlled witness comparison`
5. `G5 — Critical consolidation and validation`
6. `G6 — Scholarly edition`

Create only Milestones that are useful for actual Issue-based work; do not pre-create all six for completeness.

## Assignment rule

Assign a scholarly Issue to a Project gate Milestone when:

- it is a discrete work package rather than ordinary line-by-line research;
- completing it materially contributes to that gate;
- the work has actually been scheduled;
- any separate authority/admission required for the work is already satisfied.

If an Issue contributes to several gates, choose the primary immediate planning target and expose secondary relevance in labels/body links. Do not duplicate Issues merely to place the same work in several Milestones.

## Gate Milestone lifecycle

- **Open:** scheduled Issue work toward the gate exists.
- **Closed:** that scheduled Issue set is complete/replanned; this is not a scholarly gate claim.
- **Gate reached/reopened:** only the Project's canonical status, evaluated against `research-gates.md`, may state this.

When evidence changes gate state, update the canonical Project state first. Adjust GitHub planning afterwards only if useful.

## Labels

Labels classify domain/kind, not truth or authority. Prefer a small reusable vocabulary such as archival/diplomatics, palaeography, editing/textual criticism, source criticism/history, philology, codicology, onomastics, metrology/accounting, research data/GWP, AI/HITL, software/data engineering and documentation/navigation.

Cross-disciplinary work belongs in one target Milestone with multiple domain labels when appropriate.

## Backlog / deferred Issues

An unscheduled Issue may preserve a future option without authorizing work. Deferred Issues should state:

1. problem/research benefit;
2. why not now;
3. observable trigger;
4. acceptance/definition of done.

When the trigger fires, either schedule the Issue deliberately or record why it remains unscheduled. Close/update obsolete, completed, superseded or duplicate Issues instead of carrying dead backlog indefinitely.

## Maintenance rules

- No calendar due date without a real external deadline.
- Do not assign Issues merely to make progress bars look tidy.
- Do not infer evidence confidence, gate attainment, Project purpose or priority from Milestone state.
- Do not infer D-016 admission from a Milestone assignment.
- Use labels for domains; use Milestones for targets/phases.
- GitHub metadata may point to canonical state but must not become a competing state store.
- Historical planning detail belongs in GitHub history, Issues and PRs rather than accumulating here.

## Human reading rule

Interpret GitHub as follows:

- `GOV-*` → scheduled research-system/governance work;
- `<project> / G*` → scheduled scholarly Issue work contributing to a Project gate;
- labels → affected domain(s)/kind;
- no Milestone → unscheduled/backlog;
- Project `project.yml` / `STATUS.md` → Project purpose/scope and actual restart/gate/authorized-next-action state;
- Corpus/Project research records → canonical evidence and research truth;
- D-016 record/owner decision → material implementation admission where required.

GitHub metadata makes work legible. It does not decide what the sources prove or what research must happen next.
