# Repository Audit

**Audit date:** 2026-09-27  
**Scope:** Godot XR project setup, first playable slice, verifier system, Android APK path, documentation, and known acceptance gaps.

## Current State

### XR project configuration

- `project.godot` enables Godot OpenXR and XR shaders.
- The project uses Godot's Mobile renderer, appropriate for standalone Quest XR.
- `openxr_action_map.tres` defines Quest Touch actions for trigger, grip, both thumbsticks, A/X, B/Y, controller poses, and haptics.
- `scenes/xr_player.tscn` composes one `XROrigin3D`, `XRCamera3D`, left/right `XRController3D`, low-poly tracked hands, `XRToolsPlayerBody`, direct movement, turn, optional arm-swing jog, pickup and pointer functions, and `StartXR`.
- `scenes/main.tscn` uses an XR Tools world-space viewport menu.
- The interaction lab includes ranged pickup, a scan area/state machine, a hero state flow, and an aim-gated target with health and feedback.

### Verified behavior

The current verification suite runs twelve checks, including:

- static scene, node, script, OpenXR, action-map, and controller contracts;
- runtime HeroState transitions;
- runtime scan overlap, soul filtering, duplicate rejection, and reset;
- end-to-end desktop-fallback soul selection, scan, transformation, off-target rejection, aimed target hits, and loop reset;
- a negative verifier test proving a missing required menu node is rejected with its source path.

Latest local validation on Godot 4.7.2:

```text
12 passed, 0 failed
Godot editor import passed
First-slice fallback runtime test passed
```

These results prove code-level and fallback behavior only. They do not prove headset tracking, Touch input, comfort, performance, or APK installation.

## OpenXR and Quest Gaps

- This workspace has no active desktop OpenXR runtime or connected headset. Godot reports that OpenXR cannot initialize, then runs the desktop fallback.
- No physical Quest 3S acceptance test has been performed.
- Controller tracking, pointer aim, ranged pickup, Grip/Trigger behavior, haptics, arm-swing, and snap/smooth turn still require headset testing.
- Quest frame timing, thermal behavior, comfort, and Android lifecycle behavior remain unmeasured.
- The transformed state has no production hero profile or transformed player presentation yet; it is a gameplay-state prototype.
- No multiplayer authority/networking, construction sandbox, enemy waves, production weapons, or production hero roster are implemented. These remain deliberately deferred until the single-player slice passes Quest acceptance.

## Android Build Path

- `export_presets.cfg` defines an ARM64 Android/OpenXR debug preset.
- `.github/workflows/android-quest3s-debug.yml` uses the published `barichello/godot-ci:4.7.2` image and builds/uploads a debug APK.
- The latest observed Actions run, `36226832612`, completed project import and failed at the verifier step because `python3` is absent from the container image.
- A local workflow fix now installs Python 3 with `apt-get` before running verifiers. That fix has not yet been pushed or confirmed by a successful GitHub Actions run.
- This local workspace has no `ANDROID_HOME`, `adb`, `sdkmanager`, or Godot Android export templates, so local APK export cannot be verified here.
- No successful APK artifact is currently evidenced by this audit. After the workflow fix is pushed, the Actions run and artifact must be checked.

## Documentation and Maintenance Notes

- `docs/IMPLEMENTATION_CHECKLIST.md` must distinguish implemented code from physical-device acceptance; checkboxes alone are not Quest evidence.
- Root README and project bible should describe the current prototype as configured and locally verified, not Quest validated or release ready.
- `tools/verify/` is the required gate for code changes. Every new verifier must be registered in `verifier_manifest.json`.
- Multiplayer and sandbox work should remain deferred until the first slice passes physical Quest testing.

## Recommended Next Actions

1. Push the Android workflow Python installation change and confirm a successful APK artifact.
2. Install the APK on Quest 3S and record boot, tracking, controller, menu, pickup, scan, attack, comfort, and performance results.
3. Fix any issues found on the device and rerun the verification suite.
4. Define a small hero profile and visible transform feedback after the current loop is accepted.
5. Only then begin multiplayer, sandbox, and enemy-wave architecture.
