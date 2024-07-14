import sys 
import pygame
from pygame.locals import *

vec = pygame.math.Vector2

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30,30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect(center= (40, 420))

        self.pos = vec((40,420))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self,g,ACC,fric):
        """
        Implements movement
        """
        self.acc = vec(0,g)

        pressed_keys = pygame.key.get_pressed()

        ## Acceleration events
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        
        ## Equations of motion
        self.acc += self.vel * fric
        self.vel += self.acc
        self.pos += self.vel +0.5*self.acc
        
        self.rect.midbottom = self.pos

    def update(self, sprite_group):
        """
        detects collisions
        """
        hits = pygame.sprite.spritecollide(self, sprite_group,
                                           False)
        if hits and self.vel.y > 0.5:
            self.pos.y = hits[0].rect.top+1
            self.vel.y = 0
        
    def jump(self):
        """
        implements jump
        """
        self.vel.y = -20


class Platform(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.surf = pygame.Surface((50,50))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center= position)

        self.acc = vec(0,0)
        self.vel = vec(0,0)
        self.pos = vec(position)

    def oscilate(self,ACC, fric):
        if self.vel.x <= 0:
            self.acc.x = ACC
        elif self.vel.x > 20:
            self.acc.x = -ACC

        self.acc += self.vel * fric
        self.vel += self.acc
        self.pos += self.vel +0.5*self.acc
        
        self.rect.midbottom = self.pos

