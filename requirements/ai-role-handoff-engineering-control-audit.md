# AI role / handoff engineering — Phase A control audit

Status: **analytical / assurance evidence for #79; not normative METHOD, not a new requirement owner, and not implementation authority for #64/#77-dependent work**.

Primary owner: #79. Related owners: #71, #74, #77, #78, #66. Canonical authority remains `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, `requirements/domain-requirements.tsv`, authoritative methodology and canonical corpus/project state.

This audit records work that can be completed independently of the live #64 Source Research → Domain Review → Dev cycle. It operationalizes the broader analysis in `requirements/ai-role-handoff-engineering-analysis.md` without promoting its conclusions to normative rules.

## 1. Scope and stop boundary

Included now:

- map the #79 competency profile to existing requirements and owners;
- inventory current executable controls and current regression coverage;
- add regression fixtures only for already-settled validator semantics;
- test whether a historical material Dev case is reconstructable without its originating chat;
- distinguish handoff information that must be supplied from information that should be derived from canonical state;
- map risks to current controls and remaining evidence/trigger gaps.

Excluded until real fixtures justify them:

- no G2 Line/Span/Phenomenon control;
- no handoff template files;
- no handoff validator;
- no context-composer/runtime;
- no evidence-storage platform;
- no Technical Assurance role;
- no new Requirement family;
- no new canonical-state transition schema;
- no rewrite of #71–#79 into METHOD before falsification.

## 2. Competency → requirement → owner → current control

| #79 competency | Primary existing requirements | Current canonical/operational owners | Current control / evidence | Current gap or trigger |
|---|---|---|---|---|
| Research Software Engineering | REQ-RSE-001/002/003/005/009; REQ-GWP-001 | Requirements; `AGENTS.md`; `methodology/maintenance.md`; #36/#66 | requirement-first derivation, one-owner rule, anti-bloat/technical-subsidiarity rules, Git scope/review | engineering judgement remains non-deterministic; no further executable control justified merely for style/architecture preference |
| Requirements Engineering | REQ-RSE-001/005; REQ-AI-001/007; REQ-UX-012 | Requirements; #73 Domain Review; #74 Dev | #73 requires evidence→requirement derivation; #74 requires bounded/admitted handoff and returns semantic ambiguity | first real #73→#74 handoff still pending; do not create ticket/schema automation beforehand |
| Information/Data Modelling / canonical ownership | REQ-GWP-001/002; REQ-RSE-003/004/005; REQ-ARCH-001/003/006/007 | CORPUS/PROJECT owners; `source-contract.json`; `source_contract.py` | stable IDs, references, `part_of`, Project root, derived structural status, Project→Source use, Use→File evidence and owner separation are executable | G2 locus/unit addressing remains explicitly dependent on #64 |
| Provenance / Research Data Stewardship | REQ-GWP-002/004/006/008/009/010; REQ-ARCH-003/004; REQ-RSE-008 | `corpus/files.tsv`; crosswalks; project decisions/research state; source/provenance method | SHA format, File→Source, storage status, repo-preserved byte/path verification, crosswalk ownership/locator rules, migration fixtures | research-ready availability is not implied by identity/provenance; #78 owns that distinction |
| Verification / Validation / semantic-loss engineering | REQ-RSE-004/006/007/008; REQ-AI-008; REQ-GWP-004/010 | validator/tests/CI; #66; future #73 scholarly return | Source Contract CI, synthetic negative fixtures, current migration/loss regression fixtures, governance ownership regression | G2 deterministic witness/loss checks wait for #64; technical pass remains distinct from scholarly acceptance |
| AI Context / Tool Engineering | REQ-AI-001/002/004/008/009; REQ-UX-011 | `AGENTS.md`; AI governance; #71/#77 | mandatory applicable-context rule, role/task routing principles, deterministic tool preference, stage-specific contamination rules | no context composer justified yet; real handoff/task-resume omissions must first be observed |
| Human-in-the-loop / authority engineering | REQ-AI-007/010; REQ-RSE-010; REQ-UX-011/012; REQ-GWP-005 | `AGENTS.md`; `maintenance.md` D-016; #75; #76 | owner-reserved decision boundary, material-change admission, no owner fallback for technical/specialist ambiguity, independent-review distinction | no workflow/approval engine; challengeability tested through traceability/review rather than mandatory confirmation |
| Human auditability / information architecture | REQ-UX-001/005/007/008/009/010/012; REQ-GWP-004/005/008 | project `STATUS.md`; derived review surfaces when triggered; Git/decisions | restart surface, evidence/decision drill-down requirements, explanation chain, derived-vs-canonical rule | final G2 human witness/review surface remains #64-dependent |
| Reproducibility / preservation-aware engineering | REQ-ARCH-003/004; REQ-GWP-002/006/008/009/010; REQ-PAL-008 | File/crosswalk/provenance owners; #68/#78 where applicable | exact File IDs/SHA, crosswalk separation, storage/right state, repo-preserved byte checks, documented derivative provenance | #78 shows `identifiable` and `reproducible` are insufficient if evidence is not accessible to a fresh authorized context |
| Rights/Security-aware engineering | REQ-GWP-006; REQ-AI-006; AGENTS hard stops | `corpus/files.tsv`; source/provenance method; Human Owner for unresolved authority facts | controlled storage status; explicit rights state; byte/path checks for repo-preserved; prohibition on convenience upload of restricted material | legal/institutional authority remains judgement/fact input where not verifiable; do not automate it into truth |
| Scholarly-interface literacy | REQ-GWP-003/004/005; REQ-AI-003/005/010; relevant domain REQ-* | #72/#73/#76; domain methodology | evidence/inference/review separation, unresolved/alternatives retention, specialist-review boundary | Dev must detect and return scholarly-semantic ambiguity; it does not acquire specialist adjudication authority |

