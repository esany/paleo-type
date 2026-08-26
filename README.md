# paleo-type

Lean, evidence-based workspace for the transparent transcription and scholarly analysis of early modern handwritten sources.

## Purpose

`paleo-type` helps a non-specialist reliably unlock early modern handwritten sources without turning the research task into either a software project or a demand that the user become a trained historian or palaeographer. It is a general method and lightweight workspace; each source is handled as a separate project.

The assistant is expected to contribute relevant historical, palaeographic, linguistic, archival and methodological expertise proactively. That expertise guides comparisons, hypotheses and tests; it does not replace source evidence.

The first benchmark is the Knau visitation material in ThHStAW, EGA, Reg. Ii 5 (working images 132–135).

## Start here — what to read

The README is the orientation layer for both humans and AI. It should remain sufficient to understand what the repository is for, how it is organized, where the authoritative records live and what must be read next.

### Human who wants to understand the repository

Read this README first. It is intentionally the shortest complete map of the system. Open deeper files only when you need the underlying rule, evidence or project detail.

### AI continuing research

Before substantive work on an existing project:

1. read this README if the repository structure is not already established in context;
2. read `AGENTS.md` for mandatory operating constraints;
3. read the active project's `STATUS.md` for the exact restart point;
4. read relevant rows in `apparatus/decisions.tsv` and the project's `LEARNINGS.md`;
5. read only the methodology files relevant to the task;
6. continue from `next_action` unless evidence gives a concrete reason to change course.

The old chat must not be required to reconstruct the research state.

## Where truth lives

`paleo-type` avoids parallel truth stores.

- **README** — repository purpose, map and required reading path.
- **`AGENTS.md`** — binding AI/research guardrails.
- **`methodology/`** — reusable normative method and governance.
- **`project.yml`** — stable project identity/scope metadata.
- **`STATUS.md`** — canonical current state and exact next action for a project.
- **`transcription/`** — current line-level readings.
- **`apparatus/decisions.tsv`** — substantive changes, rejections and adjudications.
- **`sources/` / `research/`** — what sources were actually inspected and what they can support.
- **`palaeography/`** — empirical hand/source-specific comparison evidence.
- **`LEARNINGS.md`** — project-specific failures, corrections and lessons.
- **GitHub Wiki** — end-user handbook and explanation; not a second research-status store.
- **Chat** — transient working space; not durable research memory.
- **Primary sources** — historical evidence.

For the detailed ownership and maintenance rules see `methodology/maintenance.md`.

## Non-negotiable principles

1. **Evidence before plausibility.** Never turn a plausible completion into a reading.
2. **Separate layers.** Observation, transcription, normalization, historical identification and interpretation are different claims.
3. **Source status is explicit.** A catalogue entry, snippet, review or table of contents is never treated as if the underlying source/full text had been read.
4. **Uncertainty stays visible.** Alternatives and unresolved graphemes are recorded rather than silently resolved.
5. **No AI slop.** Earlier AI output is not evidence. Repetition does not increase confidence. Fluent prose must not hide missing evidence.
6. **AI supplies expertise; evidence constrains conclusions.** The assistant should provide specialist method and domain knowledge rather than requiring the user to supply it, but source-specific claims remain limited by inspected evidence.
7. **The user controls purpose and depth.** The user should not have to adjudicate specialist questions they cannot validate. The system must expose unresolved points and identify the next useful evidential test.
8. **Human experts are escalation, not routine.** Seek qualified independent review when a consequential unresolved issue, specialist notation or publication-level claim genuinely warrants it.
9. **Reproducible decisions.** Material revisions are logged with reason and evidence.
10. **AI provenance is proportional.** Record consequential AI use, not every prompt. If a model materially shapes a research decision, preserve enough context to understand what it did and how the result was checked.
11. **Rights and confidentiality come before convenience.** Do not send restricted, sensitive or rights-unclear material to external AI systems merely because it is easier.
12. **Validation scales with consequence.** Exploration can be lightweight; working claims require evidence control; publication-level or consequential claims require stronger independent validation.
13. **AI-as-method requires evaluation.** If HTR/LLM/automation systematically determines corpus-level findings, validate it against representative human-checked material and examine failure patterns before relying on aggregate results.
14. **Research outcome before system development.** `paleo-type` exists to unlock sources, not to become an end in itself. Build or automate only when it materially improves the current research result.
15. **Lean by default.** Add tooling only when it shortens the path to a more reliable transcription or interpretation.
16. **Learning feeds back.** Proven project learnings may improve the general method, but project-specific facts never become general palaeographic rules.
17. **Maintenance follows change.** When research truth changes, update the one canonical record that owns it. Do not create duplicate status or documentation stores.

