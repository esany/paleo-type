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

- **#271 canonical product/skill owner:** update currentness first with exact Dresden scope, known navigation/URL rule, no TinyFish default, new test, current PR and **productive acceptance OPEN**. Preserve old content as dated provenance; do not silently rewrite prior official test evidence.
- **#282 productive runtime owner:** unchanged requirements; add pointer that code-only PR cannot close durable storage acceptance. No invented destination.
- **#280 whole-system owner:** remain open for outcome-preserving, fresh-context behavior; record recurrence: another skill failure despite existing rule.
- **#297 assurance owner:** false-Lean check remains P0; record that a local sketch/CI may not be used to close the whole source package requirement.
- **#320:** closed earlier incident record stays closed; fresh regression is separate evidence under #271/#280, not pretext to reopen old incident.
- **PR #329:** historical review and general plan; its broad SStA scope and multiple older 'DEV READY' claims are **superseded as current execution guidance** by this document once verified on the new carrier. Retain linked evidence; do not merge an old plan in place of code.
- **PR #331:** standalone GUID diagnostic still unmerged and is **not** the coherent repair for this user case; preserve as optional historic/proposed diagnostic, not execution blocker.
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

**Implementation candidate:** [Draft PR #332](https://github.com/esany/paleo-type/pull/332), exact head `7bb47ac865b52a91e35ef006c292fbfe7fe05737` at first completed assurance. [GitHub Actions `source-contract` #689](https://github.com/esany/paleo-type/actions/runs/40581079304) / [validate job 122460296746](https://github.com/esany/paleo-type/actions/runs/40581079304/job/122460296746): **COMPLETED SUCCESS**, including the repository shared deterministic full check. Job log explicitly shows **167 Python tests** and both new cases `test_dresden_1303_record_preserves_exact_two_real_listed_jpegs` and `test_fullsize_from_nonsequential_list_never_invents_intermediate_names` as `ok`. This is **technical/fixture PASS**, not a Byte-/Runtime-/Human-PASS. No new helper API for parsing a thumbnail `src` exists on the branch; the known navigation ID pattern is implemented as a **skill routing rule** plus the tested existing provider's `fullsize` URL composition.

**Observed-vs-test provenance:** The exact two-entry Dresden `files.json` was observed from the official endpoint in the preceding ChatGPT case via a read/extraction tool; the current repair **did not start TinyFish or another metered archive-browser workflow**. The new test uses the explicitly written two-entry fixture in memory, **not a current live provider HTTP response**. It must therefore not be used to claim a new independent direct-HTTP or JPEG-byte verification. Similarly, previous Nr. 632 live list observation proves adapter inventory only, not preserved JPEGs.

**Defensible completed claim:** Skill contract now identifies Dresden and the known viewer/fullsize mapping, rejects metered browser default, preserves the existing external-save contract, and the existing provider plans exactly actual listed JPEG paths in the new regression cases. **Unfulfilled claims:** automatic activation in an arbitrary ChatGPT session, actual rendered thumbnail `src` from the full JS DOM of this particular record, direct JPEG bytes/completely decoded pixels, Atlas false-field interpretation, real persistent external acquisition, owner acceptance. These remain explicit in W2–W4 and must not be relabeled PASS because #689 passed.
