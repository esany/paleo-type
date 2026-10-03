# Product / co-development boundary analysis delta — 2026-10-03

**Status:** NON-NORMATIVE PRODUCT / CO-DEVELOPMENT BOUNDARY ANALYSIS — PROVISIONAL / EVIDENCE-SEEKING  
**Repository baseline:** `main@7eeb490e0644e5e445580e48ba782aa306a1f239`  
**Related evidence:** `requirements/repository-target-state-implementation-readiness-2026-10-03.md`; `requirements/repository-knowledge-lifecycle-d016-decision-surface-2026-10-02.md`  
**This artifact is not:** METHOD, a D-016 admission, a Project scope or manuscript `NEXT ACTION`, a productization decision, a package/refactor authorization, a claim that #225 acceptance criteria are satisfied, or authority to implement a lifecycle revision.

## Purpose

Persist a material analysis delta before deeper falsification so that the current product/development-boundary correction does not remain dependent on the originating chat. The statements below are hypotheses to be tested in a separate focused deep check. Persistence here does not promote them to canonical METHOD or accepted architecture.

## DELTA-01 — Product-boundary correction

Working hypothesis:

> `paleo-type` is not commissioned as a clone-and-go repository template or distributable software/framework product. Its governing product remains scholarly result and source understanding; software, AI, automation, repository structures and presentation remain supporting infrastructure.

The existing target-state phrase `research-system development workspace with live reference research instances and reusable framework-like METHOD/contracts/tools` may therefore be directionally useful about reuse while still creating an avoidable product-metaphor risk if `framework-like` is read as the development objective rather than a property of supporting layers.

This hypothesis must be tested against repository history and Human-Owner-grounded state rather than accepted from wording alone.

## DELTA-02 — Co-development hypothesis

Working hypothesis:

Concrete scholarship and generic research-system development intentionally co-evolve rather than forming a one-way `framework first -> later consumers` sequence:

```text
real scholarly use
→ demonstrated need / failure
→ Project-local understanding or correction
→ Generic-Fit question
→ generic METHOD / system / tooling candidate where warranted
→ D-016 admission where material
→ implementation / assurance
→ renewed real scholarly use and falsification
→ broader materially different validation where genericity is claimed
```

This is a candidate explanatory/development model, not a mandatory pipeline. Phase B must test whether repository genealogy actually supports it and whether another model explains the evidence better.

## DELTA-03 — Current research artifacts are first real examples, not the system boundary

The current Reg. Ii 3 / Reg. Ii 4 Bd. II / Reg. Ii 5 Projects, their source material, research artifacts, fixture scripts and regressions are to be treated as:

- real scholarly work;
- real-use evidence;
- first reference/falsification fixtures;
- sources of demonstrated needs and counterexamples.

They are not automatically:

- a complete typology of future research;
- the outer boundary of generic METHOD or system architecture;
- a consumer API;
- sufficient Generic-Fit evidence;
- a blueprint that future Projects must reproduce.

A single case may falsify a generic assumption without defining the whole replacement architecture.

## DELTA-04 — Genericity is not distribution

Working hypothesis:

Genericity is important primarily to prevent pilot overfitting, preserve cross-investigation validity and allow materially different future historical-source research to use/falsify shared METHOD and system capabilities. That requirement does not by itself imply:

- a GitHub Template repository;
- an external software consumer;
- a package distribution contract;
- SemVer or GitHub Releases;
- repository splitting.

Distribution/productization remains a separate future requirement that needs a demonstrated consumer/compatibility need or explicit Human product decision.

## DELTA-05 — Wirknetz is a property/trace hypothesis, not a preselected component

Current comparator evidence from `esany/Wissensarbeit` suggests that the relevant `Wirknetz` semantics may concern relations such as:

```text
Intent
→ Gap / Need / Pain / Goal
→ Requirement / Requirement Candidate
→ Constraint / safeguard
→ Acceptance / Verification / Validation
→ Feedback / correction / supersession
```

plus source role, uncertainty, chronology and relation correctness.

Phase B must establish what `Wirknetz` currently is in `Wissensarbeit` and test whether paleo-type should reuse:

- principles/properties;
- an analytical/qualification lens;
- implementation;
- or nothing material.

No new `Wirknetz` Skill, graph store, ontology, Bridge or runtime candidate is created by this artifact.

## DELTA-06 — `src` / package threshold is broader than external distribution

Working hypothesis:

A Python package or `src/` boundary can become justified without an external software product if generic executable research-system logic develops a stable internal module/API boundary consumed by multiple CLIs, tests or derived views and the current script namespace causes import, test-isolation, cohesion or fixture-separation problems.

This does not establish that the threshold has been reached. Phase B must inspect the actual import/dependency/responsibility graph before dispositioning the current IC-10 conclusion.

## DELTA-07 — Decision-surface consequence remains open

Before any D-016 lifecycle-revision admission, the existing target-state and D-016 decision surface should be tested for whether they correctly preserve:

- scholarly-product primacy;
- Genericity ≠ Distribution;
- current research artifacts as first real fixtures rather than system limits;
- co-development between scholarship and system support where evidence carries it;
- Wirknetz-like provenance/relation/supersession properties without inventing a component;
- an internal-runtime trigger for future package boundaries.

Possible later dispositions remain:

1. current target state already sufficient;
2. target state / decision surface need bounded refinement while the Class-B architecture remains unchanged;
3. a material architecture assumption is falsified and a revised D-016 surface is required.

No outcome is selected here.

## Fresh-state anomaly requiring Phase-B treatment

Fresh repository inspection at this baseline found that GitHub Issue #225 is now **closed as work metadata** (closed 2026-10-02), while `README.md` still describes it as currently open. This artifact does **not** infer from closure that #225's whole-system scholarly acceptance criteria were met. Phase B must distinguish:

- work-owner state (`closed`);
- any durable terminal/acceptance disposition actually supported by evidence;
- stale navigation prose;
- consequences for the lifecycle/current-history analysis.

The mismatch is itself relevant evidence for currentness/closure analysis but not permission to rewrite #225's historical meaning.

## Phase-B falsification questions

The focused deep check must answer four questions before this delta can affect target-state/D-016 semantics:

1. **Co-development genealogy:** is the proposed co-development model actually borne out by the repository's sequence of real scholarly work, Project-local corrections, Generic-Fit and generic system changes?
2. **Wirknetz transfer:** which current `Wissensarbeit` Wirknetz properties are supported, transferable and already covered by paleo-type candidates, and which are not?
3. **Fixture independence:** which generic paleo-type contracts/tools genuinely remain independent of the current visitation examples, and where does pilot-family form still leak into generic semantics or testing?
4. **Runtime/package threshold:** do the generic Python tools already constitute an internal library-like core, and is there any demonstrated failure that justifies a package/`src` migration now?

## Phase-A restartability check

A fresh maintainer should be able to recover from this file alone that:

- the product/framework interpretation is being challenged, not yet canonically changed;
- current research artifacts are deliberately treated as first real examples rather than the system boundary;
- Genericity and Distribution are separated as hypotheses;
- Wirknetz is under comparative property-level evaluation, not selected as a component;
- `src` is under a technical threshold test, not scheduled;
- #225's closed work-state versus acceptance meaning is unresolved and must not be inferred;
- Phase B must complete before target-state/D-016 refinement or implementation admission.
