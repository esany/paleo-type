# Source / Project handling control audit — 2026-09-01

Status: **analytical / review artifact only; not normative METHOD, not implementation admission, and not authority to migrate current Project/Corpus state**.

Audit branch: `audit/source-project-handling-2026-09-01`  
Current `main` inspected: `b506ed3559fec66236326f9977ac3e20cbaf83c7`  
Pre-interpretation comparison checkpoint: `e8a7235bff875bf2c191c96c41638c4095f7ec76`  
Relevant existing owners: `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, `requirements/domain-requirements.tsv`, `methodology/historical-source-workflow.md`, `methodology/project-lifecycle.md`, `methodology/source-and-provenance.md`, `methodology/maintenance.md`, `templates/project/`, `templates/source/`, `corpus/source-contract.json`, `tools/source_contract.py`, Issues #58, #59 and #69.

## 1. Audit question and governing objective

The problem is not absence of scholarly/source rules. The repository already contains strong requirements and several deterministic controls. The audit asks why source/project handling nevertheless became model-dependent enough that successive AI sessions could reinterpret Project identity, current source focus and prior work state as though the relevant semantics were new.

The target is **model-independent execution wherever semantics are stable**:

```text
human/scholarly decision where genuinely non-derivable
→ explicit bounded input
→ deterministic generic routing / ownership / derivation
→ templates / scripts / validator / tests / CI
→ canonical restartable state
→ AI supplies expertise and execution, but does not redefine settled mechanics
```

This is not a goal of replacing scholarly judgement with a workflow engine. It is the existing technical-subsidiarity principle: stable recurring semantics/errors should be encoded once and checked deterministically; judgement and uncertainty remain scholarly/HITL concerns.

## 2. Existing requirements already cover the intended design

The relevant requirement families were already present before the latest drift:

- **REQ-ARCH-001** — stable Source identity independent of Project role/title/File instance;
- **REQ-ARCH-003** — exact inspected File distinct from historical/intellectual Source;
- **REQ-ARCH-004** — folio, portal/export image, PDF page and working identifiers remain distinct mappings;
- **REQ-ARCH-006** — Source relations are evidence-bearing claims, not identity shortcuts;
- **REQ-ARCH-007** — research function is Project-relative, never an absolute Source property;
- **REQ-GWP-001** — one canonical owner for durable fact/decision/state;
- **REQ-GWP-002** — exact Source/File/locus provenance is recoverable;
- **REQ-GWP-004** — consequential revision/rejection history remains reconstructable;
- **REQ-GWP-008** — research state is restartable without old chat;
- **REQ-GWP-010** — derived outputs are reproducible, never parallel manual truth;
- **REQ-RSE-001** — every technical component/change traces to a scholarly requirement or observed failure;
- **REQ-RSE-003/004** — canonical/derived separation and stable referential integrity;
- **REQ-RSE-005** — formalize only stable recurring semantics/errors;
- **REQ-RSE-007/008** — semantic-loss testing and provenance/history preservation for migrations;
- **REQ-RSE-010** — automation writing canonical state must remain narrower than scholarly judgement;
- **REQ-AI-001/002** — applicable governing context/requirements/project state must be loaded and routing may not omit applicable rules;
- **REQ-AI-007** — distinguish routine analysis/derived writes/canonical writes/material system changes;
- **REQ-AI-008** — deterministic failure classes should use deterministic checks rather than AI self-certification;
- **REQ-UX-007** — gate/gaps/NEXT ACTION visible without chat;
- **REQ-UX-011** — researcher does not operate repository paths/schemas/validators; deterministic mechanics are system responsibility;
- **REQ-UX-012** — consequential system/repository actions remain explainable and challengeable.

**Audit conclusion:** the present failure is primarily an **operationalization / consistency / admission failure**, not a missing-requirement problem.

## 3. Durable components that already exist and should be preserved

### 3.1 Scholarly/source workflow

`methodology/historical-source-workflow.md` already defines the authoritative S1–S9 sequence. Its S1 separates source-group/provenance work; S5 requires independent external-control/collation work; Project state and corpus truth are separate layers.

`methodology/workflow.md` provides the operational execution map and current role/handoff/prerequisite/freshness controls.

### 3.2 Canonical Source/File model

The Corpus layer already has stable owners:

```text
Source identity                 corpus/sources.tsv
Source structure/relations      corpus/relationships.tsv
exact File/bytes/provenance     corpus/files.tsv
reusable folio/image/PDF/URN    corpus/source-data/<source_id>/crosswalk.tsv
```

This is strong and should not be replaced by Project-local copies.

### 3.3 Project target model

The target model already separates:

```text
Project metadata/purpose/scope      project.yml
Project→Source research function    source-uses.tsv
Project-use→concrete File evidence  research/use-evidence.tsv
Project current work state          STATUS.md
```

`research_function` is open-vocabulary and Project-relative; File evidence is a separate relation. These are sound D-015 / REQ-ARCH-007 semantics.

### 3.4 Templates

`templates/project/` currently contains:

- `project.yml`;
- `STATUS.md`;
- `source-uses.tsv`;
- `research/use-evidence.tsv`.

`templates/source/` contains the generic source/crosswalk bootstrap.

### 3.5 Deterministic Source Contract

`corpus/source-contract.json` + `tools/source_contract.py` + tests + `.github/workflows/source-contract.yml` already enforce substantial stable mechanics, including:

- required/unique Source and File IDs;
- Source/File referential integrity;
- paired date consistency;
- Source relation endpoints;
- `part_of` duplicate/self/cycle rejection;
- deterministic `part_of*` ancestry;
- File SHA syntax and `repo-preserved` path/byte/hash verification;
- Project ID/directory equality;
- `project_source_id` resolves to a Source;
- legacy Project Source row integrity;
- target `use_id` uniqueness and Source resolution;
- open `research_function` vocabulary with syntax-only control;
- use-evidence cannot cross Projects;
- use-evidence File must instantiate the same Source as the Use;
- crosswalk owner (`source_id` vs directory), locator presence and URN syntax;
- resolver-derived root/internal/external structural status.

`tests/test_source_contract_assurance.py` contains negative regression fixtures for several of these stable failure classes.

**This is the correct model-independent direction.** The problem is not that deterministic controls are undesirable; it is that critical Project/intake/work-state semantics never reached equivalent executable coverage.

## 4. Historical Project-model evolution

The Git history shows repeated Project-model revisions in a very short period. This matters because different canonical files still reflect different generations.

### 4.1 Initial minimal Project contract

Commit `3757c674e01a2916a254f2038fcb706727cb85e1` introduced a Project template with `project_kind: source-unit | research-scope`.

### 4.2 Investigation-centered correction

Commit `65c68501c506760e7630e1a30c0c96b3d8fb1c64` deliberately changed the template to an investigation-centered Project:

```text
project title / repository role
research_object
active_scope
source register
optional principal Source
```

Commit `3679737ecf6f54abf09264044de14ad0d69f43e7` added the Project source-group table.

### 4.3 Removal of source-as-Project wrappers

A sequence beginning with `c7273c1a1254e3821bb499fcc9833a3a5791ec16` removed several Source-record Project wrappers (`Remove source record masquerading as project`). The Source/File/crosswalk facts were substantially moved to Corpus ownership.

**Loss not equivalently migrated:** the removed Project `STATUS.md` surfaces contained consequential work state (dormant/activation state, inspection/evidence limits and restart points). The structured Source facts survived; the same work-state audit surface did not. No executable Project-organization migration loss check prevented this.

This is a concrete failure against the intent of REQ-GWP-004/008 and REQ-RSE-007/008.

### 4.4 PR #57: anchor promoted into Project identity rule

PR #57 / commit `f560dcaef754a8401022c07870513e9c2d9a0401` solved a real problem — deterministic anchoring and internal/external derivation — but also explicitly said it would:

> `Supersede the investigation-defined project boundary with one historically independent source root per project.`

and changed the binding guardrail to:

> `Project identity follows historical structure.`

This is stronger than the minimum requirement needed to solve source-as-Project duplication. A stable documentary **anchor** became a Project **generator/identity rule**.

GitHub records PR #57 as created through the ChatGPT/Codex connector and it has zero discussion/review comments. Therefore GitHub provenance alone does **not** establish the later repository claim that this semantic strengthening was an `explicit human owner decision`. A connector-authored PR under the owner's GitHub account is not independent evidence of human semantic admission.

### 4.5 D-015 target research-use model

Commits `c175f40606610b41822f63b453280c1d2ef2cc27`, `4177c018...`, `8e36d7d...` and related Phase-1 work established `source-uses.tsv` and separate `use-evidence.tsv`. This was a useful normalization and should not be conflated with the Project-boundary dispute.

### 4.6 #69 recognized the missing intake execution path

Issue #69 explicitly states that the needed semantic components already exist but their **execution order is distributed across several owners**. It defines the intended flow:

```text
supplied File
→ exact byte identity
→ known/new/unresolved File
→ Source identity
→ evidenced Source structure
→ File provenance/rights/preservation
→ source-wide crosswalk when evidenced
→ explicit Project routing:
     existing Project | candidate new Project | no Project yet
