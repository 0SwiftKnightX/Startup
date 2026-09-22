extends Node

var active_level_id := "interaction_lab"
var xr_runtime_ready := false
var device_validation_status := "pending"

func set_xr_runtime_ready(ready: bool) -> void:
	xr_runtime_ready = ready
