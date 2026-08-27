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

Corrective practice: generic method/gates now live only in `methodology/`; Knau `STATUS.md` records only its own state and evidence gaps against those generic requirements. Concrete pilot observations remain here or in project research records and are promoted only after an explicit generalisability check.

Generalizable: yes; reflected in `methodology/historical-source-workflow.md`, `methodology/research-gates.md`, `AGENTS.md` and `DECISIONS.md` D-009.

## L009 — source records were turned into artificial projects

Observed failure: PR #40 created `source-unit` projects for individual archival records so that source-wide crosswalks would have a single owner. This made one historical investigation appear as several duplicate projects, obscured the actual source group, and introduced artificial project-to-project relations whose targets were really sources.

Corrective practice: define a project as the bounded historical investigation / source-unlocking undertaking. Keep canonical corpus source information outside projects, declare project role/locus in `sources/sources.tsv`, and keep reusable crosswalks in `corpus/source-data/<source_id>/`. Preserve exact original exports as first-class file assets rather than treating a URN as equivalent backup.

Generalizable: yes; promoted through `methodology/project-lifecycle.md`, `methodology/source-and-provenance.md`, `AGENTS.md` and `DECISIONS.md` D-012.

## L010 — provider record IDs were mistaken for archival-act boundaries

Observed failure: `stat_visitation_00000197` and `stat_visitation_00000235` were initially represented as two Reg. Ii 3 archival records because DigiRef exposes separate record identifiers. Owner-supplied archival identification plus Archivportal context showed that *Visitation in Neustadt an der Orla* (41r–63v) and *Pfarreinkommen Gössitz, Knau …* (303r–306r) are two protocol/source units within the same parent act `ThHStAW, EGA, Reg. Ii 3 — Visitation in Jena, Neustadt an der Orla, Pößneck, Saalfeld`. The same review showed that Reg. Ii 4 Bd. II and Reg. Ii 5 need parent-act titles above their Ziegenrück protocol records.

Corrective practice: determine archival granularity independently of provider-record granularity. Model parent acts in `corpus/sources.tsv`, bounded reusable protocols in `corpus/source-units.tsv`, and retain provider IDs/URLs at the level they actually identify. Never create a second parent act solely because a portal exposes a second record ID.

Generalizable: yes; promoted into source/provenance method, project lifecycle, AGENTS guardrails and source-contract validation.
