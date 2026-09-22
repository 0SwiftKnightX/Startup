# Interaction Contracts

## Purpose

These contracts define the intended behavior of shared XR interaction systems
before implementation-specific nodes are added.

## Grab and Throw

- A grabbable object has one clear owner at a time.
- Grab begins only from a valid controller or hand interaction.
- Release preserves the object's physical state and applies throw velocity when
  supported.
- Failed grabs do not mutate ownership or leave partial state.

## Viewport UI

- UI interaction is isolated from world-object interaction layers.
- The active pointer has clear source, target, and activation state.
- UI remains legible and usable with both controller and hand input where
  supported.

## Physics Hands

- Hand visuals, collision representation, and input pose remain separable.
- Physics response must not create uncontrollable player motion.
- The system must degrade gracefully when hand tracking is unavailable.

## Snap Turn

- Rotation occurs around the configured player center.
- Repeated input is debounced according to the comfort profile.
- Snap-turn state does not interfere with teleport or climbing state.
