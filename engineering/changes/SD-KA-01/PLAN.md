# SD-KA-01 implementation plan

## WP1 — verified and returned

WP1 persisted the Human-Owner admission, established the in-place `engineering/` semantic owners and representative F01–F45 baseline, added deterministic structural validation and returned its exact result/whole-system consequence to #244. No physical migration or scholarly Project state changed.

## WP2 — current implementation cursor (#257)

Execution baseline: `main@2c683beaefa18bc07810bf91cbbe67a07ef81f6a`.

1. Advance bounded work ownership from completed #256/WP1 to #257/WP2 without changing D-016 admission or accepted architecture.
2. Extend configuration/currentness semantics with explicit change state, focus/absence and applicability provenance.
3. Implement rebuildable current/query derivation in `tools/engineering.py` without committing a generated current-state clock.
4. Add adversarial deterministic fixtures for proposed-as-current, work-metadata/currentness laundering, latest-wins pressure, explicit absence and invalid applicability/transition semantics.
5. Run full repository tests and Fresh Context review against the exact PR head.
6. Merge only after scoped technical review/CI; run post-merge exact-main assurance.
7. Persist the WP2 Result/whole-system return, reconcile #257 and #244, and expose only the readiness that actually follows for WP3/WP4.

## Later admitted work

WP3 adds Human/developer/Agent contexts and `.prompt`; WP4 adds engineering fitness/CI closure; WP5 performs controlled physical migration; WP6 performs adversarial qualification and terminal SD-KA-01 Result Review. No later work is started by WP2 technical PASS alone.
