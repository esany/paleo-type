# Source / Project handling recovery and deterministic-control plan — 2026-09-01

Status: **concept / owner-review artifact only. This file is not normative METHOD, not implementation admission, not a Project-routing decision, and not authority to migrate current Corpus/Project state.**

Audit basis: `requirements/source-project-handling-control-audit.md` in Draft PR #88.  
Inspected `main`: `b506ed3559fec66236326f9977ac3e20cbaf83c7`.  
Pre-interpretation comparison checkpoint: `e8a7235bff875bf2c191c96c41638c4095f7ec76`.  
Relevant existing owners/components: `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, `requirements/domain-requirements.tsv`, `methodology/historical-source-workflow.md`, `methodology/workflow.md`, `methodology/project-lifecycle.md`, `methodology/source-and-provenance.md`, `methodology/maintenance.md`, `templates/project/`, `templates/source/`, `corpus/source-contract.json`, `tools/source_contract.py`, tests/CI, Issues #58, #59, #69, #71–#79 and current project/corpus state.

## 1. Purpose

The repair must not be reduced to “fix the Project definition”, “restore Li 3/4/5”, “add one validator check”, or “improve prompts”. The observed failure spans the full source-handling lifecycle:

```text
research need / supplied evidence
→ File identity
→ Source identity
→ Source structure
→ digital/folio crosswalk
→ Project routing
→ Project materialization
→ dynamic Project→Source research use
→ exact use→File evidence
→ current work state / NEXT ACTION
→ source research / comparison / review
→ migration / restructuring
→ restartability and audit
```

The goal is model independence where semantics are stable:

```text
stable generic semantics
→ one canonical owner
→ machine-readable contract where appropriate
→ deterministic helper/resolver
→ template
→ regression test
→ CI
```

while preserving genuinely non-deterministic boundaries:

```text
research purpose / whether a Project should exist / Project boundary when not derivable
source identity when evidence is genuinely ambiguous
rights/authority facts not otherwise verifiable
scholarly interpretation, palaeography, textual criticism, historical judgement
publication/consequential-use decisions
```

The human researcher should review meaningful research choices, not repository paths, schemas, identifiers, validation mechanics or migration bookkeeping.

## 2. Governing constraints

This plan is subordinate to the existing requirement set and especially:

- REQ-ARCH-001/003/004/006/007;
- REQ-GWP-001/002/004/008/010;
- REQ-RSE-001/003/004/005/007/008/010;
- REQ-AI-001/002/007/008;
- REQ-UX-007/011/012;
- D-015 Project→Source use / Use→File evidence separation;
- D-016 material-change admission;
- the S1–S9 scholarly workflow;
- current role/handoff boundaries where already falsified and accepted.

No new requirement family is proposed unless later analysis finds a requirement genuinely missing rather than merely unenforced.

## 3. Non-negotiable design principles

### P1 — Preserve strong existing Source/File ownership

Do not replace the current canonical split:

```text
Source identity                    corpus/sources.tsv
Source relations / part_of         corpus/relationships.tsv
File identity / SHA / rights       corpus/files.tsv
source-wide crosswalk              corpus/source-data/<source_id>/crosswalk.tsv
Project purpose/scope              project.yml
Project→Source research use        source-uses.tsv
Project-use→File evidence          research/use-evidence.tsv
Project work/restart state         STATUS.md or an admitted successor
```

### P2 — Project-relative functions remain dynamic

`principal`, `textual-comparison`, `palaeographic-comparison`, `notation-control`, `historical-context` and similar functions are Project→Source research-use semantics. They are not Source properties, structural membership, Project identity or current priority.

### P3 — `part_of` remains structural truth

Source containment is represented once and deterministically resolved. Do not duplicate `internal/external` flags in Project data when they can be derived from the selected Project anchor plus `part_of*`.

### P4 — Documentary anchoring and Project choice are separate questions

The likely synthesis for owner review is:

> A Project is a durable scholarly investigation/work container established for a research purpose. Where it has a coherent documentary Source root, `project_source_id` records the stable canonical documentary anchor used for deterministic structural resolution. The Source graph does not by itself decide that a Project exists, what the current research purpose is, or what should be done next.

This is a **candidate synthesis**, not a normative rule until reviewed/admitted.

### P5 — File identity never chooses research routing

Correct SHA/File→Source mapping can prove that a supplied export is Reg. Ii 4 or Reg. Ii 5. It cannot by itself decide:

- whether that Source belongs in an existing Project;
- whether a new Project should be created;
- what research function it has;
- what the next scholarly task is.

### P6 — Restartability includes work-state meaning, not only data survival

A migration/restructure is not lossless merely because Source/File/crosswalk rows survive. Consequential state such as inspected/not-inspected, unresolved questions, dormant/active status, current gate, exact next action and decision history must remain recoverable and visible.

### P7 — No AI self-certification for deterministic failure classes

Where a stable relationship can be checked mechanically, the system must not rely on a model saying “looks consistent”.

### P8 — No form-filling for judgement

Determinism constrains stable semantics and transitions; it does not force scholarly reasoning into rigid templates where semantics are genuinely open.

### P9 — No hidden migration by documentation rewrite

Changing README/METHOD wording is not sufficient to migrate actual Project/Corpus semantics. Conversely, data migration without synchronizing canonical method/templates/contracts leaves future models with contradictory instructions.

### P10 — Pilot fixtures test the generic system but do not define it

Reg. Ii 3/4/5, the Knau loci, #64, #69 and #85 are valuable falsification/regression fixtures. Generic behavior must remain applicable to another archival corpus.

## 4. Freeze and evidence-preservation boundary before repair

Before any implementation admission:

1. Treat `b506ed3...` as the current-main audit baseline and `e8a7235...` as the pre-interpretation comparison checkpoint, without declaring either semantically “correct”.
2. Preserve the full post-`e8a7235...` mutation range as review evidence; do not squash/rewrite history.
3. Do not perform additional Project-model, Project-routing or Project-priority mutations on `main` from conversational clarification alone.
4. Preserve PR #88 as the analysis/concept review surface.
5. Build a recovery inventory from Git for every removed/renamed Project/work-state surface before deleting or migrating anything else.
6. Treat current Li 3/4/5 project materialization as reviewable current state, not as proof that all underlying semantic decisions were admitted correctly.

Acceptance: another reviewer can reconstruct what existed before, what changed, and which changes are currently under semantic review.

## 5. Workstream A — Canonical semantic convergence

### Objective

Make one coherent meaning visible across GO/AGENTS/METHOD/README/Templates/Contract without discarding sound distinctions.

### Tasks

A1. Compare and classify every current generic Project statement in:

- `README.md`;
- `AGENTS.md`;
- `methodology/historical-source-workflow.md`;
- `methodology/project-lifecycle.md`;
- `methodology/source-and-provenance.md`;
- `methodology/maintenance.md`;
- `DECISIONS.md`;
- Project template comments;
- #59/#69 planning semantics.

A2. Classify each statement as:

```text
retain unchanged
retain but narrow
compatibility-only
historical rationale only
contradictory / superseded
owner decision required
```

A3. Reconstruct D-012 → D-014 → D-015 evolution and separate three questions that became conflated:

```text
What is a Project?
What documentary Source anchors a Project?
How does a Project use a Source?
```

A4. Present one minimal generic synthesis for owner review before modifying canonical METHOD.

A5. Separately review current corpus-specific organization (including Li 3/4/5) without promoting it automatically to generic METHOD.

### Acceptance

A fresh model can load all required canonical context and cannot encounter two incompatible generic definitions of Project/Source use.

## 6. Workstream B — Recover historical work state before deciding current organization

### Objective

Use Git as project memory so the human does not need to remember prior state.

### Tasks

B1. Inventory every historical Project/source-wrapper/status surface removed during the 2026-08-26/27 restructuring.

B2. For each historical unit, recover:

- Project/source identifier used at that time;
- purpose/scope wording;
- inspected evidence;
- dormant/active state;
- crosswalk state;
- transcription/analysis state;
- unresolved points;
- NEXT ACTION/restart point;
- source/file references;
- later destination of each durable fact.

B3. Produce a recovery matrix:

```text
old owner/path
→ information class
→ current canonical owner/path
→ preserved exactly / transformed / missing / ambiguous
→ evidence commit
→ action required
```

B4. Do not “restore” historical wrappers merely because they existed. Recover their meaning first, then decide whether current Project state already represents it or needs an explicit migration/recovery record.

B5. Reconstruct source-specific identifier evidence independently: URNs, portal IDs, PDF pages, export-image labels and file mappings must be assessed per Source, never generalized from a neighboring Source.

### Acceptance

No consequential prior research state is known only from old chat or human memory; any missing state is explicitly listed as a recovery gap.

## 7. Workstream C — Source/File intake pipeline

### Objective

Operationalize the already-designed #69 sequence rather than invent a new intake architecture.

### Target lifecycle

```text
SUPPLIED BYTES / SOURCE MATERIAL
        ↓
