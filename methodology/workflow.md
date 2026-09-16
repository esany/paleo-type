# Workflow — operational execution map

## Authority

This file owns **execution mechanics**: how a bounded task starts, advances, hands off, detects no-progress loops and returns to canonical state.

It does not own the underlying scholarly or data semantics. Use:

- `historical-source-workflow.md` — authoritative scholarly end-to-end method;
- `research-gates.md` — generic G1–G6 maturity requirements;
- `project-lifecycle.md` — Project authority, documentary anchor, Project→Source use and priority boundaries;
- `source-and-provenance.md` — Source/File/provenance/preservation/access semantics;
- `transcription-guidelines.md` — diplomatic/source-phenomenon semantics;
- `evidence-policy.md` — evidence/source-status semantics;
- `ai-governance.md` — AI provenance/evaluation obligations;
- `maintenance.md` — ownership, D-016 admission and propagation.

If an operational shortcut conflicts with one of those owners, repair the shortcut rather than redefining the owner here.

## Goal

Execute the authorized scholarly/technical task with the least process necessary to preserve evidence, authority, restartability and reviewability.

The operational sequence is the same S1–S9 scholarly sequence defined in `historical-source-workflow.md`; this file adds only the execution safeguards needed across sessions/roles.

## Cross-role work-context contract

Role/chat contexts are execution environments, not durable owners of Project knowledge or generic method.

For consequential work, a fresh capable context must be able to determine, preferably by derivation rather than copied prose:

```text
ROLE / RESPONSIBILITY
TASK / ISSUE OWNER
CURRENT EXECUTABLE STAGE
FIRST / NEXT BOUNDED ACTION
PREREQUISITES: unknown | pass | fail
INVALIDATION EVENT for any sticky PASS
EVIDENCE REQUIRED
EVIDENCE / ACCESS STATE
EXECUTION CURSOR
COMPLETION CONDITION
OUT OF SCOPE / NOT AUTHORIZED
HANDOFF TARGET
RETURN / REVIEW CONDITION
```

These are required meanings, not a mandatory serialization/template. Assurance is semantic: do not reject a usable handoff merely because a preferred field label is absent.

Stable Project/Source/File facts should be resolved/derived from their canonical owners rather than recopied into handoffs.

## Semantic-boundary and translation check

Whenever a **consequential meaning crosses a boundary** — scholarly domain → scholarly domain, Domain → Dev/RSE, Dev/RSE → Domain, machine field/token → human explanation, human language → structured value, or German ↔ English — perform a meaning-preservation check before treating the expressions as equivalent.

Resolve, as applicable:

```text
SOURCE SEMANTIC OWNER / CONTRACT
SOURCE TERM + CLAIM TYPE
TARGET / OBJECT / SCOPE
EVIDENCE / AUTHORITY / REVIEW LEVEL
UNCERTAINTY / STATUS

TARGET SEMANTIC OWNER / CONSUMER
PROPOSED TARGET TERM / FIELD / EXPLANATION
LOSS / GAIN / AMBIGUITY CHECK
```

Rules:

1. **Lexical equality is not a mapping rule.** The same word may denote different things in archival, diplomatic, palaeographic, philological, editorial, historical, workflow, GitHub/API or software contexts.
2. **Contract semantics are local.** A machine-facing field/token means only what its owning contract defines. Technical validity or `PASS` cannot silently acquire scholarly meaning.
3. **Human wording is not a status code.** Ordinary language may express a broader or vaguer judgement; do not silently normalize it into a gate, confidence value, controlled vocabulary or specialist claim.
4. **Translation may simplify wording, not epistemic content.** Preserve claim type, target/scope, evidence/authority level, uncertainty and relevant residual limits. Do not add certainty, precision, identity, chronology, causality or disciplinary interpretation during translation.
5. **Qualify polysemy instead of globalizing it.** Prefer contextual forms such as `Textzeuge` / historical witness, Project `research_function` / historical role, technical owner / Human Owner, or `G2 representation completeness` / reading resolution where ambiguity matters.
6. **Keep machine precision where required.** In human-facing explanation, retain the exact contract token alongside the explanation when translation alone could blur an operative distinction.
7. **No forced mapping.** If the target vocabulary cannot carry the source meaning without loss or gain, preserve the original distinction and mark the mapping/explanation as partial or unresolved.
8. **Automate only stable semantics.** Deterministic vocabulary or mapping checks are appropriate only after the relevant meanings are stable and formally owned; open scholarly semantics remain a domain judgement.

