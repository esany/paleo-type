# Route B / #90 — default-branch promotion enforcement Requirements resolution

Status: **COMPLETE bounded D-016 Requirements result under #214.**

Authority / scope:

- input Analysis owner: GitHub Issue #90 fresh technical audit;
- programme navigation: GitHub Issue #206;
- governing change lifecycle: `methodology/maintenance.md` / D-016;
- this file is a bounded Requirements-resolution artifact, not METHOD, not Project priority, not implementation admission, and not authority to purchase/upgrade a GitHub plan or change repository visibility/ownership.

Baseline inspected: `main@4d176a9038cf2327d565da470268b60512a7e028`.

## 1. Requirements question

Given the demonstrated #90 failure — direct promotion to canonical `main` remains possible even though CI exists — what exact properties must the smallest acceptable solution satisfy before any implementation mechanism is chosen?

## 2. Demonstrated inputs

The #90 audit established:

- repository is private and user-owned;
- `main` remains `protected:false` with classic protection disabled and no required checks;
- exactly one repository workflow exists: `.github/workflows/source-contract.yml`;
- its single job `validate` runs on pull requests and on pushes to `main`;
- `validate` has recent successful PR and `main`-push executions;
- the pre-audit `main` head had no associated PR, directly demonstrating that CI existence does not enforce PR promotion;
- current native private-repository protection capability is plan-gated under the observed GitHub response;
- the current ChatGPT GitHub connector lacks repository Administration permission and cannot configure branch protection/rulesets.

Current GitHub documentation inspected on 2026-09-16 confirms that protected branches and repository rulesets are available for private repositories with GitHub Pro / Team / Enterprise capability, and that classic branch protection can require a pull request without requiring approvals, require status checks, disable force pushes/deletion, and apply restrictions to administrators.

## 3. Required properties

### RB-REQ-01 — canonical promotion boundary

Changes entering canonical `main` must go through a pull request rather than unrestricted direct promotion.

This controls promotion only. It must not constrain ordinary exploratory work on non-canonical branches/workspaces beyond what is necessary for the final merge boundary.

### RB-REQ-02 — smallest current deterministic gate

The existing GitHub Actions job **`validate`** is the only currently evidenced required-check candidate.

The solution must require `validate` to pass before promotion to `main`. It must not invent a second required check, duplicate the workflow, or add a generic assurance pipeline absent new evidence.

### RB-REQ-03 — no mandatory human approval by default

PR use must not silently become a review-bureaucracy requirement.

No approving review, CODEOWNERS review, last-push approval, conversation-resolution requirement or additional reviewer count is required by current evidence. Human/specialist review remains governed separately by consequence and scholarly METHOD.

### RB-REQ-04 — no silent admin / automation bypass

Owner/admin and automation-assisted work must be subject to the same canonical promotion boundary unless a future concrete recovery requirement separately justifies a narrowly scoped bypass.

The current solution must therefore not preserve an ordinary admin/owner bypass for PR/check enforcement.

### RB-REQ-05 — irreversible-history protections

Force pushes to `main` and deletion of `main` must be blocked.

Acceptance must establish these properties by protection readback and safe/non-destructive enforcement evidence; no destructive test against live canonical `main` is required.

### RB-REQ-06 — loose status-check freshness

The solution must **not** require the branch to be up to date with `main` before merge unless later evidence demonstrates that stricter freshness is necessary.

The current repository evidence supports a required `validate` result, not mandatory rebuild/rebase churn.

### RB-REQ-07 — preserve repository privacy and ownership

Current repository privacy and user ownership are preserved by this Requirements result.

Making the repository public, transferring it to an organization, or otherwise changing repository authority/visibility is outside scope and requires a separate Human-Owner decision.

A platform-plan/capability prerequisite may be surfaced, but this Requirements stage does not authorize purchase or subscription change.

### RB-REQ-08 — preserve merge-method flexibility

Current availability of merge commit, squash merge and rebase merge need not change.

No demonstrated #90 failure is caused by merge-method plurality. The enforcement target is the promotion gate, not merge-style uniformity.

### RB-REQ-09 — technical PASS stays technical

Passing `validate` establishes only the deterministic properties that workflow actually checks.

It must never be interpreted as manuscript truth, specialist validation, Human-Owner scholarly acceptance, Project priority, publication approval or generalized research adequacy.

### RB-REQ-10 — restartable and testable enforcement state

After implementation, a fresh capable context must be able to establish from GitHub/repository state that:

- PR-before-merge is enforced for `main`;
- `validate` is required;
- admin/owner does not silently bypass the boundary;
- force pushes and deletion are disabled;
- no additional policy layer was introduced by implication.

The final Result Review must test actual enforcement, not merely document intended settings.

## 4. Formal Requirement / owner disposition

**No new row in `requirements/domain-requirements.tsv` is warranted.**

Reason: #90 is a concrete repository-specific deterministic Git promotion-control requirement. Its semantics are already bounded by the Governing Objective, AGENTS technical-subsidiarity/authority rules, D-016, and the explicit #90 acceptance boundary. Promoting this into a cross-domain scholarly Requirement family would create a broader owner than the evidence warrants.

The durable bounded Requirements owner for this Route-B arc is this artifact plus #90's technical work/audit state.

## 5. Requirements-stage conclusion

Disposition: **bounded Concept warranted.**

The required properties are precise enough to compare implementation mechanisms without guessing:

```text
private/user-owned repository preserved
+ PR-only canonical promotion
+ existing validate check required
+ zero mandatory approvals by default
+ no admin/automation bypass
+ no force push / no deletion
+ no hard up-to-date requirement
+ current merge methods preserved
+ CI PASS remains technical only
+ actual enforcement must be tested
```

The remaining unresolved design questions are mechanism-level only:

- classic Branch Protection versus repository Ruleset;
- how the private-repository capability prerequisite is satisfied;
- which authorized GitHub Administration surface performs configuration and readback.

Those belong to the distinct D-016 Concept stage, not Requirements.

## 6. Deliberate non-changes

This Requirements result creates no:

- GitHub plan purchase/upgrade;
- visibility or ownership change;
- protection/ruleset configuration;
- new CI workflow/check;
- approval requirement;
- CODEOWNERS policy;
- merge queue;
- signed-commit requirement;
- deployment gate;
- strict up-to-date rule;
- METHOD or Project mutation;
- scholarly `NEXT ACTION`.
