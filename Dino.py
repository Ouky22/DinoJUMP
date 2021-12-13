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
        self.__stooping = False
        self.__jumping = False

        self.__running_counter = 0
        self.__jump_counter = 0

    def move(self):
        if not self.__jumping:
            if self.__has_bazooka:  # set current dino image to next bazooka dino
                if self.__running_counter >= len(Dino.__bazooka_sprite_paths):
                    self.__running_counter = 0
                self.__dino_image = pygame.image.load(Dino.__bazooka_sprite_paths[self.__running_counter])
            elif self.__stooping:  # set current dino image to next stooping dino
                if self.__running_counter >= len(Dino.__stooping_sprite_paths):
                    self.__running_counter = 0
                self.__dino_image = pygame.image.load(Dino.__stooping_sprite_paths[self.__running_counter])
                pass
            else:  # set current dino image to next normal dino
                if self.__running_counter >= len(Dino.__running_sprite_paths):
                    self.__running_counter = 0
                self.__dino_image = pygame.image.load(Dino.__running_sprite_paths[self.__running_counter])

            self.__running_counter += 1
        else:
            pass

        return self.__dino_image

    def set_stooping(self, stooping):
        self.__stooping = stooping

    def activate_bazooka(self):
        self.__has_bazooka = True

    def activate_jumping(self):
        self.__jumping = True
