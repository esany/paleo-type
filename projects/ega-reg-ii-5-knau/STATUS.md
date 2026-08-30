# STATUS — ThHStAW, EGA, Reg. Ii 5

Last checkpoint: 2026-08-30

## Historical project root

This project is anchored to the historically independent source structure `ACT-THHSTAW-EGA-REG-II-5` — *Registratur für die Superintendenz Neustadt an der Orla (Auszug)* — via `project.yml: project_source_id`.

The current Knau work is a bounded research scope inside that project root; it does not define the project boundary.

Generic scholarly method is defined in `../../methodology/historical-source-workflow.md`; reusable maturity requirements are in `../../methodology/research-gates.md`; diplomatic requirements are in `../../methodology/transcription-guidelines.md`.

## Research purpose and active scope

Produce a source-exact, critically controlled scholarly edition and historical understanding of the relevant material within Reg. Ii 5. The active diplomatic focus is the Knau passage at fol. 61v–63r inside the Ziegenrück protocol fol. 55v–66v.

## Sources used

The project uses four canonical protocol/source records. Structural membership is derived from `corpus/relationships.tsv` `part_of` relations, not from project roles.

- **internal / principal** — `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`: *Visitation im Amt Ziegenrück*, fol. 55v–66v, structurally inside `ACT-THHSTAW-EGA-REG-II-5`. Principal Knau locus: fol. 61v–63r / export images 132–135.
- **external / comparison** — `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089`: *Visitation im Amt Ziegenrück*, fol. 294r–313r, structurally inside `ACT-THHSTAW-EGA-REG-II-4-BD-II`. Corresponding Knau locus: fol. 306v–309r / export images 667–672.
- **external / context** — `THHSTAW-EGA-REG-II-3-PROT-NEUSTADT-41R-63V`: *Visitation in Neustadt an der Orla*, fol. 41r–63v, structurally inside `ACT-THHSTAW-EGA-REG-II-3`. Exact supplied range: 1529-05-23 to 1529-06-01; supplied calendar label `gregorian`; supplied serial values 2279668–2279677.
- **external / control** — `THHSTAW-EGA-REG-II-3-STAT-VIS-00000235`: *Pfarreinkommen Gössitz, Knau (mit Laskau, Bahren), Liebschütz (mit Liebengrün)*, fol. 303r–306r, structurally inside the same Reg. Ii 3 act. Includes `Knaw Kirch Einkommen` on fol. 304r / export image 625.

The project source register records research function and relevant locus only. The resolver derives whether each source is internal or external from its `part_of` ancestry relative to `ACT-THHSTAW-EGA-REG-II-5`.

## Digital addressing state

- Reg. Ii 4 Bd. II / Knau 306v–309r: exact folio↔export-image↔PDF-page mapping **and stable per-image URNs recorded**.
- Reg. Ii 5 / protocol 55v–66v: folio↔export-image↔PDF-page mapping recorded. Stable per-image URNs are **not established** from the inspected export and must not be inferred. For active fol. 61v–63r, directly observed provider derivative/TIFF labels are recorded in the Source crosswalk: `stat_derivate_00000416:/ThHStAW_RegIi_5_0130.tif` through `_0133.tif`.
- Reg. Ii 5 exact parent export: local File `FILE-REG-II-5-00000129-EXCERPT`; provider file object `stat_file_00000033` is directly evidenced on the export metadata page and remains distinct from Source/provider record `stat_visitation_00000129`.
- Reg. Ii 3 / Pfarreinkommen 303r–306r: folio↔export-image↔PDF-page mapping recorded; stable per-image URNs are **not yet recorded**.
- Reg. Ii 3 / Neustadt 41r–63v: exact protocol extent and inspected export identity are known, but a canonical folio↔export-image/PDF-page crosswalk has **not yet been reconstructed** in the repo.

Crosswalks are source-level. Adjacent pages present in an export but outside an evidenced source boundary are not silently assigned to that source.

