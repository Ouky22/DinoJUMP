import pygame as pygame

from Dino import Dino
from BazookaCoin import BazookaCoin
from obstacle.Bird import Bird
from obstacle.Cactus import Cactus
from obstacle.Explosion import Explosion

DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 500
WHITE = (255, 255, 255)
FPS = 60
clock = pygame.time.Clock()

quit = False
dino = Dino(30, 30)
cactus = Cactus(700, 400)
bird = Bird(1100, 400)
bazookaCoin = BazookaCoin(1100, 300)
explosion = Explosion(800, 300)

pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

dino.activate_bazooka()

while not quit:
    gameDisplay.fill(WHITE)
    gameDisplay.blit(dino.get_image(), (dino.get_x(), dino.get_y()))
    dino.move()
    for box in dino.get_collision_boxes():
        pygame.draw.rect(gameDisplay, (255, 0, 0), box, 2)

    pygame.display.update()
    clock.tick(FPS)
