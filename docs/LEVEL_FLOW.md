# Level Flow

## Responsibility

The level-flow layer owns transitions, loading policy, and cleanup between the
Quest lobby, interaction lab, and future gameplay scenes. Individual levels must
not initialize the XR runtime or globally own application state.

## Initial Flow

Boot -> XR initialization -> Quest Lobby + Menu -> Interaction Lab -> Quest Lobby

The lobby world and menu UI are separate responsibilities:

- main.tscn owns the physical lobby space, player spawn area, lighting, floor,
  and menu surface.
- main_menu_panel.tscn owns the menu controls.
- interaction_lab.tscn owns the first gameplay/test interaction space.
- xr_player.tscn remains the single canonical XR player.

## Planned Expansion

Quest Lobby -> Tutorial -> Locomotion Lab -> Interaction Lab -> Gameplay Level

## Requirements

- One canonical XR initialization path.
- Explicit loading and failure states.
- No stale references to unloaded levels.
- Shared resources are cached deliberately and released when appropriate.
- Scene transitions remain testable without a headset.
- Physical Quest validation must verify the player can see, move through, and
  interact with the lobby before the interaction lab is treated as usable.