### Result

The current competency expansion is **covered by existing Requirement families**. No new Requirement row/family is justified by this Phase-A audit.

The current gap is primarily **operational assurance and real handoff falsification**, not missing mission semantics.

## 3. Current executable-control coverage

### 3.1 Source / relationship structure

Implemented in `tools/source_contract.py`:

- required Source fields;
- unique Source IDs;
- paired date fields and serial-date/calendar consistency;
- relationship IDs and required evidence/status fields;
- Source existence for structural/locus relationships;
- `part_of` self-link rejection;
- duplicate `part_of` rejection;
- `part_of` cycle rejection;
- deterministic `is_within()` ancestry;
- resolver-derived `project_root | internal | external` status.

Relevant requirements include REQ-ARCH-001/006/007, REQ-GWP-001/002 and REQ-RSE-004/005.

### 3.2 Exact File / preservation structure

Implemented:

- File ID uniqueness;
- File→Source referential integrity;
- lowercase 64-character SHA-256 format;
- controlled `storage_status`;
- `repo-preserved` requires `repository_path`;
- repository-preserved path must actually exist;
- repository-preserved bytes must match the recorded SHA-256.

This is a particularly important anti-false-preservation control: a metadata row cannot make absent or different bytes `repo-preserved`.

Relevant requirements include REQ-ARCH-003, REQ-GWP-002/006/008 and AGENTS' explicit hard stop against false repository-preservation claims.

### 3.3 Project root and Project→Source use

Implemented:

- required Project keys;
- project `id` must match directory;
- duplicate Project IDs rejected;
- `project_source_id` must resolve to a canonical Source;
- legacy project Source rows remain readable during compatibility phase;
- target `use_id` uniqueness;
- target use `source_id` resolution;
- `research_function` remains open vocabulary with syntax-only lowercase-kebab control;
- same Source may have multiple research functions;
- structural membership remains derived, not stored as Project-use truth.

Relevant requirements include REQ-ARCH-007, REQ-RSE-004/005 and D-014/D-015.

### 3.4 Use→File evidence

Implemented:

- unique evidence IDs;
- no redundant `source_id` column in use-evidence;
- `use_id` must exist;
- evidence may not bind to a Use owned by another Project;
- `file_id` must exist;
- File's canonical Source must equal the Use's canonical Source;
- one Use may have multiple evidence records;
- the same File may support multiple Uses of its Source.

This protects canonical ownership and prevents a technically convenient File from silently becoming evidence for the wrong Project use.

### 3.5 Source crosswalk

Implemented:

- source-data directory must resolve to a Source;
- each row's `source_id` must match its source-data directory owner;
- archival folio is required and unique within the source-wide crosswalk;
- mapping status is controlled;
- at least one digital locator (`export_image`, `pdf_page`, `stable_image_urn`) is required;
- a stable image URN, when present, must be syntactically a URN.

This is structural provenance enforcement only. It does not establish that an institutional image is currently accessible or that a mapping is palaeographically correct.

## 4. Regression coverage added in Phase A

No validator semantics were changed. Only synthetic regression fixtures for already-existing behavior were added.

### Commit `474ec7ecf29d4a87a732d59d6b4ed05682ec996e`

Added `tests/test_source_contract_assurance.py` with explicit failure fixtures for:

1. `part_of` cycles;
2. Use-Evidence referencing a Use owned by another Project;
3. `repo-preserved` when expected bytes are absent;
4. `repo-preserved` when present bytes do not match SHA-256;
5. open-vocabulary `research_function` accepted when lowercase-kebab;
6. invalid research-function syntax rejected without closing the vocabulary.

GitHub Actions `source-contract` run **#41** completed successfully.

