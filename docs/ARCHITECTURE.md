# Architecture

## Status

This is the initial architecture direction. It is intentionally lightweight
until the first Godot project scene and gameplay slice are implemented.

## Proposed Layers

### 1. Platform and Runtime

Godot, Android export, OpenXR initialization, Quest device configuration, and
vendor-specific extensions live at the platform boundary.

The [Godot XR Template](https://github.com/GodotVR/godot-xr-template) is the
initialization and export reference for this layer.

### 2. XR Foundation

The XR origin, camera, tracked controllers, hand tracking, input actions,
haptics, locomotion providers, and interaction pointers form the XR foundation.
Godot XR Tools should provide established mechanics where possible.

The [Godot XR Tools repository](https://github.com/GodotVR/godot-xr-tools) is the
primary API and mechanics reference for this layer.

### 3. Interaction and Gameplay

Gameplay systems consume stable interaction contracts rather than reaching
through platform-specific nodes. Grabbable objects, interactable controls,
climbing surfaces, and UI should expose clear ownership and lifecycle behavior.

### 4. Presentation

World scenes, spatial UI, audio, effects, comfort options, and feedback are
presentation concerns. They should not own inventory, progression, or device
initialization state.

The [Flynn demo](https://github.com/BastiaanOlij/godot-xr-flynn-demo) informs
larger scene and game-loop organization. The [Malcolm Nixon demo](https://github.com/Malcolmnixon/godot-xr-tools-demo)
informs specialized locomotion recipes and movement test environments.

## Boundary Rules

- Keep OpenXR and Quest-specific code at the platform boundary.
- Prefer Godot XR Tools over duplicating common XR mechanics.
- Keep gameplay logic testable without requiring a physical headset where
  possible.
- Treat input actions as named contracts, not scattered controller checks.
- Separate headless CI from physical XR validation.
- Keep performance-sensitive allocations and effects visible in profiling.

## Proposed Scene Flow

`Boot -> XR initialization -> Main menu -> Gameplay scene -> Pause/settings`

The first implementation may simplify this flow, but device initialization must
have a clear failure path when no XR runtime is available.

## Future Decisions

Record significant changes in the audit archive and update this document when a
decision becomes authoritative.
