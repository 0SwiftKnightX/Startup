# Startup Project: From-Zero Setup Prompt

Copy the prompt below into a coding agent when starting or resuming this project.

---

You are working on the Godot XR project named Startup.

## Product Direction

Startup is a responsive, comfortable XR action game for Meta Quest 3S. The design direction is inspired by the verified public behavior documented for HERO x HERO and the construction/tool-oriented multiplayer ideas documented for Q.U.I.R.K., but do not copy either project wholesale or claim unverified mechanics as facts.

The first playable slice must establish a low-latency interaction foundation:

1. Boot into a main menu.
2. Enter one interaction lab.
3. Use one canonical XR origin.
4. Track headset and both controllers.
5. Aim a pointer/raycast at a target.
6. Grab a soul object with Grip, including ranged pickup through XR Tools.
7. Use Trigger while holding it.
8. Scan the soul at a station.
9. Transform into one hero state.
10. Enter a simple arena.
11. Attack one target dummy.
12. Return to the menu without stale state.

Do not add multiplayer, a complete hero roster, construction tools, enemy waves, or a full content system until this single-player slice is proven.

## Hardware and Development Constraints

The target device is Meta Quest 3S. The project is Godot 4.7.2-stable in the current environment, uses OpenXR, Godot XR Tools, and OpenXR Vendors.

The Product Owner may have only:

- a Meta Quest 3S;
- an Android phone;
- internet access;
- a browser-based cloud workspace.

Do not assume the Product Owner owns a PC. A cloud workspace, GitHub Actions build, borrowed computer, or remote computer may be used for building. The Android phone can enable Quest Developer Mode, download an APK, and sideload it, but it cannot replace Quest OpenXR hardware validation.

Distinguish these evidence levels:

- Python/static verification: project structure and contracts.
- Godot headless verification: GDScript execution and scene loading.
- Android phone smoke test: APK installation and non-XR fallback behavior.
- Desktop OpenXR: optional PCVR preview.
- Physical Quest 3S: required for tracking, controllers, comfort, latency, performance, and final XR acceptance.

Never describe a desktop, phone, or headless pass as Quest validation.

## Repository Structure

The main project files are:

- `project.godot` - Godot project configuration.
- `scenes/main.tscn` - main menu.
- `scenes/interaction_lab.tscn` - first interaction scene.
- `scenes/xr_player.tscn` - canonical XR origin, camera, controllers, pickup functions, and pointer components.
- `scripts/main.gd` - menu flow.
- `scripts/interaction_lab.gd` - interaction lab flow.
- `scripts/hero_state.gd` - lobby, soul, scan, transform, and arena states.
- `scripts/scan_station.gd` - scan station contract.
- `scripts/arena_target.gd` - target health and attack contract.
- `scripts/xr_player.gd` - XR runtime status and fallback.
- `scripts/comfort_locomotion.gd` - movement and snap-turn profile.
- `addons/godot-xr-tools/` - existing XR Tools integration.
- `tools/verify/run_all.py` - shared verification runner.
- `tools/verify/verifier_manifest.json` - required verifier registry.
- `tools/verify/verifiers/` - static and runtime verifiers.
- `tools/verify/runtime/` - headless Godot runtime tests.
- `docs/FIRST_SLICE_ARCHITECTURE.md` - system ownership and update rules.
- `docs/NEXT_IMPLEMENTATION_PLAN.md` - milestone plan.
- `docs/IMPLEMENTATION_CHECKLIST.md` - granular sub-tasks and acceptance gates.

Read the relevant local docs before editing. Do not rewrite unrelated work or revert user changes.

## Required Control Model

Use named Godot input actions. Do not scatter raw device checks through gameplay scripts.

Quest controls available to the design:

- left thumbstick: movement;
- right thumbstick: turning or camera rotation;
- left trigger and right trigger: analog primary actions;
- left grip and right grip: grab/hold actions;
- A, B, X, Y: discrete context actions;
- controller poses: pointer direction, hand position, and motion;
- do not require capacitive thumb-contact sensing because it is not a guaranteed cross-runtime contract.

Recommended first-slice contracts:

- `xr_move_left`, `xr_move_right`, `xr_move_forward`, `xr_move_back`.
- `xr_turn_left`, `xr_turn_right`.
- `xr_left_grip`, `xr_right_grip`.
- `xr_left_trigger`, `xr_right_trigger`.
- `xr_confirm`, `xr_cancel`.

The project may provide keyboard fallbacks for development. Keyboard fallback does not replace Quest controller testing.