→ minimal Project-relative state
→ deterministic contract checks
→ STATUS/NEXT ACTION synchronization
→ restartability check
```

This is very close to the needed model-independent intake pipeline. However #69 remains a **planning Issue**, so the sequence was never promoted into one executable/canonical intake path. A fresh model is therefore still required to synthesize the ordering from prose and can reinterpret it.

### 4.7 #58 had already identified the exact governance failure

Issue #58 was opened because a material architecture change had been implemented immediately after conceptual clarification before the owner reviewed a consolidated analysis/requirements/concept. It established:

```text
analysis
→ requirements
→ concept
→ owner review / explicit implementation admission
→ development
→ deterministic tests / scholarly loss checks
→ result review
```

The acceptance criteria explicitly say that silence, enthusiasm, previous model state or repeated AI agreement cannot be treated as approval.

The source/project changes made after `e8a7235...` on 2026-08-31 repeated this same failure class: user clarification was translated directly into Project/METHOD/DECISIONS mutations before a consolidated audit/concept review.

## 5. Current `main` — observed contradictions and enforcement gaps

### F1 — Canonical Project semantics are internally contradictory

Current files do not expose one consistent generic Project definition:

- `methodology/historical-source-workflow.md` still describes PROJECT as a **bounded historical investigation / source-unlocking undertaking over a coherent source group**;
- `README.md` and `AGENTS.md` still state the stronger **Project identity follows historical structure / project follows the historically independent documentary structure** model;
- `methodology/project-lifecycle.md` was modified on 2026-08-31 to state explicitly that Project existence/boundary are human-owner decisions and the Source root is an anchor after selection;
- `methodology/maintenance.md` and `methodology/source-and-provenance.md` still contain root-centric wording inherited from PR #57.

A fresh AI following REQ-AI-001 can therefore load **all applicable context and still receive contradictory normative statements**.

**Failure class:** canonical semantic drift; no executable cross-owner consistency check.

### F2 — Template contract and validator contract disagree

`templates/project/project.yml` marks `research_object` and `active_scope` as REQUIRED.

`corpus/source-contract.json` requires only:

```text
id
project_source_id
source_register
canonical_status_file
```

Therefore a Project can pass machine validation without the very research-purpose/scope information that makes it a scholarly Project rather than a structural wrapper.

**Failure class:** machine contract weaker than human template contract.

### F3 — Path fields are checked only for non-empty text, not referential meaning

`source_register` and `canonical_status_file` are required Project keys, but `tools/source_contract.py` does not resolve/check those paths. The current validator therefore does not prove that:

- the declared source register exists;
- it is the target/explicit legacy representation expected for that Project;
- the declared STATUS file exists.

**Failure class:** declared deterministic relationship not actually enforced.

### F4 — STATUS/restartability is prose-owned but structurally unchecked

REQ-GWP-008 and REQ-UX-007 treat `STATUS.md` as the restart surface. Yet Source Contract does not validate STATUS existence/currentness or any transition relation.

The already observed stale Reg. Ii 5 STATUS incident demonstrates the consequence: CI can pass while a fresh context is routed to a completed stage.

The recently added METHOD freshness rule is useful, but it is still an AI/prose check, not deterministic assurance where simple checks are possible.

### F5 — Current and target Project source-use paths are both live in prose

The target template uses `source-uses.tsv`, but `AGENTS.md` and `methodology/source-and-provenance.md` still use `projects/<id>/sources/sources.tsv` as the generic Project research-use entry point in several places. `maintenance.md` correctly treats this as legacy only for Reg. Ii 5.

The validator intentionally supports both models for compatibility, but the canonical prose does not consistently distinguish **target generic contract** from **one explicit legacy Project**.

**Failure class:** compatibility path leaked back into generic instructions.

### F6 — Project authority/admission has no durable executable state

The repository can require a `project_source_id`, but it cannot currently distinguish:

```text
Project created after a genuinely non-derivable human research decision
```

from

```text
Project inferred by an AI from an archival act, Source structure or convenient current scope
```

Git commit/PR authorship is not sufficient because connector writes are performed under the owner's GitHub identity. A prose phrase `accepted by explicit human owner decision` can therefore be written by the same AI whose inference is being audited.

This is not necessarily solved by a boolean `owner_confirmed: true`; that would only automate self-assertion. The missing control is an **admission/authority interface whose non-derivable input is explicit and reviewable, while all downstream mechanics are deterministic**.

### F7 — Project-organization migration preserved data but lost work-state visibility

The old Source-wrapper deletion preserved many canonical Source/File/crosswalk facts but not equivalent Project/STATUS restart information. Git history remains recoverable, but ordinary current-state navigation lost the prior checkpoint as a review surface.

**Failure class:** migration semantic-loss testing focused on data ownership, not research work-state/restartability.

### F8 — #69 intake is designed but not operationalized

#69 already defines `existing Project | candidate new Project | no Project yet` routing and separates deterministic from human questions. Because it remains Issue planning rather than an executable/canonical pipeline, each AI context can still reconstruct the sequence differently.

**Failure class:** known recurring workflow remained prose/backlog rather than promoted deterministic generic mechanism.

### F9 — `corpus/sources.tsv` still contains absolute-looking `relevance`

`corpus/sources.tsv` retains a `relevance` column with values such as `high`, `medium`, `context`. This field is not required by the Source Contract and its semantics are not aligned with REQ-ARCH-007 / D-015 Project-relative research functions.

Several Source notes also contain Project/work-state language (`project protocol`, current transcription/collation state). That creates a risk that Project-relative work truth leaks back into canonical Source identity records.

**Failure class:** legacy Project-relative semantics remain in the Corpus layer without machine ownership control.

### F10 — Generic CI contains a hard-coded Reg. Ii 5 regression

`.github/workflows/source-contract.yml` includes a useful real-data regression for `ega-reg-ii-5-knau`. Real fixtures are valuable, but a generic Source Contract should not depend on one pilot Project as its only resolver regression. The synthetic tests are more portable; the pilot fixture should remain an explicit additional regression, not the generic contract definition.

**Failure class:** model-independent generic control is partially coupled to pilot state.

### F11 — A structural CI PASS can mask invalid research routing

The 2026-08-31 creation of Li 3/Li 4 Project material passed `source-contract` CI. This proves only that IDs/roots/files/relations satisfied the implemented structural contract. It did not prove that the Project creation itself was correctly authorized or that reconstructed prior work-state meaning was correct.

**Key distinction:**

```text
STRUCTURAL CONTRACT PASS
!= PROJECT AUTHORITY PASS
!= WORK-STATE RECOVERY PASS
!= SCHOLARLY ADEQUACY PASS
```

### F12 — Current repository orientation itself is stale

`README.md` still states that the repository is public, while the GitHub repository is currently private. It also describes only the Reg. Ii 5/Knau benchmark as the current Project orientation while `main` now contains three Project directories after the latest interpretation pass.

This is not the core Project-model issue, but it is direct evidence that synchronization remains AI/prose-dependent and that fresh contexts can load a stale navigation surface despite strong local validators.

## 6. Why the system appeared to “forget” existing rules

The mechanism is now reconstructable:

```text
strong requirements existed
→ some stable mechanics became code/tests
→ Project/intake/admission semantics remained distributed prose
→ Project model changed several times
→ migrations left compatibility paths and stale instructions
→ #69 identified the missing ordered intake flow but stayed planning-only
→ fresh AI had to synthesize contradictory/partial instructions
→ plausible interpretation became canonical prose/state
→ structural validator checked references, not authority/meaning
→ CI PASS increased confidence
→ later models rehydrated the now-canonical interpretation
```

This is not primarily “AI forgot the rule”. It is **insufficient conversion of settled generic semantics into one deterministic control surface plus incomplete protection of the genuinely non-deterministic decision boundary**.

## 7. Stable invariants that should not be thrown away

The audit does **not** recommend rebuilding the Source/Project model from scratch. The following existing rules are strong and should be preserved unless later evidence contradicts them:

1. Source identity is canonical and Project-independent.
2. Exact File identity/provenance is separate from Source identity.
3. Persistent identifiers/URNs and exact File bytes are complementary, not substitutes.
4. Folio / export image / PDF page / stable URN remain distinct mapped identifiers.
5. Reusable crosswalks are Source-owned once.
6. `part_of` is canonical Source structure; ancestry is deterministically derivable.
7. Source relations are evidence-bearing claims.
8. Research functions are dynamic Project→Source relations, never absolute Source properties.
9. The same Source may have several Project-relative functions.
10. Concrete File evidence for a Project use is separate from the research function.
11. `project_source_id` can serve as a stable documentary anchor **after an actual Project has been established**; it need not be discarded merely because it was previously overinterpreted.
12. Structural `root/internal/external` status is deterministically derived from Project anchor + `part_of`.
13. A File/Source/current focus does not automatically create a Project.
14. A Source use does not automatically create a Project→Project relation.
15. Project `STATUS.md` is the restart surface for actual work state.
16. Material canonical/model migrations require semantic-loss/restartability checks.
17. Material METHOD/CORPUS/Project-architecture changes require the D-016 admission sequence.
18. Deterministic mechanics belong in templates/scripts/contracts/tests/CI rather than in repeated prompts.

## 8. Current 2026-08-31 mutation range requires review, not automatic acceptance or automatic rollback

The following commits after the completed Reg. Ii 5 source-work checkpoint `e8a7235...` were driven by successive interpretations of the owner's corrections and include material Project/METHOD assertions:

```text
3322d4f  Separate source roles from current research priority
17129a5  Restore owner-grounded Reg Ii 4 comparison focus
e31a37d  Record research-routing drift fixture
d452cdd  Restore Reg Ii 4 comparison as scholarly next action
9a042cc  Guard current work target against inferred priority drift
1191711  Add owner-grounded priority assurance
cab9311  Restore owner-defined Li 3 and Li 4 project audit state
e43936c  Correct Li 5 project authority and preserve audit state
71f7cc6  Make project creation explicitly owner-defined
3992aa0  Record owner authority for project materialization
b506ed3  Extend authority review to project definition
```

Some propositions in this range may ultimately be correct; some clearly corrected real failures. The **process state is nevertheless not valid as an admitted material architecture change**, because the owner had not first reviewed one consolidated analysis/requirements/concept. Do not use the presence of these commits as proof of owner semantic approval.

This audit intentionally does not revert them. Automatic rollback would repeat the same error in reverse. They are comparison evidence for owner review.

## 9. Control maturity matrix

| Area | Semantic requirement | Current deterministic control | Audit state |
|---|---|---|---|
| Source identity | strong | Source IDs/required fields/ref integrity | PASS |
| Source structure | strong | `part_of`, endpoints, cycle checks, ancestry | PASS |
| exact File/provenance | strong | File refs, SHA/storage/byte checks | PASS |
| crosswalk ownership | strong | owner row/source match, locator/status checks | PASS/PARTIAL |
| Project→Source dynamic functions | strong | target table + syntax/ref checks | PASS/PARTIAL (legacy coexistence) |
| Use→File evidence | strong | same-Project/same-Source checks | PASS |
| Project bootstrap | described | templates only; no deterministic init/routing transaction | GAP |
| Project purpose/scope contract | described as required | not required by machine contract | GAP |
| `source_register` path | declared | not path-validated | GAP |
| STATUS path/existence | declared | not path-validated | GAP |
| STATUS freshness | strong METHOD | no deterministic structural check | GAP/PARTIAL |
| Project authority / non-derived choice | strong HITL principle | no explicit durable admission interface | GAP |
| Intake order | detailed in #69 | planning-only, not canonical executable flow | GAP |
| Project-organization migration | lossless principle | no generic work-state migration regression | GAP |
| canonical-doc semantic consistency | one-owner principle | essentially prose/manual; one narrow governance string test only | GAP |
| model-independent task context | strong | partially canonicalized #77/#86 patterns | PARTIAL |
| pilot-independent generic CI | strong principle | synthetic tests + hard-coded Reg. Ii 5 CI fixture | PARTIAL |

## 10. Proposed recovery/control plan — **concept only, not implementation admission**

The smallest model-independent repair should reuse existing components rather than introduce a new platform.

### Phase A — Owner review / semantic recovery

1. Treat this audit as the analysis/requirements stage under D-016.
2. Compare `e8a7235...`, the early investigation-centered template (`65c685...`), PR #57/D-014, D-015/#59, #69 and the current main mutation range.
3. Establish one reviewed generic Project statement. The likely minimal synthesis to review is:

   > A Project is a durable scholarly investigation/work container selected for a research purpose. When that Project has a coherent documentary Source root, `project_source_id` records the stable canonical anchor used for deterministic structural resolution; the Source graph does not itself create the Project. Project→Source functions remain dynamic and Project-relative.

   This sentence is an **audit candidate**, not a new rule until owner review.
4. Review the current church-visitation Project routing separately from the generic rule. Corpus-specific Project selection must not become generic METHOD merely because it is currently useful.
5. Decide which post-`e8a7235...` mutations should be retained, revised or reverted; do not infer this from commit order.

### Phase B — Deterministic Project contract alignment

After explicit admission, prefer extending the existing Source Contract rather than creating another framework:

1. make the machine Project contract match the actual template contract;
2. require/check the stable Project keys that are genuinely invariant (candidate: `research_object`, `active_scope` only if the reviewed semantics still require them);
3. resolve/check `source_register` path rather than accepting arbitrary non-empty text;
4. resolve/check `canonical_status_file` existence;
5. test that `templates/project/` itself satisfies the same contract used for live Projects;
6. ensure target projects use `source-uses.tsv` and only explicitly grandfathered Projects use legacy `sources/sources.tsv`;
7. remove stale generic prose references to legacy paths once the intended compatibility boundary is agreed.

### Phase C — Deterministic Project bootstrap / intake orchestration

Do not create a UI/service/workflow engine. Operationalize #69 using the smallest reusable entry point, likely an extension of existing `tools/source_contract.py` or one equally small Project helper.

Desired behavior:

```text
supplied File
→ deterministic hash / known-File match
→ derive known canonical facts
→ stop for Source identity only if genuinely ambiguous
→ establish/reuse Source + evidenced structure
→ explicit routing state:
     EXISTING_PROJECT
     CANDIDATE_NEW_PROJECT
     CORPUS_ONLY
