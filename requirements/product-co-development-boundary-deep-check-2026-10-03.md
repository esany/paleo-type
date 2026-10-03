# Product / co-development boundary deep check — 2026-10-03

**Status:** NON-NORMATIVE DEEP CHECK / TARGET-STATE REFINEMENT EVIDENCE — NO D-016 ADMISSION  
**Paleo-type baseline:** `main@7eeb490e0644e5e445580e48ba782aa306a1f239`  
**Comparator baseline:** `esany/Wissensarbeit@b448915cf774c573dbf82cf2e17bcb03c10a9ed8`  
**Phase-A hypothesis anchor:** `requirements/product-co-development-boundary-analysis-delta-2026-10-03.md`  
**Refines interpretation of:** `requirements/repository-target-state-implementation-readiness-2026-10-03.md` and `requirements/repository-knowledge-lifecycle-d016-decision-surface-2026-10-02.md`  
**This artifact is not:** METHOD, Project scholarly state, a manuscript `NEXT ACTION`, a D-016 implementation admission, a productization decision, a package/refactor authorization, or proof that historical #225 acceptance criteria were satisfied.

## 1. Executive disposition

The focused deep check returns **RESULT B — TARGET STATE NEEDS BOUNDED REFINEMENT; CORE ARCHITECTURE CLASS UNCHANGED**.

The material findings are:

1. **Clone-and-go/template/productization is not the paleo-type development objective.** The Governing Objective makes scholarly result/source understanding the product and treats software/AI/automation/GitHub/presentation as replaceable support infrastructure. Reuse and genericity remain important, but they are not evidence of a distributable framework product.
2. **The co-development hypothesis is supported, with refinement.** Repository history repeatedly shows a cycle in which real scholarship exposes a local problem; the local result is preserved at Project level; only a genuinely reusable safeguard is promoted through Generic-Fit/D-016 as applicable; the system then returns to scholarship. This is a strong explanatory model, but it must not become a mandatory fixed pipeline.
3. **Current research artifacts are first real examples and falsification fixtures, not the system boundary.** This is not merely a new interpretation: current METHOD and #225 explicitly prohibit pilot-specific structures from defining generic architecture and require portability beyond Reg. Ii 5 / materially different source structures.
4. **`Wirknetz` should not be added as a new runtime/Skill/graph candidate.** In current `Wissensarbeit`, the relevant Wirknetz work is a provenance-aware reconstruction/trace method and semantic lens. Its strongest reusable properties map into existing paleo-type lifecycle/currentness/provenance candidates. `Wissensarbeit` #76 independently falsified the necessity of a separate Wirknetz↔Skill Bridge for its tested cases.
5. **The generic executable layer is already a small internal library-like core, but the `src/` threshold has not been reached.** `source_contract`, `source_intake`, `project_context` and `outcome_context` form a real dependency chain, yet current execution and tests remain stable as repo-local scripts and no import/test/distribution failure is demonstrated. IC-10 should therefore be refined from a distribution-centric rationale to an explicit internal-runtime threshold, while remaining `NOT WARRANTED NOW`.
6. **Fixture independence is structurally better than physical co-location suggests, but Generic Fit remains incompletely demonstrated.** Generic tools are parameterized and Project-specific scripts are visibly bounded. Remaining concerns are untested portability across materially different source structures, a few current-contract assumptions (for example mandatory archive/fonds/signature fields for every canonical Source), and prose-pattern coupling in `outcome_context.py`.
7. **#225 now exposes a live current/history/closure example.** GitHub records #225 as closed on 2026-10-02, while its issue body still says `ACTIVE` and the current README says it is open. The inspected #225 contract states that closure requires full vertical/restart/repair/materially-different-fixture evidence. No terminal comment establishing that T11 acceptance was found in the current issue-comment set. Therefore work-owner state is `closed`, but this pass does not infer whole-system scholarly acceptance from closure alone.

The existing Class-B lifecycle direction remains the best-supported material architecture class. This deep check sharpens its product boundary and qualification semantics; it does not establish a new architecture class and does not admit implementation.

---

## 2. Authority and evidence boundary

Fresh paleo-type authority/state inspected for this pass included:

- `GOVERNING_OBJECTIVE.md`;
- `AGENTS.md`;
- `README.md`;
- `DECISIONS.md`;
- `MILESTONES.md`;
- `methodology/maintenance.md`;
- `methodology/workflow.md`;
- `methodology/quality-and-learning.md`;
- `methodology/project-lifecycle.md`;
- `methodology/historical-source-workflow.md`;
- `methodology/source-and-provenance.md`;
- current Project `project.yml` / `STATUS.md` owners;
- #165, #166, #169, #206, #225, #230;
- the current target-state and D-016 decision-surface artifacts;
- `corpus/source-contract.json`;
- current tools, tests and CI.

Fresh `Wissensarbeit` comparator state included:

- `project/GOVERNING_OBJECTIVE.md`;
- `project/CURRENT_STATE.md`;
- #52 Skill-system candidate;
- #53 Intent/Gap Semantic Fidelity candidate;
- #56, #58, #60, #61 Wirknetz reconstruction/disposition work;
- #76 Wirknetz↔Skill handoff discrimination and its final independent-review disposition;
- current `skills/README.md`.

`Wissensarbeit` is comparative evidence only. It does not own paleo-type semantics.

---

## 3. B1 — Co-development genealogy

### 3.1 The model is already present as distributed semantics

The repository does not currently have one canonical statement literally named `co-development model`. Nevertheless the governing owners establish its component rules:

- the scholarly result/source understanding is the product;
- no current pilot or technical architecture is universally sufficient;
- software is support infrastructure;
- a Project/pilot finding remains local by default;
- Generic-Fit precedes generic promotion;
- material shared-system changes use D-016;
- maintenance propagates only actual changed consequences and returns to research;
- a single case can falsify a generic assumption without defining the whole replacement architecture;
- Project-specific evidence may expose a METHOD weakness, but pilot form does not become METHOD by example.

The authoritative historical-source workflow already asks the generalisation question in counterfactual form: would the statement remain a valid requirement if the next Project used a different early-modern manuscript/source group?

### 3.2 Concrete genealogy: scholarship can correct itself without system promotion

#165 is a strong negative-control case. A previous correction over-grouped two observed Reg. Ii 5 blocks because a larger cross-witness correspondence range had been promoted into a source/text unit. The bounded reconciliation restored the distinction among direct observation blocks, comparison range and open analysis question. The Issue explicitly classifies this as **Project-specific correction** and states that no new METHOD/REQ/gate/schema family is required.

#166 then performed the real source work and established two distinct adjacent rules plus a bounded evidence ceiling. Its terminal result explicitly made no diplomatic TSV, METHOD/REQ/schema/tooling, HTR/OCR or automatic-next-scope change.

These two cases show that real scholarly evidence can refine the local system state without automatically generating generic system architecture.

### 3.3 Concrete genealogy: scholarship can expose a genuinely generic system failure

#169 is the strongest positive co-development case found in this pass. It states that a systemic failure was **exposed by #166**:

```text
observed resource unavailability
→ inferred task prerequisite consequence
→ REAL BLOCKER
→ STOP / NEXT ACTION / roadmap dependency
```

The correction then promoted only the reusable safeguard — `Resource state is descriptive, not task authority` — into existing generic owners (`AGENTS.md`, workflow/source-provenance semantics, regressions), while correcting affected Project state and explicitly avoiding a new gate, schema, role, workflow engine or substitute research scope.

This is direct evidence for:

```text
real scholarship
→ concrete system failure
→ bounded local diagnosis
→ generic-fit/general safeguard
→ shared-system correction
→ regression
→ return/no invented research priority
```

### 3.4 Wider system programmes preserve the same boundary

The 2026-09-14 problem landscape explicitly warns that Knau/visitation structures may serve as fixtures but must not become universal architecture and that analogous failure classes must be established locally in another Project/repository before being imported. Its C4 construction site labels generic-vs-Project-specific separation as a standing constraint, with portability across very different source types not yet broadly demonstrated.

#206 shows another important property: a system programme can terminate without creating a permanent meta-programme or automatic successor. Future system work needs its own trigger or Human-Owner selection.

#225 then made the relation even more explicit. Its own body says:

> `The Reg. Ii 5 history is evidence/fixture only. The solution must survive after that pilot disappears.`

It also requires genericity across materially different manuscripts/source structures and vertical acceptance rather than component-only success.

### 3.5 Disposition of the four co-development hypotheses