A compact formulation of the intended division of labour is:

`AI supplies expertise and maintains research state → evidence tests and constrains → provenance records consequential AI use → validation scales with stakes → uncertainty remains visible → user controls purpose/depth → expert review only when warranted`

## Human–AI division of labour

### AI / assistant

The assistant is responsible for the specialist and procedural work it can perform reliably:

- historical, palaeographic, linguistic, archival and methodological analysis;
- candidate generation and controlled comparison;
- source-status discipline and evidence tracing;
- identifying the next evidential test instead of asking the user to guess;
- maintaining affected repository records as research progresses;
- keeping `STATUS.md` restartable;
- detecting documentation drift after structural or methodological changes;
- surfacing uncertainty, missing metadata or rights constraints rather than inventing them.

### User

The user controls decisions that depend on purpose, access or authority:

- the research question and desired result;
- which material should be investigated and any source access only the user can provide;
- facts about permissions, ownership, confidentiality or embargoes that are not otherwise verifiable;
- acceptable effort/depth where several defensible research paths exist;
- whether a consequential unresolved question warrants external expert review;
- whether and where results will be published or used consequentially.

The user is not expected to maintain repository synchronization manually or to adjudicate specialist historical/palaeographic questions they cannot validate.

### Qualified human expert

A qualified specialist is an escalation and independent-review role when consequences or unresolved expertise warrant it, not a routine prerequisite for ordinary source work.

## Evidence layers

`OBSERVATION → READING → NORMALIZATION → IDENTIFICATION → INTERPRETATION`

A later layer may use earlier layers; it must never silently rewrite them.

## Source-status codes

| Code | Meaning |
|---|---|
| P | Primary source actually inspected |
| E | Scholarly edition actually inspected in full text/relevant pages |
| F | Research publication actually inspected in full text/relevant pages |
| K | Catalogue/finding aid/metadata only |
| R | Review only |
| S | Search result/snippet/table of contents only |
| H | Hypothesis/inference, not a source |

Only `P`, `E`, and `F` support claims about content, and only within the passages actually inspected.

## Lean file model

- **Markdown**: rules, status, reasoning, context and learnings.
- **TSV**: line-level transcriptions, source register, palaeographic concordances and decision logs. TSV is human-readable, diffable and spreadsheet-friendly.
- **YAML**: small project configuration/metadata where key-value structure is useful.
- **JSON**: deliberately avoided until machine validation or interchange creates a concrete need.

## Repository structure

```text
AGENTS.md                    Mandatory AI/research guardrails
README.md                    Repository entry point and reading map
methodology/                 General rules that apply to every project
  ai-governance.md           Lean AI provenance, rights and validation rules
  evidence-policy.md         Source status and claim discipline
  maintenance.md             Canonical ownership, upkeep triggers and responsibilities
  quality-and-learning.md    Error taxonomy and learning loop
  transcription-guidelines.md Conservative transcription conventions
  workflow.md                Minimal research workflow
projects/
  ega-reg-ii-5-knau/         First benchmark/source project
    STATUS.md                Exact restart point and next action
    LEARNINGS.md             Project-specific lessons
    project.yml              Minimal project metadata
    sources/                 Source register
    transcription/           Page/line readings
    palaeography/            Empirical hand-specific concordances
    apparatus/               Revisions and adjudication decisions
    research/                Audit of external sources/publications
    context/                 Context kept separate from blind reading
```

