# Decisions — lean architectural and methodological record

This file records only consequential **cross-project decisions** whose rationale a future researcher or agent would otherwise have to rediscover.

It is intentionally not a full ADR system.

## What belongs here

Record a decision when it changes the shared data model or method, establishes a durable cross-project rule, rejects a plausible alternative, or would be difficult to understand from the implementation alone.

Do **not** record here:

- concrete manuscript readings or adjudications → project `apparatus/decisions.tsv`;
- current research state → project `STATUS.md`;
- project-specific corrections/failure modes → project `LEARNINGS.md`;
- deferred improvements → GitHub Issues;
- ordinary implementation details → Git history/commit message.

Each entry should remain short: **decision, reason, consequence**, and where useful what it supersedes or when it should be revisited.

---

## D-001 — Lean canonical formats

**Status:** accepted  
**Decision:** Use Markdown for method/status/reasoning, TSV for structured research records and YAML for small stable project metadata. Do not introduce a database, RDF/RiC-O store, TEI authoring environment or custom application without a demonstrated research need.

**Reason:** The project optimizes for reliable source work, inspectability, Git diffs and restartability rather than infrastructure. RiC and TEI remain conceptual/interchange reference standards.

**Consequence:** More elaborate technology is deferred to a trigger-based GitHub Issue and adopted only when it measurably improves correctness, interoperability or repeated workload.

## D-002 — Canonical source identity is provenance-derived

**Status:** accepted; supersedes the initial use of `A`, `B`, `C1`, `C2` as corpus identifiers.  
**Decision:** Canonical source identifiers must derive from stable archival/record identity. Ordinal witness sigla may be used only as explicitly defined local shorthand, never as corpus primary identity.

**Reason:** Research roles change and ordinal labels are meaningless outside their immediate context. Provenance-derived identity remains interpretable across projects and chats.

**Consequence:** Source identity, research role and optional edition siglum are separate fields/concepts.

## D-003 — Archival record, witness, locus and digital instantiation remain distinct

**Status:** accepted  
**Decision:** Preserve the chain `archival unit → record → witness → locus → instantiation`. Folio, portal image number, PDF page, export sequence, URN and working image ID remain separate identifiers.

**Reason:** Digital archive exports expose multiple numbering systems and representations that are not interchangeable. Collapsing them can create false provenance.

**Consequence:** Project crosswalks map these identifiers explicitly; no folio is inferred from an export/image number alone.

## D-004 — Three truth domains must not silently rewrite each other

**Status:** accepted  
**Decision:** Keep **ARCHIVAL**, **TEXTUAL/PALAEOGRAPHIC** and **HISTORICAL** claims distinct. Within textual work preserve `OBSERVATION → READING → NORMALIZATION → IDENTIFICATION → INTERPRETATION`.

**Reason:** Historical plausibility, catalogue metadata or a clearer parallel can otherwise contaminate what is claimed to be visible in a manuscript.

**Consequence:** Later-layer knowledge may generate hypotheses and tests but cannot silently change an earlier-layer claim.

## D-005 — Source relationships are claims, not identity shortcuts

**Status:** accepted  
**Decision:** Statements such as `extract from`, `copy of`, `parallel to` or `textually corresponds to` carry an explicit evidence status. Catalogue metadata supports catalogue-level relationship claims; textual dependence/correspondence requires inspection and collation.

**Reason:** Similar subject matter or archival metadata does not itself demonstrate textual dependence.

**Consequence:** Related records remain independently identified and read before collation; a clearer witness cannot overwrite the witness under transcription.

## D-006 — Chat is transient; GitHub owns durable research state

**Status:** accepted  
**Decision:** No consequential fact, decision, open problem, source identity, research state or deferred design rationale may depend on recovery of an old chat.

**Reason:** Research must be restartable and independently inspectable.

**Consequence:** Durable state is persisted in its canonical repository record; deferred but potentially valuable improvements use trigger-based Issues.

## D-007 — Quality assurance is evidence-first and proportional

