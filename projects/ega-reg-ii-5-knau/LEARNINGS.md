# LEARNINGS — Reg. Ii 5 / legacy Knau scope

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

Corrective practice: explicit source/evidence status and passage-level audit.

Generalizable: yes.

## L006 — repeated AI readings are not independent confirmation

Observed issue: multiple model passes can reproduce the same contextual bias.

Corrective practice: treat repeated model output as one reader unless the evidence source changes.

Generalizable: yes.

## L007 — the project must preserve a restart point

Observed failure: chat-based work repeatedly revisited method and lost the exact next task.

Corrective practice: durable work state must remain inspectable without old chat.

Generalizable: yes.

## L008 — the pilot was allowed to define generic method

Observed failure: generic scholarly gate requirements and parts of the method were copied into the Knau working area and mixed with source-specific facts.

Corrective practice: generic method/gates live in `methodology/`; concrete research state remains project-local and is generalized only after an explicit check.

Generalizable: yes.

## L009 — protocol-level source wrappers were mistaken for projects

Observed failure: PR #40 created `source-unit` projects for individual protocol/source records mainly to give source-wide crosswalks one owner. This confused documentary components with Projects.

Corrective practice: reusable Source identity/crosswalk/File provenance remains in `corpus/`; internal protocol/section nodes remain Sources related by `part_of`.

Generalizable: yes.

## L010 — provider record IDs and one hierarchy were mistaken for the data model

Observed failure: provider/DigiRef identifiers and one observed act→protocol arrangement were repeatedly over-promoted into model semantics.

Corrective practice: determine Source granularity from evidence; represent needed historical/documentary nodes independently and containment generically via `part_of`.

Generalizable: yes.

## L011 — AI-organized research scope was mistaken for Project identity

Observed failure: the repository first created `ega-reg-ii-5-knau` as a Knau benchmark/research scope. That organization was AI-generated, not a human-owner decision defining a Project. Later corrections changed the technical theory of what a Project should be, but still treated the inherited Knau scope as if it supplied owner-grounded Project purpose.

Corrective practice: **Project existence and boundary are human-owner decisions.** Once a Project is chosen, `project_source_id` anchors it to canonical Source structure and `part_of` may derive internal membership. Source structure itself does not create a Project, and an inherited AI scope is not owner authority merely because it has become canonical.

Current owner correction: for the church-visitation material the Projects are Reg. Ii 3, Reg. Ii 4 Bd. II and Reg. Ii 5 at act level. Knau is an initial/historical research focus inside them and further sections may be added.

Generalizable: yes; this refines the interpretation of D-014 rather than rejecting structural Source anchoring.

## L012 — correct Source/File identity can coexist with scope/priority drift

Observed failure: File/Source identity checks correctly distinguished Reg. Ii 4 Bd. II from Reg. Ii 5, but correct technical routing did not test whether the surrounding Project definition, active scope or subsequent priority had human-owner authority. Later fresh contexts therefore reproduced an internally consistent AI-created Knau/Reg. Ii 5 narrative.

A further attempted correction incorrectly inferred from the existence of earlier Reg. Ii 4 comparison material that detailed Reg. Ii 4 collation should now become the owner-grounded current task. That was another unsupported priority inference.

Corrective practice: keep Source/File identity, Project existence/boundary, structural membership, project-relative research functions, bounded strand-local next steps and Project-wide current priority distinct. Correct bytes or a valid old `next_step` do not establish present owner priority. If owner grounding for the next task is absent, record that absence rather than choosing the most plausible historical cursor.

Generalizable: yes.

## L013 — project-model migration removed a useful work-state audit surface

Observed failure: the temporary source-unit Projects preserved separate STATUS records for Li 3 sections, Li 4 and Li 5, including evidence limits, dormant/activation state and restart instructions. When those source-as-project directories were removed, reusable Source/File/crosswalk facts were largely migrated to `corpus/`, but the work-state/checkpoint surface was not equivalently preserved in the new Project structure.

Consequence: Git history still contained the old state, so evidence was not destroyed; however it stopped functioning as an ordinary visible Prüfinstanz on `main`. This made later AI-created Project narratives harder to falsify against earlier working state.

Corrective practice: structural migrations must perform a semantic-loss check not only for Source/File/research rows but also for consequential work-state/restartability information. Historical state may remain non-canonical, but a current audit pointer must make it discoverable without archaeological Git reconstruction.

Current repair: `projects/README.md` records the recovery snapshot and deletion sequence; owner-defined Li 3 and Li 4 Projects expose recovered prior state in their STATUS files; this Reg. Ii 5 STATUS does the same without reviving source-as-project semantics.

Generalizable: yes.
