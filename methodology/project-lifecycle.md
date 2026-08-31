# Project lifecycle and historical-source project model

## Purpose

Define what a project is, how its historical source structure is anchored, how Project→Source research use is represented, and how project work reuses canonical corpus truth without duplication.

This file is generic METHOD. Canonical source identity/relations/files live in `corpus/`; project work state lives in `projects/<id>/`.

## Project definition

A **project is anchored to one historically independent source structure**, represented by exactly one canonical `project_source_id` in `project.yml`.

In the current corpus that root is an archival act. The rule is structural rather than technical: the project boundary follows the historically independent documentary unit, not a convenient research bundle, portal export, PDF, place name or current question.

A project may work only on a small locus of its root structure at a given time. `active_scope` is therefore allowed to be narrower than the project itself.

A project may also use sources outside its root structure for comparison, control or context. Those sources remain **external** to the project even though they are used in its research.

## Structural membership

Historical/documentary source nodes live in `corpus/sources.tsv`. Structural containment is represented generically in `corpus/relationships.tsv` with `part_of`.

For a source `S` and project root `R`:

- `S = R` → project root;
- `S part_of* R` → structurally internal source;
- otherwise, when used by the project → external research source.

No separate canonical `internal/external` field is required. The resolver derives `structural_status` deterministically from `project_source_id` plus the canonical `part_of` graph.

This preserves the distinction between:

- **historical structure** — Source→Source `part_of` relations;
- **research use** — Project→Source research functions.

A source can be external to a project and still be important or even decisive as comparison/control evidence.

## Canonical ownership

One fact has one canonical owner:

- source identity/type/description → `corpus/sources.tsv`;
- historical/documentary structure and other Source→Source claims → `corpus/relationships.tsv`;
- exact digital/export file identity, checksum, coverage, storage state and rights → `corpus/files.tsv`;
- reusable source-wide image/PDF/export/folio crosswalk → `corpus/source-data/<source_id>/`;
- project root identity → `project.yml: project_source_id`;
- Project→Source research function and source-relative relevant locus → `projects/<id>/source-uses.tsv`;
- concrete Project-use→File evidence binding → `projects/<id>/research/use-evidence.tsv` when actually needed;
- project inspection details → project source/inspection records when needed;
- project transcription/decisions/analysis/status → that project;
- generic rules → `methodology/` and consequential cross-project decisions → `DECISIONS.md`.

A project references canonical Source/File nodes; it does not redefine them.

## Project→Source use

The target project-local use table is:

`use_id | source_id | research_function | relevant_locus | status | evidence_basis | notes`

Each row represents **one concrete research function of one canonical Source in one Project**.

Rules:

- `use_id` is unique;
- `source_id` resolves to `corpus/sources.tsv`;
- one use row expresses one `research_function`;
- the same Source may have multiple use rows/functions in the same Project;
- `research_function` is project-relative, open vocabulary and never a Source property;
- functions are not inferred automatically from source type, `part_of`, another project, shared event or textual similarity;
- `principal` is a research function, not a project boundary or Source identity;
- `relevant_locus` is the source-relative scholarly scope of that use and does not redefine the Source's full extent;
- Project→Source use never creates a Project→Project relation.

The validator controls only syntax/referential integrity, not a closed function ontology or specialist research judgement.

### Research function is not current work priority

Keep four states distinct:

```text
SOURCE / FILE IDENTITY                 what historical/digital object this is
PROJECT STRUCTURAL STATUS              root | internal | external, derived from source structure
PROJECT→SOURCE RESEARCH FUNCTION       principal | comparison | control | context | other evidenced function
CURRENT WORK TARGET / NEXT ACTION      which source/question is to be worked on now
```

Correct identity or structural status does not authorize a research function, and a research function does not select the current work target. In particular, `project_source_id`, `principal`, source availability, upload order, newly verified metadata, an exact-file match, or a technical/architecture fixture must not silently promote that Source into the current scholarly priority.

The current work target must be traceable to the project's owner-grounded `research_object` / `active_scope` or to an explicit later purpose/priority/scope decision. A supporting prerequisite may be completed without becoming the research objective that it supports.

An external `comparison` or `control` Source may legitimately be the current work target while an internal `principal` Source remains the principal witness. Current priority therefore must not be reconstructed from structural membership or the label `principal`.