### Commit `404f6f7e3ac991ec4edfea5ea893aa0629560e48`

Added explicit crosswalk failure fixtures for:

1. crosswalk row `source_id` not matching the `source-data/<source_id>/` owner;
2. crosswalk row with no digital locator.

GitHub Actions `source-contract` run **#42** completed successfully.

### Why these tests are in scope

They convert existing settled validator behavior into regression evidence. They do **not**:

- add a new controlled vocabulary;
- change Source/Project semantics;
- infer research function;
- define G2 loci;
- decide rights authority;
- create storage infrastructure;
- add a new workflow layer.

## 5. Existing control areas deliberately not extended now

The audit found further validator branches that could receive more unit tests (for example project-ID/directory mismatch, unknown `project_source_id`, several additional crosswalk and legacy-compatibility error branches).

They are not all converted into fixtures merely to maximize line/branch coverage. The current additions prioritize controls directly tied to the #79 risks of ownership drift, provenance/preservation misstatement and cross-context evidence routing.

Further regression fixtures should be added when:

- a real failure occurs;
- a migration makes the invariant consequential;
- a branch changes materially;
- or the audit shows the missing fixture is the only protection against a high-consequence regression.

Coverage percentage is not a project objective.

## 6. Historical #74 restartability fixture — PR #67

The completed Phase-1 Project/Source safeguard work provides a real historical Dev fixture independent of #64.

### Reconstruction inputs available without old chat

From repository/GitHub state alone a fresh Dev context can recover:

- **problem/admission semantics:** #58 defines the consequence-based material-change admission workflow;
- **target Project/Source semantics:** #59 defines `project_source_id`, multiple Project-relative research functions and separate Use-Evidence;
- **implementation/admitted scope:** PR #67 explicitly lists the bounded Phase-1 implementation and its non-goals;
- **canonical owners:** `maintenance.md` for D-016; CORPUS owners for File/Source; Project uses/evidence for Project-relative use;
- **deterministic/epistemic boundary:** PR #67 states what the resolver/validator derives and what it explicitly does not infer;
- **migration/loss obligations:** PR #67 and the project migration fixture enumerate legacy preservation requirements;
- **tests:** PR #67 records validator, unit and resolver regression coverage;
- **closure/result:** #58's post-merge comment identifies the merge SHA and states what the completed admitted scope did and did not authorize.

### Restartability result

**PASS for bounded implementation reconstruction.** A capable Dev does not need the originating chat to determine the Phase-1 technical target, protected meanings, non-goals, canonical owners or deterministic checks.

**PARTIAL for the newer role-return vocabulary.** PR #67 predates #73/#74 and therefore does not use today's explicit `Dev → Domain Review scholarly adequacy return` packet. It nevertheless preserves a review gate and explicitly refuses to equate CI with later migration/research authorization.

This is evidence that #74's current information model is directionally compatible with successful historical work; the first real #73→#74→#73 cycle is still required to test the new role-return contract itself.

## 7. Handoff information: derive vs supply

A future handoff should not force humans/chats to repeat facts already deterministically recoverable from canonical state.

### Prefer deriving from canonical state

Where the task supplies stable identifiers, derive rather than manually restate:

- Source title/identity from `source_id`;
- File Source ownership from `file_id`;
- Project root from `project.yml: project_source_id`;
- `internal/external/project_root` structural status from `project_source_id + part_of*`;
- Project(s) structurally containing a Source;
- concrete File provenance from `corpus/files.tsv`;
- existing Project→Source research functions from source-use records;
- exact source-wide folio/image/PDF mapping from an established crosswalk;
- validator/contract result for already-formalized structure.

### Must be supplied or explicitly established by the sending role

These are not safely derivable merely from repository structure:

- the demonstrated research/problem trigger;
- why the finding matters now;
- the exact evidence/fixture inspected;
- what is established versus unresolved/not investigated;
- the specific scholarly/information distinction that must survive;
- the requested downstream action;
- admitted scope/non-goals where material;
- scholarly acceptance/return question;
- genuinely owner-reserved purpose/rights/publication/admission facts;
- specialist judgement that has not been independently established.

### Only if applicable

- migration/loss constraints;
- derivative/image transformation provenance;
- independent specialist-review status;
- model/tool/version information when materially relevant;
- research-ready evidence-access path for tasks that need direct source inspection.

This distinction should be tested by #77 before any template freezes these elements into manual form fields.

## 8. Risk → control → remaining evidence matrix

