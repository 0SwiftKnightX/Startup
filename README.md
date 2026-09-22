# Startup

An experimental XR game project focused on creating responsive, comfortable, and
polished experiences for Meta Quest headsets.

## Project Status

Early development. The repository is currently being prepared as a Godot-based
XR project, with Meta Quest 3S as the first target device.

## Target Platform

- **Headset:** Meta Quest 3S
- **Stable Quest target:** 4.7.1
- **XR runtime:** OpenXR
- **Engine:** Godot 4.6+

## XR Stack

- [Godot XR Tools 4.5.1](https://github.com/GodotVR/godot-xr-tools/releases/tag/4.5.1)
	for locomotion, grabbing, climbing, interaction, haptics, and XR UI.
- [OpenXR Vendors 5.1.0-stable](https://github.com/GodotVR/godot_openxr_vendors/releases/tag/5.1.0-stable)
	for Android headset support and vendor-specific OpenXR extensions.
- [Godot XR Tools documentation](https://godotvr.github.io/godot-xr-tools/)
	for implementation guidance and reference scenes.

## Planned Mechanics

- Comfortable direct movement and teleportation
- Controller and hand-based interaction
- Physical grabbing and object manipulation
- Climbing and traversal systems
- Haptic feedback and spatial UI
- Quest-friendly performance and comfort settings

## Development Setup

1. Install Godot 4.6 or newer with Android export templates.
2. Install the OpenXR and OpenXR Vendors plugins for the selected Godot version.
3. Add Godot XR Tools 4.5.1 to the project.
4. Configure an Android export preset for Meta Quest.
5. Enable developer mode on the headset and deploy through Godot.

The project should be tested on physical Quest hardware regularly. PCVR preview
is useful during development, but it does not replace Quest testing for tracking,
performance, passthrough, or controller behavior.

## Repository Status

This README defines the initial technical direction. Project scenes, gameplay
systems, and export configuration will be added as development progresses.

## Update Record

- **Updated:** 2026-09-22T03:04:17Z
- **Signed:** GitHub Copilot
