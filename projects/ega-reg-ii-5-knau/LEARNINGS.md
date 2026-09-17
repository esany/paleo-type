# LEARNINGS — Reg. Ii 5 / legacy Knau scope

This file records project-specific lessons. It is not evidence for manuscript readings.

Cross-project synthesis: `requirements/source-context-model-synthesis-2026-09-07.md`.

## L001 — whole-word silhouette guessing caused major errors

Observed failure: early readings such as `welch` versus later `wolff`, and other fluent-looking words, were produced before enough same-hand grapheme evidence existed.

Corrective practice: prefer local grapheme comparison and repeated same-hand forms. Do not promote a word because its silhouette and syntax look plausible.

**Current qualification (2026-09-08):** Repeated forms are admissible comparanda only when they are exactly localized and graphically relevant to the target question. Occurrence in the same Source, record or textual environment is not same-hand evidence. Treat a comparison as same-hand evidence only after hand identity has been independently established.

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

**Current qualification (2026-09-08):** The underlying need for graphical/notational comparison remains valid, but the current method is target-problem-driven rather than concordance-driven. Localize a consequential unresolved sign or graph first, formulate the discriminating question, and only then seek exactly located relevant comparanda. Do not build or extend a concordance merely because similar forms exist. `palaeography/*` is not a current witness-reading owner; legacy entries retain only the authority assigned in `research/legacy-witness-provenance.tsv`.

Generalizable: likely; the historical artifact-first implementation is retained here as a lesson, not as the current workflow.

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

## L020 — legacy artifact topology can reactivate a superseded method

Observed risk: even after the scientific authority of old material was narrowed, directory names and historical learning language such as `palaeography/`, `lexicon.tsv`, `numerals.tsv`, `apparatus/`, “same-hand forms” and “concordance” can still make an earlier artifact-first workflow look like the current research architecture. A capable fresh context can therefore be pulled back toward building or extending repertories even though current method requires a concrete target problem first.

Corrective practice: retain historical/recovery artifacts, but make their current epistemic role visible at the directory entry point and qualify superseded recommendations in place rather than rewriting the historical record. Path, filename or historical usefulness does not confer current-owner authority. New comparison work starts from a localized unresolved target and exact evidence question; auxiliary structures are created only on demonstrated semantic-loss or recurring-use need.

Generalizable: yes as a restartability/maintenance failure pattern; the present repair remains Project-local because generic canonical-ownership and restartability rules already exist.

## L021 — a correspondence range is not automatically an analysis unit

Observed failure: the first #165 correction correctly rejected a premature functional split between `62r-L19–25` and `62v-L01–07`, but then promoted the larger G4-008 cross-witness correspondence range into one Reg. Ii 5 `cross-folio unit`. Direct Reg. Ii 5 G2 observation instead records two adjacent paragraph blocks, while G4 explicitly records resegmentation across the witnesses.

Corrective practice: keep **source address / directly observed layout block / cross-witness correspondence range / analysis unit / functional rule** distinct. A comparison mapping may challenge a functional interpretation and generate a new source-side test; it does not itself establish the target witness's text-unit structure.

For the current A1 region the defensible question is how the two observed paragraph blocks relate, not how one pre-established unit is internally segmented.

Generalizable: likely. The generic method already contains the needed S2/S3/S4 distinctions, so the present repair is Project-state/activation correction rather than a new METHOD family.

## L022 — the analysis unit itself must remain falsifiable

Observed failure: after #161 demonstrated the value of a higher-level pass, the corrective process risked turning that success into an implicit `larger unit = better analysis` heuristic. #165 is the counterexample: higher-level synthesis can over-group just as microanalysis can over-atomize.

Corrective practice: fix the **research address** when needed, but treat the **analysis unit** as a hypothesis until source evidence establishes it. Choose the smallest source-evidenced observation frame capable of answering the research question; enlarge or split only when evidence, not routing convenience, supports that move.

A good source-understanding question may therefore have multiple legitimate terminal models (`one overarching rule`, `two coupled rules`, `unresolved relation`) rather than requiring one preferred segmentation.

Generalizable: yes as a research-selection/activation lesson; no new schema or gate is implied.

