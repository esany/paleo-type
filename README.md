# paleo-type

Lean, evidence-based workspace for transparent transcription, source criticism and scholarly analysis of early modern handwritten sources.

## Purpose

The highest-order purpose, precedence and Human Owner change authority are defined once in `GOVERNING_OBJECTIVE.md`.

This README is the repository **orientation and reading-path view**. It is not a second method manual, Project status store or executable contract.

The research sources and scholarly result are the product. Software, AI models, GitHub, connectors and working formats are support infrastructure.

## Repository layers

### METHOD

`methodology/`, `AGENTS.md`, `DECISIONS.md`, `templates/`

Reusable scholarly/operational rules, governance rationale and templates. Concrete Source/File/Project research state does not belong here.

### CORPUS

`corpus/`, `entities/`

Canonical historical/documentary Source identity, exact digital File identity, reusable Source-wide mappings, evidenced relationships and shared normalized entities.

### PROJECT

`projects/<id>/`

Durable scholarly state for a purpose-established investigation: Project purpose/scope, documentary Source anchor, Project→Source research use, evidence bindings, transcription/analysis/decisions and restart state.

Project existence/priority is not inferred from Source/File structure. Detailed semantics live in `methodology/project-lifecycle.md`.

## Start here

### Human

1. Read this README for orientation.
2. Read `GOVERNING_OBJECTIVE.md` for purpose, precedence and Human Owner authority.
3. Open the relevant Project `project.yml` for purpose/scope/documentary anchor.
4. Open its `STATUS.md` for actual gate/evidence/restart state and authorized `NEXT ACTION` when one exists.
5. Open Project `source-uses.tsv` / `research/use-evidence.tsv` when Project→Source use or concrete File evidence matters.
6. Follow the owning methodology file for the specific question.

### AI / implementation agent

1. read `GOVERNING_OBJECTIVE.md` and `AGENTS.md`;
2. read the relevant Project/Corpus canonical state;
3. establish and load every canonical rule/requirement applicable to the concrete task;
4. use resolver/generated context where available instead of reconstructing structure/priority from names or chat;
5. continue only from an authorized task/`NEXT ACTION` when one exists.

Old chat must never be required to reconstruct durable research state.

## Cross-project analytical audit evidence

`requirements/` also contains **non-normative audit/review evidence** that can make recurring research-system risks visible across Projects and, with fresh local evidence, in other repositories. These files are not METHOD, Requirement owners or automatic task authority.

Current orientation set:

- `requirements/research-framing-transdisciplinary-competency-audit-2026-09-14.md` — reconstructs the transdisciplinary competency/authority architecture, role absorption and the research-framing gap;
- `requirements/research-system-problem-landscape-2026-09-14.md` — maps the currently identified construction sites, maturity asymmetries, interactions and known correction side-effects **without reducing them to one root cause or solution**;
- `requirements/pre-synthesis-research-program-2026-09-14.md` — non-normative planning/history owner for the now **closed pre-synthesis Research phase**; it records the original #183–#186 programme and the later bounded #191 closure extension without authorizing downstream synthesis;
- `requirements/shared-fixture-research-findings-2026-09-14.md` — frozen #184 internal/shared-fixture evidence on Requirement efficacy, failure mechanisms, dependency provenance and positive counterfixtures;
- `requirements/cross-source-research-findings-2026-09-14.md` — frozen #185 heterogeneous-source comparison across Reg. Ii 5, Darwin correspondence and Washington historical accounts;
- `requirements/pre-synthesis-research-integration-2026-09-14.md` — #186 decision-ready integration and hypothesis-by-hypothesis challenge of the pre-existing Concept Candidate;
- `requirements/final-multi-question-generation-research-2026-09-14.md` — #191 final bounded experiment positively demonstrating plural serious question formation while retaining source-/purpose-sensitive limits; this closes the pre-synthesis Research phase;
- `requirements/post-research-synthesis-concept-approaches-2026-09-14.md` — non-normative concept approaches used to bound the admitted post-Research synthesis, including mechanism-specific disposition, #186+#191 handling, authority separation, anti-regression questions and hard stop rules;
- `requirements/post-research-capability-requirement-synthesis-2026-09-14.md` — completed #198 bounded Capability/Requirement disposition: most findings are already normatively covered or mechanism-specific efficacy issues; one residual Concept-worthy need remains around plural evidence-grounded research-direction formation/challenge before Human-Owner priority selection, without authorizing architecture or implementation;
- `requirements/executable-transdisciplinary-research-system-concept-idea-2026-09-14.md` — preserves the earlier **non-normative concept candidate** as design history/hypothesis; its specific framing-layer/schema/leadership/AI/control-plane forms are not established merely by the Research evidence and it remains non-authoritative;
- `projects/ega-reg-ii-5-knau/research/post-166-research-framing-review-2026-09-14.md` — Project-specific fixture/review from which part of the cross-project evidence was derived.