1. exact File fingerprint / known-file match
        ↓
2. Source identity resolution
        ↓
3. Source structure / part_of resolution
        ↓
4. File provenance / rights / preservation
        ↓
5. reusable crosswalk extraction/registration where evidenced
        ↓
6. Project routing state
        ↓
7. Project-relative use/evidence
        ↓
8. validation + restart state
```

### Deterministic responsibilities

- calculate SHA-256;
- match exact known File rows;
- prevent one File from being silently attached to the wrong Source;
- generate/validate stable IDs according to an admitted deterministic convention;
- resolve known Source parents/ancestry;
- detect missing/duplicate/conflicting crosswalk rows;
- separate folio/export/PDF/URN fields;
- preserve exact original filename and coverage;
- enforce storage/right-state vocabulary where semantics are settled;
- never infer a URN from image-number patterns;
- never convert “retrievable” to “preserved” or “research-ready”.

### Human/scholarly boundaries

Ask only if evidence cannot resolve:

- which historical Source an export represents;
- whether a genuinely new Source node is warranted when documentary identity is ambiguous;
- unresolved rights/redistribution authority;
- whether/how the material is to be used in research when that purpose is not derivable.

### Implementation direction after admission

Prefer extending `tools/source_contract.py` or one small adjacent intake helper over a new service/UI/workflow engine.

## 8. Workstream D — Explicit Project routing state

### Objective

Prevent File/Source availability from silently creating or reprioritizing Projects.

### Required routing states

At intake, the system must be able to reach one of:

```text
EXISTING_PROJECT
CANDIDATE_NEW_PROJECT
CORPUS_ONLY / NO_PROJECT_YET
UNRESOLVED_PROJECT_ROUTING
```

These states describe routing, not scholarly truth.

### Rules

D1. The system first searches existing canonical Projects and their purpose/scope/use relations.

D2. It may **propose** an existing Project or a candidate new Project using source structure and current research context.

D3. It must explain the proposal in research-facing language, not ask the user to choose paths/IDs/schemas.

D4. A Source/File/current place focus may not silently materialize a new Project.

D5. Once the non-derivable Project decision is made, deterministic mechanics own directory/id/template creation and registration.

D6. Absence of a Project is a valid state; Corpus intake must not be blocked merely because Project purpose is not yet established.

### Acceptance

A supplied File can be ingested and preserved correctly even when no Project decision has been made.

## 9. Workstream E — Project bootstrap and template/contract unification

### Objective

Make `templates/project/` the executable target contract rather than suggestive prose.

### Tasks

E1. Decide after semantic review which Project fields are truly generic invariants versus optional human-readable context.

E2. Make `corpus/source-contract.json` match the admitted Project template invariants.

E3. Deterministically validate:

- Project `id` / directory relation;
- declared `project_source_id` when the admitted model requires one;
- existence of the declared `source_register`;
- whether the register is target or explicitly grandfathered legacy form;
- existence of `canonical_status_file`;
- Source references in `source-uses.tsv`;
- Use IDs/functions/status syntax;
- use-evidence File and Source consistency.

E4. Test the template itself with the same validator used for live Projects.

E5. Add a small deterministic bootstrap command after admission, conceptually:

```text
init-project
  --project-id <derived/confirmed id>
  --project-source-id <confirmed anchor if applicable>
  --research-object <human-readable confirmed purpose>
  --active-scope <confirmed initial scope>
