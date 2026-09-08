# LEARNINGS — Reg. Ii 5 / legacy Knau scope

This file records project-specific lessons. It is not evidence for manuscript readings.

Cross-project synthesis: `requirements/source-context-model-synthesis-2026-09-07.md`.

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

## L014 — evidence provenance must be claim/artifact-level, not directory-level

Observed failure: after the Reg. Ii 4/Reg. Ii 5 witness separation was clarified, the safest immediate reaction was to quarantine the historical Knau/G2 material under this legacy path. That was correct for the old diplomatic rows and witness-dependent apparatus where attribution could not be trusted from path/page labels alone. However, the same directory later contains `g2-baseline-provenance.md` and `g2-checkpoint-a-physical-inventory.md`, whose evidence chain is independently exact and explicitly Reg. Ii 5.

Corrective practice: determine scientific authority from the concrete artifact/claim’s Source/File/locus provenance and evidence class. A path can explain history; it cannot establish or revoke witness identity by itself.

Generalizable: yes.

## L015 — protective quarantine must be as narrow as the uncertainty

Observed failure/risk: `research/legacy-witness-provenance.tsv` currently contains a wildcard classification for `research/g2-*`. This safely prevents overpromotion but also catches later exact-source direct-image G2 artifacts whose witness provenance is actually established.

Corrective practice: quarantine only the claims/artifacts that inherit unresolved witness provenance. Preserve later directly established evidence at the level it actually supports, without using that fact to promote older readings.

Generalizable: yes.

## L016 — physical/source-order observation and diplomatic reading are different evidential layers

Direct Reg. Ii 5 Checkpoint-A inspection securely established physical order/layout and phenomena such as the 61v accounting/list block and cancellations at 61v-L16 and 62r-L18. It did not thereby validate the old diplomatic text row-by-row.

Corrective practice: preserve direct source observation, diplomatic reading, source phenomenon, editorial expansion/supply, normalization and interpretation as separable layers with their own evidence status.

Generalizable: yes; aligned with existing palaeographic/editorial requirements.

## L017 — research-ready access is distinct from identity and reproducibility

Observed failure: an exact File ID/SHA and a reproducible render recipe can exist while a fresh research context still cannot open the actual pixels. Conversely, an accessible derivative is not automatically a fresh byte-level verification of the canonical parent.

Corrective practice: distinguish evidence identifiability, reproducibility and current authorized research-ready accessibility.

Generalizable: yes; this is the core fixture behind #68/#78.

## L018 — source-specific addressing needs must not become a universal manuscript ontology

The real 61v–63r G2 work demonstrates that physical Line is necessary for this source and that finer line-local targeting is sometimes required. It does not establish that every future Source must be represented as folio→line→span.

Corrective practice: require unambiguous recoverable targets at the granularity justified by the source/claim, while letting different source types use different physical/logical structures.

Generalizable: yes.

## L019 — text identity was stabilized before witness identity

Observed failure: the earliest Knau working transcription was persisted from an accumulated chat/reading state before every diplomatic reading had exact Source/File/locus witness provenance. The initial benchmark stabilized working images `132–135` as one Knau text and only afterwards reconstructed their archival source identity. A historical intermediate correction even attached that working text to the wrong Reg.-Ii.-5 provider record `stat_visitation_00000128`; Reg. Ii 4 Bd. II was then localized independently as a separate parallel witness.

Because the already accumulated Knau text could contain direct readings, later re-readings and comparison-witness knowledge from different work phases, neither the legacy project path nor `page_id` values `132–135` can establish witness attribution for an individual diplomatic reading. `Potentially mixed` therefore describes unresolved reading provenance, not a claim that every legacy row literally combines both witnesses.

Corrective practice: establish target witness identity and exact Source/File/locus provenance before promoting diplomatic readings. Textual similarity, project path, export-image label or a previous synthesized transcription must never be used to infer witness provenance. Preserve legacy readings and uncertainty as recovery/checking evidence, but re-establish any reading that is to regain scientific witness authority directly against the target Source/File/locus.

Generalizable: yes. **Textual identity or correspondence is not witness provenance.**