Examples of forbidden implicit conversions:

```text
technical / CI PASS       ≠ scholarly validation
G2 PASS                   ≠ every reading resolved / transcription "finished"
Project research_function principal ≠ historical principal actor/role
canonical Source node     ≠ any generic citation/information source
textual witness           ≠ historical/legal witness
same wording              ≠ same identity / date / hand / production stage
resource unavailable      ≠ task blocked / NEXT ACTION changed / STOP
```

This check does not create a universal glossary, translation registry or ontology. `AGENTS.md` owns the universal guardrail; D-019 records the durable cross-project decision. The owning scholarly/technical contract remains authoritative for each local meaning.

## Current-work-target authority

At task start and whenever `NEXT ACTION` changes, verify that the current executable target is traceable to the canonical Project purpose/scope or another explicit authority source.

Do not infer current priority from Source/File identity, `project_source_id`, structural status, research-function labels, upload order, File availability, staged evidence, a migration fixture, GitHub scheduling or whichever prerequisite required the most recent work.

The underlying Project/priority semantics are owned by `project-lifecycle.md`. This workflow enforces only the execution consequence:

> If target authority is missing, preserve valid completed evidence/support work and block only the unsupported target mutation. Do not invent a replacement priority.

A support task may be necessary and complete without becoming the scholarly objective it supports.

## Resource state and dependency provenance

Resource/capability state is **descriptive execution evidence**, not authority over the task or roadmap.

When a PDF, scan, attachment, credential, tool capability, repository write path or other resource needed for an action is unavailable, report it immediately in action-local form:

```text
RESOURCE UNAVAILABLE: <resource/capability>
AFFECTED ACTION: <specific action that cannot currently execute>
OBSERVED BASIS: <what was actually tested/seen>
```

Before promoting that fact to `BLOCKED`, `STOP`, a changed `NEXT ACTION`, a task-wide prerequisite, a roadmap dependency or substitute work, identify the **dependency authority** that establishes that consequence:

```text
DEPENDENCY AUTHORITY: <canonical task/Project owner or explicit Human-Owner decision>
DEPENDENCY: <resource X is prerequisite for action/task Y>
AUTHORIZED CONSEQUENCE: <only what that authority actually says>
```

If the authority is absent or ambiguous:

- preserve the resource fact and affected-action limitation;
- do not infer a broader blocker or planning consequence;
- do not select another Source, witness, tool, support task or scholarly target as a substitute;
- surface the planning ambiguity to the Human Owner when it materially affects continuation.

Resource absence does not relax evidence standards. An action that requires unavailable evidence still cannot be simulated, completed from metadata/prior transcription, or silently replaced by a parallel witness.

## Sticky prerequisites

A prerequisite deterministically established as `PASS` remains `PASS` for the current execution context until an explicit invalidation event occurs.

Valid invalidation events include, as applicable:

- actual retrieval/access failure;
- checksum/identity contradiction;
- rights/authority change;
- relevant canonical state change making the earlier check stale.

New model uncertainty is not an invalidation event.

Re-entering an already-passed prerequisite without invalidation is an execution fault, not progress.

An invalidated prerequisite changes only the dependency whose authority is already established. It does not itself select a new task, priority or roadmap consequence.

## Evidence staging for visual work

Source/File identity and preservation semantics are owned by `source-and-provenance.md`. For execution, keep these target-context states distinct:

