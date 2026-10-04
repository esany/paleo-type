# Bugwave design closure — engineering assurance, CI fitness and local-to-whole return — 2026-10-04

**Status:** NON-NORMATIVE DETAILED DESIGN / **#250 DESIGN COMPLETE / CI IMPLEMENTATION NOT ADMITTED**  
**Baseline:** `main@b633ac81f65952775d2d203b7b9986903d48365b`  
**Work owner:** #250; parent #244  
**Depends on:** #245 finding coverage; #246 configuration/reference semantics; #247 context; #249 readiness/return semantics  
**Explicit residual:** F17 #225 positive scholarly end-to-end acceptance remains outside this change.

## 1. Assurance objective

The engineering plane must be able to prove stable structural/semantic properties that are actually formalizable, while refusing to convert a green check into scholarly adequacy, specialist validation, Human acceptance or whole-system completion.

The target is not `more CI`. It is:

> **every deterministic check maps to a demonstrated failure and a stable canonical contract; every non-deterministic judgement remains visibly outside that check.**

## 2. Assurance dimensions remain separate

The system must preserve at least these dimensions:

```text
technical / deterministic verification
semantic contract consistency
scholarly/domain adequacy
qualified specialist validation
Human/governance decision or acceptance
restartability / context usability
whole-system closure
```

One dimension may provide evidence for another but cannot silently establish it.

## 3. Proposed deterministic engineering fitness set

Only implement a check after the corresponding owner/representation is admitted and stable.

### ENG-FIT-01 — artifact identity / locator integrity

Detect:

- duplicate managed `artifact_id`;
- managed artifact whose current path does not exist;
- stable reference to an unknown artifact/decision/change/Requirement;
- legacy path map pointing to no managed target;
- illegal use of physical path as stable identity where contract requires an ID.

**Closes:** F02/F07/F30 classes.  
**Does not establish:** semantic quality of artifact content.

### ENG-FIT-02 — configuration integrity

Detect:

- missing accepted baseline reference;
- incompatible duplicate current owner for the same configured scope;
- current reference to explicitly superseded artifact without declared exception;
- transition lacking required authority/evidence reference;
- recency/date used as implicit currentness;
- active/admitted change reference to missing change state.

**Closes:** F02–F04/F09/F16/F32 classes.

### ENG-FIT-03 — finding coverage / disposition integrity

Detect at the managed representation level:

- material source declared closed/reconciled but coverage account incomplete;
- material finding with no disposition;
- disposition that requires a target but has no resolvable target;
- `integrated/promoted` finding whose target cannot be found;
- unsupported claim that coverage completeness was proved when source coverage remains `unknown`.

Important: the check cannot determine from arbitrary prose whether a missed finding was materially important. Coverage completeness therefore needs a bounded extraction/review step whose result becomes checkable input. CI verifies that declared coverage/dispositions remain structurally intact; it does not replace analysis.

**Closes:** F29/F35 structural loophole without pretending free prose extraction is fully deterministic.

### ENG-FIT-04 — relation / trace integrity

Detect:

- relation endpoint missing;
- accepted relation using unresolved/candidate status;
- evidence-required relation with missing evidence reference;
- forbidden inference such as `supersedes` based only on dates;
- forward/backward reference asymmetry where the representation requires reciprocal queryability.

Relation completeness is not required. Unsupported relations should be absent or candidate.

### ENG-FIT-05 — generated-view freshness / rebuildability

For any committed generated engineering view:

- regenerate from canonical inputs;
- compare exact expected representation or stable semantic digest;
- fail when stale;
- ensure generated view does not contain fields that have no canonical derivation/declared judgement basis.

If deterministic exact regeneration cannot be guaranteed, do not commit the generated Markdown as a synchronized truth surface; generate on demand.

### ENG-FIT-06 — bounded change state integrity

Detect contradictions such as:

- material change `implementing` while admission says `not-admitted`;
- `closed` with mandatory Result absent;
- `dev-ready` with a declared blocking uncertainty unresolved;
- implementation plan referencing missing accepted/proposed decision basis;
- `accepted/current` transition without Result/decision evidence.

This validates state consistency, not whether the Human should have admitted the change.

### ENG-FIT-07 — context profile integrity

Detect mechanically checkable failures:

- included item with missing applicability basis;
- required canonical owner reference missing;
- task packet missing its work owner/acceptance/whole-return fields where the contract says they are mandatory;
- generated packet claiming authority from Issue/PR/CI state;
- unresolved candidate applicability silently emitted as accepted/applicable.

A separate adversarial review tests context starvation/adequacy; CI cannot prove that every judgement-selected item was epistemically sufficient.

