# Route B / #90 — Human-Owner defer / risk disposition — 2026-09-17

Status: **B-DEFER — explicit Human-Owner disposition of the current Route-B implementation/risk at the GitHub Free/private-repository platform boundary.**

This record is a new Human-Owner decision after the earlier `B-ADMIT` record. It does not claim that branch protection has been implemented or that the deterministic enforcement gap disappeared. It changes only the current programme/work disposition of that known gap.

## 1. Basis

Current authoritative Route-B chain:

- Analysis/audit: #90 — deterministic default-branch promotion gap CONFIRMED;
- Requirements: #214 / `requirements/default-branch-promotion-enforcement-requirements-resolution-2026-09-16.md`;
- Concept: #215 / `requirements/default-branch-promotion-enforcement-concept-2026-09-16.md`;
- bounded implementation admission: `requirements/default-branch-promotion-enforcement-owner-admission-2026-09-17.md` / PR #219;
- programme navigation: #206;
- lifecycle authority: `methodology/maintenance.md` / D-016.

Fresh state before this disposition:

- repository remains private and user-owned;
- `main` remains unprotected (`protected:false`, classic protection disabled, required status-check enforcement off);
- the GitHub feature response for this private repository still requires an eligible paid capability or public visibility;
- the Human Owner states that the current account is using the free GitHub tier;
- repository privacy is retained; making the repository public is not selected as a workaround;
- the current ChatGPT GitHub connector still has no repository-Administration branch-protection write surface.

## 2. Human-Owner decision

The Human Owner explicitly chooses:

**B-DEFER at the platform-capability boundary.**

Consequences:

1. no GitHub plan purchase/upgrade is authorized or required by the current research-system programme;
2. the repository remains private and under its current ownership;
3. the admitted classic `main` Branch Protection implementation is **not current work** while the required private-repository capability/admin execution path is unavailable and unselected;
4. #90's deterministic enforcement risk remains known and explicit rather than being called solved;
5. voluntary use of pull requests plus the existing `validate` workflow may continue as working practice, but must not be described as enforced branch protection;
6. this disposition does not create substitute CI/prose machinery, a new governance layer, Project priority or scholarly `NEXT ACTION`.

## 3. Retained known risk

Under the current Free/private state:

```text
PR-only promotion to main: NOT ENFORCED
validate as required merge gate: NOT ENFORCED
admin/owner direct-promotion prevention: NOT ENFORCED
force-push/delete protection: NOT ESTABLISHED
```

The Human Owner accepts this as a **known deferred technical risk for the current programme state**, rather than purchasing/changing platform capability solely to eliminate it now.

This is a risk/work disposition, not a statement that the control is unnecessary in every future context.

## 4. Future reactivation boundary

#90 may be reconsidered if the Human Owner later chooses to make an eligible private-repository protection capability and an authorized Administration-capable execution path available.

If that happens, a fresh context must re-read #90/#206, the Requirements, Concept, B-ADMIT and this B-DEFER record, and the actual GitHub protection/check state.

The previously admitted implementation scope may then be reused **without inventing a broader Concept**, provided its assumptions still match current state; the Human Owner must explicitly reactivate the deferred work before execution resumes.

No reactivation is inferred merely because a platform feature becomes available.

## 5. Programme consequence

The P3A programme synthesis defined PC7 completion as either:

- actual tested enforcement; **or**
- explicit Human-Owner re-disposition of the requirement/risk.

This B-DEFER decision satisfies the second completion path for the current research-system programme.

Therefore Route B is now:

```text
technical enforcement gap: STILL KNOWN
implementation: NOT EXECUTED
current Route-B work: DEFERRED / INACTIVE by Human-Owner decision
current programme residual from Route B: DISPOSITIONED
```

Return this consequence to #206 for the final programme-completion review.
