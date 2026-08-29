# STATUS — ThHStAW, EGA, Reg. Ii 5

Last checkpoint: 2026-08-29

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
- Reg. Ii 5 / protocol 55v–66v: folio↔export-image↔PDF-page mapping recorded; stable per-image URNs are **not yet recorded** and must not be inferred from neighboring identifiers.
- Reg. Ii 3 / Pfarreinkommen 303r–306r: folio↔export-image↔PDF-page mapping recorded; stable per-image URNs are **not yet recorded**.
- Reg. Ii 3 / Neustadt 41r–63v: exact protocol extent and inspected export identity are known, but a canonical folio↔export-image/PDF-page crosswalk has **not yet been reconstructed** in the repo.

Crosswalks are source-level. Adjacent pages present in an export but outside an evidenced source boundary are not silently assigned to that source.

For the active G2 slice, the exact parent File was re-verified on 2026-08-29 and unprocessed baselines for fol. 61v–63r were rendered from canonical PDF pages 14–17. Durable reproduction/provenance is recorded in `research/g2-baseline-provenance.md`; project inspection state is recorded in `sources/inspection-log.tsv`.

## Original-export preservation state

The exact four central archive-export PDFs used for this project are checksum-verified against `corpus/files.tsv`:

- `1a03ea95927-120-143.pdf` — SHA-256 `e989fe614c715e417e3586e29628d67d274964f195b3f1e66a8682bfcde54f6f`;
- `1a03e6fca87-642-681.pdf` — SHA-256 `dc61e65822a34b84c9d88e57690609bbea6eb4537a9efc00294d1520f8f3b86f`;
- `1529-Visitationsprotkolle-ThHStAW-EGA-Reg. Ii 3-Neustadt-O-p41r-63v.pdf` — SHA-256 `451bb32b0bca077c4089966594e2bf234b39e87d9e087d3c1c2e2a569f31fd12`;
- `1529-Visitationsprotkolle-ThHStAW-EGA-Reg. Ii 3-303-306.pdf` — SHA-256 `963a29eff5cc98bb35cecc28e20c6ed3fcb835261e322f991e42b60662d54c06`.

These PDFs are central preservation assets, not replaceable by URNs. The repository is public and the current archive exports are recorded as `InC/1.0`; therefore committing the binary bytes publicly is not treated as authorized by default. Until rights/authority for public redistribution is confirmed, repository preservation is **not complete**.

The same public-redistribution caution applies to the four G2 baseline PNG derivatives. Their provenance is not uncertain, but no additional authority for public GitHub redistribution is documented. They therefore remain a controlled/local research working set when available; an authorized researcher can reconstruct them from the exact parent File and the durable render recipe in `research/g2-baseline-provenance.md`.

Legacy single-image Reg. Ii 5 PDF exports remain separately checksum-tracked for provenance.

## Generic gate state

- **G1 — Source and transmission basis secured:** substantially reached, but repository-local preservation of the central original exports remains a source-preservation gap pending rights resolution.
- **G2 — Principal witness completely and diplomatically represented:** **ACTIVE — not reached. Checkpoint A baseline-level physical/source-order + phenomenon inventory is complete; owner visual review is pending; Checkpoint B has not started.**
- **G3 — Internal palaeographic and notational analysis completed:** not reached.
- **G4 — Comparison witnesses/controls independently assessed and collated:** not reached.
- **G5 — Critically consolidated and proportionally validated text state:** not reached.
- **G6 — Scholarly edition produced and quality-controlled:** final goal, not reached.

## Existing text checkpoint

The existing `transcription/132.tsv`–`135.tsv` files are legacy working transcription data, not yet the final G2-compliant representation. Controlled anchors include `Knawe` on fol. 61v, closing Knau lines on fol. 63r, repeated `wolff von`, Arabic `1`, and twice-reinspected Arabic `80` on fol. 62r. Known representation gaps remain especially W1–W6/U1–U2 on 61v, the upper economic passage/U3–U5 on 62r, and substantial multi-line gaps on 62v.

## Active G2 project gaps

1. **Checkpoint A analytical inventory complete at baseline level:** physical/source-order anchors, broad layout and observed baseline-level phenomenon classes for all four folia are persisted in `research/g2-checkpoint-a-physical-inventory.md`; owner/human visual source↔anchor review remains pending.
2. verified mapping from legacy `132–135` working rows to archival folio/physical-line addresses where possible — **Checkpoint B, not yet started**;
3. explicit loss audit for existing apparatus decisions, W/U/variant/unresolved states and palaeographic/numeral records — **Checkpoint B, not yet started**;
4. smallest source-evidenced G2 representation, only after Checkpoints A and B;
5. derived human-readable diplomatic witness view;
6. full representation-completeness and transition/decision falsification across fol. 61v–63r.

