# G2 Domain Review — Checkpoint-B consequence classification

Status: **#73 DOMAIN REVIEW COMPLETE FOR CHECKPOINT-B FINDINGS — bounded G2 consequence set established; no implementation authorized.**

Reviewed: 2026-08-31

Upstream evidence fixture:

`projects/ega-reg-ii-5-knau/research/g2-checkpoint-b-semantic-loss.md`

Upstream completion commit:

`7d20d7b18e34c34cb3f4a3a166dc41889d371b9c`

Role boundary: this is #73 cross-disciplinary Domain Review. It classifies persisted source-bound findings. It does not redo Source Research, invent a new ontology/REQ family, authorize implementation, or claim independent specialist validation.

## 1. Review rule

For every finding this review applies:

`source-bound finding → demonstrated loss/adequacy → scholarly information established? → existing REQ-* → current canonical support → actual remaining gap → consequence class(es) → smallest justified action`

A missing legacy representation is not automatically a system defect. A deterministic/system consequence is admitted here only where:

1. the scholarly distinction is already sufficiently established;
2. existing canonical project data cannot preserve that distinction losslessly or address it reliably;
3. the distinction is already covered by reusable existing requirements and is materially needed beyond the single lexical reading.

No new `REQ-*` is created.

## 2. 61v Domain Review classification

| finding | source evidence / confidence | scholarly information established? | existing REQ-* / domain | current canonical support | demonstrated loss/risk | remaining gap | consequence classes | smallest action | needs #72 evidence? | senior/specialist? | Dev candidate? | acceptance evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eight physical list/accounting lines vs six legacy list rows | `61v-L04–L11`; **partial** legacy mapping, physical eight-line structure accepted | **yes** for physical line count/order; no for unresolved W1–W6 readings | REQ-EDIT-002; REQ-COD-004; REQ-ARCH-009; editing/codicology/archival addressing | Legacy `132:03–08` + `region=list` cannot encode one-to-one physical lineation | physical lineation and exact source targeting collapse | reusable ability to preserve canonical physical units/order is missing in current G2 legacy representation | source-local + project + **existing generic requirement instantiated** + **deterministic-system candidate** | carry this fixture into smallest G2 representation/admission step; do not solve W1–W6 to justify it | **no** for classification; later junior re-localization only when migrating exact rows | no specialist for structural fact | **yes**, bounded to unit/address preservation; no implementation authorization | candidate representation must preserve 8 ordered physical anchors and allow old six rows to map without pretending equivalence |
| Spatial alignment of left signs/quantities with list entries | `61v-L04–L11`; **partial**; alignment is accepted, individual sign readings unresolved | **yes** for existence/material spatial relation; no for individual sign values | REQ-COD-004; REQ-EDIT-002; REQ-PAL-006 | `region=list` + inline W1–W6 preserve existence but not recoverable eight-line spatial association | spatial/accounting relation cannot be reconstructed | reusable meaningful region/order/association support is missing for this fixture | source-local + project + **existing generic requirement instantiated** + **deterministic-system candidate** | preserve only the minimum source-order/spatial association demonstrated; no layout ontology | no for capability classification | specialist only later if a sign/value interpretation becomes consequential | **yes**, only for lossless structural association | round-trip fixture must distinguish the eight list lines and their associated sign/quantity positions without inventing values |
| Cancellation at `61v-L16` absent as explicit phenomenon | confirmed visible cancellation; **partial** mapping; deleted wording unresolved | **yes** that a cancellation exists at L16; **no** for deleted text/replacement relation | REQ-EDIT-003; REQ-COD-005; REQ-GWP-002 | current `132.tsv` has surviving text/fragments but no explicit source-phenomenon carrier | manuscript intervention disappears from canonical transcription data | current G2 legacy owner cannot losslessly preserve the established cancellation as a distinct phenomenon | source-local + project + **existing generic requirement instantiated** + **deterministic-system candidate**; unresolved textual content remains research | preserve phenomenon + uncertainty separately from reading; do not reconstruct deleted text | no for existence/classification; **yes later** only if deleted wording must be transcribed | cancellation/revision interpretation is senior scholarly work if consequential; independent specialist only if high-consequence unresolved judgement persists | **yes**, capability only | candidate representation must record cancellation at exact locus while permitting deleted content/replacement to remain unresolved |
| `61v-L12–L16` and final prose fine row→physical-line localization ambiguous | accepted bounded source blocks; **ambiguous/partial** | not fully for row-level equivalence | REQ-ARCH-009; REQ-PAL-001; REQ-GWP-002 | source block and legacy fragments exist; exact mappings not established | exact re-addressing of individual legacy fragments cannot yet be asserted | **evidence gap**, not automatically system gap beyond already-proven canonical addressing need | source-local + project + **needs further evidence when exact migration target is required** | defer exact row mapping until a concrete migration/re-addressing step; then return bounded anchors to junior #72 | **yes, conditionally**, only for exact row re-localization | senior only if re-localization requires difficult reading/segmentation adjudication | no additional Dev conclusion from the ambiguity itself | re-localization records exact/partial/ambiguous outcomes without forcing one-to-one mapping |
| U2 and D005/D006 rejected proposals survive | final 61v prose; **ambiguous target**, but decision state preserved | **yes** for rejection/unresolved history | REQ-PAL-007; REQ-EDIT-006; REQ-GWP-004 | decisions.tsv materially preserves previous/current/reason/evidence/uncertainty | no semantic-history loss demonstrated; target precision remains separate issue | no additional history model gap demonstrated by this case | source-local + project + **no additional action for decision-state semantics** | retain as positive regression fixture | no | no | **no** for decision-state/history semantics | future migration must preserve both rejected proposals and unresolved U2 state |
| W1–W6 remain unresolved | list block; unresolved values/readings | **no** for readings/values | REQ-PAL-006; REQ-AI-005 | unresolved states already preserved | no failure from unresolved outcome itself | scholarly reading work, not representation requirement discovery | source-local + project; **no system action** | continue G3/source research only when those signs matter to next gate | only if active research requires their readings | senior/metrological/palaeographic review if consequential; #76 only on genuine high-consequence unresolved specialist need | **no** | unresolved state remains valid and no guessed value enters canonical data |
| legacy “same-hand” wording | hand differentiation `not investigated` | **no** hand identity established | REQ-PAL-003; REQ-PAL-010 | prose/evidence wording can overstate support; method already forbids promotion | epistemic overreach risk, not demonstrated hand-model need | project qualification; hand model only on actual research trigger | project + methodological enforcement; **no current system/Dev gap established** | treat same-hand language as non-authoritative unless investigated; revisit only if hand evidence becomes consequential | yes only if a concrete hand claim is needed | senior palaeographic review; #76 if consequential independent validation is required | **no now** | no downstream claim treats record/context identity as established hand identity |

