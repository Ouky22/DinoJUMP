import os


class Bullet:
    __bullet_image_path = os.path.join("sprites", "bazooka", "bazookaBullet.py")
    __speed = 10

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def move_right(self):
        pass

    def get_image(self):
        pass

    def get_collision_boxes(self):
        pass

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
