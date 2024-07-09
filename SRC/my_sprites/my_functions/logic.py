import pygame
from pygame.locals import *
from  my_sprites.my_functions.read_graphics import level_reader

def border_move(P1, object_sprites, width:int ,ACC, fric):
    """
    Implements movement when player reaches 

    :param P1 Player: player
    :param object_sprites sprite.group: All non player sprites
    :param width int: width of display
    """
    pressed_keys = pygame.key.get_pressed()

    if P1.pos.x < 0.2*width and P1.vel.x < 0:
        for entity in object_sprites:
            entity.rect.x -= P1.vel.x+0.5*P1.acc.x
        P1.pos.x = 0.2*width

    if P1.pos.x > 0.8*width and P1.vel.x > 0:
        for entity in object_sprites:
            entity.rect.x -= P1.vel.x+0.5*P1.acc.x
        P1.pos.x = 0.8*width

def death(path, all_sprites, object_sprites, P1):
    if P1.pos.y > 900:
        all_sprites.empty()
        object_sprites.empty()
        level_reader(path, all_sprites, object_sprites)
        all_sprites.add(P1)
        P1.pos.x = 0
        P1.pos.y = 200
