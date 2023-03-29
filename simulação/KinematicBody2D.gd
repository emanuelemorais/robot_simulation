extends KinematicBody2D

onready var tween = get_tree().create_tween()

func set_XY(pos):
	var target_rotation = (pos - global_position).angle() + PI / 2 #PI/2 = 90 graus de offset
	tween.tween_property(self, "rotation", target_rotation, 1) #tempo de rotação

func set_Z(size):
	var claw = get_node("garra")
	size = clamp(size, 0, 100)
	size = 1.0 + size/100.0
	#claw.scale = Vector2(size, size)
	tween.tween_property(claw, "scale", Vector2(size, size), 1) #tempo de rotação
	
func set_R(degrees):
	var claw = get_node("garra")
	#claw.rotation_degrees = degrees
	tween.tween_property(claw, "rotation_degrees", degrees, 1) #tempo de rotação

func _ready():
	var target_pos = Vector2(191, 338) # posição de destino do braço robótico
	set_XY(target_pos) # move o braço robótico
	set_R(45)
	set_Z(100)
	


