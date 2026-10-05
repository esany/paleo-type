# Source / Project owner decision and bounded implementation admission — 2026-09-02

Status: **human-owner decision and bounded implementation admission**. This record closes the A2 semantic review for Draft PR #88 and authorizes the implementation scope below. It does not itself choose a manuscript NEXT ACTION or certify historical D-017 authority retroactively.

## Plain-language owner decision

The Human Owner accepts the following in ordinary research-facing language:

- **Projects exist because there is a concrete scholarly investigation/research purpose.** A Source, File, upload, archival structure, `part_of` relation, place focus, evidence bundle or AI working bundle does not automatically create a Project.
- **Reg. Ii 3, Reg. Ii 4 Bd. II and Reg. Ii 5 are the current Projects for this corpus.** The Reg. Ii 5 Project retains the legacy directory/id `ega-reg-ii-5-knau` for path continuity; that name does not make Knau the current research priority.
- **Earlier Knau work remains valid research/work history but does not automatically define the current priority or NEXT ACTION.**
- **File/Source intake may validly end without a Project.** `CORPUS_ONLY / NO_PROJECT_YET` is a legitimate outcome.
- **The completed loss-checked Reg. Ii 5 migration is accepted.** Historical Project→Source functions are carried by `source-uses.tsv`; concrete historical use→File bindings are carried by `research/use-evidence.tsv`. Removed legacy `sources/sources.tsv` / `principal_source_id` compatibility owners must not be recreated merely because they existed historically.

Internal labels such as D-018 are references to the decision history; they are not a substitute for this plain-language meaning.

## 1. Accepted generic semantics

1. **Project purpose** — A Project is a durable scholarly investigation/work container established because there is a research purpose. Source, File, archival structure, `part_of`, upload order, evidence availability, an AI-created working bundle or an inherited research-function label does not by itself create a Project.
2. **Documentary anchor** — `project_source_id` is the stable canonical Source anchor used for deterministic structural resolution after Project selection. It does not create Project existence, define research purpose, choose the current scholarly priority or choose the current scholarly NEXT ACTION.
3. **Corpus-only intake** — File/Source intake may be completed validly without a Project. `CORPUS_ONLY / NO_PROJECT_YET` is a legitimate routing outcome; Project creation is not an intake invariant.
4. **Current visitation organization** — Reg. Ii 3, Reg. Ii 4 Bd. II and Reg. Ii 5 continue as the current Projects as the present application of the accepted generic semantics. This current owner decision must not be rewritten as proof that the full historical D-017 wording was already explicitly authorized on 2026-08-31.

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

The owner explicitly authorizes implementation of the following scope under the canonical material-change admission rule:

- converge canonical normative text/decisions on the accepted Project semantics;
- treat `project_source_id` only as a post-selection documentary anchor;
- preserve and regression-test Corpus-only / no-Project intake;
- align existing contract/resolver/template/CI behavior with stable deterministic rules without creating a second semantic owner;
- add regression fixtures for authority drift, migration loss and restartability where the failure class is deterministic;
- reconcile current Li 3 / Li 4 / Li 5 state losslessly using the recovery matrix;
- retain/remap legacy project-relative information until a loss-checked mapping proves what can be moved/removed;
- preserve historical work-state and authority audit pointers during cleanup;
- repair stale binding/orientation surfaces exposed by the result audit;
- distinguish exact File identity/byte availability/reproducibility from target-context staging/inspectability;
- add generated/rebuildable context views only where they reduce restart risk without becoming parallel truth;
- apply a lean Generic-Fit/systemic-integration check before pilot findings are promoted into generic METHOD/contract/regression semantics.

Not authorized by this admission:

- new manuscript readings or historical interpretations;
- automatic Project creation from Source/File structure;
- invention of current scholarly priorities from structural or legacy metadata;
- a workflow engine, universal lifecycle or new role/gate bureaucracy;
- broad schema redesign unrelated to demonstrated invariants;
- automatic merge/release merely because deterministic tests pass;
- treating local/retrievable bytes as proof that a target work context has staged or can visually inspect the evidence.

## 5. Implementation strategy

Use the smallest existing owner/core first:

```text
canonical scholarly semantics
→ deterministic Source/Project contract
→ read-only derivations/adapters
→ rebuildable context/orientation views
→ proportionate assurance
```

New material aspects are integrated against the existing objective, state, requirements and decisions rather than appended blindly. Useful review dispositions are `fuse | refine | reframe | supersede | conflict | reject | defer`; these are review vocabulary, not a new schema/state machine.

A Project/pilot finding remains Project-specific unless a Generic-Fit check justifies a genuinely reusable safeguard. A single case may falsify a bad generic assumption without itself defining the complete replacement generic model.

## 6. Assurance boundary

Keep these claims separate:

- deterministic/formal checks PASS;
- canonical consistency/restartability PASS;
- target-context evidence staging/vision-inspectability PASS;
- scholarly/domain/specialist validation PASS;
- Human Owner result/merge/release acceptance PASS.

One does not imply another. In particular, successful CI is not manuscript evidence, specialist validation, target-context staging or merge authorization.
