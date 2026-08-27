# Project lifecycle and historical-source project model

## Purpose

Define what a project is, how its historical source structure is anchored, how internal and external sources are distinguished, and how project work reuses canonical corpus truth without duplication.

This file is generic METHOD. Canonical source identity/relations/files live in `corpus/`; project work state lives in `projects/<id>/`.

## Project definition

A **project is anchored to one historically independent source structure**, represented by exactly one canonical `project_source_id` in `project.yml`.

In the current corpus that root is an archival act. The rule is structural rather than technical: the project boundary follows the historically independent documentary unit, not a convenient research bundle, portal export, PDF, place name or current question.

A project may work only on a small locus of its root structure at a given time. `active_scope` is therefore allowed to be narrower than the project itself.

A project may also use sources outside its root structure for comparison, control or context. Those sources remain **external** to the project even though they are registered for research use.

## Structural membership

Historical/documentary source nodes live in `corpus/sources.tsv`. Structural containment is represented generically in `corpus/relationships.tsv` with `part_of`.

For a project source `S` and project root `R`:

- `S = R` → project root;
- `S part_of* R` → structurally internal source;
- otherwise → external research source.

No separate `internal/external` field is required. The resolver derives this deterministically from the canonical `part_of` graph.

This preserves the distinction between:

- **historical structure** — source-to-source `part_of` relations;
- **research function** — project-relative roles such as `principal`, `comparison`, `control`, `context`.

A source can be external to a project and still be highly important to its research.

## Canonical ownership

One fact has one canonical owner:

- source identity/type/description → `corpus/sources.tsv`;
- historical/documentary structure and other source relations → `corpus/relationships.tsv`;
- exact digital/export file identity, checksum, coverage, storage state and rights → `corpus/files.tsv`;
- reusable source-wide image/PDF/export/folio crosswalk → `corpus/source-data/<source_id>/`;
- project root identity → `project.yml: project_source_id`;
- project-relative source function and relevant locus → `projects/<id>/sources/sources.tsv`;
- project inspection details → `projects/<id>/sources/inspection-log.tsv` when needed;
- project transcription/decisions/analysis/status → that project;
- generic rules → `methodology/` and consequential cross-project decisions → `DECISIONS.md`.

A project references canonical source nodes; it does not redefine them.

## Minimal project contract

Create every new project from `templates/project/`.

Required at creation:
1. unique project ID and human-readable title;
2. exactly one `project_source_id` resolving to the historically independent project root in `corpus/sources.tsv`;
3. a scholarly `research_object` and bounded `active_scope` within that root;
4. `sources/sources.tsv` listing the actual sources used and their project-relative roles/loci;
5. every referenced source ID exists in `corpus/sources.tsv`;
6. every exact digital export used as evidence exists in `corpus/files.tsv` with checksum and preservation state;
7. `STATUS.md` records evidence state and one bounded `NEXT ACTION`;
8. generic gates/method are referenced rather than copied;
9. no empty future-proof directories.

If `principal_source_id` is present, it must be registered in the project and structurally lie within the `project_source_id` root.

## Project source register

`projects/<id>/sources/sources.tsv` is the human-readable research-use register.

Required columns:

`source_id | archival_title | project_role | relevant_locus | primary_file_id | status | notes`

Each row states **how the project uses a canonical source**. It does not determine whether that source belongs structurally to the project; structural membership is derived from `part_of`.

Rules:
- one row represents one canonical source used by the project;
- `project_role` is project-relative and never part of source identity;
- `comparison`, `control`, `context` may legitimately be external sources;
- `principal`, when declared in `project.yml`, must be internal to the project root;
- `relevant_locus` is project-specific and does not redefine full source extent;
- `primary_file_id` points to `corpus/files.tsv`;
- source relationships remain in `corpus/relationships.tsv` with evidence status.

## Current regression example

The current Reg. Ii 5 project is rooted at:

`ACT-THHSTAW-EGA-REG-II-5`

Its Ziegenrück protocol `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129` is structurally internal because it is `part_of` that act.

The related Reg. Ii 4 Bd. II and Reg. Ii 3 sources are external comparison/control/context sources because their `part_of` ancestry terminates in different historical source roots.

This distinction is derived, not manually duplicated.

## Original source exports

The exact PDF/image export actually used for research is part of the evidential chain. A portal URL or URN is useful provenance but is not a substitute for the exact inspected export.

For consequential project source exports:
- preserve original filename and exact bytes when rights permit;
- record SHA-256 in `corpus/files.tsv`;
- record coverage and preservation state;
- keep derivatives separate;
- if public-repository rights block preservation, state that explicitly.

## Project creation procedure

Before creating a project:
1. identify the historically independent source structure that will be the project root;
2. verify/create that canonical source node and necessary `part_of` relations in the corpus;
3. set `project_source_id` to that root;
4. identify the internal source nodes actually needed for current work;
5. register any external comparison/control/context sources separately in the project source register;
6. register exact source exports and preservation state;
7. instantiate `project.yml`, `STATUS.md`, and `sources/sources.tsv`;
8. run `python tools/source_contract.py validate`;
9. use the resolver rather than reconstructing membership from names or chat.

Do not create a project merely because a PDF, protocol fragment, place, question or temporary comparison task exists. Create/split a project when a distinct historically independent source structure requires its own scholarly state.

## Project creation check

A project is valid only if all applicable checks pass:

- [ ] `project_source_id` resolves to one canonical historical source root;
- [ ] project identity follows the historical structure, not the current narrow locus or research convenience;
- [ ] active scope may be narrower but is explicit;
- [ ] every project source resolves to `corpus/sources.tsv`;
- [ ] internal/external status is derivable from `part_of` rather than copied manually;
- [ ] principal source, if any, lies inside the project root;
- [ ] project-relative roles are not treated as canonical source properties;
- [ ] every exact evidence file resolves to `corpus/files.tsv` with checksum/preservation state;
- [ ] project-relevant loci are separated from full source extents;
- [ ] reusable crosswalks have one canonical corpus home;
- [ ] source relationships remain evidence-status-controlled in `corpus/relationships.tsv`;
- [ ] generic G1–G6 requirements are referenced, not copied;
- [ ] another capable researcher can identify the historical project root, internal material, external research sources, exact exports, current state and next action without chat.

## Change propagation

### Source identity/structure/file/crosswalk correction

`project discovery → verify → update corpus owner → update affected project consequences → bounded consistency pass`

### Project root correction

If evidence shows that `project_source_id` points to the wrong historical structure, correct the root first. Then re-resolve all project sources through `part_of`; do not manually relabel internal/external rows.

### Project source-use change

Update `projects/<id>/sources/sources.tsv`. A changed role/locus does not change canonical source identity or structural membership.

### Generic methodological weakness

`project observation → project LEARNING/status → explicit generalisability check → methodology/DECISIONS update → bounded consistency pass`

## Project relations

Project-to-project relations are research-organisational only. Historical/documentary structure belongs in `corpus/relationships.tsv`.

A project relation never proves a historical/source relation.

## Closure and restartability

A completed/inactive project remains a scholarly provenance package for its historical source root. If superseded or split because archival understanding changes, record that explicitly.

At any time the repository should answer without chat:
- which historically independent source node defines the project;
- which used sources are structural parts of it;
- which used sources are external comparison/control/context;
- what role/locus each source has in the work;
- which exact exports were used and their preservation state;
- which source relationships are evidenced;
- which gate is active and what the next action is.
