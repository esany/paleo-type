# Source / Project owner decision and bounded implementation admission — 2026-09-02

Status: **human-owner decision and bounded implementation admission**. This record closes the A2 semantic review for Draft PR #88 and authorizes the implementation scope below. It does not itself migrate Project/Corpus data, choose a manuscript NEXT ACTION, or certify historical D-017 authority retroactively.

## 1. Accepted generic semantics

The human owner accepts the following generic semantics:

1. **Project purpose** — A Project is a durable scholarly investigation/work container established because there is a research purpose. Source, File, archival structure, `part_of`, upload order, evidence availability, an AI-created working bundle or an inherited research-function label does not by itself create a Project.
2. **Documentary anchor** — `project_source_id` is the stable canonical Source anchor used for deterministic structural resolution after Project selection. It does not create Project existence, define research purpose, or choose the current scholarly NEXT ACTION.
3. **Corpus-only intake** — File/Source intake may be completed validly without a Project. `CORPUS_ONLY / NO_PROJECT_YET` is a legitimate routing outcome; Project creation is not an intake invariant.
4. **Current visitation organization** — Reg. Ii 3, Reg. Ii 4 Bd. II and Reg. Ii 5 should currently continue as act-oriented Projects as the present application of the accepted generic semantics. This current owner decision must not be rewritten as proof that the full historical D-017 wording was already explicitly authorized on 2026-08-31.

## 2. Authority distinction

Keep two questions separate:

```text
RETROSPECTIVE AUTHORITY
Was the complete D-017 specification of 2026-08-31 explicitly human-authorized in exactly that form?
→ not independently established by Git; historical authority claim remains audit evidence.

CURRENT OWNER INTENT / AUTHORITY
Does the owner currently accept the generic semantics above and the current Li 3 / Li 4 / Li 5 organization as their present application?
→ yes, explicitly accepted on 2026-09-02.
```

Repository authorship, connector writes, `owner_confirmed` metadata or internal consistency are not substitutes for semantic admission.

## 3. Recovery constraints carried into implementation

Historical recovery remains descriptive evidence and is not reclassified by the new model. For every migration/reconciliation distinguish at least:

- **information survival** — preserved / transformed / missing / ambiguous;
- **work-state survival** — current / historical-only / lost-from-normal-view / partially recovered / superseded / ambiguous;
- **authority survival** — owner-grounded / AI-derived / repository-claimed-owner-authority / historical assumption / unknown / not applicable.

The source-unit wrappers are not to be restored merely because they existed. Their consequential activation/dormancy/evidence-limit/NEXT-ACTION state must remain recoverable without reviving source-as-project semantics.

`e8a7235bff875bf2c191c96c41638c4095f7ec76` is only the last cleanly identified scholarly checkpoint before the investigated interpretation/authority series. It is not a baseline-truth or rollback anchor.

For Reg. Ii 5 distinguish exact File coverage from Source crosswalk coverage: the inspected File covers export images 120–143; the canonical Source crosswalk maps 120–142 because image 143 / fol. 67r is adjacent File context outside the Source boundary.

## 4. Bounded implementation admission

The owner explicitly authorizes implementation of the following scope under D-016:

- converge canonical normative text/decisions on the accepted Project semantics;
- treat `project_source_id` only as a post-selection documentary anchor;
- preserve and regression-test Corpus-only / no-Project intake;
- align existing contract/resolver/template/CI behavior with stable deterministic rules without creating a second semantic owner;
- add regression fixtures for authority drift, migration loss and restartability where the failure class is deterministic;
- reconcile current Li 3 / Li 4 / Li 5 state losslessly using the recovery matrix;
- retain `relevance` and legacy `principal/comparison/control/context` information until a loss-checked mapping proves what can be moved/removed;
- preserve historical work-state and authority audit pointers during cleanup.

Not authorized by this admission:

- new manuscript readings or historical interpretations;
- automatic Project creation from Source/File structure;
- invention of current scholarly priorities from structural or legacy metadata;
- a workflow engine or new role/gate bureaucracy;
- broad schema redesign unrelated to demonstrated invariants;
- automatic merge/release merely because deterministic tests pass.

## 5. Implementation order

```text
1. normative/decision convergence
2. deterministic contract + regression protection
3. #69 intake/routing behavior, reusing the existing core
4. restartability / evidence-readiness protection
5. migration/restructuring guard
6. generated context/handoff adapters where justified
7. loss-checked Li 3 / Li 4 / Li 5 reconciliation and legacy cleanup
8. bounded G2 operational support only where independently required
9. heterogeneous-model + technical/scholarly/reproducibility/human acceptance
```

Historical recovery remains admissible evidence throughout and does not wait on implementation stages.
