import os.path

import pygame.image
import glob

from bazooka.Bullet import Bullet


class Dino:
    # sprites for running dino
    __running_sprite_paths = [f for f in glob.glob(os.path.join("sprites", "dino", "dino_running_normal", "*.png"))]
    __stooping_sprite_paths = [f for f in glob.glob(os.path.join("sprites", "dino", "dino_running_stooping", "*.png"))]
    __bazooka_sprite_paths = [f for f in glob.glob(os.path.join("sprites", "dino", "dino_running_bazooka", "*.png"))]
    # sprites for jumping dino
    __jumping_sprite_path = os.path.join("sprites", "dino", "dino_running_normal", "trex01.png")
    __jumping_bazooka_sprite_path = os.path.join("sprites", "dino", "dino_running_bazooka", "trexBazooka01.png")
    # sprites for dino when game is over
    __game_over_sprite_path = os.path.join("sprites", "dino", "dino_game_over", "trex04.png")
    __game_over_bazooka_sprite_path = os.path.join("sprites", "dino", "dino_game_over", "trexBazooka04.png")

    __jump_height = 8

    # how often move() has to be called after the current image
    # gets changed for creating movement effect
    __running_speed = 5

    # how often move() has to be called after the next bullet can be shot
    __bullet_loading_speed = 10

    #  ground_y is the coordinate of the ground the dino is moving on
    def __init__(self, x, ground_y):
        self.__current_image = pygame.image.load(Dino.__running_sprite_paths[0])

        self.__x = x
        self.__y = ground_y - self.__current_image.get_height()

        self.__has_bazooka = False
        self.__stooping = False
        self.__jumping = False

        self.__running_counter = 0
        self.__current_image_index = 0
        self.__jump_counter = Dino.__jump_height * -1

        self.__bullets = []
        # how many bullets the dino has after collecting bazookaCoin
        self.__bullet_amount = 0
        # for bullet loading (bullets shouldn't be shot at the same time)
        self.__bullet_loading_counter = 0
        self.__bullet_loaded = False

    def move(self):
        self.__running_counter += 1
        # do not perform movement if __running_counter is not a multiple of __running_speed
        if self.__running_counter % Dino.__running_speed != 0:
            return

        if not self.__jumping:
            self.__current_image_index += 1

            if self.__has_bazooka:  # set current dino image to next bazooka dino
                if self.__current_image_index >= len(Dino.__bazooka_sprite_paths):
                    self.__current_image_index = 0
                self.__current_image = pygame.image.load(Dino.__bazooka_sprite_paths[self.__current_image_index])
            elif self.__stooping:  # set current dino image to next stooping dino
                if self.__current_image_index >= len(Dino.__stooping_sprite_paths):
                    self.__current_image_index = 0
                self.__current_image = pygame.image.load(Dino.__stooping_sprite_paths[self.__current_image_index])
            else:  # set current dino image to next normal dino
                if self.__current_image_index >= len(Dino.__running_sprite_paths):
                    self.__current_image_index = 0
                self.__current_image = pygame.image.load(Dino.__running_sprite_paths[self.__current_image_index])
        else:
            if self.__jump_counter <= Dino.__jump_height:
                # jump up
                if self.__jump_counter < 0:
                    self.__y -= self.__jump_counter ** 2
                # jump down
                else:
                    self.__y += self.__jump_counter ** 2

                self.__jump_counter += 1
            else:
                self.__jumping = False
                self.__jump_counter = Dino.__jump_height * -1

        # for bullet loading
        if not self.__bullet_loaded:
            self.__bullet_loading_counter += 1
        if self.__bullet_loading_counter % Dino.__bullet_loading_speed == 0:
            self.__bullet_loaded = True

        # move bullets right
        for bullet in self.__bullets:
            bullet.move_right()

    # this method is for getting down the dino faster when the dino is jumping
    def jump_down_faster(self):
        if not self.__jumping \
                or self.__jump_counter > Dino.__jump_height or self.__jump_counter <= Dino.__jump_height * -1:
            return

        # if dino is moving up
        if self.__jump_counter < 0:
            # make him moving down to the ground
            self.__jump_counter = (self.__jump_counter - 1) * -1  # decrement jump_counter and make it positive

        self.__y += self.__jump_counter ** 2

        self.__jump_counter += 1

    def set_stooping(self, stooping):
        self.__stooping = stooping

    def activate_bazooka(self):
        self.__has_bazooka = True
        self.__bullet_amount = 3
        self.__bullet_loaded = True

        if self.__jumping:
            self.__current_image = pygame.image.load(Dino.__jumping_bazooka_sprite_path)

    def activate_jumping(self):
        if not self.__jumping:
            self.__jumping = True
            if self.__has_bazooka:
                self.__current_image = pygame.image.load(Dino.__jumping_bazooka_sprite_path)
            else:
                self.__current_image = pygame.image.load(Dino.__jumping_sprite_path)

    def get_collision_boxes(self):
        if self.__stooping:
            return [(self.__x * 0.5, self.__y + self.get_image().get_height() * 0.42,
                     self.__current_image.get_width(), self.__current_image.get_height() * 0.5)]
        elif self.__has_bazooka:
            return [
                (self.__x + self.__current_image.get_width() * 0.4, self.__y + self.__current_image.get_height() * 0.05,
                 self.__current_image.get_width() * 0.45, self.__current_image.get_height() * 0.4),
                (self.__x, self.__y + self.get_image().get_height() * 0.4,
                 self.__current_image.get_width() * 0.65, self.__current_image.get_height() * 0.3),
                (self.__x + self.__current_image.get_width() * 0.25, self.__y + self.get_image().get_height() * 0.7,
                 self.__current_image.get_width() * 0.3, self.__current_image.get_height() * 0.25)]
        else:
            return [
                (self.__x + self.__current_image.get_width() * 0.5, self.__y + self.__current_image.get_height() * 0.05,
                 self.__current_image.get_width() * 0.45, self.__current_image.get_height() * 0.4),
                (self.__x + self.__current_image.get_width() * 0.05, self.__y + self.get_image().get_height() * 0.4,
                 self.__current_image.get_width() * 0.65, self.__current_image.get_height() * 0.3),
                (self.__x + self.__current_image.get_width() * 0.25, self.__y + self.get_image().get_height() * 0.7,
                 self.__current_image.get_width() * 0.3, self.__current_image.get_height() * 0.25)]

    def shoot_bullet(self):
        if self.__has_bazooka and self.__bullet_amount > 0 and self.__bullet_loaded:
            self.__bullets.append(Bullet(self.__x + self.__current_image.get_width(),
                                         self.__y + self.__current_image.get_height() * 0.37))
            self.__bullet_amount -= 1
            self.__bullet_loaded = False

        if self.__bullet_amount <= 0:
            self.__has_bazooka = False
            if self.__jumping:
                self.__current_image = pygame.image.load(Dino.__jumping_sprite_path)

    def remove_bullet(self, bullet):
        self.__bullets.remove(bullet)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_image(self):
        return self.__current_image

    def get_bullets(self):
        return self.__bullets

    def is_jumping(self):
        return self.__jumping
