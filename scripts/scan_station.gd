class_name ScanStation
extends Node3D

signal scan_started
signal scan_completed
signal scan_rejected

const READY := "ready"
const SCANNING := "scanning"
const COMPLETE := "complete"
const REJECTED := "rejected"

var state := READY
var scanned_object: Node3D

func scan(target: Node3D) -> bool:
	if state != READY or target == null:
		state = REJECTED
		scan_rejected.emit()
		return false
	state = SCANNING
	scanned_object = target
	scan_started.emit()
	state = COMPLETE
	scan_completed.emit()
	return true

func reset() -> void:
	state = READY
	scanned_object = null