### ENG-FIT-08 — managed link/path migration integrity

During/after migration:

- all managed legacy-path aliases resolve;
- no current owner/reference points at removed old paths without compatibility mapping;
- repository links in managed current surfaces resolve;
- representative historical provenance remains discoverable.

### ENG-FIT-09 — prompt capability contract, if activated

If `.prompt` is operationally implemented:

- `.prompt <task>` returns prompt only and does not execute repository writes;
- repo-target prompts contain the required fresh-authority instruction class where applicable;
- tests distinguish self-review judgement from independent evidence;
- generated prompt cannot set admission/priority/current state.

This is behavior regression, not proof that every generated prompt is high quality.

## 4. Seeded failure fixtures

Before implementation acceptance, tests must include intentionally broken fixtures.

Minimum fixture families:

1. **stale current:** superseded design referenced as current;
2. **latest-wins trap:** newer dated proposal must not become current;
3. **orphan finding:** material finding exists with no disposition;
4. **coverage loophole:** coverage source marked complete while one declared material item is absent;
5. **broken stable reference:** artifact moved and path-only reference breaks while ID route should survive;
6. **missing transition authority:** baseline change with no admissible decision/result evidence;
7. **stale generated view:** canonical input changes without derived output update;
8. **local-PASS trap:** implementation technical checks pass while parent whole-return says unresolved;
9. **context starvation:** compact packet omits a required authority/uncertainty item and adversarial test rejects it;
10. **false relation:** plausible but unsupported relation must not be promoted to accepted;
11. **no-change result:** successful work can close without synthetic baseline mutation;
12. **concurrent investigations:** two proposals coexist without recency selecting one;
13. **tiny routine change:** system does not require full material-change ceremony when D-016 is genuinely not applicable;
14. **exact-head:** final qualification is tied to the actual PR/main head under review.

## 5. One local assurance entrypoint

Target developer contract after implementation:

```bash
python tools/check.py
```

or an equivalent single repository-local command.

It should invoke the current checks plus admitted engineering checks. CI calls the same command or a thin wrapper around it.

Current CI behavior remains the interim source of truth until such a command is admitted and implemented.

A one-command entrypoint does not mean one monolithic checker module internally. It is a developer interface.

## 6. Local result → whole-system return contract

Every material bounded work result must explicitly reconcile to the owning whole. The Result/Issue return has five required questions:

```text
1. What changed in actual/canonical state?
2. Which Findings changed disposition?
3. Which Requirements / accepted or proposed ADRs changed consequence?
4. Which parent dependencies/readiness changed?
5. Did the remaining whole-system gap shrink, remain, or expose a new material decision?
```

Optional but usually useful:

- what can now leave default context;
- what new evidence/uncertainty appeared;
- what must be invalidated/re-entered;
- what remains explicitly unchanged.

A material result may return `no whole-system change` with rationale. It must not be forced to claim progress.

## 7. Closure semantics

### 7.1 Local completion

A child Issue is locally complete when its own acceptance/verification/validation contract is satisfied and its whole-system return is recorded.

### 7.2 Parent/programme closure

The parent closes only when its own acceptance owner reconciles all material children/residuals. Child closure does not auto-close the parent.

### 7.3 Technical PASS

Technical PASS says only that checked formal/deterministic properties passed at the referenced head.

### 7.4 F17 residual

Nothing in this engineering fitness set proves the historical #225 positive real scholarly vertical acceptance contract. That remains explicit evidence/status work and must not be manufactured by running engineering fixtures.

## 8. Exact-head / post-mutation assurance

For consequential repo change:

1. checks run on the PR head actually proposed for merge;
2. merge uses the expected head where supported;
3. after merge, read back `main` exact SHA;
4. require a post-merge run on that exact SHA when the repository workflow provides it;
5. report what that run establishes and what it does not.

A stale successful run is evidence for the stale SHA only.

## 9. Human-readable CI boundary

The current workflow's explicit assurance summary is retained as a strong pattern. Future engineering checks must extend, not weaken, that clarity.

A passing engineering workflow should say in substance:

```text
PASS establishes structural/deterministic consistency for the contracts checked.
It does not establish scholarly truth, specialist validity, Human material acceptance,
independent evidential review, or whole-system closure beyond explicit parent reconciliation.
```

## 10. Readiness disposition

**#250 design is complete.**

The deterministic properties, seeded failures, one-command developer interface and local→whole reconciliation semantics are now sufficiently specified for implementation planning. Actual CI/tool implementation remains downstream of admitted #245/#246/#247/#251 representations and D-016.