class_name ArenaTarget
extends Node3D

signal damaged(amount: int, remaining_health: int)
signal defeated

@export var max_health := 3
var health := 3

func _ready() -> void:
	health = max_health
	_set_visual_color(Color(0.2, 0.75, 0.95))

func receive_attack(amount: int = 1) -> bool:
	if health <= 0 or amount <= 0:
		return false
	health = maxi(health - amount, 0)
	damaged.emit(amount, health)
	if health == 0:
		_set_visual_color(Color(0.45, 0.5, 0.55))
		defeated.emit()
	else:
		_set_visual_color(Color(0.95, 0.28, 0.12))
	return true

func reset() -> void:
	health = max_health
	_set_visual_color(Color(0.2, 0.75, 0.95))

func _set_visual_color(color: Color) -> void:
	var target_mesh := get_node_or_null("Mesh") as MeshInstance3D
	if not target_mesh:
		return
	var material := StandardMaterial3D.new()
	material.albedo_color = color
	material.emission_enabled = true
	material.emission = color
	target_mesh.material_override = material
