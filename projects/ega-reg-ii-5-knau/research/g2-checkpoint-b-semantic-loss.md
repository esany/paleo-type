# G2 Checkpoint B — legacy/apparatus semantic-loss mapping, Reg. Ii 5 fol. 61v–63r

Status: **#72 CHECKPOINT B COMPLETE — READY FOR #73 DOMAIN REVIEW.**

Completed: 2026-08-31

This is a **Source Research evidence fixture for #64/#72**. It records source-bound mapping, demonstrated loss/adequacy and bounded uncertainty. It does **not** derive a final G2 representation, generic requirement, schema, migration, Dev handoff or specialist-validation claim.

## 1. Authority and evidence boundary

Governing chain:

`GOVERNING_OBJECTIVE.md → AGENTS.md → applicable REQ-* → authoritative methodology → canonical project/source state → inspected source evidence`

Exact fixture:

- Source: `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`
- File: `FILE-REG-II-5-00000129-EXCERPT`
- verified parent SHA-256: `e989fe614c715e417e3586e29628d67d274964f195b3f1e66a8682bfcde54f6f`
- fol. 61v → image 132 → PDF page 14 → `stat_derivate_00000416:/ThHStAW_RegIi_5_0130.tif`
- fol. 62r → image 133 → PDF page 15 → `stat_derivate_00000416:/ThHStAW_RegIi_5_0131.tif`
- fol. 62v → image 134 → PDF page 16 → `stat_derivate_00000416:/ThHStAW_RegIi_5_0132.tif`
- fol. 63r → image 135 → PDF page 17 → `stat_derivate_00000416:/ThHStAW_RegIi_5_0133.tif`

No literal image `urn:` has been established and none is inferred.

Checkpoint A is the accepted direct visual source↔anchor inspection of the exact unprocessed baselines. It establishes the source-order fixture used here: 61v `L01–L20`, 62r `L01–L25`, 62v `L01–L25`, 63r `L01–L11`, including the cancellation/numeral/layout observations recorded there. Checkpoint B compares those accepted source observations with **current `main`** legacy transcription, apparatus and palaeography. It does not re-adjudicate difficult readings merely to force an exact row mapping.

During the 2026-08-31 continuation, the 61v private attachment could be retrieved through the connector but was not exposed as a fresh locally openable analysis image. Per the #72 anti-loop rule, access was not repeatedly retried. No new pixel-dependent reading is asserted from that failed fresh handle. Any finer row→physical-line or decision→span localization requiring renewed pixel comparison remains explicitly `ambiguous`/`unresolved`; the structural/phenomenon source evidence below remains the already visually validated Checkpoint-A fixture.

## 2. Current-main input note

Current `main` is authoritative. It contains:

- `transcription/132.tsv`–`135.tsv` with `page_id / line_id / region / reading / status / alternatives / evidence_note`;
- `apparatus/decisions.tsv` with current D001–D011 from `welch → wolff` through the `80` observation;
- `palaeography/lexicon.tsv` and `palaeography/numerals.tsv`.

Historical/convenience `K132-*` labels and an alternate D001–D011 description present in a handoff are **not** silently treated as current records. This is an input/version-provenance distinction, not a manuscript semantic-loss finding.

Legacy `line_id` values are never presumed to be physical manuscript line numbers.

### Mapping vocabulary

- **exact** — current record can be tied to one exact source anchor or exact bounded source range without guessing;
- **partial** — bounded source region is established, but current representation collapses structure/content or cannot preserve a finer distinction;
- **ambiguous** — more than one source-local mapping remains plausible;
- **unresolved** — no responsible source-local mapping can currently be established.

---

# 3. fol. 61v / image 132 — COMPLETE with bounded unresolved detail localization

Checkpoint-A source structure: `L01` heading; `L02–L03` introduction; `L04–L11` eight-line spatial list/accounting block; `L12–L16` prose; `L17–L20` second prose block. Cancellation is visibly established at `L16`. Left quantity/sign notation belongs to the list block and is spatially relevant.

