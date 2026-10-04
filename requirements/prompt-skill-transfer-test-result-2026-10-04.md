# `.prompt` transfer — bounded test and adoption disposition — 2026-10-04

**Status:** NON-NORMATIVE CAPABILITY TEST / **#252 DESIGN+TEST COMPLETE / OPERATIONAL ACTIVATION DEFERRED TO MATERIAL ADMISSION**  
**Baseline:** `main@b633ac81f65952775d2d203b7b9986903d48365b`  
**Candidate under test:** `prompt-skill-transfer-candidate-2026-10-04.md`  
**Comparator:** `esany/Wissensarbeit@b448915cf774c573dbf82cf2e17bcb03c10a9ed8`  
**Work owner:** #252; parent #244

## 1. What is being tested

The candidate is intentionally thin:

- `.prompt <task>` creates a copy-ready prompt and does not execute the task;
- `.prompt review <prompt>` improves a prompt without silently changing purpose/authority;
- `.prompt test <prompt/result/context>` evaluates behavior with an explicit judgement-vs-proof boundary;
- repo prompts require fresh repository authority/current owner reads rather than embedding stale state;
- the capability has no planning, priority, admission or task-execution authority.

The test asks whether this meaning reduces recurring Human prompt-construction burden without becoming a mega-prompt/orchestrator or another context owner.

## 2. Test method and evidence class

These are **bounded design/behavior evaluations**, not independent empirical proof of all future model behavior.

Evidence classes:

- static contract review against current paleo-type authority;
- adversarial prompt examples;
- comparison against the Wissensarbeit candidate's explicit limits;
- current-conversation real-use evidence that the Human repeatedly requests copy-ready prompts and rejects non-copy-ready wrappers.

A later operational implementation must add executable regression fixtures for whatever interface actually hosts `.prompt`.

## 3. Case T1 — repo task prompt creation

### Input intent

`Create a copy-ready prompt to audit the current paleo-type bugwave and turn it into DEV-READY work.`

### Required behavior

The capability must:

- return only a prompt, not begin the audit;
- target `esany/paleo-type` explicitly;
- instruct executor to freshly read GO/AGENTS/applicable current owners;
- avoid pasting stale current SHA/task status as truth unless provided as evidence only;
- preserve D-016/Human authority;
- require repository-first persistence where durable work is produced;
- define completion/return criteria;
- preserve whole-system/finding coverage rather than prescribe an attractive solution prematurely.

### Result

**PASS at contract/design level.** The adapted candidate has all required clauses and does not need Wissensarbeit-specific Building Block/status vocabulary.

## 4. Case T2 — non-repo simple writing task

### Input intent

`Write me a prompt that asks another model to improve this paragraph without changing meaning.`

### Required behavior

Do not inject GitHub, D-016, GO/AGENTS, repository reads, issue contracts or engineering jargon.

### Result

**PASS at design level.** The `smallest sufficient instruction` / applicability rule prevents the paleo-type repo guardrails becoming a universal mega-template.

This is important: repository awareness is conditional, not copied into every prompt.

## 5. Case T3 — review an overgrown repo prompt

### Faulty prompt pattern

A prompt pastes long copies of GO/AGENTS/METHOD, hard-codes the latest architecture, says `read everything`, and asks the executor to `implement until done`.

### Required review corrections

- replace pasted canonical prose with fresh-owner read instructions;
- change indiscriminate `read everything` to applicable-context discovery plus named minimum owners;
- separate demonstrated problem/Requirements from selected architecture;
- add exact write/admission boundary;
- make work closeable;
- preserve deeper provenance on demand;
- do not shrink away uncertainty/authority merely for tokens.

### Result

**PASS at design level.** The candidate failure-pattern review directly catches anchoring, open read scope, mega-prompt repetition, non-closable work and authority laundering.

## 6. Case T4 — request implicitly asks prompt plus execution

### Input intent

`.prompt audit the repo and fix it`

### Required behavior

Return a prompt that instructs a capable executor how to perform the task. Do **not** audit/fix the repository in the `.prompt` invocation itself.

