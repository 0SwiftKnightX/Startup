extends Node3D

const MAIN_MENU_SCENE := "res://scenes/main.tscn"

func _ready() -> void:
	print("Interaction Lab foundation loaded; XR plugin integration is pending.")

func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("menu_cancel"):
		get_tree().change_scene_to_file(MAIN_MENU_SCENE)
