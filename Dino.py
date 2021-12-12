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

    __jump_height = 10

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__dino_image = pygame.image.load(Dino.__running_sprite_paths[0])
        self.__has_bazooka = False
        self.__running_counter = 0
        self.__running_counter = 0
        self.__jump_counter = 0

    def run(self):
        if self.__has_bazooka:
            if self.__running_counter >= len(Dino.__bazooka_sprite_paths):
                self.__running_counter = 0
            self.__dino_image = pygame.image.load(Dino.__bazooka_sprite_paths[self.__running_counter])
        else:
            if self.__running_counter >= len(Dino.__running_sprite_paths):
                self.__running_counter = 0
            self.__dino_image = pygame.image.load(Dino.__running_sprite_paths[self.__running_counter])

        self.__running_counter += 1

    def run_stooping(self):
        if self.__running_counter >= len(Dino.__stooping_sprite_paths):
            self.__running_counter = 0
        self.__dino_image = pygame.image.load(Dino.__stooping_sprite_paths[self.__running_counter])

        self.__running_counter += 1

    def jump(self):
        pass

    def getImage(self):
        return self.__dino_image
