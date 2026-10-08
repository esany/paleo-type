# Source-entry transition + granular coverage — Option C currentness-corrected concept

**Date:** 2026-10-08  
**Status:** Human-admitted bounded implementation; reconstructed against shared `main@c64ac5c9a36c723275cc54e18c3f232da791174e`  
**Engineering artifact:** `artifact:ENG-A-0119`  
**Natural work owners:** #309 (transition/materialization completeness), #267 (granular inspection coverage/restartability), #272 (whole-system reconciliation)  
**Admission:** `artifact:ENG-A-0120`

## Recovery provenance and claim ceiling

This record reconstructs the admitted Option C scope from the externally preserved
`OPTION-C-RECOVERY-SNAPSHOT.md` and then reconciles it against the current shared repository
and the latest owner state. It does **not** claim byte-identical recovery of the historical local
`requirements/source-entry-transition-coverage-concept-2026-10-08.md` file or of local commit
`e26a470`.

The recovered local implementation/tests are evidence and design input, not current repository
authority. Shared GitHub `main`, current canonical method/owner files and the current #309/#267/#272
owner surfaces control currentness.

## Currentness corrections

1. **Repository information architecture.** The old local concept lived in `requirements/`.
   Current shared architecture narrows `requirements/` to the accepted reusable Requirement
   baseline. This concept therefore lives as managed engineering research evidence under
   `engineering/evidence/research/`; the D-016 owner decision lives under
   `engineering/evidence/decisions/`.
2. **Nr. 632 Project authority.** Nr. 632 is no longer a legitimate positive
   `CORPUS_ONLY / NO_PROJECT_YET` fixture. Current #270 + #293 + #309/#272 reconciliation
   establishes Human-grounded Project existence/boundary, with canonical materialization still
   missing.
3. **Rights/use currentness.** `rights_status: unknown` is not by itself a blocker to truthful
   canonical File/provenance materialization. Controlled local research use is Human-authorized;
   provenance must remain explicit; no open/public-redistribution licence is inferred.
4. **Generic #267 acceptance.** A genuinely legitimate real `CORPUS_ONLY / NO_PROJECT_YET`
   case is still required before full route-spanning Generic-Fit acceptance may be claimed.
5. **Local PASS ceiling.** The recovered 66-test local PASS is historical recovery evidence only.
   Current implementation must be checked through the shared GitHub/CI route.

## Demonstrated problem

### #309 — omitted required transition/materialization state can still PASS

The demonstrated failure is not “a Project row is missing”. It is:

```text
authorized sustained source-entry work
→ work metadata / dependent state advances
→ required canonical Source/File/routing ownership can be omitted
→ present-state consistency validation still PASSes
→ chat/Issue/local worktree becomes the practical state carrier
```

The safeguard must fail closed when durable source-entry coverage is recorded without an explicit
resolved route basis, while preserving `CORPUS_ONLY / NO_PROJECT_YET` as a valid route and never
auto-creating a Project.

### #267 — granular restartable inspection coverage must survive Project routing

The source-entry layer must preserve, at source/locus appropriate granularity:

- exact Source and optional File evidence identity;
- inspection domain and exact locator domain/locus;
- purpose and depth;
- inspected / not-inspected / partial / unreadable / unavailable / missing state;
- candidate relevance / exclusion / unresolved relevance;
- evidence status and claim/derivation layer as separate axes;
- exclusions, unresolved/partial state, continuation boundary and claim ceiling;
- provenance/responsibility needed to restart consequential source-entry work.

This is **not** active scholarly scope, a gate, G2 completeness, a page-progress counter or
`NEXT ACTION`.

## Admitted bounded target

Option C creates one dedicated repository owner at `source-entry/` for:

1. append-only Source routing history; and
2. append-only source-entry inspection/coverage records.

The owner may reference canonical Source/File identity and an optional Project binding. It does
not own or redefine Source/File identity, Project purpose/boundary/active scope, Project gate state,
Project `NEXT ACTION`, or Project-specific mature reading/interpretation truth.

The existing `tools/source_contract.py validate` entrypoint validates this owner alongside the
existing Source/File/Project-use contract. No workflow engine, database, event-sourcing platform,
universal page tracker or automatic Project creation is introduced.

## Physical concept

### Route history

`source-entry/routes.tsv` is append-only. Each Source has monotonically increasing
`transition_sequence` rows.

