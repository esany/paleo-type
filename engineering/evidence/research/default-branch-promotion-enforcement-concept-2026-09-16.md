# Route B / #90 — default-branch promotion enforcement Concept

Status: **COMPLETE bounded D-016 Concept result under #215. Human-Owner implementation admission still required.**

Upstream:

- Analysis: #90 fresh technical audit — promotion gap CONFIRMED;
- Requirements: #214 / `requirements/default-branch-promotion-enforcement-requirements-resolution-2026-09-16.md` — COMPLETE, bounded Concept warranted;
- programme navigation: #206;
- lifecycle authority: `methodology/maintenance.md` / D-016.

Baseline: `main@4d176a9038cf2327d565da470268b60512a7e028`.

This file is Concept evidence. It is not protection configuration, subscription/plan authority, repository-visibility authority, METHOD, Project state or implementation admission.

## 1. Concept question

What is the smallest coherent mechanism that satisfies the fixed Route-B Requirements for canonical `main` promotion while preserving the current private, user-owned repository and avoiding a new policy/workflow layer?

## 2. Current capability facts

Fresh audit/current documentation establishes:

- repository is private, user-owned and currently `protected:false`;
- the only current CI workflow is `source-contract`, with one materially relevant job `validate`;
- GitHub supports classic protected branches and repository rulesets for private repositories with eligible paid capability; for the current user-owned repository, GitHub Pro is the smallest documented plan tier that supplies private-repository protected branches/rulesets;
- classic branch protection supports `Require a pull request before merging` with approvals optional, required status checks, admin enforcement, and force-push/deletion controls;
- the installed ChatGPT GitHub connector lacks repository Administration permission and does not expose a branch-protection/ruleset write action.

Therefore the Concept must separate **platform prerequisite**, **protection mechanism**, **administrative execution surface** and **enforcement validation** rather than pretending CI alone can solve the gap.

## 3. Alternatives

### C1 — classic Branch Protection for `main`

Mechanism:

- one branch-protection rule targeting `main`;
- require pull request before merge;
- do not require approvals;
- require the observed GitHub Actions check corresponding to job `validate`;
- do not require branch to be up to date before merge;
- apply protection to administrators / do not allow bypassing;
- force pushes disabled;
- deletion disabled;
- leave current merge methods otherwise unchanged.

Strengths:

- directly expresses every fixed Requirement;
- one native GitHub object for one branch;
- no new repository workflow, policy file, service, bot or state store;
- clear settings/readback and straightforward rollback/edit path;
- preserves free branch-level exploration and controls only canonical promotion.

Costs/dependencies:

- private-repository protection capability must first be available;
- configuration/readback requires an authorized GitHub Administration surface outside the current ChatGPT connector.

Disposition: **SELECTED Concept.**

### C2 — repository Ruleset targeting `main`

A branch Ruleset can also require pull requests, status checks and block force pushes/deletion, with explicit bypass configuration.

Strengths:

- modern rule model with visible composition and ruleset inspection;
- useful where multiple overlapping rules, branches or organization-level policy need composition.

Weaknesses for this repository:

- same private-repository capability prerequisite;
- no demonstrated need for overlapping/multiple rulesets, organization-level reuse or richer composition;
- adds a named rule layer where a single classic protection rule is sufficient.

Disposition: **valid but not smallest; reject as default for current scope.**

### C3 — CI/prose convention only

Examples: keep `push`/`pull_request` workflow, document that contributors should use PRs, or add another CI workflow without branch enforcement.

Failure:

- does not prevent direct promotion;
- does not make `validate` a merge prerequisite;
- does not block admin/automation bypass, force push or deletion.

Disposition: **rejected as insufficient.**

### C4 — make repository public to obtain Free-plan protection capability

This could alter platform feature availability but changes repository visibility/rights exposure rather than merely enforcing promotion.

Disposition: **rejected from this Concept scope.** Repository privacy is a fixed Requirements property and visibility change requires separate Human-Owner authority with its own consequences.

### C5 — transfer repository / introduce organization-level governance

Could unlock different plan/role structures but would change ownership/administration topology and add governance beyond the evidenced need.

Disposition: **rejected as disproportionate.**

### C6 — defer at capability boundary

The Human Owner may explicitly defer implementation while preserving #90 as unresolved evidence.

Disposition: **valid owner disposition, not the selected implementation Concept after B-CONTINUE.**

## 4. Selected Concept — thin native protection

Selected topology:

```text
existing repository / existing main
        ↓ platform prerequisite
eligible private-repository protection capability
        ↓ one native object
classic Branch Protection: main
        ↓ one existing CI gate
source-contract / validate
        ↓ enforcement validation
safe PR fixture + settings/readback
```

No new repository architecture is introduced.

### 4.1 Platform prerequisite

Preserve current repository facts:

- visibility: private;
- ownership: current user-owned repository.

Before configuration, an eligible private-repository branch-protection capability must be available. Under current GitHub documentation and the audit response, the smallest relevant capability for this user-owned private repository is GitHub Pro (or an already-equivalent eligible capability if repository/account state changes independently).

**This Concept does not authorize purchase, billing, plan upgrade or visibility change.** The Human Owner must separately provide/confirm the platform prerequisite before implementation can execute.

