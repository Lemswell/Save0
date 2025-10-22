import farm_fn, g_fn, setup_fn
clear()
setup_fn.till_checkered_defined(False, 4, 6, 0, get_world_size())
setup_fn.till_defined(6, get_world_size(), 0, get_world_size())
# setup_fn.till_rect(0, 0, get_world_size(), get_world_size())