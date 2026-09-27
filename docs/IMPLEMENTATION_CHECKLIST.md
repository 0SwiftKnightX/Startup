# Implementation Checklist

This checklist is the executable breakdown of [Next Implementation Plan](NEXT_IMPLEMENTATION_PLAN.md). A parent item is not complete until every child item and its acceptance check is complete.

## Milestone 1: Runtime Proof and Verification

### 1.1 Hero state runtime tests

- [x] Create a headless Godot test scene for `HeroState`.
- [x] Test the valid sequence: lobby -> soul selected -> soul scanned -> transformed -> arena.
- [x] Test invalid transitions are rejected.
- [x] Test `return_to_lobby()` resets the state.
- [x] Print a machine-readable pass/fail result.
- [x] Run this test from `tools/verify/run_all.py`.

**Done when:** state behavior is proven by executing GDScript, not only reading files.

### 1.2 Contract verification

- [x] Validate required scene node names.
- [x] Validate script attachments on required nodes.
- [x] Validate required input action names.
- [x] Validate required action bindings.
- [x] Validate verifier manifest coverage.
- [x] Include source path and contract name in failures.
- [x] Add a negative test proving a missing contract fails.

**Done when:** removing a required node, action, or verifier produces a clear failure.

## Milestone 2: XR Player Foundation

### 2.1 Canonical XR origin

- [x] Add one `XROrigin3D` to the gameplay rig.
- [x] Add one `XRCamera3D` under the origin.
- [x] Add one left `XRController3D`.
- [x] Add one right `XRController3D`.
- [x] Add tracked low-poly controller hands.
- [x] Confirm no second XR origin is created by another scene.
- [x] Add XR runtime status: active, unavailable, or desktop fallback.

**Done when:** the lab uses one rig and remains launchable without an XR runtime.

### 2.2 Named input contract

- [x] Add left-stick move action.
- [x] Add right-stick turn action.
- [x] Add left/right grip actions.
- [x] Add left/right trigger actions.
- [x] Add confirm actions for A/X context use.
- [x] Add cancel actions for B/Y context use.
- [x] Set stick dead zones.
- [x] Set grip and trigger thresholds.
- [x] Document action priority and permitted overlaps.
- [x] Verify gameplay scripts do not read raw controller buttons.

**Done when:** the first slice is driven through named actions with seated fallback.

## Milestone 3: Interaction Core

### 3.1 XR Tools pickup
 [x] Add a negative test proving a missing contract fails.
- [x] Replace the temporary soul node with `XRToolsPickable`.
- [x] Add `XRToolsFunctionPickup` to the controller rig.
 [x] Connect pickup and release signals.
 [x] Connect Trigger action while held.
 [x] Configure XR Tools throw velocity sampling.
 [x] Preserve desktop keyboard fallback.
- [x] Connect Trigger action while held.
- [x] Configure XR Tools throw velocity sampling.
 [x] Add pointer origin to each controller.
 [x] Add pointer direction from current controller pose.
 [x] Add valid-target collision layer.
 [x] Add visible target marker and laser feedback.
 [x] Use first-hit ray collision for obstruction handling.
 [x] Set an 8-meter pointer range.
 [x] Verify off-target attacks are rejected in the runtime slice test.
- [x] Add pointer direction from current controller pose.
- [x] Add valid-target collision layer.
 [x] Add haptic feedback after confirmed scan.
 [x] Add visual feedback after confirmed scan.
 [x] Add verifier coverage for valid and invalid scans.
- [x] Verify off-target attacks are rejected in the runtime slice test.

 [x] Add optional smooth turn.
 [x] Add collision-aware body movement through `XRToolsPlayerBody`.
### 3.3 Scan station

 [x] Sample controller velocity through the XR Tools jog provider.
 [x] Detect arm-stroke frequency through the XR Tools jog provider.
 [x] Filter incidental movement with the provider confidence threshold.
 [x] Convert detected strokes into player-body movement.
 [x] Configure bounded slow/fast movement speeds.
 [ ] Add fatigue limits.
 [x] Add enable/disable setting in the XR menu.
 [x] Preserve thumbstick fallback.
 [x] Add verifier coverage for the provider and menu setting.
- [x] Add visual feedback after confirmed scan.
- [x] Add verifier coverage for valid and invalid scans.
 [x] Lock transformation to the valid hero-state sequence.
 [x] Verify transformed-state transitions.
 [x] Reset the state after target defeat.

