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

## 5. AI/HITL application of material research-system change admission

The canonical general material research-system change-admission workflow is owned by `methodology/maintenance.md`. AI/HITL applies that rule as follows:

- AI may analyse, derive requirements and propose a concept, but it may not infer or manufacture owner admission for a material implementation.
- Silence, enthusiasm, prior autonomous work or repeated agreement are not implementation admission.
- If work inside an admitted scope exposes a new material architecture or migration decision outside that scope, AI must stop the affected work and return that decision to the canonical admission path in `maintenance.md`.
- Once the owner has explicitly admitted a sufficiently precise implementation scope, AI may execute the bounded implementation without asking the owner to micromanage routine implementation details.
- Owner admission governs permission and scope for material system change; it never substitutes for qualified archival, palaeographic, historical, philological or other specialist validation.

AI/method-compliance status and independent specialist validation remain separate statuses.

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