| Hypothesis | Disposition | Basis |
|---|---|---|
| C1 — co-development is already an implicit repository model | **SUPPORTED** | governing product boundary + Generic-Fit + #165/#166/#169 + #225 |
| C2 — it is only a retrospective AI synthesis | **FALSIFIED as a total explanation** | the constituent rules and concrete cycles pre-exist this analysis |
| C3 — repository history includes framework/system-first pressure at times | **PARTLY SUPPORTED** | audits document support dominance, artifact topology and local-system optimization; however current canonical rules repeatedly correct that pressure rather than making it the governing product model |
| C4 — another model explains the evidence better | **NO STRONGER ALTERNATIVE FOUND** | `METHOD + executable support + live scholarly Projects` and `co-evolving scholarly research system` are compatible; the latter better explains the feedback loop, while neither implies a distributable framework product |

### 3.6 Refined co-development model

The best-supported model is therefore:

```text
owner-authorized scholarly purpose / question
        ↓
real source work and source-constrained result
        ↓
local success, ceiling or demonstrated failure
        ↓
Project-local persistence first
        ↓
Generic-Fit only for genuinely recurring/shared semantics
        ↓
D-016 when the shared research system materially changes
        ↓
METHOD / contract / tooling change only as warranted
        ↓
re-use and falsification in real scholarship
        ↓
materially different evidence before strong Generic-Fit claims
```

This is an **event-driven feedback model**, not a fixed lifecycle pipeline. Ordinary research does not require a generic system-change pass, and every system change does not require an immediate new scholarly Project merely for ceremony.

---

## 4. Product/development model comparison

| Model | Fit | Disposition |
|---|---|---|
| M1 — framework + consumers | useful as a limited technical analogy, but implies a stronger product/consumer boundary than current evidence carries | **REJECT as governing model** |
| M2 — clone/template product | no Human-Owner or GO basis; no compatibility/distribution contract | **REJECT** |
| M3 — monorepo research system + live scholarly applications | matches current physical/repository organization well | **SUPPORTED structural description** |
| M4 — METHOD + executable support + concrete Projects | closely matches existing owners and README layers | **SUPPORTED architectural description** |
| M5 — co-evolving scholarly research system | best explains why live research, Generic-Fit, learning and system development interact | **SUPPORTED development model** |

### Target formulation

A more accurate target description than `framework-like workspace` is:

> **`paleo-type` is a co-evolving scholarly research system for evidence-constrained historical-source research. Generic METHOD and executable support exist to make high-quality scholarship reliable, auditable and reusable across materially different investigations; concrete research is simultaneously product work, real-use evidence and a falsification source. Current Projects are first real instances, not the limit of intended application.**

This formulation does not amend the Governing Objective; it is a lower-level architecture/development interpretation of it.

---

## 5. B2 — `Wissensarbeit` / Wirknetz reconstruction

### 5.1 Product identity must not be copied

`Wissensarbeit` has a different product boundary: it is explicitly a Git-native project-operation/reference/template effort for transdisciplinary knowledge/concept work. Its architecture may therefore legitimately optimize for a future generic project template in ways that paleo-type does not need.

Its transferable value is in tested semantics and failure handling, not its product identity.

### 5.2 What Wirknetz currently is

Fresh current evidence does **not** show a Skill named `Wirknetz` under `skills/`; current skill candidates listed there are `prompt/` and `failure-pattern-check/`.

The Histo-Orla RECON work instead uses Wirknetz as a provenance-aware reconstruction/trace figure:

```text
source / origin class / statement
→ Intent
→ Gap
→ Need / Pain / Goal
→ Requirement / Requirement Candidate
→ Constraint / safeguard
→ Acceptance / Verification / Validation
→ Feedback / correction / supersession
→ current uncertainty / non-conclusion
```

#58 explicitly says its matrix is an **Arbeitsmittel, kein Datenmodell, keine Ontologie und kein neues System**. #56/#60 prohibit solution-building and automatic promotion. #61 dispositions concepts by evidenced Wirknetz function rather than by current usefulness intuition.

Therefore the current best classification is:

> **analytical reconstruction / semantic trace method with provenance, chronology and uncertainty discipline**

—not a canonical graph store, runtime, Skill, ontology or universal project-state model.

### 5.3 Relation to the modular Skill model

#52 is itself still a candidate (`no runtime / no Building-Block promotion / generic fit unproven`). Its useful cross-cutting principles include:

- state != operator;
- state-/event-driven rather than fixed pipeline;
- small interfaces;
- authority external to capability;
- generalize without flattening;
- growth only from observed necessity;
- trace correctness > trace completeness;
- storage neutrality;
- verification != validation;
- materially different project types before Generic-Fit.

#53 adds the semantic-fidelity distinctions:

- primary statement ≠ paraphrase ≠ inference ≠ confirmed meaning;
- `latest wins` prohibited;
- refine/generalize/extend/supersede/conflict are distinct;
- semantic shift and false traceability are first-class failures;
- candidate relations remain unresolved when evidence is insufficient.

### 5.4 The decisive Track-B result

#76 directly tested whether the Wirknetz↔Skill boundary justified a distinct Bridge/Interface capability. The final independent review returned:

`EXISTING MECHANISMS SUFFICIENT`

It specifically falsified the writer's stronger necessity claim for contract sharpening on the frozen cases and found no support for a separate Bridge Skill/Capability/Building Block. It also kept operational/runtime maturity separate from semantic sufficiency.

This is important negative evidence against inventing a paleo-type `Wirknetz` runtime merely because the conceptual relation network is useful.

### 5.5 Wirknetz transfer matrix

| Property | Wissensarbeit role | Paleo-type analogue / need | Disposition |
|---|---|---|---|
| primary source / origin class | protects Human/source meaning | Source/File/evidence provenance + Human authority | **REUSABLE WITH DOMAIN REFINEMENT** |
| Intent / Goal | reconstructs what is sought | GO / Project purpose / Human need | **ALREADY PARTLY PRESENT** |
| typed Gap | prevents generic `missing` flattening | scholarly/evidence/capability/authority gaps have different closure modes | **REUSABLE PRINCIPLE** |
| Requirement vs Candidate | prevents premature promotion | D-016 / requirements / audit candidate boundary | **ALREADY PRESENT** |
| Constraint / safeguard | records intended protection | METHOD/DECISIONS/guardrails | **REUSABLE ANALYTICAL LENS** |
| Verification vs Validation | separates formal behavior from Human/domain success | quality-and-learning / specialist validation | **ALREADY PRESENT** |
| feedback / correction / supersession | preserves change genealogy | IC-01/02 current/history/closure semantics | **STRONGLY RELEVANT** |
| uncertainty / non-conclusion | prevents false completion | core paleo-type epistemic invariant | **ALREADY STRONGER LOCALLY** |
| relation correctness > completeness | prevents plausible graph fabrication | IC-03/07 and provenance qualification | **REUSABLE PRINCIPLE** |
| `latest wins` prohibition | preserves cumulative meaning | current/history/supersession | **REUSABLE PRINCIPLE** |
| graph/database runtime | not implied | no demonstrated paleo-type need | **NOT SUPPORTED** |
| separate Wirknetz↔operator Bridge | independently falsified as necessary in Track B cases | existing owners/composition should be tried first | **DO NOT ADD** |

### 5.6 Transfer conclusion

Disposition:

- **1:1 semantic/runtime reuse:** REJECTED;
- **property-set reuse:** SUPPORTED;
- **implementation reuse:** NOT SUPPORTED by current evidence;
- **architecture/qualification lens:** SUPPORTED;
- **new implementation candidate:** NOT NEEDED.

The strongest mapping is to IC-01/02/03/07 rather than a new IC.

---

## 6. B3 — Fixture-independence / system-boundary audit

### 6.1 Productive generic boundaries already exist

The current generic METHOD explicitly separates METHOD, CORPUS and PROJECT and uses a counterfactual generalisation test against a different future manuscript/source group.

`source-and-provenance.md` deliberately avoids a fixed Source hierarchy: holding context, act, record, protocol, section, attachment, witness and locus may be represented recursively through generic Source nodes and `part_of`; intermediate nodes exist only when identity/provenance/citation/research requires them.

The executable contract similarly keeps Project source `research_function` vocabulary open: `source_contract.py` checks lower-case kebab-case form rather than a closed Reg.-Ii.-specific function enumeration.

`project_context.py` is parameterized by arbitrary Project ID and resolves established owners rather than hard-coding Reg. Ii semantics.

`source_intake.py` resolves exact File/Source facts and leaves Project routing/authority open.

`outcome_context.py` is also Project-parametric and explicitly refuses to manufacture Project/outcome authority.

These are strong signs that the semantic core is not merely Reg.-Ii.-5 code with generic names.

### 6.2 Project-specific tools are visibly bounded rather than silently generic

`regii5_evidence_packet.py` explicitly identifies itself as a **project-bounded prototype**, hard-codes its Reg. Ii 5 Project/use/reading paths and states that it is not a canonical owner or replacement for `project_context.py`. It imports generic `source_contract` support rather than exporting its Reg. Ii 5 assumptions into the generic contract.

