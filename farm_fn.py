import setup_fn
import g_fn

def tcg_farm(x_from, x_to, y_from, y_to):
	g_fn.go_to_pos(x_from, y_from)
	
	for i in range(x_from, x_to):
		for y in range(y_from, y_to):
			if can_harvest(): 
				harvest()
			elif get_entity_type() != None and get_entity_type() != Entities.Dead_Pumpkin:
				use_item(Items.Water)
				while not can_harvest():
					continue
				harvest()
			if get_ground_type() == Grounds.Soil:
				plant(Entities.Carrot)
			if g_fn.is_even(get_pos_y() + get_pos_x()):
				plant(Entities.Tree)
			move(North)
		g_fn.go_to_pos(get_pos_x(), y_from)
		move(East) 
		

def pumpkin_farm(x_from, x_to, y_from, y_to):
	for i in range(x_from, x_to):
		for y in range(y_from, y_to):
			if can_harvest(): 
				harvest()
			elif get_entity_type() == None:
				# plant(Entities.Carrot) # ASSUMES SOIL
				pass
			else:
				use_item(Items.Water)
				is_dead = False
				while not can_harvest():
					if get_entity_type() == Entities.Dead_Pumpkin:
						is_dead = True
						break
					continue
				if not is_dead:
					harvest()
			plant(Entities.Pumpkin)
			move(North)
		g_fn.go_to_pos(get_pos_x(), y_from)
		move(East) 

def megapumpkin_farm_no_fert(x_from, x_to, y_from, y_to):
	g_fn.go_to_pos(x_from, y_from)
	x_loc = []
	y_loc = []

	for i in range(x_from, x_to):
		for y in range(y_from, y_to):
			if get_entity_type() == None:
				plant(Entities.Pumpkin)
			move(North)
		g_fn.go_to_pos(get_pos_x(), y_from)
		move(East)
	
	g_fn.go_to_pos(x_from, y_from)
	
	for i in range(x_from, x_to):
		for y in range(y_from, y_to):
			# wait func
			while not can_harvest():
				if get_entity_type() == Entities.Dead_Pumpkin:
					x_loc.append(get_pos_x())
					y_loc.append(get_pos_y())
					plant(Entities.Pumpkin)
					break
				use_item(Items.Water)
				continue
			move(North)
		g_fn.go_to_pos(get_pos_x(), y_from)
		move(East)

	g_fn.go_to_pos(x_from, y_from)

	while len(x_loc) > 0:
		mod = 0
		for i in range(len(x_loc)):
			g_fn.go_to_pos(x_loc[i - mod], y_loc[i - mod])
			# wait func
			bad = False
			while not can_harvest():
				if get_entity_type() == Entities.Dead_Pumpkin:
					bad = True
					plant(Entities.Pumpkin)
					break
				use_item(Items.Water)
				continue
			if not bad:
				x_loc.pop(i-mod)
				y_loc.pop(i-mod)
				mod = mod + 1
	harvest()