The current route is **derived** as the row with the greatest valid transition sequence. No mutable
`current=yes/no` flag is stored; the recovered prototype's flag was rejected because changing an
older row from current to historical would contradict append-only history.

Allowed route states remain:

- `UNRESOLVED`
- `CANDIDATE_NEW_PROJECT`
- `CORPUS_ONLY / NO_PROJECT_YET`
- `EXISTING_PROJECT`

A resolved route sufficient for durable coverage is either:

- Human-confirmed `CORPUS_ONLY / NO_PROJECT_YET` with no Project ID; or
- Human-confirmed `EXISTING_PROJECT` with an existing canonical Project ID.

`UNRESOLVED` and `CANDIDATE_NEW_PROJECT` are preservable routing states, but they do not authorize
new durable inspection/coverage records.

### Coverage

Each `inspection-coverage.tsv` row references the exact `route_id` under which that source-entry
record was created. This makes pre-Project coverage reconstructable after a later transition to an
existing Project without mutating the earlier row.

A durable coverage row therefore fails validation when:

- its Source is missing;
- its route is missing or belongs to another Source;
- the referenced route is `UNRESOLVED` or `CANDIDATE_NEW_PROJECT`;
- its File reference is absent/mismatched;
- an explicit Project binding does not match an `EXISTING_PROJECT` route;
- evidence/claim axes collapse (`H + OBSERVATION`, `NOT_INSPECTED + P`);
- Project/scholarly-state columns such as `active_scope`, `gate` or `next_action` are introduced.

Empty owner tables are valid. They mean no source-entry route/coverage has yet been persisted.

### Truth-store boundary

`result` is limited to the source-entry/reconnaissance result needed to understand the inspection
record and its claim ceiling. It must not become a duplicate canonical store for Project-specific
mature readings, Project decisions, Project scope or historical interpretation. Where later Project
research owns such truth, the source-entry record retains coverage/provenance and points through its
evidence/notes to the natural owner rather than copying that truth.

## Migration disposition

No Reg. Ii inspection-log rows are migrated. The existing
`projects/ega-reg-ii-5-knau/sources/inspection-log.tsv` is a semantic loss-check precedent only.
A future migration remains a separate decision if real use demonstrates that it is warranted.

No Nr. 632 route or positive manuscript coverage is fabricated by this implementation.

## Explicit non-goals

This admission does not authorize:

- a #265 active-scope representation;
- a Project type or automatic Project creation;
- File/package/rights schema expansion;
- a new canonical Source/File identity model;
- migration of existing Project-local research logs;
- a workflow engine, global planner, event store or database;
- activation of #266, #268 or #269 without their real evidence triggers;
- claiming that synthetic fixtures establish scholarly/domain acceptance;
- treating Nr. 632 as a real Corpus-only fixture.

## Deterministic acceptance

Shared CI must demonstrate at least:

1. empty owner state validates;
2. coverage without a route fails;
3. coverage referencing unresolved/candidate routing fails;
4. Human-confirmed Corpus-only routing accepts pre-Project coverage without creating a Project;
5. append-only `CORPUS_ONLY → EXISTING_PROJECT` history preserves earlier coverage and accepts later
   Project-bound coverage;
6. Project-bound coverage requires the matching existing Project route;
7. provider-image/PDF/archival locator meanings are not conflated by the owner;
8. `H + OBSERVATION` and `NOT_INSPECTED + P` fail;
9. scope/gate/`NEXT ACTION` columns fail;
10. Reg. Ii meanings used for the loss check remain representable without migration;
11. a simple/short source does not acquire Nr.-632-specific bureaucracy;
12. the repository's shared deterministic full check passes at the exact PR head.

## Acceptance ceiling / remaining real-use work

A deterministic PASS establishes only the implemented contract at the checked Git head.

Still open after technical PASS:

- genuine real `CORPUS_ONLY / NO_PROJECT_YET` Generic-Fit evidence for #267;
- real Nr. 632 coverage on the **established-Project / large-composite** side after concrete canonical
  materialization and actual target-context image inspection;
- scholarly/domain review of the resulting source-entry practice;
- any new semantic requirement discovered by real use, which must return to D-016 if outside this
  admitted scope.

## Return condition

Return to #309, #267 and #272 with:

- exact shared branch/commit/PR;
- exact shared CI result and claim ceiling;
- deliberate non-changes;
- remaining real-use acceptance gaps;
- no claim that technical validation closes the Issues or creates scholarly truth.