## L023 — independent review can inherit the same derived premise

Observed failure: the #171 independent review freshly rehydrated several relevant owners and correctly warned against `larger unit = better analysis`, yet still repeated the phrase that #165 had `restored the cross-folio unit`. Its explicit review basis did not descend to the direct Reg. Ii 5 G2 structural owner that made the two observed paragraph blocks visible.

Corrective practice: independence of **context** is not independence of **evidence basis**. When a consequential dispute concerns source structure, witness identity, segmentation or another lower-level claim, review must trace the contested premise back to the strongest direct owner/evidence layer rather than only compare later syntheses/issues that may share the same inherited assumption.

This does not require every review to reperform all source work. It requires enough premise tracing to know which lower-level claim the review is actually accepting rather than testing.

Generalizable: yes; consistent with D-004/D-019 and existing evidence-first review principles.

## L024 — execution-economy fixes do not validate the scholarly scope they protect

Observed failure/risk: #169 correctly identified support-dominance during #166 execution and added useful first-scholarly-action / support-delta controls. The later whole-repository review shows that the #166 scope itself still contained an over-strong analysis-unit premise.

Corrective practice: keep **scope correctness** and **execution economy** as separate review questions. A workflow can efficiently protect or preflight a scope that is still scientifically biased. Conversely, a good research question can still be buried under support work.

Current consequence: retain #169's execution-economy lesson, but do not use its passed #166 backtest as evidence that the old `one cross-folio unit` framing was scientifically correct.

Generalizable: yes; this sharpens the meaning of technical/process backtests without requiring another METHOD change.

## L025 — resource state was laundered into task and roadmap authority

Observed failure: during #166, absence of the Reg. Ii 5 parent PDF / p15-p16 pixels in the current execution context was first recorded as an access/readiness fact, then promoted to `REAL BLOCKER`, then to `#166 not executable`, and finally to canonical `STOP until evidence changes`. No independent canonical task owner had established that this resource state should carry those task-wide and roadmap consequences.

This created a particularly dangerous failure chain because later maintenance, tests and restart-state synchronization made the inferred dependency internally consistent and durable.

Corrective practice: keep **resource/capability state**, **explicit action dependency**, **task-level blocker state**, and **Project/roadmap authority** separate. When a PDF, scan, attachment, credential or tool capability is unavailable, report the missing resource and the specific action affected immediately. Before deriving `BLOCKED`, `STOP`, `NEXT ACTION`, roadmap dependency or substitute work, identify the canonical/explicit authority that establishes that dependency and consequence. If that authority is absent, preserve only the action-local limitation and surface any planning ambiguity to the Human Owner.

Evidence discipline remains strict: an action that really requires missing pixels cannot be simulated from metadata, prior transcription or a parallel witness. The correction limits the *scope of the consequence*; it does not weaken evidence requirements.

Generalizable: yes. **Resource availability is descriptive execution state, not task or roadmap authority.**

## L026 — direction formation exposed a Project-purpose recoverability gap

Observed failure: the first real post-D-020 direction-formation pass produced a serious but strongly local candidate surface whose main directions substantially reproduced the already rich Reg. Ii 5 / Knau–Ziegenrück fixture explored in #191. The individual candidate questions were not thereby invalid, but the pass could not demonstrate that the candidate set represented the scientifically relevant space of the owner-established Reg. Ii 5 Project rather than the most richly addressable current research state.

The current Project authority is real: Reg. Ii 5 is an owner-established act-level Project and `Knau` is not its boundary. However, `project.yml` currently represents the substantive `research_object` only as `Source-based scholarly research within Reg. Ii 5`, while `active_scope` is explicitly unset. That is sufficient to recover Project identity/boundary and the absence of a current task, but not sufficiently discriminating for the additional operation of grounding broad next-direction formation against a substantive Project purpose.

Corrective practice: when pre-priority direction formation needs a substantive Project-purpose discriminator, first verify that the needed purpose meaning is recoverable from its canonical owner. If it is not, return the purpose/authority gap to the Human Owner rather than allowing the richest available evidence, Source group, unresolved locus, gate or prior fixture to substitute for the missing discriminator. Keep stable Project purpose, iterative scholarly maturity, current scope and `NEXT ACTION` separate.