This is a good example of **PRODUCTIVE CO-LOCATION / INTENTIONAL REFERENCE FIXTURE**, not a boundary leak by itself.

The test/CI layout similarly combines generic contract/governance/context regressions with concrete Reg.-Ii. fixtures. Real-data fixtures are valuable because they can falsify generic code against actual repository state; they become a problem only if their shape is mistaken for generic sufficiency.

### 6.3 Demonstrated or plausible boundary weaknesses

#### F-01 — current fixture-family breadth is narrow

The current live scholarly Projects are all related early-modern archival visitation material. #225 itself required materially different source/problem fixtures for strong genericity claims. The current repository therefore has **real-use evidence but incomplete broad Generic-Fit evidence**.

Disposition: `UNTESTED GENERICITY`, not `PILOT OVERFIT` by default.

#### F-02 — mandatory archival provenance columns may be narrower than the top-level purpose

`corpus/source-contract.json` currently requires `archive`, `fonds` and `signature` to be non-empty for every canonical Source. Current Source methodology strongly privileges provenance-derived archival identity, which is appropriate for the present corpus. The Governing Objective, however, is phrased more broadly as early-modern historical sources, especially handwritten manuscript material.

No current failure demonstrates that these fields are wrong. But a future materially different historical source with a legitimate non-archival/private/edition/other provenance pattern would test whether the executable contract has encoded the current archival family more strongly than METHOD intends.

Disposition: **UNTESTED GENERICITY / FUTURE-FIXTURE TRIGGER**, not a current schema change.

#### F-03 — crosswalk vocabulary is archival-folio-shaped, but crosswalk use is optional

The crosswalk contract requires `archival_folio` when a crosswalk exists. That is natural for current manuscript work and does not force every Source to have a crosswalk. A future paginated/unfoliated/non-image source could test whether the generic locator contract should remain this specific or use another source-specific mapping owner.

Disposition: **UNTESTED GENERICITY**, no migration now.

#### F-04 — hidden textual API in `outcome_context.py`

`outcome_context.py` detects explicit absence of authorized outcome by scanning owner prose for the phrase `no owner-selected` plus one of `scope`, `task`, `target`, `action`.

This is a real coupling to current Human-readable wording. It is conservative and currently safe because lack of a match never becomes positive authority, but it is a **hidden textual interface**. If lifecycle/current-state semantics become more structured under a future admitted revision, this should be revisited rather than expanded by adding more phrases.

Disposition: **REAL BOUNDARY FRAGILITY / DESIGN INPUT FOR IC-01/03**, not a standalone implementation task.

### 6.4 Future-fixture thought tests

Without inventing a new Project, the current generic core was challenged conceptually against materially different shapes:

- Source hierarchy without act→record visitation structure;
- unfoliated or differently paginated historical material;
- multiple independent Source families in one Project;
- text/image/table evidence with different locators;
- Project research functions beyond `principal`/`comparison`/`context`;
- different specialist triggers and maturity paths.

The recursive Source relation model, open Project-relative `research_function`, explicit evidence ownership and Project-parametric tools survive most of these thought tests. The strongest unresolved assumptions are the mandatory archival identity columns and folio-specific optional crosswalk contract. These require a real future fixture before changing the schema.

### 6.5 Mixing classification

Current physical co-location should be classified as:

- generic tools + concrete fixture tools under `tools/`: **PRODUCTIVE CO-LOCATION**;
- generic tests + Reg.-Ii. real-data regressions: **INTENTIONAL REFERENCE FIXTURE**;
- generic tools importing Reg.-Ii. scripts: **NOT OBSERVED**;
- Reg.-Ii. script importing generic contract: **EXPECTED DEPENDENCY**;
- generic METHOD universalizing Knau/visitation semantics: **PROHIBITED BY CURRENT METHOD; no current direct example found in the inspected boundaries**;
- broad Generic-Fit across materially different source types: **NOT YET DEMONSTRATED**.

---

## 7. B4 — Runtime / package / `src` threshold

### 7.1 Current dependency graph

The generic Python layer is no longer a set of wholly independent scripts:

```text
source_contract
   ↑          ↑
source_intake │
   ↑          │
project_context
   ↑
outcome_context
```

More exactly:

- `source_intake.py` imports `source_contract`;
- `project_context.py` imports both `source_contract` and `source_intake`;
- `outcome_context.py` imports both `project_context` and `source_contract`;
- project-bounded `regii5_evidence_packet.py` imports the generic `source_contract` helper layer.

