extends Node

const INTERACTION_LAB := preload("res://scenes/interaction_lab.tscn")

func _ready() -> void:
	var failures: Array[String] = []
	var lab := INTERACTION_LAB.instantiate()
	add_child(lab)
	await get_tree().physics_frame
	await get_tree().physics_frame

	var pointer: RayCast3D = lab.get_node("Pointer")
	var soul: XRToolsPickable = lab.get_node("SoulBlock")
	var hero_state: HeroState = lab.get_node("HeroState")
	var station: ScanStation = lab.get_node("ScanStation")
	var target: ArenaTarget = lab.get_node("ArenaTarget")
	pointer.force_raycast_update()
	_check(pointer.get_collider() == soul, "fallback ray selects soul", failures)

	lab.call("_toggle_soul_grab")
	await get_tree().physics_frame
	await get_tree().physics_frame
	lab.call("_confirm_interaction")
	_check(hero_state.current_state == HeroState.ARENA, "scan transforms and enters arena", failures)
	_check(station.state == ScanStation.COMPLETE, "arena entered after a valid scan", failures)
	_check(not soul.visible, "soul is hidden after transformation", failures)

	pointer.force_raycast_update()
	_check(pointer.get_collider() == target, "fallback ray selects target", failures)
	pointer.target_position = Vector3(8.0, 0.0, -8.0)
	pointer.force_raycast_update()
	lab.call("_confirm_interaction")
	_check(target.health == 3, "attack misses when target is not aimed at", failures)

	pointer.target_position = Vector3(0.0, 0.0, -8.0)
	pointer.force_raycast_update()
	lab.call("_confirm_interaction")
	_check(target.health == 2, "aimed attack damages target", failures)
	lab.call("_confirm_interaction")
	lab.call("_confirm_interaction")
	_check(hero_state.current_state == HeroState.LOBBY, "defeating target returns to lobby", failures)
	_check(target.health == target.max_health, "arena target resets for next loop", failures)
	_check(station.state == ScanStation.READY, "scan station resets for next loop", failures)

	if failures.is_empty():
		print("RUNTIME_PASS Quest first-slice fallback loop")
		lab.queue_free()
		await get_tree().process_frame
		get_tree().quit(0)
		return

	for failure in failures:
		push_error("RUNTIME_FAIL " + failure)
	lab.queue_free()
	await get_tree().process_frame
	get_tree().quit(1)

func _check(condition: bool, description: String, failures: Array[String]) -> void:
	if not condition:
		failures.append(description)
