from abc import ABC, abstractmethod


class LeftMovingObject(ABC):
    def __init__(self, x, y, image, speed=10):
        self._x = x
        self._y = y
        self._image = image
        self._speed = speed

    def increase_speed(self, increase):
        self._speed += increase

    @abstractmethod
    def moveLeft(self):
        pass

    @abstractmethod
    def get_collision_boxes(self):
        pass

    def get_image(self):
        return self._image

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y
