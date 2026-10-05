# Work prompt — repair the gap between documented learning and claimed operational learning

Status: **EXECUTED REPAIR SPECIFICATION / HISTORICAL PROMPT.**  
This prompt does not itself change METHOD, Project state, requirements, implementation authority, #225 priority or any `Wissensarbeit` execution cursor.

Parent system context: `paleo-type` #225.  
Cross-repository generic evidence source: `esany/Wissensarbeit`.

## 1. Problem to repair

Two separate failures occurred and MUST remain separate.

### Failure A — pre-existing rule was not applied

Before the Human asked to persist the learning, the system already contained relevant semantics:

- Human/Owner statements are evidence of need/intent/constraint, not automatic Requirement/decision/architecture authority;
- new aspects must be reconciled against the governing objective and whole state;
- material semantic ambiguity requires Human consultation;
- local failure should be corrected and then return to the valid higher-level cursor;
- Generic-Fit precedes framework growth.

Nevertheless, the assistant repeatedly misclassified Human symptom feedback as direct product/system redirection.

This failure is already documented in:

- `requirements/human-feedback-intent-classification-learning-2026-09-18.md`
- `esany/Wissensarbeit/project/audits/WA-AUDIT-2026-09-18-HUMAN-INTENT-SYMPTOM-DELTA.md`

### Failure B — persistence was overstated as operational learning

After the Human explicitly asked to **secure the learning**, the assistant:

1. persisted learning/audit evidence;
2. explicitly left it non-normative and non-promoted;
3. did not add or prove an executable regression or other enforcement;
4. did not establish a new operational guarantee;
5. then told the Human in chat, in substance:

> “And exactly for that reason, this applies going forward…”

That statement exceeded the actual repository-backed assurance state.

The assistant collapsed:

```text
learning observed
→ learning documented/persisted
```

into:

```text
learning operationally integrated
→ future behavior reliably changed
```

without evidence for those stronger states.

This second failure is the primary target of this work prompt.

## 2. Governing question

Determine and repair, using current repository truth:

> **What exactly must be persisted, reconciled, normatively integrated, executable or verified before the system may claim that it “learned” from a failure or that a behavior “will apply going forward”?**

Do not assume that every learning requires a new rule or test.

Do not assume that writing a learning file is operationalization.

Do not assume that an existing rule is operational merely because prose already states it.

## 3. Fresh context required before action

Freshly read at minimum in `esany/paleo-type`:

- `GOVERNING_OBJECTIVE.md`
- `AGENTS.md`
- `methodology/maintenance.md`
- `methodology/workflow.md`
- `methodology/quality-and-learning.md`
- `methodology/ai-governance.md`
- `requirements/human-feedback-intent-classification-learning-2026-09-18.md`
- `requirements/design-product-development-methodology-learning-2026-09-19.md`
- current Issue #225 body and current comments

Freshly read at minimum in `esany/Wissensarbeit`:

- `project/GOVERNING_OBJECTIVE.md`
- `project/CURRENT_STATE.md`
- `project/requirements.json`
- `project/quality.json`
- `system/authority.json`
- `system/reconciliation.json`
- `system/building_blocks.json`
- `system/lifecycle.json`
- `tests/evals/failure_corpus.json`
- `project/conversation_harvest_p1_v1.json`
- `project/audits/WA-AUDIT-2026-09-18-HUMAN-INTENT-SYMPTOM-DELTA.md`
- `project/audits/WA-AUDIT-2026-09-19-DESIGN-PROJECT-DEVELOPMENT-METHOD-DELTA.md`
- current Issue #7 and the current execution cursor

Do not reconstruct current authority or cursor from this prompt.

## 4. Evidence discipline

Keep these evidence classes separate.

### A. Human evidence

The Human explicitly distinguishes:

- the original failure before the persistence request;
- the later failure after the persistence request;
- “documented in repo” from “integrated so it affects future work”.

Treat this as owner-need / quality evidence, not automatic solution authority.

### B. Repository state

Use the current repositories to establish:

- where the learning is merely described;
- whether the relevant behavior already exists normatively;
- whether the behavior is part of an operational contract;
- whether any deterministic/procedural regression exists;
- whether any real restart/eval has demonstrated the behavior.

### C. Assistant claims

Audit what the assistant told the Human against what the repository actually established.

Do not defend intent. Evaluate assurance level.

## 5. First analytical task — reconstruct the exact assurance ladder

Do not invent a new canonical taxonomy unless required.

Start from existing repository semantics, including the `Wissensarbeit` audit distinctions such as documented/canonical/implemented/tested/real/enforced/human-visible and the existing separation of:

- candidate vs accepted;
- analysis evidence vs normative rule;
- technical PASS vs Domain Truth / Owner Acceptance;
- persisted state vs executable mechanism;
- regression candidate vs executable regression;
- local PASS vs higher-level acceptance.

Produce a precise mapping for this case answering:

