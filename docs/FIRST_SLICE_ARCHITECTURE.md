# First Slice Architecture

## Purpose

The first playable slice establishes the responsive XR interaction loop before adding full multiplayer, hero rosters, or user-generated arenas. It combines the verified interaction ideas from HERO x HERO and Q.U.I.R.K. with the four existing XR reference repositories.

The slice must be playable on desktop first and remain compatible with the Quest 3S target. A Python verifier checks project contracts; Godot runtime checks prove that GDScript and scenes actually execute.

## Verified Reference Inputs

- HERO x HERO tutorial: arm-driven movement, thumbstick turning, Grip-based pickup and attack, Trigger-based transformation, charged Grip + Trigger action, soul selection, scanning, hero transformation, lobby-to-battle flow, and cooperative demon waves.
- Q.U.I.R.K. Steam page: multiplayer modes, cooperative AI and PvP, sandbox construction, colorful blocks and props, special tools including jet packs, bazookas, stun guns, and a grappling plunger, and HTC Vive support.
- Godot XR Template: project boot and Quest export conventions.
- Godot XR Tools: reusable XR hands, pointers, grabbing, haptics, and locomotion APIs.
- Flynn demo: scene lifecycle and asset organization.
- Malcolm Nixon demo: isolated locomotion experiments and traversal recipes.

These references inform behavior and boundaries. Their projects are not merged wholesale.

## Runtime Ownership

### XR Input Layer

Reads headset and controller state from Godot XR Tools/OpenXR and exposes named actions. Gameplay scripts must consume actions and poses, not raw device-specific checks.

Required action groups:

| Action | Default Quest input | Owner |
| --- | --- | --- |
| Move | Left thumbstick | Locomotion |
| Turn | Right thumbstick | Locomotion |
| Point | Controller pose and ray direction | Pointer |
| Grab | Grip, with threshold and hysteresis | Interaction |
| Primary | Trigger | Interaction / hero state |
| Cancel | B or Y | Flow / interaction cancellation |
| Confirm | A or X | UI / flow confirmation |
| Secondary | Unassigned until a feature needs it | Feature-specific |

A and X, and B and Y, are context actions. Thumb contact or capacitive side sensing is optional and must never be required because it is not a guaranteed contract across runtimes.

### Player Rig

Owns the XR origin, head, controller poses, hand poses, and sampled controller velocities. Tracking poses are read every frame. The rig does not own object physics, level transitions, or hero progression.

### Locomotion

Consumes Move and Turn actions plus the player rig. It applies comfort settings, snap-turn or smooth-turn policy, and collision-aware movement. Arm-swing locomotion may be a later profile; it must not replace a reliable thumbstick fallback for seated play.

### Pointer and Interaction

Each controller may own one pointer. The pointer ray is updated from the current controller pose and queries only interaction layers. A target is valid when it exposes the interaction contract and is within the configured range.

Grab flow:

1. Pointer identifies the nearest valid target.
2. Grip crosses its press threshold.
3. Interaction claims the target and records the owning hand.
4. While held, the target follows the hand through a defined hold constraint.
5. Release or cancellation returns ownership to physics.
6. Throw velocity comes from sampled hand motion, not a delayed animation.

A remote ray grab is an explicit feature and must define maximum range, obstruction behavior, target filtering, and release behavior before it is enabled.

### Hero State

Owns the progression state: lobby, soul-selected, scanned, transformed, battle, and returned. It requests interaction actions but does not directly move controllers or manipulate physics bodies.

First-slice state flow:

`Menu -> Interaction Lab -> Select Soul -> Scan -> Transform -> Test Arena -> Return`

### World and Physics

Godot physics owns collision and rigid-body integration. Interaction supplies target ownership and desired hand constraints; physics resolves the resulting motion. Visual effects and haptics react to confirmed state changes and must not block tracking or input.

## Update and Latency Rules

- Tracking poses are sampled before interaction queries each frame.
- Locomotion and pointer rays use the current sampled pose.
- Physics bodies are moved through physics-safe APIs in the physics step.
- Held-object visuals may follow the hand immediately, while collision resolution remains physics-owned.
- No blocking scene load, allocation-heavy effect, or network request may run in the tracking/input path.
- Input actions use press/release thresholds with hysteresis to prevent grip and trigger chatter.
- Every feature must define whether it runs in the frame loop, physics loop, or deferred scene-flow loop.
- The system must tolerate a missing XR runtime and expose a desktop fallback for development.

The goal is responsive correspondence with tracking, not an unsupported claim that game code can run faster than the headset's tracking source. Rendering and physics may have their own rates, but they must not fabricate stale poses or fight the XR runtime.

## First-Slice Features

1. Boot and main menu.
2. Desktop/XR player rig initialization.
3. Controller pose and pointer visualization.
4. One grabbable soul object.
5. Grip pickup and Trigger confirm/transform.
6. One scan station.
7. One transformed hero state.
8. One test arena with a target dummy.
9. Return-to-menu and state reset.
10. Haptic and visual feedback on confirmed interaction.

Remote ray grabbing, arm-swing movement, hero weapons, multiplayer networking, AI waves, construction blocks, and Q.U.I.R.K.-style tools follow only after this slice passes runtime and Quest checks.

## Verification Contract

Every feature adds one verifier under `tools/verify/verifiers/`. The verifier must check the feature's required files and wiring, not merely that a filename exists.

| Feature | Static verifier | Runtime proof |
| --- | --- | --- |
| Setup | Project and dependency checks | Godot project imports |
| Menu | Scene/script signal and transition checks | Menu opens and launches lab |
| XR rig | Input actions, origin, controller nodes | Headset/controller poses update |
| Pointer | Ray origin, collision layer, target contract | Ray selects a visible target |
| Grab | Grip action and ownership path | Object follows, releases, and throws |
| Hero flow | State transitions and reset path | Soul scans and transform completes |
| Arena | Scene references and target setup | Target interaction works |
| Performance | Asset and scene budget checks | Quest frame-time observation |

Run the static gate with:

```bash
python3 tools/verify/run_all.py
```

A static pass is necessary but not sufficient. Completion additionally requires a Godot runtime smoke test and, for XR behavior, physical Quest 3S acceptance evidence.
