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
- [ ] Add a negative test proving a missing contract fails.

**Done when:** removing a required node, action, or verifier produces a clear failure.

## Milestone 2: XR Player Foundation

### 2.1 Canonical XR origin

- [x] Add one `XROrigin3D` to the gameplay rig.
- [x] Add one `XRCamera3D` under the origin.
- [x] Add one left `XRController3D`.
- [x] Add one right `XRController3D`.
- [x] Add controller pose visuals.
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

- [x] Replace the temporary soul node with `XRToolsPickable`.
- [x] Add `XRToolsFunctionPickup` to the controller rig.
- [x] Configure near-grab collision layers.
- [x] Configure ranged-grab collision layers.
- [x] Configure maximum ranged-grab distance.
- [ ] Connect pickup and release signals.
- [ ] Connect Trigger action while held.
- [ ] Verify throw velocity sampling.
- [ ] Preserve desktop keyboard fallback.

**Done when:** near pickup, remote pickup, hold, release, and throw work in the lab.

### 3.2 Ray pointer

- [ ] Add pointer origin to each controller.
- [ ] Add pointer direction from current controller pose.
- [ ] Add valid-target collision layer.
- [ ] Add target highlight state.
- [ ] Add obstruction handling.
- [ ] Add maximum pointer range.
- [ ] Verify the ray does not select invalid world geometry.

**Done when:** the player can aim at a remote valid object and receive immediate feedback.

### 3.3 Scan station

- [x] Add station collision target.
- [x] Accept only the selected soul.
- [x] Add ready state.
- [x] Add scanning state.
- [x] Add completed state.
- [x] Add rejected state.
- [x] Prevent duplicate scans.
- [ ] Add haptic feedback after confirmed scan.
- [ ] Add visual feedback after confirmed scan.
- [ ] Add verifier coverage for valid and invalid scans.

**Done when:** scanning is an explicit interaction contract rather than a distance shortcut.

## Milestone 4: Locomotion and Responsiveness

### 4.1 Comfort locomotion

- [x] Add left-stick movement.
- [x] Add dead-zone handling.
- [x] Add acceleration and deceleration limits.
- [x] Add right-stick snap turn.
- [ ] Add optional smooth turn.
- [ ] Add collision-aware body movement.
- [ ] Add comfort/vignette configuration.
- [ ] Add movement frame-time instrumentation.
- [ ] Verify no blocking work runs in the tracking path.

**Done when:** movement is predictable, comfortable, and does not visibly lag tracking.

### 4.2 Arm-swing profile

- [ ] Sample controller velocity.
- [ ] Detect a valid arm stroke.
- [ ] Reject accidental hand motion.
- [ ] Convert strokes into movement intent.
- [ ] Add speed and fatigue limits.
- [ ] Add enable/disable setting.
- [ ] Preserve thumbstick fallback.
- [ ] Add verifier coverage.

**Done when:** arm-swing movement is optional, controlled, and usable while seated fallback remains available.

## Milestone 5: Hero and Arena

### 5.1 Transformation

- [ ] Add one hero profile resource.
- [ ] Change visual state after transformation.
- [ ] Lock transformation to one successful scan.
- [ ] Add transformed-state verifier.
- [ ] Add reset behavior.

**Done when:** transformation visibly and deterministically changes the player state.

### 5.2 Hero action

- [ ] Add one primary attack action.
- [ ] Add Grip-driven attack intent.
- [ ] Add charged Grip + Trigger action.
- [ ] Add cooldown ownership.
- [ ] Add hit feedback.
- [ ] Add haptic feedback.
- [ ] Add runtime test coverage.

**Done when:** attacks are unavailable before transformation and deterministic afterward.

### 5.3 Arena target

- [ ] Add one target dummy.
- [ ] Add health state.
- [ ] Add valid hit detection.
- [ ] Add invalid-hit rejection.
- [ ] Add hit visual feedback.
- [ ] Add reset behavior.
- [ ] Add arena verifier.
- [ ] Verify return to menu clears arena state.

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