| Question | Required answer |
|---|---|
| Was the failure observed? | evidence |
| Was it persisted? | exact owner/path |
| Was it systemically reconciled? | exact evidence |
| Is the corrective behavior already normative? | owner and scope |
| Was any normative owner actually changed? | yes/no |
| Is the behavior executable/procedural rather than prose-only? | mechanism |
| Is there a regression/eval? | candidate vs executable |
| Has the behavior passed a real/fresh-context fixture? | evidence |
| What future-behavior claim is justified by that state? | calibrated wording |

The key question is not “is there a file?” but:

> **What level of assurance does that file actually establish?**

## 6. Second analytical task — classify Failure B

Test Failure B against existing generic failure families, especially:

- false assurance / overclaiming;
- authority/promotion creep;
- systemic drift/local optimization;
- execution/progress pathologies;
- restart/context-fidelity gaps.

Determine whether this is:

1. only a case-specific communication error;
2. a missing application of an existing generic safeguard;
3. an under-specified generic safeguard;
4. an executable-regression gap;
5. evidence requiring a normative change.

Give a reasoned disposition. Do not jump to option 5.

## 7. Third task — determine the correct owner(s)

For every necessary correction, identify **one existing owner where possible**.

Possible owner classes to test:

### In paleo-type
- `methodology/quality-and-learning.md` for what “learning” means and when promotion is justified;
- `methodology/workflow.md` for return-to-cursor / operational behavior;
- `AGENTS.md` only if a stable always-on guardrail is genuinely missing;
- #225 if this is only system-level reconciliation/acceptance evidence;
- the existing learning artifact if the missing content is historical case evidence only.

### In Wissensarbeit
- existing Requirement(s), especially REQ-003/004/007/011;
- `BB-LEARN`, `BB-INTEGRATE`, `BB-ASSURE`, `BB-TRACE`;
- `system/authority.json`;
- `tests/evals/failure_corpus.json`;
- existing eval fixtures.

Do not create a new owner merely to make the distinction explicit.

## 8. Fourth task — repair the historical record

Persist the second failure explicitly.

At minimum the repository must be able to reconstruct without this chat:

1. the learning was persisted as **evidence only**;
2. no normative METHOD/Requirement change was made at that point;
3. no executable regression was promoted at that point;
4. no real fixture had demonstrated changed future behavior;
5. the assistant nevertheless described the behavior to the Human as if future application were established;
6. that wording was an **overclaim of learning/operational assurance**;
7. the correct status at that moment was narrower.

Do not rewrite or delete the original historical artifacts. Add a corrective record or refine an existing learning only where provenance remains clear.

## 9. Fifth task — define calibrated claim semantics

Derive from existing semantics what the assistant may say at each state.

Example form to evaluate/refine:

- **Observed:** “We have evidence of this failure.”
- **Persisted:** “The learning is documented and restartable.”
- **Reconciled:** “The learning has been dispositioned against existing system owners.”
- **Normatively integrated:** “The applicable repository rules now require this behavior.”
- **Executable/procedurally guarded:** “A mechanism/check exercises part of the behavior.”
- **Regression-tested:** “The stable invariant is covered by an executable regression.”
- **Real-world/fresh-context demonstrated:** “The behavior has been demonstrated under the tested fixture.”

Do NOT automatically accept these labels as a new canonical status model.

The deliverable is the **claim calibration rule**, not a new status ontology.

Core invariant to test:

> **Never claim a stronger learning/operational state than the strongest evidence actually establishes.**

## 10. Sixth task — determine whether an operational gap remains

After historical correction, ask:

### If existing normative rules already require the behavior
Then the issue may be:
- application fidelity;
- context compilation;
- evaluation coverage;
- or model behavior.

Do not duplicate the rule.

### If the stable safeguard is absent
Then propose the smallest refinement to an existing owner.

### If part of the safeguard is deterministic/procedural
Add or propose a regression only for that stable part.

Examples of stable negative invariants that may be testable:

- a `SYSTEM LEARNING / FAILURE EVIDENCE ONLY` artifact must not be represented as normative METHOD;
- a regression candidate must not be represented as an executable regression;
- a non-admitted analysis/audit must not be represented as implementation authority;
- a persisted learning without stronger evidence must not produce a derived status claiming “operationalized” or “verified”.

Do not attempt to deterministically classify all natural-language Human intent.

## 11. Seventh task — fresh-context falsification

Design or execute, only where current authority permits, a fresh-context check:

Give a fresh capable context only repository state and ask it to determine:

- what happened;
- what the learning says;
- what is actually integrated;
- what is merely evidence/candidate;
- whether future behavior is guaranteed/tested;
- what claim it may responsibly make to the Human.

Failure condition:

> A fresh context reads the learning file and concludes “this behavior is now operationally guaranteed” when the repository only supports “documented learning / existing rule / candidate regression”.

This is a restartability/XAI test, not proof that a language model can never repeat the behavior.

## 12. Cross-repository Generic-Fit

Audit whether the paleo-type failure supplies new evidence to existing `Wissensarbeit` families.

In particular inspect:

- FF-FALSE-ASSURANCE;
- FF-EXECUTION-PROGRESS;
- FF-SYSTEMIC-DRIFT;
- BB-LEARN;
- BB-ASSURE;
- BB-TRACE.

