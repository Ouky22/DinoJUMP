import os

import pygame


class Bullet:
    __bullet_image_path = os.path.join("sprites", "bazooka", "bazookaBullet.py")
    __speed = 10

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__image = pygame.image.load(Bullet.__bullet_image_path)

    def move_right(self):
        self.__x += self.__speed

    def get_image(self):
        return self.__image

    def get_collision_boxes(self):
        return [(self.__x, self.__y, self.__image.get_width(), self.__image.get_height())]

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
