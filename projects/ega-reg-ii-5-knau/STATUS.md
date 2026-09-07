# STATUS — ThHStAW, EGA, Reg. Ii 5

Last checkpoint: 2026-09-07

## Project authority and identity

The human owner confirmed on 2026-09-02 that **Reg. Ii 5 continues as an act-oriented Project**, anchored at `ACT-THHSTAW-EGA-REG-II-5`. The directory/id `ega-reg-ii-5-knau` is a legacy path from an earlier AI-organized Knau benchmark; `Knau` is not the Project boundary.

On 2026-09-07 the human owner selected a new bounded scholarly target: **source-exact editorial development of the Reg. Ii 5 Ziegenrück witness at fol. 61v–63r**, tracked in #115. This is an Editionsbaustein, not a completed scientific edition and not authority for an abstract transcription/person-role/date ontology.

## Canonical Source structure

Keep archival container, concrete Source record and research use distinct.

- `ACT-THHSTAW-EGA-REG-II-5` — archival act / documentary Project anchor: **ThHStAW, EGA, Reg. Ii 5**.
- `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129` — concrete internal Source record: **Visitation im Amt Ziegenrück**, fol. 55v–66v, described in archival metadata as an extract related to the Reg. Ii 4 Bd. II Ziegenrück transmission.
- `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089` — separate Source record in the separate archival act **Reg. Ii 4 Bd. II**, fol. 294r–313r; its Knau passage is fol. 306v–309r / export images 667–672.
- The two Reg. Ii 3 records remain separate Sources inside the Reg. Ii 3 archival act and are not witnesses of the Ziegenrück text merely because they were historically used for context/control.

The Reg. Ii 4 and Reg. Ii 5 Ziegenrück records are separate material witnesses/transmissions. Close textual correspondence does not collapse their identities, dates, hands, production stages or diplomatic readings.

## Current active Source use and exact evidence

The current principal Project-relative Source use is:

- use `USE-REGII5-00000129-PRINCIPAL`;
- Source `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`;
- relevant locus fol. 61v–63r;
- status `active` for #115.

The exact active File binding is:

- evidence `EVID-REGII5-00000129-PRINCIPAL`;
- File `FILE-REG-II-5-00000129-EXCERPT`;
- export images 132–135;
- SHA-256 `e989fe614c715e417e3586e29628d67d274964f195b3f1e66a8682bfcde54f6f` in canonical `corpus/files.tsv`.

The previous Knau-era principal use and File relation remain recoverable through Git/migration history. Reactivation does not retroactively validate any legacy diplomatic line.

**Evidence identity is not current target-context readiness.** At execution time the source-work context must still establish `STAGED` and `VISION-INSPECTABLE` for the required Reg. Ii 5 pixels under `methodology/workflow.md` before making new pixel-dependent readings.

## Legacy diplomatic material — verification/recovery only

The historical diplomatic and witness-dependent Knau material under this legacy Project path — especially `transcription/132.tsv` through `135.tsv`, `apparatus/decisions.tsv`, the legacy palaeography tables and any claims that depend on their old page/path attribution — is preserved because it documents earlier work and remains useful for checking readings, failure modes and migration loss.

**It is not canonical current Reg. Ii 5 diplomatic transcription state.**

Owner clarification and direct comparison of the separately supplied Reg. Ii 4 Bd. II and Reg. Ii 5 Ziegenrück PDFs on 2026-09-02 showed that the earlier working diplomatic corpus cannot safely be assigned wholesale to one witness from its legacy path/page labels alone. The two transmissions are closely parallel, and historical work phases may have imported or compared readings across them. Until witness provenance is re-established for a concrete reading, the old diplomatic material has status **legacy verification/recovery evidence; witness attribution unresolved or potentially mixed**.

Consequences:

- preserve every old reading, uncertainty, apparatus decision and palaeographic observation;
- do not delete or silently normalize the old material;
- do not cite `transcription/132.tsv`–`135.tsv` as proof of a Reg. Ii 5 reading without fresh witness-specific inspection;
- do not move a legacy reading into Reg. Ii 4 merely because it matches that witness; attribution requires explicit Source/File/locus verification;
- new diplomatic work starts from the explicitly identified Reg. Ii 5 Source, exact File and locus;
- comparison between Reg. Ii 4 and Reg. Ii 5 is witness-to-witness collation, not reuse of a shared transcription.

## Later exact-source G2 research artifacts — bounded direct authority

The legacy directory later accumulated four `research/g2-*` artifacts with evidential roles that are **not** inherited from the unresolved witness provenance of the older diplomatic corpus. Their authority follows their own Source/File/locus chain and is classified explicitly in `research/legacy-witness-provenance.tsv`:

- `research/g2-baseline-provenance.md` — exact Reg. Ii 5 Source/File/SHA/crosswalk/render and research-access provenance;
- `research/g2-checkpoint-a-physical-inventory.md` — direct Reg. Ii 5 visual observations of physical/source order, layout and bounded source phenomena on fol. 61v–63r;
- `research/g2-checkpoint-b-semantic-loss.md` — source-bound mapping and semantic-loss/adequacy analysis against the accepted Reg. Ii 5 physical anchors and the legacy research records;
- `research/g2-domain-review-checkpoint-b.md` — consequence/requirements classification derived from that source-bound fixture.