```text
RETRIEVABLE        an authorized path can recover the bytes
STAGED              the required evidence object is present in the target work context
VISION-INSPECTABLE  the scholarly context can actually inspect the required pixels
```

Derived gate:

```text
VISUAL EVIDENCE READY = PASS
iff STAGED = PASS
and VISION-INSPECTABLE = PASS
for the same evidence object in the same target context
```

Historical success in another session does not establish current `STAGED` or `VISION-INSPECTABLE` state.

If the object is staged but inspectability has not yet been demonstrated, the target scholarly context may perform one local preflight:

```text
STAGED = PASS
→ local pixel-inspectability check
→ VISION-INSPECTABLE = PASS
→ execute source inspection
```

If the check fails:

```text
VISION-INSPECTABLE = FAIL
→ EVIDENCE NOT READY FOR THAT VISUAL ACTION
→ report resource state + affected action
→ do not simulate scholarship from metadata/transcription alone
```

After this failure the scholarly role does **not** perform upstream evidence search, retrieval diagnosis or access repair unless that support action is separately authorized. It does not infer task-wide blocker/STOP/NEXT-ACTION semantics from the readiness failure. Apply the resource/dependency-authority rule above.

Do not use `EVIDENCE STAGED = PASS` as an ambiguous composite token.

If the decisive staging capability lies outside repository/tool control, record the platform/resource boundary and affected action instead of building repo machinery that cannot cross it or manufacturing a roadmap consequence.

## Repository-first persistence in execution contexts

Keep transient evidence processing distinct from research-state persistence.

```text
EPHEMERAL TECHNICAL PROCESSING
staged source bytes | renders | crops | temporary calculations

PERSISTABLE / RESTART-RELEVANT RESEARCH STATE
readings | decisions | evidence notes | Project state | durable research artifacts
```

The first class may exist temporarily in the target execution environment when required for source inspection or technical computation. The second class must not use the chat/tool sandbox as an intermediate working store when an authorized repository write path is available.

For persistable research state:

1. resolve the scholarly object and its canonical owner/artifact role before creating or changing a file;
2. use the intended repository working branch as the working persistence surface;
3. once a bounded result is ready to persist, create/update it directly through the authorized repository write path rather than first writing a local TSV/Markdown/JSON/YAML research file for later promotion;
4. keep exploratory reasoning transient until it becomes a persistable result; not every hypothesis or scratch thought requires a commit;
5. if a repository write path is unavailable or fails, preserve the already-canonical state and report the unavailable capability plus the affected persistence action; do not create a local research-state fallback or infer broader task/priority consequences without dependency authority;
6. where a temporary image/derivative materially supports a consequential result, preserve the required provenance under the applicable Source/File/evidence rules before relying on that result in a future context.

This is an execution rule, not a requirement to store source binaries in Git or to commit every intermediate thought. Rights/access rules still govern source-byte persistence, and `maintenance.md` still governs canonical ownership and propagation.

## Progress / delta and loop control

A repeated action, delegation or return is justified only when at least one material state changes, for example:

- new evidence was inspected;
- uncertainty/decision state changed;
- the bounded question became narrower;
- canonical state advanced;
- a prerequisite was invalidated;
- escalation/review level changed for a stated reason.

Repeated delegation with no evidence/state/question delta is a `no-progress / delegation-loop candidate`.

On first detection, redirect to the valid cursor. If the same no-delta re-entry repeats, stop the loop, preserve current state and route the execution/process defect to its owner. Resume scholarship only from a valid executable state.

This rule does not forbid legitimate scholarly iteration where new inspection/comparison/judgement changes evidential state.

## Senior Domain → Senior Dev interface

A demonstrated research-system/process problem crosses into Dev/RSE only after the scholarly/domain side has established enough meaning to avoid technical guesswork.

The domain side supplies:

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

Before Dev treats a domain phrase as a field, enum, status, entity, relation or acceptance token, apply the semantic-boundary check above. A technically convenient name is not authority to collapse distinct domain meanings.

