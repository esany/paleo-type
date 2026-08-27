# Project lifecycle and source-group model

## Purpose

Define what a project is, how a source group enters a project, how source-level truth is reused without duplication, and how project findings feed back into corpus and method.

This file is generic METHOD. Concrete project facts belong in `projects/<id>/`; canonical archival-act/source-unit identity, file identity and historical/source relationships belong in `corpus/`.

## Project definition

A **project is a bounded historical investigation / source-unlocking undertaking**: a specific source group investigated for a coherent scholarly purpose.

A project is **not**:
- an archival act/record merely because it exists;
- a protocol/source unit merely because a portal exposes it separately;
- a PDF/export or digital instantiation;
- a technical container for reusable source metadata;
- an automatic one-to-one mirror of `corpus/sources.tsv` or `corpus/source-units.tsv`.

A project may contain one principal source unit and several comparison/control/context units, or several co-equal units. The project boundary follows the research object and source group, not a storage convenience.

## Source hierarchy inside a project

Keep these levels distinct:

`project → source group → archival holding/signature → parent archival act/record → protocol/source unit → relevant locus → digital instantiation`

A shared shelfmark does not collapse genuinely separate archival acts. Conversely, multiple provider/DigiRef records do not automatically imply multiple archival acts: a provider may expose separate protocols or sections inside one act as separate digital records.

Establish provider-record granularity from archival context before assigning canonical ownership. One parent act may contribute several project source units, each with a different project role.

## Canonical ownership

One fact has one canonical owner:

- parent archival act/record identity and archival description → `corpus/sources.tsv`;
- reusable protocol/source-unit identity, title, extent and unit-level provider identifiers → `corpus/source-units.tsv`;
- exact digital/export file identity, filename, checksum, coverage, storage state, rights and optional unit linkage → `corpus/files.tsv`;
- reusable parent-act image/PDF/export/folio crosswalk → `corpus/source-data/<source_id>/`, with `source_unit_id` on rows where membership is evidenced;
- historical/archival/textual source/unit relationships → `corpus/relationships.tsv`;
- project source-unit membership, project-relative function and project-relevant locus → `projects/<id>/sources/sources.tsv`;
- project inspection events/details → `projects/<id>/sources/inspection-log.tsv` when needed;
- project transcription/decisions/analysis/status → that project;
- research-organisational project-to-project relations → `projects/relationships.tsv` only when multiple genuine projects exist and a material relation needs recording;
- generic project/source-group rules → this file and `templates/project/`.

A project references canonical act/unit/file records; it does not redefine them. Reusable crosswalks are not copied into every project.

## Original source exports are first-class research assets

The exact PDF/image export actually used for research is part of the evidential chain. A portal URL or URN is useful provenance but is **not a substitute for preserving the exact inspected export**.

For central project source exports:
- preserve the original filename and exact bytes;
- record SHA-256 in `corpus/files.tsv`;
- record parent `source_id` and `source_unit_id` when the export specifically instantiates a known unit;
- record the intended/actual repository path;
- do not modify, recompress, OCR-overwrite or normalize the preserved original;
- derived crops/renders/OCR belong separately and must point back to the original file ID;
- if a public-repository rights constraint prevents committing the binary, mark preservation as incomplete/blocked explicitly rather than pretending a URL/URN is equivalent backup.

The project is not restartable if its consequential source evidence depends on a transient chat attachment or an unrecorded local file.

## Minimal project contract

Create every new project from `templates/project/`, never by cloning an existing concrete project.

Required at creation:
1. unique project ID and human-readable title;
2. bounded `research_object` / `active_scope` describing the investigation, not a storage unit;
3. `sources/sources.tsv` listing the actual source group and each project's use of each protocol/source unit or, if not yet delimited, parent act;
4. every referenced parent `source_id` exists in `corpus/sources.tsv` and every claimed `source_unit_id` exists in `corpus/source-units.tsv` under that parent;
5. every exact digital export used as evidence exists in `corpus/files.tsv` with checksum and storage/preservation state;
6. `STATUS.md` records actual evidence state and a bounded `NEXT ACTION`;
7. generic gates/method are referenced rather than copied;
8. no empty future-proof directories.

Optional directories are created only when real work exists: `transcription/`, `apparatus/`, `palaeography/`, `research/`, `context/`, `LEARNINGS.md`.

## Project source register

`projects/<id>/sources/sources.tsv` is the human-readable source-group entry point.

Required columns:

`source_id | source_unit_id | archival_title | source_unit_title | project_role | relevant_locus | primary_file_id | status | notes`

Semantically, each row is a **project-to-source-unit/use relation plus its project-relative function and locus**, not an additional properties record for the act or unit. Canonical act/unit identity stays in the corpus; function may differ legitimately between investigations.

