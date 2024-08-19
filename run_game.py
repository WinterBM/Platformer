# Libraries
import pygame
from pygame.locals import *
import sys
from my_sprites.my_functions.logic import border_move, death
from my_sprites.my_functions.read_graphics import level_reader
from my_sprites.my_sprites import Player, Platform

# Initiaze and set constants
pygame.init()

height = 500
width = 800
g = 0.5
ACC = 0.5
fric = -0.12
fps = 60

FramesPerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")

# Read levels
all_sprites = pygame.sprite.Group()
object_sprites = pygame.sprite.Group()
level_reader("Levels/level1.txt", all_sprites, object_sprites)

P1 = Player()
all_sprites.add(P1)
# Game loop
while True:
    ## Get player inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.sprite.spritecollide(P1, object_sprites, False):
                    P1.jump()

    displaysurface.fill((0,0,0))
    
    ## Dynamics
    border_move(P1, object_sprites, width, ACC, fric) 
    P1.move(g, ACC, fric)
    P1.update(object_sprites)
    death("Levels/level1.txt", all_sprites, object_sprites, P1)

    ## Draw sprites
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        
    pygame.display.update()
    FramesPerSec.tick(fps)
