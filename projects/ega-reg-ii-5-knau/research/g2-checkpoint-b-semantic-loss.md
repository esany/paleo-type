# G2 Checkpoint B — legacy/apparatus semantic-loss mapping, Reg. Ii 5 fol. 61v–63r

Status: **Source Research evidence fixture for #64/#72. Sufficient for handoff to #73 Domain Review. No final G2 representation, generic requirement, schema, migration or Dev conclusion is made here.**

Date: 2026-08-30

## Authority and evidence boundary

This checkpoint compares the source structure already visually validated in Checkpoint A with the current `main` legacy transcription, apparatus and palaeographic records.

Governing chain:

`GOVERNING_OBJECTIVE.md → AGENTS.md → applicable REQ-* → authoritative methodology → canonical project/source state → inspected source evidence`

The exact source fixture is:

- Source: `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`
- File: `FILE-REG-II-5-00000129-EXCERPT`
- verified parent SHA-256: `e989fe614c715e417e3586e29628d67d274964f195b3f1e66a8682bfcde54f6f`
- fol. 61v → image 132 → PDF page 14 → `stat_derivate_00000416:/ThHStAW_RegIi_5_0130.tif`
- fol. 62r → image 133 → PDF page 15 → `stat_derivate_00000416:/ThHStAW_RegIi_5_0131.tif`
- fol. 62v → image 134 → PDF page 16 → `stat_derivate_00000416:/ThHStAW_RegIi_5_0132.tif`
- fol. 63r → image 135 → PDF page 17 → `stat_derivate_00000416:/ThHStAW_RegIi_5_0133.tif`

No literal image `urn:` has been established and none is inferred.

Checkpoint A passed direct source↔anchor structural review on these exact baselines. It establishes the physical/source-order fixture used here: 61v `L01–L20`, 62r `L01–L25`, 62v `L01–L25`, 63r `L01–L11`, including the source phenomena recorded there. This checkpoint does not re-adjudicate difficult readings, abbreviation expansions, hands or deleted wording merely to complete a mapping.

## Current-main input note

The execution handoff supplied to #72 contains historical/convenience fixture labels such as `K132-*`, a different D001–D011 description, and references to `palaeography/abbreviations.tsv` and `palaeography/forms.tsv`.

Current `main` is authoritative. It currently contains:

- `transcription/132.tsv`–`135.tsv` in the `page_id / line_id / region / reading / status / alternatives / evidence_note` form;
- `apparatus/decisions.tsv` with current D001–D011 beginning with the `welch → wolff` rejection and ending with the `80` observation;
- `palaeography/lexicon.tsv` and `palaeography/numerals.tsv`;
- no current `palaeography/abbreviations.tsv` or `palaeography/forms.tsv` at the project path.

The stale/alternate labels in the handoff are therefore **not silently reinterpreted as current records**. This is an input/version provenance limitation, not by itself a manuscript semantic-loss finding.

## Mapping-status vocabulary

- **exact** — the current record can be tied to one exact source anchor or exact bounded source range without guessing.
- **partial** — a bounded source region is established, but current representation collapses structure/content or does not support the finer source distinction.
- **ambiguous** — more than one source-local mapping remains plausible from the current evidence/legacy segmentation.
- **unresolved** — no responsible source-local mapping can currently be established.

Legacy `line_id` values are not assumed to be physical manuscript line numbers.

# 1. fol. 61v / image 132

Checkpoint-A source structure: `L01` heading; `L02–L03` introduction; `L04–L11` eight-line spatial list/accounting block; `L12–L16` prose; `L17–L20` second prose block. Cancellation is visibly established at `L16`. Left quantity/sign notation is part of the list block and spatially relevant.

