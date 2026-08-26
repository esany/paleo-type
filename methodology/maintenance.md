# Maintenance and documentation ownership

## Purpose

Keep `paleo-type` continuously usable without creating a second documentation project. Maintenance is event-driven: when research or method changes, update the canonical record that owns that information. Do not create periodic process work merely to make the repository look maintained.

## One fact, one canonical home

Avoid duplicated truth. Explanations may summarize canonical information, but changing the explanation must never become a substitute for changing the owning record.

| Information | Canonical home | Role |
|---|---|---|
| project purpose, repository map, required reading path | `README.md` | entry point for humans and AI |
| mandatory AI/research guardrails | `AGENTS.md` | binding operating rules |
| general research method | `methodology/*.md` | reusable normative method |
| project identity and stable scope metadata | `projects/<id>/project.yml` | structured project identity |
| current research state and exact next action | `projects/<id>/STATUS.md` | canonical restart point |
| current line-level readings | `projects/<id>/transcription/*.tsv` | transcription record |
| substantive reading changes/adjudications | `projects/<id>/apparatus/decisions.tsv` | revision trail |
| primary-source identity/provenance | `projects/<id>/sources/` | inspected source record |
| external literature/source audit | `projects/<id>/research/` | checked-vs-lead distinction |
| hand/source-specific empirical comparisons | `projects/<id>/palaeography/` | reusable internal evidence |
| project-specific failure modes and lessons | `projects/<id>/LEARNINGS.md` | learning record |
| end-user explanation and how-to material | GitHub Wiki | handbook; never canonical research state |
| exploratory reasoning and interaction | chat | transient workspace; not a durable research record |

## README, Wiki and chat

### README — repository orientation

The README must remain sufficient to answer:

- What is `paleo-type` for?
- What are its non-negotiable principles?
- Where does each kind of information live?
- What must a human or AI read before working in the repository?
- Which file is the canonical continuation point for an active project?

It should link or point to deeper rules rather than duplicate them in full.

### Wiki — end-user handbook

The Wiki explains the system from the perspective of a person using the results: how an source is processed, how to read statuses and uncertainty, what AI does, what the user needs to provide, and what a result can or cannot establish.

The Wiki may summarize project progress for orientation, but must point to the project's `STATUS.md` for the current state. Do not maintain a second list of open readings, decisions or source statuses in the Wiki.

### Chat — workspace, not memory

Chat is where exploratory work happens. Any result needed for reliable continuation must be persisted in the owning repository file before it is treated as part of the research state. A future agent must not need the old chat to reconstruct the next action.

## Required reading paths

### Human who wants to understand the repository

Start with `README.md`. It should provide enough orientation to understand the architecture and current benchmark. Read the linked methodology or project files only when deeper detail is needed.

### AI continuing an existing project

Before substantive work:

1. read `README.md` if the repository or structure is not already established in context;
2. read `AGENTS.md`;
3. read the active project's `STATUS.md`;
4. read relevant rows in `apparatus/decisions.tsv` and the project's `LEARNINGS.md`;
5. read only the methodology files relevant to the task;
6. continue from `next_action` rather than reopening broad exploration without evidence-based reason.

## Maintenance triggers

Update records because an event changed their truth, not because a calendar says so.

### If a transcription changes

- update the relevant `transcription/*.tsv` row;
- log a substantive replacement/rejection in `apparatus/decisions.tsv`;
- update palaeographic concordances if the change creates or invalidates a comparison anchor;
- update `STATUS.md` if the active uncertainty or next action changed.

### If a source is inspected or its status changes

- update `sources/` or `research/` with what was actually inspected and what it supports;
- promote `K/S` to `P/E/F` only under the evidence policy;
- update `STATUS.md` only if this changes the active research state.

### If a project lesson is learned

- record the concrete failure/correction in `LEARNINGS.md`;
- change general `methodology/` only if the rule is genuinely generalizable;
- update `README.md` only if repository-level orientation or principles changed.

### If method, governance or structure changes

- update the owning file in `methodology/` or `AGENTS.md`;
- update `README.md` when the reading path, repository map or top-level principles changed;
- update the Wiki explanation if the end-user experience or meaning of outputs changed materially.

### If the active task changes

Update `STATUS.md` immediately enough that another agent can continue without reconstructing the task from chat.

## Human–AI maintenance responsibilities

### AI responsibility

The assistant owns routine research-state hygiene. It should:

- identify which canonical records are affected by its research work;
- update those records as part of the same substantive work session when possible;
- keep `STATUS.md` restartable;
- preserve rejected/replaced readings rather than silently overwriting history;
- detect documentation drift and repair cross-references when it changes structure or method;
- avoid asking the user to perform repository housekeeping that the assistant can perform itself;
- surface a missing fact instead of inventing metadata or rights information.

### User responsibility

The user owns decisions that depend on purpose, access or authority rather than specialist historical technique. The user should provide or decide, when needed:

- research goals and desired output;
- source material or access that the assistant cannot obtain;
- facts about permissions, ownership, embargoes or private material that are not otherwise verifiable;
- acceptable effort/depth when several research paths are possible;
- whether to escalate a consequential unresolved issue to an external expert;
- whether and where results will be published or otherwise used consequentially.

The user is **not** responsible for manually synchronizing repository records or adjudicating palaeographic questions they cannot validate.

### Qualified human expert

A specialist human is an escalation/review role, not the default maintenance mechanism. Use one when the consequence of error warrants independent specialist judgement and the available evidence/tooling cannot resolve the issue sufficiently.

## End-of-work integrity check

Before treating a substantive research session as complete, the assistant asks:

1. Did the evidence or reading state change?
2. If yes, is the owning canonical file updated?
3. Did a material reading change require a decision-log entry?
4. Did the active problem or next action change? If yes, is `STATUS.md` restartable?
5. Did a project-specific failure teach a reusable lesson?
6. Did a general rule, structure or user-facing meaning change? If yes, are README/methodology/Wiki references consistent?
7. Would another capable agent be able to continue from the repository without the chat?

If the answer to 7 is no, persist the minimum missing state. Do not create documentation merely to satisfy the checklist.

## Lean maintenance rule

`Maintain on change, at the canonical source, with the minimum record needed for reliable continuation.`
