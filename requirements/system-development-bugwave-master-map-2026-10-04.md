# System-development bugwave master map — 2026-10-04

**Status:** NON-NORMATIVE CURRENT ANALYSIS / WORK-PORTFOLIO EVIDENCE — **BUGWAVE ANALYSIS/DESIGN EXECUTION READY / SD-KA IMPLEMENTATION NOT READY / NOT D-016 ADMITTED**  
**Repository baseline:** `main@68c9536cfc566cd629aeaaae9ba2ad778cf0f9e7`  
**Human-visible work owner:** GitHub #244  
**Refines current process wording from:** `system-development-pre-implementation-anti-regression-baseline-2026-10-04.md`  
**Does not supersede:** governing objective, METHOD, accepted `DECISIONS.md`, Project/Corpus owners, or the evidence sources behind the findings.  
**This artifact is not:** D-016 admission, implementation permission, manuscript scope, scholarly `NEXT ACTION`, a second current-configuration owner, or proof of #225 scholarly whole-system acceptance.

## 1. Executive result

The 2026-10 audits describe one connected **system-development bugwave**, not a bag of unrelated cleanup items.

The central loop is:

```text
real failure
→ rich audit / many simultaneous findings
→ some findings promoted, some remain only in history
→ current meaning becomes distributed
→ fresh Human / developer / AI reconstructs state from chronology
→ pressure for a small local fix
→ locally correct PASS
→ parent/system gap survives
→ another audit reconstructs the whole
```

The current work therefore has two simultaneous obligations:

1. **preserve and disposition the entire material finding set**; and
2. **turn the remaining gaps into bounded, visible, dependency-aware work rather than another prose-only synthesis**.

The architecture class selected by the holistic design — Engineering Information Management + Configuration Management + finding/decision trace + bounded work/change state + derived context/query + developer/CI fitness + controlled migration — remains the strongest current candidate. It is **not yet ready for implementation admission** because several architecture contracts remain design work.

The earlier broad phrase `DEV-READY WITH BOUNDED REFINEMENT` is therefore made more precise here:

- **Bugwave analysis / coverage work:** executable now.
- **Architecture/design refinement:** executable now.
- **Physical migration / EKCP implementation:** not ready to implement and not admitted.
- **Human D-016 implementation decision:** not yet ready; first close the architecture-decision, finding-coverage and dependency gaps below.

Readiness is always stated relative to the next activity.

---

## 2. Bugwave — whole-system failure families

| Family | What repeatedly fails | Material findings | Active work |
|---|---|---|---|
| BW-1 Current state / configuration | current, proposed, historical and superseded system-development meaning require manual reconstruction | F02–F04, F09, F14, F18, F30, F32 | #246 |
| BW-2 Knowledge / promotion / trace | persisted audits do not guarantee that every material finding survives into current consequences | F01, F05, F06, F08, F11, F13, F19, F24, F29 | #245 |
| BW-3 Repository IA / DevEx | `requirements/` mixes semantic roles; system developer lacks one current entry path and target architecture view | F07, F18, F27, F30, F33 | #247, #251 |
| BW-4 Context / Human burden | applicable context is required but not compiled; Human risks becoming relay or confirmation proxy | F20, F21, F23, F31, F34 | #247, #249 |
| BW-5 Development-method adequacy | solution-shaped work and `lean/minimal` pressure can precede proof of sufficiency | F12, F22 | #249, #248 |
| BW-6 Assurance / closure | local technical success can look like system closure; engineering IA itself lacks fitness checks | F05, F09, F11, F15, F17, F26, F28 | #250 |
| BW-7 Epistemic review independence | fresh context may inherit the same contested premise; trace alone does not make evidence independent | F10 | #253 |
| BW-8 Product / genericity boundary | useful generic mechanisms can be over-promoted into product/package/runtime architecture | F24–F26 | #248, #251, #250 |
| BW-9 Interaction / prompt assets | prompts/work instructions are mixed into evidence; repeated copy-ready prompt need has no bounded capability owner | F20, F21, F23, F27, F40 | #252 |

