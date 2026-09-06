# Reg. Ii 4 Bd. II Knau fol. 306v-309r — evidence lock and contamination control

Created: 2026-09-04
Reconciled: 2026-09-06

## Authority and scope

This project-local file records the execution lock for the owner-selected current task in `projects/ega-reg-ii-4-bd-ii/STATUS.md` and `project.yml`.

It does not create a new Project, Source, Project->Source use, research priority or textual-dependence claim. It only constrains how the already-authorized Reg. Ii 4 Bd. II Knau first reading is executed, internally tested and later compared.

Current bounded target:

- Project: `ega-reg-ii-4-bd-ii`
- Source: `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089`
- Historical locus: Knau passage, fol. 306v-309r
- Digital locus: export images 667-672 / PDF pages 27-32
- Current execution state: complete independent working first-reading representation present; next step #97 G2 completeness audit
- Mode: Reg. Ii 4 internal representation/audit; external textual comparison remains locked

## Evidence state for the active work context

Canonical repository state already records the exact inspected export as `FILE-REG-II-4-II-00000089-EXPORT` and the crosswalk fol. 306v-309r <-> export images 667-672 <-> PDF pages 27-32.

The 2026-09-03/04 active target context additionally had the uploaded PDF `1533-Visitationsprotokoll-Ziegenrueck-ThHStAW, EGA, Reg. Ii 4 Bd. II-294r-313r.pdf` visually inspectable. Its relevant visible pages show:

| folio | PDF page | export image |
|---|---:|---:|
| fol. 306v | 27 | 667 |
| fol. 307r | 28 | 668 |
| fol. 307v | 29 | 669 |
| fol. 308r | 30 | 670 |
| fol. 308v | 31 | 671 |
| fol. 309r | 32 | 672 |

This is a target-context visual-evidence PASS for that work context only. If the work context changes, staging and pixel-inspectability must be re-established for the same evidence object instead of relying on this prose.

For the 2026-09-05 fol. 307r execution, the active context re-verified the staged PDF against the canonical SHA-256 for `FILE-REG-II-4-II-00000089-EXPORT` and pixel-inspected image 668 / PDF page 28 before transcription.

For the 2026-09-06 remaining-folio execution, the same canonical Reg. Ii 4 export and folio/image/PDF mapping were rechecked and images 669–672 were pixel-inspected before the prepared local first-reading files were persisted. The exact first-reading row counts are 22 / 25 / 25 / 5 for 307v / 308r / 308v / 309r respectively; 309r stops at the Knau boundary before the following Ziegenrück heading.

## Internal Reg. Ii 4 comparison rule during first reading

Witness independence means independence from external/parallel wording; it does **not** require folio isolation inside the same Reg. Ii 4 witness.

For a difficult first-reading locus:

1. inspect and localize the target graph/sign in Reg. Ii 4 first;
2. classify the actual problem before comparison where useful: grapheme, abbreviation, numeral/accounting sign, segmentation, source phenomenon, possible hand issue, etc.;
3. only then inspect directly and exactly locatable internal Reg. Ii 4 comparanda anywhere in fol. 306v-309r when they are relevant to that problem;
4. compare discriminating graphical/sign features, including evidence that fails to discriminate, rather than searching for or copying an expected word;
5. keep `same witness/source` distinct from `same hand`; hand relevance is a separate palaeographic claim;
6. keep lexical, onomastic, metrological and historical context downstream of graphically viable candidates;
7. if a consequential comparison materially supports, rejects or fails to decide a reading, preserve the exact anchor and concise reasoning in the owning research/transcription record; do not build a general survey register merely because direct inspection was broader.

A later folio may therefore provide an internal comparison anchor for an earlier difficult graph without becoming wording authority for that earlier locus. Source-order remains the persistence/traversal order; palaeographic learning may iterate within the same witness.

## Contamination lock

The following separation is mandatory until the project-local release gate below is satisfied.

