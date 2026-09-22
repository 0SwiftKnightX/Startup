# Project Bible

## Identity

**Startup** is an experimental Godot XR game project focused on comfortable,
responsive, and polished experiences for Meta Quest headsets.

## Current Direction

- Initial device target: Meta Quest 3S standalone.
- Runtime direction: OpenXR on Android.
- Engine direction: Godot 4.7.2-stable for the current validation baseline.
- Development phase: Godot foundation and integration planning.

These are project targets, not claims that the repository is already deployable
or validated on physical hardware.

## Product Principles

1. Comfort is a product requirement, not a late optimization.
2. Physical interaction should feel readable, predictable, and forgiving.
3. Device performance must be measured on Quest hardware.
4. Every important technical claim must have a source or verification record.
5. AI-assisted changes must remain reviewable, reversible, and attributable.

## Planned Experience

The initial mechanics direction includes locomotion, teleportation, controller
and hand interaction, grabbing, climbing, haptics, and spatial UI. The primary
core loop remains to be selected before production gameplay implementation.

The first implementation slice is a boot scene, main menu, and interaction lab.
The lab is a composition target for XR Tools interactions and locomotion profiles;
it does not yet claim OpenXR or Quest runtime support.

## Technology Direction

- [Godot XR Tools current master](https://github.com/GodotVR/godot-xr-tools/tree/master)
- [OpenXR Vendors 5.1.0-stable](https://github.com/GodotVR/godot_openxr_vendors/releases/tag/5.1.0-stable)
- [Godot XR Tools documentation](https://godotvr.github.io/godot-xr-tools/)

Version compatibility must be checked against the selected Godot editor before
implementation begins. Dependencies are not considered integrated until they are
installed and verified in the project.

The current local baseline is Godot 4.7.2-stable, XR Tools master, and OpenXR
Vendors 5.1.0-stable. The XR Tools master branch is used because its version
history includes the Godot 4.7 compatibility fixes not present in the 4.5.1
release package.

## Reference Repositories

The following repositories are the approved reference set for the initial XR
stack. They are documented references; they are not all project dependencies.

| Repository | Role in this project | Reference scope |
| --- | --- | --- |
| [GodotVR/godot-xr-template](https://github.com/GodotVR/godot-xr-template) | Initialization reference | Android and Meta Quest export presets, vendor loaders, main menu structure, and basic locomotion configuration. |
| [GodotVR/godot-xr-tools](https://github.com/GodotVR/godot-xr-tools) | Core mechanics reference | Physics hands, viewport UI interaction, grab and throw mechanics, and snap-turning. |
| [BastiaanOlij/godot-xr-flynn-demo](https://github.com/BastiaanOlij/godot-xr-flynn-demo) | Architecture reference | Multi-level management, performance-aware asset organization, and game-loop integration. |
| [Malcolmnixon/godot-xr-tools-demo](https://github.com/Malcolmnixon/godot-xr-tools-demo) | Locomotion reference | Gliding, low-traction surfaces, wind-assisted movement, and physics climbing. |

Reference code must be evaluated for license, version compatibility, performance,
and Quest 3S behavior before it is adopted.

## Scope Boundaries

This document records project intent and current direction. It does not replace
architecture decisions, test evidence, release notes, or AI worklogs.

## Open Decisions

- Select the primary gameplay interaction loop.
- Confirm the exact Godot editor version to lock for the first implementation.
- Confirm the final XR Tools and vendor plugin package versions for that editor.
- Define the first playable vertical slice.