**Status:** accepted  
**Decision:** Apply domain expertise proactively, but validate claims against the evidence appropriate to their consequence. Unresolved is an acceptable result; unsupported resolution is not. Use adversarial spot-checking for consequential working claims.

**Reason:** Formal consistency and model agreement can preserve or amplify an initial error.

**Consequence:** The workflow may stop or downgrade a claim rather than complete it semantically. Stronger validation is required as consequence/publication stakes rise.

## D-008 — Automation must solve an observed bottleneck

**Status:** accepted  
**Decision:** Add schema validation, HTR, import automation or other tooling only after a real repeated failure/bottleneck demonstrates value. Until then preserve the option and trigger in an Issue.

**Reason:** Tooling overhead can displace the actual historical research and create maintenance burden.

**Consequence:** The default response to a research problem is the simplest discriminating source/evidence action, not new infrastructure.

## D-009 — Method, corpus and project knowledge are separate layers

**Status:** accepted; supersedes project-local copies of generic research gates.  
**Decision:** Reusable scholarly method and G1–G6 maturity requirements live once in `methodology/`; cross-source identities/context live in `corpus/` and `entities/`; concrete source observations, readings, decisions, validation state and next actions live in `projects/<id>/`. A pilot project may expose a methodological weakness but does not define generic method automatically.

**Reason:** Mixing pilot facts with reusable method creates hidden coupling, duplicated truth, drift and false generalisation from a single source.

**Consequence:** Project `MILESTONES.md` copies are removed. Generic gates live in `methodology/research-gates.md`; project `STATUS.md` records only state and source-specific gaps against those gates. Generalisation follows `project observation → project learning/status → explicit generalisability check → methodology/decision update`.

## D-010 — Milestone families organize admitted work; they never own scholarly truth

**Status:** accepted; supersedes the initial narrower rule that prohibited G1–G6 GitHub Milestone mirrors.  
**Decision:** GitHub Milestones may organize different work families. Use `GOV-*` Milestones for repository governance/architecture phases and project-scoped `<project> / G*` Milestones for discrete scholarly Issues contributing to generic G1–G6 gates. Open Issues without a Milestone remain backlog/deferred until scheduled or triggered. Labels remain the orthogonal classifier for scholarly/technical domains.

**Reason:** GitHub needs to expose both system-level work sequences and human-readable project research work. A project G2 Milestone can usefully group the Issues required for diplomatic representation without becoming the scientific claim that G2 has been reached. Prohibiting all gate mirrors loses that navigation benefit; treating Milestone completion as gate completion would instead duplicate truth and create synchronization drift.

**Consequence:** `MILESTONES.md` defines Milestone-family semantics and naming. Generic G1–G6 requirements remain canonical only in `methodology/research-gates.md`; actual gate state remains canonical only in project `STATUS.md`. A GitHub project-gate Milestone means planned Issue work toward that gate, not evidence-based gate attainment. One Issue uses the primary target Milestone and multiple labels for cross-disciplinary relevance. No Milestone means backlog/unscheduled, not low scholarly maturity.

## D-011 — Projects have explicit kinds and project relations are not source relations

**Status:** accepted  
**Decision:** Create projects from a generic minimal contract, not by cloning a pilot. Distinguish `source-unit` projects, which own reusable source-local mapping/work for one canonical source, from `research-scope` projects, which own bounded questions/loci/edition tasks. Research-organisational project relations live in `projects/relationships.tsv`; historical/archival/textual source relations remain in `corpus/relationships.tsv`.

**Reason:** As multiple archival units enter the repository, copying source mappings into every consuming research project would create drift, while treating research organisation as source history would create false scholarly claims.

**Consequence:** Source-unit mappings have one canonical home; research-scope projects reference them. New projects are instantiated from `templates/project/` and must pass `methodology/project-lifecycle.md`. Project findings feed back through the explicit project → source-unit/corpus → related-project or project → generalisability → method consistency loops.
