import glob
import os
import random

import pygame.image

from obstacle.LeftMovingObject import LeftMovingObject


class Cactus(LeftMovingObject):
    __cactus_image_paths = [f for f in glob.glob(os.path.join("sprites", "obstacle", "cactus", "*.png"))]

    #  ground_y is the coordinate of the ground the cactus is moving on
    def __init__(self, x, ground_y):
        image = pygame.image.load(Cactus.__cactus_image_paths[random.randint(0, len(Cactus.__cactus_image_paths) - 1)])
        super().__init__(x, ground_y - image.get_height(), image)

    def moveLeft(self):
        self._x -= self._speed

    def get_collision_boxes(self):
        return [(self._x + self._image.get_width() * 0.1, self._y,
                 self._image.get_width() * 0.9, self._image.get_height())]
