import glob
import os
import random

from Ground.GroundPiece import GroundPiece


# The ground which the dino and obstacles are moving on is made out of several ground images (ground_pieces).
# GroundGenerator is for creating enough such ground_pieces for displaying a continuous ground.
class GroundGenerator:
    __sprite_paths = [f for f in glob.glob(os.path.join("sprites", "ground", "*.png"))]

    def __init__(self, display_width, ground_y):
        self.__display_width = display_width
        self.__y = ground_y
        self.__ground_pieces = [GroundPiece(0, self.__y, GroundGenerator.__sprite_paths[0])]

    def move_grounds(self):
        self.__fill_ground_pieces()

        for ground_piece in self.__ground_pieces:
            ground_piece.moveLeft()

    # create new ground_pieces if needed.
    def __fill_ground_pieces(self):
        # new ground_pieces are needed if last ground_piece in the ground_pieces list exceeds
        # the right side of the display with its right edge (ground_pieces move left)
        last_ground_piece = self.__ground_pieces[-1]
        # x coordinate of the right edge of last ground_piece
        last_ground_piece_right_x = last_ground_piece.get_x() + last_ground_piece.get_image().get_width()

        while last_ground_piece_right_x < self.__display_width:
            image_path = GroundGenerator.__sprite_paths[random.randint(0, len(GroundGenerator.__sprite_paths) - 1)]
            self.__ground_pieces.append(GroundPiece(last_ground_piece_right_x, self.__y, image_path))

            last_ground_piece = self.__ground_pieces[-1]
            last_ground_piece_right_x = last_ground_piece.get_x() + last_ground_piece.get_image().get_width()

    def get_images(self):
        return self.__ground_pieces
