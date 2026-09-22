# Next Implementation Plan

## Current Baseline

Completed and verified:

- Godot 4.7.2 project imports and launches headlessly.
- Main menu opens the interaction lab.
- First-slice architecture is documented.
- Shared Python verifier runner exists.
- Five verifiers currently pass.
- Hero state flow exists: lobby, soul selected, soul scanned, transformed, and arena.
- Desktop prototype supports raycast targeting, `G` grab/release, `Space` interaction, and `Esc` return.
- Godot XR Tools is available and already contains ranged pickup, grip/trigger actions, haptics, and throw velocity sampling.

This baseline is a prototype. It is not yet Quest-validated and does not yet contain a complete XR player rig.

## Priority 0: Correctness and Contracts

### 1. Add a runtime test harness

**Goal:** Prove the interaction lab transitions without relying only on static text checks.

Tasks:

- Add a headless Godot test scene or test script.
- Exercise the hero state transitions in order.
- Assert invalid transitions are rejected.
- Assert returning to the lobby resets the state.
- Make the runtime test return a non-zero process status on failure.

Acceptance:

- The test runs from the verification command.
- Valid transitions pass.
- Invalid transitions fail safely.
- Reset behavior is proven by runtime output.

### 2. Strengthen the feature verifier

**Goal:** Make verifiers check contracts rather than only file presence.

Tasks:

- Validate scene node names and script attachments.
- Validate input action names and expected bindings.
- Validate the interaction scene references the hero-state script.
- Report source file and contract name for each failure.
- Add a verifier manifest so expected verifiers cannot silently disappear.

Acceptance:

- Removing a required node or action causes a clear failure.
- Adding a feature without a verifier causes a clear failure once the manifest is enabled.

## Priority 1: XR Player Foundation

### 3. Compose the XR player rig

**Goal:** Replace the temporary camera path with one canonical XR origin.

Tasks:

- Add one `XROrigin3D`.
- Add `XRCamera3D`.
- Add left and right `XRController3D` nodes.
- Add controller pose visualization for desktop and XR modes.
- Keep the desktop camera fallback available when no XR runtime exists.
- Add a runtime status indicator for XR available, unavailable, or fallback.

Acceptance:

- No scene initializes a second XR origin.
- Desktop launch remains usable without an OpenXR runtime.
- Controller poses are available to pointer and interaction systems.

### 4. Define canonical input actions

**Goal:** Make every feature consume named actions instead of raw controller checks.

Tasks:

- Add left/right movement and turn actions.
- Add left/right grip and trigger actions.
- Add confirm/cancel actions for A/X and B/Y context mappings.
- Configure dead zones and grip/trigger thresholds.
- Document which actions may overlap and which have priority.

Acceptance:

- All first-slice systems use action names.
- No feature reads controller buttons directly outside the input layer.
- Seated fallback works with thumbstick movement and turning.

## Priority 2: Interaction Core

### 5. Replace the temporary desktop grab with XR Tools pickup

**Goal:** Use the existing XR Tools ownership, ranged-grab, and throw behavior.

Tasks:

- Use `XRToolsPickable` for the soul block.
- Add `XRToolsFunctionPickup` to the appropriate controller nodes.
- Configure ranged pickup distance and collision layers.
- Connect picked-up, released, and action signals to the hero-state flow.
- Preserve desktop keyboard simulation as a development fallback.

Acceptance:

- Nearby pickup works with Grip.
- Ranged pickup works through the configured ray.
- Trigger interaction works while the soul is held.
- Release and throw behavior are stable.
- Invalid targets cannot be picked up.

### 6. Add the scan station interaction contract

**Goal:** Make scanning an explicit interactable rather than a distance shortcut.

Tasks:

- Add a scan station collision target.
- Accept only the selected soul block.
- Provide visible ready, scanning, complete, and rejected states.
- Add haptic and visual feedback after confirmed scanning.
- Prevent duplicate scans and stale state.

Acceptance:

- The selected soul must be placed or aimed at the station.
- An unrelated object is rejected.
- A successful scan enables transformation exactly once.

## Priority 3: Locomotion and Responsiveness

### 7. Implement the comfort locomotion profile

**Goal:** Establish smooth, configurable movement before experimental movement modes.

Tasks:

- Left-stick movement with dead zone and acceleration limits.
- Right-stick snap turn as the default comfort option.
- Optional smooth turn setting.
- Collision-aware body movement.
- Vignette or comfort setting where appropriate.
- Frame-time instrumentation for movement and pointer updates.

Acceptance:

- Movement follows current tracking without visible catch-up.
- Turning is predictable while seated and standing.
- Comfort settings are accessible and persisted.
- No blocking work runs in the tracking path.

### 8. Add arm-swing locomotion as a separate profile

**Goal:** Reproduce the verified Hero x Hero-style arm-driven movement without making it mandatory.

Tasks:

- Sample controller velocity in the player rig.
- Detect alternating or qualifying arm strokes.
- Convert validated strokes into movement intent.
- Add fatigue, speed, and comfort limits.
- Keep thumbstick fallback available.

Acceptance:

- Arm-swing movement can be enabled or disabled.
- Accidental hand motion does not move the player unexpectedly.
- Seated players can use the fallback.

## Priority 4: Hero and Arena Slice

### 9. Add one transformed hero interaction

**Goal:** Prove the transformation state changes gameplay presentation and controls.

Tasks:

- Add one hero profile resource.
- Change avatar or hand visual state after transformation.
- Add one primary attack action.
- Add one charged Grip + Trigger action.
- Add cooldown and feedback ownership.

Acceptance:

- Transformation changes state once.
- Attack is unavailable before transformation.
- Charge and release produce deterministic feedback.
- All actions have verifier coverage.

### 10. Add one arena target

**Goal:** Prove the hero can interact with a world target.

Tasks:

- Add a target dummy with health and hit feedback.
- Use physics-safe hit detection.
- Add a simple enemy or wave placeholder only after the single target works.
- Keep visual effects bounded for Quest performance.

Acceptance:

- Target receives valid hits only.
- Damage and reset behavior are testable.
- The arena can return to the lobby without stale nodes or state.

## Priority 5: Multiplayer and Q.U.I.R.K.-Inspired Systems

These are deliberately deferred until the single-player interaction loop is proven.

### 11. Multiplayer boundary

- Define authoritative ownership for soul, hero, and target state.
- Choose a networking approach compatible with Godot and Quest.
- Replicate gameplay state, not raw controller noise.
- Add connection, disconnection, and host migration behavior.

### 12. Construction and tool sandbox

Q.U.I.R.K. provides a reference for user-built arenas, blocks, props, and special tools. Do not add all of these at once.

Implement in this order:

1. One placeable block.
2. One validated snap or placement rule.
3. Save/load for a small arena definition.
4. One tool such as a grappling plunger.
5. Multiplayer synchronization.
6. Additional tools only after performance profiling.

### 13. Cooperative enemy waves

- Define enemy lifecycle and spawn ownership.
- Add one enemy type.
- Add wave state and completion conditions.
- Add team-friendly hero roles only after single-player behavior is stable.

## Verification Matrix

Every item above must have both static and runtime evidence:

| Area | Static verifier | Runtime check | Quest evidence |
| --- | --- | --- | --- |
| Project setup | Required files, settings, plugins | Godot import and launch | Not applicable |
| XR rig | Origin, camera, controllers | Poses update | Tracking stability |
| Input | Actions and mappings | Press, release, analog values | Controller behavior |
| Pointer | Ray origin and layers | Target selection | Aim latency |
| Grab | Pickable and pickup wiring | Pickup, hold, release, throw | Hand feel |
| Scan | Station contract | Valid and invalid scans | Haptics and comfort |
| Locomotion | Profile configuration | Movement and turn | Comfort and frame time |
| Hero state | Transition graph | Transform and reset | Visual/physical response |
| Combat | Attack contract | Hit and charge behavior | Performance |
| Multiplayer | Authority contract | Join, sync, disconnect | Network behavior |
| Sandbox | Placement/save contract | Build and reload | Performance and stability |

## Definition of Done for the Next Milestone

The next milestone is complete only when:

- the XR player rig is present;
- named input actions drive the player;
- the soul uses XR Tools pickup behavior;
- the scan station validates the correct object;
- one hero transformation changes state and presentation;
- one arena target responds to a hero action;
- static verifiers and runtime tests pass;
- the interaction lab works without an XR runtime through fallback controls;
- Quest 3S acceptance evidence is recorded separately from desktop evidence.
