import pygame
from pygame.locals import *

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