| source anchor | visible/source observation | current representation | mapping | demonstrated loss / adequacy | uncertainty |
|---|---|---|---|---|---|
| `61v-L01` | display heading | `132:00` `Knawe`, observed | **exact** | Heading presence/order is preserved. **No demonstrated loss.** | No new reading adjudication. |
| `61v-L02–L03` | two-line introduction | `132:01–02`, region `top` | **partial** | Both introductory records survive, but row boundaries are not promoted to physical-line identity from numbering alone. | Exact `132:01/02`→L02/L03 split remains unverified. |
| `61v-L04–L11` | eight physical list/accounting lines | `132:03–08`, six `list` rows; W1–W6 in `numerals.tsv` | **partial** | **Eight physical source lines are represented by six legacy list rows.** One-to-one physical lineation is therefore lost/collapsed. W1–W6 uncertainty survives. | Exact W1–W6→physical-line localization remains unresolved. |
| `61v-L04–L11`, left sign/quantity positions | left quantity/sign notation aligned with written entries; not a separate margin | inline W1–W6 placeholders + `region=list` + `numerals.tsv` | **partial** | Existence of sign/value groups survives, but the validated spatial association of the eight source lines cannot be reconstructed from six rows alone. | Individual sign values/readings remain unresolved; no marginal stream is inferred. |
| `61v-L12–L16` | five physical prose lines | `132:09–15`, seven prose fragments | **ambiguous** | Legacy prose segmentation is not physical lineation; seven fragments cannot be assigned one-to-one to five physical lines from IDs alone. | Fine lexical row→line mapping requires renewed source-local comparison if consequential. |
| `61v-L16` | confirmed cancellation at beginning/within line | no explicit cancellation/deletion phenomenon in `132.tsv` | **partial** | **The source intervention is not recoverable from the legacy transcription alone.** | Deleted wording/replacement relation remains unresolved. |
| `61v-L17–L20` | four physical lines in second prose block | `132:16–19`, four prose fragments | **partial** | Coverage is bounded and ordered, but exact one-to-one identity is not assumed after the demonstrated earlier segmentation divergence. U1/U2 and surname uncertainty survive. | Exact row→line localization remains unresolved where needed. |
| U2 locus in final prose | unresolved source reading | `132:18`; D005/D006 | **ambiguous** | **Positive preservation:** two semantic completions are explicitly rejected and `[U2]` remains unresolved. Loss is target precision, not decision history. | `132/18` is a legacy fragment target, not an established physical line/span. |
| `ij`, Arabic `1`, W1–W6 | notation/sign evidence | `numerals.tsv`: `ij` at `132:01`; `1` at `132:06;132:13`; W1–W6 unresolved | **partial** | Written notation and uncertainty are retained. Legacy addresses are not yet exact physical anchors. | No forced expansion/value reading. |
| legacy “same-hand” language | hand differentiation was **not investigated** at Checkpoint A | e.g. `132:09` note / D001 evidence wording | **unresolved as hand attribution** | Such wording cannot be promoted into an established hand claim. **This is not by itself a system failure.** | Requires palaeographic investigation only if consequential. |

### 61v coverage / completion result

All Checkpoint-A anchors `L01–L20` are accounted for as exact or bounded partial/ambiguous ranges. All current `132.tsv` rows `00–19`, relevant notation records and 61v-affecting apparatus material are accounted for. Fine row/line and decision/span localization is deliberately left unresolved rather than guessed.

**61v COMPLETE for Checkpoint B — bounded unresolved detail localization retained.**

Positive non-results:

- W1–W6 remain unresolved rather than being invented;
- D005/D006 preserve rejected proposals and residual uncertainty;
- no independent marginal/interlinear stream is manufactured;
- no hand attribution is promoted.

Governing domains/requirements implicated: REQ-EDIT-002, REQ-EDIT-003, REQ-ARCH-009, REQ-PAL-001, REQ-PAL-003, REQ-PAL-006, REQ-PAL-007, REQ-GWP-002, REQ-GWP-004.

Request to #73: determine whether the demonstrated physical-line/spatial/intervention losses are project-local mapping/research consequences, already-covered generic scholarly requirements, or evidence of any reusable gap; preserve the positive uncertainty/decision-history cases.

---

