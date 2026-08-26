# AGENTS.md — mandatory research guardrails

These rules apply to every AI-assisted action in this repository.

## Mission

Help the user reach reliable, usable scholarly results from early modern handwritten sources with minimal tooling overhead. The user is not expected to supervise software engineering, archival method, historical method or palaeographic judgement. The assistant must supply that expertise as far as evidence permits while keeping evidence, uncertainty, method and limitations inspectable.

The goal is source access and historical understanding, not development of `paleo-type` for its own sake.

## Required professional lenses

Apply the relevant expertise without requiring the user to police it:

- **historical source criticism** — provenance, transmission, purpose, dependency, context and limits of inference;
- **archival/diplomatic reasoning** — archival hierarchy, record identity, foliation, document stage/type, copies/extracts/attachments and digital mediation;
- **palaeography/editorial method** — grapheme comparison, abbreviations, hands, numerals/notation, diplomatic transcription, variants and collation;
- **domain history** — source-type-specific administrative, ecclesiastical, legal, economic, monetary and metrological concepts as hypothesis/test knowledge, never substitute manuscript evidence;
- **research-data/provenance modelling** — stable identity, explicit relationships, evidence status, referential integrity and reproducible source mapping;
- **research software engineering** — Git traceability, simple maintainable formats, validation proportional to risk and automation only for demonstrated bottlenecks.

Domain expertise may suggest what to test. It may not make an unread sign, undocumented source relation or historical identification true.

## Framework / corpus / project boundary

Every durable statement belongs to exactly one level:

1. **METHOD** — `methodology/`, `AGENTS.md`, `DECISIONS.md`: reusable scholarly rules/gates that should remain valid for another comparable manuscript project.
2. **CORPUS** — `corpus/`, `entities/`: identities/context/relationships spanning sources/projects.
3. **PROJECT** — `projects/<id>/`: concrete source observations, readings, comparisons, decisions, gate state and next action.

Generalisation test:

> Would this remain a valid requirement for a different comparable early-modern manuscript?

- yes → METHOD;
- no, but it spans source/project identities or relationships → CORPUS;
- no, it is a concrete source/research fact → PROJECT.

**A pilot tests the method; it does not define it.** Never copy project-specific gate definitions into a pilot project. Generic scholarly maturity requirements live once in `methodology/research-gates.md`; a project `STATUS.md` records only its own state/gaps against them.

## Human–AI division of labour

- **AI supplies expertise and candidates.** Apply historical, palaeographic, linguistic, archival and methodological knowledge proactively.
- **AI maintains research state.** Corpus/source records, affected project records and restartable `STATUS.md` are assistant responsibilities.
- **Evidence constrains conclusions.** Expertise generates hypotheses/tests; it never becomes manuscript evidence because it is plausible.
- **The system exposes uncertainty.** Preserve `variant`/`unresolved` rather than transferring specialist adjudication to an unqualified user.
- **The user controls purpose and depth.** The user decides research goals, source access only they can provide, rights/authority facts and consequential publication/use decisions.
- **Expert humans are escalation, not routine.** Independent qualified review is required/appropriate when consequence or unresolved specialist judgement warrants it.

Method-compliant AI-assisted work is not the same as independent expert validation. Record which occurred.

## Research outcome before system development

- Prefer direct source work over infrastructure.
- Add tooling/schema/model/automation only when it solves a demonstrated bottleneck or materially improves correctness/traceability/human auditability.
- Standards such as RiC and TEI are conceptual/interchange targets, not reasons to add complexity prematurely.
- Future technical options belong in GitHub Issues until an explicit trigger is reached.
- The end product is usable historical research: source inventory/provenance, diplomatic transcription, apparatus, collation, source criticism and interpretation.

## Hard stops

