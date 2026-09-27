# Validation

## Validation Policy

Validation must report what was actually tested, with which version, on which
environment, and with what result. Static inspection, headless CI, PCVR preview,
and physical Quest testing are different evidence levels.

## Current Status

| Area | Status | Evidence |
|---|---|---|
| Godot project import | Passed | Godot 4.7.2-stable headless editor import, 2026-09-27 |
| Automated verifier suite | Passed | python3 tools/verify/run_all.py: 12 passed, 0 failed, 2026-09-27 |
| First-slice fallback runtime | Passed | Headless test covers soul selection, scan, transform, off-target rejection, aimed hits, defeat, and reset |
| OpenXR project configuration | Configured | project.godot enables OpenXR and references openxr_action_map.tres |
| Desktop OpenXR preview | Not run | Desktop OpenXR is a fallback/development surface, not product acceptance |
| Android export configuration | Configured | ARM64 Android/OpenXR Quest 3S preset exists |
| GitHub Actions APK build | Needs fresh run | Run 36226832612 failed because the CI image lacked Python; the workflow now installs Python and requires a successful rerun |
| Local Android export | Blocked in audit workspace | ANDROID_HOME, adb, and sdkmanager are absent in this audit environment |
| Physical Meta Quest 3S exploratory run | Observed, not accepted | User loaded Startup on Quest 3S; tracked hands and controller buttons worked, but the lobby/menu was extremely dark or not visible and there was no usable player area |
| Physical Quest 3S acceptance | Open | Locomotion, menu interaction, scene transition, pickup, scan, attack, comfort, frame time, thermal behavior, and lifecycle still require verification |
| Release readiness | Not certified | Quest acceptance and APK evidence remain incomplete |

## Required Evidence

Every validation entry should include:

- UTC timestamp
- Git commit or working-tree state
- Godot editor and export template version
- Device and runtime, when applicable
- Exact command or manual test performed
- Result and any known limitations

## Interpretation Rules

- A passing parser check does not prove runtime behavior.
- A passing headless check does not prove headset tracking or comfort.
- PCVR behavior does not certify Quest standalone performance.
- A checklist is not evidence until its steps have been executed.
- Do not describe the project as Quest-validated until physical Quest 3S
  testing has passed and been recorded.

## Current Repair Gate

The next physical validation pass should specifically verify:

1. The lobby is visible and adequately lit.
2. The player starts on the lobby floor at a usable eye height.
3. Left-stick movement works and respects collisions.
4. Right-stick snap turn works; smooth turn can be enabled from the menu.
5. The world-space menu is visible and pointer/hand interaction works.
6. Menu launch enters the interaction lab.
7. The interaction lab floor, lighting, pickup, scan, and target are usable.
8. Returning to the lobby clears stale gameplay state.

Only after those checks pass should the project move to broader gameplay systems.
