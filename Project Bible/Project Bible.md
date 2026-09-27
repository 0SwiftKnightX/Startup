# Project Bible

## Identity

**Startup** is an experimental Godot XR game project focused on comfortable,
responsive, and polished experiences for Meta Quest headsets.

## Current Direction

- Primary product target: Meta Quest 3S standalone.
- Runtime direction: OpenXR on Android.
- Engine direction: Godot 4.7.2-stable for the current validation baseline.
- Development phase: XR-first gameplay foundation, lobby repair, and Quest validation.
- Desktop behavior: developer fallback only, not a primary game loop.

These are project targets. An exploratory Quest 3S run has confirmed hands and
button input, but scene presentation, locomotion, interaction, and gameplay acceptance
are not yet complete on the device.

## Product Principles

1. Comfort is a product requirement, not a late optimization.
2. Physical interaction should feel readable, predictable, and forgiving.
3. Device performance must be measured on Quest hardware.
4. Every important technical claim must have a source or verification record.
5. AI-assisted changes must remain reviewable, reversible, and attributable.

## Planned Experience

The current prototype uses a dedicated lobby scene with a separate world-space XR
menu, tracked low-poly hands, thumbstick locomotion/turning, optional arm-swing
movement, ranged soul pickup, scan, hero-state transition, and a test target. This is a systems slice,
not a claim that production gameplay, comfort, or Quest runtime acceptance is
complete.

Teleportation, climbing, multiplayer, enemy waves, and sandbox construction
remain later features. Desktop controls exist only to exercise fallback logic
without an OpenXR runtime; they do not define product acceptance.

## Technology Direction

- Godot XR Tools
- OpenXR Vendors 5.1.0-stable
- Godot XR Tools documentation

Version compatibility must be checked against the selected Godot editor before
implementation begins. Dependencies are not considered integrated until they are
installed and verified in the project.

The current local baseline is Godot 4.7.2-stable, XR Tools master, and OpenXR
Vendors 5.1.0-stable. The XR Tools master branch is used because its version
history includes the Godot 4.7 compatibility fixes not present in the 4.5.1
release package.

## Reference Repositories

The approved initial XR reference set includes:

| Repository | Role | Reference scope |
| --- | --- | --- |
| GodotVR/godot-xr-template | Initialization | Android and Meta Quest export presets, vendor loaders, menu structure, and locomotion configuration. |
| GodotVR/godot-xr-tools | Core mechanics | Physics hands, viewport UI interaction, grabbing, throwing, and snap-turning. |
| BastiaanOlij/godot-xr-flynn-demo | Architecture | Multi-level management, performance-aware organization, and game-loop integration. |
| Malcolmnixon/godot-xr-tools-demo | Locomotion | Gliding, low-traction movement, wind-assisted movement, and physics climbing. |

Reference code must be evaluated for license, version compatibility, performance,
and Quest 3S behavior before adoption.

## Scope Boundaries

This document records project intent and governing direction. It does not replace
architecture decisions, validation evidence, release notes, AI worklogs, or individual
handoff records.

## Project Governance

The Project Bible and the Handoff system are associated but separate.

- **Project Bible:** governing project intent, principles, boundaries, and durable rules.
- **Handoff Template:** protocol for transferring project context between AI sessions.
- **Handoffs:** immutable historical records of individual handoff events.
- **Logs / audits / changelogs:** current and historical project activity and evidence.

The repository is the continuity source. Actual implementation and verification
evidence take precedence over remembered conversational state.

## Open Decisions

- Accept or revise the prototype interaction loop after Quest 3S testing.
- Lock the Android/Godot export toolchain after the first successful cloud APK.
- Define hero profiles and production presentation after the first target loop is accepted.
- Design multiplayer and sandbox systems only after the single-player Quest slice passes acceptance.