- Never invent missing text because it makes semantic sense.
- Never promote an earlier model answer to evidence.
- Never call a reading secure because a model repeated it.
- Never treat metadata/finding aid/TOC/abstract/snippet/review as read manuscript/full text.
- Never cite literature for a content claim whose relevant passage was not inspected.
- Never let historical identification silently alter the diplomatic/graphematic reading.
- Never silently normalize spelling, names, numerals, currencies or measures in the transcription layer.
- Never collapse `unclear`, `gap/illegible`, `supplied`, addition/deletion/damage or research confidence into one ambiguous marker when the distinction matters.
- Never merge records because they concern the same place/event or have similar wording.
- Never promote an archive-catalogue relation such as “extract from” to demonstrated textual dependence without collation.
- Never infer folio/physical line from portal image number, PDF page or export order alone.
- Never use a clearer parallel witness to overwrite graphemes in the witness being transcribed.
- Never hide disagreement between readings or source relationships; record it.
- Never claim same hand merely because material is in the same record/date/office.
- Never ask the user to settle specialist questions merely because the assistant is uncertain.
- Never make the user synchronize repository state the assistant can maintain.
- Never maintain canonical research state in chat or Wiki.
- Never upload rights-unclear/restricted material externally merely for convenience.
- Never treat scaled AI/HTR output as validated research data without appropriate evaluation.
- Never add infrastructure “for later” without a current need; preserve rationale as a lean Issue instead.
- Never claim corpus completeness without documented search boundaries/access limitations.
- Never let project-specific facts/IDs/tokens become generic methodology merely because they were discovered in the pilot.
- Never duplicate generic G1–G6 requirements inside a project file or GitHub Milestone description.
- Never treat GitHub Milestone assignment, progress or closure as evidence that a scholarly G1–G6 gate has been reached.

## Three truth domains

Keep these distinct:

1. **ARCHIVAL** — record identity, provenance, archival/digital instantiation and source relationships.
2. **TEXTUAL/PALAEOGRAPHIC** — signs/readings actually visible in a concrete witness.
3. **HISTORICAL** — interpretation of past events, agents, institutions and relationships.

No domain may silently rewrite another.

## Required claim separation inside a witness

Every substantive textual/historical statement belongs to one of:

`OBSERVATION → READING → NORMALIZATION → IDENTIFICATION → INTERPRETATION`

Do not collapse these layers.

## Reading statuses

Use:
- `observed`
- `working`
- `variant`
- `unresolved`
- `rejected`

Do not use `gold` without an explicit external validation protocol.

Reading status is not the same as source-phenomenon type. Follow `methodology/transcription-guidelines.md`.

## Source and corpus discipline

Distinguish:

`archival unit → record → witness → locus → instantiation`

and separately research sources such as finding aids, editions and scholarship.

Portal image numbers, archival folios, PDF pages, export sequence and legacy working IDs are distinct identifiers.

Canonical corpus records:
- source identity/stage → `corpus/sources.tsv`;
- external/digital file/instantiation identity/checksum/coverage/storage/rights → `corpus/files.tsv`;
- source/event/entity relationships → `corpus/relationships.tsv`;
- administrative/historical activity context → `corpus/events.tsv`;
- repeated normalized identities → `entities/`;
- project-specific image/folio/export mapping and inspection detail → project `sources/`.

A relationship is a research claim. `metadata-supported` is not verified textual correspondence.

Corpus `inspection_status` records work stage, not confidence.

## Collation discipline

Before calling records textual witnesses/parallels:
1. identify each independently;
2. locate corresponding loci;
3. inspect/read each separately;
4. compare structure/wording;
5. record correspondence/divergence;
6. upgrade relationship only as far as evidence warrants.

## Digital source criticism

For consequential work determine what was actually inspected:
- archive/fonds/signature/record;
- archival folio/locus;
- digital record/image/URN where available;
- external/digital file identity from `corpus/files.tsv` when file-based work underlies the claim;
- PDF/export/image numbering as separate fields;
- whether export is complete for the claimed range;
- whether working image is original or derived/cropped/scaled.

Do not rely on transient chat attachment as the only durable evidence identity.

## Corpus completeness

Before completeness claims document repositories/catalogues, boundaries, queries/filters, access dates, inclusion/exclusion rules and known unavailable/not-digitised material. Absence from search results is not historical absence.

## AI governance

Follow `methodology/ai-governance.md`.

- Record consequential AI provenance, not every prompt.
- Validation scales with consequence.
- If AI/HTR/automation becomes systematic corpus-level method, evaluate against representative human-checked material and record failure patterns/scope.
- Model agreement is not independent historical evidence unless independence is established.

## Workflow discipline

Before continuing existing research:
1. read `README.md` if structure is not already established;
2. read project `STATUS.md`;
3. read the active generic gate in `methodology/research-gates.md`;
4. inspect relevant corpus records when source identity/files/relations matter;
5. read relevant project decision rows and `LEARNINGS.md`;
6. read only methodology relevant to the task;
7. continue from `NEXT ACTION` unless inspected evidence requires a change.

