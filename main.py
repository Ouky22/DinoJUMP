import pygame as pygame

from Dino import Dino
from coin.BazookaCoin import BazookaCoin
from obstacle.Bird import Bird
from obstacle.Cactus import Cactus
from obstacle.Explosion import Explosion

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
explosion = Explosion(800, 300)

pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

while not quit:
    gameDisplay.fill(WHITE)
    if not explosion.isExplosionOver():
        gameDisplay.blit(explosion.get_image(), (explosion.get_x(), explosion.get_y()))
        explosion.moveLeft()
    for box in explosion.get_collision_boxes():
        pygame.draw.rect(gameDisplay, (255, 0, 0), box, 2)

    pygame.display.update()
    clock.tick(FPS)