### 61v conclusion

61v does **not** require new generic requirements. It empirically instantiates already-canonical requirements for physical line/order preservation, meaningful layout/spatial association, exact consequential addressing, and separation of source phenomena from written/editorial text.

The deterministic/system candidates are therefore bounded capabilities already anticipated by existing requirements, not a Knau-derived ontology:

1. lossless canonical physical unit/locus addressing (`REQ-EDIT-002`, `REQ-ARCH-009`, `REQ-RSE-004`);
2. preservation of materially meaningful source order/spatial association (`REQ-COD-004`);
3. lossless distinct source-phenomenon representation for cancellation/intervention (`REQ-EDIT-003`, `REQ-COD-005`).

The unresolved W1–W6 readings, deleted wording, fine fragment mapping and hand identity are **not** prerequisites for recognizing those capability gaps.

---

## 3. 62r Domain Review classification

| finding | evidence/confidence | scholarly information established? | existing REQ-* | current support / loss | consequence | smallest action | #72 / specialist routing | Dev candidate? | acceptance evidence |
|---|---|---|---|---|---|---|---|---|---|
| `L01–L11` collapsed into one legacy record | eleven accepted physical lines → one bounded record; **partial** | yes for physical lineation; no for full text | REQ-EDIT-002; REQ-ARCH-009 | paragraph survives but internal line/address structure does not | project + existing generic requirement + deterministic-system candidate | include in same canonical physical unit/address solution as 61v | junior #72 later for actual line text/mapping; senior only for difficult readings | **yes**, same bounded addressing/unit capability | represent all 11 physical anchors without pretending current single record is one physical line |
| cancellation at `62r-L18` absent | confirmed source phenomenon; deleted word unresolved | yes for cancellation; no for deleted reading | REQ-EDIT-003; REQ-COD-005 | surviving text exists; intervention is absent | project + existing generic requirement + deterministic-system candidate | same minimum phenomenon capability as 61v | senior only if deleted/replacement interpretation becomes consequential | **yes**, shared phenomenon capability | exact locus can carry cancellation while deleted content remains unresolved |
| Arabic `80` at `L19` preserved | exact written-sign observation; meaning unresolved | yes for sign | REQ-PAL-005/006 | numeral record preserves sign separately from meaning | **adequate / no additional system action** | retain as positive regression fixture | no #72 need for form; specialist only for consequential value/unit interpretation | **no** | migration preserves written `80` without forced normalization/value |
| second lower `80` has coarser localization | sign preserved, exact physical occurrence not distinguished | yes sign exists; fine source target not exact | REQ-ARCH-009; REQ-PAL-006 | content adequate; address coarse | project re-localization + existing canonical-addressing gap; not a new notation gap | re-address during migration if consequential | junior #72 can localize occurrence; senior only if source reading ambiguity arises | only via **shared addressing candidate**, not a numeral-specific Dev item | both occurrences remain separately targetable after migration |
| D007 variant / D008 withdrawal / D011 promotion survive | decision history materially reconstructable | yes | REQ-PAL-007; REQ-EDIT-006; REQ-GWP-004 | history adequate, targets coarse | positive adequacy; target precision handled separately | preserve decision semantics unchanged; re-address only as needed | junior source localization where non-adjudicative; senior if target identification depends on reading judgement | **no new history-system gap** | previous/current/rejected/unresolved status remains reconstructable |