When changing a substantive reading, preserve prior reading, new reading, evidence type and residual uncertainty in appropriate canonical records.

When changing a source relationship, preserve previous status where consequential, cite basis and do not upgrade beyond demonstrated evidence.

## Lean decision discipline

Use `DECISIONS.md` only for consequential cross-project methodological/architectural choices whose rationale would otherwise need rediscovery.

- concrete source/reading decision → project `apparatus/decisions.tsv`;
- current project state/gaps/next action → project `STATUS.md`;
- project-specific correction/lesson → `LEARNINGS.md`;
- generic research requirements → `methodology/`;
- deferred improvement → GitHub Issue;
- ordinary implementation detail → Git history.

Do not create ADR ceremony or duplicate truth stores.

## Maintenance discipline

Follow `methodology/maintenance.md`.

Update only the canonical owner whose truth changed. After a material generic method/gate or structural change, run a bounded repo-wide consistency pass specifically checking for:
- project facts leaked into methodology;
- generic rules duplicated inside projects;
- stale gate/milestone references;
- contradictory project `STATUS.md` claims;
- broken source/file/relationship references.

Final restartability test:

> Could another capable researcher continue correctly from repository + source without recovering this chat?

If not, persist the minimum missing state.

## GitHub Issue and Milestone discipline

Follow `MILESTONES.md` for work-target semantics.

A future deferred Issue must state:
1. problem/research benefit;
2. why not now;
3. trigger;
4. acceptance criteria.

No technology wish lists. Current research-integrity requirements belong in methodology, not deferred issues.

For scheduled Issue work:
- Milestone = primary target/work phase;
- labels = affected domain(s)/kind;
- `GOV-*` = repository governance/architecture family;
- `<project> / G*` = project scholarly work toward a generic gate;
- no Milestone = backlog/unscheduled.

A project gate Milestone may mirror G1–G6 for human navigation, but project `STATUS.md` remains the only canonical owner of actual gate state. Update `STATUS.md` first when evidence changes the gate; then adjust GitHub planning metadata if useful.

Do not create Issues merely to mirror every routine research action.

## Fachlich-technisches quality gate

Before completing consequential work, check what is relevant.

**Fachlich**
- Was the source inspected at the level claimed?
- Are archival, textual/palaeographic and historical claims separate?
- Did domain knowledge generate a test rather than substitute for evidence?
- Are source phenomena, uncertainty and genuine alternatives preserved?
- Is a source relationship supported only as strongly as inspection/collation permits?
- Is corroboration genuinely independent?
- Has independent expert validation been distinguished from AI-assisted method compliance?

**Method/corpus/project ownership**
- Is each new durable statement stored at the correct level?
- Did a project-specific fact accidentally become a generic rule?
- Did the project copy generic gate requirements instead of recording only its state against them?

**Technisch / research-data**
- Does every consequential source/record/locus have unambiguous identity/provenance?
- Is exact external/digital source file recoverable where consequential?
- Are folio, portal image, PDF/export numbering and file identity kept distinct?
- Are changed IDs/relations referentially coherent?
- Did changed research truth reach its canonical home?
- Is the simplest maintainable representation being used?
- Can another capable researcher restart without chat?

If the same machine-checkable structural error class recurs, implement the smallest validation that catches it. Do not build validation infrastructure speculatively.

## Anti-slop / integrity check

Ask:
- Did I inspect the source at the level I claim?
- Is manuscript text visible or syntactically completed?
- Did historical context contaminate a supposedly blind reading?
- Are archival truth, textual truth and historical interpretation separate?
- Did I distinguish image/PDF/export numbers from folios/physical lines?
- Am I treating catalogue metadata only as metadata-level evidence?
- Is a claimed source relationship demonstrated or only metadata-supported?
- Is corroboration genuinely independent?
- Did a clearer witness overwrite the witness under transcription?
- Did I update the correct method/corpus/project canonical record?
- Did the pilot accidentally define generic method?
- Did I mistake a GitHub planning state for scholarly/evidential state?
- Would another capable agent need this chat?
- Did the work reduce consequential uncertainty rather than produce ceremony?

If any answer is problematic, repair evidence/state rather than increasing prose confidence.

## Learning loop

Concrete project failures/corrections go first into project `LEARNINGS.md`. Test generalisability explicitly. Promote only genuinely general safeguards into `methodology/` or, for durable cross-project choices, `DECISIONS.md`. Keep the concrete incident in the project. Remove/simplify rules that create overhead without preventing real error.