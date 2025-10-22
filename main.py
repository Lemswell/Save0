import farm_fn, g_fn, setup_fn
while True:
	farm_fn.tcg_farm(0,6,0,get_world_size())
	farm_fn.pumpkin_farm(6, get_world_size(), 0, get_world_size())