### Root coupling

```text
weak engineering information lifecycle
+ weak engineering configuration/status accounting
+ incomplete finding/decision promotion
+ incomplete development-readiness operationalization
        ↓
chronology-aware reconstruction
        ↓
Human/AI/developer context tax
        ↓
premature local shaping becomes attractive
        ↓
local PASS without whole closure
        ↓
repeat audit
```

This does **not** reduce every bug to EKCP. F10 review-premise independence and F17 positive #225 scholarly vertical acceptance remain explicit residuals.

---

## 3. Activated finding coverage

F01–F34 remain the current activated register from the anti-regression baseline. This pass adds only findings that were not explicit enough there.

| ID | Additional finding from this pass | Evidence / consequence | Work path |
|---|---|---|---|
| F35 | **Audit coverage completeness must itself be proved.** Dispositioning registered findings is insufficient if a material finding was never registered. | direct consequence of F29 and re-audit requirement | #245 |
| F36 | **Architecture-decision visibility is underpowered.** `DECISIONS.md` is explicitly not a full ADR system while material architecture rationale remains distributed across designs/audits. | current `DECISIONS.md`; Portfolio comparator | #248 |
| F37 | **Readiness is activity-relative.** `DEV-READY` can collapse ready-to-analyse/design/decide/implement/validate. | current Human confusion + Portfolio ADR-0010 comparator | #249 |
| F38 | **Human decision-readiness jargon can itself hide meaning.** A technically correct label is not a usable decision surface. | current Human feedback; prior rebaseline | #249 |
| F39 | **Anti-regression can become a meta-loop.** Detail safeguards must not prevent bounded work that is already ready for its declared activity. | current Human feedback + no-progress principles | #249 / #244 |
| F40 | **Prompt/work-instruction is a real information class.** Prompt artifacts are currently mixed with Requirements/audits and repeated prompt creation is a real interaction burden. | `requirements/` brownfield + Wissensarbeit `.prompt` comparator | #252 / #251 |
| F41 | **Human strategic overview and Agent execution context are different products of the same state.** Optimizing one as the other causes either blindness or context swamp. | Portfolio ADR-0011 comparator + current Human need | #247 |
| F42 | **The bugwave itself lacked a visible bounded work surface.** Before #244–#253, current architecture work was primarily dated design/audit artifacts rather than open executable work. | fresh open-Issue audit | #244 and children |

### Material finding → Issue coverage

All currently activated findings have an Issue/disposition path:

- F01 → #245/#247
- F02 → #246
- F03 → #246/#247
- F04 → #246/#247
- F05 → #245/#250
- F06 → #245/#248
- F07 → #251
- F08 → #245/#247/#251
- F09 → #246/#250
- F10 → #253
- F11 → #245/#250
- F12 → #248/#249
- F13 → #245/#250
- F14 → #246/#247
- F15 → #250
- F16 → #246/#250
- F17 → #250 as an explicit residual **not solved by EKCP**
- F18 → #246/#247/#248/#251
- F19 → #245
- F20 → #247/#249/#252
- F21 → #249/#252
- F22 → #249
- F23 → #247/#249/#252
- F24 → #245/#248
- F25 → #248/#251
- F26 → #250
- F27 → #247/#251/#252
- F28 → #250
- F29 → #245
- F30 → #246/#248/#251
- F31 → #247
- F32 → #246/#248
- F33 → #246/#248/#251
- F34 → #247/#249
- F35 → #245
- F36 → #248
- F37–F39 → #249
- F40 → #252/#251
- F41 → #247
- F42 → #244

This is **work visibility**, not proof that finding coverage is complete. #245 owns the completeness proof across source audits.

---

## 4. GitHub work portfolio