This is already **library-like internal reuse**.

### 7.2 Why that does not yet require `src/`

Current execution evidence points the other way:

- all tools live in one repo and are invoked directly as `python tools/<script>.py`;
- tests for Project/Outcome contexts execute the CLI scripts in fresh subprocesses rather than requiring an installed package;
- CI invokes the scripts directly and succeeds in a clean checkout;
- current generic tooling is standard-library Python;
- no external package consumer, stable public API, compatibility promise or independent installation requirement exists;
- no circular import, import-path failure or duplicated package namespace problem was demonstrated in this pass;
- fixture-specific scripts are visibly named/bounded and do not define generic module APIs.

Therefore the evidence supports:

> **small internal library-like core exists; package migration is not yet justified.**

### 7.3 Revised package threshold

IC-10 should no longer be justified mainly by `no external consumer`. A package boundary becomes warranted when one or more demonstrated internal conditions make script co-location unsafe or costly, for example:

1. multiple independent CLIs/derived views share a growing stable service layer;
2. another lifecycle/current-state resolver would create repeated parsing/owner-resolution logic rather than consuming a coherent module API;
3. tests need to verify the installed/imported runtime rather than only direct script execution;
4. sibling-script import/path assumptions become fragile across execution environments;
5. generic and fixture code can no longer be distinguished reliably by namespace/responsibility;
6. cycles or duplicated domain objects appear;
7. a real independent consumer/installability/compatibility requirement appears.

Conditions 1–6 can justify an internal package even without external distribution. Condition 7 would make the product/distribution question materially stronger.

### 7.4 Options

| Option | Current disposition | Why |
|---|---|---|
| S0 — keep `tools/` | **CURRENTLY SUFFICIENT** | clean direct execution, no demonstrated import/test failure |
| S1 — clearer generic vs fixture namespace under tools | **TRIGGERED OPTION** | useful if role ambiguity/maintenance friction appears; physical move alone has no current payoff |
| S2 — root package `paleo_type/` | **TRIGGERED OPTION** | plausible if a coherent internal API forms before installability matters |
| S3 — `src/paleo_type/` | **NOT YET WARRANTED** | strongest when installed-package/test isolation or stable API matters |
| S4 — multiple packages | **NOT SUPPORTED** | no independent package domains/consumers demonstrated |
| S5 — repo split | **NOT SUPPORTED** | would add compatibility/versioning/migration obligations without a consumer need |

### 7.5 One adjacent technical threshold

`source_contract.py` currently contains a deliberately simple scalar-YAML reader. This is proportionate for current Project metadata, but it is another trigger-based threshold: if Project/work metadata becomes structurally richer, a real parser/library boundary may become necessary. It is not a current defect or reason to package the repository now.

---

## 8. Co-development operationalization matrix

| Property | Normative support | Executable support | Tested / real evidence | Current gap |
|---|---|---|---|---|
| scholarship is product | strong GO/AGENTS | n/a | repeated Project practice | none material |
| Project finding local first | maintenance / quality / workflow | owner boundaries | #165/#166 | strong |
| Generic-Fit before generic promotion | maintenance / decisions | regressions after promotion | #169; other failure-derived guards | materially different fixtures still limited |
| system change admission | D-016 | Git/PR/tests | multiple historical admitted changes | current lifecycle revision not admitted |
| system support returns to scholarly objective | workflow / #225 semantics | partial derived contexts | #169 return/no-auto-priority; #225 work history | whole chain not represented by one generic current/closure mechanism |
| current research as system falsification | explicit in Project lifecycle / #225 | real-data tests | Reg.-Ii. history | fixture-family breadth narrow |
| materially different genericity proof | #225 / Generic-Fit principles | no universal mechanism required | insufficient in paleo-type current live fixture set | open qualification property |
| current/history/supersession | partial existing owners | some status/resolvers | many local examples | IC-01/02 structural gap remains |
| bounded operational current context | principles + C1R | project/outcome contexts | local passes | system work/currentness still partly Issue chronology based |
| package/runtime boundary | technical subsidiarity | current tools graph | clean CI/direct scripts | threshold should be explicit, no migration yet |

---

## 9. #225 current-state finding and its lifecycle significance

Fresh GitHub state reports #225 as **closed** at `2026-10-02T20:50:23Z`. Its issue body, however, still begins `ACTIVE SYSTEM-WIDE REQUIREMENTS / DESIGN ISSUE`, while current `README.md` also calls it currently open.

