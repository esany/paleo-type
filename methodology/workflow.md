# Workflow — operational map

## Authority

The authoritative scholarly end-to-end method is `historical-source-workflow.md`. Generic maturity requirements live in `research-gates.md`. This file is only the **operational execution map**. Detailed transcription requirements live in `transcription-guidelines.md`; provenance/preservation in `source-and-provenance.md`; project/source-group semantics in `project-lifecycle.md`; evidence/source-status rules in `evidence-policy.md`; AI validation rules in `ai-governance.md`.

If an operational shortcut conflicts with the scholarly method or generic gate requirements, the scholarly method/gates win and the conflict must be repaired.

## Goal

Produce a traceable, human-auditable historical source transcription and analysis with the least process necessary to keep it reliable. Research activity must advance an explicit unmet requirement of the active generic research gate, repair an invalid prerequisite, or provide necessary evidence for doing so.

## Operational sequence

### S1 — Establish project source group and provenance
Define the investigation's source group in project `sources/sources.tsv`. Register each distinct archival record canonically in `corpus/sources.tsv`; do not collapse separately identified records because they share a signature. Register the exact original export used in `corpus/files.tsv` with filename, SHA-256, coverage and preservation state. Keep folio, portal/export image, PDF page and working IDs distinct. Put reusable source-wide crosswalks in `corpus/source-data/<source_id>/`. Record source relationships at their actual evidential level.

### S2 — Inspect document/material structure
Before claiming complete transcription, inspect the working locus for foliation/boundaries, physical lineation, reading order, layout/list/table structure, headings/marginalia, additions/deletions/corrections, damage/illegibility, abbreviation practice and evidence of hand shifts where relevant.

Do not mark unexamined phenomena absent; use `not investigated` where necessary.

### S3 — Diplomatic transcription
Transcribe the principal witness by archival locus and directly inspected physical line where relevant. Preserve source structure and written forms. Distinguish uncertainty/source phenomena according to `transcription-guidelines.md`. Do not replace visible multi-line source text with semantic summaries.

A human-readable witness view must be derivable from canonical transcription data; machine-oriented fragments alone are not sufficient for G2.

### S4 — Internal palaeographic analysis
For consequential uncertainty, localise the sign sequence, classify the problem, seek appropriate controlled internal comparanda, compare graphical features and record candidates/evidence. Same record is not automatically same hand. Context follows graphematic candidate formation rather than replacing it.

### S5 — Freeze/review principal-witness checkpoint
Before strong external-witness influence, ensure the principal witness has a coherent source-based checkpoint. It may contain unresolved readings.

### S6 — Independent external control and collation
Identify/read related witnesses and controls independently, then map corresponding loci and collate. Record agreements/divergences and upgrade source relationships only as far as evidence warrants. Never copy a clearer witness into the principal-witness transcription.

### S7 — Normalize/identify/interpret
Only after source readings are explicit, link manuscript forms to normalized people/places/institutions/values/concepts and perform historical source criticism. Keep manuscript form, expansion, normalization, identification and interpretation distinct.

### S8 — Critical consolidation/validation
Run the relevant scholarly and technical integrity gates: complete source representation, decision traceability, adversarial checking, provenance/referential consistency, witness-contamination check and explicit independent-human-review status for consequential specialist claims.

An unresolved but well-tested result may pass; an unsupported resolved result may not.

### S9 — Edition/publication
Define an explicit edition concept, then derive the user-facing edition from the consolidated research state. Do not introduce new manuscript readings at the presentation stage. Match publication/interchange technology to a concrete scholarly need.

## Cross-role work-context contract

Role/chat contexts are execution environments, not durable owners of project knowledge or generic workflow mechanics. A fresh capable context must reconstruct its task from canonical repository state, controlled evidence and the bounded Issue/handoff that activates the role.

For consequential work, the executable context must be able to determine, preferably by derivation rather than copied prose:

