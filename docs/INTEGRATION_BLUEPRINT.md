# XR Integration Blueprint

This document defines how the four reference repositories combine without
merging unrelated project ownership or copying entire demo projects.

## Composition Plan

| Capability | Reference | Integration boundary |
| --- | --- | --- |
| Project boot and Android export | [Godot XR Template](https://github.com/GodotVR/godot-xr-template) | Platform configuration and startup flow |
| Hands, UI, grabbing, throwing, snap turn | [Godot XR Tools](https://github.com/GodotVR/godot-xr-tools) | XR foundation and reusable interaction components |
| Multi-level flow and asset organization | [Flynn demo](https://github.com/BastiaanOlij/godot-xr-flynn-demo) | Scene lifecycle, resource loading, and performance patterns |
| Gliding, ice, wind, climbing | [Malcolm Nixon demo](https://github.com/Malcolmnixon/godot-xr-tools-demo) | Locomotion profiles and isolated movement test scenes |

## Integration Rules

1. Use one project boot path and one XR origin; do not initialize OpenXR from
   multiple demos.
2. Use Godot XR Tools components as the canonical interaction primitives.
3. Adapt locomotion recipes behind a shared locomotion profile interface.
4. Keep level transitions and asset loading in the game-flow layer.
5. Keep demo-specific test maps separate from production gameplay scenes.
6. Profile each combined mechanic on Quest 3S before enabling it by default.
7. Preserve licenses and attribution for every reused asset or code sample.

## First Vertical Slice

The initial slice should prove, in order:

1. Boot into the main menu.
2. Enter one interaction lab scene.
3. Initialize OpenXR through one canonical path.
4. Grab and throw a test object.
5. Use viewport UI and snap turn.
6. Return to the menu without stale scene state.

Gliding, low-traction surfaces, wind, climbing, multi-level streaming, and
performance optimization follow after the foundation passes desktop and Quest
smoke tests.
