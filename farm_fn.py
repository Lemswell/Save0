import setup_fn
import g_fn

def wcg_farm(x_from, x_to, y_from, y_to):
	g_fn.go_to_pos(x_from, y_from)
	
	for i in range(x_from, x_to):
		for y in range(y_from, y_to):
			if can_harvest(): 
				harvest()
			elif get_entity_type() != None:
				se_item(Items.Water)
				while not can_harvest():
					continue
				harvest()
			if get_ground_type() == Grounds.Soil:
				plant(Entities.Carrot)
			if g_fn.is_even(get_pos_y() + get_pos_x()):
				plant(Entities.Tree)
			move(North)
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
		move(East)
		