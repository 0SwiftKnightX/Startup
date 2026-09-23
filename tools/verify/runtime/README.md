# Runtime Verification

This folder contains headless Godot scenes and GDScript tests.

Runtime tests execute actual project scripts and report machine-readable pass/fail output. They are stronger than text checks but do not replace physical Quest testing.

Current test:

- `hero_state_runtime_test.tscn` executes the valid and invalid `HeroState` transitions and verifies reset behavior.
