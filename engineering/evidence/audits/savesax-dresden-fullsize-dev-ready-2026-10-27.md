# savesax — Dresden fullsize / thumbnail routing: single current DEV-READY record

**Recorded:** 2026-10-27 · **Owner:** [#271](https://github.com/esany/paleo-type/issues/271) · **Base:** `main@ad577a38efd400017582b10a7f5b215e20a6d98f` · **Proposed carrier:** `fix/savesax-thumbnail-fullsize-contract-20261027`. This is **non-normative implementation/readiness evidence**, not a change to accepted method, Project scope/priority, research truth or D-016 implementation authority.

**Status at creation:** **skill/adapter workflow correction implemented on the development branch; final exact-head CI and fresh-context productive acceptance pending**. **DEV READY** means work can proceed within the existing bounded #271 owner. **Full image acquisition, platform skill auto-invocation and product acceptance are NOT PASSED.** An earlier PR, Issue or test label must never override this evidence ceiling.

## 1. Outcome locked before engineering slices

Human provides a **Hauptstaatsarchiv Dresden** archival URL at the exact HTTPS origin `https://www.archiv.sachsen.de` and expects the actual **online manually downloadable fullsize images** to be identified without guessing and saved completely to a controlled durable external folder with the verified source record, full hashes, image checks and restartable progress. The Human must not reconstruct internal viewer/CLI/browser choices.

No general SStA/Leipzig product expansion; no extra archival master-on-request/licence debate; no thumbnail/canvas screenshot accepted as high-resolution file; no automatic corpus/Project or scholarly acceptance. The existing generic adapter fixtures beyond Dresden are not thereby invalidated, but must not silently change the skill's explicit Human-facing scope.

## 2. Fresh authority and review reconcile

Freshly inspected on 2026-10-27: `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, `methodology/workflow.md`, `methodology/maintenance.md`, current `.agents/skills/savesax/SKILL.md` and its `agents/openai.yaml`, `tools/archival_source_acquisition.py`, `tests/test_archival_source_acquisition.py`, `docs/archival-source-acquisition.md`, and owner Issues **#271 / #282 / #280 / #297 / #320**. Parallel reviews **[PR #327](https://github.com/esany/paleo-type/pull/327)** (bounded D-016 admission *only on that PR*), **[PR #329](https://github.com/esany/paleo-type/pull/329)** (general/incomplete W0→W3 draft), and **[PR #331](https://github.com/esany/paleo-type/pull/331)** (GUID-only diagnostic, draft) were freshly compared. Their unchanged historical evidence is not product acceptance or a second current implementation plan.

**Currentness correction:** supersede the *execution instructions* in #329 where they tell us to reopen a general OpenSeadragon/DOM/provider-discovery question or treat any SStA archive branch as the same `savesax` scope. The provider may still support other records. PR #331 may remain a separate non-merged diagnostic proposal, but its live-or-offline `--inspect-guid` enhancement is not a prerequisite for the known Dresden fullsize mapping. Neither a second general plan nor a global shared workflow engine is warranted. Supersession does **not** destroy previous evidence, change Issue priority, close PR/Issue, grant another D-016 admission or imply previous negative cases are resolved.

## 3. Known technical facts vs open verification

| Fact/requirement | Grounding / claim limit |
| --- | --- |
| R1 exact URL routing | Standard archive route requires parsed HTTPS scheme + exact `www.archiv.sachsen.de` host; text merely *containing* that hostname is not a valid origin. No paid TinyFish/browser for known direct route. |
| R2 known viewer DOM | `.digitalisat-viewer-thumbnail.loaded.active` = currently selected thumbnail/navigation; `.openseadragon-wrapper` / `.openseadragon-container` = viewer. Initial HTML may show `#openseadragon` before JS renders thumbnail nodes. Absence of the dynamically inserted thumbnail in static HTML ≠ no archive image. |
| R3 preview to fullsize | Navigation `src=/digitalisate/<GUID>/fullsize/../preview/<NAME>.jpg` provides exact name; fetch actual bytes via `/digitalisate/<same GUID>/fullsize/<NAME>.jpg`. Existing provider already constructs the latter from list name; do not download preview/canvas as master. |
| R4 complete inventory | `/digitalisate/<verified GUID>/files.json`, not an active thumbnail, a count, a DOM screenshot, or adjacent guessed numbering, establishes inventory. Validate `name`, `typ`, flag, unique filenames, ordering, actual GUID. |
| R5 real Dresden two-image example | `10001 Ältere Urkunden Nr. 01739`, GUID `8bdce320-0ce6-4ddb-b37a-eed8fe52cb94`: live-listed `0002.jpg`, `0001.jpg`, both `jpg/true` on 2026-10-27; two sorted actual fullsize URLs. No `0003.jpg`. *Byte delivery not independently established.* |
| R6 historic Nr 632 | Earlier in-conversation live list for `edd69aa1-eae4-4970-a695-94aaeccd6724`: 135 `jpg/true`; repo fixture exact entries agreed. This is a **Leipzig** adapter case, not Dresden skill acceptance. |
| R7 ambiguous provider flag | `istEinzelbild=false` interpretation on atlas `c52a0351-970a-4896-a349-918c35636cfc`, reported 240/163/77, **UNVERIFIED**, no silent filtering / no blanket JPEG admission; case-specific live byte evidence before changing core logic. |
| R8 actual image integrity | HTTP text extraction's `empty_content` for a JPEG proves neither 404 nor corruption. Use byte-capable ordinary HTTP; validate JPEG SOI/SOF plus *actual complete decode/terminal marker* and measured pixels. Existing `jpeg_dimensions` only parses dimensions; complete-decode strengthening remains open. SHA-256 alone is acquired-byte identity, not source master authenticity. |
| R9 route/quality | Skill prefers publicly offered fullsize for this user task. Code supports `--route fullsize` and `download`; compare actual pixel/byte evidence before any claim that one is highest offered. |
| R10 controlled storage | Select/prerequisite a persistent external root (not repository/worktree, CI runner, Chat sandbox) and show state persistence, observation, stop, cancel, restart containment before bulk start; #282 owns productive proof. |
| R11 restart and finalization | `ACQUISITION_STATE.json` after each verified image; recorded verified image revalidation; missing/corrupt blocks; `QUELLENINFO.json`, `QUELLENINFO.txt`, `SHA256SUMS.txt` and progress must all be finalized before `complete`; status-only is read-only. |
| R12 provenance and claims | Archive, fonds, signature, title/dating, original catalog URL, actual GUID, filenames, list hash, per-image SHA/pixels/route are attributable. No publication permission or Corpus/Project use inferred. |
| R13 skill runtime | Repository skill YAML `allow_implicit_invocation:true` does not establish that arbitrary ChatGPT session auto-registers it. Test in a genuinely supported fresh invocation context; absence is a separate platform-enforcement residual, not evidence archive unsupported. |
| R14 outcome return / no false Lean | #297/#280: a unit test or skill prose is not a successful user-level acquisition. One operator-facing response must return actual source/result/remaining gaps with evidence, not ask Human to choose internal tooling or drift into general DOM/prose. |

## 4. Bounded coherent implementation/change inventory

**This branch** revises the skill's actual activation/scoping/host-aware direct HTTP/no-metered-browser policy, the known thumbnail navigation and fullsize mapping, and the durable package contract. `docs/archival-source-acquisition.md` describes the same contract. `tests/test_archival_source_acquisition.py` adds direct provider-plan regression for the observed Dresden two-file source and a nonsequential list without guessed intermediates. Existing parser, restart, status, manifest and repository-only storage protections must remain intact.

**Not part of this branch:** new generic DOM-crawler architecture, new source-discovery backend, reinterpreting `istEinzelbild=false` without evidence, global skill registries/ChatGPT plugin installation, unapproved paid browser sessions, full productive download or modifying research/Corpus/Project owners. A proposed additional Python thumbnail helper was blocked by the GitHub connector safety check; **it was NOT committed or validated**, and the already-existing `SaechsischesStaatsarchivProvider.image_url` is sufficient for list-derived fullsize URLs.

## 5. Definition of Ready / execution gates

| Stage | Preconditions | Current assessment |
| --- | --- | --- |
| W0 — known-host source and inventory | Current repo+owner, standard origin, canonical catalogue, verified digitalisat identity/list, known viewer URL rule, non-metered fetch path | **READY for bounded source tests**; real record Nr 01739's two entries independently observed. Actual image JPEG bytes still unverified. |
| W1 — behavior-level skill/provider fix | Owner-local implementation, exact expected names, no paid browser fallback, safe route and runtime behavior, changed files under #271 | **IMPLEMENTED AS PR CANDIDATE; acceptance subject to exact-head CI/review**. No proof of automatic skill use. |
| W2 — measured images and regressions | Full suite, discriminating direct HTTP 1–2 JPG samples, pixel/byte integrity, nonsequential/one-image/flag-negative, fresh-context user URL invocation | **PARTIAL** until actual HTTP JPEG bytes and fresh-context behavior checked; tests do not replace these. |
| W3 — productive preservation (#271/#282) | Authorized durable external destination, observable cancel/resume/persistence and full download | **NOT READY** absent verified destination/runtime and start. |
| W4 — whole-system result (#280/#297) | Genuine user-flow E2E outcome and accountable acceptance owner | **OPEN**; no completion/closure claims. |

## 6. Test/quality protocol

1. **Code review:** compare exact branch diff to main. Assert no extra scope, status mutation, fabricated images, unlicensed/premium-browser gate, Corpus/Project mutation, skill scope expansion to Leipzig.
2. **Deterministic:** execute `python tools/check.py` (repository shared assurance) at the **exact final PR HEAD**; inspect run/job/log, total tests and named discriminating cases. Older CI on prior commits does not count.
3. **Source probes (only bounded direct ordinary HTTP):** for `8bdce320...`, independently GET `files.json`, verify two exact names and GUID/cat linkage; GET one real `fullsize/0001.jpg` as **bytes** to validate HTTP status, content type, SOI/EOI, complete decode, pixels. If this runtime lacks byte access, label precisely **UNVERIFIED**, not 'provider unavailable'. Do not use TinyFish.
4. **Regression negatives:** reject constructed `0003.jpg` on two-file source and nonexistent intermediate on non-contiguous names; no preview-as-preserved-file; unsupported `istEinzelbild=false` fails explicitly rather than silently omits; corrupted JPEG and cancellation/resume; `--status` does not mutate.
5. **Fresh-context runtime qualification:** Human gives only official Dresden URL; assistant loads actual skill and automatically follows list→fullsize→external package where host registration permits; no HTML class excavation, no metered-browser detour, no hidden metadata-only fallback.
6. **External package acceptance:** only on a fit intended persistent destination; verify all expected JPEG hashes, pixel sizes and generated sidecars against actual file list; confirm retrievable after restart and stop/resume. No prior CI may substitute.
7. **Claim ceiling:** separate 'reproduced / implemented / deterministic PASS / live JPEG verified / externally secured / accepted', return explicit owner and residual for all failures.

## 7. Issue/PR reconciliation and next executable action

- **#271 canonical product/skill owner:** **UPDATED** with exact Dresden scope, known navigation/URL rule, no TinyFish default, current [PR #332](https://github.com/esany/paleo-type/pull/332), fixture/test boundaries; renamed to reflect Dresden fullsize, retains **productive acceptance OPEN**. Historical issue content preserved below currentness.
- **#271 previous real-package evidence:** historic Nr. 632 **135/135 controlled package PASS** at its narrower previous target; keep it distinct from an unverified current archive/host and the unverified Atlas mixed-mode case.
- **#282 productive runtime owner:** **UPDATED** with a currentness pointer to PR #332, explicitly retains productive storage/runtime requirements OPEN. No invented destination.
- **#280 whole-system owner:** **UPDATED** with the recurrence despite existing rules; remains OPEN for a fresh-context Human outcome and controlled runtime/package proof.
- **#297 assurance owner:** **UPDATED** with the false-PASS recurrence and PR #332 pointer; remains P0-equivalent and OPEN.
- **#320:** closed earlier incident record stays closed; fresh regression is separate evidence under #271/#280, not pretext to reopen old incident.
- **PR #329:** **CLOSED / UNMERGED / SUPERSEDED BY #332** as a current implementation/DEV-plan carrier on 2026-10-27. Generalized SStA guidance and older 'DEV READY' statements are historical review evidence only. Do not reactivate as an independent execution plan.
- **PR #331:** **CLOSED / UNMERGED / SUPERSEDED BY #332** on 2026-10-27. Its GUID-only diagnostic and prior 170-test remote PASS were candidate evidence, **not merged into main and not the coherent Human-outcome repair**. Retain its audit trail, not its old execution cursor.
- **PR #327:** scoped D-016 return gate remains parallel, unmerged, and no authority transfers to #271.

**Single next executable step after PR verification:** review/merge only via proper owner; test a direct *byte-capable* fullsize HTTP sample and fresh-context Dresden URL invocation, then preflight the actual external destination for the separate deliberate productive acquisition. Until then report **DEV-READY scoped branch** and **PRODUCT OUTCOME OPEN**; no fabricated URL / package or automatic host registration claim.

### Outcome-return tuple

**Outcome:** human archive URL → all genuine publicly downloadable fullsize originals → verified enduring source package.  
**Semantics:** thumbnail navigation ≠ preview image as original ≠ fullsize bytes; list vs guessed count; adapter scope vs Dresden skill scope; technical PASS vs preserved and accepted.  
**Coupled owners:** #271 (source and skill), #282 (runtime/destination), #280 (whole-system), #297 (adequacy).  
**Authority:** bounded #271 skill/docs/tests only; no new architecture/D-016, rights, research or Project mutation.  
**DoR:** exact live source/list + current owner and branch + testable host-aware rule.  
**DoD:** actual output images and sidecar completeness at durable destination, verified hashes/pixels, truthful UI, owner acceptance.  
**Residual/return:** true live fullsize bytes, `false` semantics for other cases, platform invocation, persistent target, clean E2E.  
**Claim ceiling:** branch code and deterministic tests only until evidence proves more.

## 8. Exact-head assurance result and final readiness check — 2026-10-27

**Implementation candidate:** [Draft PR #332](https://github.com/esany/paleo-type/pull/332). First technical assurance `7bb47ac865b52a91e35ef006c292fbfe7fe05737`: [Actions #689](https://github.com/esany/paleo-type/actions/runs/40581079304) / [validate job 122460296746](https://github.com/esany/paleo-type/actions/runs/40581079304/job/122460296746) **SUCCESS**. Second assurance after requirements/issue reconciliation `62c43ec77f0f3a220f59ae2d12bb056934aef10f`: [Actions #690](https://github.com/esany/paleo-type/actions/runs/40581528374) / [validate job 122461885886](https://github.com/esany/paleo-type/actions/runs/40581528374/job/122461885886) **SUCCESS**. For the *final current HEAD* test status, check [PR #332 checks](https://github.com/esany/paleo-type/pull/332/checks), not a previous commit's run. Job log explicitly shows **167 Python tests** and both new cases `test_dresden_1303_record_preserves_exact_two_real_listed_jpegs` and `test_fullsize_from_nonsequential_list_never_invents_intermediate_names` as `ok`. This is **technical/fixture PASS**, not a Byte-/Runtime-/Human-PASS. No new helper API for parsing a thumbnail `src` exists on the branch; the known navigation ID pattern is implemented as a **skill routing rule** plus the tested existing provider's `fullsize` URL composition.

**Observed-vs-test provenance:** The exact two-entry Dresden `files.json` was observed from the official endpoint in the preceding ChatGPT case via a read/extraction tool; the current repair **did not start TinyFish or another metered archive-browser workflow**. The new test uses the explicitly written two-entry fixture in memory, **not a current live provider HTTP response**. It must therefore not be used to claim a new independent direct-HTTP or JPEG-byte verification. For Nr. 632, preserve **both** the earlier 135-entry provider list evidence **and** the independently checked [135/135 real OneDrive source package and matching SHA-256/sidecars](https://github.com/esany/paleo-type/issues/271#issuecomment-6046567327). The verified package is an established historic **Leipzig preservation PASS**, not fresh Dresden skill invocation or Atlas acceptance. Do not redownload Nr. 632 merely for another technical test.

**Defensible completed claim:** Skill contract now identifies Dresden and the known viewer/fullsize mapping, rejects metered browser default, preserves the existing external-save contract, and the existing provider plans exactly actual listed JPEG paths in the new regression cases. **Unfulfilled claims:** automatic activation in an arbitrary ChatGPT session, actual rendered thumbnail `src` from the full JS DOM of this particular record, direct JPEG bytes/completely decoded pixels, Atlas false-field interpretation, real persistent external acquisition, owner acceptance. These remain explicit in W2–W4 and must not be relabeled PASS because #689 passed.


## 9. Executed W0–W2 implementation return — 2026-10-28

**Current carrier:** draft PR #332, branch `fix/savesax-thumbnail-fullsize-contract-20261027`, product owner #271. This is the same canonical plan file as 2026-10-27, not a second DEV-READY owner. This addendum controls over the earlier "no downloader-core change" / "SOF decoder still open" statements **for this branch only**; earlier descriptions remain historical audit state.

**Implemented on this branch, not yet merged:**
- `AGENTS.md`: thin task-specific route for requested image preservation at `www.archiv.sachsen.de`, requiring positive **Hauptstaatsarchiv Dresden** branch evidence before loading `.agents/skills/savesax/SKILL.md`. User need not say "savesax"; status/read-only intent is not acquisition authorization. This reference cannot register a skill into a host.
- `.agents/skills/savesax/SKILL.md`: discoverable German verbs "sichern/speichern/herunterladen" and archive host; known thumbnail-navigation `src` → existing fullsize URL (no DOM rediscovery, no paid browser), true `files.json` inventory, external preservation and cancellation boundaries unchanged.
- `tools/archival_source_acquisition.py`: `jpeg_dimensions` now checks JPEG SOI/EOI and **fully decodes compressed pixels using Pillow**, returns measured dimensions and rejects corrupt/truncated data. This is invoked on every new and existing recorded JPEG. This is a genuine fidelity improvement but **not provider-authenticity verification**.
- `tools/requirements-archival-source-acquisition.txt` and `.github/workflows/source-contract.yml`: declare and install Pillow for deterministic test/decoder runtime. A productive runtime must independently install the same requirement before executing acquisition.
- `tests/test_archival_source_acquisition.py`: replaces old header-only pseudo-JPEG with a valid generated compressed image; adds malformed/truncated JPEG negatives. Earlier 2-image Dresden and nonconsecutive-name list cases stay covered. `docs/archival-source-acquisition.md` covers decoder prerequisite and separately verified historic Nr632 package.

**Executed source/runtime preflight:**
- Direct ordinary Python HTTPS `urlopen` for Dresden Nr01739 official `files.json` attempted in the available execution container; it fails at local DNS resolution: `URLError: [Errno -3] Temporary failure in name resolution`. This is **P01 local runtime FAIL / provider availability UNVERIFIED**; no inference that the archive is broken. No TinyFish, browser-agent, fullsize byte fetch or productive download started.
- Actual session skill catalogue freshly inspected using the available skills interface: 60 mounted skills, **no `savesax`**. Thus this ChatGPT session cannot establish H00/H01 implicit host invocation and must not claim it. `allow_implicit_invocation: true` in repo metadata is not runtime registration. A fresh compatible repo-aware host remains required.
- The two-source-ID Dresden `files.json` list and the verified historical 135/135 Nr632 OneDrive package remain existing **separate evidence states**, not new JPEG-byte tests.

**CI investigation/evidence, not hidden:** [source-contract run 40648913645](https://github.com/esany/paleo-type/actions/runs/40648913645) **FAILED** after first decoder change because the embedded base64 "valid JPEG" fixture was actually invalid (one failure and seven errors). Replaced it with Pillow-generated real compressed JPEG test data. [source-contract run 40649123595](https://github.com/esany/paleo-type/actions/runs/40649123595) on commit `e40601fd371fbe98c1d5be850a603fe421fc70cc` **SUCCESS**, shared full check **167 tests**, including new Dresden/list and real JPEG negative checks. **Re-check exact final head CI after further writes**, and do not count the earlier green run as final-head evidence.

**Honest quality ceiling:** Code/skill/routing and stronger deterministic JPEG checks implemented; no actual remote JPEG bytes, no true one-image / mixed `istEinzelbild=false` provider proof, no fresh external host automatic trigger, no suitable new persistent runtime/destination or new completed package. Existing older Nr632 135/135 externally secured evidence is not downgraded or rerun.


## 10. P00–P12 and H00–H05: execution disposition (single owner)

The earlier [independent P00–P12 review](https://github.com/esany/paleo-type/pull/329#issuecomment-6440298605) remains valid input even though PR #329 was closed unmerged. **This table explicitly tracks the surviving gates without inventing acceptance.**

| Gate | Outcome / demonstrated evidence | Status as of this execution |
| --- | --- | --- |
| P00 repository/currentness | Read current governing files, #271/#282/#280/#297, main and PR #332; working branch identified; all repository writes GitHub connector | **PASS for this bounded execution; recheck at next run** |
| P01 capable direct provider runtime | Direct URL attempt failed at runtime DNS; no provider status returned | **RUNTIME FAIL / PROVIDER UNVERIFIED** |
| P02 catalogue vs digitalisat GUID | Earlier Dresden Nr01739 catalogue and 2-entry list observed; no new direct live GUID crosswalk | **PARTIAL** |
| P03 real one-image + Atlas lists | Existing 2-image Dresden case != one-image case; Atlas `c52a0351-...` true/false still unverified directly | **UNVERIFIED** |
| P04 live fullsize bytes/HTTP/decoder | No reachable byte HTTP host in this runtime | **UNVERIFIED**, not server failure |
| P05 `istEinzelbild=false` semantic | Existing parser still fails closed; no silently inferred JPEG support | **NO-GO for parser change** |
| P06 route/image quality/resume | Provider constructs `fullsize`; route + list hash bind saved plan; public actual fullsize quality not measured here | **TECHNICAL PARTIAL** |
| P07 complete JPEG decoding | Pillow decoder + SOI/EOI with tests; real provider sample pending | **IMPLEMENTED / DETERMINISTIC PASS on prior tested head; LIVE OPEN** |
| P08 natural URL-only to metadata/CLI | Skill text instructs seven catalogue fields + output path; no supported host invocation proved | **HOST UNVERIFIED** |
| P09 full regression set | Existing restart/status/sidecar tests plus Dresden list and new corrupt JPEG negatives; real mixed provider/HTTP responses not exercised | **PARTIAL** |
| P10 integrated skill/CI/host | Thin `AGENTS.md` referral, German skill discovery, decoder and requirement are on one PR; earlier CI success after red test; final head must pass | **IMPLEMENTED PR CANDIDATE; HOST OPEN** |
| P11 suitable external productive run | No verified new destination or stop/observe/containment preflight; historical OneDrive package remains intact | **NO-GO new bulk run (#282)** |
| P12 full real new package | No new acquisition; historical Nr632 external 135/135 package verified separately | **OPEN for current Dresden/Atlas; historic PASS retained** |

**Additional host/intent gates (a written skill is not invocation evidence):**

| Gate | What would prove it | Current disposition |
| --- | --- | --- |
| H00 installed skill | Host shows `savesax` path and actual loaded version | **FAIL in this conversation's mounted 60-skill catalogue; not a global host claim** |
| H01 implicit activation | Fresh compatible host receives German acquisition instruction plus URL, no skill-name hint, and actually loads skill | **UNVERIFIED** |
| H02 negative triggers | Host does not acquire for pure `Status?`, transcription, wrong host or Leipzig case with unverified branch | **UNVERIFIED** |
| H03 executable orchestration | Seven catalog facts from source, `--metadata -`, `--route fullsize`, correct list and fit root passed to live downloader | **UNVERIFIED** |
| H04 cost-aware route | Fresh trace demonstrates direct provider fetch and no TinyFish/DOM rediscovery | **NOT PROVED IN HOST**; this review itself used no TinyFish |
| H05 independent product outcome | Real destination state, images, SHA/decode, full source metadata, stop/restart, independent verification | **OPEN** |

**Claim ceiling:** The branch is DEV-IMPLEMENTED for the deterministic referral/decoder improvement; **the complete user outcome is still NOT product accepted or whole-system DEV READY for W3**. Host absence and direct HTTP DNS failure are **specific unavailable resources**, not a change to the Human's acquisition goal. No blanket architecture/D-016 claim or fresh one-image/Atlas truth is created.
