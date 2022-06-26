from cmath import rect
import pygame
from debug import debug
from settings import *


class Player(pygame.sprite.Sprite):

    def __init__(self, pos, groups, obstacles_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(
            'graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-26)

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.obstacles_sprites = obstacles_sprites

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == 'horizontal':
            for obs_sprite in self.obstacles_sprites:
                if obs_sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # moving rigth
                        self.hitbox.right = obs_sprite.hitbox.left
                    if self.direction.x < 0:  # moving left
                        self.hitbox.left = obs_sprite.hitbox.right

        if direction == 'vertical':
            for obs_sprite in self.obstacles_sprites:
                if obs_sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving down
                        self.hitbox.bottom = obs_sprite.hitbox.top
                    if self.direction.y < 0: # moving up
                        self.hitbox.top = obs_sprite.hitbox.bottom
                    

    def update(self):
        self.input()
        self.move(self.speed)
