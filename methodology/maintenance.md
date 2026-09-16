# Maintenance and documentation ownership

## Purpose

Keep `paleo-type` continuously usable without creating a second documentation project. Maintenance is event-driven: update the canonical record that owns a changed truth, propagate only material consequences, then return to research.

## One fact, one canonical home

| Information | Canonical home | Role |
|---|---|---|
| highest-order scholarly purpose, precedence and human material-change authority | `GOVERNING_OBJECTIVE.md` | repository constitution / mission boundary |
| repository purpose/map/required reading path | `README.md` | orientation view / entry point |
| mandatory AI/research guardrails | `AGENTS.md` | binding stable rules |
| shared architectural/methodological rationale | `DECISIONS.md` | lean cross-project decision record |
| GitHub Milestone-family/naming/backlog semantics | `MILESTONES.md` | planning/navigation rules only |
| authoritative end-to-end scholarly method | `methodology/historical-source-workflow.md` | reusable normative method |
| generic scholarly maturity gates | `methodology/research-gates.md` | reusable G1–G6 requirements |
| material research-system change-admission workflow | `methodology/maintenance.md` | canonical operational admission rule |
| Project/Source-use lifecycle | `methodology/project-lifecycle.md` | reusable Project rules |
| Source/File identity, provenance, preservation and access method | `methodology/source-and-provenance.md` | reusable Source/File rules |
| evidence/source-status semantics | `methodology/evidence-policy.md` | reusable evidence-status rules |
| transcription/source-phenomenon semantics | `methodology/transcription-guidelines.md` | reusable transcription rules |
| AI-specific provenance/evaluation obligations | `methodology/ai-governance.md` | reusable AI/HITL rules |
| stable machine-checkable Source/File/Project-use constraints | `corpus/source-contract.json` + `tools/source_contract.py` | executable contract / resolver |
| Source/File/relationship/crosswalk truth | `corpus/`, `entities/` | canonical Corpus truth |
| Project purpose, documentary anchor and current scope | `projects/<id>/project.yml` | canonical Project definition |
| Project-relative Source use | `projects/<id>/source-uses.tsv` | canonical Project→Source use truth |
| concrete Project-use→File evidence | `projects/<id>/research/use-evidence.tsv` | Project-local evidence binding |
| current Project gate/evidence/access/restart state and authorized next action when one exists | `projects/<id>/STATUS.md` | canonical restart point |
| Project-specific readings, decisions, evidence and lessons | owning Project files | Project research truth |
| rebuildable Project/task context | `tools/project_context.py` output | derived view; never canonical truth |
| deferred/discrete work and review history | GitHub Issues/PRs | work/audit metadata, not research truth |
| exploratory reasoning | chat | transient workspace only |

Explanations, generated views and GitHub metadata may summarize canonical records but must not become parallel truth stores. Volatile Project state should be referenced or derived rather than recopied into orientation/guard surfaces.

## Governing-objective change control

`GOVERNING_OBJECTIVE.md` is not ordinary maintenance. A material change to its purpose, precedence or governing invariants is a special governance event and requires an explicit human owner decision.

- AI/collaborators may analyse or propose an amendment, but must not autonomously weaken, replace or supersede the objective.
- A material amendment must be isolated in a visible, cohesive PR with rationale and consequences; it must not arrive as incidental cleanup or automatic propagation.
- Routine synchronization/refactor machinery must never rewrite the governing objective merely because lower-level method, standards, models or architecture changed.
- Lower-level files should reference the objective rather than restate it.

## Material research-system change admission

This file is the canonical operational owner of the general consequence-based admission workflow for material research-system changes:

`analysis → requirements → concept → owner review / explicit implementation admission → development → deterministic tests / scholarly loss checks → result review`

Apply this workflow when a proposed change materially alters shared METHOD, the CORPUS information model or canonical ownership, Project architecture/invariants, canonical research-data migration semantics, or another research-system rule where error could change provenance, scholarly meaning, auditability or restartability.