| Risk | Current primary control | Deterministic part now | Remaining non-deterministic / empirical need |
|---|---|---|---|
| role drift | #71–#77 boundaries; #74 stop rule | role/task identifiers and some completeness may later be checkable | whether a finding crosses a scholarly authority boundary remains Domain Review judgement |
| context omission | AGENTS applicable-context rule | canonical owner/reference resolution is available | #77 must test what minimum context a fresh role actually misses |
| prompt dependency | canonical state + restartability | Source/Project/File structure already resolved from repo | real cross-chat handoff still needed to falsify missing process state |
| semantic reinterpretation by Dev | #73 handoff + #74 return | settled structural semantics can be regression-tested | scholarly adequacy cannot be reduced to CI |
| false determinism | #66 three-level distinction | known structural failure classes can be negative-tested | deciding whether a new phenomenon is stable/generic remains scholarly review |
| CI = scholarly acceptance | #74 return rule | CI result is explicit technical evidence | Domain Review acceptance remains required for scholarly semantics |
| silent canonical overwrite | #66 transition discipline | some history/reference invariants may become executable | final G2 transition representation waits for #64 |
| handoff information loss | #77 candidate contract | presence/completeness may later be checkable | exact minimum fields must be learned from real handoffs |
| owner fallback overload | AGENTS + UX-011/012 + #75 | deterministic repository mechanics can be resolved without owner | genuine purpose/rights/use choices remain human |
| specialist-status confusion | AI governance + #76 | explicit status/presence can be structurally checked when represented | independent specialist judgement remains external/human evidence |
| source/context contamination | #72/#73 stage rules | context package composition could be controlled later | task-specific contamination boundary remains scholarly-method judgement |
| evidence inaccessible in fresh context | #78 | path/reachability and exact File identity may be technically checked | rights/storage/retrieval policy and scholarly sufficiency may require judgement |
| rights/data leakage | storage/right state + AGENTS hard stops | repo path/storage status can be checked where formalized | authority interpretation remains human/institutional when unresolved |
| role proliferation | #71 lean blueprint | no executable control needed | architecture/governance judgement based on demonstrated burden |
| process bloat | #77 falsification criteria | no form/engine has been implemented | real handoff burden must be observed |
| technical self-assurance | tests + scholarly return | regressions can be independent of model judgement | separate technical reviewer only on demonstrated high-consequence trigger |
| tool/model drift | provenance/evaluation triggers | version/fixture regression possible when material | systematic AI evaluation trigger has not fired |

## 9. #78 engineering consequence

#78's distinction is retained as an explicit engineering constraint:

```text
IDENTIFIABILITY != REPRODUCIBILITY != RESEARCH-READY AVAILABILITY
```

Current Source Contract coverage strongly protects identifiability/provenance and some preservation claims. It does not and should not claim that a fresh authorized context can open an externally controlled/restricted source simply because its File ID/SHA/crosswalk is known.

Therefore a future Task Start/Resume or source-access control may need to test actual evidence accessibility where the NEXT ACTION requires direct inspection. That control belongs to #78/#77 falsification, not to this Phase-A Source Contract expansion.

## 10. Technical-assurance conclusion

No separate Technical Assurance role is justified by this audit.

The current layered assurance path is adequate for the demonstrated workload:

```text
settled requirement
→ deterministic contract/validator where justified
→ regression fixture
→ CI
→ Dev result
→ Domain Review when scholarly semantics are carried
→ canonical persistence / NEXT ACTION
```

Create an independent technical-assurance function only if a real trigger appears, such as repeated high-consequence defects surviving ordinary Dev regression checks, institutional transfer/release requirements, or systematic AI infrastructure where evaluator/implementer independence materially changes reliability.

## 11. Independent Phase-A completion status

Completed independently of #64:

- [x] competency→Requirement→Owner→Control mapping;
- [x] executable Source Contract coverage inventory;
- [x] prioritized missing regression fixtures for already-settled high-value invariants;
- [x] CI verification of the added fixtures;
- [x] historical Dev restartability test using #58/#59/PR #67;
- [x] derive-vs-supply handoff information analysis;
- [x] risk→control→remaining-evidence matrix;
- [x] Technical Assurance trigger boundary retained without new role.

Still intentionally waiting for live fixtures:

- [ ] first real #72→#73 handoff from #64;
- [ ] first real #73→#74 admitted technical handoff;
- [ ] first real #74→#73 scholarly adequacy return;
- [ ] #77 decision on whether persistent handoff/task fragments materially help;
- [ ] #78 fresh-context source-evidence availability test;
- [ ] G2-specific deterministic witness/locus/transition checks.

## 12. Stop / next action for #79

Do not continue by inventing additional controls merely because the audit can imagine them.

The independent Phase-A work is complete enough to wait for real fixtures.

Next #79 evidence should come from either:

1. a demonstrated regression/control failure in already-settled technical semantics; or
2. the first real #64-derived #73→#74 handoff, which tests whether this competency/control model is sufficient without old-chat reconstruction.

Until then, #64 and the active scholarly `NEXT ACTION` remain primary.
