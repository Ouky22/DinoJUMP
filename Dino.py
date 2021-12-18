import os.path

import pygame.image
import glob


class Dino:
    __running_sprite_paths = [f for f in glob.glob(os.path.join("sprites", "dino", "dino_running_normal", "*.png"))]
    __stooping_sprite_paths = [f for f in glob.glob(os.path.join("sprites", "dino", "dino_running_stooping", "*.png"))]
    __bazooka_sprite_paths = [f for f in glob.glob(os.path.join("sprites", "dino", "dino_running_bazooka", "*.png"))]
    __jumping_sprite_path = os.path.join("sprites", "dino", "dino_running_normal", "trex01.png")
    __game_over_sprite_path = os.path.join("sprites", "dino", "trex04.png")
    __game_over_bazooka_sprite_path = os.path.join("sprites", "dino", "trexBazooka04.png")

    __jump_height = 8
    # how often move has to be called after the current image
    # gets changed for creating movement effect
    __running_speed = 4

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

        self.__current_image = pygame.image.load(Dino.__running_sprite_paths[0])

        self.__has_bazooka = False
        self.__stooping = False
        self.__jumping = False

        self.__running_counter = 0
        self.__current_image_index = 0
        self.__jump_counter = Dino.__jump_height * -1

    def move(self):
        if not self.__jumping:
            self.__running_counter += 1

            # do not perform movement if __running_counter is not a multiple of __running_speed
            if self.__running_counter % Dino.__running_speed != 0:
                return

            self.__current_image_index += 1

            if self.__has_bazooka:  # set current dino image to next bazooka dino
                if self.__current_image_index >= len(Dino.__bazooka_sprite_paths):
                    self.__current_image_index = 0
                self.__current_image = pygame.image.load(Dino.__bazooka_sprite_paths[self.__current_image_index])
            elif self.__stooping:  # set current dino image to next stooping dino
                if self.__current_image_index >= len(Dino.__stooping_sprite_paths):
                    self.__current_image_index = 0
                self.__current_image = pygame.image.load(Dino.__stooping_sprite_paths[self.__current_image_index])
                pass
            else:  # set current dino image to next normal dino
                if self.__current_image_index >= len(Dino.__running_sprite_paths):
                    self.__current_image_index = 0
                self.__current_image = pygame.image.load(Dino.__running_sprite_paths[self.__current_image_index])
        else:
            if self.__jump_counter <= Dino.__jump_height:
                if self.__jump_counter < 0:
                    self.__y -= self.__jump_counter ** 2
                else:
                    self.__y += self.__jump_counter ** 2

                self.__jump_counter += 1
            else:
                self.__jumping = False
                self.__jump_counter = Dino.__jump_height * -1

    def set_stooping(self, stooping):
        self.__stooping = stooping

    def activate_bazooka(self):
        self.__has_bazooka = True

    def activate_jumping(self):
        self.__jumping = True
        self.__current_image = pygame.image.load(Dino.__jumping_sprite_path)

    def get_collision_boxes(self):
        if self.__stooping:
            return [(self.__x, self.__y, self.__current_image.get_width(), self.__current_image.get_height()),
                    (self.__x, self.__y, self.__current_image.get_width(), self.__current_image.get_height())]
        elif self.__has_bazooka:
            return [(self.__x, self.__y, self.__current_image.get_width(), self.__current_image.get_height()),
                    (self.__x, self.__y, self.__current_image.get_width(), self.__current_image.get_height())]
        else:
            return [(self.__x + self.__current_image.get_width() * 0.5, self.__y,
                     self.__current_image.get_width() * 0.45, self.__current_image.get_height() * 0.4),
                    (self.__x + self.__current_image.get_width() * 0.05, self.__y + self.get_image().get_height() * 0.4,
                     self.__current_image.get_width() * 0.65, self.__current_image.get_height() * 0.3),
                    (self.__x + self.__current_image.get_width() * 0.25, self.__y + self.get_image().get_height() * 0.7,
                     self.__current_image.get_width() * 0.3, self.__current_image.get_height() * 0.25)]

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_image(self):
        return self.__current_image
