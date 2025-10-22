import g_fn

def till_defined(x_from, x_to, y_from, y_to):
	g_fn.go_to_pos(x_from, y_from)
	
	for i in range(x_from, x_to):
		for y in range(y_from, y_to):
			g_fn.better_till()
			move(North)
		g_fn.go_to_pos(get_pos_x(), y_from)
		move(East)

def till_checkered_defined(even, x_from, x_to, y_from, y_to):
	g_fn.go_to_pos(x_from, y_from)
	
	for i in range(x_from, x_to):
		for y in range(y_from, y_to):
			if even == g_fn.is_even(get_pos_x() + get_pos_y()):
				g_fn.better_till()
			move(North)
		g_fn.go_to_pos(get_pos_x(), y_from)
		move(East) 
		
def till_rect(x_from, x_to, y_from, y_to):
	g_fn.go_to_pos(x_from, y_from)
	
	for i in range(x_from, x_to):
		g_fn.better_till()
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
	