Expected default:

> refine evidence / regression coverage before inventing new architecture.

If the generic lesson is already owned, preserve that fact and avoid duplicate prose.

## 13. Required outputs

Produce and persist, as warranted by the analysis:

### A. Corrective failure record
A repo-backed description of Failure B:
**documented learning was overstated as operationally integrated learning.**

### B. Owner/disposition matrix
For each affected existing owner:
- current semantics;
- demonstrated gap;
- disposition: unchanged / refine / candidate regression / needs decision;
- rationale.

### C. Claim-calibration rule
What the system may say about:
- documented;
- integrated;
- operational;
- tested;
- verified;
- real-world proven.

Use existing semantics rather than introducing status inflation.

### D. Regression decision
State separately:
- what can be tested deterministically/procedurally;
- what remains judgement-based;
- what real fixture would be needed for stronger assurance.

### E. Repository reconciliation
Update #225 and, if genuinely generic, the appropriate `Wissensarbeit` audit/evidence owner.

### F. Final assurance statement
End with a precise answer:

> **What changed in the repository, what behavior is now required, what is now tested, and what is still only a learning/expectation?**

## 14. Anti-drift constraints

Do NOT:

- create a “learning management system”;
- invent a maturity model for learnings;
- add a new workflow engine;
- add a new Requirement merely because Failure B is embarrassing;
- treat prose persistence as enforcement;
- treat an executable test as proof of all AI behavior;
- treat Human dissatisfaction as automatic architecture authority;
- move the #225 main cursor unless current owners and Human authority actually do so;
- change `Wissensarbeit`'s execution cursor through this repair unless its own current authority requires it.

## 15. Quality checks

The repair passes only if all are true:

1. **Historical honesty:** the repo shows that the prior “going forward” claim exceeded evidence.
2. **State calibration:** persisted / normative / executable / tested / real evidence are not collapsed.
3. **Owner fit:** corrections land in existing owners where possible.
4. **No duplicate truth:** learning evidence is not turned into a parallel policy store.
5. **No fake determinism:** semantic Human-intent judgement remains judgement where appropriate.
6. **Regression proportionality:** only stable invariants are mechanized.
7. **Restartability:** fresh context can reconstruct the exact assurance state.
8. **Cursor integrity:** local repair does not become a new programme.
9. **Human XAI:** future user-facing claims state what has actually been secured, not what the assistant hopes to remember.
10. **Generic-Fit:** cross-project learning is refined only to the extent supported by evidence.

## 16. Stop condition

Do not continue into broader design-methodology work in the same repair.

This prompt closes only the specific missing chain:

```text
failure
→ learning evidence
→ persistence
→ integration/disposition
→ operational/test status
→ calibrated Human-facing claim
```

The broader weakness in user research / design / project-development methodology remains separately documented and must not be silently absorbed into this repair.


## 17. Restart / owner linkage after chat-knowledge-monopoly audit — 2026-09-23

A fresh audit of the current chat against repository state found:

- the material distinction between **Failure A** (pre-existing rule not applied) and **Failure B** (persisted learning overstated as operationally integrated future behavior) is already contained in this prompt;
- the broader Human-feedback and design-methodology learnings are also persisted in their dedicated evidence files;
- therefore the substantive learning is **not chat-only**;
- however, this prompt was not yet linked back from the current parent owner #225, creating a discoverability/restartability gap for a fresh context that starts from the owner rather than from recent commits/files.

### Current disposition

This prompt is now explicitly classified as:

- **owned repair-analysis evidence under #225**;
- **not executed yet**;
- **not an implementation admission**;
- **not a new #225 NEXT ACTION or priority**;
- **not authority to change any manuscript Project scope**;
- **not evidence that the corrective behavior is already operationally guaranteed**.

The purpose of the owner linkage is only to ensure that a fresh context can discover:

1. why the repair prompt exists;
2. which historical overclaim it is meant to analyze/repair;
3. that the work is still pending analysis/execution rather than complete;
4. that the higher-level #225 cursor remains unchanged unless separately changed by valid authority.

This section repairs **discoverability and restartability only**. It does not itself perform the repair tasks defined above.


## 18. Execution completion — 2026-09-23

This repair specification has now been executed.

Execution prompt:
`requirements/learning-integration-claim-repair-execution-prompt-2026-09-23.md`

Completed result:
`requirements/learning-integration-claim-repair-result-2026-09-23.md`

Cross-project Generic-Fit evidence:
`esany/Wissensarbeit/project/audits/WA-AUDIT-2026-09-23-LEARNING-ASSURANCE-OVERCLAIM-DELTA.md`

The execution found no missing generic METHOD rule requiring D-016 implementation. The demonstrated defect was primarily false assurance/application fidelity: existing owners already prohibit claims stronger than their evidence/assurance state. No executable natural-language behavioral regression was added, and no guarantee of future model compliance is established.

This prompt is no longer an open work router. The #225 main cursor remains governed by #225 itself.
