import pygame as pygame

from Dino import Dino
from coin.BazookaCoin import BazookaCoin
from obstacle.Bird import Bird
from obstacle.Cactus import Cactus

DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 500
WHITE = (255, 255, 255)
FPS = 60
clock = pygame.time.Clock()

quit = False
dino = Dino(30, 30)
cactus = Cactus(700, 400)
bird = Bird(1100, 400)
bazookaCoin = BazookaCoin(1100, 300)

pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

while not quit:
    gameDisplay.fill(WHITE)
    gameDisplay.blit(bazookaCoin.get_image(), (bazookaCoin.get_x(), bazookaCoin.get_y()))
    for box in bazookaCoin.get_collision_boxes():
        pygame.draw.rect(gameDisplay, (255, 0, 0), box, 2)
    bazookaCoin.moveLeft()

    pygame.display.update()
    clock.tick(FPS)
