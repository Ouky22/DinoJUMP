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
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
SCORE_FONT = pygame.font.SysFont('impact', 40)

# Colors
WHITE = (255, 255, 255)
SCORE_COLOR = (200, 200, 200)

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
game_over = True

current_score = 0
high_score = 0
score_counter = 0


def handle_pressed_keys(pressed_keys):
    global quit_game

    if pressed_keys[pygame.K_ESCAPE] or pressed_keys[pygame.K_q]:
        quit_game = True

    if not game_over:
        if pressed_keys[pygame.K_SPACE] or pressed_keys[pygame.K_UP]:
            dino.activate_jumping()
        elif pressed_keys[pygame.K_DOWN]:
            if dino.is_jumping():
                dino.jump_down_faster()
            else:
                dino.set_stooping(True)
        else:
            dino.set_stooping(False)

        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_RIGHT]:
            dino.shoot_bullet()
    else:
        if pressed_keys[pygame.K_SPACE]:
            start_game()


def start_game():
    global dino, cacti, birds, bazookaCoins, explosions, game_over, current_score
    # reset game objects for new game
    dino = Dino(10, ground_y)
    cacti = []
    birds = []
    bazookaCoins = []
    explosions = []

    game_over = False
    current_score = 0


def draw_moving_objects():
    # draw dino
    game_display.blit(dino.get_image(), (dino.get_x(), dino.get_y()))
    # draw bullets
    for bullet in dino.get_bullets():
        game_display.blit(bullet.get_image(), (bullet.get_x(), bullet.get_y()))
    # draw cacti
    for cactus in cacti:
        game_display.blit(cactus.get_image(), (cactus.get_x(), cactus.get_y()))
    # draw Bird
    for bird in birds:
        game_display.blit(bird.get_image(), (bird.get_x(), bird.get_y()))
    # draw bazookaCoin:
    for bazookaCoin in bazookaCoins:
        game_display.blit(bazookaCoin.get_image(), (bazookaCoin.get_x(), bazookaCoin.get_y()))
    # draw explosion
    for explosion in explosions:
        game_display.blit(explosion.get_image(), (explosion.get_x(), explosion.get_y()))


def draw_score_text():
    global current_score, high_score

    # draw current score
    current_score_text = SCORE_FONT.render(str(current_score).zfill(5), True, SCORE_COLOR)
    game_display.blit(current_score_text, (DISPLAY_WIDTH - current_score_text.get_width() - 20, 10))
    # draw high score
    high_score_text = SCORE_FONT.render("HI " + str(high_score).zfill(5), True, SCORE_COLOR)
    game_display.blit(high_score_text, (20, 10))


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

    #  check if dino collides with bazookaCoin
    for bazookaCoin in bazookaCoins:
        if does_collide(bazookaCoin.get_collision_boxes(), dino.get_collision_boxes()):
            dino.activate_bazooka()
            bazookaCoins.remove(bazookaCoin)

    #  check if bullets collide with obstacle
    for bullet in dino.get_bullets():
        for cactus in cacti:
            if does_collide(bullet.get_collision_boxes(), cactus.get_collision_boxes()):
                explosions.append(Explosion(cactus.get_x(), ground_y))
                cacti.remove(cactus)
                dino.remove_bullet(bullet)
        for bird in birds:
            if does_collide(bullet.get_collision_boxes(), bird.get_collision_boxes()):
                explosions.append(Explosion(bird.get_x(), bird.get_y() + bird.get_image().get_height()))
                birds.remove(bird)
                dino.remove_bullet(bullet)


def remove_finished_explosions():
    for explosion in explosions:
        if explosion.isExplosionOver():
            explosions.remove(explosion)


while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    handle_pressed_keys(pygame.key.get_pressed())

    if not game_over:
        perform_object_movements()

        # game object spawning
        game_obj_spawn_counter += 1
        if game_obj_spawn_counter % game_obj_spawn_frequency == 0:
            create_rnd_left_moving_object()

        handle_collision()

        remove_finished_explosions()

        # handle score
        score_counter += 1
        if score_counter % 10 == 0:
            current_score += 1
            if current_score > high_score:
                high_score = current_score

        # drawing
        game_display.fill(WHITE)
        draw_moving_objects()
        draw_score_text()
        pygame.display.update()
        clock.tick(FPS)

        if game_over:
            pygame.time.wait(1500)

pygame.quit()
