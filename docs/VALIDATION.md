# Validation

## Validation Policy

Validation must report what was actually tested, with which version, on which
environment, and with what result. Static inspection, headless CI, PCVR preview,
and physical Quest testing are different evidence levels.

## Current Status

| Area | Status | Evidence |
|---|---|---|
| Documentation structure | Complete | Repository files created 2026-09-22 |
| Godot project import | Passed | Godot 4.7.2-stable headless editor import |
| Headless XR validation | Partial | Project smoke test passed; no headset runtime was available |
| Android export templates | Installed | Godot 4.7.2-stable templates installed locally |
| Android SDK and ADB | Not installed | Container has no Android SDK, ADB, or `ANDROID_HOME` |
| PCVR preview | Not run | Requires a configured desktop OpenXR runtime |
| Physical Meta Quest 3S test | Not run | Requires a deployable Android build |
| Release readiness | Not certified | Implementation and device evidence are pending |

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

Configure a desktop OpenXR runtime, run the interaction lab, then deploy the
same scene to Quest 3S and record the results here and in the audit archive.
