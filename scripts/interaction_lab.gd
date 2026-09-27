extends Node3D

const MAIN_MENU_SCENE := "res://scenes/main.tscn"

@onready var hero_state: HeroState = $HeroState
@onready var soul_block: Node3D = $SoulBlock
@onready var scan_station: ScanStation = $ScanStation
@onready var pointer: RayCast3D = $Pointer
@onready var status_label: Label = $Status
@onready var arena_target: ArenaTarget = $ArenaTarget
@onready var left_pickup: XRToolsFunctionPickup = $PlayerRig/LeftController/Pickup
@onready var right_pickup: XRToolsFunctionPickup = $PlayerRig/RightController/Pickup
@onready var left_controller: XRController3D = $PlayerRig/LeftController
@onready var right_controller: XRController3D = $PlayerRig/RightController
@onready var left_pointer: XRToolsFunctionPointer = $PlayerRig/LeftController/Pointer
@onready var right_pointer: XRToolsFunctionPointer = $PlayerRig/RightController/Pointer

var soul_held := false
var _last_left_hand_position := Vector3.ZERO
var _last_right_hand_position := Vector3.ZERO
var _has_left_hand_position := false
var _has_right_hand_position := false
var _attack_cooldown := 0.0

func _ready() -> void:
	if not soul_block.is_in_group("scannable_soul"):
		soul_block.add_to_group("scannable_soul")
	hero_state.state_changed.connect(_on_state_changed)
	left_pickup.has_picked_up.connect(_on_xr_picked_up)
	right_pickup.has_picked_up.connect(_on_xr_picked_up)
	left_pickup.has_dropped.connect(_on_xr_dropped)
	right_pickup.has_dropped.connect(_on_xr_dropped)
	soul_block.action_pressed.connect(_on_soul_action_pressed)
	left_controller.button_pressed.connect(_on_controller_button_pressed)
	right_controller.button_pressed.connect(_on_right_controller_button_pressed)
	_update_status("Point at the soul block. Press G to grab, then Space to interact.")

func _physics_process(delta: float) -> void:
	_attack_cooldown = maxf(_attack_cooldown - delta, 0.0)
	var left_speed := _sample_hand_speed(left_controller, delta, true)
	var right_speed := _sample_hand_speed(right_controller, delta, false)
	if hero_state.current_state != hero_state.ARENA or _attack_cooldown > 0.0:
		return
	if left_controller.get_float("grip") > 0.55 and left_speed > 1.2:
		_perform_attack(1, left_controller)
	elif right_controller.get_float("grip") > 0.55 and right_speed > 1.2:
		_perform_attack(1, right_controller)

func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("menu_cancel"):
		get_tree().change_scene_to_file(MAIN_MENU_SCENE)
	elif event.is_action_pressed("interact_grab"):
		_toggle_soul_grab()
	elif event.is_action_pressed("interact_primary"):
		_confirm_interaction()

func _toggle_soul_grab() -> void:
	if soul_held:
		soul_held = false
		soul_block.position = Vector3(0, 1.6, -1.5)
		_update_status("Soul released. Point at it and press G to grab again.")
		return

	if pointer.is_colliding() and pointer.get_collider() == soul_block:
		soul_held = true
		soul_block.global_position = scan_station.global_position
		hero_state.select_soul()
		_update_status("Soul selected. Press Space at the scanner to scan it.")
	else:
		_update_status("No valid soul target. Aim the pointer at the soul block.")

func _confirm_interaction() -> void:
	if hero_state.current_state == hero_state.ARENA:
		_perform_attack(1)
		return

	if not soul_held:
		_update_status("Grab the soul before interacting.")
		return

	if hero_state.current_state == hero_state.SOUL_SELECTED and scan_station.scan(soul_block):
		var held_controller := (soul_block as XRToolsPickable).get_picked_up_by_controller()
		if held_controller:
			_play_haptic(held_controller.tracker, 0.8, 220)
		hero_state.scan_soul()
		hero_state.transform()
		hero_state.enter_arena()
		_release_soul()
		soul_held = false
		soul_block.visible = false
		_update_status("Soul scanned. Transformed. Grip-swing at the target to attack.")
	else:
		_update_status("Move the selected soul to the blue scanner before pressing Space.")