These artifacts retain scientific authority **only at the level they actually claim**. Direct Reg. Ii 5 physical observations such as source order and recorded cancellations are not downgraded merely because the files live in the legacy directory. Conversely, none validates `transcription/132.tsv`–`135.tsv` row-by-row, resolves old witness attribution, establishes same hand, or promotes an old diplomatic reading into current Reg. Ii 5 truth.

The 2026-09-07 A-R reconciliation removed the former blanket `research/g2-*` quarantine and replaced it with explicit artifact-level classifications. This was a provenance-boundary correction only; no manuscript reading, source relationship or unresolved scholarly question was re-adjudicated.

## Exact-source structural starting fixture for #115

Checkpoint A directly validated 81 provisional physical/source-order anchors against the exact Reg. Ii 5 baselines:

- 61v: `L01–L20`;
- 62r: `L01–L25`;
- 62v: `L01–L25`;
- 63r: `L01–L11`.

These anchors may be reused as bounded structural evidence, subject to correction if fresh direct inspection finds a structural error. They are not current diplomatic text.

Established direct source phenomena at this level include:

- list/accounting structure on 61v;
- recurrent visible abbreviation marks;
- cancellation at `61v-L16`;
- cancellation at `62r-L18`;
- Arabic `80` at `62r-L19` and `62v-L01`;
- no hand differentiation was established: it remained `not investigated`.

Checkpoint B and its Domain Review demonstrate that the legacy representation collapses physical lineation in places, omits explicit cancellation phenomena, uses some coarse/ad-hoc targets and lacks legacy coverage for visible `63r-L05–L11`. Those findings are loss/research fixtures; they do not preselect a universal replacement schema.

## Project-local editorial execution discipline for #115

The next work follows existing generic method (`historical-source-workflow.md`, `transcription-guidelines.md`, `research-gates.md`) through a **project-specific source-exact editorial vertical slice**. This is not claimed as a standardized four-stage external model.

### 1. Diplomatic source observation / reading

Record the material/source-exact state actually supported by the pixels: physical order, written signs, abbreviations, cancellations/additions/overwriting, relevant layout, damage/unreadability and observable changes in script features.

An observable script-feature change or possible hand change does **not** by itself create a discrete hand identity. A `HAND-X` hypothesis requires separate palaeographic analysis; identification of a hand with a historical person is a still further claim.

### 2. Text-near editorial development

Where present, keep manuscript name/place forms, titles/offices/functions, date formulations, addressing, explicit relationships/statements and textual structure locus-bound. The manuscript form is an editorial finding and must not be replaced by a normalized identity.

### 3. Identification, contextual role, dating and text-critical claims

Each requires its own evidence and status. In particular:

- diplomatic reading confidence does not determine identification confidence;
- identification does not determine contextual role;
- contextual/event association does not determine scribe/hand;
- a date is always a claim about a specified target/context (archival unit, event, textual date, production/excerpt stage, etc.);
- similar/corresponding text does not transfer a date from one witness/context to another;
- textual correspondence/variant/omission/condensation/resegmentation across witnesses is permitted only after the relevant witnesses have been independently established and loci controlled.

### 4. Historical interpretation stays downstream

Visitational organization, administrative process, social/economic interpretation and causal production/redaction history are not silently presented as direct manuscript observations. They may be developed later from the established editoric/source-critical evidence.

## Witness independence and admissible comparison

**Reg. Ii 5 is not folio-isolated.** Exact, source-bound same-witness comparanda elsewhere in Reg. Ii 5 may be used for graphematic/palaeographic testing after the target problem is observed. Same Source/record still does not prove same hand.

**Reg. Ii 4 wording is excluded as reading authority during the independent Reg. Ii 5 basis.** The already completed Reg. Ii 4↔Reg. Ii 5 collation remains valid historical research evidence but may not pre-supply the new Reg. Ii 5 wording.

After the independent Reg. Ii 5 basis is sufficiently established, a controlled external comparison may open. Any externally prompted Reg. Ii 5 correction still requires direct Reg. Ii 5 reinspection and target-graph evidence.

## Source-driven Semantic-Loss / Package-B rule

Person/role/date and related Package-B work is **not a standalone architecture programme**.

Use this loop:

```text
source inspection
→ source finding / reading
→ text-near editorial development where relevant
→ identification / role / date claim only with its own evidence
→ test whether the existing representation preserves the actual finding losslessly
→ if yes: continue source work
→ if no: define the smallest missing information requirement
→ if material: route only that bounded semantic change through D-016 / loss-checked implementation
→ return immediately to the source
```

The currently demonstrated flat `corpus/sources.tsv:persons` / role-note problem is real, but it is not repaired by merely adding/removing names from a flat list. Any role/person/date structural change must be driven by the concrete editoric claims that need preservation, while keeping person identity, text mention, contextual role and hand/scribe hypothesis distinct.

