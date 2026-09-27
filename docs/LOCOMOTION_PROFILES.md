# Locomotion Profiles

Locomotion is organized as composable profiles. The current XR player already
uses Godot XR Tools for physical movement, gravity, direct thumbstick movement,
and turning; the project-owned script exists only for desktop fallback and comfort
settings.

## Profiles

- **Direct movement:** XR Tools left-stick movement with bounded speed and strafing.
- **Snap turn:** XR Tools right-stick snap turning with a 30-degree step and debounce.
- **Teleport:** planned later profile; not part of the current lobby slice.
- **Climbing:** planned later profile; not part of the current lobby slice.
- **Gliding:** planned later profile.
- **Low traction:** planned later profile.
- **Wind:** planned later profile.

## Comfort and Performance

Every profile must expose comfort settings, define its interaction with other
profiles, and be tested in isolation before it is combined in a level. Movement
features are not considered complete until they pass desktop smoke testing and a
physical Quest 3S test.
