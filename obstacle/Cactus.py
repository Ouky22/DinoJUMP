import glob
import os
import random

import pygame.image

from obstacle.LeftMovingObject import LeftMovingObject


class Cactus(LeftMovingObject):
    __cactus_image_paths = [f for f in glob.glob(os.path.join("sprites", "obstacle", "cactus", "*.png"))]

    def __init__(self, x, y):
        image = pygame.image.load(Cactus.__cactus_image_paths[random.randint(0, len(Cactus.__cactus_image_paths) - 1)])
        super().__init__(x, y, image)

    def moveLeft(self):
        self._x -= self._speed

    def get_collision_boxes(self):
        return [(self._x, self._y, self._image.get_width(), self._image.get_height())]