---

## 4. 62v Domain Review classification

| finding | evidence/confidence | scholarly information established? | existing REQ-* | current support / loss | consequence | smallest action | #72 / specialist routing | Dev candidate? | acceptance evidence |
|---|---|---|---|---|---|---|---|---|---|
| `L01–L07` and `L08–L19` strong physical-line collapse | accepted physical blocks; **partial** | yes for line counts/order; text incomplete | REQ-EDIT-002; REQ-COD-004; REQ-ARCH-009 | broad rows/placeholders lose physical unit structure | project + existing generic requirement + deterministic-system candidate | same shared physical-unit/address capability | junior #72 later for missing diplomatic lines | **yes**, shared capability only | all physical anchors can survive independently of unresolved readings |
| source-visible `80` at `L01` not separately localized | visible sign established | yes for written sign; no value/unit interpretation | REQ-PAL-006; REQ-GWP-002; REQ-ARCH-009 | current numerals data omit the established 62v occurrence | primarily **project-local research-data completion**; exact canonical targeting also exercises shared addressing gap | add/re-address this occurrence in project research when canonical target exists; do not invent meaning | junior #72 sufficient for sign occurrence; specialist only for consequential interpretation | **no numeral-specific Dev gap**; shared address capability only | project data contains 62v-L01 `80` as written sign with unresolved meaning permitted |
| physical `L19→L20` paragraph boundary conflicts with legacy numeric semantics | accepted source boundary; legacy `134:19` begins paragraph 3 | yes | REQ-EDIT-002; REQ-ARCH-009 | demonstrates legacy IDs cannot serve as physical line identities | strong acceptance/falsification evidence for shared canonical addressing/unit gap | preserve boundary independently from legacy IDs; map legacy rows as relations, not identities | exact row placement may later return to junior #72 | **yes**, shared addressing/unit candidate | migration must not convert legacy `134:19` mechanically into physical `L19` |
| D009/D010 retain unresolved/rejected/candidate state but coarse targets | history survives; target sets ambiguous | yes for decision states; exact occurrence sets incomplete | REQ-PAL-007; REQ-EDIT-006; REQ-GWP-004; REQ-ARCH-009 | no history loss, target coarseness remains | no new history gap; shared target-addressing issue | preserve history; re-localize target sets only where needed | junior for occurrence mapping; senior for graphematic/hand adjudication | shared addressing only | decisions remain reconstructable and can point to bounded/multiple canonical targets without false exactness |

