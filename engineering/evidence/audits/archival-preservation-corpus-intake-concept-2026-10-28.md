# Concept — archival preservation → canonical Source/File intake (2026-10-28)

**Status:** ANALYSIS / CONCEPT PROPOSAL, **NOT D-016 ADMITTED**; no Project activation or scholarly acceptance. **Scope split (2026-10-28): core skill #334 and entirely separate optional Zotero extension #337; Zotero is never a #334 gate.**
**Core Human-facing outcome (#334):** one command such as “Archivalie lokal und im Repo sichern” ends in (1) verified controlled external originals and (2) a traceable canonical Repository Source/File registration. A source can be Corpus-registered without a research Project. A separately requested and independently accepted Zotero bibliography extension is owned exclusively by #337, not this core result.

## Authority and owner fit

- Governing: `GOVERNING_OBJECTIVE.md`, `AGENTS.md`; workflow `methodology/workflow.md`; change admission `methodology/maintenance.md`.
- Existing METHOD: `methodology/historical-source-workflow.md` **Source/File intake precedes Project routing**; `methodology/source-and-provenance.md` owns provenance, exact File, rights and preservation meanings; `methodology/project-lifecycle.md` owns Project authority.
- Existing machine owners: `corpus/source-contract.json` + `tools/source_contract.py`; `corpus/sources.tsv`, `corpus/files.tsv`, `corpus/relationships.tsv`, `corpus/source-data/<source_id>/`; `source-entry/routes.tsv` under `source-entry/contract.json`; optional existing Project owners only after Human authority.
- Existing *read-only* SHA-first `tools/source_intake.py`, **not** a writer. Do not replace it with a new registry; add narrowly bounded, idempotent writing only if existing tools cannot complete the admitted task.
- Acquisition-provider side is independently owned by `savesax` / #271 (current Draft PR #332) and actual controlled external runtime #282. Overall evidence #280, system false-local-PASS #297, #272; historical intake #69 (closed), real transition failure #309 (closed), same-SHA/internal-Source model residual #268 (open). No priority/status or existing issue changed by this proposal.
- D-016 is material if the proposal introduces *new shared canonical-write semantics*, routing authority, cross-boundary automation or Source Contract changes. Planning a dev-ready gate is not permission to execute that scope; Human must explicitly admit any material portion before coding.

## Observed savesax defects, not hypothetical new architecture

1. **Host invocation failure:** A truly independent bare German archive-URL request did not load `savesax` (recorded in #271/#280). `allow_implicit_invocation: true`, AGENTS text, an explicit `$savesax` call or CI alone do not demonstrate real skill activation.
2. **Action/control boundary:** historical #277 — mere `Fertig?` triggered an unauthorized retry and disposable live CI acquisition; #276 — sandbox/DNS failure displaced a supported `files.json` source route; these incidents are resolved locally but remain required negative regressions. Current #282 still lacks proven production external destination/control.
3. **False completed outcome:** `tools/archival_source_acquisition.py` emits `complete` for its external package with `creates_corpus_rows: false`, not for Source/File registration. #309 showed a real Nr. 632 source-entry progression before corresponding canonical rows existed; that incident was later corrected. The independent existing 135/135 Nr. 632 package is a valid *historical* preservation fixture, not a new Dresden end-to-end PASS.
4. **Archive/Source confusion:** `savesax` is explicitly **Hauptstaatsarchiv Dresden only**; its shared provider or past Leipzig fixture does not authorize extending host skill scope. Dresden 10001 Nr. 01739 GUID `8bdce320-0ce6-4ddb-b37a-eed8fe52cb94` already has a **catalogue K-level Source** and `UNRESOLVED` route on main, but **no exact JPEG File rows** on main. Do not replace this with Nr. 632's 135 files or infer a current Project. One real live fullsize JPEG sample on #271 is not a complete externally preserved two-image package.
5. **Output/destination and naming:** no fixed OneDrive target in the skill; a controlled external destination is supplied/configured per authorized run. Draft PR #332 changes *new* package names to source-year prefix only and preserves legacy tracked package directories. Do not duplicate/rename historical OneDrive packages or promote a user-local path into public corpus truth.
6. **Risk of over-engineering:** the generic action is a small boundary adapter and owner-correct writes, not a second source database, job manager, universal archive scraper, proprietary Zotero truth store, or a complex chains-of-skills runtime.

## Target contract (concept; reuse existing emitted artifact shapes)

**Input:** Provenance-bearing acquisition result from any archive-specific provider:
- verified identity: archive, fonds, signature, title, source date label, official catalogue URL, provider record/digitalisat IDs **at their real granularities**, and concrete evidence/uncertainty;
- exact external package identity, durable reachable destination reference and current operation state, original image/file inventory, raw list checksum where relevant, acquisition route, each original filename + SHA-256 + byte completeness/inspection/coverage facts, preserved manifest/state/sidecar checks;
- rights/permission basis explicitly stated, separate from File preservation and publication authority; original vs PDF/render/crop derivative distinction.

For `savesax` these facts come from **JPEG originals**, `QUELLENINFO.json`, `QUELLENINFO.txt`, `SHA256SUMS.txt`, `ACQUISITION_STATE.json` and actual controlled external directory. No new generic schema must be made canonical merely to transfer them; implement the minimum validated adapter/view at the interface after D-016 disposition.

**Outputs:**
- `corpus/sources.tsv`: reuse an evidenced canonical Source node or add one at the *correct historical granularity* (catalogue K fact is not a manuscript reading); maintain provider identifiers and exact URL.
- `corpus/files.tsv`: one row for each **actually verified exact original File** with correct Source link, SHA-256, independent provider-image locator (not folio), `external-controlled` only if externally persisted/recoverable, honest `rights_status`. Do not fabricate hashes from list/count/URL; do not write image bytes into public repository.
- `corpus/relationships.tsv` and `corpus/source-data/<source_id>/`: **only if** Source relations/crosswalks are evidenced, not from viewer order.
- `source-entry/routes.tsv`: resolve already-authorized routing or preserve `UNRESOLVED` without auto-creating a Project or silently selecting `CORPUS_ONLY / NO_PROJECT_YET` (the latter requires explicit Human confirmation). Do not generate inspection-coverage rows for merely downloaded files; inspection and package verification are distinct.
- Project files: **never** create a Project, Source use, research function, relevant locus, priority or scholarly `NEXT ACTION` from a new download alone.
- Optional downstream extension (#337 only, **not part of this implementation's DoD**): a Zotero bibliographic item may later reference the canonical Source, only after separate opt-in and connector/rights checks. General bibliography development remains #13. No core build or test must depend on Zotero.

## User-facing orchestration

**Core (#334):** `ordinary archive preservation request → archive-specific skill/provider → validated durable acquisition package → generic Source/File intake → owner-correct GitHub writes + validation → one core result`. **Separately optional (#337):** a requested Zotero step may consume that completed result, but does not delay it or prevent closing #334.

The *host* must not be assumed able to invoke a second skill automatically: the archive-specific entry skill should orchestrate or invoke the generic **tool/interface** explicitly once an admitted stable interface exists; the generic `source-intake` skill may also be callable for **already preserved** packages, but only if host discovery/availability is demonstrated. Never demand that the Human hand-carry a manifest or name the next internal skill for the ordinary successful path.

Use a derivable **two-facet core completion report**: **external preservation** (`verified/partial/unverified`) and **repository Source/File registration** (`validated/unwritten/failed`). These are *presentation labels*, NOT a new canonical global state model. If a Zotero extension is separately authorized under #337, report its independent outcome without rewriting core success. If GitHub write fails after preserved files exist, preserve the original package, truthfully report partial overall result and restart from the owner-correct idempotent intake boundary. Pure status questions are read-only across **all** facets.

## Alternatives and dispositions

- **Fuse/reuse** existing #69 and #309 METHOD/Source Contract/routing; they already define semantics. Do not re-admit or redesign them.
- **Refine** narrow package→owner adapter and negative tests, potentially a new separate skill façade once runtime supports it.
- **Reject** making `savesax` a research Project manager; rejecting Zotero as authoritative Source/File store; automatic upload of rights-unknown PDFs/JPEGs; bulk import to public GitHub; fake persistent storage in CI/scratch; creating a new general source schema; adding paid browser route by default.
- **Defer** material #268 whole-root-File→internal-Source relation; if a real fixture reaches it, return to that owner rather than silently splitting or duplicating File identities.
- **Separate/optional #337:** Zotero implementation has its own API, target library/collection, duplicate-detection, rights and opt-in acceptance tests. The core may be completed, reviewed, merged and closed regardless of #337's status.

## Generic-fit and falsification

Test with (a) Dresden Nr. 01739 Source-on-main, no externally complete package yet; (b) **already externally preserved** Leipzig Nr. 632 with 135/135 SHA identities and canonical rows; (c) Reg. Ii known PDF exact-file match; (d) wholly new archive provider fixture not equating archive GUID with historical Source; (e) unsupported/partial/no-byte/corrupt, same SHA mismatch and untrusted rights/destination; (f) explicit non-acquisition status request.

Success is a third-party fresh context reconstructing **exactly what was actually preserved and registered** with no duplicate/download/Project selection, no source misidentification, no credential leakage and a one-phrase user flow; local CI and test fixture PASS remain narrower than actual host/runtime/GitHub acceptance.

**Current decision boundary:** concept proposal only. The accompanying DEV-READY plan is conditional until owner review under D-016 where material shared write/orchestration semantics would change.