G2 does **not** require every difficult token to be resolved.

## Current Checkpoint A research state

The durable working inventory currently records these provisional human-review anchors:

| folio | provisional physical-line anchors | broad visible structure |
|---|---|---|
| 61v | `61v-L01`…`L20` | display heading → two-line introduction → spatially organized list/accounting-like block → two prose paragraphs |
| 62r | `62r-L01`…`L25` | three visually distinct prose paragraphs |
| 62v | `62v-L01`…`L25` | three prose paragraphs, including a longer middle block |
| 63r | `63r-L01`…`L11` | three-line continuation → new display heading → new prose paragraph |

Baseline-level phenomenon inspection now establishes, without reconstructing uncertain text:

- 61v differs materially in layout from the following folia; its left quantity/sign notation belongs provisionally to the list block rather than an independent marginal stream;
- recurrent abbreviation marks are visible on all four folia;
- numeral/special-sign handling is empirically relevant: spatial quantity/sign notation occurs on 61v and Arabic `80` is visible on 62r and 62v;
- visible cancellation/deletion phenomena occur at least at `61v-L16` and `62r-L18`; deleted readings/replacement relations remain unresolved at this checkpoint;
- no separate marginal/interlinear text stream is established at baseline level;
- faint show-through is visible on 63r but has not been shown to obscure target text;
- hand differentiation remains `not investigated`;
- visible edge wear has not been shown to cause target-text loss.

These anchors are review fixtures, not a canonical G2 Line ontology. Any source↔anchor mismatch found during human visual review must be corrected in the working inventory rather than forcing the manuscript into the provisional numbering.

## NEXT ACTION — canonical restart point

Remain at the Checkpoint-A/Checkpoint-B boundary; do **not** begin G2 schema design:

1. if the local baseline PNG working set is unavailable, use an authorized copy of the exact parent export and reproduce fol. 61v–63r from `research/g2-baseline-provenance.md` after SHA-256 verification;
2. open `research/g2-checkpoint-a-physical-inventory.md` beside the unprocessed baseline images;
3. perform the owner/human visual source↔anchor review: every visible target text line must be findable under the recorded folio/local anchor, and the two recorded cancellation loci must be visibly locatable without requiring the owner to adjudicate their readings;
4. correct any missed/doubled/reordered physical line or misclassified spatial stream before proceeding;
5. if the visual review passes or only explicit unresolved specialist questions remain, begin #64 Checkpoint B against legacy `132.tsv`–`135.tsv`, `apparatus/decisions.tsv` and relevant palaeography/numeral records;
6. do not re-adjudicate manuscript readings merely to make legacy mapping complete, and do not choose a final Line/Span/Phenomenon representation before Checkpoint B evidence exists.

Do not let external comparison-source work displace this active G2 task.

## Human-in-the-loop state

The user must be able to inspect the current diplomatic/source-order work against the manuscript images without understanding internal TSV architecture. The immediate review path is:

`authorized exact parent / reproduced unprocessed baseline → visible physical line/source order → research/g2-checkpoint-a-physical-inventory.md → later diplomatic witness → uncertainty/intervention → evidence/decision drill-down`.

No independent qualified palaeographic expert review of the full Knau transcription has yet been recorded.

## Restartability test

A new capable researcher/agent must be able to determine from repository + preserved/controlled sources: the historical project root `ACT-THHSTAW-EGA-REG-II-5`, which used sources are internal versus external, exact exports/preservation state, available/missing URNs and crosswalks, the reproducible G2 baseline derivation, the current physical/source-order inventory and its provisional limits, active gate, remaining G2 gaps, current text evidence and next action without old chat.

Current durable restart path:

- exact parent/file rights state → `corpus/files.tsv`;
- canonical folio↔image↔PDF mapping → Source crosswalk;
- baseline derivation + controlled/local storage boundary → `research/g2-baseline-provenance.md`;
- inspection event → `sources/inspection-log.tsv`;
- Checkpoint-A working source-order fixture → `research/g2-checkpoint-a-physical-inventory.md`;
- active consequence/next action → this `STATUS.md`.