```text
ROLE / RESPONSIBILITY
TASK / ISSUE OWNER
CURRENT EXECUTABLE STAGE
FIRST / NEXT BOUNDED ACTION
PREREQUISITES: unknown | pass | fail
INVALIDATION EVENT for any sticky PASS
EVIDENCE REQUIRED
EVIDENCE STATE / ACCESS STATE
EXECUTION CURSOR
COMPLETION CONDITION
OUT OF SCOPE / NOT AUTHORIZED
HANDOFF TARGET
RETURN / REVIEW CONDITION
```

Do not freeze these labels into a mandatory serialization when the same semantics can be derived more simply. The invariant is reconstructability and role clarity, not form-filling.

Assurance review is **semantic, not lexical/template-based**. Do not reject or rewrite a handoff merely because it lacks a literal field heading such as `COMPLETION CONDITION:` when the required role, stage, prerequisite, cursor, completion, scope and return meaning are already unambiguous. Add structure only when it prevents a demonstrated ambiguity or loss.

### Current-work-target authority

At task start and whenever `NEXT ACTION` changes, distinguish four different questions:

```text
SOURCE / FILE IDENTITY             what evidence object this is
STRUCTURAL / RESEARCH ROLE         where it sits and what function it serves
EVIDENCE / PREREQUISITE STATE      whether required support is available
CURRENT WORK TARGET                which source/question is authorized to execute now
```

A correct answer to the first three does not determine the fourth. Do not infer the current scholarly target from `project_source_id`, `principal`, internal/external status, upload order, exact-file availability, newly verified metadata, a staged image, a migration fixture, an architecture Issue, or whichever prerequisite required the most recent effort.

The current work target must be traceable to owner-grounded research purpose / `active_scope`, or to an explicit later purpose/priority/scope decision. A supporting technical, provenance, access or architecture task may be necessary and valid without becoming the research objective that it supports.

If repository state is internally consistent around a current target but the authority basis for the priority change is missing, classify a **priority-authority gap**. Preserve valid completed evidence/support work, do not rewrite Source identity or research functions merely to repair the priority, and restore/derive the next scholarly action from the last owner-grounded purpose/scope plus the current evidential state. Ask the Human Owner only when the surviving canonical state does not resolve a genuinely new purpose/priority/scope choice.

An external comparison/control source may be the current executable scholarly target while an internal principal witness remains principal. `principal` is not a priority token.

### Sticky prerequisites

A prerequisite whose state is deterministically established as `PASS` remains `PASS` for the current work context until an explicit invalidation event occurs. Valid invalidation events include actual retrieval failure, checksum/identity contradiction, rights/authority change, or a canonical state change that makes the earlier test stale.

Re-entering an already-passed prerequisite without an invalidation event is a work-context execution fault, not research progress.

### Evidence staging for visual work

For source-critical visual work keep these raw states distinct:

```text
RETRIEVABLE        an authorized tool/path can recover bytes
STAGED              the required evidence object is present in the target work context
VISION-INSPECTABLE  the target scholarly context can actually inspect the required pixels
```

Do not overload `STAGED` as a synonym for complete visual research readiness. The derived execution gate is:

```text
VISUAL EVIDENCE READY = PASS
iff STAGED = PASS
and VISION-INSPECTABLE = PASS
for the same evidence object in the same target context
```

Historical retrieval success in another session is neither `STAGED = PASS` nor `VISUAL EVIDENCE READY = PASS` for a new target context.

An upstream staging owner may assert `STAGED = PASS` when the required object has actually been delivered into the intended target context. If vision-inspectability has not already been demonstrated in that same target context, the scholarly context may perform exactly one local inspectability preflight as its first action:

```text
STAGED = PASS
→ local pixel-inspectability check
→ VISION-INSPECTABLE = PASS
→ VISUAL EVIDENCE READY = PASS
→ execute scholarship
```

If that local check fails:

```text
VISION-INSPECTABLE = FAIL
→ VISUAL EVIDENCE READY = FAIL / EVIDENCE NOT READY
→ return to evidence-availability/staging owner
→ no evidence search, retrieval diagnosis or access repair inside the scholarly role
```

Avoid using the shorthand `EVIDENCE STAGED = PASS` as a composite readiness token, because it collapses raw object presence and inspectability into one ambiguous state.