# 4. fol. 62r / image 133 — COMPLETE with bounded unresolved target localization

Checkpoint-A source structure: `L01–L11`, `L12–L18`, `L19–L25`. Cancellation at `L18`. Arabic `80` begins `L19`.

| source anchor | visible/source observation | current representation | mapping | demonstrated loss / adequacy | uncertainty |
|---|---|---|---|---|---|
| `62r-L01–L11` | eleven physical lines, first paragraph | single `133:01-11` unresolved record | **partial** | **Eleven physical lines collapse into one legacy record.** Bounded paragraph survives; internal physical lineation/targeting does not. | Text remains intentionally unresolved. |
| `62r-L12–L18` | seven physical lines, second paragraph | `133:12–18`, seven ordered records | **partial** | Coverage/order are substantially preserved, but ID equality is not treated as proof of physical-line identity without lexical source comparison. | Exact individual row→line identity remains pending only where consequential. |
| `62r-L18` | confirmed word cancellation | `133:18` carries surviving reading only | **partial** | **Cancellation is not represented as a source phenomenon in the legacy transcription.** | Deleted reading unresolved; no interlinear replacement established. |
| `62r-L19` | Arabic `80` visibly begins third paragraph | `133:19` begins `Von des pfarrholtz / 80 ...`; `numerals.tsv` records `80` observed | **exact** | The visible numeral form is preserved separately from unresolved meaning/syntax. **No demonstrated loss for this numeral occurrence.** | N1/unit/syntax remain unresolved. |
| `62r-L20–L25` | remaining six physical lower-paragraph lines | `133:20–25` | **partial** | The lower block is covered and ordered, but individual row→line identity beyond the exact L19 start is not asserted without renewed lexical image alignment. | Exact fine localization if consequential. |
| second lower `80` | second matching `80` in lower paragraph | `133:24`; `numerals.tsv`; D011 | **partial** | The second `80` is preserved and D011 retains promotion from tentative to observed. D011 does not distinguish exact physical source targets for the two occurrences. | Exact physical line of the second occurrence remains unasserted here. |
| conflict around legacy `133:15` | competing graphematic readings | D007 | **partial** | **Positive preservation:** variant history remains explicit rather than normalized away. | Physical-line equivalence requires re-localization if consequential. |
| upper economic passage | over-fluent reconstruction withdrawn | D008 target `133/upper` | **partial** | **Positive preservation:** withdrawal to unresolved survives; target is the broad `L01–L11` region rather than an internal exact locus. | Internal span(s) remain unspecified. |

### 62r coverage / completion result

All physical anchors `L01–L25`, all current `133.tsv` rows, both recorded `80` occurrences and D007/D008/D011 effects are accounted for. The cancellation’s deleted reading and any finer decision target are not guessed.

**62r COMPLETE for Checkpoint B — bounded unresolved target localization retained.**

Positive non-results:

- `80` remains a written numeral observation, not a forced interpretation;
- D007/D008/D011 preserve conflict, withdrawal and promotion history;
- the cancellation’s deleted wording remains unresolved rather than reconstructed for completeness.

Governing domains/requirements implicated: REQ-EDIT-002, REQ-EDIT-003, REQ-ARCH-009, REQ-PAL-001, REQ-PAL-005, REQ-PAL-006, REQ-PAL-007, REQ-GWP-002, REQ-GWP-004.

Request to #73: classify the eleven-line collapse, cancellation omission and decision-target precision; retain the observed `80` and revision-history cases as adequacy constraints.

---

# 5. fol. 62v / image 134 — COMPLETE with bounded unresolved boundary localization

Checkpoint-A source structure: `L01–L07`, `L08–L19`, `L20–L25`. Arabic `80` is visibly established at `L01`. No cancellation was observed at baseline level; this remains `not observed`, not proof of nonexistence.

