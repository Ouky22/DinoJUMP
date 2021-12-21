import random

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
ground_y = DISPLAY_HEIGHT - 100

# game objects
dino = Dino(10, ground_y)
cacti = []
birds = []
bazookaCoins = []
explosions = []

quit_game = False


def handle_pressed_keys(pressed_keys):
    if pressed_keys[pygame.K_SPACE] or pressed_keys[pygame.K_UP]:
        dino.activate_jumping()
    elif pressed_keys[pygame.K_DOWN]:
        if dino.is_jumping():
            dino.jump_down_faster()
        else:
            dino.set_stooping(True)
    else:
        dino.set_stooping(False)

    if pressed_keys[pygame.K_s]:
        dino.shoot_bullet()


def draw_moving_objects():
    # draw dino
    gameDisplay.blit(dino.get_image(), (dino.get_x(), dino.get_y()))
    # draw bullets
    for bullet in dino.get_bullets():
        gameDisplay.blit(bullet.get_image(), (bullet.get_x(), bullet.get_y()))
    # draw cacti
    for cactus in cacti:
        gameDisplay.blit(cactus.get_image(), (cactus.get_x(), cactus.get_y()))
    # draw Bird
    for bird in birds:
        gameDisplay.blit(bird.get_image(), (bird.get_x(), bird.get_y()))
    # draw bazookaCoin:
    for bazookaCoin in bazookaCoins:
        gameDisplay.blit(bazookaCoin.get_image(), (bazookaCoin.get_x(), bazookaCoin.get_y()))
    # draw explosion
    for explosion in explosions:
        gameDisplay.blit(explosion.get_image(), (explosion.get_x(), explosion.get_y()))


def create_obstacles():
    rnd_number = random.randint(0, 100)
    # todo create obstacles


def perform_object_movements():
    dino.move()

    for cactus in cacti:
        cactus.moveLeft()

    for bird in birds:
        bird.moveLeft()

    for bazookaCoin in bazookaCoins:
        bazookaCoin.moveLeft()

    for explosion in explosions:
        explosion.moveLeft()


while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    handle_pressed_keys(pygame.key.get_pressed())

    perform_object_movements()

    gameDisplay.fill(WHITE)
    draw_moving_objects()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
