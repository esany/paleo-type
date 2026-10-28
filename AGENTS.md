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

For an **image-preservation/acquisition** request concerning a record at `https://www.archiv.sachsen.de`, resolve the archival branch from the record and load the current repository skill `.agents/skills/savesax/SKILL.md` when it is **Hauptstaatsarchiv Dresden**. The Human need not name the skill. This is a task-specific routing reference to the skill owner (#271), not a general SStA/Leipzig scope expansion, a status-read download authorization, or a guarantee that a host which has not mounted repository skills can invoke it. The skill owns the provider route and external-preservation contract; do not reproduce them here.

## Mission

Help the user obtain reliable, usable scholarly results from early modern handwritten sources with minimal tooling overhead.

The sources and scholarly result are the product. Software, AI models, connectors, GitHub and working formats are replaceable support infrastructure.

Apply the relevant archival, palaeographic, philological, historical, editorial, research-data and engineering expertise. Expertise generates hypotheses and tests; it never becomes evidence merely because it is plausible.

## Adequacy before minimality

“Lean” is a constraint on a solution that is already adequate; it is not evidence that the solution is adequate. Before simplifying, minimizing, cleaning up, using a shortcut or selecting a smaller patch, make the following explicit:

- the user/research outcome, pain or need being protected;
- the root cause and the affected owner chain;
- the required invariants and semantic distinctions that must survive;
- the evidence, acceptance condition and non-goals;
- the counter-extreme check: which failure appears if this mechanism is applied too weakly or too strongly;
- the whole-system return condition and the residual uncertainty.

A smaller diff, fewer workflow steps, lower token/runtime cost, local or CI PASS, or a completed work package is not proof of root-cause resolution or user acceptance. Keep work-package completion, root-cause resolution and user acceptance distinct. If the adequacy evidence is missing, return the material decision instead of silently implementing the shortcut.

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

### Preserve semantic context across domains and translations

A consequential term means what its **owning scholarly/technical context or contract** defines; lexical identity, familiar wording or a plausible translation does not establish semantic equivalence.

Do not silently collapse terms that happen to look alike across archival science, diplomatics, palaeography, philology, scholarly editing, historical interpretation, research-data/software engineering, GitHub/API/CI contexts or ordinary human language. In particular:

- a technical field/token asserts only the semantics defined by its contract; schema validity, a resolver result or CI `PASS` does not create a scholarly claim;
- human wording is not automatically normalized into a technical status, controlled value or specialist term;
- a specialist term from one domain is not automatically reused with another domain's meaning;
- German↔English, technical↔scholarly, domain↔domain and expert↔ordinary-language translations must preserve the original claim type, target/scope, evidence/authority level and uncertainty; translation must not silently add precision, certainty or causal meaning;
- when a one-to-one translation is unsafe, qualify the term by context (for example `Textzeuge` versus historical/legal witness, Project `research_function` versus historical role, technical `owner` versus Human Owner) and preserve the original contract term where machine-facing precision matters;
- lexical similarity is never by itself a mapping rule. If the target vocabulary cannot carry the source meaning losslessly, preserve the distinction or mark the mapping unresolved rather than forcing equivalence.

This is a boundary discipline, not a global glossary or universal ontology. The relevant domain/contract owner remains authoritative for local meaning. Follow the semantic-boundary execution check in `methodology/workflow.md` and the durable cross-project decision D-019 in `DECISIONS.md`.

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

### Resource state is descriptive, not task authority

If a PDF, scan, attachment, credential, tool capability or other needed resource is unavailable, **surface that fact immediately** and name the concrete action affected.

Do not infer from resource availability/unavailability alone that the whole task or Project is blocked, that `NEXT ACTION` changes, that work must `STOP`, that a roadmap dependency exists, or that substitute work is authorized.

Before using blocker/STOP semantics, identify the canonical or explicit authority that makes the missing resource a prerequisite with that consequence. If such authority is absent or ambiguous, record only the resource state and action-local inability and surface the planning ambiguity to the Human Owner.

Resource absence never relaxes evidence standards: an action that actually requires unavailable evidence still cannot be simulated or completed from metadata, prior transcription or a parallel witness.

Follow the dependency-provenance and action-local resource rule in `methodology/workflow.md`.

### Research-assistance capability assessment and Human collaboration

Normal source research is a scholarly-assistance task, not a request for the Human to operate the system's internal tooling. When a technical/access limitation or uncertainty materially affects the next scholarly action, preserve the scholarly question/outcome and make the assistance boundary intelligible before converting the limitation into Human work.

Where material, distinguish enough of the following meanings to support the next decision without turning them into a mandatory form or universal status vocabulary:

```text
ESTABLISHED / DIRECTLY SUPPORTED
NOT YET VERIFIED / UNRESOLVED
EVIDENCE OR TEST NEEDED
TECHNICAL ROUTE(S) ACTUALLY TRIED
WHAT THE FAILURE PROVES / DOES NOT PROVE
BOUNDED VIABLE OPTIONS + EXPECTED INFORMATION GAIN
CLAIM CEILING / WHAT REMAINS UNESTABLISHED
```

Then choose the continuation that best advances the scholarly outcome with proportionate effort and least unnecessary Human burden:

- continue internally when a reasonable authorized route remains and has expected information gain;
- report a truthful, scoped inability when the current environment cannot establish or perform the needed action reliably;
- ask the Human for a bounded contribution when that is genuinely useful or necessary;
- return a Human-Owner authority question only when the missing decision/fact is owner-reserved;
- preserve `unresolved` or route to qualified specialist review when the remaining question is specialist judgement.

A request to the Human is legitimate; reflexive transfer of internal tool/retrieval work is not. When Human input is needed, explain in ordinary research-facing language **why** it is useful, **what exact evidence/fact/action** is requested, **what has already been established or failed to be established**, **what becomes possible if supplied**, and any **material uncertainty that remains afterwards**.

Do not exhaust every imaginable route or retry indefinitely. Use the workflow no-progress rule: alternatives need a plausible discriminating information gain. Do not hide uncertainty behind fluent completion, and do not turn one technical failure into global scholarly blockage.

### Consequential read, retry, resume and mutation boundary

Preserve the Human/research outcome as the control cursor when routing through tools, execution contexts, runtimes or storage. Technical decomposition may implement an authorized task; it does not acquire authority to replace the task or create a new one.

Before a consequential external or repository mutation, preserve the distinction among:

```text
READ / STATUS
    inspect or report existing state; no new top-level mutation

ACTIVE-OPERATION RETRY
    bounded retry already authorized inside the same still-active operation

RESUME
    continue previously authorized persisted operation state under its valid operation contract

NEW TOP-LEVEL MUTATION / RUN
    start a new consequential action after no active operation or after terminal state
```

Rules:

- A plain status/read request such as `Fertig?`, `Status?`, `läuft es noch?` or `was ist passiert?` is non-mutating by default. It does not authorize a rerun, resume, new download, push, workflow trigger, consequential message send, merge or canonical write.
- A terminal failure/cancellation ends the prior top-level operation unless its already-authorized contract explicitly defines a valid persisted resume. Do not infer a new run from the failure, from tool availability or from a later status read.
- Internal capability/runtime routing stays internal where the needed choice is derivable. Do not make the Human choose Chat/Work/CLI/provider/connector/runtime vocabulary merely because the implementation has those boundaries.
- One tool/path failure remains action-local. It cannot manufacture task-wide `STOP`, substitute work, new priority or source unavailability without authoritative dependency semantics.
- Before starting a long-running consequential external side effect, check the task-relative execution fitness that materially affects control and restartability: intended durable destination/progress where required, restart/resume/failure containment, observability, meaningful stop/containment capability and unnecessary transfer/runtime hops. `Can run code` is not evidence that a runtime is fit for the task.
- If a material stop/cancel/containment limitation cannot be removed, expose it before start when it would affect Human control. Do not promise universal cancellation, but do not discover a known material control gap only after the Human says `Stop`.
- Keep operation/result levels distinct. Running, partial/restartable, failed/cancelled, technically complete, preserved/secured and accepted are not interchangeable states; one layer's `PASS` must not launder another.
- After bounded repair/resume, return to the same valid higher-order outcome unless evidence/authority actually invalidated it.

`methodology/workflow.md` owns the detailed execution mechanics. Stable owner-local behavior should be enforced by the interface/tool plus regression fixture where possible; do not build a central workflow engine or duplicate this guardrail into every skill.

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

### GitHub-only access for ChatGPT Work and Codex

For every action concerning `esany/paleo-type`, ChatGPT Work and Codex must read and modify the current online GitHub repository exclusively through the authorized GitHub connector. This applies equally to locally executed and cloud-executed chats. Execution location does not authorize a different repository access or persistence route.

- Resolve governance, current task/Project owners and applicable rules freshly from online GitHub. Local checkouts, synced project mirrors, sandbox files and old chat are not substitutes for current repository authority.
- Do not clone, create or use local repository checkouts/worktrees, run local Git commands, or use shell/HTTP/API-key routes as a substitute for the GitHub connector.
- Create/update durable work directly in its canonical online repository owner on the intended GitHub working branch. This covers research and engineering work, drafts, evidence notes, decisions, status and restart/handoff state. Do not create local project-state files for later upload or promotion. Chat, Slack and Issue/PR summaries do not replace canonical repository-file persistence.
- If the connector, required permission or required connector operation is unavailable/fails, stop the affected repository action and visibly report the specific unavailable capability. Do not fall back to local persistence or another repository access route; do not infer changed Project priority or scholarly `NEXT ACTION`.
- Run repository checks through the authorized GitHub/CI route where available. If a required check cannot be invoked or inspected through that route, report it as unverified rather than executing from a local checkout or claiming a PASS.
- Non-authoritative source-byte staging, renders, crops and temporary calculations remain allowed only under the evidence-processing rules below. They are not repository checkouts or working stores for project results; source preservation/access rules still apply.

Before calling a work result persisted/secured, verify GitHub confirms the write and identify its repository path, branch and commit. A working-branch commit is durable work, not an accepted main-branch result. Before handoff/completion, check that consequential results from the active work block reached all actually affected canonical owners; a fresh repository read alone does not prove persistence completeness.

### Online execution proof gate

For every consequential repository work block:

1. Before mutation, freshly resolve the current main commit, applicable owner/current task, intended working branch or PR, bounded scope, DOR, DOD and STOP criteria through the authorized GitHub connector.
2. Use the authorized GitHub connector exclusively. Do not clone, create or use a local checkout/worktree, run local Git, or save repository state for later promotion.
3. After every mutation, verify the remote repository path, branch and commit. Record the exact remote commit as the durable work cursor.
4. Before handoff, status or completion, prove fresh-context restartability, reconcile every materially affected canonical owner, and state unresolved residuals and non-changes.
5. Treat local/technical/CI PASS, Issue closure, PR status or working-package completion as evidence only for the properties they actually check, never as automatic user or whole-system acceptance.

If the connector, permission, remote write, branch verification, restart proof or affected-owner reconciliation fails, stop the affected repository action and report the specific missing proof. Do not fall back locally or silently downgrade the work to a smaller unrelated slice.

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