For the active G2 slice, the exact parent File was again supplied and SHA-256 verified on 2026-08-30. Unprocessed baselines for fol. 61v–63r were re-rendered from canonical PDF pages 14–17 and reproduced the earlier Poppler working-set fingerprints exactly. Durable derivation/recovery provenance is recorded in `research/g2-baseline-provenance.md`.

## Original-export preservation / availability state

The exact four central archive-export PDFs used for this project are checksum-verified against `corpus/files.tsv`:

- `1a03ea95927-120-143.pdf` — SHA-256 `e989fe614c715e417e3586e29628d67d274964f195b3f1e66a8682bfcde54f6f`;
- `1a03e6fca87-642-681.pdf` — SHA-256 `dc61e65822a34b84c9d88e57690609bbea6eb4537a9efc00294d1520f8f3b86f`;
- `1529-Visitationsprotkolle-ThHStAW-EGA-Reg. Ii 3-Neustadt-O-p41r-63v.pdf` — SHA-256 `451bb32b0bca077c4089966594e2bf234b39e87d9e087d3c1c2e2a569f31fd12`;
- `1529-Visitationsprotkolle-ThHStAW-EGA-Reg. Ii 3-303-306.pdf` — SHA-256 `963a29eff5cc98bb35cecc28e20c6ed3fcb835261e322f991e42b60662d54c06`.

These PDFs are central research assets, not replaceable by identifiers. The repository is now **private**. On 2026-08-30 the human project owner explicitly authorized controlled storage of the Reg. Ii 5 source in this private project repository. This authorizes the intended private research-storage use; it does not assert a public redistribution right for the `InC/1.0` archive export.

The canonical Reg. Ii 5 parent-binary target is recorded in `corpus/files.tsv`:

`corpus/source-files/THHSTAW-EGA-REG-II-5-STAT-VIS-00000129/original/1a03ea95927-120-143.pdf`

A control README exists in that directory, but the exact parent PDF binary is **not yet verified present at the target path**. Consequently the File must not be marked `repo-preserved` until byte presence and SHA-256 are verified. This is a preservation item, not a blocker for the active fol. 61v–63r research slice.

For active visual research, four unprocessed baseline images are attached to private Issue #84. A fresh authorized connector retrieval from a newly fetched `private-user-images` attachment URL succeeded on 2026-08-30. This demonstrates that the Issue-attachment route can restore actual inspectable pixels to a fresh connected work context. The attachment route is therefore the current research-ready visual-access carrier for fol. 61v–63r. The four attachment bytes have **not** been separately re-hashed as a new acceptance condition; their historical baseline fingerprints remain the locally reproduced Poppler fixture fingerprints recorded in `research/g2-baseline-provenance.md`.

Current state:

```text
exact parent identity / SHA                                      PASS
canonical folio↔image↔PDF mapping                               PASS
reproducible baseline derivation                                PASS
controlled private storage authority                            PASS
private #84 baseline attachments present                        PASS
fresh-context visual retrieval route via private #84 attachment PASS (tested 2026-08-30)
exact parent binary committed + SHA reverified in repo           PENDING — preservation only, nonblocking
```

Thus **research-ready visual availability for the active fol. 61v–63r slice is PASS**. Exact parent-PDF repository preservation remains a distinct open preservation task. Identifier/path/recipe alone would still be insufficient if the private image-access route ceased to work.

## Generic gate state

- **G1 — Source and transmission basis secured:** substantially reached. For Reg. Ii 5, controlled private storage is authorized and the active fol. 61v–63r images have a tested fresh-context retrieval route; exact parent-PDF repository preservation remains pending as a nonblocking preservation item.
- **G2 — Principal witness completely and diplomatically represented:** **ACTIVE — not reached. Checkpoint A has passed and Checkpoint B source-bound semantic-loss mapping is sufficiently complete for #73 Domain Review; final G2 information/representation consequences are not yet classified.**
- **G3 — Internal palaeographic and notational analysis completed:** not reached.
- **G4 — Comparison witnesses/controls independently assessed and collated:** not reached.
- **G5 — Critically consolidated and proportionally validated text state:** not reached.
- **G6 — Scholarly edition produced and quality-controlled:** final goal, not reached.

