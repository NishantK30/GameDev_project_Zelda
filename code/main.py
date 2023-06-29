import pygame, sys
from settings import *
from overworld import Overworld
from stage import Stage
from level import *
from upgrade import *

class Game:
	def __init__(self):
		self.max_level = 1
		
		#audio
		self.overworld_bg_music = pygame.mixer.Sound('./audio/main2.mp3')
		
		self.overworld = Overworld(1,self.max_level,screen,self.create_level)
		self.status = 'overworld'
		self.overworld_bg_music.play(loops= -1)

		#audio
		#self.level_bg_music = pygame.mixer.Sound('./audio/main.ogg')
		#self.overworld_bg_music = pygame.mixer.Sound('./audio/main.ogg')

	def create_level(self,current_level):
			self.level = Level(current_level,self.create_overworld)
			self.stage = Stage(current_level,screen,self.create_overworld)
			self.status = 'level'
			self.overworld_bg_music.fadeout(100)
			self.level_bg_music = pygame.mixer.Sound(music[current_level])
			self.level_bg_music.play(loops = -1,fade_ms=100)
			self.level_bg_music.set_volume(0.6)
	
   

	def create_upgrade(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_m:
					self.level.toggle_menu()
 	
	def create_overworld(self,current_level,new_max_level):
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
		self.status = 'overworld'
		self.level_bg_music.stop()
		self.overworld_bg_music.play(loops= -1,fade_ms=100)
		self.overworld_bg_music.set_volume(0.6)

	def run(self):
		if self.status == 'overworld':
			self.overworld.run()
	    
		else:
			self.level.run()
			self.stage.run()
			self.create_upgrade()	

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGTH))
clock = pygame.time.Clock()
game = Game()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	screen.fill((135, 15, 213, 0.8))
	game.run()

	pygame.display.update()
	clock.tick(60)