Evidence-access/staging mechanics belong upstream. If the decisive staging capability lies outside repository/tool control, record the platform/orchestrator boundary instead of building repo code that cannot cross it.

### Progress / delta and loop control

A repeated action, delegation or return is justified only when at least one material state changes, for example:

- new evidence was inspected;
- uncertainty/decision state changed;
- the bounded question became narrower;
- canonical state advanced;
- a prerequisite was invalidated;
- escalation level changed for a stated reason.

A repeated delegation with no evidence/state/question delta is a `no-progress / delegation-loop candidate`. Do not bounce it indefinitely between role contexts. Preserve the research state, route the execution/process defect to the technical/process owner, and resume the scholarly role only from a valid executable state.

This rule applies to settled process mechanics, not to legitimate scholarly iteration where new inspection, comparison or judgement changes the evidential state.

## Senior Domain → Senior Dev interface

The primary competence boundary for a demonstrated research-system/process problem is the **Senior Domain / scholarly review → Senior Development/RSE** interface. Junior/bounded Source Research contexts may expose a failure, but they are not owners of generic workflow, connector, state-control or QA repair.

The scholarly/domain side supplies enough information to make the technical problem reconstructable without prescribing the implementation:

```text
DEMONSTRATED PROBLEM
EVIDENCE / REPRODUCTION POINTER
RESEARCH CONSEQUENCE
ESTABLISHED DOMAIN SEMANTICS / REQUIRED MEANING
UNRESOLVED / NOT INVESTIGATED
REQUIRED SYSTEM PROPERTY
SCOPE / NON-GOALS
DOMAIN ACCEPTANCE / RETURN QUESTION
```

The domain side stops before connector architecture, retry logic, state-machine design, storage/platform selection or other technical mechanism choices unless those mechanics are themselves already governed by an admitted requirement.

The Dev/RSE side then owns:

```text
REHYDRATE canonical state
→ VERIFY scope / authority / requirements
→ CAPABILITY / FEASIBILITY TEST
→ BOUND repo vs platform responsibility
→ DESIGN smallest adequate mechanism
→ EXECUTE admitted deterministic mechanics
→ VERIFY technical invariants / regression / provenance / restartability
→ PERSIST consequential result
→ RETURN to the correct scholarly/domain owner
```

Dev must not use the technical task to re-adjudicate manuscript readings, scholarly classification, research purpose or other owner-reserved semantics. A technical `PASS` is never scholarly acceptance.

## Consequential technical Issue contract

A consequential technical/process Issue is the reviewable interface between problem classification and implementation. It is ready for Dev only when the following are reconstructable, deriving stable facts from canonical state where safe rather than duplicating them:

```text
DEMONSTRATED PROBLEM / FAILURE
EVIDENCE / REPRODUCTION FIXTURE
CANONICAL OWNER / AUTHORITY
DEPENDENCIES / PREREQUISITES
BOUNDED SCOPE
EXPLICIT NON-GOALS
DETERMINISTIC ACCEPTANCE CRITERIA
SCHOLARLY / DOMAIN / HUMAN ACCEPTANCE CRITERIA where applicable
PERSISTENCE / RESTARTABILITY OBLIGATION
REQUIRED REVIEW LENSES
RETURN / CLOSE CONDITION
```

For material research-system changes, this Issue contract does not replace the admission workflow in `maintenance.md`. It supplies a bounded technical interface only after the relevant authority/admission state is satisfied.

A domain/process observation must not be translated automatically into a Dev requirement. The scholarly/domain review first determines whether the problem is incomplete research, project-local, already covered by existing requirements, genuinely reusable/systemic, specialist-dependent, or no action.

## State transition and canonical freshness

A completed stage or handoff is not restartable if the canonical restart surface still points to the prior stage.

Whenever a consequential stage or `NEXT ACTION` changes, perform the smallest bounded freshness pass:

```text
result persisted in its canonical owner
→ project STATUS/NEXT ACTION synchronized where applicable
→ current work target still traceable to owner-grounded purpose/priority/scope
→ handoff points to current canonical state
→ stale prior prose is not treated as current authority
```

