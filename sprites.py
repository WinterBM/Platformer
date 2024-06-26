import sys
import pygame
from pygame.locals import *

vec = pygame.math.Vector2

# Functions
def level_reader(path:str, all_sprites, object_sprites):
    """
    Reads level txt file and adds to aproriate sprite groups

    :param path str: path to level txt file
    :param all_sprites : sprite group for all sprites
    :param object_sprites [TODO:type]: sprite group for platform sprites
    """
    with open(path, "r") as f:
        lines = f.readlines()
        for y, line in enumerate(lines):
            for x, pos in enumerate(line):
                if pos =="x":
                    PT = Platform((x*50,y*50))
                    all_sprites.add(PT)
                    object_sprites.add(PT)

def border_move(P1, object_sprites, width:int ,ACC, fric):
    """
    Implements movement when player reaches 

    :param P1 Player: player
    :param object_sprites sprite.group: All non player sprites
    :param width int: width of display
    """
    pressed_keys = pygame.key.get_pressed()
    if P1.pos.x < 0.2*width and pressed_keys[K_LEFT]:
        for entity in object_sprites:
            entity.move(ACC, fric, "left")
        P1.pos.x = 0.2*width
    if P1.pos.x > 0.8*width and pressed_keys[K_RIGHT]:
        for entity in object_sprites:
            entity.move(ACC, fric, "right")
        P1.pos.x = 0.8*width    
        P1.vel.x = 0
        P1.acc.x = 0

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
        if hits:
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
    
    def move(self, ACC:float, fric:float, direction:str):
        """
        Implements movement of platform sprites

        :param ACC float: acceleration
        :param fric float: friction
        :direction str: direction of movement
        """
                
        ## Acceleration events
        self.acc = vec(0,0)
        if direction=="left":
            self.acc.x = ACC
        if direction=="right":
            self.acc.x = -ACC
        
        ## Equations of motion
        self.acc += self.vel * fric
        self.vel += self.acc
        self.pos += self.vel +0.5*self.acc
        
        self.rect.midbottom = self.pos

    


