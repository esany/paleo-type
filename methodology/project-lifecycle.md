# Project lifecycle and historical-source project model

## Purpose

Define how a human-owner-defined Project is anchored to historical Source structure, how Project→Source research use is represented, and how project work reuses canonical corpus truth without duplication.

This file is generic METHOD. Canonical source identity/relations/files live in `corpus/`; project work state lives in `projects/<id>/`.

## Project definition and authority

**Project existence and Project boundary are human-owner decisions.** A Source, archival act, protocol, PDF, place, current question, available export or AI-organized working bundle does not become a Project merely because it exists or is structurally identifiable.

Once the owner has decided that a Project exists, it is anchored to exactly one canonical historical Source root through `project_source_id`. That anchor makes the Project structurally reconstructable; it does not create the Project and does not choose the research priority.

For the current church-visitation corpus, the owner has explicitly chosen one Project per act: Reg. Ii 3, Reg. Ii 4 Bd. II and Reg. Ii 5. Their internal protocol/section nodes remain Sources related by `part_of`. Preserved Knau-related work remains valid historical/research state, but no current scholarly scope is inferred from that history.

The source-root rule is therefore structural, not generative: after Project selection, `project_source_id` should point to the historically independent documentary unit that anchors that Project. Current scope may be narrower than the whole root or explicitly unset until an owner-grounded question activates it.

A Project may also use Sources outside its root structure for comparison, control or context. Those Sources remain **external** to the Project even though they are used in its research.

## Structural membership

Historical/documentary Source nodes live in `corpus/sources.tsv`. Structural containment is represented generically in `corpus/relationships.tsv` with `part_of`.

For a Source `S` and an already established Project root `R`:

- `S = R` → Project root;
- `S part_of* R` → structurally internal Source;
- otherwise, when used by the Project → external research Source.

No separate canonical `internal/external` field is required. The resolver derives `structural_status` deterministically from `project_source_id` plus the canonical `part_of` graph.

This preserves the distinction between:

- **Project authority** — whether/what Project the human owner has chosen;
- **historical structure** — Source→Source `part_of` relations;
- **research use** — Project→Source research functions;
- **current work priority** — which bounded question/locus is worked on now.

A Source can be external to a Project and still be important or decisive as comparison/control evidence. A Source can also be structurally internal without having any currently active research function.

## Canonical ownership

One fact has one canonical owner:

- Source identity/type/description → `corpus/sources.tsv`;
- historical/documentary structure and other Source→Source claims → `corpus/relationships.tsv`;
- exact digital/export File identity, checksum, coverage, storage state and rights → `corpus/files.tsv`;
- reusable source-wide image/PDF/export/folio crosswalk → `corpus/source-data/<source_id>/`;
- owner-defined Project identity/purpose/root/current bounded scope → `project.yml`;
- Project→Source research function and source-relative relevant locus → `projects/<id>/source-uses.tsv`;
- concrete Project-use→File evidence binding → `projects/<id>/research/use-evidence.tsv` when actually needed;
- Project inspection/details/results/decisions/status → that Project;
- generic rules → `methodology/` and consequential cross-project decisions → `DECISIONS.md`.

A Project references canonical Source/File nodes; it does not redefine them.

## Project→Source use

The canonical project-local use table is:

`use_id | source_id | research_function | relevant_locus | status | evidence_basis | notes`

Each row represents **one concrete research function of one canonical Source in one Project**.

Rules:

- `use_id` is unique;
- `source_id` resolves to `corpus/sources.tsv`;
- one use row expresses one `research_function`;
- the same Source may have multiple use rows/functions in the same Project;
- `research_function` is Project-relative, open vocabulary and never a Source property;
- functions are not inferred automatically from Source type, `part_of`, another Project, shared event or textual similarity;
- functions are dynamic: they may change as the investigation changes, with consequential changes preserved rather than silently rewritten;
- historical uses may remain explicitly historical so prior work-state survives without being promoted to current scope;
- `principal` is a research function, not a Project boundary, Source identity or priority selector;
- `relevant_locus` is the source-relative scholarly scope of that use and does not redefine the Source's full extent;
- Project→Source use never creates a Project→Project relation.

The validator controls only syntax/referential integrity, not a closed function ontology or specialist research judgement.

