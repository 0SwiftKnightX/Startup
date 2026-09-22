class_name ComfortLocomotion
extends Node

@export var move_speed := 2.0
@export var acceleration := 8.0
@export var snap_turn_degrees := 30.0
@export var snap_turn_cooldown := 0.25

var velocity := Vector3.ZERO
var _turn_timer := 0.0
var last_frame_time_usec := 0

@onready var origin: XROrigin3D = get_parent() as XROrigin3D

func _physics_process(delta: float) -> void:
	if origin == null:
		return
	last_frame_time_usec = Time.get_ticks_usec()
	var input_vector := Input.get_vector("xr_move_left", "xr_move_right", "xr_move_forward", "xr_move_back")
	var desired_velocity := Vector3(input_vector.x, 0.0, input_vector.y) * move_speed
	velocity = velocity.move_toward(desired_velocity, acceleration * delta)
	origin.position += origin.basis * velocity * delta
	_turn_timer = maxf(_turn_timer - delta, 0.0)
	if _turn_timer == 0.0:
		if Input.is_action_just_pressed("xr_turn_left"):
			origin.rotate_y(deg_to_rad(snap_turn_degrees))
			_turn_timer = snap_turn_cooldown
		elif Input.is_action_just_pressed("xr_turn_right"):
			origin.rotate_y(deg_to_rad(-snap_turn_degrees))
			_turn_timer = snap_turn_cooldown
