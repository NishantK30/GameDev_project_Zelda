import pygame
from math import sin

class Entity(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()

    def move(self,speed):
        #fixing diagonal speeding up issue
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        #movement
        self.hitbox.x += self.direction.x * speed
        self.collison('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collison('vertical')
        self.rect.center = self.hitbox.center

    def collison(self,direction):
        #detecting horizontal collision
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #moving up
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: #moving down
                        self.hitbox.left = sprite.hitbox.right


            
        #detecting vertical collision
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y < 0: #moving up
                        self.hitbox.top = sprite.hitbox.bottom
                    if self.direction.y > 0: #moving down
                        self.hitbox.bottom = sprite.hitbox.top

    def wave_value(self):
        value = sin(pygame.time.get_ticks()) 
        if value >= 0:
            return 255
        else:
            return 0   
    