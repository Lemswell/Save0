import g_fn

def till_defined(x_from, x_to, y_from, y_to):
	g_fn.go_to_pos(x_from, y_from)
	
	for i in range(x_from, x_to):
		for y in range(y_from, y_to):
			g_fn.better_till()
			move(North)
		move(East)

def till_checkered_defined(even, x_from, x_to, y_from, y_to):
	g_fn.go_to_pos(x_from, y_from)
	
	for i in range(x_from, x_to):
		for y in range(y_from, y_to):
			if even == g_fn.is_even(get_pos_x() + get_pos_y()):
				g_fn.better_till()
			move(North)
		move(East)
			
def wcg_farm():
	while get_pos_x() in range(x_from, x_to):
		for i in range(get_world_size()):
			if can_harvest(): 
				harvest()
			else:
				use_item(Items.Water)
				while not can_harvest():
					continue
				harvest()
			if get_ground_type() == Grounds.Soil:
				plant(Entities.Carrot)
			if g_fn.is_even(get_pos_y() + get_pos_x()):
				plant(Entities.Tree)
			move(North)
		move(North)
		move(East)

def pumpkin_farm():
	while True:
		for i in range(get_world_size()):
			if can_harvest(): 
				harvest()
			else:
				use_item(Items.Water)
				while not can_harvest():
					continue
				harvest()
			if get_ground_type() == Grounds.Soil:
				plant(Entities.Carrot)
			if g_fn.is_even(get_pos_y() + get_pos_x()):
				plant(Entities.Tree)
			move(North)
		move(East)
