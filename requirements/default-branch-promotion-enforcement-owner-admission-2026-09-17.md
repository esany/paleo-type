# Route B / #90 — Human-Owner implementation admission — 2026-09-17

Status: **B-ADMIT — human-owner decision and bounded D-016 implementation admission.**

This record persists the Human Owner's explicit decision to admit the already-completed Route-B Concept under #215. It authorizes only the bounded protection implementation defined below. It does not itself perform GitHub configuration, purchase or upgrade a plan, change repository visibility/ownership, create scholarly priority, or establish that #90 is resolved.

## 1. Admitted upstream scope

Upstream stages are complete:

- Analysis / audit: #90 — deterministic default-branch promotion gap CONFIRMED;
- Requirements: #214 / `requirements/default-branch-promotion-enforcement-requirements-resolution-2026-09-16.md`;
- Concept: #215 / `requirements/default-branch-promotion-enforcement-concept-2026-09-16.md`;
- programme navigation: #206;
- lifecycle authority: `methodology/maintenance.md` / D-016.

The Human Owner admits **C1 — one classic Branch Protection rule for `main`** as the implementation scope.

## 2. Exact admitted protection semantics

Once the platform and administrative prerequisites are actually available, implementation may configure exactly one classic protection rule for branch pattern `main` with these semantics:

1. require pull request before merging: **ON**;
2. mandatory approving reviews: **0 / OFF**;
3. require status checks before merging: **ON**;
4. required check: the live GitHub check context produced by the existing `validate` job; resolve the live context at configuration time rather than guessing a stale string;
5. require branch to be up to date / strict status checks: **OFF**;
6. admin/owner bypass of the protection boundary: **OFF**; protection applies to administrators;
7. force pushes: **OFF**;
8. branch deletion: **OFF**;
9. preserve existing merge-commit / squash / rebase availability;
10. no bypass actor is added by default.

## 3. Admitted execution and validation

Within this admitted scope, bounded implementation may proceed without another owner-approval loop once the prerequisites below are available. It may include:

- configuration through an explicitly authorized GitHub Administration-capable surface;
- Administration/settings readback of the resulting protection;
- a disposable PR whose branch-local deterministic fixture deliberately makes `validate` fail, proving merge is blocked while the required check fails;
- a harmless passing PR proving normal PR promotion works when `validate` passes;
- non-destructive verification that admin bypass is disabled and force-push/deletion protections are configured;
- Result Review against the fixed #214 Requirements;
- only the #90/#206/README freshness propagation materially caused by the result.

No destructive force-push/delete experiment against live canonical `main` is required.

## 4. Explicit non-authorizations

B-ADMIT does **not** authorize:

- GitHub plan purchase, billing or subscription change;
- making the repository public;
- repository transfer or organization migration;
- a Ruleset substitution merely because it exists;
- a new CI workflow or extra required check;
- CODEOWNERS or mandatory approving review;
- merge queue, signed-commit requirement, deployment gate or strict/up-to-date requirement;
- standing recovery/bypass actors;
- METHOD or formal Requirement mutation;
- Project scholarly scope, priority or `NEXT ACTION`;
- interpreting CI PASS as manuscript truth, specialist validation or Human-Owner scholarly acceptance.

A genuinely new material choice outside the admitted Concept returns to D-016 owner review rather than being silently absorbed.

## 5. Fresh prerequisite state at admission

Freshly checked on 2026-09-17:

- `main@855023f0b8b8bd2a61aef9bc76e0992844d33783` reports `protected:false`, protection disabled and required status-check enforcement off;
- the repository remains private and user-owned;
- the repository Rulesets endpoint still returns GitHub `403`: `Upgrade to GitHub Pro or make this repository public to enable this feature.`;
- current GitHub documentation states that protected branches for private repositories require GitHub Pro, Team, Enterprise Cloud or Enterprise Server capability;
- the installed ChatGPT GitHub connector does not expose repository `Administration` write permission / branch-protection write action.

Therefore **implementation is admitted but cannot currently execute through this connector, and the observed private-repository platform capability is not yet sufficient.** This is a concrete implementation prerequisite, not permission to weaken the selected mechanism.

Repository privacy remains fixed by the admitted Requirements; public visibility is not an inferred workaround.

## 6. Restart / continuation boundary

A fresh context may continue directly from this admission **without another admission ceremony** only when both of the following are true:

1. eligible private-repository protected-branch capability is available; and
2. an explicitly authorized GitHub Administration-capable execution surface is available.

It must then freshly re-read #90/#206, this admission, the Requirements/Concept artifacts and the actual GitHub protection/check state before configuration.

If either prerequisite remains unavailable, record only that implementation-local capability state. Do not call #90 solved, do not invent substitute CI/prose enforcement, and do not infer a programme STOP.

After successful configuration and enforcement tests: perform Result Review → return the result to #90 and #206 → run the final programme-completion review.