| Material | Status before external comparison release | Allowed use | Forbidden use |
|---|---|---|---|
| Reg. Ii 4 Bd. II, Source `...00000089`, images 667-672 | primary evidence / same-witness internal comparison space | target-first visual inspection; physical-line inventory; diplomatic first reading; uncertainty marking; exact internal graphematic/sign comparison after target observation | expected-word copying; semantic completion of unread graphs; treating same source/record as same-hand proof |
| Reg. Ii 5 Ziegenrück material | quarantined parallel material | method warning; later controlled collation after release gate | wording source; line mapping for first reading; grapheme supply; same-hand assumption |
| Legacy G2/Knau files and old TSV/apparatus/palaeography | contaminated until Source/File/locus attribution is re-established | recovery/checking after release gate | promotion as Reg. Ii 4 reading; silent import; automatic witness attribution |
| Prior chat draft of image 667 | unadjudicated local draft | cursor memory and risk signal only | canonical line text unless each row is reinspected against image 667 |
| Early-modern visitation/domain knowledge | contextual hypothesis/control | generate questions; test/rank graphically viable candidates after source inspection | replace unread graphemes; normalize diplomatic spelling; infer names/amounts as manuscript text |

## Release gate for legacy/parallels

Reg. Ii 5 or legacy Knau/G2 material may be opened for **textual comparison/collation** only after all of the following are true for the current Reg. Ii 4 locus:

1. fol. 306v-309r has a complete independent Reg. Ii 4 first-reading representation in source order;
2. the G2 completeness audit has established that every relevant visible source unit is represented and consequential uncertainty/source phenomena remain discoverable;
3. the systematic internal palaeographic/philological pass over consequential `working`/`unresolved` loci is complete for the current roadmap, with unresolved results retained where internal evidence does not decide;
4. physical line references are stable enough to cite and compare;
5. the comparison record identifies itself as collation/checking, not as original first reading;
6. any later promoted Reg. Ii 4 correction explains the inspected Reg. Ii 4 graphical basis and does not rely on parallel wording alone;
7. legacy material is used only where its exact Source/File/locus provenance is adequate for the specific comparison claim.

Current gate state after completion of the six folio-local working first-reading files:

- condition 1: **met at working-representation level**;
- conditions 2 and 3: **not yet met** (#97 and #98 pending);
- conditions 4–7: not sufficient to release external textual comparison before #97/#98 complete.

If these conditions are not met, the correct action is to continue Reg. Ii 4 representation/internal testing, not to consult a clearer external witness for wording.

This is a **project-local current release rule**, not a new universal claim that every future project must complete an identical G3 sequence before any external comparison.

## First-reading representation

First-reading data are stored one archival folio per file under `transcription/first-reading/`. These files are work/data partitions of the authorized Reg. Ii 4 first-reading representation; their directory hierarchy does not create a new scholarly parent entity or a second owner of Project state.

Stable scope/provenance facts — canonical Source ID, folio-to-export/PDF mapping, File identity and generic direct-inspection provenance — are resolved from the Project/corpus/evidence owners and are not repeated on every row. The row table is ordered around the changing scholarly information:

1. `reading_order`;
2. `diplomatic_reading`;
3. `line_ref`;
4. `region` where relevant;
5. `source_phenomena`;
6. `research_status`;
7. graphically viable `alternatives`;
8. separate `abbreviation_layer` / `editorial_supply` where needed;
9. consequential local `evidence_note`.

When an internal same-witness comparison materially affects a consequential reading, `evidence_note` may carry the exact comparison locus and concise discriminating reason. Routine direct inspection that does not affect a decision need not be serialized as a separate survey dataset.

The independent first-reading files do not carry a mutable `collation_status` column. Later external comparison belongs in a separate collation layer so that opening a parallel witness cannot silently redefine first-reading provenance.

A fluent full line with hidden uncertainty is worse than a narrower visible unresolved span.

## 2026-09-04 image 667 first-reading progress

`transcription/first-reading/306v.tsv` contains the first source-exact working row set for fol. 306v / export image 667: rows `306v-01` through `306v-21`.

This is an independent Reg. Ii 4 image-667 reading pass. Reg. Ii 5, legacy G2/Knau files and the prior chat draft were not used to supply wording. The result deliberately preserves unresolved spans and possible source phenomena rather than normalizing the account list into fluent prose.

Known limits of the image-667 pass:

- several top-account amount/measure lines remain `unresolved` or `working`;
- the left accounting signs are flagged as visible but not yet separately adjudicated;
- `Lehnherr:` and some names/measure terms remain working readings;
- the `wachs` line has a possible cancellation/entry-flourish phenomenon that is not yet classified as deletion.

This progress does not release legacy/parallels for comparison, because the release gate applies to the complete Reg. Ii 4 representation plus its G2/internal-adjudication sequence.

## 2026-09-05 image 668 first-reading progress

`transcription/first-reading/307r.tsv` contains the source-exact working representation for fol. 307r / export image 668 as rows `307r-01` through `307r-19`.

All nineteen relevant physical units are represented. Consequential local same-witness comparisons are recorded only where they materially affect a reading: the p-initial second heading remains `parem|paren` after comparison with `307r-11`/`307r-15`, and the upper G-like sequence remains unresolved because `306v-02` does not provide a discriminating basis for a `-dorff` completion. Numeral/accounting signs remain uninterpreted. These are working AI-assisted readings, not independent specialist validation.

This folio-level progress does not release legacy/parallels and does not claim whole-locus G2/G3 completion.

## 2026-09-06 images 669–672 first-reading progress

The remaining folio-local working first-reading representations are present as:

- `307v.tsv`: `307v-01`–`307v-22`;
- `308r.tsv`: `308r-01`–`308r-25`;
- `308v.tsv`: `308v-01`–`308v-25`;
- `309r.tsv`: `309r-01`–`309r-05`.

All 77 relevant visible units from these four images are represented. The 309r file ends at the Knau boundary and excludes the following new Ziegenrück heading. Working/unresolved spans remain explicit; numeral/measure/accounting contexts are not silently converted into values. Later direct Reg. Ii 4 target forms of `Greffendorff`/`greffendorff` are present, but they have not been used to alter `307r-02`; that whole-locus internal comparison belongs to #98.

Together with `306v.tsv` and `307r.tsv`, the complete authorized fol. 306v–309r locus now has an independent Reg. Ii 4 working first-reading representation. This satisfies release-gate condition 1 only; it does not establish G2 or systematic G3 completion.

## Current execution state

Next executable action:

> Run #97 G2 completeness audit over the six folio-local Reg. Ii 4 first-reading files. Verify physical/source-order completeness, stable line references, boundaries, abbreviations, source phenomena, numeral/accounting/measure sign preservation, explicit uncertainty and absence of external-witness wording. Confirm that 309r stops at the Knau boundary. Any whole-locus human-readable view must be deterministically derived rather than maintained as a second transcription truth.

If #97 passes, record G2 in the canonical Project state and proceed immediately to #98 systematic internal palaeographic/philological adjudication. Reg. Ii 5 and legacy G2/Knau remain closed as textual comparison/wording evidence until #98 is complete and the release gate is explicitly satisfied.

## Invalidation triggers

Re-run the evidence prerequisite if:

- the active work context no longer has the uploaded PDF or render/crop set for a new direct source-inspection claim;
- the inspected image does not match `FILE-REG-II-4-II-00000089-EXPORT` / image 667-672;
- a later corpus/crosswalk correction changes the folio/image/PDF-page mapping;
- visual inspectability fails or a different derivative is substituted.

New model uncertainty alone is not an invalidation trigger. It should narrow the unresolved locus or trigger qualified review, not send the work back into retrieval/governance loops.