The domain side does not prescribe connector architecture, retry logic, state-machine design, storage/platform selection or other implementation mechanics unless already governed by the admitted requirement.

The Dev/RSE side then owns:

```text
REHYDRATE canonical state
→ VERIFY scope / authority / requirements
→ CAPABILITY / FEASIBILITY TEST
→ BOUND repository vs platform responsibility
→ DESIGN smallest adequate mechanism
→ EXECUTE admitted deterministic mechanics
→ VERIFY invariants / regression / provenance / restartability
→ PERSIST consequential result
→ RETURN to the correct scholarly/domain owner
```

Dev does not re-adjudicate manuscript readings, scholarly classification, research purpose or other owner-reserved semantics. Technical `PASS` is not scholarly acceptance.

When Dev returns a result, translate technical outcomes back into the owning domain's language without upgrading them: state exactly which deterministic property passed/failed, what scholarly meaning remains untested and what domain review is still required.

## Consequential technical Issue contract

A consequential technical/process Issue is ready for Dev when these meanings are reconstructable:

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
RETURN / CLOSE CONDITION
```

Derive stable facts from canonical state where possible. Do not turn this into a mandatory template family.

For material research-system changes, this contract does not replace D-016 admission in `maintenance.md`.

A domain observation must not automatically become a Dev requirement. First determine whether it is incomplete research, Project-local, already covered, genuinely reusable/systemic, specialist-dependent, or no action.

## State transition and canonical freshness

A completed stage/handoff is not restartable if the canonical restart surface still points to the prior stage.

Whenever a consequential stage or authorized `NEXT ACTION` changes, run the smallest freshness pass:

```text
result persisted in canonical owner
→ Project STATUS/restart state synchronized where applicable
→ current target authority still valid
→ handoff points to current canonical state
→ stale prior prose is not treated as authority
```

When a consequential stage/result transition falls inside an already-established broader programme or planning context and can materially affect programme completion/maturity, selectable/current work, or materially affected restart/navigation state, apply the **programme/phase/result-transition reconciliation owned by `maintenance.md`** and return its disposition to the existing programme/planning owner before treating the handoff as complete. This execution hook does not redefine that rule and does not create a programme owner, priority or `NEXT ACTION`.

Freshness is not authority. A synchronized repository can still reproduce an unauthorized priority or blocker, so target authority and dependency authority must be checked separately.

## Review points in the flow

Use consequence-scaled review at real transitions:

```text
TASK START
→ role/authority + prerequisite/evidence check

WORK / ITERATION
→ progress/delta check when triggered

RESULT HANDOFF
→ persistence + unresolved/non-result + return question

PRE-DEV
→ requirement/scope/authority/D-016 state

DEV / PRE-MERGE
→ technical assurance + regression/provenance/loss/rebuild checks

DEV RETURN
→ scholarly/domain adequacy where scholarly meaning is affected