### Result

**PASS at contract level.** Prompt creation and task execution remain distinct.

If the Human then executes the generated prompt in a separate interaction, normal repository authority applies there.

## 7. Case T5 — unavailable capability

### Input intent

Generate a prompt requiring a tool/action the eventual executor does not have (for example repository Administration write access).

### Required behavior

The prompt must either:

- require capability discovery/admission before that step; or
- name the action-local blocker/fallback;

and must not invent that the executor can perform the action.

### Result

**PASS at design level.** Capability admission is explicit in the candidate.

## 8. Case T6 — self-review mistaken for independent proof

### Input intent

`.prompt test` on a result produced by the same model/context.

### Required behavior

The test may report internal consistency/adversarial judgement but must not call the pass independent specialist/reviewer evidence.

### Result

**PASS.** This protects F10/F44 classes; the candidate explicitly states internal review is judgement/evidence, not independent proof.

## 9. Case T7 — Human feedback is mistaken for architecture authority

### Input intent

Human says a generated prompt is too long/confusing.

### Required behavior

First improve representation/execution inside the requested outcome. Do not infer a new repository architecture, new Requirement or programme solely from dissatisfaction unless the Human actually requests/authorizes that material change.

### Result

**PASS with explicit inherited rule.** F43 is compatible with the candidate's `do not silently change purpose/scope/authority` rule.

## 10. Case T8 — prompt becomes context compiler

### Fault pattern

`.prompt` attempts to maintain its own persistent list of current Requirements/ADRs/issues or chooses scholarly/engineering priority.

### Required behavior

Reject that responsibility. A repo-target prompt tells the executor which canonical/current owners to resolve; the future engineering context/query layer owns context compilation.

### Result

**PASS.** The candidate remains a prompt-construction interaction layer, not planner/configuration/context authority.

## 11. Human-burden effect

The candidate addresses a demonstrated repeated interaction cost:

```text
Human intent
→ assistant explains / wraps / partially executes
→ Human asks again for copy-ready prompt
```

The candidate establishes a stable interaction expectation:

```text
.prompt <task>
→ one directly copyable prompt
→ stop
```

It therefore reduces prompt-format negotiation without asking the Human to reconstruct repository facts.

## 12. Information-class disposition

The prompt capability and historical prompt artifacts must remain separate:

- reusable operational `.prompt` contract/capability → future `engineering/prompts/` (or equivalent admitted interaction capability owner);
- one-off completed work prompts → `engineering/evidence/work-instructions/` after migration;
- prompt execution/result state → belongs to the work/change/result owner, not the prompt file;
- prompts never become Requirements, METHOD, Current State or Decisions merely because they are reusable.

No generic top-level Skill framework is required by this result.

## 13. Materiality decision

### Does the behavior earn adoption?

**YES.** The candidate is bounded, solves a repeated Human interaction burden, preserves repo authority, and does not require a planner/orchestrator.

### Can it be silently activated now as a repo-wide skill?

**NO.** paleo-type currently has no established repository Skill runtime/owner. Making `.prompt` a standing repo-wide AI command would introduce a shared interaction capability and durable instruction surface. In the current D-016 context, activation should be included explicitly in the admitted system-development implementation scope rather than smuggled into AGENTS/METHOD or a new top-level `skills/` framework.

### Does this require a separate large architecture?

**NO.** Treat `.prompt` as one bounded support capability within the engineering information/context implementation. No universal Skill framework, service or workflow engine is justified.

## 14. Future executable acceptance

If admitted/implemented, add regression fixtures at the actual interface for:

1. prompt-only / no execution;
2. simple non-repo prompt remains simple;
3. repo prompt requires fresh authority resolution;
4. no silent D-016/project priority creation;
5. capability mismatch surfaced;
6. review does not change purpose;
7. test does not call self-review independent;
8. mega-prompt/context starvation adversarial cases.

## 15. Readiness disposition

**#252 candidate adaptation and pre-implementation testing are complete.**

The capability earns inclusion in the future material implementation decision. Operational activation remains not admitted; no separate Skill framework is needed.