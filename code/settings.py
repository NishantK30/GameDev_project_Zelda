# game setup
WIDTH    = 1080	
HEIGTH   = 620
FPS      = 60
TILESIZE = 64

HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'grass': -10,
	'invisible': 0}

#weapons
weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphic':'./graphics/weapons/sword/full.png'},
	'lance': {'cooldown': 400, 'damage': 30,'graphic':'./graphics/weapons/lance/full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic':'./graphics/weapons/axe/full.png'},
	'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'./graphics/weapons/rapier/full.png'},
	'sai':{'cooldown': 80, 'damage': 10, 'graphic':'./graphics/weapons/sai/full.png'}}

#ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = './graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# magic
magic_data = {
	'flame': {'strength': 10,'cost': 20,'graphic':'./graphics/particles/flame/fire.png'},
	'heal' : {'strength': 20,'cost': 10,'graphic':'./graphics/particles/heal/heal.png'}}

#monsters
monster_data = {
	'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'./audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'./audio/attack/claw.wav','speed': 2, 'resistance': 0.5, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'./audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'./audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}

level_0 = {'node_pos':(100,400), 'content': 'this is level 0', 'unlock':1}
level_1 = {'node_pos':(280,220), 'content': 'this is level 1', 'unlock':2}
level_2 = {'node_pos':(460,550), 'content': 'this is level 2', 'unlock':3}
level_3 = {'node_pos':(600,350), 'content': 'this is level 3', 'unlock':4}
level_4 = {'node_pos':(850,210), 'content': 'this is level 4', 'unlock':5}
level_5 = {'node_pos':(1000,400), 'content': 'this is level 5', 'unlock':5}

levels = {
	0: level_0,
	1: level_1,
	2: level_2,
	3: level_3,
	4: level_4,
	5: level_5}
