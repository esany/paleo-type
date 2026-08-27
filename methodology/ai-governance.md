# AI governance

## Purpose

Use AI as expert assistance without allowing model output, convenience or fluency to become historical evidence. Governance must remain proportional to the research risk and must not turn source work into process administration.

## 1. AI provenance — record only consequential use

Do **not** archive every prompt or routine interaction.

Record AI provenance when a model/tool materially affects a transcription decision, corpus transformation, historical identification, interpretation, or published claim. Preserve enough information to understand and, where realistically possible, reproduce the operation:

- model/tool name and version when known;
- date or research checkpoint;
- task/purpose;
- source/input scope used;
- consequential output or decision affected;
- relevant prompt/settings only when they materially shaped the result;
- subsequent human/evidential validation.

For proprietary systems whose exact model build cannot be fixed or reproduced, say so rather than claiming false reproducibility.

AI provenance explains **how a research result was produced**. It never promotes AI output to source evidence.

## 2. Rights, confidentiality and sensitive material

Before sending source material or unpublished research to an external AI service, check whether its use is compatible with:

- archive or repository terms;
- copyright/licensing;
- confidentiality or embargoes;
- personal/sensitive data obligations;
- agreements governing unpublished material.

If permission or data handling is unclear and the material is restricted or sensitive, do not upload it merely for convenience. Prefer an approved/local/controlled route or work from non-sensitive metadata until the constraint is resolved.

Do not store restricted source images in a public repository merely to improve reproducibility. Stable provenance can be recorded without publishing the binary source.

## 3. Primary-source provenance

A source image used for substantive work should be traceable independently of a transient chat session. Record, as available:

- archive/repository and shelfmark;
- folio/page/image identifier;
- access route;
- local/stable filename or identifier;
- date inspected;
- rights/access limitation where relevant;
- checksum/hash only when it solves a concrete identity/version problem.

Do not invent missing archival metadata. Mark it as pending verification.

## 4. Validation scales with consequence

Use the lightest validation sufficient for the consequence of error.

### Exploratory

For search leads, brainstorming and candidate generation, clear labeling and source checking before reuse are sufficient. AI output is disposable.

### Working research

For transcription, identification and substantive interpretation, require direct evidence control, visible uncertainty and a traceable decision path. Important claims should seek an independent control where practical (same-hand comparison, parallel primary source, edition, specialist tool or qualified reader).

### Publication / consequential claim

Before presenting a claim externally as reliable scholarship, raise the validation standard. Resolve provenance, inspect cited passages, disclose substantive AI assistance where appropriate, and obtain independent qualified human review when the claim materially depends on specialist judgement that cannot be secured from the evidence alone.

The user is not required to become the specialist reviewer. Expert review is an escalation path for consequential unresolved claims.

## 5. Material research-system change admission

Material changes to the research system require an explicit consequence-based admission path before development:

`analysis → requirements → concept → owner review / explicit implementation admission → development → deterministic tests / scholarly loss checks → result review`

This applies when a change materially alters:

- shared METHOD;
- the CORPUS information model or canonical ownership;
- Project architecture or Project/Source invariants;
- canonical research-data migration semantics;
- other research-system rules where an error could change provenance, scholarly meaning, auditability or restartability.

The stages have distinct purposes:

1. **Analysis** — inspect the current canonical state and the demonstrated failure/need.
2. **Requirements** — derive the applicable scholarly, epistemic, provenance, usability and technical requirements.
3. **Concept** — state the smallest coherent change, alternatives, dependencies and non-goals.
4. **Owner review / explicit admission** — the human owner decides whether a sufficiently precise material scope may enter development. Silence, enthusiasm, prior autonomous work or repeated model agreement are not admission.
5. **Development** — implement only the admitted scope. A sufficiently precise admitted plan may be executed without asking the owner to micromanage routine implementation details.
6. **Tests / scholarly loss checks** — run deterministic checks and proportional evidence/provenance/regression checks before treating the implementation as ready.
7. **Result review** — compare the result with the admitted requirements and preserved research meaning; CI success alone is not scholarly acceptance.

### What does not require a new admission loop

Do not turn ordinary research into approval bureaucracy. A new material-architecture admission is not required merely for:

- source inspection;
- evidence logging;
- transcription or bounded source work performed within an already admitted method/scope;
- derived/rebuildable outputs;
- routine repository maintenance that does not change research-system semantics;
- implementation details already unambiguously covered by an explicit owner-admitted scope.

If apparently routine work exposes a new material architecture/migration choice, stop that affected change and return to the admission path rather than silently expanding scope.

### Owner approval is not specialist validation

Owner admission governs purpose, priorities and permission to make a material research-system change. It does **not** establish palaeographic, archival, historical, philological or other specialist truth.

Where consequential specialist judgement remains insufficiently supported, keep the claim unresolved or escalate it to qualified independent review. AI/method-compliance status and independent specialist validation remain separate statuses.

No workflow engine is required. The rule is satisfied by an inspectable admitted scope, bounded implementation, proportional tests/loss checks and explicit result review.

## 6. When AI becomes a research method

Routine expert assistance does not require a benchmark suite.

A validation/evaluation protocol becomes mandatory when AI/HTR/automation is used systematically across a corpus and its outputs materially determine research findings — for example bulk transcription, entity extraction, classification, coding or quantitative counts.

Before relying on such scaled outputs:

1. define the task and error that matters;
2. build or select representative human-checked ground truth/sample data;
3. measure relevant error/failure patterns, not only aggregate accuracy;
4. inspect errors for systematic historical or palaeographic bias;
5. document model/tool/version/settings where available;
6. state the validated scope and do not generalize beyond it;
7. keep human review focused on high-risk or uncertain cases where possible.

Do not build this machinery in advance. Trigger it only when AI actually becomes a method rather than an assistant.

## 7. Accountability

AI may provide specialist assistance, comparisons, hypotheses and critique, but it is not an author, witness or accountable scholarly agent.

Published claims remain human-accountable. This does **not** mean the non-specialist user must personally adjudicate every palaeographic question; it means the workflow must either produce adequate inspectable evidence or escalate consequential unresolved specialist judgement to qualified independent review.

## Lean test

Before adding governance overhead, ask:

`Will this record, check or evaluation materially improve traceability, rights compliance, error control or the credibility of a consequential result?`

If not, do not add it.