The same #225 body states that:

- local PASS/STOP/closure must not masquerade as whole-outcome completion;
- #225 cannot close from component counts/tests/architecture/documentation;
- T11 closure requires full Human-need→usable-result/ceiling evidence, fresh-context restart, bounded-repair recovery and a materially different fixture.

The current issue-comment set inspected in this pass contains extensive local-result/learning updates and the T11 contract, but no terminal comment was found that explicitly records those T11 conditions as satisfied or re-dispositioned.

Therefore this analysis records only:

```text
GitHub work-owner state: CLOSED
issue-body self-description: stale ACTIVE wording
README navigation: stale OPEN wording
T11 / whole-system acceptance: NOT INFERRED FROM CLOSURE
terminal acceptance evidence found in this pass: NONE
```

This is not a claim that T11 failed; it is an evidence-boundary statement. A later discovered terminal owner record could change it.

The mismatch is itself fresh evidence for the already-demonstrated lifecycle problem: Issue closure, current navigation and durable accepted meaning can diverge unless terminal consequence is promoted/reconciled explicitly.

Routine navigation should therefore describe #225 as closed work metadata and avoid claiming either acceptance or failure that has not been established by a durable terminal record.

---

## 10. Revised implementation-candidate map

| Candidate | Deep-check disposition | Refinement |
|---|---|---|
| IC-01 Generic work/programme lifecycle + closure | **KEEP / READY FOR HUMAN D-016 DISPOSITION** | co-development return/closure must preserve scholarly objective and explicit no-successor semantics |
| IC-02 Current/history/supersession + decision promotion | **KEEP; fuse with IC-01 unless design falsifies coupling** | Wirknetz chronology/provenance principles strengthen qualification, not implementation form |
| IC-03 Rebuildable operational status / bounded context | **KEEP / AFTER IC-01/02 SEMANTICS** | relation correctness and currentness must outrank graph completeness; #225 stale surfaces are a fresh fixture |
| IC-04 deterministic stale/current/closure checks | **KEEP CONDITIONAL** | only stable lifecycle relationships, not semantic invention |
| IC-05 migration/reconciliation | **KEEP CONDITIONAL** | migrate only surfaces proven necessary; do not reorganize current research for product cleanliness |
| IC-06 fresh-maintainer + closure qualification | **KEEP / STRENGTHEN** | include product-boundary and first-fixture/non-system-limit test; materially different fixture where a Generic-Fit claim requires it |
| IC-07 review-premise/evidence-basis provenance | **KEEP SEPARATE DESIGN** | Wirknetz source-role/relation-correctness lens is relevant, but scholarly review topology remains distinct |
| IC-08 qualified tag | **KEEP CONDITIONAL** | qualification baseline, not product release |
| IC-09 Release/SemVer/distributable template | **KEEP NOT READY** | Genericity still does not imply distribution |
| IC-10 Python package/`src` | **REFINE: TRIGGERED ARCHITECTURE OPTION; NOT WARRANTED NOW** | internal-runtime coupling/test-isolation can trigger it even without an external consumer |
| IC-11 branch protection | **UNCHANGED: REAL GAP / HUMAN-DEFERRED #90** | unrelated to this refinement |
| IC-12 #225 positive vertical fixture | **RECLASSIFY STATUS** | #225 is now closed as work metadata; its T11 acceptance is not established by closure in this pass. Preserve the vertical/materially-different-fixture criterion as historical acceptance evidence, not as an automatically active programme gap |
| IC-13 framework/template/consumer boundary | **REFRAME / DEFER** | not an active product candidate; reopen only on real consumer/distribution need or explicit Human product decision |
| IC-14 artifact reorganization | **UNCHANGED: design evidence needed** | physical separation is not required merely because live research and system development co-exist |
| Wirknetz runtime/Skill/Bridge | **DO NOT ADD** | property/trace/qualification lens only at current evidence |
| explicit co-development model | **REFINE TARGET-STATE INTERPRETATION, not standalone IC** | development/qualification principle cutting across IC-01/02/03/06 |
| generic-vs-fixture boundary | **QUALIFICATION PROPERTY, not standalone IC** | current examples must not define generic system semantics |

---

## 11. Target-state consequence

Disposition: **RESULT B — bounded refinement, core architecture unchanged**.

The 2026-10-03 target-state analysis remains valid in its central Class-B direction:

> existing canonical research owners + explicit closable work/programme lifecycle + durable decision promotion + current/history/supersession semantics + rebuildable operational views + qualification against target state.

