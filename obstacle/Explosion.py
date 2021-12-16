import glob
import os

import pygame

from obstacle.LeftMovingObject import LeftMovingObject


class Explosion(LeftMovingObject):
    __explosion_image_paths = [f for f in glob.glob(os.path.join("sprites", "obstacle", "explosion", "*.png"))]

    def __init__(self, x, y):
        image = pygame.image.load(Explosion.__explosion_image_paths[0])
        super().__init__(x, y, image)

    def moveLeft(self):
        pass

    def get_collision_boxes(self):
        pass
