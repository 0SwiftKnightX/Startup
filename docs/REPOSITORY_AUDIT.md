# Repository Audit

**Audit date:** 2026-09-27  
**Scope:** Godot XR project setup, Quest lobby, first playable slice, verifier system, Android APK path, documentation, and known acceptance gaps.

## Current State

### XR project configuration

- project.godot targets Godot 4.7.2 and enables OpenXR and XR shaders.
- The repository keeps the Quest renderer/export configuration documented in the
  project settings; the user's Quest runtime reports Compatibility/OpenGL ES 3.2
  on Qualcomm Adreno 740.
- openxr_action_map.tres defines Quest Touch actions for trigger, grip, both
  thumbsticks, A/X, B/Y, controller poses, and haptics.
- scenes/xr_player.tscn composes one XROrigin3D, XRCamera3D, left/right
  XRController3D, low-poly tracked hands, XRToolsPlayerBody, gravity/body
  physics, direct movement, right-stick turn, optional arm-swing jog, pickup,
  pointer functions, and StartXR.
- scenes/main.tscn is now a lit 3D Quest lobby with a floor, boundary wall,
  ambient/key/fill lighting, and a separate world-space menu scene.
- scenes/main_menu_panel.tscn remains the separate UI scene embedded by
  Viewport2Din3D.
- scenes/interaction_lab.tscn remains the separate gameplay/test scene with
  ranged pickup, scan state, hero state flow, and an aim-gated target.

### Verified behavior

The repository's automated verification suite has twelve checks covering static
scene/node/script/OpenXR/action-map contracts plus fallback runtime behavior.

Latest repository evidence:

12 passed, 0 failed
Godot 4.7.2 editor import passed
First-slice fallback runtime test passed

These results prove code-level and fallback behavior only.

### Physical Quest evidence

An exploratory Quest 3S run has now been observed by the user:

- tracked hands were visible and felt good;
- controller buttons responded;
- the lobby/menu presentation was extremely dark or not visible;
- there was no usable player area for normal interaction.

This is physical-device evidence, but it is not Quest acceptance evidence.

## Known gaps

- The repaired lobby requires a fresh APK/device pass to verify lighting and the
  world-space menu on the actual Quest 3S.
- Locomotion, gravity feel, floor collision, snap/smooth turn, pointer interaction,
  pickup, scan, scene transition, and attack feedback require physical validation.
- Quest frame timing, thermal behavior, comfort, and Android lifecycle behavior remain
  unmeasured.
- The transformed state has no production hero profile or transformed player
  presentation yet.
- Multiplayer, construction sandbox, enemy waves, production weapons, and production
  hero roster remain deliberately deferred.

## Android Build Path

- export_presets.cfg defines an ARM64 Android/OpenXR debug preset.
- .github/workflows/android-quest3s-debug.yml uses the published
  barichello/godot-ci:4.7.2 image and builds/uploads a debug APK.
- Actions run 36226832612 failed because python3 was absent; the workflow now
  installs Python and requires a fresh successful run.
- This audit environment has no ANDROID_HOME, adb, or sdkmanager, so local APK
  export cannot be verified here.
- No successful current APK artifact is evidenced by this audit.

## Maintenance Rules

- docs/IMPLEMENTATION_CHECKLIST.md must distinguish implemented code from
  physical-device acceptance.
- Root README and Project Bible should describe the prototype as configured and
  locally verified, not Quest accepted or release ready.
- tools/verify/ remains the required code-change gate.
- New systems should use existing XR Tools abstractions before custom replacements.
- Multiplayer and sandbox work remain deferred until the single-player Quest slice
  passes physical acceptance.

## Next Actions

1. Build/deploy the repaired lobby to Quest 3S.
2. Verify lobby visibility, floor placement, movement, turning, menu interaction,
   and transition to the interaction lab.
3. Verify pickup, scan, transformation, target attack, reset, and return to lobby.
4. Record frame-time, thermal, comfort, and lifecycle evidence.
5. Only then expand into production hero presentation, multiplayer, sandbox, and waves.
