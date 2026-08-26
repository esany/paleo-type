# Project lifecycle and relationship model

## Purpose

Define how projects are created, related, activated, maintained and retired without duplicating corpus truth or allowing pilot-specific structure to drift into a hidden second framework.

This file is generic METHOD. Concrete project facts belong in `projects/<id>/`; source identity and historical/source relationships belong in `corpus/`.

## Project is not source

A corpus source exists because an archival/historical source unit is relevant to the corpus. A project exists because there is a bounded research responsibility around one or more sources.

Do not create one project per corpus row automatically.

Two project kinds are currently supported because they solve observed needs:

- `source-unit` — owns reusable source-local work for one canonical source, especially image/folio/PDF/export crosswalks, source-level inspection state and source-wide derived work;
- `research-scope` — owns a bounded research question/locus/edition task that may use one principal source and several comparison/control/context sources.

Do not add further kinds until a real project cannot be represented by these two.

## Canonical ownership

- source identity/stage → `corpus/sources.tsv`;
- external/digital binary identity, checksum, coverage, rights/storage → `corpus/files.tsv`;
- historical/archival/textual source relationships → `corpus/relationships.tsv`;
- cross-project research organisation → `projects/relationships.tsv`;
- source-unit local crosswalks → the relevant `source-unit` project's `sources/`;
- research-scope transcription/decisions/status → that `research-scope` project;
- generic project rules → this file and `templates/project/`.

A research-scope project references reusable source-unit mappings; it does not copy them.

## Minimal project contract

Create every new project from `templates/project/`, never by cloning an existing project.

Required at creation:

1. unique `project.yml:id`;
2. explicit `project_kind` (`source-unit` or `research-scope`);
3. clear `repository_role` and bounded `active_scope`;
4. canonical source ID when a principal/source-unit source exists, and that ID must already exist in `corpus/sources.tsv`;
5. file provenance in `corpus/files.tsv` for any exact binary used as evidence;
6. `STATUS.md` with actual evidence state and either a bounded `NEXT ACTION` or explicit `not yet activated`;
7. no copied generic gate/method text beyond concise references;
8. project relations recorded centrally when another project is materially used.

Optional directories are created only when evidence/work exists: `transcription/`, `apparatus/`, `palaeography/`, `research/`, `context/`, `LEARNINGS.md`.

Empty future-proof folders are prohibited.

## Project relations

`projects/relationships.tsv` is the canonical registry for research-organisational relationships between projects.

Current relation vocabulary is intentionally small and evidence-derived:

- `scopes-source-unit` — research-scope works on a bounded locus/question inside a source-unit project;
- `compares-with` — projects are explicitly compared as part of research;
- `uses-as-control` — another project's source/work is used as a defined control;
- `uses-as-context` — another project supplies contextual comparison without becoming a textual witness.

Add a relation type only when an observed research relation cannot be expressed without semantic distortion. Document the new type here when introduced.

### Critical separation

A project relation is about **our research organisation**. It never proves a historical/source relation.

`project A compares-with project B` does not mean `source A is a copy/parallel of source B`.

Historical/archival/textual relationship claims remain in `corpus/relationships.tsv` with their own evidence status.

## Creation procedure

Before creating a project:

1. identify the research responsibility and decide whether a project is actually needed;
2. verify/create the canonical corpus source and file records first;
3. choose `source-unit` versus `research-scope`;
4. instantiate only `project.yml` + `STATUS.md`, plus `sources/` only when local mapping already exists;
5. add required rows to `projects/relationships.tsv`;
6. run the Project Creation Check below;
7. if creation establishes a new generic need, record the concrete learning first and generalise only after explicit review.

## Project Creation Check

A project is valid only if all applicable checks pass:

- [ ] project ID is unique;
- [ ] project kind is explicit and valid;
- [ ] canonical source ID exists in `corpus/sources.tsv`;
- [ ] exact evidence binaries used are registered in `corpus/files.tsv`;
- [ ] scope does not imply unverified source/corpus completeness;
- [ ] `STATUS.md` distinguishes inspected evidence from metadata/not-inspected/not-observable states;
- [ ] generic G1–G6 requirements are referenced, not copied;
- [ ] source-unit mappings have one canonical home;
- [ ] research-scope projects reference rather than duplicate source-unit mappings;
- [ ] project relations exist for material project-to-project use;
- [ ] project relations do not encode historical/source claims;
- [ ] historical/source relations remain in `corpus/relationships.tsv`;
- [ ] no empty speculative directories were created;
- [ ] a new capable researcher can restart without chat.

If the same machine-checkable creation error recurs, that is evidence for activating schema-validation automation; do not automate pre-emptively.

## Change propagation and anti-drift

When a source-unit mapping changes:

1. update the owning source-unit project;
2. identify research-scope projects linked through `projects/relationships.tsv`;
3. update only dependent status/transcription references whose truth changed;
4. do not copy the corrected mapping into consumers;
5. run the bounded consistency pass from `maintenance.md`.

When a research-scope project discovers a source-level correction:

1. record the observed project evidence;
2. correct the source-unit/corpus owner after verification;
3. propagate the changed canonical truth back to all related projects;
4. preserve project-specific consequences in each affected `STATUS.md`/decision record.

When a project discovers a generic methodological weakness:

`project observation → project learning/status → generalisability check → methodology/DECISIONS update → bounded consistency pass`.

This is the required feedback loop. A project never silently modifies generic method by example.

## Activation, dormancy and closure

A registered source-unit project may legitimately remain `not yet activated`; this is not backlog debt.

A project becomes active when it has a real research task and bounded next action. Gate state is recorded in its `STATUS.md` when applicable.

Do not delete a completed project merely because it is inactive. Preserve its research state as part of scholarly provenance. If a project is superseded, state that explicitly and point to the successor; do not silently merge histories.

## Consistency invariant

At any time the repository should answer without chat:

- what each project is for and what kind it is;
- which canonical sources/files underpin it;
- which other projects it uses and why;
- which relations are research-organisational versus historical/source claims;
- where reusable source-local mappings live;
- what changed when source/project knowledge fed back into corpus or method;
- what the active next action is, or that the project is intentionally dormant.

If those answers require comparing duplicated project data manually, the project model has drifted and must be repaired before further expansion.
