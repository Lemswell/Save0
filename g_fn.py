def go_to_pos(x, y):
	x_start = get_pos_x()
	y_start = get_pos_y()
	if onwards_for_shortest(get_pos_x(), x):
		while get_pos_x() != x:
			move(East)
	else:
		while get_pos_x() != x:
			move(West)
	if onwards_for_shortest(get_pos_y(), y):
		while get_pos_y() != y:
			move(North)
	else:
		while get_pos_y() != y:
			move(South)

def better_till():
	if can_harvest():
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
		
def is_even(n):
	return n % 2

def wait_for_harvest():
	while not can_harvest():
		continue

def onwards_for_shortest(start, fin):
	if abs(start - fin) < get_world_size() :
		return True
	return False

def abs(n):
	if n < 0:
		return n*-1
	return n
	
def harvest_all_to_clear():
	go_to_pos(0,0)
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			harvest()
			move(North)
		move(East)