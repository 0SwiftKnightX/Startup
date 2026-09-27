extends Control

signal launch_requested
signal quit_requested
signal arm_swing_toggled(enabled: bool)
signal smooth_turn_toggled(enabled: bool)

@onready var launch_button: Button = $Panel/Content/LaunchButton
@onready var quit_button: Button = $Panel/Content/QuitButton
@onready var arm_swing_toggle: CheckBox = $Panel/Content/ArmSwingToggle
@onready var smooth_turn_toggle: CheckBox = $Panel/Content/SmoothTurnToggle

func _ready() -> void:
	launch_button.pressed.connect(func() -> void: launch_requested.emit())
	quit_button.pressed.connect(func() -> void: quit_requested.emit())
	arm_swing_toggle.toggled.connect(func(enabled: bool) -> void: arm_swing_toggled.emit(enabled))
	smooth_turn_toggle.toggled.connect(func(enabled: bool) -> void: smooth_turn_toggled.emit(enabled))
	smooth_turn_toggle.toggled.connect(func(enabled: bool) -> void: smooth_turn_toggled.emit(enabled))