Rules:
- one row represents one project use of a canonical protocol/source unit, or a parent act only while the relevant unit is genuinely unresolved;
- multiple rows may share one parent `source_id` when distinct source units from the same act are used;
- keep genuinely separate parent acts separate even when they share archive, fonds or signature;
- do not manufacture separate parent acts from different provider record IDs until archival context establishes that granularity;
- `project_role` describes the function of that unit/source use **in this investigation** (`principal`, `comparison`, `control`, `context`, etc.); it is project-relative and is not part of canonical identity;
- the same canonical unit may occur in another project's source register with a different `project_role` without changing corpus identity;
- `comparison` means “used for comparison in this investigation”; it does not assert textual correspondence or dependence;
- `relevant_locus` is project-specific and does not redefine the unit's full extent;
- `primary_file_id` points to `corpus/files.tsv` and must match the parent act and, when declared there, the unit;
- source relationships are not encoded here as historical facts; use `corpus/relationships.tsv` with evidence status.

## Project creation procedure

Before creating a project:
1. define the historical investigation / source-unlocking object;
2. identify the bounded source group needed for it;
3. verify/create parent archival acts in `corpus/sources.tsv`;
4. identify/create reusable protocol/source units in `corpus/source-units.tsv` at the granularity actually evidenced;
5. register exact available source exports in `corpus/files.tsv` and establish preservation state;
6. instantiate `project.yml`, `STATUS.md`, and `sources/sources.tsv` from the generic template;
7. add only directories required by actual work;
8. add a project-to-project relation only if another genuine project is materially involved;
9. run the Project Creation Check and source-contract validation.

Do not create a project simply because a new archival act, provider-side protocol record or PDF was discovered.

## Project Creation Check

A project is valid only if all applicable checks pass:

- [ ] project ID identifies an investigation, not a source/file surrogate;
- [ ] research object and active scope are understandable to a historian without internal architecture knowledge;
- [ ] source group is explicit in `sources/sources.tsv`;
- [ ] parent acts and protocol/source units are not conflated;
- [ ] multiple units inside one act do not become false separate acts because provider IDs differ;
- [ ] project-relative source functions are not treated as canonical source properties;
- [ ] every parent source ID resolves to `corpus/sources.tsv`;
- [ ] every declared source-unit ID resolves to `corpus/source-units.tsv` and belongs to the stated parent;
- [ ] every exact evidence file resolves to `corpus/files.tsv`, has a checksum and is linked to the correct act/unit where applicable;
- [ ] central original exports have an explicit preservation state and repository path/blocked reason;
- [ ] project-relevant loci are separated from full source-unit extents;
- [ ] reusable crosswalks have one canonical parent-act source-data home;
- [ ] stable URNs are recorded only when institutionally evidenced, never synthesized from patterns;
- [ ] source relationships remain in `corpus/relationships.tsv`;
- [ ] project relations are used only between genuine research projects;
- [ ] generic G1-G6 requirements are referenced, not copied;
- [ ] no speculative empty directories were created;
- [ ] another capable researcher can identify the investigation, parent acts, source units, exact exports, current state and next action without chat.

If the same machine-checkable creation error recurs, that is evidence for the smallest validation that catches it; do not automate pre-emptively.

## Change propagation and anti-drift

### Act/unit/file/crosswalk correction

`project discovery → verify archival/provider granularity → update corpus owner → update only affected project references/consequences → bounded consistency pass`

Never repair a source fact only in one project's copy.

### Project source-group change

Update `projects/<id>/sources/sources.tsv` first, then project status/work products whose scope changes. A change of project-relative function or locus does not by itself change canonical act/unit identity or source-to-source relationships.

### Generic methodological weakness

`project observation → project LEARNING/status → explicit generalisability check → methodology/DECISIONS update → bounded consistency pass`

A pilot tests method; it does not silently define method.

## Project relations

Projects may have research-organisational relations such as `extends`, `shares-sources-with`, `provides-results-to` or other observed needs. Record them in `projects/relationships.tsv` only when there are multiple genuine investigations and the relation materially helps navigation or dependency tracking.

A project relation never proves a historical/source relation.

## Closure and restartability

A completed/inactive project remains a scholarly provenance package. If superseded, state the successor explicitly; do not silently merge histories.

At any time the repository should answer without chat:
- what the project investigates;
- which parent archival acts contain its source group;
- which protocol/source units are actually used;
- what project-relative function/locus each unit has;
- which exact original exports were used and where they are preserved;
- which persistent identifiers/URNs are actually evidenced and which remain missing;
- which source/unit relationships are actually evidenced;
- what was inspected/read/decided;
- which generic gate is active;
- what the exact next research action is.

If those answers require interpreting artificial source-as-project containers, conflated act/unit identities, or recovering transient chat files, the model has drifted and must be repaired.
