extends Node

const INTERACTION_LAB_SCENE := "res://scenes/interaction_lab.tscn"

@onready var menu_surface: XRToolsViewport2DIn3D = $PlayerRig/MenuSurface

func _ready() -> void:
	var menu_panel := menu_surface.get_scene_instance()
	while menu_panel == null:
		await get_tree().process_frame
		menu_panel = menu_surface.get_scene_instance()
	menu_panel.connect("launch_requested", _open_interaction_lab)
	menu_panel.connect("quit_requested", _quit_project)
	menu_panel.connect("arm_swing_toggled", _on_arm_swing_toggled)
	menu_panel.connect("smooth_turn_toggled", _on_smooth_turn_toggled)
	var openxr := XRServer.find_interface("OpenXR") as OpenXRInterface
	if not openxr or not openxr.is_initialized():
		menu_surface.position.z = 2.2
	$PlayerRig/LeftController.button_pressed.connect(_on_menu_controller_button_pressed)
	$PlayerRig/RightController.button_pressed.connect(_on_menu_controller_button_pressed)

func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("menu_confirm"):
		_open_interaction_lab()
	elif event.is_action_pressed("menu_cancel"):
		_quit_project()

func _open_interaction_lab() -> void:
	get_tree().change_scene_to_file(INTERACTION_LAB_SCENE)

func _quit_project() -> void:
	get_tree().quit()

func _on_menu_controller_button_pressed(button: String) -> void:
	if button == "ax_button":
		_open_interaction_lab()
	elif button == "by_button":
		_quit_project()

func _on_arm_swing_toggled(enabled: bool) -> void:
	$PlayerRig/MovementJog.enabled = enabled

func _on_smooth_turn_toggled(enabled: bool) -> void:
	XRToolsUserSettings.snap_turning = not enabled