| source anchor | visible/source observation | current representation | mapping | demonstrated loss / adequacy | uncertainty |
|---|---|---|---|---|---|
| `62v-L01–L07` | seven physical lines, first paragraph | single `134:01-07` unresolved record | **partial** | **Seven physical lines collapse into one legacy record.** Physical lineation is not reconstructable from that row alone. | Full reading remains unresolved. |
| `62v-L01` | visible Arabic `80` | `134:01-07` only says paragraph contains economic notation; no 62v `80` entry in current `numerals.tsv` | **partial** | **The source-visible `80` is not explicitly localized as its own written sign in current 62v research data.** | Meaning/unit is not adjudicated. |
| `62v-L08–L19` | twelve physical lines, second paragraph | `134:08`, `134:09`, `134:10-18` | **partial** | Twelve physical lines are represented by three legacy records, one of them a broad ranged placeholder. Fine physical lineation is lost/collapsed. | Individual row→line correspondence is not inferred from numeric labels. |
| physical boundary `62v-L19 → L20` | paragraph 2 ends at L19; paragraph 3 begins L20 | legacy region changes to `paragraph-3` at `134:19` | **ambiguous** | The mismatch demonstrates that legacy numeric IDs are unsafe as physical-line identifiers. Exact treatment of physical L19 cannot be reconstructed from IDs alone. | It is not established here which legacy fragment contains physical L19. |
| `62v-L20–L25` | six physical lines, third paragraph | `134:19–24`, six ordered paragraph-3 records | **partial** | Block coverage is structurally compatible, but one-to-one mapping is not promoted after the demonstrated boundary offset. | Exact individual row→line identities remain pending if consequential. |
| unresolved land/property clauses | conservative unresolved source state | D009 target `134/multiple` | **ambiguous** | **Positive preservation:** earlier over-smoothed clauses were withdrawn. The target label does not recover the individual physical loci. | Exact affected source spans remain unresolved. |
| repeated surname material | several 134 occurrences/candidates | D010 includes page 134 only as part of a cross-page occurrence set | **ambiguous** | Candidate spellings and separation from historical identification survive; occurrence targets are not enumerated exactly. | Exact occurrence set/hand attribution remains unresolved. |

### 62v coverage / completion result

All physical anchors `L01–L25` and all current `134.tsv` records are accounted for as bounded source regions. The L19/L20 boundary problem is explicit rather than mechanically “corrected”. D009/D010 are included without manufacturing exact targets.

**62v COMPLETE for Checkpoint B — bounded unresolved boundary/target localization retained.**

Positive non-results:

- D009 preserves conservative unresolved state and rejects prior semantic smoothing;
- no deletion/addition structure is inferred from “no cancellation observed”;
- hand differentiation remains uninvestigated.

Governing domains/requirements implicated: REQ-EDIT-002, REQ-ARCH-009, REQ-PAL-001, REQ-PAL-006, REQ-PAL-007, REQ-GWP-002, REQ-GWP-004.

Request to #73: determine whether the line collapse, missing localized `80`, boundary ambiguity and decision-target coarseness are project-local incompleteness, existing-method consequences, or reusable information problems; do not preselect representation.

---

# 6. fol. 63r / image 135 — COMPLETE

Checkpoint-A source structure: `L01–L03` continuation; `L04` display heading; `L05–L11` new prose paragraph. Lower-left show-through is visible but has no demonstrated target-text obstruction.

| source anchor | visible/source observation | current representation | mapping | demonstrated loss / adequacy | uncertainty |
|---|---|---|---|---|---|
| `63r-L01–L03` | three continuation lines | `135:01–03`, all observed after direct reinspection | **exact** | Source order and diplomatic line coverage are preserved. **No demonstrated loss.** | No new reading adjudication. |
| `63r-L02` monetary word | written `acht pfennig` in current reading | `135:02`; `numerals.tsv` records `pfennig` observed | **exact** | **Positive preservation:** source reading and palaeographic/economic note agree without forcing normalization. | None material for Checkpoint B. |
| `63r-L04` | display heading/new section boundary | `135:04` `[large new heading begins]`, observed | **exact anchor; content partial** | Section boundary is preserved while heading text is intentionally not invented. **Research incompleteness, not false completion.** | Heading wording remains unresolved/not transcribed. |
| `63r-L05–L11` | seven validated physical text lines | no rows in `135.tsv` | **exact source range → absent legacy coverage** | **Seven visible physical text lines are absent from the current legacy transcription.** This is a demonstrated completeness loss. | Their readings are not supplied merely to complete Checkpoint B. |
| lower-left show-through | visible background/show-through without target-text obstruction | no transcription record | **exact observation; no text target** | **No demonstrated semantic loss.** Omission from diplomatic text is not established as a failure. | Material effect remains unestablished. |

