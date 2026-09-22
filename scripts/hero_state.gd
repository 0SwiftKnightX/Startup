class_name HeroState
extends Node

signal state_changed(previous_state: String, current_state: String)

const LOBBY := "lobby"
const SOUL_SELECTED := "soul_selected"
const SOUL_SCANNED := "soul_scanned"
const TRANSFORMED := "transformed"
const ARENA := "arena"

var current_state := LOBBY

func select_soul() -> bool:
	return _transition_to(SOUL_SELECTED)

func scan_soul() -> bool:
	if current_state != SOUL_SELECTED:
		return false
	return _transition_to(SOUL_SCANNED)

func transform() -> bool:
	if current_state != SOUL_SCANNED:
		return false
	return _transition_to(TRANSFORMED)

func enter_arena() -> bool:
	if current_state != TRANSFORMED:
		return false
	return _transition_to(ARENA)

func return_to_lobby() -> bool:
	return _transition_to(LOBBY)

func _transition_to(next_state: String) -> bool:
	if current_state == next_state:
		return false
	var previous_state := current_state
	current_state = next_state
	state_changed.emit(previous_state, current_state)
	return true