Current consequence: the recent R1–R5/A–D candidate sets remain potentially useful research material but are **not yet validated as a Project-wide decision surface**. `NEXT ACTION = NONE` remains correct. This single real-use case is evidence to observe; it does not by itself satisfy #202's recurring-mechanism reactivation trigger.

Generalizable: not yet established. Preserve this as Project/pilot evidence first; apply Generic-Fit before any METHOD or #202 consequence.

## L027 — pilot material must not become the purpose of the generic system

Observed failure/risk: because Reg. Ii 5 / Ziegenrück / Knau is the richest worked fixture, successive attempts to repair research framing repeatedly risked letting this material define the generic problem, candidate space or implied system purpose. This repeats the older L008 pattern at a higher level: a useful pilot can become a hidden model of what the whole system is for.

Corrective practice: keep **repository mission**, **Project purpose**, **pilot/fixture evidence**, **current scholarly scope** and **source-local research findings** distinct. Real pilot scholarship should remain scientifically serious, but neither its Source structure nor its currently visible questions may silently define generic `paleo-type` purpose, universal research direction or workflow architecture.

Current consequence: Reg. Ii 5 remains the present pilot/application context, not the definition of the generic system. No Governing Objective amendment follows from this learning; any mission-level change remains a separate explicit Human-Owner governance decision.

Generalizable: likely as a pilot-design risk and already partly covered by existing generic/pilot separation; no new generic rule is admitted here.

## L028 — support dominance is a secondary symptom when AI/recovery fails

Observed failure pattern: support work became prominent after the AI/work context encountered real evidence, access, capability, premise or execution problems. The immediate support need was often legitimate. The damaging loop arose when repairing the local failure expanded into further support, assurance, status or governance work and the valid scholarly cursor did not regain primacy.

This means `support dominance` is not necessarily the root cause of the stalled scholarship. In the present pilot it can be a **secondary symptom of insufficient robustness/recovery of AI-assisted research**: the system detects or encounters a problem, but does not reliably repair the bounded failure and resume source work.

Corrective practice: treat direct scholarship as the normal path and support as bounded exception handling. On failure, identify the exact affected action, preserve evidence/authority limits, perform only the smallest authorized repair, then return to the last valid scholarly cursor. Additional assurance/support must justify itself by a concrete unresolved consequence; support success must not become a substitute research objective.

Current consequence: retain the useful A8/#169 support-dominance safeguards, but diagnose upstream AI/evidence/capability/recovery failures separately. Do not infer from this one pilot that a new generic recovery architecture is required.

Generalizable: plausible but not yet demonstrated broadly; keep Project-specific pending Generic-Fit.

## L029 — pilot quality must preserve scientific capability as well as reliability

Observed concern: the repository has substantially strengthened evidence discipline, authority separation, persistence, reviewability and restartability, while the Human Owner reports that the initial pre-repository chat may have achieved more direct scholarly/source-understanding progress than the current highly controlled pilot. The old chat is not evidence authority and this performance comparison has not yet been independently benchmarked, but the present work history does demonstrate long stretches of meta/support/system work with limited new source scholarship.

Risk: a pilot can improve epistemic safety and auditability while unintentionally reducing the AI-assisted system's ability to make timely, substantive scholarly progress. Such a system would be safer but not yet a successful research assistant.

Corrective practice: evaluate the pilot on separate dimensions rather than treating process maturity as overall success: **scientific/source-understanding capability**, **epistemic reliability**, **human auditability/restartability**, and **research overhead/recovery cost**. The desirable target is not to reproduce the informal chat's errors; it is to retain or improve its useful scholarly capabilities while preventing the demonstrated failures and making consequential results recoverable.

A historical chat may therefore serve as a non-authoritative **performance/functional benchmark** for capabilities it exhibited, never as canonical research truth. Any formal benchmark or generic acceptance criterion requires its own evidence and Generic-Fit rather than being created by this learning alone.

Generalizable: not yet established; this is a pilot-evaluation hypothesis grounded in the observed Reg. Ii 5 work history and Human-Owner experience.