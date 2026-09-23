# Godot Addons

This folder contains third-party Godot XR integrations used by Startup.

- `godot-xr-tools/` provides reusable XR hands, pointers, pickup, locomotion, haptics, and UI components.
- `godotopenxrvendors/` provides vendor-specific OpenXR extensions for Android headset support.

Keep addon code separate from project-owned gameplay scripts. Configure and compose addons from `scenes/` and `scripts/`; do not fork addon internals for a local feature unless the change is deliberately documented and verified.
