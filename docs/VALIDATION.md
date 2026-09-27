# Validation

## Validation Policy

Validation must report what was actually tested, with which version, on which
environment, and with what result. Static inspection, headless CI, PCVR preview,
and physical Quest testing are different evidence levels.

## Current Status

| Area | Status | Evidence |
|---|---|---|
| OpenXR project configuration | Configured, runtime unavailable | `project.godot` enables OpenXR/Mobile and references `openxr_action_map.tres`; this container has no active OpenXR runtime |
| Godot project import | Passed | Godot 4.7.2-stable headless editor import, 2026-09-27 |
| Automated verifier suite | Passed | `python3 tools/verify/run_all.py`: 12 passed, 0 failed, 2026-09-27 |
| First-slice fallback runtime | Passed | Headless test covers soul selection, scan, transform, off-target rejection, aimed hits, defeat, and reset |
| Desktop OpenXR preview | Not run | Requires a configured desktop OpenXR runtime and headset |
| Local Android export | Blocked | `ANDROID_HOME`, `adb`, `sdkmanager`, and Godot Android export templates are absent in this workspace |
| GitHub Actions APK build | Failed; workflow fix pending | Run `36226832612` imported successfully but failed because `python3` is missing in the container; workflow now installs Python, but that change has not been pushed/retested |
| Physical Meta Quest 3S acceptance | Not run | Requires successful APK artifact and headset deployment |
| Release readiness | Not certified | Quest, Android APK, comfort, and performance evidence are incomplete |

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
- Do not describe the project as Quest-validated until physical Quest 3S testing
  has passed and been recorded.

## Next Validation Milestone

Push the workflow's Python installation fix and confirm a successful Android
APK artifact. Then install that APK on Quest 3S and record boot, controller
tracking, pointer, ranged pickup, scan, transformation, aim-gated attacks,
comfort, and frame-time evidence here and in the audit archive.
