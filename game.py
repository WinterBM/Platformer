# Libraries
import sys
from sprites import *

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
    ## Calculate forces
    if P1.pos.x < 0.2*width:        
        for entity in object_sprites:
            entity.move(ACC,fric, "left", P1)
    if P1.pos.x > 0.8*width:
        for entity in object_sprites:
            entity.move(ACC,fric, "right", P1)

    P1.move(g, ACC, fric)
    P1.update(object_sprites)

    ## Draw sprites
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        
    pygame.display.update()
    FramesPerSec.tick(fps)
