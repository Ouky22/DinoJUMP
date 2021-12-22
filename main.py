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
ground_y = DISPLAY_HEIGHT

# game objects
dino = Dino(10, ground_y)
cacti = []
birds = []
bazookaCoins = []
explosions = []

# after how many loops a cactus, a bird or a bazookaCoin can be created
game_obj_spawn_frequency = 60
game_obj_spawn_counter = 0

quit_game = False

game_over = False


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
    # draw dino
    gameDisplay.blit(dino.get_image(), (dino.get_x(), dino.get_y()))


#  create randomly bazookaCoin, bird, cactus or none
def create_rnd_left_moving_object():
    rnd_number = random.randint(0, 50)

    if rnd_number == 0:
        #  only one bazookaCoin should exist at the same time
        if len(bazookaCoins) == 0:
            bazookaCoins.append(BazookaCoin(DISPLAY_WIDTH, ground_y - random.randint(200, 250)))
    elif rnd_number % 5 == 0:
        #  only two birds should exist at the same time
        if len(birds) <= 1:
            birds.append(Bird(DISPLAY_WIDTH, ground_y - random.randint(110, 220)))
    elif rnd_number % 2 == 0:
        cacti.append(Cactus(DISPLAY_WIDTH, ground_y))


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


def does_collide(collision_boxes_1, collision_boxes_2):
    for collision_box_1 in collision_boxes_1:
        for collision_box_2 in collision_boxes_2:
            if pygame.Rect(collision_box_1).colliderect(pygame.Rect(collision_box_2)):
                return True


def handle_collision():
    global game_over

    #  check if dino collides with cactus
    for cactus in cacti:
        if does_collide(cactus.get_collision_boxes(), dino.get_collision_boxes()):
            game_over = True
            break

    #  check if dino collides with bird
    for bird in birds:
        if does_collide(bird.get_collision_boxes(), dino.get_collision_boxes()):
            game_over = True
            break


while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    handle_pressed_keys(pygame.key.get_pressed())

    perform_object_movements()

    game_obj_spawn_counter += 1
    if game_obj_spawn_counter % game_obj_spawn_frequency == 0:
        create_rnd_left_moving_object()

    handle_collision()

    #  for testing
    if game_over:
        quit_game = True

    gameDisplay.fill(WHITE)
    draw_moving_objects()
    pygame.display.update()
    clock.tick(FPS)

#  for testing
while True:
    pass

pygame.quit()