---

## 5. 63r Domain Review classification

| finding | evidence/confidence | scholarly information established? | existing REQ-* | current support / loss | consequence | smallest action | #72 / specialist routing | Dev candidate? | acceptance evidence |
|---|---|---|---|---|---|---|---|---|---|
| `L01–L03` exact ordered coverage | **exact** | yes | REQ-EDIT-002 | adequate | **positive adequacy / no additional action** | retain as regression fixture | none | **no** | future representation reproduces ordered three-line coverage |
| `L04` heading boundary preserved while wording unresolved | exact boundary; content partial | yes boundary; no heading text | REQ-EDIT-002; REQ-AI-005 | adequate epistemic behavior | project research remains; no representation failure demonstrated by unresolved wording | transcribe heading later if G2 completion requires it; do not guess | junior first-pass if legible; senior if difficult | **no** | boundary survives and unresolved content remains explicit |
| visible `L05–L11` have no `135.tsv` coverage | exact source range absent from legacy | yes that seven text lines exist; readings not yet established | REQ-EDIT-002; REQ-EDIT-001; REQ-RSE-007 | **project transcription incomplete**; absence does not prove inability of future representation | project-level Source Research completion + useful semantic-loss/completeness fixture; **no independent system gap from omission alone** | return `63r-L05–L11` for bounded diplomatic transcription before G2 completion | **yes: junior Source Research** for first-pass coverage; senior only for difficult readings | **no**, except candidate representation must later accept the lines under already-established unit model | all seven lines receive explicit canonical coverage or explicit unresolved/gap state before G2 completion |
| lower-left show-through without demonstrated target-text effect | exact observation/no target obstruction | yes negative material result | REQ-COD-001/005 | omission from text is adequate | **no additional action** | retain negative finding | none | **no** | no phenomenon is created unless later evidence demonstrates textual/material effect |

---

## 6. Apparatus D001–D011 Domain Review

Checkpoint B establishes a strong non-result: the apparatus is **not semantically lost as a decision history**. Previous/current/rejected states, reasons/evidence and residual uncertainty are materially reconstructable for all D001–D011. This satisfies the core intent of REQ-PAL-007, REQ-EDIT-006 and REQ-GWP-004 sufficiently to reject a wholesale apparatus redesign.

The demonstrated weakness is target identity/precision:

- several targets are ad-hoc strings such as `132/name occurrence`, `133/upper`, `134/multiple`;
- repeated occurrences cannot always be distinguished;
- legacy line numbers cannot safely be equated with physical manuscript lines.

Classification:

- **project-level:** actual consequential decisions must eventually be re-addressed to canonical source loci/units;
- **generic/methodological:** already covered by REQ-ARCH-009, REQ-PAL-001/002, REQ-EDIT-006 and REQ-GWP-002/004;
- **deterministic-system candidate:** **yes, but only for canonical typed/referential decision targets**, as already anticipated by REQ-ARCH-009 and REQ-RSE-004;
- **no new apparatus-state/history requirement:** current decision-state semantics are an adequacy fixture;
- **needs further evidence:** only for individual decisions whose exact source target must be established during re-addressing. Domain Review does not require all D001–D011 to be pixel-relocalized now merely to justify the addressing capability.

Smallest action: a later admitted G2 representation must allow a decision to target an exact canonical locus/unit where evidence supports exactness, a bounded region/multiple targets where that is the honest scholarly state, and must retain existing decision history. It must not force false precision.

Junior/senior routing:

- junior #72: non-adjudicative occurrence/anchor re-localization;
- senior scholarly review: target determination that depends on difficult reading/segmentation/cancellation interpretation;
- #76 independent specialist: only if a consequential specialist judgement remains unresolved after scholarly review.

