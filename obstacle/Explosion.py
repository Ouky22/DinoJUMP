import glob
import os

import pygame

from obstacle.LeftMovingObject import LeftMovingObject


class Explosion(LeftMovingObject):
    __explosion_image_paths = [f for f in glob.glob(os.path.join("sprites", "obstacle", "explosion", "*.png"))]
    # how many times moveLeft() has to be called until
    # the next explosion image is loaded
    __explosion_speed = 2

    def __init__(self, x, y):
        image = pygame.image.load(Explosion.__explosion_image_paths[0])
        super().__init__(x, y, image)

        self.__running_counter = 0
        self.__current_image_index = 0
        self.__explosion_over = False

    def moveLeft(self):
        if self.__running_counter % Explosion.__explosion_speed == 0:
            self.__current_image_index += 1
            if self.__current_image_index < len(Explosion.__explosion_image_paths):
                self._image = pygame.image.load(Explosion.__explosion_image_paths[self.__current_image_index])
                self._x -= self._speed
            else:
                self.__explosion_over = True

        if not self.__explosion_over:
            self.__running_counter += 1

    def isExplosionOver(self):
        return self.__explosion_over

    def get_collision_boxes(self):
        # explosion is not deadly at the end, so return no collision boxes
        if self.__current_image_index < len(Explosion.__explosion_image_paths) - 6:
            return [(self._x + self._image.get_width() * 0.3, self._y + self._image.get_height() * 0.4,
                     self._image.get_width() * 0.5, self._image.get_height() * 0.6)]
        return []
