# `.prompt` capability transfer candidate — 2026-10-04

**Status:** NON-NORMATIVE CAPABILITY CANDIDATE / TRANSFER EVIDENCE — **NOT ACTIVE REPOSITORY SKILL / NOT D-016 ADMITTED**  
**paleo-type baseline:** `main@68c9536cfc566cd629aeaaae9ba2ad778cf0f9e7`  
**Comparator:** `esany/Wissensarbeit@b448915cf774c573dbf82cf2e17bcb03c10a9ed8`  
**Comparator sources:** `skills/prompt/skill.md`, `skills/prompt/CONTRACT.md`, `skills/prompt/references/core-method.md`  
**Work owner:** #252; parent #244  
**This candidate is not:** METHOD, planning authority, a workflow engine, a Context Compiler, task execution, repo-write permission, D-016 admission, independent review, or a claim that the Wissensarbeit candidate has Generic Fit.

## 1. Transfer disposition

The Human Owner explicitly requested at least the `.prompt` approach from Wissensarbeit.

Fresh comparator inspection shows a useful bounded capability, but also an important authority limit: the Wissensarbeit implementation calls itself a **Skill candidate**, has executable/real-use evidence, is **not regression-protected**, is **not Generic-Fit**, and creates no authority.

Therefore the valid transfer is:

> **adapt the behavior/contract as a paleo-type candidate, preserve provenance and limits, test it here, then decide whether operational activation is routine or a material system change.**

Do not 1:1 copy its repository/product authority.

---

## 2. Candidate user contract

### `.prompt <task>`

Return a **copy-ready prompt** for `<task>`.

Do **not** execute the task.

The produced prompt should be the smallest instruction that remains sufficient for correctness, authority, evidence, closure and the requested output.

### `.prompt review <prompt>`

Review and improve the supplied prompt against the actual task/context.

Return a copy-ready improved prompt plus only the bounded explanation needed to understand material corrections.

Do not silently change purpose/scope/authority.

### `.prompt test <prompt/result/context>`

Evaluate prompt behavior/result quality against explicit criteria/failure patterns.

State what the test actually demonstrates. Internal/self-review is judgement/evidence, **not independent proof**.

---

## 3. Core invariants

1. **Prompt creation is not task execution.** `.prompt` returns the prompt and stops.
2. **Candidate output has no authority.** A generated prompt cannot create Project scope, priority, D-016 admission, accepted Requirements/ADRs or scholarly truth.
3. **Fidelity before token savings.** Compact only after required meaning is preserved.
4. **No mega-template by default.** Include only instruction blocks needed by this task.
5. **Derive before asking.** Do not make the Human resupply repository facts/current state the tool can resolve safely.
6. **Repo target check.** For consequential repository work, the prompt must require fresh authority/current-owner reads appropriate to that repository/task rather than paste stale state.
7. **Capability admission.** Do not instruct an executor to use unavailable tools/capabilities; state bounded fallback/blocker semantics where needed.
8. **Approval gates only where authority requires them.** Do not add Human confirmation ceremonies to routine bounded work; do not omit a genuine material decision boundary.
9. **Closeable work.** Material work prompts state completion/return conditions rather than `continue until done` ambiguity.
10. **Context is selected, not starved.** Use applicable current context and pointers to deeper evidence; do not delete authority/uncertainty/provenance to reduce length.
11. **Independent review is not faked.** A new pass by the same source/model is not called independent evidence unless independence is actually established.
12. **Repository vocabulary belongs to the repository.** Do not import Wissensarbeit status enums/Building Blocks/product semantics unless separately justified.

---

## 4. paleo-type-specific repo behavior

When `.prompt` targets `esany/paleo-type`, generated prompts should normally include only the repository instructions materially needed by the task, while preserving these invariants by reference:

- repository is current authority;
- fresh `GOVERNING_OBJECTIVE.md` + `AGENTS.md` + applicable canonical owner/rules before consequential work;
- no Project/scholarly `NEXT ACTION` from Source/File/system work;
- material research-system implementation follows D-016;
- repo-first persistence for restart-relevant work;
- technical PASS != scholarly/specialist/Human acceptance;
- complete **applicable** context, not indiscriminate repo loading;
- Local PASS != System Closure where a broader owner exists.

