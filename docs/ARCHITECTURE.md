# Architecture

## Status

This is the current architecture direction for the first Quest gameplay slice.
The project is not being restarted; existing XR Tools and scene contracts are
being repaired and extended in place.

## Layers

### 1. Platform and Runtime

Godot 4.7.2, Android export, OpenXR initialization, Quest device configuration,
and vendor-specific extensions live at the platform boundary.

### 2. XR Foundation

The XR origin, camera, tracked controllers, hand tracking, input actions,
haptics, locomotion providers, gravity/body physics, and interaction pointers
form the XR foundation.

Godot XR Tools is the canonical source for common XR mechanics. Project-owned
scripts should not duplicate XR Tools movement, gravity, or controller behavior.

### 3. Interaction and Gameplay

Gameplay systems consume stable interaction contracts rather than reaching
through platform-specific nodes. Grabbable objects, interactable controls,
climbing surfaces, and UI expose clear ownership and lifecycle behavior.

### 4. Presentation

World scenes, spatial UI, audio, effects, comfort options, and feedback are
presentation concerns. They should not own inventory, progression, or device
initialization state.

## Boundary Rules

- Keep OpenXR and Quest-specific code at the platform boundary.
- Prefer Godot XR Tools over duplicating common XR mechanics.
- Keep gameplay logic testable without requiring a physical headset where possible.
- Treat input actions as named contracts, not scattered controller checks.
- Separate headless CI from physical XR validation.
- Keep performance-sensitive allocations and effects visible in profiling.
- Keep the canonical XR player in one scene.
- Keep the lobby/menu UI separate from the lobby world composition.

## Scene Flow

Boot -> XR initialization -> Quest lobby + menu -> Interaction Lab -> Pause/settings

scenes/main.tscn is the actual 3D lobby. It provides a floor, lighting, a
simple boundary wall, and the player spawn space. The menu itself remains a
separate main_menu_panel.tscn UI scene embedded through Viewport2Din3D.

scenes/xr_player.tscn is the canonical XR player and contains:

- XROrigin3D
- XRCamera3D
- XRToolsPlayerBody and gravity/ground handling
- left/right tracked controllers and hands
- left-stick direct movement
- right-stick snap/smooth turning
- pickup and pointer functions
- optional arm-swing movement
- OpenXR startup

scenes/interaction_lab.tscn remains a separate gameplay/test scene.

## Locomotion Responsibility

Physical XR locomotion is provided by XR Tools. The project-owned
comfort_locomotion.gd is only the desktop fallback and comfort-settings bridge.

The intended baseline is:

- gravity: XRToolsPlayerBody/environment physics
- physical body movement: XRToolsPlayerBody
- analog movement: left controller primary/thumbstick
- strafing: left controller secondary axis
- turning: right controller primary/thumbstick
- default turning: snap turn
- optional turning mode: smooth turn
- optional movement mode: arm-swing/jog

## Future Decisions

Teleportation, climbing, gliding, low-traction movement, wind, multiplayer,
construction, and enemy waves remain separate systems and should be added only
after the basic Quest lobby and first interaction loop are stable.
