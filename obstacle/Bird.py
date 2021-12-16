import glob
import os

import pygame

from obstacle.LeftMovingObject import LeftMovingObject


class Bird(LeftMovingObject):
    __bird_image_list = [f for f in glob.glob(os.path.join("sprites", "obstacle", "bird", "*.png"))]

    # number of times moveLeft() has to be called,
    # to load the next bird image for creating wing movement
    __wing_movement_speed = 15

    def __init__(self, x, y):
        image = pygame.image.load(Bird.__bird_image_list[0])
        super().__init__(x, y, image)

        # for switching between 2 images of bird for wing movement
        self.__running_counter = 0
        self.__current_image_index = 0

    def moveLeft(self):
        self.__running_counter += 1
        if self.__running_counter >= Bird.__wing_movement_speed:
            self.__current_image_index += 1
            if self.__current_image_index >= len(Bird.__bird_image_list):
                self.__current_image_index = 0
            self._image = pygame.image.load(Bird.__bird_image_list[self.__current_image_index])
            self.__running_counter = 0

        self._x -= self._speed

    def get_collision_box(self):
        pass