Acceptance evidence: D001–D011 must survive a representative migration/re-addressing fixture with previous/current/status/reason/evidence/residual uncertainty intact, while targets become canonically recoverable at the precision actually supported by the source.

---

## 7. Cross-folio consequence synthesis

### A. Existing requirements are sufficient; no new REQ is justified

Checkpoint B does not expose a missing scholarly requirement family. The material gaps are already covered, especially by:

- REQ-ARCH-009 — consequential loci require unambiguous canonical addressing;
- REQ-EDIT-002 — folio/page boundaries, physical lineation and reading order must survive;
- REQ-EDIT-003 — manuscript text, source phenomena and editorial interventions remain distinct;
- REQ-COD-004/005 — meaningful layout/reading order and material/source phenomena remain representable;
- REQ-PAL-005/006/007 — sign/expansion/normalization separation, notation handling, alternatives/rejections;
- REQ-GWP-002/004 — exact evidence provenance and reconstructable revisions;
- REQ-RSE-004/007/008 — stable scholarly references and semantic-loss-safe migration.

Therefore the Domain Review result is **operationalization/evidence for existing requirements**, not requirement invention.

### B. Bounded deterministic/research-system candidates established

The fixture is sufficient to establish three reusable technical-support needs, each already anticipated by existing REQ-*:

1. **Canonical source-unit/locus addressing and referential targets**
   - physical line/unit identities must be independent of legacy row IDs;
   - exact and bounded targets must be representable without false precision;
   - apparatus/claims/palaeography must be able to refer to those canonical targets.

2. **Lossless preservation of source structure that is materially meaningful**
   - ordered physical lines and relevant region/spatial association must survive;
   - 61v is the falsification fixture showing that flat rows + one `region` label are insufficient.

3. **Lossless distinction of source phenomena/interventions from written/editorial text**
   - at minimum the confirmed cancellation cases must survive as source phenomena while deleted text/replacement may remain unresolved.

These are **candidate Dev handoff subjects only**. This review does not choose tables, Line/Span ontologies, TEI, database structures or implementation technology and does not authorize implementation.

### C. Explicit no-Dev / project-research outcomes

No separate Dev item is justified for:

- resolving W1–W6/U/N readings;
- interpreting numeral values/units;
- transcribing missing `63r-L05–L11` (project Source Research);
- the omitted `62v-L01` `80` as such (project data completion, once targetable);
- hand attribution before a real consequential hand question exists;
- show-through with no demonstrated textual effect;
- decision history semantics already preserved by D001–D011;
- creating a full layout ontology, hand registry, notation ontology or apparatus database.

### D. Required Source Research returns

Domain Review does **not** reopen Checkpoint B globally. The following bounded research work is returned only as needed for G2 completion / re-addressing:

1. **Required before G2 textual completeness:** first-pass diplomatic coverage of `63r-L05–L11`; `63r-L04` wording if the G2 completeness policy requires heading text.
2. **Required when migrating/re-addressing consequential legacy records:** exact or honestly bounded row→physical-unit localization where Checkpoint B remains ambiguous, including relevant D001–D011 targets and the second 62r `80` occurrence.
3. **Not required for current representation classification:** W1–W6 values, deleted wording at 61v-L16/62r-L18, exact surname graphematics, hand attribution, difficult U/N spans.

### E. Senior/specialist routing

Senior scholarly review is required when returned source work crosses into difficult palaeographic reading, consequential segmentation, cancellation/revision interpretation, hand attribution, uncommon sign/abbreviation adjudication or conflicts among plausible readings.

Independent specialist #76 is **not triggered globally by Checkpoint B**. It becomes appropriate only for a genuinely consequential unresolved specialist judgement after AI-assisted Source Research/Domain Review, especially before publication/high-consequence claims.

---

## 8. Smallest bounded scholarship→Dev handoff candidate

If/when material implementation is admitted downstream, the evidence-supported handoff should be limited to:

### Demonstrated problem

Current legacy G2 data cannot losslessly preserve/referentially address all already-established physical source units, materially meaningful spatial/source-order structure, confirmed cancellation phenomena, and exact/bounded consequential decision targets.

