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

var soul_held := false

func _ready() -> void:
	hero_state.state_changed.connect(_on_state_changed)
	left_pickup.has_picked_up.connect(_on_xr_picked_up)
	right_pickup.has_picked_up.connect(_on_xr_picked_up)
	left_pickup.has_dropped.connect(_on_xr_dropped)
	right_pickup.has_dropped.connect(_on_xr_dropped)
	_update_status("Point at the soul block. Press G to grab, then Space to interact.")

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
		soul_block.position = Vector3(0, 1.1, -1.5)
		_update_status("Soul released. Point at it and press G to grab again.")
		return

	if pointer.is_colliding() and pointer.get_collider() == soul_block:
		soul_held = true
		soul_block.position = Vector3(0, 1.6, 0.2)
		hero_state.select_soul()
		_update_status("Soul selected. Press Space at the scanner to scan it.")
	else:
		_update_status("No valid soul target. Aim the pointer at the soul block.")

func _confirm_interaction() -> void:
	if hero_state.current_state == hero_state.ARENA:
		if arena_target.receive_attack():
			_update_status("Hero attack confirmed. Target health: %d" % arena_target.health)
		else:
			_update_status("Target is defeated or cannot receive another attack.")
		return

	if not soul_held:
		_update_status("Grab the soul before interacting.")
		return

	if hero_state.current_state == hero_state.SOUL_SELECTED and soul_block.global_position.distance_to(scan_station.global_position) < 1.5 and scan_station.scan(soul_block):
		hero_state.scan_soul()
		hero_state.transform()
		hero_state.enter_arena()
		soul_held = false
		soul_block.visible = false
		_update_status("Transformed. The first arena interaction is ready.")
	else:
		_update_status("Move the selected soul to the blue scanner before pressing Space.")

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

func _update_status(message: String) -> void:
	if status_label:
		status_label.text = message