| source anchor | current research representation | mapping | source-bound finding / limit | uncertainty | implicated existing REQ-* | provisional routing aid | request to #73 |
|---|---|---|---|---|---|---|---|
| `61v-L01` | `132:00`, heading `Knawe` | exact | Heading presence and source-order position are preserved. **No demonstrated semantic loss for the heading anchor itself.** | Reading was already carried as observed; no new reading adjudication here. | REQ-EDIT-002, REQ-GWP-002 | no further action / positive non-result | Confirm whether current support is adequate without new consequence. |
| `61v-L02–L03` | `132:01–02`, region `top` | partial | Two legacy top records correspond to the two-line introductory region, but this checkpoint does not infer that each legacy record boundary equals one physical line merely from numbering. | Exact row→line boundary remains unverified here; readings remain current working/variant state. | REQ-EDIT-002, REQ-GWP-002 | project consequence / needs further evidence | Decide whether block-level recoverability is sufficient for these non-consequential rows or whether later exact re-addressing is required. |
| `61v-L04–L11` | `132:03–08` + W1–W6 in `numerals.tsv` | partial | **Eight physical list lines are represented by only six legacy list rows.** The current row boundaries therefore cannot encode the validated physical lineation one-to-one. The existence of unresolved sign/value groups W1–W6 survives, but the full eight-line source structure does not. | Exact W1–W6→physical-line mapping must not be guessed from sequence alone. | REQ-EDIT-002, REQ-PAL-001, REQ-PAL-006, REQ-GWP-002 | possible project/generic relevance; #73 to classify | Determine consequence of the demonstrated physical-line collapse and whether current canonical owners can already preserve the needed distinction. |
| `61v-L04–L11`, left sign/quantity positions | `region=list`; inline W1–W6 placeholders; `numerals.tsv` | partial | The legacy records preserve that special numerical/economic tokens exist, but they do not by themselves reconstruct the validated eight-line spatial relation between left quantity/sign notation and written entries. | Exact individual sign readings remain unresolved; no independent marginal stream is established. | REQ-PAL-006, REQ-EDIT-002 | project consequence / possible method relevance | Determine whether the spatial relation is a reusable information requirement or only project-local source structure. |
| `61v-L12–L16` | legacy prose records within `132:09–15` | ambiguous | Five physical prose lines correspond to seven legacy prose fragments before the second source block. Legacy segmentation is therefore not physical lineation; exact individual row→line targets cannot responsibly be recovered from IDs alone. | Finer lexical mapping requires source-local line comparison; do not infer it mechanically. | REQ-ARCH-009, REQ-EDIT-002, REQ-GWP-002 | project consequence / needs further evidence | Decide which consequential legacy/apparatus objects actually require finer re-localization. |
| `61v-L16` cancellation | no explicit deletion/cancellation phenomenon in `132.tsv` | partial | **Visible source cancellation is absent as a typed source phenomenon in the current transcription.** A surviving reading alone cannot reconstruct that the manuscript contains cancellation at this physical line. | Deleted wording/replacement relation remains unresolved and is not supplied here. | REQ-EDIT-003, REQ-PAL-007 | possible generic-method/system relevance; #73 to classify | Determine whether existing method/current owner is sufficient or whether a reusable representational gap is demonstrated. |
| `61v-L17–L20` | `132:16–19` prose region | partial | Four legacy fragments occupy the final prose region, but earlier segmentation divergence means one-to-one physical-line identity must not be assumed without lexical image comparison. | U1/U2 and surname form remain unresolved/variant as currently recorded. | REQ-EDIT-002, REQ-GWP-002 | project consequence | Determine whether any consequential decision among these records needs exact source-line/span re-addressing. |
| unresolved U2 in the final prose | `132:18`; D005 and D006 | ambiguous | D005/D006 preserve two rejected semantic completions and retain `[U2]` unresolved. **Decision history is substantively preserved rather than smoothed away.** The limitation is the legacy target `132/18`, whose physical target is not yet exact. | Exact physical line/span for legacy `132:18` remains ambiguous. | REQ-PAL-007, REQ-GWP-004, REQ-ARCH-009 | positive non-result + addressing question | Preserve the successful rejection history; determine only whether target precision requires a downstream consequence. |
| comparison claims using “same-hand” wording in legacy notes/decision reasons | e.g. `132:09` evidence note; D001 reason | unresolved as hand claim | Checkpoint A explicitly records **hand differentiation = not investigated**. Existing “same-hand” convenience language therefore cannot be treated as established hand attribution in this checkpoint. | Whether the relevant forms are in fact same-hand requires palaeographic investigation outside Checkpoint B. | REQ-PAL-003 | source-research/specialist question, not demonstrated system failure | Decide whether the correct next step is project-local wording qualification, later palaeographic research, or no action until hand identity becomes consequential. |

### 61v positive non-results

- W1–W6 remain `unresolved`; Checkpoint B does not force numerical/economic completion.
- D005/D006 explicitly preserve rejected semantic proposals and residual uncertainty.
- No separate marginal/interlinear stream is introduced because Checkpoint A did not establish one.
- No hand attribution is promoted.

# 2. fol. 62r / image 133