The stages have distinct purposes:

1. **Analysis** — inspect current canonical state and the demonstrated failure/need.
2. **Requirements** — derive applicable scholarly, epistemic, provenance, usability and technical requirements.
3. **Concept** — state the smallest coherent change, alternatives, dependencies and explicit non-goals.
4. **Owner review / explicit implementation admission** — the human owner decides whether a sufficiently precise material scope may enter development.
5. **Development** — implement only the admitted scope.
6. **Deterministic tests / scholarly loss checks** — verify machine-checkable invariants and proportionate preservation of scholarly meaning, provenance and regression fixtures.
7. **Result review** — compare the result with admitted requirements and preserved research meaning; deterministic success alone does not establish scholarly acceptance.

### Lean admission boundary

Only **material research-system changes** require this path. Ordinary source inspection, evidence logging, bounded scholarship inside an admitted method/scope, rebuildable derived outputs and routine implementation details already covered by a precise admitted scope do not require repeated owner approval.

Once a material scope is admitted, bounded implementation may proceed without owner micromanagement. A genuinely new material semantic/architecture/migration choice outside that scope must return to this workflow rather than being silently absorbed.

### Admission is not specialist validation

Owner admission controls purpose, priorities and permission to implement a material research-system change. It does **not** establish archival, palaeographic, historical, philological, editorial or other specialist truth and never substitutes for qualified independent specialist validation where required.

AI/HITL-specific obligations refer to this workflow from `ai-governance.md`; they do not redefine it. No workflow engine is required.

## Systemic integration and Generic-Fit

Do not append a durable rule merely because one pilot, AI session or external reference exposed something new. Before promoting a change, compare it with the governing objective, canonical owners, applicable requirements and existing decisions.

Useful review dispositions are:

`fuse | refine | reframe | supersede | conflict | reject | defer`

This is review vocabulary, not a lifecycle/schema. Preserve enough rationale to show:

- origin/evidence of the new aspect;
- which existing semantics/requirements it supports, changes or conflicts with;
- chosen disposition and why;
- required changes and deliberate non-changes;
- remaining authority/assurance.

A Project/pilot finding stays Project-specific by default. Promote only a safeguard that genuinely applies across comparable investigations. A single case can falsify a bad generic assumption without defining the whole replacement architecture.

## Ownership and propagation rule

When truth changes:

1. update its canonical owner first;
2. derive/re-resolve machine-computable consequences through the executable owner where available;
3. update only dependent canonical state whose truth actually changed;
4. repair stale summaries/references rather than creating a second owner;
5. run proportionate deterministic and scholarly checks;
6. return to research.

Examples of routing belong to the specialist owners:

- Project creation/purpose/scope/Source-use → `project-lifecycle.md` + Source Contract;
- Source/File/crosswalk/preservation/access → `source-and-provenance.md` + Source Contract;
- evidence class/status → `evidence-policy.md`;
- diplomatic phenomena/readings → `transcription-guidelines.md`;
- gate semantics → `research-gates.md`;
- GitHub planning → `MILESTONES.md`.

Do not restate those models here merely to make maintenance self-contained.

### Controlled-value rule

Where a stable semantic is controlled executably, prose must reference that owner rather than define or alias its value set. For File storage/preservation state, `corpus/source-contract.json` is the sole controlled-value owner. Any vocabulary change belongs there through a deliberate semantic change, not through prose drift.

## Maintenance triggers

Run maintenance when an event changes truth or exposes stale dependent state, for example:

- Governing Objective proposal/change;
- Source/File/crosswalk/relationship correction;
- Project purpose/scope/documentary-anchor/Source-use change;
- transcription/decision/evidence change;
- generic method/gate/contract change;
- admitted migration/refactor;
- active gate/restart/authorized-next-action change;
- a Project lesson that passes Generic-Fit;
- a deferred Issue whose trigger fired or became obsolete.

The specialist owner determines the exact semantics of the change. Maintenance determines propagation and consistency obligations.

### Programme/phase/result-transition reconciliation