If satisfying a provenance, access, migration, architecture or other support prerequisite would materially redirect the active source/question, stop the priority change. Preserve the completed support work, compare the proposed new target against the owner-grounded research purpose/current scope, and require an explicit purpose/priority/scope basis before changing `active_scope` or `NEXT ACTION`. Internal consistency among self-authored project files is not sufficient evidence that such a priority change was authorized.

## Use-specific digital evidence — Variant B

Concrete File/Image evidence is separate from Project→Source research function.

When a specific use actually depends on a concrete digital instantiation, record minimally:

`evidence_id | use_id | file_id | evidence_locator | status | evidence_basis | notes`

Rules:

- `use_id` resolves to one Project→Source use in the same Project;
- `file_id` resolves to `corpus/files.tsv`;
- the canonical Source owning that File in `corpus/files.tsv` must equal the `source_id` of the referenced use; use-evidence is a concrete instantiation binding for that Source, not cross-Source claim evidence;
- `corpus/files.tsv` remains the sole owner of file identity, filename, SHA-256, coverage, storage/preservation and rights provenance;
- use-evidence records only that this concrete use actually used this concrete file/instantiation;
- one use may have zero, one or many evidence rows;
- one file may support zero, one or many uses of its own Source;
- evidence is never inferred from Source membership, `part_of` or mere file availability;
- do not duplicate `source_id` in use-evidence when it is deterministically recoverable through `use_id`.

### Source-relative locus vs digital locator

These are different facts:

- `source-uses.relevant_locus` = source-relative scholarly scope, e.g. `306v-309r`;
- `use-evidence.evidence_locator` = locator inside the concrete used digital instantiation, when needed.

Do not create a second independent folio truth in use-evidence. Prefer the canonical source-wide crosswalk when it already maps folio ↔ export image ↔ PDF page ↔ evidenced URN.

## Minimal project contract for new projects

Create new projects from `templates/project/`.

Required at creation:

1. unique project ID and human-readable title;
2. exactly one `project_source_id` resolving to the historically independent project root in `corpus/sources.tsv`;
3. a scholarly `research_object` and bounded `active_scope` within that root;
4. `source-uses.tsv` for actual Project→Source research uses, created/populated only as use exists;
5. every referenced Source ID exists in `corpus/sources.tsv`;
6. every exact digital export used as evidence exists in `corpus/files.tsv` with checksum and preservation state;
7. use-evidence exists only for concrete Project-use→File bindings that are actually needed;
8. `STATUS.md` records evidence state and one bounded `NEXT ACTION`;
9. generic gates/method are referenced rather than copied;
10. no empty future-proof research/source-work structures.

A new project does not require a `principal` use at creation.

## Legacy compatibility during the Reg. Ii 5 migration boundary

The current Reg. Ii 5 project still stores Project→Source use in `sources/sources.tsv` with `project_role`, `relevant_locus` and `primary_file_id`, and also has `project.yml: principal_source_id`.

Phase 1 deliberately keeps those records unchanged until the separately reviewed loss-checked migration is admitted.

During this transition:

- the validator/resolver may read the legacy register so current research state remains valid and restartable;
- target `source-uses.tsv` / `use-evidence.tsv` records are validated independently when present;
- legacy `primary_file_id` is **not** automatically materialized as target use-evidence;
- `principal_source_id` may remain temporarily as migration compatibility but is not a target structural invariant beyond `project_source_id`;
- the migration specification must preserve every current `primary_file_id` as `old project-source row → new use_id → use-evidence → same file_id` before legacy fields are removed.

This compatibility is a transition, not permission to maintain two permanent canonical truths.

## Current regression example

The current Reg. Ii 5 project is rooted at:

`ACT-THHSTAW-EGA-REG-II-5`

Its Ziegenrück protocol `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129` is structurally internal because it is `part_of` that act.

The related Reg. Ii 4 Bd. II and Reg. Ii 3 sources are external research sources because their `part_of` ancestry terminates in different historical roots.

The current Knau focus remains active scope/pilot/falsification fixture; it does not redefine the project root. The external Reg. Ii 4 comparison locus may be the current scholarly work target without changing either project root or the Reg. Ii 5 principal-witness function.

## Original source exports

The exact PDF/image export actually used for research is part of the evidential chain. A portal URL or URN is useful provenance but is not a substitute for the exact inspected export.

