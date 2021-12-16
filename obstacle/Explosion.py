import glob
import os

import pygame

from obstacle.LeftMovingObject import LeftMovingObject


class Explosion(LeftMovingObject):
    __explosion_image_paths = [f for f in glob.glob(os.path.join("sprites", "obstacle", "explosion", "*.png"))]
    # how many times moveLeft() has to be called until
    # the next explosion image is loaded
    __explosion_speed = 1

    def __init__(self, x, y):
        image = pygame.image.load(Explosion.__explosion_image_paths[0])
        super().__init__(x, y, image)

        self.__running_counter = 0
        self.__current_image_index = 0
        self.__explosion_over = False

    def moveLeft(self):
        if self.__running_counter % Explosion.__explosion_speed == 0:
            self.__current_image_index += 1
            if self.__current_image_index >= len(Explosion.__explosion_image_paths):
                self.__current_image_index = 0
                self.__running_counter = 0
                self.__explosion_over = True
            self._image = pygame.image.load(Explosion.__explosion_image_paths[self.__current_image_index])

        self.__running_counter += 1
        self._x -= self._speed

    def isExplosionOver(self):
        return self.__explosion_over

    def get_collision_boxes(self):
        pass