| Issue | Work | Next activity | Implementation authority |
|---|---|---|---|
| #244 | Bugwave whole-system programme view | maintain whole map / integrate child consequences | no implementation authority |
| #245 | material finding coverage, promotion and trace | **coverage analysis / design ready** | registry implementation not admitted |
| #246 | engineering current configuration, identity, transitions | **design ready** | implementation/migration not admitted |
| #247 | bounded context, Human overview, developer bootstrap | **design ready** | Context Compiler not admitted |
| #248 | ADR surface / decision ownership | **ADR inventory/design ready** | Proposed ADRs are not accepted architecture |
| #249 | activity-relative readiness + understandable Human decision | **design/validation ready** | not D-016 admission-ready yet |
| #250 | engineering assurance / CI fitness / whole return | **fitness-contract design ready** | CI implementation waits for stable semantics/admission |
| #251 | brownfield classification + migration design | **classification/migration design ready** | physical migration not admitted |
| #252 | `.prompt` transfer | **adapt/design/test candidate ready** | repo-wide operational activation not yet admitted/fit-proven |
| #253 | Review Premise Inheritance | **targeted analysis/Generic-Fit ready** | orthogonal; not EKCP implementation by default |

### Dependency shape

The portfolio is not a waterfall, but these material dependencies currently hold:

```text
#245 finding coverage ─┐
                      ├→ #246 identity/config/currentness ─┐
#248 ADR inventory ───┘                                    ├→ #247 context/bootstrap
                                                           ├→ #251 migration representation
                                                           └→ #250 deterministic fitness

#245 + #246 + #247 + #248
        → #249 understandable Human decision / implementation-readiness surface

#247 + #251 → #252 `.prompt` operational-placement decision

#253 remains parallel/orthogonal unless its result changes shared architecture.
```

Bounded analysis within these Issues can begin now. Material implementation still requires D-016 admission after the design basis is sufficiently closed.

---

## 5. Repository information-architecture / developer audit

### What is already strong

A real developer would find substantial professional discipline rather than an undifferentiated notebook:

- clear highest-order objective and authority;
- explicit Source/File/Project ownership boundaries;
- canonical-vs-derived discipline;
- repo-first persistence;
- deterministic Source Contract and real regressions;
- Project context compilation;
- explicit D-016 material-change admission;
- CI that states its assurance boundary instead of laundering `PASS` into scholarly truth;
- repo-local standard-library Python rather than unnecessary package/service infrastructure.

### What would make a Senior Developer hesitate

The engineering-development surface is materially less mature than the scholarly Project surface:

1. `requirements/` is a mixed brownfield information namespace whose filename/path often carries hidden lifecycle semantics.
2. README is formally navigation but currently also carries a long programme-history/current-state synthesis.
3. `DECISIONS.md` is useful but explicitly not a full ADR system; architecture alternatives/supersession live largely in dated design/audit prose.
4. There is no first-class current engineering-configuration owner.
5. There is no system-development equivalent of `project_context.py`.
6. There was no open Issue portfolio for the current bugwave before #244–#253.
7. No explicit developer guide/architecture entry point explains current architecture, active change, full local assurance and contribution semantics in one bounded place.
8. Existing CI does not yet validate engineering currentness, finding coverage, trace integrity or generated engineering views.

### Verdict

**A good developer should not run away from the technical core; they would reasonably object to the system-development information architecture and onboarding cost.**

The code/tooling footprint is intentionally simple and disciplined. The major debt is semantic/navigation/configuration debt around the engineering process itself. Calling the repository as a whole `best practice` today would therefore overstate the evidence.

The target should be:

> **professional Brownfield repository: bounded current architecture/work surfaces + expandable provenance/history + explicit decisions + executable checks, without turning the repo into a portal/database/framework.**

---

## 6. Context / provenance principle

The bugwave confirms that context economy and provenance are complementary:

```text
DEFAULT
purpose / authority
→ current configuration / current change or explicit absence
→ current bounded work
→ applicable Requirements / accepted ADRs
→ blockers / uncertainty / completion condition
→ pointers

ON DEMAND
supporting finding
→ source audit / research
→ rejected alternatives
→ Issue/PR/Git chronology
```

Success means default context grows with **applicability/current work**, not with audit history.

Do not solve context cost by deleting evidence, flattening uncertainty or hiding authority.

---

## 7. Comparator disposition

### Portfolio

Fresh `esany/Portfolio` demonstrates several directly relevant patterns:

- current whole meaning, remaining programme gap, Requirements, ADRs, bounded Issues and candidate/history have different owners;
- `CURRENT_STATE.md` is only a compatibility/navigation pointer and deliberately does not mirror active Issues;
- ADRs have explicit lifecycle and retrospective records state that the file did not cause the historical decision;
- Human work overview and Agent execution context are distinct views over the same system;
- readiness names the next admissible activity rather than using one global `dev-ready` label;
- substantial Issues expose proportional problem/effect/readiness/dependencies/acceptance/Human-boundary semantics without requiring a heavyweight template.

**Transfer:** these are strong design properties for paleo-type.  
**Do not copy:** Portfolio's product boundary, exact directories, status vocabulary or programme structure as authority.

### Wissensarbeit

Fresh `esany/Wissensarbeit` continues to support:

- state/event driven lifecycle rather than rigid waterfall;
- derive-before-asking / Human not workflow engine;
- bounded context and externalization before compaction;
- trace correctness > completeness;
- failure-pattern checks and prompt review;
- `.prompt`, `.prompt review`, `.prompt test` as a thin candidate interaction capability.

Its `.prompt` Skill is **not Generic-Fit authority even inside Wissensarbeit**; it is a candidate with executable/real-use evidence but not regression-protected. Transfer therefore means adaptation + test + explicit paleo-type disposition, not copy-and-activate.

---

## 8. Best-practice check

The useful external practice is property-level, not template copying:

- **ADRs:** record one architecturally significant decision plus context/rationale/trade-offs/consequences; retain supersession rather than rewriting history.
- **Configuration Management:** distinguish approved/current configuration and baselines from the larger information corpus and its history.
- **Information Management:** identify, retain, retrieve, version/obsolete and expose information according to lifecycle and use.
- **Issue forms/contracts:** concrete work should carry enough structured information to start/close reliably; structure should be proportional rather than ceremonial.
- **documentation IA:** different user needs (orientation, how-to, reference, rationale) should not be forced into one ever-growing document.

The repo currently implements parts of all of these but not yet a coherent engineering-development surface.

---

## 9. Human decision readiness — plain language

Do not ask the Human to `validate Human-Decision-Readiness`.

The practical test is:

> **Can the repository explain the material decision well enough that the Human can understand what is being decided without reconstructing the audit history?**

Before a future D-016 admission request, the Human should receive only the decision-relevant view:

- the demonstrated problem and why it matters;
- what already works;
- the remaining gaps;
- the accepted decisions that constrain the solution;
- the proposed decisions still requiring choice;
- the selected architecture and serious alternatives;
- what the first implementation would do;
- migration/reversibility/risk;
- how success will be verified/validated;
- exactly what `ADMIT` would authorize and what it would not.

The Human is **not** expected to find Findings, sort Issues, rebuild dependencies, choose technical sequencing, relay work between contexts or pass a comprehension quiz.

---

## 10. Whole-system anti-loop rule

Each material work result must return:

```text
which Findings changed?
which Requirements / accepted or proposed ADRs changed?
which Issue dependencies/readiness changed?
did the remaining whole-system gap shrink?
what can now leave default context?
what is now ready for its next activity?
did a genuinely new Failure Family appear?
```

A new detail does **not** start another audit when it can be absorbed by an existing Requirement/ADR/Issue. Re-enter problem/architecture analysis only when the detail materially falsifies the current model or introduces a genuinely new failure family.

---

## 11. Current disposition

The bugwave is now **visible and bounded as work**, which is a real advance over dated-audit-only state. It is not yet implementation-ready as a whole.

Current state:

> **ANALYSIS / COVERAGE / DESIGN EXECUTION READY**  
> **SD-KA IMPLEMENTATION NOT READY**  
> **D-016 IMPLEMENTATION ADMISSION NOT YET READY**  
> **NOT ADMITTED**

The next legitimate work is to execute #245/#246/#248 and the independent brownfield/context design slices that do not depend on unresolved material decisions. The system does not need another unbounded whole-repo audit before that work starts.