### 63r coverage / completion result

All physical anchors `L01–L11` and all current `135.tsv` records are accounted for. The seven uncovered lines are recorded as absence, not silently filled.

**63r COMPLETE for Checkpoint B.**

Positive non-results:

- `63r-L01–L03` is an adequacy fixture for exact ordered coverage;
- `63r-L04` correctly preserves an unresolved heading boundary without invented text;
- show-through has no demonstrated textual consequence;
- no hand shift or additional source stream is inferred.

Governing domains/requirements implicated: REQ-EDIT-002, REQ-GWP-002, REQ-RSE-007; REQ-EDIT-003 only if a later material/textual effect of show-through is demonstrated.

Request to #73: determine whether L05–L11 is only incomplete project transcription or also a reusable completeness/falsification fixture; retain L01–L04 as positive adequacy evidence.

---

# 7. D001–D011 apparatus cross-check — COMPLETE

The apparatus is **not** a wholesale failure. All eleven rows preserve a materially useful previous/current/status/reason/evidence/remaining-uncertainty record. The demonstrated weakness is source-target precision against validated physical anchors.

| decision | current target | recoverable source target | mapping | previous/current/rejected state preserved? | reason/evidence history reconstructable? | Checkpoint-B result |
|---|---|---|---|---|---|---|
| D001 | `132/name occurrence` | bounded to 61v; more than one `wolff` occurrence exists in `132.tsv` | **ambiguous** | **yes** | **yes** | `welch → wolff` rejection survives, but the exact source occurrence is not recoverable from the target string alone. “Same-hand” wording is not accepted as established hand attribution. |
| D002 | `132/place after filial` | legacy `132:01`, within physical `61v-L02–L03` introduction | **partial** | **yes** | **yes** | Earlier `kirchen` rejection and `Laßgaw/Laßkaw` uncertainty survive; exact physical line/span remains unasserted. |
| D003 | `132/surname occurrence` | bounded to 61v; repeated surname-like token occurs more than once | **ambiguous** | **yes** | **yes** | Rejection of `gemeindschafft` and surname variants survive; exact occurrence target is not encoded. |
| D004 | `132/top numeral` | legacy `132:01`; bounded to physical `61v-L02–L03` | **partial** | **yes** | **yes** | `2 → ij` revision survives; exact physical line/glyph span still requires source re-localization if consequential. |
| D005 | `132/18` | final 61v prose region `L17–L20`, exact line/span not established | **ambiguous** | **yes** | **yes** | Semantic proposal is explicitly rejected and `[U2]` retained unresolved; target precision is the limitation. |
| D006 | `132/18` | same bounded final 61v region | **ambiguous** | **yes** | **yes** | Second semantic proposal is likewise rejected without overwriting uncertainty; exact physical target remains ambiguous. |
| D007 | `133/15` | bounded to physical middle block `62r-L12–L18` | **partial** | **yes** | **yes** | Competing readings remain visible as variant history; exact physical-line equivalence is not assumed from legacy numbering. |
| D008 | `133/upper` | exact broad source region `62r-L01–L11` | **partial** | **yes** | **yes** | Withdrawal of fluent reconstruction to unresolved is reconstructable; internal target span(s) are not specified. |
| D009 | `134/multiple` | fol. 62v / multiple unresolved clauses, exact lines not enumerated | **ambiguous** | **yes** | **yes** | Withdrawal of over-smoothed clauses survives; individual physical targets are not recoverable from the location string. |
| D010 | `132/133/134 repeated surname token` | cross-folio occurrence set across 61v/62r/62v, individual occurrences not enumerated | **ambiguous** | **yes** | **yes** | Exact spelling candidates and separation from historical identification survive. Target occurrence set and hand identity remain unresolved. |
| D011 | `133/lower arabic number` | bounded to `62r-L19–L25`, where two `80` forms are recorded | **partial** | **yes** | **yes** | Promotion from tentative to observed survives and meaning/syntax remain unresolved; target string does not distinguish the two exact occurrences. |