When an **already-established broader programme or planning context** exists, a material programme/phase/result transition is also a maintenance trigger if its result can affect whole-programme completion or maturity, selectable/current work, or materially affected restart/navigation state — even when canonical research truth itself is unchanged.

For such a transition:

1. resolve the **existing** programme/planning cursor or decision owner; do not create one merely because this rule applies;
2. explicitly disposition the material consequence for that owner and materially affected restart/navigation surfaces as **changed**, **unchanged** or **needs decision** (or semantically equivalent existing vocabulary), with enough rationale to reconstruct the consequence without old chat;
3. keep the local result local: a local `PASS`, `STOP`, closeout or `no further local change` does not establish whole-programme completion unless the programme owner explicitly reaches that conclusion;
4. preserve Human-Owner authority: reconciliation may expose a decision surface but must not manufacture research priority, Project scholarly `NEXT ACTION`, Concept/implementation admission or activation of deferred work;
5. keep planning/navigation metadata distinct from Research, Requirements, METHOD, Project truth and durable accepted decisions;
6. permit **unchanged** as a valid disposition, but do not treat silence as evidence that the programme consequence was considered.

This obligation is consequence-triggered, not a universal review ceremony for ordinary task closeouts. If no broader programme/planning owner has already been established by authority, maintenance records no invented programme, roadmap, priority or `NEXT ACTION`.

## Bounded consistency pass

After a material canonical change, check only affected boundaries plus high-risk stale surfaces. At minimum, as applicable:

1. state changed canonical truths/owners and deliberate non-changes;
2. run relevant executable validation/resolution rather than re-deriving machine facts in prose;
3. verify canonical references still resolve and removed legacy owners did not reappear;
4. verify Project `project.yml`/`STATUS.md` do not contain stale purpose/scope/next-action claims;
5. verify summaries, templates and generated contexts do not promote historical/structural/support state into current authority or priority;
6. verify preservation/access claims match canonical File state and keep byte identity distinct from target-context readiness;
7. verify generic rule changes were not copied into Project truth or vice versa;
8. audit affected deferred Issues/planning metadata only when the change materially affects them;
9. verify restartability without old chat;
10. stop when coherent and return to research.

A consistency pass is not permission to invent architecture, expand scope or re-adjudicate manuscript readings.

## Reading/navigation ownership

`README.md` owns the repository reading/navigation path. This file does not maintain a second reading list. `MILESTONES.md` owns GitHub planning semantics. Specialist methodology owns its own research semantics.

Generated Project context may assist restart, but it remains rebuildable and must retain references to the canonical owners it summarizes.

## Human–AI maintenance responsibility

### AI / implementation agent

Own routine repository hygiene, propagation of changed truths, deterministic validation/resolution, generated-context refresh and restartability within admitted authority. Surface missing metadata, rights, access or authority facts rather than inventing them.

### Human Owner

Own research purpose/priority, Project materialization/boundary where not already established, non-derivable rights/authority facts, material research-system admission and consequential publication/use decisions. The owner is not the repository synchronizer or default specialist adjudicator.

### Qualified specialist

Provides independent domain judgement/review when consequence or unresolved specialist uncertainty warrants it.

## End-of-work integrity check

Before completing consequential maintenance ask:

1. What truth changed and which canonical owner now contains it?
2. Did any copied/derived surface become stale?
3. Were deterministic consequences checked by the executable owner where available?
4. Did the change accidentally create a second truth store or reintroduce a removed legacy owner?
5. Did Project purpose/priority or scholarly judgement change without the required authority/evidence?
6. Did preservation/access wording stay aligned with controlled state?
7. Can a fresh capable context reconstruct the result and authorized next state without old chat?

If not, persist or repair the minimum missing state. Do not add documentation merely to satisfy the checklist.

## Lean maintenance rule

`Maintain on change, at the canonical owner; derive rather than copy; propagate only changed consequences; validate deterministic facts mechanically; preserve scholarly/authority boundaries; then stop.`
