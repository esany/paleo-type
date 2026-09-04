# STATUS — ThHStAW, EGA, Reg. Ii 4 Bd. II

Last checkpoint: 2026-09-04

## Project authority and root

The human owner explicitly confirmed on 2026-09-02 that Reg. Ii 4 Bd. II should currently continue as one act-oriented Project, anchored at `ACT-THHSTAW-EGA-REG-II-4-BD-II`, as an application of D-018. This current authority does not retroactively certify the complete historical D-017 wording.

On 2026-09-03 the human owner selected the **Knau passage of the Reg. Ii 4 Bd. II Ziegenrück Source** as the current manuscript/source-research target. This activates a bounded research locus; it does not redefine the Project boundary and does not assign a permanent Project→Source research-function label by itself.

## Known internal section/source node

`THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089` — *Visitation im Amt Ziegenrück*, fol. 294r–313r — is an internal Source node by canonical `part_of` relation. Its identified Knau locus is fol. 306v–309r / export images 667–672.

This is a separate material Source/witness from the Reg. Ii 5 Ziegenrück record fol. 55v–66v. Their archival extract/correspondence relation does not merge witness identity, foliation, image numbering, File provenance or diplomatic readings.

`source-uses.tsv` remains empty until an actual project-relative research function needs to be recorded. The current work target is carried by the owner-selected `active_scope`/`NEXT ACTION`, not by inferring a `principal`, `comparison` or other research function.

## Recovered prior work state

Historical snapshot `699fa6eada61db483dfca950193412715d9603a5` recorded the former source-unit state: the primary export had been inspected; the Knau locus had been mapped; the source was not activated for source-wide work; and any later comparison was to begin from an **independent reading** rather than import readings from Reg. Ii 5.

The old source-unit Project files were later removed from `main`, but Source/File/crosswalk evidence survives in `corpus/`. This STATUS restores consequential work-state/audit context without reviving source-as-project semantics.

## Legacy Knau/G2 material from the Li 5 path

The historical diplomatic material preserved under `projects/ega-reg-ii-5-knau/` must **not** be promoted wholesale into Reg. Ii 4 merely because parts of it closely match this witness. The owner clarified on 2026-09-02 that this older material is primarily verification/recovery material, and direct comparison of the separate Reg. Ii 4 and Reg. Ii 5 PDFs showed that legacy witness attribution cannot safely be inferred from old path/page labels.

Current rule:

- use the old Knau/G2 files only as checking/recovery material;
- for a Reg. Ii 4 diplomatic claim, inspect the Reg. Ii 4 Source/File/locus itself;
- only after that independent inspection may a matching legacy reading be promoted as Reg. Ii 4 evidence;
- do not treat similarity to the parallel Reg. Ii 5 transmission as witness identity.

The canonical current classification of that legacy corpus is recorded in `projects/ega-reg-ii-5-knau/research/legacy-witness-provenance.tsv`.

## Evidence / crosswalk / URN state

- Exact inspected export: `FILE-REG-II-4-II-00000089-EXPORT` in `corpus/files.tsv`.
- Canonical crosswalk: fol. 306v–309r ↔ export images 667–672 ↔ PDF pages 27–32.
- The six mapped pages each have a distinct page-specific `urn:nbn:...` value in the canonical crosswalk. These values were already present when the crosswalk was first created and are not inferred from the PDF-page sequence.
- The crosswalk is intentionally partial; it does not claim page-level mapping for the full act/protocol.

## Research/gate state

The current target is now the Reg. Ii 4 Knau locus itself. No current diplomatic transcription is declared merely from the legacy Knau/G2 corpus. Any new reading must be established independently against the Reg. Ii 4 Source/File/locus.

The observed correspondence with Reg. Ii 5 remains a separate Source-relationship claim in `corpus/relationships.tsv`; it does not assign a permanent comparison role and must not supply graphemes for the independent first reading.

## 2026-09-04 source-local first-reading locks

To prevent old mixed or parallel material from being reintroduced as silent reading evidence, the Reg. Ii 4 Knau task now has project-local execution controls:

- `research/knau-fol306v-309r-evidence-lock.md` owns the immediate evidence/read-order/legacy-release lock for this bounded first-reading task.
- `research/knau-fol306v-309r-contamination-matrix.tsv` records the concrete allowed/forbidden use classes for Reg. Ii 4 evidence, Reg. Ii 5 parallels, legacy G2/Knau material, the prior chat draft and domain context.
- `transcription/README.md` defines the human-auditable information hierarchy for this transcription layer.
- independent first readings are stored one folio per file under `transcription/first-reading/`; stable Source/File/image/PDF metadata remains in its canonical corpus/evidence owners instead of being copied into every row.

The active upload/preflight in the 2026-09-03/04 work context showed the target pages visually inspectable, including page 27 / image 667 through page 32 / image 672. Because that upload path is target-context evidence rather than repository preservation, any new execution context must re-establish staging and pixel-inspectability before source inspection.

## 2026-09-04 fol. 306v / image 667 progress

The first independent Reg. Ii 4 working pass for fol. 306v / export image 667 is stored in `transcription/first-reading/306v.tsv` as rows `306v-01` through `306v-21`.

The table is deliberately human-first: `reading_order` and `diplomatic_reading` are the leading columns; line/source structure, phenomena, epistemic status, alternatives and only consequential local notes follow. Repeated Source ID, folio/image/PDF provenance, generic creation provenance and row-level `not_collated` metadata were removed from the row surface because those facts are stable or stage-level and are recoverable from canonical corpus/evidence owners and Git history.

This is not a polished edition and not a collation result. It is a source-exact diplomatic first-reading draft from image 667 itself. Reg. Ii 5, legacy G2/Knau and the prior chat draft did not supply wording. The rows intentionally retain `unresolved`, `unclear`, visible abbreviation layers, layout/divider rows and possible source phenomena.

Main unresolved areas carried forward:

- top-account amount/measure lines `306v-04` through `306v-06`;
- the descriptor after `fuder hauers` in `306v-08`;
- the place/descriptor after `holtzmarck zů` in `306v-09`;
- exact reading of `Lehnherr:` and `Vorsteter` in `306v-12`/`306v-13`;
- the final source term/name in `306v-17`;
- the source phenomenon of the `wachs` line in `306v-19`;
- the internal phrase after `meßing wagen` in `306v-20`.

The legacy/parallels release gate is still closed because fol. 306v–309r is not yet independently represented in full.

## NEXT ACTION — canonical restart point

**Continue independent source-exact inspection with fol. 307r / export image 668 and proceed through fol. 309r / image 672.**

Execution order:

1. verify that the exact Reg. Ii 4 evidence for image 668 is staged and visually inspectable in the active target context;
2. read/transcribe from Reg. Ii 4 itself in physical/source order, preserving diplomatic spelling, abbreviation signs, layout-relevant uncertainty and unresolved readings;
3. create `transcription/first-reading/307r.tsv` in the same human-first structure;
4. continue sequentially through separate folio files for images 669–672 / fol. 307v–309r;
5. only after an independent Reg. Ii 4 reading for fol. 306v–309r exists may legacy Knau/G2 or Reg. Ii 5 material be consulted as checking/collation evidence;
6. do not promote any legacy reading merely because it matches this witness.

If the required image is not staged/vision-inspectable, stop at the evidence prerequisite and obtain/stage the exact Reg. Ii 4 image rather than substituting Li 5 or legacy text.

## Restartability

A fresh context must identify the Reg. Ii 4 Bd. II Project, its separate Ziegenrück Source, exact File/crosswalk/URN state, the owner-selected current target at fol. 306v–309r / images 667–672, the completed `transcription/first-reading/306v.tsv`, and the fact that old Knau/G2 readings are verification/recovery material rather than canonical Li 4 transcription unless independently re-established against this witness.

It must also load the 2026-09-04 project-local evidence lock and contamination matrix before continuing the folio-local first-reading series. The current safe cursor is fol. 307r / image 668: detailed line-by-line first reading from the Reg. Ii 4 image itself, not from Reg. Ii 5, legacy G2/Knau, domain context or the unadjudicated preliminary chat draft.