### 4.2 Exact protection semantics

Once the prerequisite exists, configure one classic branch-protection rule for branch name pattern `main` with these intended semantics:

1. **Require a pull request before merging:** ON.
2. **Require approvals:** OFF / zero mandatory approvals.
3. **Require status checks to pass before merging:** ON.
4. Required check: select the live observed check context produced by the existing `validate` job; do not guess a stale context string if GitHub presents a more qualified check name.
5. **Require branches to be up to date before merging / strict status checks:** OFF.
6. **Do not allow bypassing the above settings / admin enforcement:** ON.
7. **Allow force pushes:** OFF.
8. **Allow deletions:** OFF.
9. CODEOWNERS review, last-push approval, conversation resolution, signed commits, linear history, merge queue, deployment gates and additional checks: OFF / unchanged unless already independently required by current repository state.
10. Existing merge methods (merge commit / squash / rebase): preserve.

No bypass actor is added by default.

### 4.3 Administrative execution surface

The current ChatGPT GitHub connector cannot perform this configuration because it lacks repository Administration permission and a branch-protection write action.

Admitted implementation therefore requires an authorized administrative surface controlled by the Human Owner, for example GitHub repository Settings or another explicitly authorized GitHub Administration-capable path.

This is a capability boundary, not a reason to replace the selected mechanism with a weaker CI-only solution.

### 4.4 Recovery / rollback

Do not preserve a standing merge/push bypass merely for recovery.

If the selected protection later blocks legitimate repository recovery (for example a broken required-check context), recovery is performed by an explicit Human-Owner administrative edit to the protection configuration, with the reason made visible in #90/#206 if it changes the admitted protection semantics.

Routine recovery therefore changes configuration deliberately rather than silently bypassing canonical promotion.

## 5. Enforcement test plan after implementation

Acceptance must establish actual enforcement, not only intended configuration.

### T1 — settings/readback

Using an Administration-capable surface, confirm:

- `main` is protected;
- PR-before-merge is enabled;
- required status checks include the live `validate` check context;
- strict/up-to-date requirement is disabled;
- admin bypass is disabled / protection applies to administrators;
- force pushes are disabled;
- deletion is disabled.

### T2 — failing required-check fixture

Create a disposable branch/PR containing a branch-local deterministic test fixture that makes `validate` fail without modifying canonical `main`.

Verify:

- workflow runs and fails as designed;
- PR merge is blocked while `validate` fails;
- fixture PR is closed without merge and branch can be discarded.

This proves required-check enforcement without contaminating canonical state.

### T3 — passing PR fixture

Create or use a harmless bounded PR whose `validate` job passes.

Verify the PR is mergeable when the fixed protection requirements are otherwise satisfied and can be promoted through the normal PR path.

### T4 — PR/admin/direct-promotion boundary

Use protection readback plus GitHub's enforced PR requirement/admin enforcement as the primary evidence that owner/admin is not an ordinary bypass path.

Do **not** perform a risky direct-push/force-push/delete experiment against live `main` merely to prove rejection. A destructive live-branch test is disproportionate when settings/readback and safe PR enforcement fixtures establish the configured boundary.

### T5 — assurance-language regression

Confirm `.github/workflows/source-contract.yml` still states that workflow PASS does not establish manuscript truth, specialist validity, Human-Owner acceptance or merge/release authority beyond the enforced technical gate.

## 6. Implementation scope if later admitted

A sufficiently precise Human-Owner admission may authorize only:

1. confirmation/provision of eligible private-repository protection capability by the Human Owner;
2. one classic branch-protection rule for `main` with the exact semantics in §4.2;
3. no new CI workflow or substantive repository code change for the protection mechanism itself;
4. safe enforcement fixtures described in §5;
5. Result Review against #214 Requirements;
6. #90/#206/README freshness propagation only as actually changed.

Configuration must be applied through an authorized GitHub Administration surface. The current ChatGPT connector cannot silently substitute for that surface.

## 7. Explicit non-goals

No:

- repository visibility change;
- repository transfer;
- organization migration;
- standing bypass actor;
- additional mandatory approval;
- CODEOWNERS policy;
- merge queue;
- signed-commit requirement;
- strict up-to-date rule;
- deployment gate;
- new CI workflow/check;
- generic security framework;
- GitHub policy registry;
- METHOD mutation;
- Project scholarly scope or `NEXT ACTION`.

## 8. Concept conclusion / D-016 boundary

Disposition: **C1 classic Branch Protection selected as the smallest coherent Route-B mechanism.**

The Concept is sufficiently precise for Human-Owner review / explicit implementation admission, but two boundaries remain owner-controlled:

1. whether to admit this exact protection implementation;
2. whether/how the required private-repository platform capability is provided.

Possible next dispositions:

- **B-ADMIT** — admit the exact bounded implementation in §6, conditional on the platform prerequisite being available;
- **B-REFINE** — return this Concept for bounded refinement;
- **B-REJECT** — reject this Concept while retaining #90's confirmed gap;
- **B-DEFER** — defer implementation at the platform-capability boundary.

Until explicit admission, #90 remains unresolved and no protection configuration may be inferred from B-CONTINUE alone.