Checkpoint-A structure: `L01–L11`, `L12–L18`, `L19–L25`. Cancellation at `L18`. Arabic `80` visibly established at `L19`; numeral records also preserve two clear `80` forms in the lower paragraph.

| source anchor | current research representation | mapping | source-bound finding / limit | uncertainty | implicated existing REQ-* | provisional routing aid | request to #73 |
|---|---|---|---|---|---|---|---|
| `62r-L01–L11` | one record `133:01-11`, unresolved upper passage | partial | **Eleven validated physical lines are collapsed into one legacy record.** The bounded source region is recoverable, but physical lineation and exact local targeting inside it are not. | Text remains intentionally unresolved; no rereading is forced. | REQ-EDIT-002, REQ-PAL-001, REQ-ARCH-009 | possible project/generic relevance | Classify whether the collapse demonstrates a reusable information requirement beyond this fixture. |
| `62r-L12–L18` | `133:12–18` | partial | The seven-row middle block matches the seven-line source block in extent, but individual ID equality is not promoted to exact physical-line identity without direct lexical line comparison. | Existing variant/working readings remain unchanged. | REQ-EDIT-002, REQ-GWP-002 | project consequence / mostly adequate | Determine whether only consequential rows require exact re-addressing. |
| `62r-L18` cancellation | `133:18` reading has no deletion/cancellation representation | partial | **The visible cancellation at L18 is not recoverable as a source phenomenon from the current legacy reading.** | Deleted reading remains unresolved; no interlinear replacement is established. | REQ-EDIT-003, REQ-PAL-007 | possible generic-method/system relevance; #73 to classify | Determine whether this is already covered by existing method/current owner or a reusable representational gap. |
| `62r-L19` | `133:19`, includes Arabic `80`; `numerals.tsv` records `80` observed | exact | The visible `80` at the beginning of L19 is preserved as a written numeral while the surrounding `[N1]`/syntax remains unresolved. **No demonstrated semantic loss for the numeral itself.** | Unit/meaning and surrounding syntax remain unresolved. | REQ-PAL-006, REQ-PAL-005 | no further action / positive non-result | Preserve separation of visible numeral from interpretation; determine no extra consequence unless another layer requires it. |
| lower paragraph `62r-L19–L25`, second `80` occurrence | `133:24`; `numerals.tsv`; D011 target `133/lower arabic number` | partial | The second `80` is retained in legacy/palaeography records, and D011 preserves the promotion from tentative to observed. However D011’s target string does not distinguish the two lower-paragraph `80` occurrences by exact physical locus. | Exact physical line of the second occurrence is not independently fixed here solely from legacy numbering. | REQ-ARCH-009, REQ-PAL-007, REQ-GWP-004 | positive history + addressing question | Determine whether consequential multi-occurrence decisions require exact distinguishable source targets. |
| `62r-L15` region | `133:15`; D007 | partial | D007 retains conflicting alternatives instead of normalizing them away. Its legacy target is more specific than `upper/lower` but is not treated as canonical physical-line identity in this audit. | Exact physical-line equivalence awaits source-local lexical alignment if consequential. | REQ-PAL-007, REQ-GWP-004 | positive non-result + project addressing | Preserve the variant history; classify only target-precision consequence. |
| `62r-L01–L11` | D008 target `133/upper` | partial | D008 successfully records withdrawal of an over-fluent reconstruction to unresolved. The research-state history is recoverable, but the target is only the whole upper region, not an exact internal locus. | Internal source span(s) responsible for the withdrawn reconstruction remain unspecified. | REQ-PAL-007, REQ-GWP-004, REQ-ARCH-009 | positive history + possible addressing relevance | Determine whether this decision needs finer target recovery before any migration/re-adjudication. |

### 62r positive non-results

- `80` is not normalized into a meaning/unit; visible sign and interpretation remain separate.
- D007/D008/D011 retain conflict, withdrawal and promotion history rather than smoothing the research record.
- The cancellation’s deleted reading remains unresolved rather than being reconstructed for completeness.

# 3. fol. 62v / image 134

Checkpoint-A structure: `L01–L07`, `L08–L19`, `L20–L25`. Arabic `80` is visibly established at `L01`. No cancellation was observed at baseline level; this remains `not observed`, not an absolute nonexistence claim.

