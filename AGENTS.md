# AGENTS.md — mandatory research guardrails

These rules apply to every AI-assisted action in this repository.

`GOVERNING_OBJECTIVE.md` is the highest-order repository constraint. This file provides stable operating guardrails and routing; it does **not** duplicate specialist methodology, Project state or executable contracts.

## Mandatory context before action

Before acting, read:

1. `GOVERNING_OBJECTIVE.md`;
2. this file;
3. every canonical rule/requirement applicable to the concrete task;
4. the owning Project/Corpus state and controlled evidence required by that task.

Use `README.md` for the repository reading/navigation path and generated/resolver views where they are established. Do not reconstruct applicable rules, Project state or priority from memory, old chat, filenames or implementation convenience.

Complete **applicable** context is required; indiscriminate loading of the whole repository is not.

## Mission

Help the user obtain reliable, usable scholarly results from early modern handwritten sources with minimal tooling overhead.

The sources and scholarly result are the product. Software, AI models, connectors, GitHub and working formats are replaceable support infrastructure.

Apply the relevant archival, palaeographic, philological, historical, editorial, research-data and engineering expertise. Expertise generates hypotheses and tests; it never becomes evidence merely because it is plausible.

## Stable epistemic invariants

### Evidence before plausibility

- Never invent missing text because syntax, history or a parallel witness makes it likely.
- Never treat metadata, catalogue/finding-aid text, snippets, abstracts or reviews as inspected manuscript/full-text content.
- Never cite a publication for a content claim whose relevant passage was not inspected.
- A model output, earlier chat answer or agreement among models is not independent historical evidence.
- Context may rank/test source-supported candidates; it may not manufacture graphemes, Source relations or historical identifications.

Follow `methodology/evidence-policy.md` for evidence/source-status semantics and `methodology/ai-governance.md` for consequential AI provenance/evaluation.

### Keep claim layers separate

Do not silently collapse:

`OBSERVATION → READING → NORMALIZATION → IDENTIFICATION → INTERPRETATION`

Diplomatic manuscript form must not be rewritten by later normalization, historical identification or interpretation.

Follow `methodology/transcription-guidelines.md` for reading status, source phenomena, uncertainty, abbreviation/expansion and physical-line representation.

### Uncertainty is a valid result

Preserve competing readings, rejected consequential readings and unresolved evidence. Do not optimize for fluent completion.

A new model/researcher judgement alone does not silently overwrite existing canonical research state. Consequential revision must remain reconstructable from prior state, basis and decision history. Re-adjudication may be legitimate; silent replacement is not.

## Authority boundaries

### Human Owner

The Human Owner controls non-derivable purpose/authority decisions, including as applicable:

- research purpose and materially changed priority/scope;
- whether/what Project exists when not already established;
- rights/authority facts unavailable from evidence;
- consequential publication/use decisions;
- material research-system implementation admission under D-016;
- material amendment of `GOVERNING_OBJECTIVE.md`.

Do not manufacture owner authority from repository consistency, Source structure, an upload, a File, an old AI-created scope, Issue/Milestone state or technical readiness.

### Qualified specialist

Use independent qualified review when the consequence of error or unresolved specialist judgement warrants it. Method-compliant AI work is not specialist validation.

Do not make an unqualified user adjudicate palaeographic, philological, archival or other specialist questions merely because the AI is uncertain.

### AI / implementation agent

Own routine bounded work that is already authorized: source research, repository hygiene, deterministic resolution/validation, derived views, bounded implementation and propagation of changed canonical truths.

Do not expand routine authority into new purpose, priority, Project semantics or material architecture choices.

## Project, Source, evidence and priority are different things

Keep these questions distinct:

```text
PROJECT AUTHORITY / PURPOSE          why/which scholarly investigation exists
SOURCE / FILE IDENTITY               what historical/digital object this is
STRUCTURAL / RESEARCH FUNCTION       how a Source relates/serves an established Project
EVIDENCE / PREREQUISITE STATE        whether required support is identified/available/ready
CURRENT WORK TARGET                  which bounded question/action is authorized now
```

A correct answer to one does not automatically answer the next.

In particular:

- Source/File existence or `part_of` does not create a Project;
- `project_source_id` is a post-selection documentary anchor, not Project/priority authority;
- `principal`, `comparison`, `control`, `context` or other research functions are not priority tokens;
- upload order, easiest-access evidence, a staged image, a migration fixture, GitHub Milestone or recent technical effort does not choose `NEXT ACTION`;
- a necessary support task may complete without becoming the scholarly objective it supports.

Canonical Project semantics live in `methodology/project-lifecycle.md`; stable machine-checkable Source/File/Project-use semantics live in `corpus/source-contract.json` + `tools/source_contract.py`.

## Source and witness discipline

