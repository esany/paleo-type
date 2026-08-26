# Project lifecycle and source-group model

## Purpose

Define what a project is, how a source group enters a project, how source-level truth is reused without duplication, and how project findings feed back into corpus and method.

This file is generic METHOD. Concrete project facts belong in `projects/<id>/`; canonical source identity, file identity and historical/source relationships belong in `corpus/`.

## Project definition

A **project is a bounded historical investigation / source-unlocking undertaking**: a specific source group investigated for a coherent scholarly purpose.

A project is **not**:
- an archival record merely because it exists;
- a PDF/export or digital instantiation;
- a technical container for reusable source metadata;
- an automatic one-to-one mirror of `corpus/sources.tsv`.

A project may contain one principal source and several comparison/control/context sources, or several co-equal sources. The project boundary follows the research object and source group, not a storage convenience.

Example: a Knau project may investigate a 1533 principal witness together with a related 1533 record and distinct 1529 control/context records. Those records remain separate sources inside one project unless a genuinely separate research undertaking is opened.

## Source hierarchy inside a project

Keep these levels distinct:

`project → source group → archival record/source → relevant locus → digital instantiation`

A shared shelfmark does not collapse distinct archival records. If an archival volume contains separately catalogued/identified records or source sections, preserve each record's own canonical `source_id`, archival title, record ID and locus.

For example, two distinct Reg. Ii 3 records remain two project sources even though both belong to the same archival volume/signature.

## Canonical ownership

One fact has one canonical owner:

- source/record identity and archival description → `corpus/sources.tsv`;
- exact digital/export file identity, filename, checksum, coverage, storage state and rights → `corpus/files.tsv`;
- reusable source-wide image/PDF/export/folio crosswalk → `corpus/source-data/<source_id>/`;
- historical/archival/textual source relationships → `corpus/relationships.tsv`;
- project membership, project role and project-relevant locus → `projects/<id>/sources/sources.tsv`;
- project inspection events/details → `projects/<id>/sources/inspection-log.tsv` when needed;
- project transcription/decisions/analysis/status → that project;
- research-organisational project-to-project relations → `projects/relationships.tsv` only when multiple genuine projects exist and a material relation needs recording;
- generic project/source-group rules → this file and `templates/project/`.

A project references canonical source/file records; it does not redefine them. Reusable source-wide crosswalks are not copied into every project.

## Original source exports are first-class research assets

The exact PDF/image export actually used for research is part of the evidential chain. A portal URL or URN is useful provenance but is **not a substitute for preserving the exact inspected export**.

For central project source exports:
- preserve the original filename and exact bytes;
- record SHA-256 in `corpus/files.tsv`;
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
3. `sources/sources.tsv` listing the actual source group and each source's role/locus;
4. every referenced canonical source ID already exists in `corpus/sources.tsv`;
5. every exact digital export used as evidence exists in `corpus/files.tsv` with checksum and storage/preservation state;
6. `STATUS.md` records actual evidence state and a bounded `NEXT ACTION`;
7. generic gates/method are referenced rather than copied;
8. no empty future-proof directories.

Optional directories are created only when real work exists: `transcription/`, `apparatus/`, `palaeography/`, `research/`, `context/`, `LEARNINGS.md`.

## Project source register

`projects/<id>/sources/sources.tsv` is the human-readable source-group entry point.

Required columns:

`source_id | archival_title | project_role | relevant_locus | primary_file_id | status | notes`

Rules:
- one row represents one canonical archival/source record used by the project;
- keep separately identified archival records separate even when they share archive, fonds or signature;
- `project_role` describes use in this investigation (`principal`, `comparison`, `control`, `context`, etc.) and is not part of source identity;
- `relevant_locus` is project-specific and does not redefine the source's full archival extent;
- `primary_file_id` points to `corpus/files.tsv`; additional files may be found there by `source_id`;
- source relationships are not encoded here as historical facts; use `corpus/relationships.tsv` with evidence status.

## Project creation procedure

Before creating a project:
1. define the historical investigation / source-unlocking object;
2. identify the bounded source group needed for it;
3. verify/create canonical source records in `corpus/sources.tsv`;
4. register exact available source exports in `corpus/files.tsv` and establish preservation state;
5. instantiate `project.yml`, `STATUS.md`, and `sources/sources.tsv` from the generic template;
6. add only directories required by actual work;
7. add a project-to-project relation only if another genuine project is materially involved;
8. run the Project Creation Check.

Do not create a project simply because a new archival record was discovered or a PDF was uploaded.

## Project Creation Check

A project is valid only if all applicable checks pass:

- [ ] project ID identifies an investigation, not a source/file surrogate;
- [ ] research object and active scope are understandable to a historian without internal architecture knowledge;
- [ ] source group is explicit in `sources/sources.tsv`;
- [ ] distinct archival records/sections remain distinct source rows;
- [ ] every source ID resolves to `corpus/sources.tsv`;
- [ ] every exact evidence file resolves to `corpus/files.tsv` and has a checksum;
- [ ] central original exports have an explicit preservation state and repository path/blocked reason;
- [ ] project-relevant loci are separated from full source extents;
- [ ] reusable source-wide crosswalks have one canonical corpus source-data home;
- [ ] source relationships remain in `corpus/relationships.tsv`;
- [ ] project relations are used only between genuine research projects;
- [ ] generic G1-G6 requirements are referenced, not copied;
- [ ] no speculative empty directories were created;
- [ ] another capable researcher can identify the investigation, source group, exact exports, current state and next action without chat.

If the same machine-checkable creation error recurs, that is evidence for the smallest validation that catches it; do not automate pre-emptively.

## Change propagation and anti-drift

### Source identity/file/crosswalk correction

`project discovery → verify → update corpus owner → update only affected project references/consequences → bounded consistency pass`

Never repair a source fact only in one project's copy.

### Project source-group change

Update `projects/<id>/sources/sources.tsv` first, then project status/work products whose scope changes. Do not change canonical source identity merely because project role changes.

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
- which distinct archival records form its source group;
- what role/locus each source has in the project;
- which exact original exports were used and where they are preserved;
- which source relationships are actually evidenced;
- what was inspected/read/decided;
- which generic gate is active;
- what the exact next research action is.

If those answers require interpreting artificial source-as-project containers or recovering transient chat files, the model has drifted and must be repaired.