→ if CANDIDATE_NEW_PROJECT:
     obtain explicit non-derivable Project purpose/boundary input
→ instantiate existing project template deterministically
→ validate
→ expose exact remaining scholarly/authority questions
```

The helper must **never decide whether a new Project ought to exist**. Its value is that every AI/model follows the same mechanics after that decision.

### Phase D — Authority/admission interface

Do not solve human authority with an AI-writable `owner_confirmed: true` boolean.

The admitted design must instead distinguish:

- **non-derivable decision input** — explicit Project creation/boundary/purpose or material-change admission;
- **deterministic consequences** — IDs, paths, template instantiation, structural membership, validation, synchronization;
- **review evidence** — enough preserved context to show what decision the deterministic consequences were based on.

The exact storage/interaction mechanism requires owner review because connector-authored Git commits cannot independently prove human semantic approval.

### Phase E — Project-organization migration guard

For any future Project restructuring/deletion:

1. inventory consequential Project state before mutation (`project.yml`, STATUS, source uses, decisions, unresolved/dormant state and project research records);
2. supply an explicit old→new/recovery mapping;
3. verify that no consequential state becomes discoverable only through accidental old-chat memory;
4. run deterministic referential checks;
5. perform a scholarly/restartability loss review before deleting the old visible owner.

Prefer a small migration manifest/regression fixture over a generic migration framework.

### Phase F — Corpus cleanup after loss check

Audit legacy Project-relative data currently retained in `corpus/sources.tsv`, especially `relevance` and Project/work-state notes. Do not delete them directly. Determine their original meaning and migrate only genuinely Project-relative information to the owning Project while preserving canonical Source facts and historical auditability.

### Phase G — Canonical consistency regression

Add only small checks for stable repeated failures, for example:

- project template required keys == machine contract required keys;
- declared project source-register/status paths resolve;
- retired generic Project-source paths appear only inside explicit legacy-compatibility sections;
- canonical owner strings for the D-016 workflow remain unique (existing `test_governance_ownership.py` already demonstrates this pattern);
- Project reorganization regression includes work-state/restartability, not only Source/File rows.

Do **not** attempt to parse all scholarly prose into a universal schema.

## 11. Acceptance criteria for a later admitted repair

A repair is successful when a fresh capable AI/model can, without old chat:

1. identify the one canonical Source/File/crosswalk owners;
2. distinguish Source identity, Source structure, Project selection, Project→Source function and current work target;
3. process a supplied File through the same ordered intake path;
4. never create/join a Project merely from Source/File/current chat context;
5. ask the human only for genuinely non-derivable Project/purpose/rights/source-identity decisions;
6. instantiate the existing Project template deterministically once that input exists;
7. derive structural membership from `part_of` rather than AI prose;
8. preserve dynamic Project-relative research functions and exact use-evidence;
9. preserve prior work state across Project-organization migrations;
10. validate all stable IDs/paths/ownership relations through code/tests/CI;
11. distinguish structural/technical PASS from Project-authority and scholarly PASS;
12. expose a current restart point or explicitly record that no authorized NEXT ACTION exists;
13. reconstruct why a Project/system mutation occurred without treating connector authorship as human semantic approval.

## 12. Immediate audit conclusion

The repository does **not** need a newly invented Source/Project architecture. It already contains most of the correct semantic pieces.

The highest-value repair is to close the gap between those pieces:

```text
settled requirement
→ one canonical semantic owner
→ one target template
→ one deterministic contract/resolver
→ one ordered intake/bootstrap path
→ regression tests for stable failure classes
→ human/scholarly decision only at the real non-derivable boundary
```

Until this audit is reviewed, do not perform further Project-model rewrites, current-work reprioritization or source/project migration merely from conversational clarification.