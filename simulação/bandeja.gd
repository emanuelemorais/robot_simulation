extends KinematicBody2D


var scale_factor = 1.1
func increase_size():
	scale *= scale_factor

func _input(event):
	if event is InputEventKey:
		if event.is_pressed():
			increase_size()
	if event is InputEventMouseButton:
		if event.is_pressed():
			increase_size()
			
