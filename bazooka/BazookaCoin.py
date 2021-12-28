import os.path

import pygame

from LeftMovingObject import LeftMovingObject


class BazookaCoin(LeftMovingObject):
    __bazooka_image_path = os.path.join("sprites", "bazooka", "bazookaCoin.png")

    def __init__(self, x, y):
        image = pygame.image.load(BazookaCoin.__bazooka_image_path).convert_alpha()
        image = pygame.transform.scale(image, (50, 40))
        super().__init__(x, y, image)

    def moveLeft(self):
        self._x -= self._speed

    def get_collision_boxes(self):
        return [(self._x, self._y, self._image.get_width(), self._image.get_height())]