This deep check refines four interpretations:

### TS-R1 — Product wording

Read `reusable framework-like METHOD/contracts/tools` only as a reuse property of support layers. It does **not** define the repository as a framework product. The development target is a scholarly research system whose support layers can be generic/reusable.

### TS-R2 — Research-instance role

`live reference research instances` means **first real scholarship + real-use/falsification fixtures**. Current Projects are not the intended limit of source/project diversity and cannot alone establish Generic Fit.

### TS-R3 — Wirknetz

No new relation store/Skill/Bridge is added to the target architecture. Provenance, correction, supersession, uncertainty and relation-correctness properties should be used to test IC-01/02/03/07 designs.

### TS-R4 — Package threshold

The target-state package criterion must include **internal coupling, test isolation and stable shared runtime APIs** as valid future triggers, not only installation/external consumption. Current evidence still says `no package migration now`.

No repository split, package layout, release model, ontology or graph store is selected.

---

## 12. D-016 consequence

The current D-016 lifecycle decision surface remains **DECISION READY / NOT ADMITTED**. No new architecture class is required by this deep check.

Before any Human disposition of that surface, read it together with this refinement evidence so that admission is not interpreted as authorization to build a clone-and-go framework product or to universalize current research fixtures.

If the Human Owner later chooses `ADMIT`, the bounded revision should still begin with the integrated IC-01/02 semantic work and should treat these as explicit qualification constraints:

1. scholarly product primacy is preserved;
2. system work cannot generate Project research priority;
3. current research fixtures are evidence, not system boundary;
4. Generic-Fit claims require evidence beyond one current fixture family where material;
5. result→owner→parent→closure semantics preserve provenance/correction/supersession without `latest wins`;
6. derived operational views do not become a second authority;
7. package/src reorganization occurs only after its own technical threshold is demonstrated.

A Human `ADMIT | REFINE | DEFER | REJECT` choice is still required before material lifecycle implementation. This artifact does not supply that choice.

---

## 13. What is not changed by this analysis

No change is made or implied to:

- `GOVERNING_OBJECTIVE.md`;
- generic scholarly METHOD;
- Source/File/Project canonical schemas or truth;
- any manuscript transcription, reading, interpretation or gate state;
- any Project `active_scope` or `NEXT ACTION`;
- #90 defer disposition;
- C1R read-only authority boundary;
- D-016 admission status;
- package layout or Python code;
- release/tag/productization status;
- `Wissensarbeit` state.

The only appropriate routine repository consequence outside this analysis evidence is navigation reconciliation for the now-closed #225 work owner and discovery of this refinement artifact.

---

## 14. Exact next bounded decision/action

After this analysis is persisted and navigation is reconciled, the next material action is **not another general audit** and not code.

The decision surface is:

```text
Human Owner disposition of the bounded lifecycle revision:
ADMIT | REFINE | DEFER | REJECT
```

The recommended evidence package for that decision is now:

1. `requirements/repository-knowledge-lifecycle-adequacy-audit-2026-10-02.md`;
2. `requirements/repository-knowledge-lifecycle-d016-decision-surface-2026-10-02.md`;
3. `requirements/repository-target-state-implementation-readiness-2026-10-03.md`;
4. this product/co-development deep check.

If admitted, implementation should use a new closable revision/programme owner; do not reopen #230. The first bounded work remains lifecycle/current-history/decision-promotion semantics, not a dashboard, package refactor, Wirknetz runtime or template product.

If not admitted, the analysis remains useful durable evidence and no implementation follows.

---

## 15. Chat-independence / completion check

The originating chat is no longer required to recover the key result of this analysis. A fresh maintainer can now determine from repository evidence that:

- clone-and-go/template productization is not the governing paleo-type objective;
- scholarship and generic support co-evolve through Project-local evidence, Generic-Fit and controlled promotion;
- current research artifacts are first real examples/falsification fixtures rather than the system boundary;
- Wirknetz contributes provenance/trace/supersession properties, not a selected new runtime component;
- current generic tools form a small library-like dependency core but do not yet justify `src/`/packaging;
- several genericity assumptions remain deliberately unproven until materially different future fixtures test them;
- #225 is closed as work metadata while terminal T11 acceptance is not inferred from that closure;
- the existing Class-B lifecycle architecture remains the best-supported direction;
- D-016 remains NOT ADMITTED and still requires explicit Human-Owner disposition.