```

The exact CLI is a Dev design decision; the semantic requirement is deterministic instantiation from the existing template after the actual research decision.

E6. The bootstrap must create only required current state, not empty future-proof directories.

### Acceptance

Two different models given the same confirmed Project input generate semantically equivalent Project structure and both pass the same contract.

## 10. Workstream F — Dynamic research-use and comparison handling

### Objective

Ensure source roles/functions stay contextual and cannot become absolute Source metadata or Project priority.

### Tasks

F1. Keep `research_function` open-vocabulary with syntax-only deterministic enforcement unless recurring semantics justify more.

F2. Allow multiple functions for the same Source in one Project.

F3. Keep `relevant_locus` source-relative and distinct from File-instance `evidence_locator`.

F4. Never derive a research function from:

- Source type;
- `part_of`;
- Project root;
- upload order;
- legacy siglum;
- current file availability.

F5. For witness comparison/collation, preserve witness independence and only create cross-witness correspondence after independent reading as required by REQ-EDIT-004/005.

F6. Separate Project→Source research-use semantics from Source→Source historical/textual relation claims.

### Acceptance

The same Source can be comparison material in one task, palaeographic control in another, and unused in a third without changing its Corpus identity.

## 11. Workstream G — Current work state and restartability

### Objective

Make restart state robust enough that a fresh model does not need to infer stage, blockers or next action from prose archaeology.

### Current problem

`STATUS.md` is the canonical restart surface but simple structural properties are not machine-checked. The stale-Reg.-Ii.-5 incident showed that a fresh model can be routed to a completed stage while CI remains green.

### Plan

G1. Preserve `STATUS.md` as the human-readable restart surface unless a later admitted design demonstrates a better owner.

G2. Separate what can be machine-checked from what remains scholarly:

Machine-checkable candidates:

- declared STATUS path exists;
- required restart headings/fields exist if the format is stabilized;
- active work item references a valid Issue/task/locus when a typed reference exists;
- completed task cannot simultaneously be the exact active cursor when both states are structured;
- declared source/use/file IDs resolve;
- status transition writes synchronize required owner files.

Scholarly/non-deterministic:

- whether evidence is sufficient for G2/G3/G4 etc.;
- what the next best research question should be;
- whether a difficult reading is resolved;
- whether comparison materially changes interpretation.

G3. Evaluate two minimal implementation options after admission:

- small machine-readable front matter in `STATUS.md`; or
- one tiny canonical machine-state record with `STATUS.md` deterministically derived/synchronized.

Do not create both as competing truth. Choose only after a loss/restartability prototype.

G4. Add a state-transition/freshness check only for settled repeated failure classes, not a universal scholarly state machine.

### Acceptance

A fresh context can determine current stage, blockers and executable cursor from canonical state; deterministic contradictions are rejected mechanically; scholarly sequencing remains reviewable judgement.

## 12. Workstream H — Authority / owner-decision boundary without turning the human into a repo operator

### Objective

Make non-derivable decisions explicit enough to prevent silent AI promotion, while preserving usability.

### Important limitation

Connector-authored Git commits appear under the owner account, so commit authorship alone cannot prove human semantic approval. An AI-writable `owner_confirmed: true` field would not solve this.

### Required behavior

H1. Before a material Project/METHOD/CORPUS-architecture mutation, apply D-016.

H2. The AI presents the research-facing decision, alternatives and consequences in ordinary language.

H3. The human approves/corrects the **meaning**, not paths/schema/implementation details.

H4. The system records the admitted decision statement and its consequences in the canonical decision/Project owner, but labels the provenance accurately; do not claim independent proof beyond what the platform can establish.

H5. Downstream IDs/paths/templates/relations/validation are deterministic and must not require repeated owner confirmation.

H6. If the human statement is ambiguous enough that two materially different research organizations remain plausible, ask one focused research-facing clarification before materialization. If Git/current evidence resolves it, do not ask.

### Design question reserved for later

Whether a stronger platform-supported human-approval signal is available should be investigated separately. Lack of such a signal must not be papered over with self-asserted metadata.

## 13. Workstream I — Migration and restructuring guard

### Objective

Prevent a repeat of “Source/File data survived, work-state audit disappeared”.

### Required pre-migration inventory

For every Project/Source organizational migration, inventory:

- Project metadata/purpose/scope;
- STATUS/restart state;
- Source uses;
- use-evidence;
- transcription/analysis files;
- decisions/apparatus;
- unresolved/dormant state;
- inspection logs;
- crosswalk references;
- Issue/handoff pointers when they carry non-derived context.

### Required migration artifact

One bounded old→new mapping stating for each consequential owner:

```text
preserved unchanged
transformed with mapping
superseded with explicit successor
retained as historical audit only
unresolved / blocked
```

### Deterministic checks

- old referenced IDs still resolve or have explicit mapped successors;
- exact File IDs/SHA remain traceable;
- Project Source uses remain traceable;
- no declared canonical path disappears without an explicit successor/historical owner;
- restartability fixture succeeds from the post-migration state.

### Scholarly loss review

Technical referential PASS is not enough. A reviewer checks that uncertainty, work status and research meaning were not flattened.

## 14. Workstream J — Legacy cleanup only after recovery

### Objective

Remove semantic leakage only after its information value is understood.

### Candidates

- absolute-looking `corpus/sources.tsv: relevance`;
- Source notes containing Project/current-work language;
- generic prose references to legacy `projects/*/sources/sources.tsv`;
- `principal_source_id` and `primary_file_id` legacy compatibility in Reg. Ii 5;
- legacy `ega-reg-ii-5-knau` directory/id naming;
- hard-coded pilot assumptions in generic CI.

### Rule

No direct cleanup. For each candidate:

```text
identify original semantics
→ classify canonical owner
→ prove migration mapping
→ regression/loss check
→ only then remove/rename
```

## 15. Workstream K — Crosswalk and identifier assurance

### Objective

Ensure folio/image/PDF/URN handling is Source-specific, inspectable and reusable.

### Tasks

K1. Preserve the existing canonical Source-level crosswalk owner.

K2. Validate owner Source, mapping status and at least one digital locator per row.

K3. Preserve distinction between:

- archival folio;
- export image number;
- PDF page;
- provider derivative/TIFF label;
- stable institutional URN.

K4. Never infer a missing URN from neighboring pages.

K5. Build source-specific recovery checks for Li 3/4/5 only after generic semantics are settled, so historical crosswalk evidence can be compared against Git and supplied archive exports.

K6. Crosswalk availability must not be conflated with File preservation or current Project routing.

## 16. Workstream L — Canonical-document consistency assurance

### Objective

Prevent METHOD/README/AGENTS/Templates from silently describing different generations of the system.

### Minimal controls

L1. Keep one canonical owner for each rule and make other documents link/summarize rather than redefine.

L2. Extend the existing governance-ownership regression pattern only for stable owner statements that have already caused real drift.

L3. Add a template/contract consistency test.

L4. Add explicit legacy markers so generic path searches cannot mistake compatibility instructions for target rules.

L5. Do not build a natural-language policy parser or universal documentation linter.

L6. README orientation should be synchronized from actual repository facts where those facts are deterministic (e.g. current privacy/public statement should not contradict repository visibility).

## 17. Workstream M — Model-independent context and handoff acceptance

### Objective

Prove the repaired system works with heterogeneous models/sessions, not only with the model that designed it.

### Acceptance exercises

M1. Fresh context receives a new File and can follow intake without old chat.

M2. Fresh context encounters a known Source already used by multiple Projects/functions and resolves all relations without inventing an absolute role.

M3. Fresh context encounters a Source with no Project and correctly stops at `CORPUS_ONLY / candidate project` rather than creating one.

M4. Fresh context resumes a Project from STATUS and does not repeat a completed stage.

M5. Fresh context reads a legacy Reg. Ii 5 Project and clearly distinguishes compatibility representation from target Project contract.

M6. Fresh context reconstructs a migration using the old→new map without Git archaeology as a normal operating requirement.

M7. Fresh Source Research context receives only executable research state; retrieval/process engineering remains upstream.

M8. Different capable models produce the same deterministic routing/validation results for the same canonical inputs, while differences in scholarly judgement remain explicitly allowed.

## 18. Regression fixture set

Use observed failures rather than synthetic completeness for its own sake.

Minimum fixture candidates:

1. **Reg. Ii 4 export presented during Reg. Ii 5 work** — File identity must remain correct and must not silently change Project routing.
2. **same Source, multiple research functions** — accepted; no absolute role created.
3. **Li 3 with multiple internal Source sections** — structure resolved through `part_of`, no separate Project inferred automatically.
4. **missing declared `source_register`** — deterministic failure.
5. **missing declared STATUS** — deterministic failure.
6. **legacy register used by non-grandfathered Project** — deterministic failure after compatibility rule is admitted.
7. **project restructuring removes old STATUS without recovery mapping** — migration/restartability failure.
8. **stale active cursor points to completed task** — freshness failure once minimal machine state is admitted.
9. **crosswalk row owned by wrong Source** — already covered, retain.
10. **URN absent but neighboring rows contain URNs** — no synthesized URN.
11. **repo-preserved claim without matching bytes** — already covered, retain.
12. **Project created from Source root without non-derivable Project decision** — process/admission acceptance fixture; do not pretend this is cryptographically machine-provable if the platform lacks a human-signature channel.

## 19. Implementation sequence after owner review

The plan should be implemented in dependency order, not by easiest code first.

### Stage 0 — Review/admission

- review this plan + audit;
- correct misunderstandings;
- explicitly admit a bounded repair scope.

No material implementation before this point.

### Stage 1 — Semantic convergence

- settle generic Project/anchor/use semantics;
- classify current post-`e8a7235...` changes;
- synchronize canonical owners conceptually before data migration.

### Stage 2 — Recovery inventory

- reconstruct removed work-state surfaces;
- build old→current information map;
- identify actual missing state/identifier evidence.

### Stage 3 — Contract/template alignment

- make Project template and machine contract agree;
- validate declared paths;
- make legacy compatibility explicit;
- add tests before migration.

### Stage 4 — Intake/bootstrap operationalization

- implement #69 as the smallest reusable deterministic helper/command path;
- no new platform.

### Stage 5 — Restart-state assurance

- prototype minimal structured/freshness control;
- choose one canonical state owner;
- validate with the stale-STATUS fixture.

### Stage 6 — Migration guard

- implement bounded work-state/referential migration checks;
- test against historical source-wrapper removal fixture.

### Stage 7 — Corpus/project-specific recovery

Only now reconcile Li 3/4/5 current Project organization, source uses, old checkpoints, crosswalk gaps and legacy Li 5 representation against the reviewed generic system.

### Stage 8 — Legacy cleanup/migration

- `relevance`/work-state leakage;
- legacy Project source register;
- possible `ega-reg-ii-5-knau` rename;
- stale generic prose;
- pilot-specific CI coupling.

Each requires its own loss map; do not bundle merely for neatness.

### Stage 9 — Fresh-model acceptance

Run the model/session-independent scenarios above before declaring the repair complete.

### Stage 10 — Result review / close-out

- technical PASS;
- scholarly/Project-state adequacy review;
- human usability/challengeability review;
- synchronize canonical docs/Issues;
- close/supersede #59/#69/#88 only when their responsibilities are actually satisfied.

## 20. Control allocation matrix

| Concern | Canonical meaning owner | Deterministic mechanism target | Human/scholarly boundary |
|---|---|---|---|
| Source identity | Corpus/source method | ID/ref validator | archival ambiguity |
| Source structure | Corpus relationships | `part_of` validator/resolver | evidential interpretation of relation |
| File identity | `files.tsv` | SHA/ref/byte checks | rights facts where unverifiable |
| Crosswalk | Source data | row-owner/locator/status checks | difficult mapping evidence |
| Project existence/purpose | Project lifecycle + owner decision | deterministic consequences only | whether/why Project exists |
| Project anchor | Project metadata | Source ref + ancestry resolver | choice if several anchors genuinely plausible |
| Source research function | Project use | syntax/ref checks; no inference | function assignment/meaning |
| Use→File evidence | Project use-evidence | same-Project/same-Source ref checks | whether File actually supports use |
| Current work state | Project restart owner | minimal structural/freshness checks | research sequencing/judgement |
| Migration | maintenance | mapping/ref/loss fixtures | semantic adequacy review |
| Material system change | maintenance D-016 | process boundary + regression | owner admission |
| Specialist judgement | domain method | exact evidence packet only | qualified specialist |

## 21. Explicit non-goals

This repair must not become:

- a database migration project without demonstrated need;
- a universal workflow engine;
- a multi-agent runtime;
- a closed ontology of research functions;
- a generic scholarly state machine;
- a mandatory ticket/template for every source action;
- a prompt-centric solution;
- a UI project;
- an attempt to encode palaeographic/historical judgement as deterministic truth;
- an automatic Project generator;
- a requirement that the human operate GitHub/repository mechanics;
- a broad cleanup that removes historical evidence before loss mapping.

## 22. Owner-review questions before implementation admission

The following are the material questions this plan leaves for review; everything else should be treated as downstream engineering if the plan is admitted:

1. Is the candidate generic distinction **Project = scholarly work container; `project_source_id` = documentary anchor after Project selection** faithful to the intended model, or does Project need a different generic definition?
2. Is `STATUS.md` to remain the canonical restart-state owner if we add only minimal machine-readable assurance, or should a tiny structured state owner be prototyped and compared first?
3. Is the intended intake behavior correctly captured as **Corpus intake may complete without any Project; Project routing may be proposed by AI but materialized only after the non-derivable research decision is established**?
4. Should the current Li 3/4/5 organization be treated purely as a corpus-specific recovery question after generic controls are repaired, rather than as a premise for the generic architecture?

No path/schema/tool choice should be pushed to the owner unless it changes scholarly meaning or the admitted system boundary.

## 23. Definition of done for the whole repair

The repair is complete only when all of the following are true:

- one coherent generic Source/Project model is visible across canonical owners;
- Project-relative functions remain dynamic and no absolute Source-role leakage remains in target state;
- #69's ordered intake logic is executable rather than reconstructed from prose;
- templates and machine contract agree;
- stable path/reference/ownership relations are checked deterministically;
- old work state is recoverable without old chat and migrations cannot silently drop it;
- STATUS/restartability has proportional machine assurance against demonstrated failure classes;
- current Li 3/4/5 state has been reconciled only after generic controls are stable;
- Source-specific crosswalk/URN evidence is preserved without inference;
- legacy compatibility is explicit and bounded;
- material changes follow D-016 and cannot be justified by AI-written “owner approved” prose alone;
- fresh heterogeneous models can execute deterministic source/project mechanics consistently;
- the human is asked only for genuine research/purpose/authority decisions and can challenge the system in ordinary language;
- technical PASS, scholarly PASS, specialist PASS and owner/system-change admission remain distinct.

## 24. Immediate next step

Review/iterate this concept together with the audit. Until explicit implementation admission, do **not** merge PR #88 and do not execute the migration/control changes described above on `main`.
