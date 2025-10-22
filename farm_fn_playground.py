import setup_fn
import g_fn

def wcg_farm(x_from, x_to):
	g_fn.go_to_pos(x_from, y_from)
	
	for i in range(x_from, x_to):
		for y in range(y_from, y_to):
			if can_harvest(): 
				harvest()
			else:
				if get_entity_type() == None:
					if get_ground_type() == Grounds.Soil:
						plant(Entities.Carrot)
				else:		
					while not can_harvest():
						use_item(Items.Water)
					harvest()
			if get_ground_type() == Grounds.Soil:
				plant(Entities.Carrot)
			if g_fn.is_even(get_pos_y() + get_pos_x()):
				plant(Entities.Tree)
			move(North)
		move(East)
		

def pumpkin_farm(x_from, x_to):
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
		