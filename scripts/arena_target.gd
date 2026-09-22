class_name ArenaTarget
extends Node3D

signal damaged(amount: int, remaining_health: int)
signal defeated

@export var max_health := 3
var health := 3

func _ready() -> void:
	health = max_health

func receive_attack(amount: int = 1) -> bool:
	if health <= 0 or amount <= 0:
		return false
	health = maxi(health - amount, 0)
	damaged.emit(amount, health)
	if health == 0:
		defeated.emit()
	return true

func reset() -> void:
	health = max_health