### Research function is not current work priority

Keep five states distinct:

```text
PROJECT AUTHORITY                         what the human owner has decided is a Project
SOURCE / FILE IDENTITY                    what historical/digital object this is
PROJECT STRUCTURAL STATUS                 root | internal | external, derived after Project selection
PROJECT→SOURCE RESEARCH FUNCTION          principal | comparison | control | context | other evidenced function
CURRENT WORK TARGET / NEXT ACTION         which source/question is to be worked on now
```

Correct Source/File identity or structural status does not authorize a research function; a research function does not select the current work target; and no combination of canonical Source facts can itself create a Project.

In particular, `project_source_id`, `principal`, Source availability, upload order, newly verified metadata, an exact-File match, a technical/architecture fixture or an inherited AI-created `active_scope` must not silently become owner authority for Project identity or current scholarly priority.

The current work target must be traceable to the owner-grounded Project purpose/current scope or to an explicit later purpose/priority/scope decision. A supporting prerequisite may be completed without becoming the research objective that it supports.

An external `comparison` or `control` Source may legitimately be a current work target while an internal `principal` Source remains the principal witness. Conversely, a historical comparison/control label may remain useful as provenance without being the present task.

If owner grounding for Project existence/boundary or a materially changed current target is absent, **do not infer it from the repository's internal consistency**. Preserve the evidence/work already completed, record the missing authority state, and stop only the unsupported Project/scope/priority mutation; ordinary bounded work whose authority is already established may continue.

## Use-specific digital evidence — Variant B

Concrete File/Image evidence is separate from Project→Source research function.

When a specific use actually depends on a concrete digital instantiation, record minimally:

`evidence_id | use_id | file_id | evidence_locator | status | evidence_basis | notes`

Rules:

- `use_id` resolves to one Project→Source use in the same Project;
- `file_id` resolves to `corpus/files.tsv`;
- the canonical Source owning that File in `corpus/files.tsv` must equal the `source_id` of the referenced use; use-evidence is a concrete instantiation binding for that Source, not cross-Source claim evidence;
- `corpus/files.tsv` remains the sole owner of File identity, filename, SHA-256, coverage, storage/preservation and rights provenance;
- use-evidence records only that this concrete use actually used this concrete File/instantiation;
- one use may have zero, one or many evidence rows;
- one File may support zero, one or many uses of its own Source;
- evidence is never inferred from Source membership, `part_of` or mere File availability;
- do not duplicate `source_id` in use-evidence when it is deterministically recoverable through `use_id`.

### Source-relative locus vs digital locator

These are different facts:

- `source-uses.relevant_locus` = source-relative scholarly scope, e.g. `306v-309r`;
- `use-evidence.evidence_locator` = locator inside the concrete used digital instantiation, when needed.

Do not create a second independent folio truth in use-evidence. Prefer the canonical source-wide crosswalk when it already maps folio ↔ export image ↔ PDF page ↔ evidenced URN.

Identifier availability is Source/File-specific. A page-level URN present for one export must not be assumed absent or present for another; preserve exactly what the inspected/provider evidence supports.

## Minimal project contract for new Projects

Create new Projects from `templates/project/` **only after the human owner has decided that a Project should be created and has supplied/confirmed its research purpose/boundary at the level that cannot be derived**.

After that owner decision, routine repository mechanics are assistant/system responsibilities.

Required at creation:

1. owner-confirmed Project existence/boundary and scholarly purpose;
2. unique Project ID and human-readable title;
3. exactly one `project_source_id` resolving to the canonical Source root that anchors the owner-defined Project;
4. a scholarly `research_object` and bounded `active_scope`; the scope may be narrower than the whole Project Source and may explicitly remain unset until a research question is selected;
5. `source-uses.tsv` for actual Project→Source research uses, created/populated only as use exists;
6. every referenced Source ID exists in `corpus/sources.tsv`;
7. every exact digital export used as evidence exists in `corpus/files.tsv` with checksum and preservation state;
8. use-evidence exists only for concrete Project-use→File bindings that are actually needed;
9. `STATUS.md` records evidence/work state and a bounded `NEXT ACTION` only when an authorized next action exists;
10. generic gates/method are referenced rather than copied;
11. no empty future-proof research/source-work structures.