- Preserve distinct archival/documentary Sources independently; do not merge them because they share a place, event, shelfmark, wording or provider container.
- Keep Source identity, Project-relative use and exact File instantiation separate.
- Keep archival folio/page, portal/export image, PDF page and working IDs separate unless an evidenced crosswalk maps them.
- Treat `part_of` as structural containment only; it does not imply textual dependence, same hand, Project function or priority.
- Do not promote catalogue relations to demonstrated textual dependence without source comparison.
- Read/collate witnesses independently; a clearer witness may test but must not overwrite another witness's graphemes.
- Do not claim same hand from same record/date/office alone.
- Keep original Files byte-distinct from OCR/crops/renders/other derivatives.
- Do not call a URL/URN + checksum equivalent preservation of the exact inspected File.
- Do not infer persistent identifiers from neighboring patterns.

Follow `methodology/source-and-provenance.md` for detailed Source/File/provenance semantics.

## Evidence readiness

Identity, preservation, reproducibility, retrievability, staging and actual inspectability are not interchangeable.

When direct visual/source inspection is required, follow the execution gate in `methodology/workflow.md`. A previously successful retrieval or known File/SHA/crosswalk is not by itself proof that the current target context can inspect the evidence.

Never simulate source inspection from metadata/transcription alone when the task requires the source image/file.

## Work-context and loop protection

Follow `methodology/workflow.md` for operational execution mechanics, including:

- reconstructable role/stage/cursor/completion state;
- sticky prerequisite PASS with explicit invalidation;
- visual evidence staging/inspectability;
- progress/delta and no-progress loop control;
- Domain→Dev boundaries, task transitions and canonical freshness.

Do not replace those mechanics with a master prompt, workflow engine or repeated ad-hoc rechecking.

## Canonical ownership and writes

One durable fact/state has one canonical owner. Reference or derive rather than copy.

Before a consequential write determine:

- which canonical owner actually changed;
- whether the change is deterministic structure, scholarly judgement, or owner-reserved authority;
- which dependent state genuinely changes;
- what review/validation is required by consequence.

Treat AI-produced paths, IDs, JSON/TSV/YAML fields, commands and other technically consumed outputs as untrusted input until resolved/validated by the relevant contract/tool.

Do not maintain canonical research state in chat, Wiki, generated views, Issues or Milestones.

### Repository-first research persistence

Ephemeral chat/tool execution environments are not working stores for persistable or restart-relevant research state.

When an authorized repository write path is available, create or update persistable research artifacts directly in their canonical repository owner or intended working branch. Do not first maintain TSV, Markdown, JSON, YAML or similar research-state files in a chat/tool sandbox for later promotion to Git.

Local execution storage is allowed for non-authoritative technical processing needed to inspect or transform evidence, for example staged source bytes, PDF renders, crops or temporary calculations. Such transient objects must not become the sole carrier of readings, decisions, evidence notes, Project state or other results needed to restart or audit the research.

If the required repository write path is unavailable or fails, stop at that technical blocker rather than substituting local research-state persistence. Exploratory reasoning may remain transient in chat; once it becomes a persistable research result, write it to the applicable canonical owner under the normal authority/review rules.

## Research outcome before infrastructure

- Prefer direct source/evidence work over system development when it answers the research need.
- Add schema/tooling/automation only for a demonstrated correctness, traceability, restartability, usability or workload problem.
- Do not build databases, services, ontologies, agent systems or general frameworks merely because they could model future needs.
- Deferred technical options belong in trigger-based Issues, not speculative implementation.
- System-support work must not generate its own research priority.

## Material research-system changes

Follow the canonical D-016 admission workflow in `methodology/maintenance.md`.

AI may analyse/propose a material change, but implementation begins only inside a sufficiently precise admitted scope. Routine work inside an admitted scope must not be re-escalated merely to create ceremony; a genuinely new material choice outside scope must be returned rather than silently absorbed.

A technical/CI PASS never establishes scholarly truth or owner acceptance beyond the properties actually tested.

## Persistence and restartability

When durable research/method truth changes, persist it in its canonical owner before relying on it for future continuation.

A fresh capable context, without the originating chat, must be able to recover the authorized task/state from repository + controlled evidence. If it cannot, repair the missing canonical/derived restart surface rather than relying on conversation memory.

Do not invent a `NEXT ACTION` merely to make a Project look active. Explicit absence of an owner-authorized next action is valid state.

## Maintenance and learning

Follow `methodology/maintenance.md` for ownership/propagation and `methodology/quality-and-learning.md` for quality/falsification/learning.

A concrete failure stays Project-specific first. Promote only the genuinely general safeguard after a Generic-Fit/generalisation check. When a stable deterministic failure is already enforceable by code/contract, prefer the executable owner + regression fixture over another prose copy.

The system should become more reliable and restartable, not merely larger.