No universal agent/role/date/hand/locus ontology is authorized by #115.

## Historical work-state audit

The earliest repository Project metadata (`251ce9ed39e04bb852e0232dbcce21c68bd4c3a7`) created `ega-reg-ii-5-knau` and the Knau scope as an AI-organized benchmark. Checkpoint `08c08bd6f90635210fbeff3f2d19cd0a485cc0b9` froze useful working readings and uncertainties, but it does not establish their witness provenance or owner authority for Project identity.

Snapshot `699fa6eada61db483dfca950193412715d9603a5` preserves the later source-unit state. Git history remains an audit/recovery source, not current scientific authority.

The former compatibility register `sources/sources.tsv` was loss-checked and removed. Its historical research functions remain in `source-uses.tsv`; the Reg. Ii 5 fol. 61v–63r principal function is now explicitly reactivated for #115 while the other preserved comparison/control/context uses remain historical. Exact File bindings remain in `research/use-evidence.tsv` with the same current/historical distinction.

## Digital addressing / provenance

For the canonical Reg. Ii 5 Source `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`:

- canonical File identity/provenance is owned by `corpus/files.tsv`;
- canonical Source crosswalk is owned by `corpus/source-data/THHSTAW-EGA-REG-II-5-STAT-VIS-00000129/crosswalk.tsv`;
- Source boundary is fol. 55v–66v;
- the PDF/export may contain adjacent context beyond that Source boundary;
- identifiability/reproducibility do not by themselves establish that evidence is staged and inspectable in a fresh target context.

For the separate Reg. Ii 4 Bd. II Ziegenrück Source, its own File, crosswalk, page-specific URNs and fol. 306v–309r / images 667–672 remain canonical under that Source. Never substitute one witness's image numbering, TIFF labels, folios, dates or readings for the other.

## Current research state

No current canonical diplomatic transcription of Reg. Ii 5 is yet declared by this STATUS. **#115 is the active work to build that witness-specific editorial basis from Reg. Ii 5 itself.**

The old diplomatic transcription/apparatus/palaeography remains a verification/recovery fixture with unresolved or potentially mixed witness attribution. Separately, the explicitly classified `research/g2-*` artifacts remain usable according to their own bounded evidence roles, including direct Reg. Ii 5 physical/source-order observations where actually revalidated.

Any new diplomatic result must be established against the explicitly targeted Source/File/locus. Existing direct physical observation must not be mistaken for diplomatic reading, and source-bound semantic-loss/domain analysis must not be mistaken for manuscript text.

## NEXT ACTION — canonical restart point

**Execute #115: begin with WP-0 and then fol. 61v.**

1. Rehydrate Source `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`, File `FILE-REG-II-5-00000129-EXCERPT`, fol. 61v / image 132 / PDF page 14 and the canonical crosswalk.
2. Verify current target-context `STAGED` + `VISION-INSPECTABLE` pixel readiness.
3. Before creating any new canonical transcription artifact, perform artifact-ownership preflight. Do not overwrite or silently promote legacy `transcription/132.tsv`–`135.tsv`.
4. Reinspect and independently read `61v-L01–L20` from Reg. Ii 5 itself, preserving source phenomena and uncertainty.
5. Add text-near names/titles/functions/date expressions only where actually present and keep identifications/roles/dating claims separate with their own evidence/status.
6. Use exact Reg. Ii 5 internal comparanda where useful; keep Reg. Ii 4 wording closed until the independent Reg. Ii 5 basis reaches controlled-comparison release.
7. If a real editoric finding cannot be represented without semantic loss, stop only that affected persistence step, define the smallest missing information requirement and route a bounded change; otherwise continue reading.

Issue #115 owns the work checklist. This STATUS owns the current scholarly/restart state.

## Restartability

A fresh capable context must be able to reconstruct without old chat that:

- Reg. Ii 5 is an archival-act Project anchor and #115 is the current bounded source-research task;
- the active target is the separate Reg. Ii 5 Ziegenrück Source at fol. 61v–63r / images 132–135;
- exact File/SHA/crosswalk identity is established, while current pixel staging/inspectability must still be checked in the execution context;
- Reg. Ii 4 Bd. II and Reg. Ii 5 contain separate Ziegenrück witnesses and must remain independently read;
- legacy `transcription/132.tsv`–`135.tsv`, apparatus and witness-dependent legacy palaeography are verification/recovery evidence, not current Reg. Ii 5 transcription truth;
- the exact-source G2 artifacts retain only their stated provenance/physical-observation/loss-analysis authority;
- 81 working physical anchors exist for 61v–63r, but they are structural evidence rather than a current diplomatic text;
- same-witness Reg. Ii 5 internal comparanda are admissible; Reg. Ii 4 wording remains excluded until independent witness basis/release;
- reading, identification, contextual role, hand hypothesis and dating claims retain separate evidence/status and do not inherit certainty from one another;
- Package B is triggered only by demonstrated editoric semantic loss and must return immediately to source work after the smallest adequate repair;
- the immediate cursor is WP-0 → fol. 61v, not an abstract schema/migration programme.