Do not paste the entire guardrail corpus into every prompt. A repository-capable executor should be instructed to read the owners freshly.

---

## 5. Candidate prompt construction method

For a requested task:

```text
1. Identify requested outcome.
2. Identify target repository/system and executor capability.
3. Resolve what context the user has already supplied.
4. For repo work, name the fresh authority/current-owner reads required.
5. Derive demonstrated problem / required effect before prescribing architecture.
6. Include only task-relevant constraints, evidence, non-goals and decision boundaries.
7. State output/deliverables.
8. State completion/stop/return condition.
9. Add consequential write/admission gate only if actually required.
10. Run a late failure-pattern review.
11. Return copy-ready prompt; do not execute it.
```

### Failure-pattern review

At minimum challenge:

- **anchoring:** does the prompt hard-code a preferred solution before analysis?
- **missing authority gate:** could it perform a consequential write/admission without permission?
- **open read scope:** does it say `read everything` without an applicability strategy?
- **contradiction:** does one instruction defeat another?
- **mega-prompt/repetition:** are repo rules duplicated instead of referenced/read freshly?
- **non-closable work:** is there no completion/return condition?
- **parallel vocabulary:** does it invent new statuses/owners without need?
- **wrong repo/target:** can it act against the wrong repository or owner?
- **capability mismatch:** does it require unavailable tools/platform actions?
- **independence overclaim:** does internal review masquerade as independent evidence?
- **checklist score:** does formal completeness substitute for substantive adequacy?
- **authority laundering:** does context, Issue state, CI or generated prompt manufacture scope/priority/acceptance?

---

## 6. Output contract

Default output:

```text
<one copy-ready prompt block>
```

Add explanation only when needed for a material ambiguity/correction or when requested.

A prompt should explain uncommon abbreviations on first use or avoid them. Do not make the Human decode internal process jargon.

If a prompt includes a Human decision, explain in plain language:

- what is being decided;
- why Human authority is needed;
- what each option changes;
- what remains unchanged.

---

## 7. Candidate result statuses

Avoid importing a mandatory lifecycle. For evaluation only, useful plain-language dispositions are:

- **copy-ready** — prompt can be used for the stated task;
- **copy-ready with bounded assumptions** — assumptions are explicit;
- **blocked** — a missing fact/capability prevents a safe sufficient prompt;
- **needs Human decision** — a genuinely non-derivable decision is required before prompt completion;
- **untested candidate** — a prompt/capability has been specified but not behavior-tested.

The Wissensarbeit term `declared` is not adopted automatically.

---

## 8. Initial paleo-type tests required by #252

At minimum test:

1. **simple copy-ready writing/analysis prompt** — verify no repo ceremony is added.
2. **paleo-type read-only audit prompt** — fresh owners required, no whole-repo dump by default.
3. **paleo-type consequential repo-write prompt** — correct D-016/authority boundary and repo-first persistence.
4. **prompt review** — catch a solution-anchored / mega-prompt variant.
5. **prompt test** — correctly state that self-review is not independent proof.
6. **Human-facing decision prompt** — no unexplained `DEV-READY`, `D-016`, `EKCP` shorthand without context.

Kill/reshape the capability if ordinary direct prompting achieves equal reliability with lower maintenance burden or if `.prompt` becomes a covert planner/context owner.

---

## 9. Information-class consequence

The transfer reinforces a needed distinction for #251:

```text
Prompt / work instruction
!= Requirement
!= Plan
!= METHOD
!= Current State
!= Decision
```

Historical one-off prompts remain evidence/history. Reusable prompt capability belongs in a deliberately selected capability surface only if #252 demonstrates value and authority compatibility.

---

## 10. Current disposition

The `.prompt` behavior is now **transferred as a documented paleo-type candidate**, satisfying the requested knowledge transfer without silently activating a new repo-wide operating rule.

Next activity under #252: run the representative tests and decide the proper operational home/materiality boundary. Until then, typing `.prompt` is not a repository-governed command merely because this candidate exists.
