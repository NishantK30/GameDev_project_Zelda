from support import *

level_00 = {'boundary': import_csv_layout('./map/map_FloorBlocks.csv'),
              'grass': import_csv_layout('./map/map_Grass.csv'),
              'object': import_csv_layout('./map/map_Objects.csv'),
              'entities': import_csv_layout('./map/map_Entities.csv')}
        
        
        
level_01 = {
           'boundary': import_csv_layout('./map/map_FloorBlocks.csv'),
    'grass': import_csv_layout('./map/map_Grass.csv'),
    'object': import_csv_layout('./map/map_Objects.csv'),
    'entities': import_csv_layout('./map/map_Entities.csv')}

level_02 = {
    'boundary': import_csv_layout('./map/map_FloorBlocks.csv'),
    'grass': import_csv_layout('./map/map_Grass.csv'),
    'object': import_csv_layout('./map/map_Objects.csv'),
    'entities': import_csv_layout('./map/map_Entities.csv')}

level_03 = {'boundary': import_csv_layout('./map/map_FloorBlocks.csv'),
    'grass': import_csv_layout('./map/map_Grass.csv'),
    'object': import_csv_layout('./map/map_Objects.csv'),
    'entities': import_csv_layout('./map/map_Entities.csv')}

level_04 = {'boundary': import_csv_layout('./map/map_FloorBlocks.csv'),
    'grass': import_csv_layout('./map/map_Grass.csv'),
    'object': import_csv_layout('./map/map_Objects.csv'),
    'entities': import_csv_layout('./map/map_Entities.csv')}

level_05 = {'boundary': import_csv_layout('./map/map_FloorBlocks.csv'),
    'grass': import_csv_layout('./map/map_Grass.csv'),
    'object': import_csv_layout('./map/map_Objects.csv'),
    'entities': import_csv_layout('./map/map_Entities.csv')}

level_graphics = {
	0: level_00,
	1: level_01,
	2: level_02,
	3: level_03,
	4: level_04,
	5: level_05}

level_0 = {'node_pos':(100,400), 'node_graphics':'./graphics/overworld/0', 'unlock':1,'map':'./graphics/tilemap/ground.png'}
level_1 = {'node_pos':(250,220), 'node_graphics':'./graphics/overworld/1', 'unlock':2,'map':'./graphics/tilemap/ground.png'}
level_2 = {'node_pos':(460,530), 'node_graphics':'./graphics/overworld/2', 'unlock':3,'map':'./graphics/tilemap/ground.png'}
level_3 = {'node_pos':(620,350), 'node_graphics':'./graphics/overworld/3', 'unlock':4,'map':'./graphics/tilemap/ground.png'}
level_4 = {'node_pos':(880,210), 'node_graphics':'./graphics/overworld/4', 'unlock':5,'map':'./graphics/tilemap/ground.png'}
level_5 = {'node_pos':(940,400),'node_graphics':'./graphics/overworld/5', 'unlock':5, 'map':'./graphics/tilemap/ground.png'}
level_6 = {'node_pos':(560,180),'node_graphics':'./graphics/overworld/6', 'unlock':5, 'map':'./graphics/tilemap/ground.png'}


levels = {
	0: level_0,
	1: level_1,
	2: level_2,
	3: level_3,
	4: level_4,
	5: level_5,
    6: level_6}

maps =['./graphics/tilemap/ground.png','./graphics/tilemap/map.png','./graphics/tilemap/ground.png','./graphics/tilemap/ground.png','./graphics/tilemap/ground.png']
music =['./audio/level1.mp3','./audio/level1.mp3','./audio/level1.mp3','./audio/level1.mp3','./audio/level1.mp3']





