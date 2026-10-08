# Source-entry route and inspection-coverage owner

This directory is the admitted Option C owner for consequential **source-entry routing history** and
**granular inspection/coverage state**. It is deliberately separate from canonical Corpus
Source/File identity and from Project purpose/scope/state.

The admission and currentness-corrected concept are:

- `artifact:ENG-A-0120` — Human D-016 admission;
- `artifact:ENG-A-0119` — admitted scope/current concept.

## Routing

`routes.tsv` is append-only route history. **Append-only is a canonical write discipline, not a claim that a single-snapshot validator can prove Git-history immutability.** The validator checks route identity, Source references, allowed states, Human authority where required, and contiguous transition sequences; repository history/review remains the evidence that an older valid row was not silently rewritten.

For each Source, `transition_sequence` starts at 1 and remains contiguous. The current route is
derived as the row with the greatest sequence; there is no mutable current flag.

Allowed route states:

- `UNRESOLVED`
- `CANDIDATE_NEW_PROJECT`
- `CORPUS_ONLY / NO_PROJECT_YET`
- `EXISTING_PROJECT`

`CORPUS_ONLY / NO_PROJECT_YET` is a valid completed route only with explicit Human-Owner
confirmation and no Project ID. `EXISTING_PROJECT` likewise requires explicit Human-Owner
confirmation and an existing canonical Project.

A Source, File, Issue, directory name, inspection need or technical readiness never creates a
Project.

## Inspection / coverage

`inspection-coverage.tsv` is append-only source-entry activity/checkpoint state, **not a page
counter**.

Every durable coverage row references the exact `route_id` that authorized that record. A
coverage row is invalid when that route is absent, belongs to another Source, or is
`UNRESOLVED`/`CANDIDATE_NEW_PROJECT`.

A coverage row may carry an optional Project binding. If it does, the referenced route must be
`EXISTING_PROJECT` for exactly that Project. Earlier pre-Project rows remain valid after a later
Project transition because their original route reference remains immutable.

The owner keeps these axes separate:

```text
inspection_domain ≠ coverage_locus ≠ locator_domain ≠ scholarly_scope
coverage_status   ≠ active_scope ≠ gate ≠ NEXT ACTION
evidence_status   ≠ claim_layer
Source/File identity ≠ Project binding ≠ inspection state
```

Provider image IDs, PDF pages and archival folios remain distinct locator meanings until evidenced
crosswalks establish a mapping. The owner preserves the distinction structurally through `locator_domain` + `coverage_locus`; it does not itself prove that a researcher selected the correct locator domain or establish a crosswalk.

## Truth-store boundary

This owner records only source-entry/reconnaissance state needed to reconstruct the inspection
activity, evidence basis, uncertainty and claim ceiling. It does **not** own:

- Source/File identity or rights/provenance truth;
- Project purpose, boundary, active scholarly scope, gates or `NEXT ACTION`;
- a Project-specific mature diplomatic reading, historical interpretation or Project decision when
  that truth belongs in the Project.

`result` must therefore stay within the source-entry record's activity/claim ceiling. Do not copy
later Project research truth here merely for convenience.

## Validation and empty state

`contract.json` is the machine contract. The existing
`python tools/source_contract.py validate` entrypoint validates this owner.

Empty `routes.tsv` and `inspection-coverage.tsv` tables are valid and mean exactly that no
source-entry route/coverage has yet been persisted. This implementation does not fabricate a Nr. 632
route or manuscript inspection.

No Reg. Ii inspection-log rows are migrated. The existing Reg. Ii log is used only as a semantic
loss-check precedent in tests.
