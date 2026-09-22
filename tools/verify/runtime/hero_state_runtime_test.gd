extends Node

func _ready() -> void:
	var hero_state := HeroState.new()
	var failures: Array[String] = []

	_check(hero_state.current_state == HeroState.LOBBY, "initial state is lobby", failures)
	_check(not hero_state.scan_soul(), "scan is rejected before soul selection", failures)
	_check(hero_state.select_soul(), "soul selection succeeds", failures)
	_check(hero_state.current_state == HeroState.SOUL_SELECTED, "state becomes soul_selected", failures)
	_check(hero_state.scan_soul(), "soul scan succeeds", failures)
	_check(hero_state.current_state == HeroState.SOUL_SCANNED, "state becomes soul_scanned", failures)
	_check(hero_state.transform(), "transformation succeeds", failures)
	_check(hero_state.current_state == HeroState.TRANSFORMED, "state becomes transformed", failures)
	_check(hero_state.enter_arena(), "arena entry succeeds", failures)
	_check(hero_state.current_state == HeroState.ARENA, "state becomes arena", failures)
	_check(not hero_state.transform(), "transformation cannot repeat in arena", failures)
	_check(hero_state.return_to_lobby(), "return to lobby succeeds", failures)
	_check(hero_state.current_state == HeroState.LOBBY, "return resets to lobby", failures)

	if failures.is_empty():
		print("RUNTIME_PASS HeroState transitions")
		hero_state.free()
		get_tree().quit(0)
		return

	for failure in failures:
		push_error("RUNTIME_FAIL " + failure)
	hero_state.free()
	get_tree().quit(1)

func _check(condition: bool, description: String, failures: Array[String]) -> void:
	if not condition:
		failures.append(description)
