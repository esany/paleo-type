# Bugwave design closure — engineering configuration, identity and transitions — 2026-10-04

**Status:** NON-NORMATIVE DETAILED DESIGN / **#246 DESIGN COMPLETE / IMPLEMENTATION NOT ADMITTED**  
**Baseline:** `main@b633ac81f65952775d2d203b7b9986903d48365b`  
**Work owner:** #246; parent #244  
**Related proposed ADRs:** P-001, P-003, P-004, P-010 in `system-development-bugwave-adr-inventory-2026-10-04.md`  
**This file is not:** Current Configuration, D-016 admission, an implementation state store, a migration, or authority to make a proposed architecture current.

## 1. Problem closed by this design

The target EKCP already named a configuration owner, stable artifact IDs, lifecycle states and relations. That was not sufficient for implementation because it did not define precisely enough:

- what `current engineering configuration` means;
- which events/authorities may change it;
- how actual repository bytes/Git relate to semantic baselines without making chronology the semantic clock;
- how stable references survive moves/supersession;
- how proposed/admitted/implemented/verified/accepted remain distinct;
- how generated current-state views avoid becoming a second manually synchronized truth store.

Those semantics are fixed here before any target file/schema is created.

## 2. Configuration model: four distinct things

The implementation must keep these four layers distinct.

### 2.1 Actual repository configuration

The actual software/document configuration is the checked-out Git tree at a concrete commit/ref. Git owns byte/path history and exact repository snapshots.

A Git commit proves only that bytes changed. It does **not** by itself prove that a material target architecture was proposed, admitted, verified or accepted.

### 2.2 Accepted engineering baselines

An accepted engineering baseline identifies which accepted Requirements/architecture/decision artifacts define the currently accepted engineering meaning of the system.

This is the core responsibility of the future Engineering Configuration owner.

It does not enumerate every repository file and does not duplicate Git.

### 2.3 Proposed target/change state

A proposal/design/change can exist and be fully developed without becoming accepted/current. Proposed architecture belongs to the bounded change plus decision/ADR evidence, not the current baseline.

### 2.4 Work/review metadata

Issues, PRs, branches, CI runs and milestones expose work/review evidence. They may be referenced by a configuration transition, but their own state never becomes semantic currentness authority.

Therefore:

```text
Git tree != accepted engineering baseline
Issue/PR state != accepted engineering baseline
newest design != accepted engineering baseline
CI PASS != accepted engineering baseline
```

## 3. Stable engineering identity and references

### 3.1 Identity rule

Once an engineering artifact enters the managed plane, it receives an immutable logical `artifact_id`. Moving or renaming the file does not change that identity.

Candidate format:

```text
ENG-A-0001
ENG-A-0002
...
```

The numeric/string format is implementation detail; the invariant is stable uniqueness within the repository.

Legacy artifacts may be assigned IDs during classification/migration without implying that they were historically governed by the new system.

### 3.2 Reference classes

The implementation must distinguish reference purpose explicitly rather than overloading one free-text `ref`.

Minimum logical reference classes:

```text
artifact:<artifact_id>              stable managed artifact identity
anchor:<artifact_id>/<anchor_id>   stable material sub-artifact anchor
decision:<D-id>                    accepted DECISIONS.md decision
adr:<adr-id>                       architecture-decision record identity
change:<change-id>                 bounded engineering change
requirement:<requirement-id>       canonical Requirement identity
git:<commit-sha>                   exact repository snapshot/provenance
github-issue:<owner/repo>#<n>      work/evidence locator
github-pr:<owner/repo>#<n>         review/change evidence locator
path:<repo-relative-path>          physical locator only, never stable identity
```

A path may be stored as the current locator of an artifact, but consumers must not treat path equality as semantic identity.

### 3.3 Stable material anchors

Markdown heading text is useful navigation but not sufficiently stable for material trace across edits/moves. Only places that actually need durable sub-document trace require an explicit `anchor_id`.

Candidate lightweight form is an unobtrusive stable marker adjacent to the material section, for example:

```text
<!-- anchor: finding-F29 -->
```

or equivalent metadata supported by the final representation.

Do **not** add anchor IDs to every paragraph. Stable anchors are required only for material evidence/decision/finding trace that must survive heading/path changes.

### 3.4 Legacy path continuity

Physical migration must preserve an explicit old-path → stable-artifact/current-path mapping for moved managed artifacts. Git history remains provenance but is not the only lookup mechanism for a current consumer.

The mapping is transitional compatibility data, not a permanent second catalog of semantics.

## 4. Currentness and supersession rules

Currentness is explicit and authority-derived.

Rules:

1. `created_at`, filename date, Git timestamp, Issue number and merge order do not establish semantic currentness.
2. A proposed artifact remains proposed until an applicable accepted decision/admission/result changes its status.
3. Supersession must name the superseded artifact/decision and the authority/evidence for supersession.
4. Multiple current artifacts are allowed when they own different scopes; conflict is an error only when the same canonical responsibility/scope has incompatible current owners.
5. Zero active engineering changes is valid state.
6. Multiple active investigations are valid; recency must not choose `current_focus`.
7. `current_focus` is optional and, when present, must have an explicit owner/authority basis rather than being inferred from activity.
8. Historical/superseded artifacts remain retrievable but are excluded from default current context unless directly relevant provenance is requested.

