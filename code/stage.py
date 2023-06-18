import pygame 
from settings import *


class Stage:
	def __init__(self,current_level,surface,create_overworld):

		# level setup 
		self.display_surface = surface 
		self.current_level = current_level
		level_data = levels[self.current_level]
		self.new_max_level = level_data['unlock']
		self.create_overworld = create_overworld


	def input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RETURN]:
			self.create_overworld(self.current_level,self.new_max_level)
		if keys[pygame.K_ESCAPE]:
			self.create_overworld(self.current_level,0)
    
	def run(self):
		self.input()