Freshness is not authority. A perfectly synchronized set of project files can still carry an incorrectly inferred priority; the work-target authority check must therefore accompany consequential cursor changes.

This is a structural/authority consistency check. It does not decide whether a scholarly gate is scientifically satisfied.

## Review points in the flow

Use consequence-scaled review at real transitions rather than continuous ceremony:

```text
ROLE / TASK START
→ role/authority + current-work-target authority + prerequisite/evidence-state check

WORK / ITERATION
→ progress/delta + circuit break only when triggered

RESULT HANDOFF
→ persistence + unresolved/non-result + request completeness

PRE-DEV
→ requirement/scope/authority/admission review

DEV / PRE-MERGE
→ technical assurance + provenance/loss/rebuild checks as applicable

DEV RETURN
→ scholarly/domain adequacy review where the change carries scholarly meaning

STATE TRANSITION
→ canonical freshness + work-target authority + restartability
```

The relevant review may be performed by a fresh/independent context when consequence or self-review risk warrants it. Do not create permanent new roles merely to name review lenses.

## Research-state persistence

When research truth changes, update its canonical owner during the same work block when practical:
- source identity/inspection stage → `corpus/sources.tsv`;
- exact original/digital file identity, checksum, coverage, preservation state/path and rights → `corpus/files.tsv`;
- reusable source-wide image/PDF/export/folio mapping → `corpus/source-data/<source_id>/`;
- source/event/entity relationship → `corpus/relationships.tsv`;
- event context → `corpus/events.tsv`;
- project source membership/role/relevant locus → project `sources/sources.tsv`;
- project-specific inspection audit → project `sources/inspection-log.tsv`;
- diplomatic reading → project `transcription/`;
- consequential reading revision/rejection → project `apparatus/decisions.tsv`;
- palaeographic evidence → project `palaeography/`;
- external-source inspection status → project `research/`;
- active gate/project-specific unmet requirements/next action → project `STATUS.md`;
- project-specific failure/lesson → project `LEARNINGS.md`;
- generic scholarly method/gates → `methodology/`;
- durable cross-project architecture rationale → `DECISIONS.md`.

Do not make a future researcher recover durable state from chat.

## Generic gate rule

`research-gates.md` defines the reusable G1–G6 scholarly maturity requirements once for all projects. A project must **not** redefine those requirements in its own milestone file.

Project `STATUS.md` identifies the active gate and records only project-specific evidence, unmet requirements/blockers, validation state and the smallest next source/evidence action.

If a proposed activity cannot be tied to an unmet generic gate requirement, an invalid prerequisite or necessary evidence, do not perform it as current research work. Even when it can, a support/gate task does not override an owner-grounded current research priority merely because it is technically ready.

## Method / corpus / project discipline

Before persisting a new rule or finding ask:

- valid for another comparable manuscript investigation? → `methodology/`;
- canonical source/file/reusable mapping/source relationship truth? → `corpus/` / `entities/`;
- concrete investigation source role/locus/reading/state? → `projects/<id>/`.

A project is the investigation, not a source record or PDF. Pilot observations may trigger methodological learning but do not define general rules automatically.

## Exact-export rule

A central original archive export is part of the evidential chain. A URL/URN does not replace it. If public-repository rights prevent committing the exact bytes, keep the intended repository path and `preservation-blocked-rights` state explicit rather than claiming complete preservation.

## Validation proportionality

Use the lightest check sufficient for the consequence of being wrong, but never omit distinctions required for scholarly source representation. Tooling can remain lean; evidence semantics cannot.

Independent specialist validation is not the same as method-compliant AI work. Record which occurred.

## Corpus expansion

Corpus discovery is separate from the active transcription/edition workflow. Discovered sources may remain metadata/images inspected. Full transcription is never automatic merely because a source exists, and discovery of a source does not automatically create a new project.

## Deferred technology

When useful technology is not required by a current scholarly gate, preserve it as a trigger-based GitHub Issue rather than implementing it speculatively.

## Maintenance

Follow `maintenance.md`: propagate material truth changes across dependent records, run a bounded consistency pass when warranted, then return to source research.
