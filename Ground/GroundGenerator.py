import glob
import os


class GroundGenerator:
    __sprite_paths = [f for f in glob.glob(os.path.join("../sprites", "ground", "*.png"))]

    def __init__(self, display_width, ground_y):
        self.__ground_pieces = []
        self.__display_width = display_width
        self.__y = ground_y

    def move_grounds(self):
        pass

    def get_images(self):
        return self.__ground_pieces
