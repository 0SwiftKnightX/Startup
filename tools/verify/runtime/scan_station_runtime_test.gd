extends Node

@onready var scan_station: ScanStation = $ScanStation
@onready var soul: XRToolsPickable = $Soul
@onready var invalid_target: StaticBody3D = $InvalidTarget

func _ready() -> void:
	var failures: Array[String] = []
	await get_tree().physics_frame
	await get_tree().physics_frame

	_check(not scan_station.scan(invalid_target), "non-soul target is rejected", failures)
	_check(scan_station.state == ScanStation.REJECTED, "rejected scan state is visible", failures)

	soul.global_position = Vector3(0.0, 0.0, -0.2)
	await get_tree().physics_frame
	await get_tree().physics_frame
	_check(scan_station.interaction_area.get_overlapping_bodies().has(soul), "soul overlaps scan area", failures)
	_check(scan_station.scan(soul), "valid soul scan succeeds", failures)
	_check(scan_station.state == ScanStation.COMPLETE, "valid scan completes", failures)
	_check(scan_station.scanned_object == soul, "scan records the soul", failures)
	_check(not scan_station.scan(soul), "duplicate scan is rejected", failures)

	scan_station.reset()
	_check(scan_station.state == ScanStation.READY, "station reset returns to ready", failures)
	_check(scan_station.scanned_object == null, "station reset clears scanned object", failures)

	if failures.is_empty():
		print("RUNTIME_PASS ScanStation contract")
		get_tree().quit(0)
		return

	for failure in failures:
		push_error("RUNTIME_FAIL " + failure)
	get_tree().quit(1)

func _check(condition: bool, description: String, failures: Array[String]) -> void:
	if not condition:
		failures.append(description)
