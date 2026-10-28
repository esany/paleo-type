# Conditional DEV-READY — one-flow archival preservation and canonical Source/File intake (2026-10-28)

**State: DEV-READY SPECIFICATION / NOT IMPLEMENTATION-ADMITTED.** This is a precise engineering work-order basis, not authorization to alter shared Source/Project/CORPUS semantics or to claim `savesax` runtime acceptance. Human's commission of **planning/work orders** is recorded; D-016 admission of material implementation remains a separate explicit owner decision.

**Concept:** [archival-preservation-corpus-intake-concept-2026-10-28.md](archival-preservation-corpus-intake-concept-2026-10-28.md).
**User-facing contract:** “Archivbestand lokal und im Repo sichern; optional Zotero.” An internally coherent handoff is mandatory; the Human must not invoke two skills or transport metadata.

## Current owner map / dependencies (resolve freshly at actual execution)

- `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, `methodology/workflow.md`, `methodology/maintenance.md`, `methodology/historical-source-workflow.md`, `methodology/source-and-provenance.md`, `methodology/project-lifecycle.md`.
- #271 / PR #332: Dresden acquisition skill and package producer; #282: controlled external productive runtime; #280: independent whole-system result review; #297 P0-equivalent still OPEN; #272: architecture/currentness audit.
- #69 (closed) already owns generic Source/File intake method; #309 (closed) is a *real failure and recovery* fixture; #277/#276/#281 (closed) are status, runtime and action-boundary regression sources; #268 (open) is **not** a licence to broaden the File/Source model.
- `tools/source_intake.py` is currently SHA-first **read-only**; `tools/source_contract.py` validates canonical `corpus/...` and `source-entry/...`; no second registry or derived current-status writer.
- `engineering/configuration.json` states no accepted new current-focus change. Do not piggyback on #271's Dresden-specific carrier as an implicit generic D-016 admission; keep a separate proposal branch/PR.

## Definition of ready and D-016 gate

**Ready for bounded implementation only if:**
1. Human Owner explicitly decides admission/limits of any *material* cross-owner automatic canonical writer / shared interface after comparing requirements/concept to #69/#309 and §D-016. If nothing material is added, document the owner-approved nonmaterial determination rather than manufacturing a new programme.
2. Fresh repository/branch/Issue/owner state and candidate run context available through the authorized GitHub connector; no checkout clone or scratch repo as authority.
3. The input package's trusted evidence and exact external persistence status can be verified; a package/manifest `complete` in CI/scratch cannot substitute for available external JPEG bytes when File registration asserts preservation.
4. Reliable client/tool access to the relevant **existing** Corpus/Source-entry read/validate/write owner, without inventing a new global data model.
5. Define tests of the host/skill dispatch and destination fitness separately from offline tests. If a host cannot load any skill, record `UNAVAILABLE`, not PASS.

## Implementation tasks (one cohesive block; no new roadmap or autonomous orchestrator)

**I. Contract adapter (archive-independent; base owner).**
- Accept a *resolved* source identity plus verified acquisition inventory from an existing provider. Use present `QUELLENINFO.json`, `ACQUISITION_STATE.json`, `SHA256SUMS.txt` and original bytes in an external controlled package; validate filename set, hashes, file completeness, original/derivative distinction, GUID granularity, rights basis, root path/identity and manifest consistency.
- Separate `catalogue/metadata K` from actual inspected File bytes and `P` manuscript observations; validate all consumed paths/tokens as untrusted.
- Pure read/preflight returns an explicit, reviewable intent/diff before any GitHub mutation. No need for a persistent parallel JSON transfer schema unless an existing interface cannot safely carry required provenance.

**II. Canonical repository materialization (existing contracts).**
- Match `corpus/sources.tsv` using evidence of exact archival identity; reuse existing Dresden `SSTA-ARCHIVIALE-8BDCE320` and Leipzig `SSTA-ARCHIVIALE-EDD69AA1` when applicable. Do not overwrite more-qualified Source facts with bare catalogue descriptions.
- Add/reconcile `corpus/files.tsv` only for independently proved, byte-exact original representations, one File identity per exact SHA, no fabricated side/folio, no duplicates and no PDF/JPEG flattening. Determine `storage_status` from actual controlled external preservation, not from HTTP status or local planned path; rights unknown is an explicit state, not permission for public redistribution.
- Apply source-wide relations/crosswalks only if independently evidenced; reference existing `source-entry/routes.tsv` with its current highest-sequence state. `UNRESOLVED` stays unresolved unless the Human authorizes a concrete route. No Project creation, research function, scholarly `NEXT ACTION`, or inspection checkpoints from downloading.
- Use exact GitHub connector online writes to intended branch, targeted canonical owners, contract CI. Each change is idempotent, conflict/partial-failure safe; no identical File row replicated on a second run. Do not push image bytes into public repository.

**III. Invisible end-user integration.**
- Archive-specific skill remains responsible for source route and bytes, a generic `source-intake` adapter/skill handles canonical mapping. The first skill must **actually invoke** a reliable shared interface, not merely suggest `$source-intake` or assume the host automatically discovers a second skill. A stand-alone explicit intake skill for existing packages is optional within the admitted scope.
- On natural language “Archivalie sichern”, check exact intended Source, existing package, current control and status before any side effect; then complete appropriate acquisition and repository registration. Read-only status must inspect each layer without triggering writes or retries. A failed GitHub phase leaves externally preserved files untouched and restartable without re-downloading.
- Report separate verified outcomes for external package, GitHub Source/File persisted and optional Zotero. No `complete` for the *whole user request* if required repo propagation is missing.

**IV. Zotero (OPTIONAL, not a core DoD gate).**
- Inspect an actual connected Zotero capability/API and target library and collection before suggesting a write. Human opt-in for bibliography and separately for attachments. Match a unique archival record, avoid duplicates, put archival title, repository Source ID, archive/signature, date and provider URL in Zotero fields suited to the verified item type. Do not claim that a Zotero item is canonical Source/File truth. Do not upload rights-unknown originals or large PDFs by default.
- If unavailable/not chosen, return `skipped` with no penalty to preservation+repo success; no speculative API auth flow, token handling or side effects as part of concept tests.

## Executable test matrix (DoD evidence)

| Gate | Scenario | PASS requires |
| --- | --- | --- |
| T0 | Fresh repo authority + provider/owner match | Exact branch/commit, canonical rules and owner state resolved; Dresden-only scope not extended to Leipzig merely by same host |
| T1 | Positive natural German source request, fresh independent host | Actual `savesax` loading/selection, authoritative source identity, correct list/bytes route, **actual** generic intake invocation, no manual two-skill handoff |
| T2 | Historical package reuse: Nr. 632 (135/135 verified) | Same Source and all canonical File IDs/SHA reused, no new acquisition, zero duplicates, legacy dated folder not renamed |
| T3 | Dresden Nr. 01739 (2 listed; 1 historical live byte sample) | Existing `sources.tsv` root reused; **no** `files.tsv` rows or full preservation success solely from a provider list/dry-run/one sample; only actual externally persisted verified files registered |
| T4 | New third archive provider and Reg. Ii PDF fixture | Identical generic intake rules without hardcoded SStA GUID/filename/PNG assumptions; exact byte/File matching, source grain and derivatives preserved |
| T5 | Unsafe metadata, wrong source GUID, no external storage, stale/corrupt/missing JPEG, unsupported list flags | No false `external-controlled`/complete, no fabricated Source/File rows or new Project; actionable error, preexisting package unharmed |
| T6 | Repeat, partial failure and recovery | GitHub write failure after complete external package leaves it intact; retry resumes **repo intake** only and verifies all existing IDs/rows; read-only preflight never mutates |
| T7 | Negative requests and conflicting context | `Status?`/transcription/wrong host/other archive branch never cause acquisition or canonical writes; Nr. 632 status does not replace Dresden Nr. 01739 |
| T8 | Source-entry/project authority | `UNRESOLVED` retained without project invention; no append-only invalid route, no coverage claim from merely checking JPEG bytes; material #268 composite-File case escalated without schema hacks |
| T9 | GitHub integrity + whole outcome review | Exact-head `tools/source_contract.py validate` and shared CI pass; host and external-package assertions **separately** evidenced; third-party fresh context can restart from repository + controlled file storage |
| T10 | Zotero option | Unavailable/opt-out → no calls; explicit opt-in + working connector → correct unique bibliographic entry, no unconsented JPEG uploads, rights and link semantics honest |

Test fixtures must preserve separate evidence levels: **static contract/CI**, **real host trigger/tool trace**, **real durable image bytes**, **actual GitHub commit/write**, **optional Zotero item ID**. No fixture or 174-test `savesax` CI PASS implies the rest.

## Hard STOP / return boundaries

- No controlled durable external target / unverifiable actual file bytes → no false Source/File preservation claim; return exact missing proof.
- Missing/contradictory archive/source identification or unsupported rights conclusion → do not guess; preserve existing truth and return the specific unresolved decision.
- Unauthorized Project/corpus schema or new shared semantic change → return to D-016 Human review / relevant owner; do not silently implement within a routine Skill patch.
- Source/File SHA identity collision, schema validation failure, concurrency conflict, old/new dated folder collision → fail closed, preserve old data and give the exact safe continuation.
- No GitHub connector permission → no local clone/HTTP alternative for canonical writes.
- Host skill unavailable → no claimed implicit invocation. Zotero unavailable → skip Zotero only.
- One failed action or unavailable runtime is **action-local**; it does not change Project priority or current scholarly target.

## Definition of done / owner return

1. Bounded admitted changes implemented only on dedicated PR with tests and exact commit; no change of accepted baselines or Source Contract unless separately reviewed/authorized.
2. Natural single-request **real** flow demonstrates already-saved case and new archive case: externally controlled verified originals → canonical Source/File rows and validated GitHub changes, with source identities unconfused, no manual second-skill user intervention and truthful partial result on failure.
3. No new research Project, priority, interpretation, folio claim, Zotero credential leakage or paid browser path.
4. `#271` receives only skill/provider interface findings; `#282` only runtime/destination findings; `#280` receives independent end-to-end acceptance evidence; `#297` priority unchanged; D-016 decision recorded if applicable. Do not close these owners by CI or planning deliverables.
5. If not all gates are executable, mark individual gates `UNVERIFIED`/`UNAVAILABLE`; report exact outstanding evidence/authority rather than force PASS.

**Next permissible action now:** Human review/disposition of proposal and, if material, D-016 implementation admission. Planning tickets may exist before admission; this document is not itself one.
