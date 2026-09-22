# Verification Framework

This verification system is intentionally built as a reusable gate for the game foundation.

## Purpose

Every feature, controller, and system added to the project must have a verifier that can be executed through the same runner. The runner is designed to fail fast when a required part of the current slice is missing, and to keep the project honest by checking both project structure and expected runtime wiring.

## Structure

- `run_all.py` - master verifier runner
- `verifiers/` - feature and setup checks
- each verifier class must subclass `BaseVerifier`
- new system or feature check should be added as a new file in `verifiers/`

## Required behavior

When the runner executes:

1. Confirm setup-level requirements are valid.
2. Confirm required feature files exist.
3. Confirm feature wiring matches the intended architecture.
4. Confirm the Godot project is importable or at least structurally valid.
5. Report pass/fail for every verifier.
6. Return a non-zero exit code if any verifier fails.

## Current first-slice verifiers

- Setup controller verifier
- Main menu feature verifier
- Interaction lab feature verifier
- XR runtime verifier

These are the baseline checks for the first playable slice.

## How to run

```bash
python3 tools/verify/run_all.py
```

## Future rule

When a new feature or system is implemented, add a new verifier module in `tools/verify/verifiers/` and the main runner will automatically include it.
