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

@onready var interaction_area: Area3D = $InteractionArea
@onready var station_visual: MeshInstance3D = $Mesh

func _ready() -> void:
	_set_visual_color(Color(0.1, 0.45, 0.95))

func scan(target: Node3D) -> bool:
	if state == REJECTED:
		state = READY
	if state != READY or not _is_valid_target(target):
		state = REJECTED
		_set_visual_color(Color(0.95, 0.2, 0.15))
		scan_rejected.emit()
		return false
	state = SCANNING
	_set_visual_color(Color(0.95, 0.75, 0.15))
	scanned_object = target
	scan_started.emit()
	state = COMPLETE
	_set_visual_color(Color(0.15, 0.9, 0.4))
	scan_completed.emit()
	return true

func reset() -> void:
	state = READY
	scanned_object = null
	_set_visual_color(Color(0.1, 0.45, 0.95))

func _is_valid_target(target: Node3D) -> bool:
	return (
		target is XRToolsPickable
		and target.is_in_group("scannable_soul")
		and interaction_area.get_overlapping_bodies().has(target)
	)

func _set_visual_color(color: Color) -> void:
	if not is_instance_valid(station_visual):
		return
	var material := StandardMaterial3D.new()
	material.albedo_color = color
	material.emission_enabled = true
	material.emission = color
	material.emission_energy_multiplier = 0.35
	station_visual.material_override = material