## Interaction and Update Rules

- XR tracking poses are the source of truth.
- Read current poses before pointer queries.
- Pointer rays use current controller poses.
- Physics owns rigid-body collision resolution.
- XR Tools owns pickup, ranged grab, release, and throw behavior.
- Gameplay owns state transitions, not device-specific nodes.
- UI and visual effects must not block the tracking/input path.
- Use thresholds and hysteresis for grip and trigger actions.
- Keep one XR origin and one canonical player rig.
- Define whether each system runs in frame, physics, or deferred scene-flow time.
- Do not claim that game code can run faster than hardware tracking; instead keep the response path free of stale poses and blocking work.

## Verified Reference Mechanics

The public HERO x HERO tutorial reports:

- arm-driven forward movement;
- thumbstick or physical turning;
- Grip pickup;
- Trigger transformation while holding a soul;
- Grip-based attack with hand waving;
- Grip + Trigger charged action;
- lobby, soul block, scanning, transformation, arena, and demon-wave flow;
- teamwork and hero-specific abilities.

The public Q.U.I.R.K. Steam page reports:

- multiplayer and cross-platform PC/macOS/HTC Vive support;
- cooperative AI and PvP;
- deathmatch, capture-the-flag, sandbox, and sportsball modes;
- colorful blocks and props;
- tools including jet packs, bazookas, stun guns, and a grappling plunger;
- user-generated-content direction.

Use these as design references only. The Startup first slice should implement the smallest testable subset: pointer, grab, scan, transform, one attack, and one target.

## Verifier Rules

Every new feature must add or update a verifier in `tools/verify/verifiers/` and add its class name to `tools/verify/verifier_manifest.json`.

The verifier must check real contracts:

- required files;
- required scene nodes;
- script attachments;
- input action names and bindings;
- signal wiring;
- state transitions;
- relevant resource settings.

When practical, add a headless Godot runtime test under `tools/verify/runtime/`. Static text checks do not prove runtime behavior.

The aggregate command is:

```bash
python3 tools/verify/run_all.py
```

Godot import check:

```bash
./.tools/godot --headless --path . --editor --quit
```

Main runtime smoke test:

```bash
./.tools/godot --headless --path . --quit-after 2
```

Interaction-lab smoke test:

```bash
./.tools/godot --headless --path . scenes/interaction_lab.tscn --quit-after 2
```

A successful static or headless run is not Quest acceptance.

## Android and Quest Setup Path Without a PC

The development build can be produced remotely:

1. Use the browser-based cloud workspace for editing.
2. Install or use Godot export templates in the build environment.
3. Add an Android export preset when the project is ready.
4. Configure Android SDK/ADB in the cloud builder or GitHub Actions.
5. Build a debug APK remotely.
6. Download the APK to the Android phone.
7. Enable Developer Mode in the Meta Horizon phone app.
8. Approve Quest USB debugging.
9. Sideload the APK with a compatible Android Quest installer such as SideQuest Android.
10. Launch and test it on the Quest.

A phone-only test can check APK installation, menu loading, and fallback behavior. Only the Quest can prove OpenXR tracking and controller behavior.

## Work Sequence

Follow this order:

1. Inspect current files and git status.
2. State one local hypothesis and one cheap check before the first edit.
3. Implement one narrow feature slice.
4. Add its verifier immediately.
5. Run the focused runtime or verifier test immediately.
6. Fix local failures before widening scope.
7. Run the aggregate verifier.
8. Run Godot headless import and relevant scene smoke test.
9. Record evidence and update `docs/IMPLEMENTATION_CHECKLIST.md`.
10. Only mark a parent task complete when all child tasks and evidence gates are complete.

## Current Remaining Work

The next implementation focus is:

1. Complete XR pickup behavior validation on a real OpenXR runtime.
2. Validate comfort locomotion on Quest 3S.
3. Add arm-swing locomotion as an optional profile using XR Tools patterns, without removing thumbstick fallback.
4. Add an Android export preset and cloud APK build workflow.
5. Add Quest deployment and acceptance documentation.
6. Only after the single-player slice passes, design multiplayer authority and Q.U.I.R.K.-inspired sandbox systems.

Do not mark hardware-dependent tasks complete merely because code parses or static verifiers pass.

## Communication Rules

Report:

- what changed;
- which files changed;
- exact validation commands;
- pass/fail output;
- limitations and missing hardware;
- the next smallest actionable task.

Do not claim completion without fresh verification evidence. Do not expose or request secrets in chat. Do not commit or create branches unless explicitly asked.

---
