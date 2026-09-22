# Level Flow

## Responsibility

The level-flow layer owns transitions, loading policy, and cleanup between menu,
testbed, and gameplay scenes. Individual levels must not initialize the XR
runtime or globally own application state.

## Initial Flow

```text
Boot -> Main Menu -> Interaction Lab -> Main Menu
```

## Planned Expansion

```text
Main Menu -> Tutorial -> Locomotion Lab -> Interaction Lab -> Gameplay Level
```

## Requirements

- One canonical XR initialization path.
- Explicit loading and failure states.
- No stale references to unloaded levels.
- Shared resources are cached deliberately and released when appropriate.
- Scene transitions remain testable without a headset.
