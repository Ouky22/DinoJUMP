import pygame

from LeftMovingObject import LeftMovingObject


class GroundPiece(LeftMovingObject):

    def __init__(self, x, ground_y, image_path):
        image = pygame.image.load(image_path).convert_alpha()
        super().__init__(x, ground_y - image.get_height(), image)

    def moveLeft(self):
        self._x -= self._speed

    # ground pieces don't need collision boxes
    def get_collision_boxes(self):
        return []
