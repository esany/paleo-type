# Review Premise Inheritance — targeted Generic-Fit / safeguard disposition — 2026-10-04

**Status:** NON-NORMATIVE TARGETED ANALYSIS / **#253 ANALYSIS COMPLETE — NO SEPARATE RUNTIME OR EKCP OWNER REQUIRED**  
**Baseline:** `main@b633ac81f65952775d2d203b7b9986903d48365b`  
**Work owner:** #253; parent visibility #244  
**Failure:** F10 Review Premise Inheritance  
**This file is not:** independent scholarly validation, a change to manuscript truth, a new Project scope, or D-016 implementation admission.

## 1. Frozen demonstrated failure

The 2026-09 Pilot #171 provides a strong real fixture.

The first review context did fresh repository rehydration and produced a useful challenge, but still inherited a derived statement that #165 had `restored the cross-folio unit`. A later pass descended further to the primary G2 physical-structure owner and the Reg. Ii 4 folio-local unit evidence. That showed the cross-witness correspondence range with `resegmentation` did not establish one Reg. Ii 5 source/text unit. The derived premise had propagated through #165/PR #167 and into #166's question framing.

The material lesson is:

> **fresh context is not an independent evidence basis; independence depends on what evidence/premises are actually re-examined.**

This is not primarily a transport or EKCP failure.

## 2. Existing mechanisms already support the core epistemic rule

Current repository authority already establishes most of the needed meaning:

- model output / model agreement is not independent historical evidence;
- qualified review must be traceable to exact source evidence at appropriate depth;
- observation/reading/normalization/identification/interpretation must not collapse;
- derived/generated views are not canonical truth;
- uncertainty and competing readings remain valid;
- consequential review/validation is distinct from technical PASS;
- source/witness comparison must not overwrite one witness with another.

Therefore F10 does **not** justify a new global provenance ontology, review service, duplicate scholarly workflow, `independent=true` flag, or separate Review Bridge.

The demonstrated problem is operational: a reviewer can be correctly told to `freshly rehydrate` yet still begin below the contested premise.

## 3. Competing safeguards

### Option A — fresh context / second model only

**Reject.** Reproduces the failure. A second context can consume the same derived owners/premises.

### Option B — always repeat all primary scholarship from scratch

**Reject as default.** It would duplicate expensive work, relocate burden and make review impractical. Independent review depth should follow consequence and the contested premise.

### Option C — global provenance ontology / evidence graph

**Reject for current need.** Better trace can help locate evidence but cannot determine epistemic independence merely from graph structure. It adds architecture without evidence of necessity.

### Option D — review-evidence-basis contract + contested-premise descent

**SELECT.** For consequential review, explicitly state what level of evidence the review actually re-examined and which material premises are inherited vs re-tested. Descend to a stronger/primary owner when the challenged claim depends on a contested derived premise.

This is a small semantic/interaction safeguard compatible with existing quality/evidence rules.

## 4. Review-evidence-basis contract

For a consequential review, the review packet/result should make these meanings explicit when applicable:

```text
review target
material claim/premise under review
basis actually inspected
inherited premises
premises re-tested
independence claim, if any
unresolved evidence-depth limitation
```

Useful descriptive basis classes:

- **direct-source-inspection** — reviewer actually inspected the relevant source evidence;
- **primary-owner-reinspection** — reviewer re-read the strongest current evidence/owner supporting the premise, without necessarily inspecting raw source bytes;
- **same-evidence-rejudgement** — reviewer independently reasons over substantially the same evidence set;
- **derived-owner-review** — reviewer evaluates a derived synthesis/result without descending to primary support;
- **independent-external-support** — materially independent evidence/source supports/challenges the premise;
- **unknown / not established** — independence/evidence depth cannot be claimed.

These are analysis semantics, not automatically a mandatory repository enum. Only formalize values that prove useful across real review fixtures.