For consequential project source exports:

- preserve original filename and exact bytes when rights permit;
- record SHA-256 in `corpus/files.tsv`;
- record coverage and preservation state;
- keep derivatives separate;
- if public-repository rights block preservation, state that explicitly;
- project use-evidence references `file_id` rather than copying file metadata.

## Project creation procedure

Before creating a project:

1. identify the historically independent source structure that will be the project root;
2. verify/create that canonical Source node and necessary `part_of` relations in the corpus;
3. set `project_source_id` to that root;
4. identify only the Project→Source research uses actually needed;
5. create one use row per concrete research function;
6. register exact source exports in `corpus/files.tsv` and explicit use-evidence only where actually used;
7. instantiate `project.yml`, `STATUS.md`, and needed use records;
8. run `python tools/source_contract.py validate`;
9. use the resolver rather than reconstructing structural membership or file evidence from names/chat.

Do not create a project merely because a PDF, protocol fragment, place, question or temporary comparison task exists. Materialize a project when a historically independent source structure requires its own durable scholarly state.

## Project validation check

A project is valid only if all applicable checks pass:

- [ ] `project_source_id` resolves to one canonical historical Source root;
- [ ] project identity follows historical structure, not current narrow locus or research convenience;
- [ ] active scope may be narrower but is explicit;
- [ ] every Project→Source use resolves to `corpus/sources.tsv`;
- [ ] internal/external status is derived from `part_of` rather than copied;
- [ ] multiple research functions for one Source remain representable;
- [ ] research functions are not treated as canonical Source properties;
- [ ] current work target is not inferred from `project_source_id`, structural status, research-function labels, file availability/upload order or support fixtures;
- [ ] a consequential change of `active_scope` / `NEXT ACTION` is traceable to owner-grounded purpose/priority/scope rather than repository self-consistency alone;
- [ ] each explicit use-evidence File resolves to `corpus/files.tsv` and belongs to the same canonical Source as the referenced use;
- [ ] exact File identity/provenance is not duplicated in Project use records;
- [ ] source-relative relevant locus is distinct from digital evidence locator;
- [ ] reusable crosswalks have one canonical corpus home;
- [ ] Source→Source claims remain evidence-status-controlled in `corpus/relationships.tsv`;
- [ ] no Project→Project relation is inferred from Project→Source use;
- [ ] generic G1–G6 requirements are referenced, not copied;
- [ ] another capable researcher can identify project root, structural status, research functions, exact evidence files, current state and next action without chat.

No duplicate-project-root or ancestor/descendant-root prohibition is implied by this checklist.

## Change propagation

### Source identity/structure/file/crosswalk correction

`project discovery → verify → update corpus owner → update affected project consequences → bounded consistency pass`

### Project root correction

If evidence shows that `project_source_id` points to the wrong historical structure, correct the root first. Then re-resolve Project sources through `part_of`; do not manually relabel internal/external records.

### Project source-use change

Update the relevant `source-uses.tsv` row(s). A changed function/locus does not change canonical Source identity or structural membership.

If concrete digital evidence for a use changes, update use-evidence while keeping File identity/provenance in `corpus/files.tsv` and keeping the File bound to a use of its own canonical Source.

A change in source use, evidence availability or technical support does not by itself authorize a change in current research priority. Synchronize `active_scope` / `STATUS.md` only from an owner-grounded purpose/priority/scope basis.

### Generic methodological weakness

`project observation → project LEARNING/status → explicit generalisability check → methodology/DECISIONS update → bounded consistency pass`

## Project relations

Project→Project relations are explicit research-organisational relations only. Historical/documentary structure and textual/source claims belong in `corpus/relationships.tsv`.

Using a Source that belongs structurally to another Project root never auto-creates a Project→Project relation.

## Closure and restartability

A completed/inactive project remains a scholarly provenance package for its historical Source root. If superseded or split because archival understanding changes, record that explicitly.

At any time the repository should answer without chat:

- which historically independent Source node defines the Project;
- which Sources are structurally internal or external by derivation;
- which concrete research functions each used Source serves;
- what source-relative loci matter;
- which exact digital files actually support which uses;
- which Source→Source claims are evidenced;
- which gate is active and what the next action is;
- which owner-grounded purpose/priority/scope basis authorizes the current work target when it changed materially.