STATE TRANSITION
→ canonical freshness + target authority + restartability
```

The review may use a fresh/independent context when consequence or self-review risk warrants it. Do not create permanent roles merely to name review lenses.

Detailed review/certification questions live in `quality-and-learning.md`.

## Persistence and canonical owners

When durable truth changes, update the owning canonical record during the same work block when practical. Use `maintenance.md` for propagation and `README.md`/generated context for navigation.

Do not maintain a second routing table here.

Do not make a future context recover durable research state from chat.

## Gate and priority boundary

`research-gates.md` owns G1–G6 maturity semantics. Project `STATUS.md` owns actual Project gate/restart state.

A gate requirement or support task may justify work only when it is also compatible with the authorized current target. Gate readiness, technical readiness, resource readiness or Milestone scheduling does not independently select research priority or task-wide blocker state.

## Deferred technology

If a useful technical option is not required by an authorized current need, preserve it as a trigger-based Issue rather than implementing it speculatively.

## Operational acceptance test

A fresh capable context passes the workflow/restart test when it can answer without old chat:

- what role/stage may execute now;
- what bounded action is authorized;
- which prerequisites are PASS/FAIL/unknown and what invalidates PASS;
- which exact evidence is required and whether it is actually ready in this context;
- for any claimed blocker/STOP/dependency, which authoritative owner establishes that consequence;
- where the execution cursor/completion boundary lies;
- what is explicitly out of scope;
- what changed since the prior state;
- who receives the result and under what return condition;
- for any consequential cross-domain/technical/human wording, what semantic owner defines it and whether the translation preserved scope, status and uncertainty.

If the answer requires replaying a prior chat, re-running an already-valid prerequisite without cause, inferring priority or blocker state from structural/support/resource state, or relying on an unstated semantic conversion between domains, the execution surface is not restartable.

## Research execution: protect the first scholarly action

For an authorized research work block, identify the **first scholarly action** before substantial support work expands. This is the first bounded action that either inspects new scholarly evidence, discriminates a scholarly hypothesis, changes a relevant scholarly uncertainty/decision state, or establishes a bounded scholarly evidence ceiling.

Before broader activation, state synchronization, tooling or assurance work, perform the cheapest legitimate feasibility preflight for that action:

```text
FIRST SCHOLARLY ACTION
→ exact evidence/capability required
→ canonical evidence/access owner or path
→ cheap feasibility/access test where available
→ report unavailable resource + affected action immediately
→ only the separately authorized support work required to make that action executable
```

This preflight does not waive authority, provenance, Evidence Readiness, Target Return, sticky prerequisites or required canonical synchronization. It changes ordering: verify the real research execution path before support work recursively expands.

If the first scholarly action cannot execute because a resource/capability is unavailable, record that action-local resource fact early. Do **not** promote it to task-wide blocker/STOP/NEXT-ACTION/roadmap semantics unless an authoritative dependency explicitly establishes that consequence.

### Scholarly delta and support delta

Keep two kinds of legitimate progress distinct:

**Scholarly delta** includes, as applicable:

- new primary/specialist evidence actually inspected;
- a scholarly hypothesis discriminated;
- relevant scholarly uncertainty or decision state changed;
- a bounded scholarly evidence ceiling established.

**Support delta** includes, as applicable:

- canonical/current state synchronized;
- tests or CI repaired;
- evidence-access/restart machinery changed;
- branch/PR/merge completed;
- support metadata or technical readiness advanced.

A support delta may be necessary and valuable, but must not be represented as scholarly progress merely because canonical or technical state changed.

### Support-to-support escalation stop

Before the first scholarly action occurs, if one support action exposes another support action, immediately re-run Goal Alignment from `quality-and-learning.md`:

> Does the next support action directly make the first scholarly action executable, or protect a required invariant for that immediate execution?

If **yes**, perform it only when that support action is already authorized by the task/owner state. If **no**, defer it or route a demonstrated separate system defect to its owner without continuing that defect inside the research work block.

An unavailable resource is not itself authorization to create a support task. If acquiring/repairing the resource is not already authorized, report the resource gap and affected action rather than turning the gap into a self-generated work chain.

Do not allow an open-ended support chain merely because each step creates a local technical/canonical delta.

### Research-workblock terminal semantics

A substantive research work block should terminate in one of these research-relevant outcomes:

1. **SCHOLARLY DELTA** — the scholarly state materially advanced;
2. **SCHOLARLY EVIDENCE CEILING** — the bounded question was tested and the current evidence cannot responsibly discriminate further;
3. **AUTHORIZED BLOCKER / ESCALATION** — an evidenced condition prevents continuation **and** the applicable canonical/explicit authority establishes the dependency and its task-level consequence.

A resource unavailable only in the current context is not automatically a terminal research outcome. Record the resource fact and affected action; do not call it an evidence ceiling or task blocker without the required authority.

`CI green`, `state synchronized`, `PR merged`, `restartability improved` or another support-only result may be necessary milestones, but do not by themselves satisfy the terminal research outcome.

Project-specific incidents belong in their Issues/audit evidence as regression fixtures; generic METHOD states only the reusable authority/resource rule.