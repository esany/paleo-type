# LEARNINGS — Reg. Ii 5 / Knau

This file records project-specific lessons. It is not evidence for manuscript readings.

## L001 — whole-word silhouette guessing caused major errors

Observed failure: early readings such as `welch` versus later `wolff`, and other fluent-looking words, were produced before enough same-hand grapheme evidence existed.

Corrective practice: prefer local grapheme comparison and repeated same-hand forms. Do not promote a word because its silhouette and syntax look plausible.

Generalizable: yes; reflected in `methodology/quality-and-learning.md`.

## L002 — semantic coherence is dangerous during first transcription

Observed failure: incomplete clauses were turned into grammatically coherent historical German, then later treated as if read from the image.

Corrective practice: blind reading first; unresolved spans remain unresolved. Interpretation is a later layer.

Generalizable: yes.

## L003 — historical name knowledge can leak into manuscript spelling

Observed issue: historical `Gräfendorf` and manuscript working forms such as `grevendorff`/variants risked being conflated.

Corrective practice: manuscript reading and historical identification remain separate records.

Generalizable: yes.

## L004 — numerical/economic notation needs its own concordance

Observed issue: itemized income/measure passages were substantially harder than running prose and mixed Roman/Arabic or specialist notation.

Corrective practice: collect numerals, currency and measure signs across pages before interpreting individual tokens.

Generalizable: likely; currently implemented as a project workflow and palaeography table.

## L005 — metadata was overstated as source content

Observed failure: finding-aid/search information about possible parallel volumes was described too strongly before the actual pages were inspected.

Corrective practice: explicit P/E/F/K/R/S/H source status and passage-level audit.

Generalizable: yes.

## L006 — repeated AI readings are not independent confirmation

Observed issue: multiple model passes can reproduce the same contextual bias.

Corrective practice: treat repeated model output as one reader unless evidence source changes (new image detail, same-hand comparison, independent HTR, external primary parallel, human validation).

Generalizable: yes.

## L007 — the project must preserve a restart point

Observed failure: chat-based work repeatedly revisited method and lost the exact next task.

Corrective practice: `STATUS.md` contains one canonical `NEXT ACTION` and is updated when the research state changes.

Generalizable: yes.

## L008 — the pilot was allowed to define generic method

Observed failure: generic scholarly gate requirements and parts of the method were copied into the Knau project and mixed with source-specific facts such as concrete folios, working IDs and unresolved tokens. This made the pilot a hidden second definition of the framework.

Corrective practice: generic method/gates now live only in `methodology/`; project `STATUS.md` records only its own state and evidence gaps against those generic requirements. Concrete pilot observations remain here or in project research records and are promoted only after an explicit generalisability check.

Generalizable: yes; reflected in `methodology/historical-source-workflow.md`, `methodology/research-gates.md`, `AGENTS.md` and `DECISIONS.md` D-009.

## L009 — protocol-level source wrappers were mistaken for projects

Observed failure: PR #40 created `source-unit` projects for individual protocol/source records mainly to give source-wide crosswalks one owner. This duplicated infrastructure and confused documentary components with historically independent project structures.

Corrective practice: reusable source identity/crosswalk/file provenance remains in `corpus/`. A project is anchored once to its historically independent source root via `project_source_id`; protocol/section/etc. nodes inside it remain corpus sources related by `part_of`, not separate projects merely because they need canonical metadata.

Generalizable: yes; reflected in `methodology/project-lifecycle.md`, `AGENTS.md` and `DECISIONS.md` D-014.

## L010 — provider record IDs and one current hierarchy were mistaken for the data model

Observed failure: the four user-supplied source-group entries were repeatedly reinterpreted as archival acts because portal/DigiRef identifiers were treated as if they fixed archival granularity. A subsequent correction then encoded the current `act → protocol` pattern itself as a special `archival-acts.tsv` + `archival_act_id` infrastructure. Both moves confused one observed hierarchy with the generic structure needed by the corpus.

Corrective practice: determine source granularity independently of provider-record granularity. Keep every historical/documentary object that needs stable identity as a source node in `corpus/sources.tsv`; express containment generically as evidence-status-controlled `part_of` relations in `corpus/relationships.tsv`. The current Knau case is simply four protocol nodes related to three larger act nodes. Future section/protocol/act/volume/series or other part–whole structures use the same node/relation pattern without schema changes.

Generalizable: yes; reflected in `methodology/source-and-provenance.md` and source-contract validation.

## L011 — a research bundle was mistaken for project identity

Observed failure: after correcting source granularity, the project itself was still defined as the current Knau investigation over one principal and several comparison/control/context sources. That made the project boundary depend on a research question rather than the historically independent documentary structure.

Corrective practice: bind each project to one `project_source_id`. Current scope may be narrow; external sources may be used; neither changes project identity. Determine whether any used source is internal or external from its canonical `part_of` ancestry relative to the project root.

Generalizable: yes; promoted through `methodology/project-lifecycle.md`, `AGENTS.md`, the source resolver and `DECISIONS.md` D-014.