## Working cycle

1. Register the source and what was actually inspected; preserve enough provenance to identify the source independently of a transient chat.
2. Check rights/access constraints before sending restricted or sensitive material to external AI services.
3. Segment by physical page/region/line.
4. Produce a blind graphematic reading from the image.
5. Record alternatives and unresolved tokens without semantic filling.
6. Build internal comparisons from repeated forms in the same hand.
7. Adjudicate only where evidence warrants it; log substantive changes.
8. Record consequential AI assistance when it materially affects a research decision; routine prompting need not be archived.
9. Freeze a versioned transcription checkpoint.
10. Only then introduce parallel primary sources, editions and historical context.
11. Keep source-derived facts separate from inference and interpretation.
12. Use expert knowledge to choose the next best comparison or source check, not to overwrite uncertainty.
13. Raise validation when the consequence of error rises; evaluate AI explicitly if it becomes a systematic corpus-level method.
14. Persist the changed research state in its canonical files so another agent can continue without the chat.
15. Feed genuinely generalizable lessons back into `methodology/`.

## Continuous maintenance

Maintenance is **event-driven, not calendar-driven**. There is no value in a recurring maintenance ritual if nothing relevant changed.

When research changes a reading, source status, active uncertainty, next action, project lesson or general method, the assistant updates the affected canonical record as part of the same work session when practical. The assistant should not leave repository housekeeping to the user.

Before a substantive research session is considered complete, the decisive check is:

> **Could another capable agent continue correctly from the repository without recovering this chat?**

If not, persist the minimum missing state. Do not generate extra documentation merely to satisfy the check.

Detailed maintenance triggers are defined in `methodology/maintenance.md`.

## Wiki contract

The GitHub Wiki is for **end users**, not for maintaining a parallel research state.

It should explain, in accessible language, how `paleo-type` works, what the user must provide, what the AI does, how to understand `working`/`variant`/`unresolved`, what the evidence statuses mean, and what an output can or cannot establish.

The Wiki may show a human-friendly project overview, but the authoritative current state remains the project's `STATUS.md`; readings remain in `transcription/`; source status remains in `sources/` and `research/`. If Wiki and repository ever disagree, the repository wins and the Wiki should be corrected.

## Research-first rule

Before adding tooling, ask whether direct source work would solve the current problem faster. More tables, agents, HTR models, confidence scores or automation do not constitute rigor by themselves. A technical extension belongs in the repository only when it reduces consequential uncertainty, improves traceability or materially accelerates the present research task.

The preferred next action is always the one with the highest expected research value per unit effort.

## AI governance

`methodology/ai-governance.md` defines the minimum additional safeguards for consequential AI use: proportional provenance, rights/confidentiality checks, stable primary-source identity, validation scaled to stakes, evaluation when AI becomes a research method, and human accountability for published claims.

It is intentionally lean. It does **not** require archiving every chat, prompt or model output.

## Current benchmark

The active project is `projects/ega-reg-ii-5-knau/`. Its `STATUS.md` is the canonical restart point. At the current checkpoint, the next task is to collate numerical, monetary and measure notation across image 132 and the upper section of 133 before attempting further semantic reconstruction.

## Definition of useful output

The project succeeds when it produces a transcription and historical working basis that a user can inspect, cite, challenge and reuse. The desired result is a usable source transcription, visible uncertainty/apparatus, a verified source basis and historical interpretation whose claims remain traceable. Tooling is secondary. If a proposed feature does not materially improve speed, traceability or correctness, it does not belong in the project yet.