| source anchor | current research representation | mapping | source-bound finding / limit | uncertainty | implicated existing REQ-* | provisional routing aid | request to #73 |
|---|---|---|---|---|---|---|---|
| `62v-L01–L07` | one record `134:01-07` | partial | **Seven physical lines are collapsed into one unresolved legacy record.** Physical lineation cannot be reconstructed from the record itself. | Full reading intentionally remains unresolved. | REQ-EDIT-002, REQ-PAL-001, REQ-ARCH-009 | possible project/generic relevance | Classify the lineation/addressability loss without preselecting representation. |
| `62v-L01`, visible Arabic `80` | `134:01-07` summary; no 62v `80` entry in current `numerals.tsv` | partial | **A source-visible numeral established by Checkpoint A is not explicitly preserved as a localized written sign in the current 62v legacy/palaeography representation.** It is only subsumed under a paragraph-level “economic notation” summary. | Meaning/unit is not adjudicated; only visibility of the written `80` is established. | REQ-PAL-006, REQ-PAL-001, REQ-GWP-002 | possible project/generic relevance | Determine whether this demonstrated omission is source-local research incompleteness or exposes a reusable representational requirement. |
| `62v-L08–L19` | `134:08`, `134:09`, `134:10-18` | partial | The twelve-line physical second paragraph is represented by two local rows plus one nine-ID range placeholder. Current boundaries do not provide a lossless one-to-one physical-line map for the paragraph. | Individual row→line correspondence beyond the bounded paragraph remains unverified; do not infer from labels. | REQ-EDIT-002, REQ-ARCH-009 | project consequence / possible generic relevance | Determine which exact distinctions must survive before any canonical migration. |
| boundary `62v-L19 → L20` | legacy region changes from `134:10-18` paragraph-2 to `134:19` paragraph-3 | ambiguous | Checkpoint A places paragraph 3 at physical `L20`, while legacy `region=paragraph-3` begins at legacy ID `19`. This directly demonstrates that legacy numeric IDs are not safe physical-line identifiers and leaves the exact treatment of physical `L19` unresolved in the current mapping. | It is not established here whether physical L19 is absorbed into the range placeholder or another legacy fragment. | REQ-EDIT-002, REQ-GWP-002, REQ-ARCH-009 | project consequence / needs further evidence | Determine whether further direct line-level mapping is required before downstream representation decisions. |
| `62v-L20–L25` | legacy `134:19–24`, six paragraph-3 rows | partial | The six-row legacy block is structurally compatible with the six physical lines of the third paragraph, but ID equality is offset by the demonstrated boundary difference and is not promoted to exact one-to-one mapping without lexical image alignment. | Exact individual row→line identities remain pending if consequential. | REQ-EDIT-002, REQ-GWP-002 | project consequence | Decide whether block-level mapping is sufficient for non-consequential rows. |
| multiple 62v unresolved land/property clauses | D009 target `134/multiple` | ambiguous | D009 preserves withdrawal of earlier over-smoothed clauses and the unresolved state. **The decision history itself is useful and should not be discarded**, but `134/multiple` does not identify exact physical line/span targets. | Exact loci of each withdrawn clause are not reconstructable from the target string alone. | REQ-PAL-007, REQ-GWP-004, REQ-ARCH-009 | positive history + addressing question | Determine required target precision for preserving D009 through future re-addressing/migration. |

### 62v positive non-results

- D009 preserves a conservative unresolved state and explicitly rejects earlier semantic smoothing.
- No deletion/addition model is inferred from the absence of a baseline-observed cancellation on this folio.
- Hand differentiation remains uninvestigated.

# 4. fol. 63r / image 135

Checkpoint-A structure: `L01–L03` continuation; `L04` display heading; `L05–L11` new prose paragraph. Faint lower-left show-through is visible but has no demonstrated obstruction of target text.