A new Project does not require a `principal` use at creation and does not require a manuscript NEXT ACTION to be invented merely to make the Project look active.

## Reg. Ii 5 completed structured-use migration and remaining legacy path

Reg. Ii 5 still lives under the legacy directory/id `ega-reg-ii-5-knau`, but the old Project→Source register `sources/sources.tsv` and `project.yml: principal_source_id` are no longer canonical compatibility owners. Their four evidenced Knau-era Project→Source functions have been loss-checked into `source-uses.tsv`, and the same four exact File bindings have been preserved in `research/use-evidence.tsv`.

The migrated uses are explicitly historical work-state. Their former `active` / `identified` labels and role meanings remain recoverable through the migration record and current historical use rows; they do **not** establish a current Knau scope, current `principal` priority or current manuscript NEXT ACTION.

The old register was removed only after the target representation and exact File bindings were present and regression-protected. The executed migration record remains in `research/project-source-migration.tsv`; it distinguishes completed structured-use cleanup from still-deferred G2 transcription/line/span/phenomenon migration.

The remaining `ega-reg-ii-5-knau` directory/id is therefore a path/history compatibility issue only. Any later path/reference rename must be separately loss-checked so research references, provenance, STATUS/recovery pointers and scholarly history remain intact.

## Current visitation-project example

The current owner-defined Projects are:

- Reg. Ii 3 → `ACT-THHSTAW-EGA-REG-II-3`;
- Reg. Ii 4 Bd. II → `ACT-THHSTAW-EGA-REG-II-4-BD-II`;
- Reg. Ii 5 → `ACT-THHSTAW-EGA-REG-II-5`.

Within Reg. Ii 3, the currently known internal Source nodes include both the Neustadt visitation at fol. 41r–63v and the Pfarreinkommen section at fol. 303r–306r. They are two internal sections of one owner-defined Li 3 Project, not two Projects merely because they have separate record IDs/exports.

Reg. Ii 4 Bd. II and Reg. Ii 5 likewise have their currently identified internal Ziegenrück Source nodes. Cross-act comparison/correspondence does not merge the Projects and does not fix permanent `principal/comparison/control/context` roles.

The preserved Reg. Ii 5/Knau work remains valid project work and a G2 falsification fixture. Its historical role/use records are retained as historical state, not as current scope. `Knau` does not define any of the three Project identities.

## Original source exports

The exact PDF/image export actually used for research is part of the evidential chain. A portal URL or URN is useful provenance but is not a substitute for the exact inspected export.

For consequential Project source exports:

- preserve original filename and exact bytes when rights permit;
- record SHA-256 in `corpus/files.tsv`;
- record coverage and preservation state;
- keep derivatives separate;
- if public-repository rights block preservation, state that explicitly;
- Project use-evidence references `file_id` rather than copying File metadata.

Identifiability and reproducibility do not automatically establish that the evidence is accessible in the current authorized work context. Direct source work must separately verify research-ready availability.

## Project creation procedure

Before creating a Project:

1. **obtain/record the human-owner decision that this should be a Project and its intended scholarly boundary/purpose**;
2. identify the canonical historical Source structure that best anchors that owner-defined boundary;
3. verify/create that canonical Source node and necessary `part_of` relations in the corpus;
4. set `project_source_id` to that root;
5. identify only the Project→Source research uses actually needed; do not turn structural membership into a role;
6. register exact source exports in `corpus/files.tsv` and explicit use-evidence only where actually used;
7. instantiate `project.yml`, `STATUS.md`, and needed use records;
8. recover/migrate consequential prior work-state/checkpoint information if this Project supersedes an older organization;
9. run `python tools/source_contract.py validate`;
10. use the resolver and generated read-only context/intake helpers rather than reconstructing structural membership, File evidence or current scope from names/chat.

Do not create a Project merely because a PDF, protocol fragment, archival act, place, question, current source group or temporary comparison task exists. Source discovery/intake may remain Corpus-only until the owner chooses Project routing.

## Project validation check

A Project is valid only if all applicable checks pass:

- [ ] Project existence/boundary/purpose has a human-owner authority basis rather than being inferred from Source structure or AI convenience;
- [ ] `project_source_id` resolves to the canonical historical Source root anchoring that owner-defined Project;
- [ ] narrow `active_scope` does not silently redefine Project identity;
- [ ] every Project→Source use resolves to `corpus/sources.tsv`;
- [ ] internal/external status is derived from `part_of` rather than copied;
- [ ] multiple/dynamic research functions for one Source remain representable;
- [ ] historical research functions remain distinguishable from current active scope;
- [ ] research functions are not treated as canonical Source properties;
- [ ] current work target is not inferred from `project_source_id`, structural status, research-function labels, File availability/upload order, old AI scopes or support fixtures;
- [ ] a consequential change of `active_scope` / `NEXT ACTION` is traceable to owner-grounded purpose/priority/scope rather than repository self-consistency alone;
- [ ] each explicit use-evidence File resolves to `corpus/files.tsv` and belongs to the same canonical Source as the referenced use;
- [ ] exact File identity/provenance is not duplicated in Project use records;
- [ ] source-relative relevant locus is distinct from digital evidence locator;
- [ ] reusable crosswalks have one canonical corpus home;
- [ ] Source→Source claims remain evidence-status-controlled in `corpus/relationships.tsv`;
- [ ] no Project→Project relation is inferred from Project→Source use;
- [ ] consequential old work/checkpoint state remains recoverable when Project organization changes;
- [ ] generic G1–G6 requirements are referenced, not copied;
- [ ] another capable researcher can identify Project authority/root/sections, research functions, exact evidence files, evidence-readiness limits, current state and authorized next action—or the explicit absence of one—without old chat.

No duplicate-Project-root or ancestor/descendant-root prohibition is implied by this checklist.

## Change propagation

### Source identity/structure/File/crosswalk correction

`Project discovery → verify → update corpus owner → update affected Project consequences → bounded consistency pass`

A Source correction does not itself create, delete, merge or reprioritize Projects.

### Project boundary/root correction

If the owner changes a Project boundary, or evidence shows that the current `project_source_id` does not correctly anchor the owner-defined boundary, preserve the prior state and correct the Project metadata. Then re-resolve internal/external Sources through `part_of`; do not manually relabel structural status.

### Project source-use change

Update the relevant `source-uses.tsv` row(s). A changed function/locus does not change canonical Source identity, structural membership or Project identity.

If concrete digital evidence for a use changes, update use-evidence while keeping File identity/provenance in `corpus/files.tsv` and keeping the File bound to a use of its own canonical Source.

A change in Source use, evidence availability or technical support does not by itself authorize a change in current research priority. Synchronize `active_scope` / `STATUS.md` only from an owner-grounded purpose/priority/scope basis.

### Project-organization migration

When Project organization changes, perform a semantic-loss/restartability check over both research data **and work-state audit information**. A deleted STATUS or old Project wrapper may cease to be canonical, but consequential evidence limits, dormant/activation state, unresolved tasks and recovery pointers must not become discoverable only through accidental chat memory.

### Generic methodological weakness

`project observation → project LEARNING/status → explicit generalisability check → methodology/DECISIONS update → bounded consistency pass`

## Project relations

Project→Project relations are explicit research-organisational relations only. Historical/documentary structure and textual/source claims belong in `corpus/relationships.tsv`.

Using a Source that belongs structurally to another Project root never auto-creates a Project→Project relation.

## Closure and restartability

A completed/inactive Project remains a scholarly provenance package for its owner-defined research Project and historical Source anchor. If superseded or reorganized, record that explicitly and preserve enough prior-state linkage to audit the transition.

At any time the repository should answer without chat:

- which Projects the human owner has actually defined;
- which canonical Source root anchors each Project;
- which Sources are structurally internal or external by derivation;
- which sections/source nodes are currently known inside the Project;
- which concrete research functions each used Source serves, including whether a use is historical rather than current;
- what source-relative loci matter;
- which exact digital Files actually support which uses;
- whether evidence needed for a direct action is actually research-ready in the current authorized context;
- which Source→Source claims are evidenced;
- what prior work/checkpoint state remains relevant after structural migrations;
- which gate is active and what the next action is, or that no owner-grounded next action is currently selected;
- which owner-grounded purpose/priority/scope basis authorizes any material current work target.