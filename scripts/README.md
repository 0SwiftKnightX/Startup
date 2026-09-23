# Gameplay Scripts

This folder contains project-owned GDScript.

- `main.gd` controls menu navigation.
- `interaction_lab.gd` coordinates the first interaction flow.
- `hero_state.gd` owns lobby, soul, transformation, and arena state transitions.
- `scan_station.gd` owns scan acceptance and scan states.
- `arena_target.gd` owns target health and attack results.
- `xr_player.gd` reports XR runtime state and desktop fallback.
- `comfort_locomotion.gd` owns the initial movement and snap-turn profile.
- `game_state.gd` contains shared project state.

Scripts should consume named input actions and clear node contracts. Add a runtime test or verifier for each new system.
