import pygame as pygame

from Dino import Dino
from bazooka.BazookaCoin import BazookaCoin
from obstacle.Bird import Bird
from obstacle.Cactus import Cactus
from obstacle.Explosion import Explosion

pygame.init()

# display
pygame.display.set_caption("Dino Jump")
DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 500
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
WHITE = (255, 255, 255)

# time
FPS = 60
clock = pygame.time.Clock()

# game constants
ground_y = DISPLAY_HEIGHT - 10

# game objects
dino = Dino(30, 30)
cactus = Cactus(700, 400)
bird = Bird(1100, 400)
bazookaCoin = BazookaCoin(1100, 300)
explosion = Explosion(800, 300)

quit_game = False


def perform_dino_actions(pressed_keys):
    pass


while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    gameDisplay.fill(WHITE)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
