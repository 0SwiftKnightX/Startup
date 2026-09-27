# Gameplay Scripts

This folder contains project-owned GDScript.

- `main.gd` controls lobby/menu navigation and keeps the world-space menu in a stable position.
- `interaction_lab.gd` coordinates the first interaction flow.
- `hero_state.gd` owns lobby, soul, transformation, and arena state transitions.
- `scan_station.gd` owns scan acceptance and scan states.
- `arena_target.gd` owns target health and attack results.
- `xr_player.gd` reports XR runtime state and keeps only the desktop fallback camera at eye height.
- `comfort_locomotion.gd` provides desktop fallback movement and snap turning; physical XR movement/turning is provided by XR Tools nodes in `xr_player.tscn`.
- `game_state.gd` contains shared project state.

Scripts should consume named input actions and clear node contracts. Do not duplicate XR Tools gravity, body movement, or controller locomotion in project-owned scripts.
