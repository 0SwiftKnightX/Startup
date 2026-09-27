# Scenes

This folder contains Godot scene composition.

- `main.tscn` is the Quest lobby scene and contains the separate world-space menu surface.
- `main_menu_panel.tscn` is the separate UI scene embedded into the lobby menu surface.
- `interaction_lab.tscn` is the first playable interaction scene.

- `xr_player.tscn` is the canonical XR origin, camera, controller, pointer, pickup, gravity/body, direct movement, snap/smooth turn, and optional arm-swing rig.

Scene ownership belongs here. Gameplay rules belong in `scripts/`, and reusable third-party nodes remain under `addons/`. Keep one canonical XR origin in the gameplay path.