## Existing text checkpoint

The existing `transcription/132.tsv`–`135.tsv` files are legacy working transcription data, not yet the final G2-compliant representation. Controlled anchors include `Knawe` on fol. 61v, closing Knau lines on fol. 63r, repeated `wolff von`, Arabic `1`, and twice-reinspected Arabic `80` on fol. 62r. Known representation gaps remain especially W1–W6/U1–U2 on 61v, the upper economic passage/U3–U5 on 62r, and substantial multi-line gaps on 62v.

G2 does **not** require every difficult token to be resolved.

## Active G2 project gaps

1. **Checkpoint A — PASS:** physical/source-order anchors, broad layout and observed baseline-level phenomenon classes for all four folia are persisted and were visually re-validated against the recovered exact baselines on 2026-08-30. No missed/doubled/reordered target line or spatial-stream correction was required.
2. **Checkpoint B — SOURCE RESEARCH COMPLETE ENOUGH FOR HANDOFF:** source-bound legacy/apparatus mapping and semantic-loss/non-loss findings are persisted in `research/g2-checkpoint-b-semantic-loss.md`; mappings remain `partial`, `ambiguous` or `unresolved` where exactness is not supported rather than being guessed.
3. **Domain Review — active next step:** #73 must classify the persisted findings as source-local/project/generic-method/deterministic-system/specialist/no-action or needs-further-evidence, using existing REQ-* first.
4. smallest source-evidenced G2 representation only after #73 classification and any returned evidence work;
5. derived human-readable diplomatic witness view after the required information is settled;
6. full representation-completeness and transition/decision falsification across fol. 61v–63r after classification/representation work is admitted.

## Current Checkpoint A research state

The durable working inventory records:

| folio | provisional physical-line anchors | broad visible structure | structural review |
|---|---|---|---|
| 61v | `61v-L01`…`L20` | display heading → two-line introduction → spatially organized list/accounting-like block → two prose paragraphs | PASS |
| 62r | `62r-L01`…`L25` | three visually distinct prose paragraphs | PASS |
| 62v | `62v-L01`…`L25` | three prose paragraphs, including a longer middle block | PASS |
| 63r | `63r-L01`…`L11` | three-line continuation → display heading → new prose paragraph | PASS |

Baseline-level phenomenon inspection establishes, without reconstructing uncertain text:

- 61v differs materially in layout from the following folia; its left quantity/sign notation belongs provisionally to the list block rather than an independent marginal stream;
- recurrent abbreviation marks are visible on all four folia;
- numeral/special-sign handling is empirically relevant: spatial quantity/sign notation occurs on 61v and Arabic `80` is visible on 62r and 62v;
- visible cancellation/deletion phenomena occur at least at `61v-L16` and `62r-L18`; deleted readings/replacement relations remain unresolved at this checkpoint;
- no separate marginal/interlinear text stream is established at baseline level;
- faint show-through is visible on 63r but has not been shown to obscure target text;
- hand differentiation remains `not investigated`;
- visible edge wear has not been shown to cause target-text loss.

These anchors are review fixtures, not a canonical G2 Line ontology. The structural PASS does not decide difficult readings, hand attribution, expansion or final storage semantics.

## Current Checkpoint B research state

Durable Source Research fixture:

`research/g2-checkpoint-b-semantic-loss.md`

Material source-bound findings now demonstrated for downstream review include:

- legacy row segmentation is not physical manuscript lineation; multi-line collapse is demonstrated on 61v, 62r and 62v;
- the eight-line spatial list on 61v cannot be reconstructed one-to-one from six legacy list rows, although W1–W6 uncertainty survives;
- confirmed cancellations at `61v-L16` and `62r-L18` are absent as explicit source phenomena from the current legacy transcription;
- the source-visible Arabic `80` at `62v-L01` is not explicitly localized in current 62v legacy/palaeographic records;
- `63r-L05–L11` are validated physical text lines with no coverage in `135.tsv`;
- D001–D011 preserve materially useful rejection/variant/observation history, but several legacy target strings are too coarse or ambiguous to recover exact physical targets without re-localization;
- legacy “same-hand” wording is not promoted because hand differentiation remains `not investigated`;
- positive non-results are recorded, including adequate `63r-L01–L03`, preserved unresolved/rejected states, preserved 62r `80`, and no demonstrated textual consequence from 63r show-through.

