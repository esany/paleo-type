# SD-KA-01 implementation plan

## WP1 — current branch

1. Persist the Human-Owner admission and affected navigation/decision surfaces.
2. Create the in-place `engineering/` semantic owners and representative F01–F45 baseline.
3. Implement the standard-library validator/query entrypoint and regression fixtures.
4. Run the full existing and WP1-specific deterministic checks.
5. Return actual state, finding disposition, ADR/configuration consequences and downstream readiness to #244/#256.

## Later admitted work

WP2 derives current/query views; WP3 adds Human/developer/Agent contexts and `.prompt`; WP4 adds engineering fitness; WP5 performs controlled physical migration; WP6 performs adversarial qualification and Result Review. No later work is started by WP1's technical PASS alone.
