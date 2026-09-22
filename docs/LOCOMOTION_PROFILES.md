# Locomotion Profiles

Locomotion is organized as composable profiles rather than one large movement
script. The profiles below are references for future Godot XR Tools integration.

## Profiles

- **Direct movement:** smooth movement with comfort settings.
- **Snap turn:** discrete rotation with configurable increments.
- **Teleport:** targeted relocation with valid-surface filtering.
- **Climbing:** physics-aware handholds and release behavior.
- **Gliding:** controlled aerial movement and safe landing behavior.
- **Low traction:** reduced friction for ice-like surfaces.
- **Wind:** directional forces with bounded player control.

## Comfort and Performance

Every profile must expose comfort settings, define its interaction with other
profiles, and be tested in isolation before it is combined in a level. Movement
features are not considered complete until they pass desktop smoke testing and a
physical Quest 3S test.