For another Project/repository, use these as **inspection maps, Research findings or concept hypotheses according to each file's stated evidence status**, not as inherited diagnoses or implementation authority: establish analogous local evidence before deriving requirements, priorities or system changes.

## Where truth lives

| Question | Canonical owner |
|---|---|
| Why does the repository exist / what has precedence? | `GOVERNING_OBJECTIVE.md` |
| What stable AI/research guardrails always apply? | `AGENTS.md` |
| What cross-project rationale/decision history matters? | `DECISIONS.md` |
| What is the authoritative scholarly end-to-end method? | `methodology/historical-source-workflow.md` |
| What are the generic G1–G6 maturity requirements? | `methodology/research-gates.md` |
| How are Projects established/anchored/related to Sources and priority? | `methodology/project-lifecycle.md` |
| How are Source/File identity, provenance, preservation and access handled? | `methodology/source-and-provenance.md` |
| What evidence/source-status semantics apply? | `methodology/evidence-policy.md` |
| How is diplomatic/source-phenomenon transcription handled? | `methodology/transcription-guidelines.md` |
| How are execution context, prerequisites, evidence staging and loops handled? | `methodology/workflow.md` |
| How are quality/falsification/review dimensions handled? | `methodology/quality-and-learning.md` |
| How are ownership, D-016 admission and propagation handled? | `methodology/maintenance.md` |
| How are GitHub Milestones interpreted? | `MILESTONES.md` |
| What stable machine-checkable Source/File/Project-use constraints apply? | `corpus/source-contract.json` + `tools/source_contract.py` |
| What is a Source/File/relationship/crosswalk fact? | `corpus/` |
| Why/what is one Project and what is its current scope? | Project `project.yml` |
| How does the Project currently use Sources? | Project `source-uses.tsv` |
| Which concrete File supports a Project use? | Project `research/use-evidence.tsv` |
| What is the current Project restart/gate/evidence state? | Project `STATUS.md` |
| What did the Project actually read/decide/observe? | owning Project research files |

Generated views such as `tools/project_context.py` are rebuildable navigation/restart aids, never canonical truth.

## Current Project directories

The repository currently contains:

- `projects/ega-reg-ii-3/`;
- `projects/ega-reg-ii-4-bd-ii/`;
- `projects/ega-reg-ii-5-knau/`.

The last path is a legacy directory/id retained for continuity. Its current Project meaning, scope and priority are defined only by its canonical Project files, not by the `knau` slug.

Do not copy current Project scope/gate/`NEXT ACTION` into this README. Read the Project owner directly or use the rebuildable Project-context view.

## Canonical-versus-derived rule

One durable fact/state has one canonical owner. Human-facing summaries, generated context, GitHub Issues/Milestones and chat may point to that state but must not become parallel truth stores.

When stable structure can be resolved deterministically, use the executable resolver/validator instead of asking AI to infer it repeatedly.

## Repository structure

```text
GOVERNING_OBJECTIVE.md
AGENTS.md
DECISIONS.md
MILESTONES.md
README.md
methodology/
templates/
corpus/
  sources.tsv
  files.tsv
  relationships.tsv
  source-contract.json
  source-data/
entities/
projects/
  <project-id>/
    project.yml
    STATUS.md
    source-uses.tsv
    research/
      use-evidence.tsv
    ... scholarly work as required ...
tools/
  source_contract.py
  source_intake.py
  project_context.py
tests/
```

Optional Project work directories exist only when real work requires them.

## Restartability acceptance

Another capable researcher/agent, given repository + authorized evidence and no old chat, should be able to determine:

- repository purpose/authority boundaries;
- Project purpose/scope and documentary anchor;
- canonical Source/File identity and structural relationships;
- Project-relative Source use and concrete evidence bindings;
- actual Project research/gate/evidence state;
- whether required evidence is merely identifiable/reproducible or actually ready for the target task;
- whether an authorized `NEXT ACTION` exists;
- which outputs are canonical versus derived;
- which GitHub items are only planning/review metadata.

If continuation requires stale orientation prose, duplicated state, inferred priority or recovery of the old chat, the repository has drifted and the owning surface must be repaired.