## 5. Configuration-transition contract

The implementation must support the following semantic transitions. The exact field names are not fixed here.

| From | Event / evidence | Authority | To | What does **not** follow automatically |
|---|---|---|---|---|
| none | bounded analysis/design starts | existing work authority | proposed change/design | no implementation admission |
| proposed | explicit D-016 Human admission for material change | Human Owner | admitted change | not implemented, verified or current baseline |
| admitted | repository implementation mutation | implementation agent within admitted scope | implemented candidate / actual tree changed | no verification or acceptance |
| implemented | deterministic checks / required reviews pass | corresponding assurance mechanism | verified candidate | no scholarly/Human acceptance beyond checked properties |
| verified | Result Review reconciles actual result with admitted scope and requirements | result-review owner; Human only when reserved consequence requires it | accepted result **or** needs-decision / partial / rejected / no-change | no current-baseline update until accepted consequence is explicit |
| accepted result | explicit accepted consequence says baseline changes | applicable accepted decision/result authority | accepted/current baseline reference updated | does not rewrite historical proposal/evidence |
| any material stage | evidence invalidates premise/requirement/design | applicable owner | re-entered / revoked / superseded / rejected | latest replacement is not automatically accepted |

### 5.1 No-change result

A successful bounded change may legitimately conclude that no accepted engineering baseline changes. The Result record must be able to state `no baseline change` explicitly rather than forcing a synthetic configuration mutation.

### 5.2 Revocation

An admitted but not yet completed material change may be revoked only by the authority capable of changing that admission or by an already-defined invalidation rule. A branch deletion or closed Issue is not revocation by itself.

## 6. Relation to Git and exact-head assurance

Git remains the authoritative byte/provenance history.

The future configuration owner may record the commit SHA at which an accepted semantic baseline was established for reproducibility. That SHA is provenance for the transition, not the definition of what is current forever.

At runtime/current checkout:

```text
actual repository head = derived observation from Git
accepted semantic baseline = configuration owner
transition provenance = accepted decision/result + Git evidence
```

Generated views may report all three and flag inconsistency. They must never silently resolve a mismatch by choosing the newest one.

## 7. Minimal future configuration responsibility

The prior illustrative `engineering/configuration.json` remains a viable representation, but its logical responsibility is now fixed independently of JSON.

It must be able to identify at least:

- schema/version of the configuration contract;
- accepted architecture baseline(s);
- accepted Requirements baseline(s) applicable to engineering-system work;
- admitted/active changes, if any;
- optional explicitly authorized current focus;
- accepted decision owner reference;
- configuration-transition provenance;
- explicit absence where no active change/focus exists.

It must **not**:

- duplicate every artifact lifecycle row;
- mirror all open Issues;
- copy Git history;
- manufacture priority;
- own Project scholarly state;
- decide unresolved conflicts by recency.

## 8. Brownfield scenarios

### Scenario A — superseded design remains in `requirements/`

The old design receives a stable artifact ID during migration. It is marked superseded by a later design/decision relation. Its path can remain retrievable. A current query excludes it unless provenance/history is requested.

### Scenario B — material design merged but not admitted

Git contains the proposal; its artifact lifecycle is `proposed/non-normative`. Configuration baseline does not change. A generated current view may show it under `proposed changes`, never under `current architecture`.

### Scenario C — admitted implementation passes CI

Actual Git tree changes and deterministic verification passes. The result remains `verified candidate` until the admitted Result Review establishes the actual consequence. CI cannot move accepted architecture by itself.

### Scenario D — Human rejects proposed architecture

The proposal/ADR remains permanent decision evidence with `rejected` disposition. Current baseline is unchanged. History is not rewritten/deleted.

### Scenario E — file moves during IA migration

`artifact_id` remains constant, `path` changes, legacy-path mapping preserves navigation, and material stable anchors remain resolvable. Git supplies exact historical byte provenance.

## 9. Failure handling / fitness requirements

Future validation must reject or surface at least:

- two incompatible canonical-current artifacts for the same owned scope;
- current references to missing artifact IDs;
- superseded artifact referenced as current without an explicit valid exception;
- transition with missing authority/evidence reference;
- currentness derived only from date/order;
- path used where stable identity is required;
- derived Current State stale against its canonical inputs;
- configuration file attempting to own Project scholarly priority/state.

## 10. Representation intentionally left to #251

This design fixes semantics, not storage layout. Central TSV, local typed metadata and hybrid representations remain comparable implementation options.

The representation must preserve these semantics without requiring duplicate manually synchronized truth.

## 11. Readiness disposition

**#246 design is complete enough for downstream #247/#250/#251/#249 design.**

The implementation of configuration/artifact/reference schemas remains D-016-gated. An implementer should no longer need to invent the material meaning of currentness, stable reference, supersession or configuration transitions.