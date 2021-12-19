import pygame as pygame

from Dino import Dino
from bazooka.BazookaCoin import BazookaCoin
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

counter = 0

dino.activate_bazooka()
dino.shoot_bullet()

while not quit:
    gameDisplay.fill(WHITE)
    gameDisplay.blit(dino.get_image(), (dino.get_x(), dino.get_y()))
    for bullet in dino.get_bullets():
        gameDisplay.blit(bullet.get_image(), (bullet.get_x(), bullet.get_y()))

    dino.move()

    counter += 1
    if counter % 100 == 0:
        dino.shoot_bullet()
        counter = 0

    for box in dino.get_collision_boxes():
        pygame.draw.rect(gameDisplay, (255, 0, 0), box, 2)

    for box in dino.get_bullets_collision_boxes():
        pygame.draw.rect(gameDisplay, (255, 0, 0), box, 2)

    pygame.display.update()
    clock.tick(FPS)
