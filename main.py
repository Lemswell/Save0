import farm_fn, g_fn, setup_fn
while True:
	farm_fn.wcg_farm(0,4,0,get_world_size())
	farm_fn.pumpkin_farm(4, get_world_size(), 0, get_world_size())