## 5. Contested-premise descent rule

When a review materially challenges or validates a claim whose correctness depends on a derived premise:

1. identify the premise;
2. locate its strongest current support/owner through trace/provenance;
3. determine whether the current review actually inspects that support or merely inherits it;
4. if the premise is itself the point at issue, descend one or more levels until the review reaches evidence capable of testing it;
5. state any remaining inherited premise explicitly;
6. do not call the result independent beyond the actual evidence basis.

This is consequence-driven. It does not require raw-source reinspection for every routine review.

## 6. How this interacts with EKCP

EKCP can **support** this safeguard by providing:

- stable backward trace from current claim/design/finding to source/evidence owners;
- explicit derived-vs-canonical/accepted lifecycle;
- review/context packets capable of naming evidence basis;
- expandable provenance on demand.

EKCP cannot establish:

- that a reviewer actually looked deeply enough;
- specialist competence;
- evidential independence merely because a relation exists;
- scholarly correctness.

Therefore:

> **F10 constrains context/review semantics but does not add a new EKCP service, database, graph runtime or canonical review owner.**

## 7. Generic-Fit against materially different review situations

### Fixture 1 — Reg. Ii 5 structural premise (#171)

A derived `cross-folio unit` premise is challenged. The safeguard requires premise descent to G2/source-structure/current direct owners rather than review of later synthesis only. **Useful / necessary.**

### Fixture 2 — software architecture review

Reviewer challenges `central TSV is necessary`. Direct manuscript source evidence is irrelevant. The primary evidence is failure/Requirement/trade-study evidence. The same contract says whether the reviewer inspected those inputs or merely the selected design. **Transfers cleanly.**

### Fixture 3 — deterministic CI result

CI reruns the same tests at exact head. It can provide independent execution in a technical sense, but not independent scholarly judgement. The basis class/assurance boundary makes that distinction explicit. **Transfers cleanly.**

### Fixture 4 — specialist validation

A qualified palaeographer re-examines the manuscript crop/source image. This can be direct-source review by a separate specialist. The contract records actual basis; it does not infer competence from metadata. **Transfers cleanly.**

### Fixture 5 — second AI summarizes same canonical synthesis

No new evidence basis. Label as derived-owner/same-evidence review; do not call independent. **Prevents false independence.**

The property is therefore generic enough to preserve as a review/context requirement, while the exact basis vocabulary should remain proportional rather than become an ontology.

## 8. Where the safeguard should live

### Accepted current rule

Core epistemic meaning already belongs to GO/AGENTS/evidence/quality owners. No new top-level METHOD family is required by this result.

### Operationalization

Future context/review tooling should support a `review evidence basis / inherited premise` section for consequential review profiles. The architecture-review and specialist-review profiles from #247 should expose it where material.

### Tests

Deterministic tests can verify that a declared review packet carries required basis/provenance fields. They cannot verify the substantive truth of a Human/AI claim that evidence was competently inspected.

Adversarial evaluation should include the original #171 pattern: a fresh reviewer reads only derived owners and must not be labeled independent.

## 9. Disposition

**EXISTING MEANING SUFFICIENT; OPERATIONAL REVIEW-BASIS SURFACE NEEDED.**

Consequences:

- no separate EKCP subsystem;
- no new workflow engine/Bridge/graph;
- no Project-specific change from this analysis;
- no independent-validation claim;
- #247 review-context design gains an evidence-basis/inherited-premise requirement;
- #250 assurance fixtures preserve `fresh context != independent evidence`;
- F10 remains visible as a validation/usage risk until real review-context implementation is exercised, but it no longer blocks the architecture class with an undefined solution question.

## 10. Readiness disposition

**#253 targeted design question is resolved at the present evidence state.**

If later real use shows that the lightweight review-basis contract cannot prevent premise inheritance, reopen Generic-Fit from that failure rather than pre-building a richer review infrastructure now.