### 4.1 Comfort locomotion
 [x] Add one primary attack action.
 [x] Add Grip-swing attack intent.
 [x] Add charged Grip + Trigger action.
 [x] Add attack cooldown.
 [x] Add target visual/status hit feedback.
 [x] Add haptic attack feedback.
 [x] Add fallback runtime coverage for hit gating and damage/reset.
- [ ] Add comfort/vignette configuration.
- [ ] Add movement frame-time instrumentation.
 [x] Add one pointable target dummy.
 [x] Add health state.
 [x] Require aim at the target before applying damage.
 [x] Reject off-target attacks.
 [x] Add hit/defeat visual feedback.
 [x] Add reset behavior.
 [x] Add arena verifier.
 [x] Reset the loop after defeat; unloading to menu clears scene state.
- [x] Filter incidental movement through the provider's confidence threshold.
- [x] Convert detected strokes into player-body movement.
- [x] Configure slow/fast movement speed limits.
- [ ] Add fatigue limits.
- [x] Add enable/disable setting in the XR menu.
- [x] Preserve thumbstick fallback.
- [x] Add verifier coverage for the provider/menu wiring.

**Done when:** arm-swing movement is optional, controlled, and usable while seated fallback remains available.

## Milestone 5: Hero and Arena

### 5.1 Transformation

- [ ] Add one hero profile resource.
- [ ] Change visual state after transformation.
- [x] Lock transformation to the validated hero-state sequence.
- [x] Verify transformed-state transitions.
- [x] Reset the hero state and scene after target defeat.
- [ ] Add a production hero profile resource and transformed player presentation.

**Done when:** transformation visibly and deterministically changes the player state.

### 5.2 Hero action

- [x] Add one primary attack action.
- [x] Add Grip-swing attack intent.
- [x] Add charged Grip + Trigger attack.
- [x] Add attack cooldown.
- [x] Add target color/status hit feedback.
- [x] Add haptic attack feedback.
- [x] Add runtime test coverage for aim gating, damage, defeat, and reset.

**Done when:** attacks are unavailable before transformation and deterministic afterward.

### 5.3 Arena target

- [x] Add one pointable target dummy.
- [x] Add health state.
- [x] Require the XR pointer or desktop ray to target the dummy before damage.
- [x] Reject off-target attacks.
- [x] Add hit/defeat visual feedback.
- [x] Add reset behavior.
- [x] Add arena verifier.
- [x] Reset the loop after defeat; scene unloading clears it on menu return.

**Done when:** one complete transform-to-target interaction loop works.

## Milestone 6: Deferred Expansion

### 6.1 Multiplayer boundary

- [ ] Define authority for soul state.
- [ ] Define authority for hero state.
- [ ] Define authority for target state.
- [ ] Choose Godot networking approach.
- [ ] Replicate state rather than raw tracking noise.
- [ ] Handle connection failure.
- [ ] Handle disconnection.
- [ ] Add multiplayer verifier.

### 6.2 Q.U.I.R.K.-inspired sandbox

- [ ] Add one placeable block.
- [ ] Add placement validation.
- [ ] Add snap or grid rule.
- [ ] Add small arena save format.
- [ ] Add arena reload.
- [ ] Add one grappling-style tool only after the core slice passes.
- [ ] Profile Quest performance.
- [ ] Add sandbox verifier.

### 6.3 Cooperative enemy waves

- [ ] Add one enemy type.
- [ ] Define spawn ownership.
- [ ] Add enemy lifecycle.
- [ ] Add wave state.
- [ ] Add wave completion condition.
- [ ] Add reset behavior.
- [ ] Add enemy-wave verifier.

**Done when:** expansion systems are added only after the single-player slice and Quest acceptance pass.

## Evidence Gate

For every checked item, record:

- exact command or manual action;
- Godot version;
- environment or device;
- result;
- known limitation.

A parent milestone remains open until its children are checked and its `Done when` statement has fresh evidence.

## Acceptance Blockers

The code-level first-slice loop is implemented and covered by local runtime
tests, but these acceptance gates remain open:

- Push the Python installation step in `.github/workflows/android-quest3s-debug.yml` and confirm a successful APK artifact.
- Install and launch that APK on a physical Meta Quest 3S.
- Verify tracked poses, controller bindings, pointer targeting, near/ranged pickup, scan haptics, arm-swing comfort, smooth/snap turn, and attack feedback on-device.
- Record Quest frame-time, thermal, comfort, and lifecycle results.
- Add fatigue limits and production hero transformation visuals before treating the prototype slice as gameplay-complete.

Do not mark the first playable slice Quest-accepted until the device evidence is recorded in [Validation](VALIDATION.md).
