# Verification Framework

This verification system is the reusable gate for the current first playable
slice and every future feature added to the project.

## Purpose

Every feature, controller, and system added to the project must have a verifier that can be executed through the same runner. The runner is designed to fail fast when a required part of the current slice is missing, and to keep the project honest by checking both project structure and expected runtime wiring.

## Structure

- `run_all.py` - master verifier runner
- `verifier_manifest.json` - required verifier registry
- `verifiers/` - feature, setup, scene, XR, and arena checks
- `runtime/` - headless Godot behavior tests
- `README.md` files in child folders - local tool ownership and usage notes
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

- Setup controller
- Main menu
- Interaction lab
- Hero flow
- Hero state runtime
- Project contracts
- XR player
- XR runtime
- Arena target

These are the baseline checks for the first playable slice.

## How to run

```bash
python3 tools/verify/run_all.py
```

## Future rule

When a new feature or system is implemented, add a new verifier module in
`tools/verify/verifiers/`, register its class in
`verifier_manifest.json`, and add a runtime test under `runtime/` when static
inspection cannot prove behavior.
