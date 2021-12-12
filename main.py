import pygame as pygame

from Dino import Dino

DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 500
WHITE = (255, 255, 255)
FPS = 30
clock = pygame.time.Clock()

quit = False
dino = Dino(30, 30)

pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

while not quit:
    gameDisplay.fill(WHITE)
    gameDisplay.blit(dino.getImage(), (50, 50))
    dino.run()

    pygame.display.update()
    clock.tick(FPS)
