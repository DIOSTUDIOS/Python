import sys
import pygame


class Bullet:
    def __init__(self,plane_coord_x, plane_coord_y):
        self.coord_x = plane_coord_x
        self.coord_y = plane_coord_y
        self.image = pygame.image.load(r'images\bullet1.png')

    def move_up(self):
        self.coord_y -= 3
