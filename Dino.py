import os.path

import pygame.image
import glob


class Dino:
    __running_sprite_paths = [f for f in glob.glob(os.path.join("sprites", "dino", "dino_running_normal", "*.png"))]
    __stooping_sprite_paths = [f for f in glob.glob(os.path.join("sprites", "dino", "dino_running_stooping", "*.png"))]
    __bazooka_sprite_paths = [f for f in glob.glob(os.path.join("sprites", "dino", "dino_running_bazooka", "*.png"))]
    __jumping_sprite_path = os.path.join("sprites", "dino", "dino_running_normal", "trex04.png")
    __game_over_sprite_path = os.path.join("sprites", "dino", "trex04.png")
    __game_over_bazooka_sprite_path = os.path.join("sprites", "dino", "trexBazooka04.png")

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__dino_image = pygame.image.load(Dino.__running_sprite_paths[0])
        self.__has_bazooka = False
        self.__running_counter = 0

    def run(self):
        pass

    def run_stooping(self):
        pass

    def jump(self):
        pass

    def getImage(self):
        return self.__dino_image