### Evidence fixture

`projects/ega-reg-ii-5-knau/research/g2-checkpoint-b-semantic-loss.md`

Key falsification anchors:

- 61v `L04–L11`: 8 physical list lines vs 6 legacy rows + spatial sign relations;
- 61v `L16`: cancellation absent as phenomenon;
- 62r `L01–L11`: 11 physical lines collapsed into one row;
- 62r `L18`: cancellation absent;
- 62v `L19→L20`: legacy ID/physical-line mismatch;
- D001–D011: history survives but several targets are non-referential/coarse.

### Existing requirements

REQ-ARCH-009; REQ-EDIT-002; REQ-EDIT-003; REQ-COD-004; REQ-COD-005; REQ-GWP-002; REQ-GWP-004; REQ-RSE-004; REQ-RSE-007; REQ-RSE-008.

### Minimum information that must survive

- canonical source + folio/locus identity;
- ordered physical source units sufficient for exact/bounded targeting;
- materially relevant region/order/spatial association without imposing unsupported geometry;
- source phenomenon/intervention distinct from reading/editorial expansion/normalization;
- exact, bounded or multi-target decision references at the precision actually supported;
- existing previous/current/rejected/reason/evidence/residual-uncertainty history;
- mapping from legacy rows/targets so migration is auditable.

### Deterministic vs scholarly boundary

Deterministic:

- ID/reference integrity;
- ordering/link/mapping preservation;
- reproducible migration/derived views;
- decision-history completeness;
- semantic-loss regression fixtures.

Scholarly judgement:

- what the manuscript reads;
- where ambiguous legacy fragments map when source evidence underdetermines them;
- cancellation/deleted-text interpretation;
- sign/abbreviation/numeral meaning;
- hand identity;
- whether a source feature is materially meaningful beyond established fixtures.

### Non-goals

No universal ontology; no TEI/RDF/database mandate; no automatic resolution of readings; no hand registry; no notation ontology; no apparatus redesign; no forced exact target where evidence is bounded; no full-corpus migration before the vertical-slice acceptance test.

### Acceptance checks

A later candidate representation/implementation must demonstrate on the Reg. Ii 5 fixture that:

1. 61v retains all 20 accepted physical anchors and preserves the eight-line list plus relevant sign/quantity association;
2. 61v-L16 and 62r-L18 can be represented as cancellations without requiring deleted wording to be resolved;
3. 62r L01–L11 are addressable as 11 physical units even while text may remain unresolved;
4. 62v L19→L20 cannot be corrupted by legacy numeric-ID equivalence;
5. 63r L01–L03 remain exact positive coverage and missing/new L05–L11 data can be added without a new addressing convention;
6. D001–D011 decision histories survive, and consequential targets can use canonical exact/bounded/multi-target references;
7. `unresolved`, rejected and variant states survive unchanged;
8. migration mapping is auditable and no manual parallel truth is introduced.

### Return path

Any implementation must return to #73/#64 for scholarly adequacy review before G2 is declared represented or migration proceeds beyond the fixture.

No implementation is authorized by this file.

---

## 9. Domain Review completion state / next action

**#73 CHECKPOINT-B DOMAIN REVIEW COMPLETE.**

Results:

- no new generic `REQ-*` justified;
- existing requirements are sufficient to describe the demonstrated scholarly needs;
- three bounded reusable deterministic support gaps are evidenced: canonical source-unit/target addressing, meaningful source-structure preservation, and explicit source-phenomenon/intervention preservation;
- apparatus decision-history semantics are positively adequate; target addressing is the reusable weakness;
- multiple findings remain project-local Source Research rather than Dev work;
- no global #76 specialist escalation is triggered;
- bounded junior/senior returns are explicit and do not reopen Checkpoint B.

**NEXT SCHOLARLY ACTION:** feed this classification to the #64 / GOV-M4 synthesis/admission path and, in parallel where allowed by #64 sequencing, return the explicitly required project-local G2 transcription completeness work (`63r-L05–L11`, and other exact re-localization only when needed) to #72. Do not begin implementation until the existing material-change admission path authorizes the bounded technical target.
