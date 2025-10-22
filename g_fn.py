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

def onwards_for_shortest(frm, to):
	if abs(frm - to) < get_world_size()/2:
		return True
	return False

def abs(n):
	if n < 0:
		return n*-1
	return n