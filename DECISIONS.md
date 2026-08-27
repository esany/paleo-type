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

**Consequence:** Reusable source-wide crosswalks map these identifiers under `corpus/source-data/<source_id>/`; project source-use records carry project-relative function/relevant locus, while concrete Project-use→File evidence is separate. No folio is inferred from an export/image number alone.

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

## D-011 — Source-unit/research-scope project kinds

**Status:** superseded by D-012  
**Decision:** PR #40 introduced `source-unit` projects for individual canonical sources and `research-scope` projects for bounded investigations.

**Reason:** The intent was to give reusable source mappings one owner and prevent copied crosswalks.

**Consequence:** The distinction is retained only as historical rationale. It proved confusing to humans and semantically weak as a backend because a source record was represented as a project. D-012 preserves single ownership without source-as-project containers.

## D-012 — A project is an investigation over a source group; exact exports are first-class assets

**Status:** superseded by D-014  
**Decision:** Define a project as a bounded historical investigation / source-unlocking undertaking over one or more distinct canonical source records. Do not create projects automatically for archival records or files. Project-source membership, project-relative function (`principal`, `control`, `context`, `comparison`, etc.) and project-relevant locus live in `projects/<id>/sources/sources.tsv`; these functions are relations of the form `(project, source) → function`, not properties of the canonical source. The same source may therefore have different functions in different projects without changing `corpus/sources.tsv`. Canonical source identity remains in `corpus/sources.tsv`; reusable source-wide crosswalks live in `corpus/source-data/<source_id>/`. Source-to-source claims such as `extract_of` or demonstrated textual correspondence remain separate in `corpus/relationships.tsv`. Exact original exports used as evidence are first-class research assets tracked byte-exactly in `corpus/files.tsv` and should be repository-preserved when rights/authority permit.

**Reason:** Historians investigate coherent source groups, not technical source wrappers. A source has stable identity but no absolute research role: its function arises only within a concrete investigation. Conflating project-relative function with source identity or with source-to-source relationships would create false cross-project semantics. The source-unit model created apparent duplicate projects and artificial project-to-project relations. At the same time, relying on URNs/portal links without preserving the exact inspected PDF is inadequate for reproducibility and personal source safeguarding.

**Consequence:** Retained only as historical rationale. D-014 keeps project-relative roles and exact-export provenance but replaces the investigation-defined project boundary with a historically independent source-root boundary.

## D-013 — Governing scholarly objective has precedence over derived method and architecture

**Status:** accepted by explicit human owner decision during GOV-M1 / Issue #41.  
**Decision:** Establish `GOVERNING_OBJECTIVE.md` as the single highest-order, implementation-independent statement of repository purpose, governing invariants, precedence and human material-change authority. Methodology, information models, AI/HITL workflows, software, automation, GitHub workflow and presentation are derived means and may not silently weaken that objective.

**Reason:** The mission is already expressed across several repository files, but without one canonical precedence point a locally reasonable AI/engineering optimization could gradually substitute a proxy goal or reinterpret lower-level rules as authority to change the research purpose.

**Consequence:** Lower-level files should reference rather than restate the governing objective. Material amendments to it require an explicit human owner decision and visible rationale; routine research remains lean. The objective does not freeze current formats, standards, models, gates, GitHub or the Knau pilot.

## D-014 — A project is anchored to one historically independent source structure

**Status:** accepted by explicit human owner decision  
**Decision:** Every project has exactly one canonical `project_source_id` identifying its historically independent source root. In the current archival domain this root is an act. Sources structurally contained in that root are internal; sources outside it may still be used for comparison, control or context but remain external. Internal/external status is derived from the canonical `part_of` relations rather than copied into project metadata. Project-relative research functions remain relations of the form `(project, source) → function` and do not alter source identity. Exact source exports remain first-class byte-identified research assets as established in D-012.

**Reason:** A project should preserve the historically autonomous documentary structure rather than create a synthetic container from whatever source bundle a current question happens to use. This keeps historical structure stable while still allowing a narrow active research locus and external comparative evidence.

**Consequence:** `project.yml` requires `project_source_id`; the resolver derives project-root/internal/external status from `part_of`. Project scope may be narrower than the whole root, but it does not redefine project identity. The current Reg. Ii 5 `principal_source_id` remains temporarily supported only as legacy migration compatibility; target Principal semantics are governed by D-015. D-012 is superseded only on project-boundary semantics; its source-identity and exact-export provenance rationale remains retained here.

## D-015 — Project→Source research use and concrete File evidence are separate

**Status:** accepted by explicit human owner decision in the partial GOV-M4 synthesis / Phase-1 admission.  
**Decision:** Represent Project→Source use as one row per concrete `research_function`, allowing several functions for the same Source. Keep `research_function` project-relative, open-vocabulary and non-inferred. Represent concrete digital evidence for a use separately as `use_id → file_id` with an optional instance-relative locator; `corpus/files.tsv` remains the sole canonical owner of File identity/provenance. `principal` is a research function, not a Source property or second Project boundary anchor.

**Reason:** One coarse role per Project/Source collapses transdisciplinary use semantics, while storing one `primary_file_id` on that coarse relation conflates scholarly use with the exact digital instantiation used as evidence. Separating them preserves Source identity, allows multiple real research functions and keeps exact File provenance single-owned.

**Consequence:** Target project records use `source-uses.tsv` and optional `research/use-evidence.tsv`. `source-uses.relevant_locus` is source-relative scholarly scope; `use-evidence.evidence_locator` is a locator within the concrete used digital instance. A use may have zero or many evidence records and one File may support many uses. No evidence or Project→Project relation is inferred automatically. During the Reg. Ii 5 transition, the legacy source register, `primary_file_id` and `principal_source_id` remain readable until a separately admitted loss-checked migration proves `old project-source row → new use_id → use-evidence → same file_id` for every current link.

## D-016 — Material research-system changes require explicit admission before development

**Status:** accepted by explicit human owner decision in Issue #58 / Phase-1 admission.  
**Decision:** Material METHOD/CORPUS-model/Project-architecture/research-system changes follow `analysis → requirements → concept → owner review / explicit implementation admission → development → deterministic tests / scholarly loss checks → result review`. Routine source inspection, evidence logging, bounded research, transcription within an already admitted method/scope and implementation details already covered by a precise admitted scope do not require repeated approval loops.

**Reason:** A technically plausible implementation can still be epistemically wrong if it is built before the owner has reviewed the material concept and scope. Conversely, requiring approval for every routine source action would obstruct scholarship without improving accountability.

**Consequence:** Owner admission controls purpose, priorities and permission for material system change; it never substitutes for archival, palaeographic, historical or other qualified specialist validation. AI/method-compliance and independent specialist validation remain separate statuses. No workflow engine is required. `methodology/maintenance.md` is the canonical operational owner of the general admission rule; `methodology/ai-governance.md` owns only its AI/HITL-specific application and consequences and references the canonical workflow.
