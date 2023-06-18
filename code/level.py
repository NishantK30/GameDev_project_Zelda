import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice,randint
from weapon import Weapon
from ui import UI
from enemy import Enemy
from particles import AnimationPlayer
from magic import MagicPlayer
from upgrade import Upgrade
from game_data import *
from overworld import *


class Level:
    def __init__(self,current_level,create_overworld):
        
        self.current_level = current_level
        self.create_overworld = create_overworld

        #get the display surface
        self.display_surface = pygame.display.get_surface()
        self.game_paused = False
        #sprite group setup
        self.visible_sprites = YsortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        self.game_active = False
        
        #attack sprite
        self.current_attack = None

        self.create_map()
        self.player_alive = True
        self.Running = True

        #ui
        self.ui = UI()
        self.upgrade = Upgrade(self.player)
        
        

        #particles
        self.animation_player = AnimationPlayer()
        self.magic_player = MagicPlayer(self.animation_player)
    
    def create_map(self):
        layouts = level_graphics[self.current_level]

        graphics = {'grass': import_folder('./graphics/grass'),
                    'object': import_folder('./graphics/objects')}
         
        for style,layout in layouts.items():
                for row_index, row in enumerate(layout):
                    for col_index, col in enumerate(row):
                        if col != '-1':
                            x = col_index * TILESIZE
                            y = row_index * TILESIZE
                            if style == 'boundary':
                                Tile((x,y),[self.obstacle_sprites],'invisible')
                            if style == 'grass':
                                random_grass_image = choice(graphics['grass'])
                                Tile(
                                    (x,y),
                                    [self.visible_sprites,self.obstacle_sprites,self.attackable_sprites],
                                    'grass',
                                    random_grass_image)
    
                            if style == 'object':
                                surf = graphics['object'][int(col)]
                                Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)
    
                            if style == 'entities':
                                if col == '394':
                                    self.player = Player((x,y),
                                                    [self.visible_sprites], 
                                                    self.obstacle_sprites,
                                                    self.create_attack,
                                                    self.destroy_attack,
                                                    self.create_magic,
                                                     )
                            
                                else:
                                    if col == '390': monster_name = 'bamboo'
                                    elif col == '391': monster_name = 'spirit'
                                    elif col == '392': monster_name ='raccoon'
                                    else: monster_name = 'squid'
                                    Enemy(
                                        monster_name,
                                        (x,y),
                                        [self.visible_sprites,self.attackable_sprites],
                                        self.obstacle_sprites,
                                        self.damage_player,
                                        self.trigger_death_particles,
                                        self.add_exp)
    
    def toggle_menu(self):
        self.game_paused = not self.game_paused

    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])
 
    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def create_magic(self,style,strength,cost):
        if style == 'heal':
            self.magic_player.heal(self.player,strength,cost,[self.visible_sprites])

        if style == 'flame':
            self.magic_player.flame(self.player,cost,[self.visible_sprites,self.attack_sprites])

    def trigger_death_particles(self,pos,particle_type):
        self.animation_player.create_particles(particle_type,pos,self.visible_sprites)

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprites in self.attack_sprites:
               collision_sprites = pygame.sprite.spritecollide(attack_sprites,self.attackable_sprites,False)
               if collision_sprites:
                   for target_sprite in collision_sprites:
                       if target_sprite.sprite_type == 'grass':
                           pos = target_sprite.rect.center
                           offset = pygame.math.Vector2(0,50)
                           for leaf in range(randint(3,6)):
                               self.animation_player.create_grass_particles(pos-offset,[self.visible_sprites])
                           target_sprite.kill()
                       else:
                           target_sprite.get_damage(self.player,attack_sprites.sprite_type)

    def damage_player(self,amount,attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            self.animation_player.create_particles(attack_type,self.player.rect.center,[self.visible_sprites])
            #spawn particle

    def add_exp(self,amount):
        self.player.exp += amount
    
    def check_player_death(self):
        if self.player.health <= 0:
            self.create_overworld(self.current_level,0)
	
    def check_win(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_n] :
            self.create_overworld(self.current_attack,self.new_max_level)
	
    
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.ui.display(self.player)
        self.check_player_death()
        self.check_win()
        
       
        if self.game_paused:
            self.upgrade.display()
        else:
            self.visible_sprites.update()
            self.visible_sprites.enemy_update(self.player)
            self.player_attack_logic()
            #self.check_player_death(self.player)
        


#creating a custome sprite Group
class YsortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        #general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] //2
        self.floor_surface = pygame.image.load('./graphics/tilemap/ground.png')
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))
        
    def custom_draw(self,player):

        #creating offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface,floor_offset_pos)
       


        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)




        