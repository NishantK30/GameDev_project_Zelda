from support import *
level_0 = {'node_pos':(110,400), 'node_graphics':'./graphics/overworld/0', 'unlock':1}
level_1 = {'node_pos':(300,220), 'node_graphics':'./graphics/overworld/1', 'unlock':2}
level_2 = {'node_pos':(480,610), 'node_graphics':'./graphics/overworld/2', 'unlock':3}
level_3 = {'node_pos':(610,350), 'node_graphics':'./graphics/overworld/3', 'unlock':4}
level_4 = {'node_pos':(880,210), 'node_graphics':'./graphics/overworld/4', 'unlock':5}
level_5 = {'node_pos':(1050,400),'node_graphics':'./graphics/overworld/5', 'unlock':5}

levels = {
	0: level_0,
	1: level_1,
	2: level_2,
	3: level_3,
	4: level_4,
	5: level_5}

print(levels[0]['node_graphics'])









