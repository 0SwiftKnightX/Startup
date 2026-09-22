extends Node

const INTERACTION_LAB_SCENE := "res://scenes/interaction_lab.tscn"

@onready var launch_button: Button = $MainMenu/Panel/Content/LaunchButton
@onready var quit_button: Button = $MainMenu/Panel/Content/QuitButton

func _ready() -> void:
	launch_button.pressed.connect(_open_interaction_lab)
	quit_button.pressed.connect(_quit_project)

func _open_interaction_lab() -> void:
	get_tree().change_scene_to_file(INTERACTION_LAB_SCENE)

func _quit_project() -> void:
	get_tree().quit()
