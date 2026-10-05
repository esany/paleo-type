# SD-KA-01 implementation plan

## WP1 — verified and returned

WP1 persisted the Human-Owner admission, established the in-place `engineering/` semantic owners and representative F01–F45 baseline, added deterministic structural validation and returned its exact result/whole-system consequence to #244. No physical migration or scholarly Project state changed.

## WP2 — verified and returned (#257)

Execution baseline: `main@2c683beaefa18bc07810bf91cbbe67a07ef81f6a`.

Completed bounded sequence:

1. advanced work ownership from completed #256/WP1 to #257/WP2 without changing D-016 admission or accepted architecture;
2. extended configuration/currentness semantics with explicit change state, focus/absence and applicability provenance;
3. implemented rebuildable current/query derivation in `tools/engineering.py` without committing a generated current-state clock;
4. added adversarial deterministic fixtures for proposed-as-current, work-metadata/currentness laundering, latest-wins pressure, explicit absence and invalid applicability/transition semantics;
5. ran exact-head repository CI and repository-first fresh-context/self-review on PR #278;
6. merged at `main@e10a51a56a6db1924d4500698d2dd2be2b222bc4` and passed exact post-merge `source-contract` run #527;
7. persisted the WP2 Result/whole-system return and downstream readiness without promoting the whole SD-KA-01 target to accepted architecture.

## Next eligible admitted work

WP3 (#258) adds Human/developer/Agent contexts and `.prompt`. It is `ready-next` after WP1/WP2 but is not started by the WP2 return. WP4 adds engineering fitness/CI closure after the required preceding semantics exist; WP5 performs controlled physical migration; WP6 performs adversarial qualification and terminal SD-KA-01 Result Review.

No later work package is started by WP2 technical PASS alone.
