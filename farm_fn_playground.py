import setup_fn
import g_fn

# TODO: floor/ceil segment defs funcitions based on world size

# TODO: auto unlocks

# TODO: cacti corner/perim
	#
	
# TODO: Impl watering

def cacti_rect_farm(x_from, x_to, y_from, y_to):
	g_fn.go_to_pos(x_from, y_from)
	
	for i in range(x_from, x_to):
		g_fn.better_till()
		if get_entity_type == None:
			plant(Entities.Cactus)
		move(North)
	for i in range(y_from, y_to):
		g_fn.better_till()
		move(East)
	for i in range(x_from, x_to):
		g_fn.better_till()
		move(South)
	for i in range(y_from, y_to):
		g_fn.better_till()
		move(West)
	

# TODO: big pump field
		
def pumpkin_field_farm_no_fert(x_from, x_to, y_from, y_to):
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
				
# g_fn.harvest_all_to_clear()
# clear()
setup_fn.till_defined(0,8,0,8)
while True:
	pumpkin_field_farm_no_fert(0,8,0,8)