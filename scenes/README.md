# Scenes

This folder contains Godot scene composition.

- `main.tscn` is the boot menu.
- `interaction_lab.tscn` is the first playable interaction scene.
- `xr_player.tscn` is the canonical XR origin, camera, controller, pointer, pickup, and locomotion rig.

Scene ownership belongs here. Gameplay rules belong in `scripts/`, and reusable third-party nodes remain under `addons/`. Keep one canonical XR origin in the gameplay path.