The fixture explicitly stops before deciding whether any finding is source-local, project-level, generic methodological, deterministic/system, specialist-review, or no-action. That classification belongs to #73.

## NEXT ACTION — canonical restart point

Proceed to **#73 Domain Review of the persisted Checkpoint-B fixture**. Do **not** begin G2 schema design or Dev work.

1. load `research/g2-checkpoint-b-semantic-loss.md` together with Checkpoint A, current `STATUS.md`, #64, #72 and applicable REQ-*;
2. review each material source-bound finding against existing requirements and current canonical support;
3. classify each as source-local, project consequence, generic scholarly/methodological requirement, deterministic research-system requirement, specialist-review requirement, no additional action, or `needs further evidence`;
4. where `needs further evidence`, return an exact source-research question/anchor to #72/#64 rather than guessing or designing around uncertainty;
5. preserve the positive non-results and existing apparatus history; do not make every manuscript phenomenon a system requirement;
6. only if #73 establishes a real reusable representational/deterministic gap may a later bounded Dev handoff be prepared through the defined scholarly→Dev path;
7. no G2 migration/implementation is authorized merely because Checkpoint B is complete enough for review.

Exact parent-PDF repository preservation may proceed independently under #68 and must not displace or block the scholarly next action.

Do not let external comparison-source work displace this active G2 task.

## Human-in-the-loop state

The user must be able to inspect source images and research-facing results without understanding internal TSV architecture. The non-specialist owner is **not** required to validate palaeographic readings or perform the Source Research or Domain Review role.

Checkpoint A source↔anchor review and Checkpoint B mapping are AI-assisted Source Research under #72, not independent specialist validation. Human challengeability remains available through the visible image→anchor→research finding→later witness/evidence path.

No independent qualified palaeographic expert review of the full Knau transcription has yet been recorded.

## Restartability test

A new capable researcher/agent must be able to determine from repository + controlled sources: the historical project root `ACT-THHSTAW-EGA-REG-II-5`, which used sources are internal versus external, exact exports/preservation/access state, available/missing provider identifiers and URNs, the G2 baseline derivation/fingerprints, the Checkpoint-A physical/source-order inventory and PASS status, Checkpoint-B source mappings/loss and non-loss findings, active gate, remaining G2 gaps and exact next action without old chat.

Current durable restart path:

- exact parent/file rights, storage authority and provider-file state → `corpus/files.tsv`;
- intended private parent-binary location + expected SHA → `corpus/source-files/THHSTAW-EGA-REG-II-5-STAT-VIS-00000129/original/README.md`;
- canonical folio↔image↔PDF mapping + observed provider image locators → Source crosswalk;
- baseline derivation + recovered fingerprints + tested private-attachment access distinction → `research/g2-baseline-provenance.md`;
- actual private visual working images → Issue #84 attachments; fresh retrieval route tested 2026-08-30;
- inspection events → `sources/inspection-log.tsv`;
- Checkpoint-A source-order fixture and structural PASS → `research/g2-checkpoint-a-physical-inventory.md`;
- Checkpoint-B mapping/loss/non-loss evidence → `research/g2-checkpoint-b-semantic-loss.md`;
- active consequence/next action → this `STATUS.md`;
- generic evidence-availability derivation → #78; operational source-access/preservation owner → #68.

For the active fol. 61v–63r slice, a fresh connected authorized work context can recover actual image pixels from #84 rather than depending on the old chat. Exact parent-PDF repository preservation remains a separate, still-open preservation task and must not be confused with the already-passed visual-access gate or the completed-enough Checkpoint-B Source Research handoff.