### Apparatus result

- all D001–D011 have been cross-checked;
- previous/current/status/reason/evidence/residual-uncertainty information is materially reconstructable for all eleven rows;
- no decision row is discarded merely because its location is coarse;
- `unresolved`, `variant`, `rejected` and narrow `observed` outcomes remain valid scholarly states;
- the source-bound limitation is chiefly **target precision and dependence on non-physical legacy addressing**;
- no apparatus redesign is made here.

Governing domains/requirements implicated: REQ-ARCH-009, REQ-PAL-007, REQ-GWP-004, REQ-GWP-002, REQ-RSE-008.

Request to #73: determine what target precision is required for consequential decisions and which existing apparatus practices should explicitly remain unchanged because this fixture demonstrates adequacy.

---

# 8. Palaeography / notation cross-check

Current `numerals.tsv` positively preserves:

- `ij` as working at legacy `132:01`;
- Arabic `1` at `132:06;132:13`;
- Arabic `80` as observed twice in the 133 lower paragraph;
- W1–W6 as unresolved rather than invented values;
- comparison-source C2 notation with an explicit warning that hand identity with Reg. Ii 5 is not established and that comparison evidence is not direct grapheme proof.

Material limits:

1. legacy addresses such as `132:06` are not automatically physical-line addresses;
2. the Checkpoint-A-visible `80` at `62v-L01` is not localized as its own current 62v numeral observation;
3. any legacy note using “same-hand” language exceeds Checkpoint-A evidence until hand differentiation is actually investigated.

Current `lexicon.tsv` keeps historical identification separate and surname variants unresolved. No current-main `abbreviations.tsv` or `forms.tsv` exists at the project palaeography path; their mention in a handoff is not converted into a manuscript finding.

No new notation ontology or hand model is inferred.

---

# 9. Demonstrated loss classes and positive non-results

## Demonstrated source-bound loss / limit

1. **Physical-line collapse / non-physical legacy segmentation** — demonstrated on 61v, 62r and 62v.
2. **Spatial/source-order detail loss** — demonstrated for the 61v eight-line list/accounting structure versus six legacy list rows.
3. **Source-intervention loss** — confirmed cancellations at `61v-L16` and `62r-L18` are not explicit source phenomena in current legacy transcription.
4. **Visible-source omission/incompleteness** — `62v-L01` visible `80` is not separately localized in current 62v data; `63r-L05–L11` have no `135.tsv` coverage.
5. **Apparatus target coarseness** — D001–D011 preserve history, but multiple target strings cannot resolve to exact physical loci.
6. **Hand-evidence overreach risk** — convenience “same-hand” wording cannot be promoted while hand differentiation remains `not investigated`.

## Positive adequacy / non-loss findings

- `63r-L01–L03` preserve exact ordered line coverage.
- `63r-L04` preserves a section boundary without fabricating heading text.
- 62r `80` remains a written-sign observation separate from meaning/unit.
- W1–W6, U-states, variants and rejected readings remain unresolved/traceable rather than smoothed away.
- D005/D006/D008/D009 preserve explicit withdrawal/rejection of over-semantic or over-fluent proposals.
- D010 preserves surname candidates and keeps historical identification separate.
- D011 promotes only the numeral form while retaining uncertainty about surrounding meaning/syntax.
- no independent marginal/interlinear stream is required by current four-folio evidence.
- 63r show-through has no demonstrated target-text effect.
- absence of a baseline-observed cancellation on 62v/63r is not promoted to proof of nonexistence.
- hand differentiation remains `not investigated` rather than silently decided.
- stale/alternate handoff labels are an input-version issue, **not** a manuscript semantic-loss finding.

---

# 10. Existing requirements genuinely implicated

No new `REQ-*` is created here. Existing requirements implicated by the source findings include:

- REQ-ARCH-004 — folio/image/PDF/working identifiers remain distinct;
- REQ-ARCH-009 — consequential loci require unambiguous canonical addressing;
- REQ-PAL-001 — consequential uncertain signs are localized before completion;
- REQ-PAL-002 — palaeographic/comparison anchors remain exactly recoverable;
- REQ-PAL-003 — same-record/context and same-hand claims remain distinct;
- REQ-PAL-005 — written sign, abbreviation/expansion, normalization and identification remain distinct;
- REQ-PAL-006 — numeral/accounting notation may require distinct sign handling;
- REQ-PAL-007 — alternatives/rejections/residual uncertainty remain traceable;
- REQ-PHIL-002 — abbreviation sign and expansion remain distinct;
- REQ-PHIL-003 — segmentation uncertainty remains representable;
- REQ-EDIT-002 — folio, physical lineation and reading order survive where relevant;
- REQ-EDIT-003 — manuscript text/source phenomenon/editorial intervention remain distinct;
- REQ-GWP-002 — consequential evidence remains recoverable to exact Source/File/locus;
- REQ-GWP-004 — consequential revision/rejection history remains reconstructable;
- REQ-RSE-007 — representative semantic-loss testing precedes canonical migration;
- REQ-RSE-008 — transformations preserve provenance/decision history.

This list identifies governing domains only; it does not decide downstream consequence class.

---

# 11. #72 → #73 Domain Review handoff questions

#73 must independently determine, from this persisted source evidence and existing requirements/current owners first:

1. Which line-collapse/addressing findings are only project-local mapping work, and which instantiate an already-existing reusable scholarly information requirement?
2. Does current canonical method/ownership already support the two confirmed cancellation phenomena, or does their disappearance in legacy transcription expose a reusable representational gap?
3. Is the 61v spatial-list loss source-local, generally relevant, or both at different consequence levels?
4. Is the unlocalized `62v-L01` `80` incomplete project research or evidence of a reusable information-preservation problem?
5. Is `63r-L05–L11` only incomplete legacy transcription, or also a representative completeness/falsification fixture?
6. What target precision is required for consequential decisions given the D001–D011 results?
7. Which apparatus/status practices should explicitly remain unchanged because the fixture demonstrates adequacy?
8. Does legacy “same-hand” wording require project-local qualification, further palaeographic research, specialist escalation, or no action until consequential?
9. Which ambiguous mappings, if any, must be returned to #72 for more direct Source Research rather than generalized?
10. Only after those questions: does any finding establish a genuine reusable/deterministic gap suitable for a later scholarly→Dev handoff?

No answer to those Domain Review questions is preselected here.

---

# 12. Completion audit / stop boundary

| completion criterion | result |
|---|---|
| 61v mapped or explicitly bounded unresolved | **PASS** |
| 62r mapped or explicitly bounded unresolved | **PASS** |
| 62v mapped or explicitly bounded unresolved | **PASS** |
| 63r mapped or explicitly bounded unresolved | **PASS** |
| all current transcription rows accounted for | **PASS** |
| D001–D011 individually cross-checked | **PASS** |
| relevant numeral/lexicon records checked | **PASS** |
| demonstrated loss and adequacy cases explicit | **PASS** |
| unresolved states retained without guessing | **PASS** |
| no generic requirement/schema/Dev conclusion derived | **PASS** |

**#72 CHECKPOINT B COMPLETE — READY FOR #73 DOMAIN REVIEW.**

Remaining source-research uncertainties are deliberately bounded:

- exact W1–W6 readings/values and their fine physical-line localization;
- exact deleted wording/replacement relations at `61v-L16` and `62r-L18`;
- fine row→physical-line localization where legacy segmentation diverges;
- exact individual target spans/occurrence sets for several D001–D011 decisions;
- exact surname graphematics;
- hand differentiation/identity;
- heading text at `63r-L04` and readings of currently absent `63r-L05–L11`;
- other difficult U/N spans already retained as unresolved.

These unresolved questions do **not** block Domain Review because Checkpoint B's purpose is to demonstrate and bound semantic loss/adequacy, not to finish the diplomatic transcription.

The Source Research role stops here. The next action is **#73 Domain Review**. Any `needs further evidence` result must return an exact source question/anchor to #72/#64 rather than being guessed or designed around.