func _complete_arena_loop() -> void:
	hero_state.return_to_lobby()
	arena_target.reset()
	scan_station.reset()
	soul_held = false
	soul_block.visible = true
	soul_block.position = Vector3(0, 1.6, -1.5)
	_update_status("Arena complete. Quest loop reset to lobby. Select the soul again.")

func _on_state_changed(_previous_state: String, current_state: String) -> void:
	print("Hero state: ", current_state)

func _on_xr_picked_up(what: Node3D) -> void:
	if what != soul_block:
		return
	soul_held = true
	hero_state.select_soul()
	_update_status("Soul selected through XR pickup. Press Trigger at the scanner to scan it.")

func _on_xr_dropped() -> void:
	if soul_held and hero_state.current_state == hero_state.SOUL_SELECTED:
		soul_held = false
		_update_status("Soul released. Point at it and press Grip to pick it up again.")

func _on_soul_action_pressed(_pickable: XRToolsPickable) -> void:
	_confirm_interaction()

func _on_right_controller_button_pressed(button: String) -> void:
	if button == "trigger_click" and hero_state.current_state == hero_state.ARENA:
		var damage := 2 if right_controller.get_float("grip") > 0.55 else 1
		_perform_attack(damage, right_controller)
	elif button == "by_button":
		get_tree().change_scene_to_file(MAIN_MENU_SCENE)
	elif button == "ax_button":
		_confirm_interaction()

func _on_controller_button_pressed(button: String) -> void:
	if button == "by_button":
		get_tree().change_scene_to_file(MAIN_MENU_SCENE)
	elif button == "ax_button":
		_confirm_interaction()

func _perform_attack(damage: int, controller: XRController3D = null) -> void:
	if not _is_targeted(controller):
		_update_status("Aim a controller pointer at the target before attacking.")
		return
	if arena_target.receive_attack(damage):
		_attack_cooldown = 0.35
		_play_haptic(right_controller.tracker, 0.45 if damage == 1 else 0.8, 100 if damage == 1 else 220)
		_update_status("Hero attack confirmed. Target health: %d" % arena_target.health)
		if arena_target.health == 0:
			_complete_arena_loop()
	else:
		_update_status("Target is defeated or cannot receive another attack.")

func _is_targeted(controller: XRController3D) -> bool:
	if controller == left_controller:
		return left_pointer.target == arena_target
	if controller == right_controller:
		return right_pointer.target == arena_target
	return pointer.is_colliding() and pointer.get_collider() == arena_target

func _sample_hand_speed(controller: XRController3D, delta: float, is_left: bool) -> float:
	if not controller.get_is_active():
		return 0.0
	var current_position := controller.position
	var previous_position := _last_left_hand_position if is_left else _last_right_hand_position
	var has_previous := _has_left_hand_position if is_left else _has_right_hand_position
	var speed := current_position.distance_to(previous_position) / maxf(delta, 0.0001) if has_previous else 0.0
	if is_left:
		_last_left_hand_position = current_position
		_has_left_hand_position = true
	else:
		_last_right_hand_position = current_position
		_has_right_hand_position = true
	return speed

func _release_soul() -> void:
	var pickable := soul_block as XRToolsPickable
	if not pickable or not pickable.is_picked_up():
		return
	var pickup := pickable.get_picked_up_by() as XRToolsFunctionPickup
	if pickup:
		pickup.drop_object()

func _play_haptic(tracker: StringName, magnitude: float, duration_ms: int) -> void:
	var event := XRToolsRumbleEvent.new()
	event.magnitude = magnitude
	event.duration_ms = duration_ms
	XRToolsRumbleManager.add("interaction_feedback", event, [tracker])

func _update_status(message: String) -> void:
	if status_label:
		status_label.text = message
