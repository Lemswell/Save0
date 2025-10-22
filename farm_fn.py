import g_fn

def wcg_farm():
	while True:
		for i in range(get_world_size()):
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
		move(North)
		move(East)