| source anchor | current research representation | mapping | source-bound finding / limit | uncertainty | implicated existing REQ-* | provisional routing aid | request to #73 |
|---|---|---|---|---|---|---|---|
| `63r-L01–L03` | `135:01–03` observed closing lines | exact | Physical continuation lines and their diplomatic readings are represented in source order. **No demonstrated lineation loss here.** | No new reading adjudication. | REQ-EDIT-002, REQ-GWP-002 | no further action / positive non-result | Treat as an adequacy fixture when evaluating any downstream change. |
| `63r-L04` | `135:04` `[large new heading begins]` | exact for source anchor; content partial | The section boundary/heading position is preserved, while heading text is intentionally not inferred. This is research incompleteness, not evidence that the legacy record falsely supplies a reading. | Heading reading remains unresolved/not transcribed here. | REQ-EDIT-002, REQ-AI-005 | source-local / continue research | Determine whether any further consequence exists beyond completing the source research later. |
| `63r-L05–L11` | no rows in `135.tsv` | exact source range → absent legacy coverage | **Seven validated physical text lines are absent from the current legacy transcription.** This is the clearest completeness loss in the four-folio fixture. | Their readings are not supplied in Checkpoint B; absence of legacy coverage is the finding. | REQ-EDIT-002, REQ-RSE-007, REQ-GWP-002 | project consequence / possible generic loss-test relevance | Determine whether this is solely incomplete project transcription or also evidence for a reusable completeness requirement. |
| lower-left blank-area show-through | no transcription record | exact observation; no textual target | **No demonstrated semantic loss.** Checkpoint A found no target-text obstruction and no separate text stream; omission from diplomatic text is therefore not established as a failure. | Material effect remains unestablished. | REQ-EDIT-003 only if later effect is shown | no further action / positive non-result | Do not turn show-through into a required phenomenon absent a demonstrated textual consequence. |

# 5. Apparatus / revision-history audit across the fixture

The current D001–D011 apparatus is a **strong partial historical record**, not an across-the-board failure.

| decision(s) | current target | mapping status | Checkpoint-B result |
|---|---|---|---|
| D001–D004 | human strings such as `132/name occurrence`, `132/place after filial`, `132/top numeral` | ambiguous / partial | Previous→current/rejected reasoning survives, but exact physical line/span targets are not encoded by the target strings. Preserve the history; do not treat legacy location strings as final physical addresses. |
| D005–D006 | `132/18` | ambiguous | Rejected semantic completions and residual `[U2]` uncertainty survive. Exact physical target is not safely reconstructable from legacy ID alone because 61v legacy segmentation is not physical lineation. |
| D007 | `133/15` | partial | Variant history survives. Exact physical line equivalence should be re-localized only if consequential. |
| D008 | `133/upper` | partial | Withdrawal of a fluent reconstruction is preserved; target resolves only to `62r-L01–L11` as a broad source region. |
| D009 | `134/multiple` | ambiguous | Withdrawal history is preserved, but the source targets are not individually recoverable from the target label. |
| D010 | `132/133/134 repeated surname token` | ambiguous | Candidate spellings and separation from historical identification survive. The occurrence set is not a list of exact source loci, and “same-hand” must not be inferred because hand differentiation is uninvestigated. |
| D011 | `133/lower arabic number` | partial | Promotion of visible `80` from tentative to observed survives, including residual uncertainty about meaning/syntax. The target does not distinguish the two lower-paragraph `80` occurrences. |

### Apparatus positive non-results

- Existing rejection/variant/observed history is materially useful and should remain reconstructable.
- `unresolved` survives as a legitimate research outcome.
- D005/D006/D008/D009 demonstrate that prior fluent/semantic proposals can be withdrawn rather than silently retained.
- D010 preserves multiple graphematic surname candidates and explicitly separates historical identification.
- D011 promotes only the observed numeral form while leaving meaning/syntax unresolved.

The demonstrated limitation is primarily **source-target precision and dependence on non-physical legacy addressing**, not wholesale absence of revision history.

# 6. Palaeography / notation audit

Current `numerals.tsv` usefully preserves:

- `ij` as working at legacy `132:01`;
- Arabic `1` at legacy `132:06;132:13`;
- Arabic `80` as observed in the 133 lower paragraph;
- W1–W6 as unresolved rather than invented values;
- comparison-source C2 notation with an explicit warning that hand identity is not established and the comparison is not direct grapheme proof.

Material limits demonstrated in this fixture:

1. legacy addresses such as `132:06` are not yet guaranteed physical-line addresses on 61v;
2. the visible `80` at `62v-L01` established in Checkpoint A is not localized as its own current 62v numeral observation;
3. any current note that says or presupposes “same-hand” exceeds Checkpoint-A evidence until hand differentiation is actually investigated.

No current-main `abbreviations.tsv` or `forms.tsv` exists at the project palaeography path. Their mention in the #72 execution handoff is not converted into a finding about the manuscript. If they were historical files, their provenance/intent must be established before they are treated as canonical research inputs.

# 7. Required positive non-results / no manufactured failures

The following are explicit Checkpoint-B outcomes:

- **adequate:** `63r-L01–L03` line/source-order representation;
- **adequate:** preservation of many alternatives, rejected readings and residual uncertainty in current transcription/apparatus;
- **adequate:** 62r `80` remains a written numeral observation separate from its unresolved meaning/unit;
- **adequate:** W/U placeholders retain unresolved states rather than forcing completion;
- **no demonstrated failure:** 63r show-through has no established textual effect;
- **no demonstrated failure:** no separate marginal/interlinear stream is required by the current four-folio evidence;
- **continue research, not system inference:** hand attribution remains `not investigated`;
- **continue research:** exact deleted wording at `61v-L16` and `62r-L18` remains unresolved;
- **not a manuscript-loss finding:** stale/alternate `K132-*`/D00* fixture labels and absent `abbreviations.tsv`/`forms.tsv` in the handoff conflict with current `main`; current main is retained as authority.

# 8. Material Checkpoint-B findings for Domain Review

The evidence above is sufficient to expose these source-bound problems without deciding their downstream class:

1. **physical-line collapse / non-physical legacy segmentation** — demonstrated on 61v, 62r and 62v;
2. **source-order/spatial-detail loss** — demonstrated in the 61v list where the eight-line spatial structure cannot be reconstructed from six legacy list rows alone;
3. **source-phenomenon loss** — confirmed cancellations at `61v-L16` and `62r-L18` are not represented as such in the legacy transcription;
4. **visible-source omission** — `62v-L01` visible `80` is not explicitly localized in current 62v research data, and `63r-L05–L11` are absent from `135.tsv`;
5. **apparatus target coarseness** — decision history survives well, but current location strings often cannot resolve to exact physical line/span targets;
6. **hand-evidence qualification** — legacy “same-hand” language cannot be treated as established while hand differentiation remains uninvestigated;
7. **positive adequacy fixtures** — unresolved/variant/rejection history and several exact source/readings survive and should constrain any later recommendation against unnecessary replacement.

# 9. Existing requirements implicated by the source findings

This Source Research checkpoint references only already-existing requirements that are directly implicated; it does not derive new requirements:

- REQ-ARCH-004 — keep folio/image/PDF/working identifiers distinct;
- REQ-ARCH-009 — consequential loci require unambiguous canonical addressing;
- REQ-PAL-001 — localize consequential uncertain sign/grapheme sequences;
- REQ-PAL-002 — comparison anchors must be exactly recoverable;
- REQ-PAL-003 — same-record/context and same-hand claims remain distinct;
- REQ-PAL-005 — written sign, abbreviation/expansion, normalization and identification remain separate;
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

# 10. Explicit #72 → #73 handoff questions

Domain Review #73 must determine, from the persisted source evidence above, **without presupposing storage design**:

1. Which demonstrated line-collapse/addressing findings are only project-local mapping work, and which instantiate an already-existing reusable scholarly information requirement?
2. Does the current canonical method/owner already have sufficient capacity for the two confirmed cancellation phenomena, or does their disappearance in legacy transcription constitute a reusable representational/system gap?
3. Is the 61v spatial-list loss a source-local layout requirement, a general G2 information requirement, or both at different consequence levels?
4. Is the missing `62v-L01` `80` merely incomplete project research, or evidence that a current canonical owner cannot preserve a source-visible sign distinctly enough?
5. Is `63r-L05–L11` simply incomplete legacy transcription, or does it also supply an acceptance/completeness fixture for a reusable requirement?
6. What precision must a consequential Decision target, given that D001–D011 preserve useful history but several current target strings cannot resolve to exact physical source loci?
7. Which parts of the existing apparatus/status practice should explicitly remain unchanged because the fixture demonstrates adequacy?
8. Does any “same-hand” legacy language require immediate project-local qualification, further palaeographic research, specialist escalation, or no action until hand identity becomes consequential?
9. Which mappings need additional direct Source Research before classification rather than being generalized from ambiguity?
10. Only after answering the above: does any finding establish a genuine deterministic/reusable system gap suitable for a later Dev handoff?

# 11. Completion / stop boundary

Checkpoint B is **sufficiently complete for Domain Review handoff** because it now provides exact source-bound evidence for material loss classes and important non-loss cases across all four folia without forcing resolution of difficult readings.

This Source Research role stops here before:

- final G2 Line/Span/Phenomenon semantics;
- generic requirement derivation;
- schema/table/field design;
- migration choice;
- Dev handoff;
- specialist-validation claims.

The next scholarly action is **#73 Domain Review of this fixture**. Any finding returned as `needs further evidence` comes back to #72/#64 for source research.