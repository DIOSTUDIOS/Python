import sys
import pygame
from weapon import Bullet
import random


class Plane:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.is_destroyed = False
        self.is_attacked = False
        self.health = 100

    def move_up(self):
        self.coord_y -= 1

    def move_down(self):
        self.coord_y += 3

    def move_left(self):
        self.coord_x -= 5

    def move_right(self):
        self.coord_x += 5

    def check_border(self):
        if self.coord_x <= 0:
            self.coord_x =0
        elif self.coord_x >= 378:
            self.coord_x = 378
        elif self.coord_y >= 958:
            self.coord_y = 0
        else:
            pass

    def check_crash(self):
        pass

    def be_destroyed(self):
        self.is_destroyed = True

    def be_attacked(self):
        self.is_attacked = True


class Hero(Plane):
    def __init__(self):
        self.coord_x = 189
        self.coord_y = 564
        self.is_flying = True
        self.image = [
            pygame.image.load(r'images\hero\hero_1.png'),
            pygame.image.load(r'images\hero\hero_2.png'),
            pygame.image.load(r'images\hero\be_destroyed_1.png'),
            pygame.image.load(r'images\hero\be_destroyed_2.png'),
            pygame.image.load(r'images\hero\be_destroyed_3.png'),
            pygame.image.load(r'images\hero\be_destroyed_4.png')
        ]

    def display(self, forms):
        forms.blit(self.image[self.is_flying], (self.coord_x, self.coord_y))
        self.is_flying = not self.is_flying


class Soldier(Plane):
    def __init__(self):
        self.coord_x = random.randint(0, 423)
        self.coord_y = -43
        self.health = 10
        self.image = [
            pygame.image.load(r'images\enemy\soldier\soldier.png'),
            pygame.image.load(r'images\enemy\soldier\be_destroyed_1.png'),
            pygame.image.load(r'images\enemy\soldier\be_destroyed_2.png'),
            pygame.image.load(r'images\enemy\soldier\be_destroyed_3.png'),
            pygame.image.load(r'images\enemy\soldier\be_destroyed_4.png')
        ]

    def display(self, forms):
        forms.blit(self.image[0], (self.coord_x, self.coord_y))


class Captain(Plane):
    def __init__(self):
        self.health = 50
        self.image = [
            pygame.image.load(r'images\enemy\captain\captain.png'),
            pygame.image.load(r'images\enemy\captain\be_destroyed_1.png'),
            pygame.image.load(r'images\enemy\captain\be_destroyed_2.png'),
            pygame.image.load(r'images\enemy\captain\be_destroyed_3.png'),
            pygame.image.load(r'images\enemy\captain\be_destroyed_4.png')
        ]


class General(Plane):
    def __init__(self):
        self.health = 100
        self.image = [
            pygame.image.load(r'images\enemy\general\general.png'),
            pygame.image.load(r'images\enemy\general\be_destroyed_1.png'),
            pygame.image.load(r'images\enemy\general\be_destroyed_2.png'),
            pygame.image.load(r'images\enemy\general\be_destroyed_3.png'),
            pygame.image.load(r'images\enemy\general\be_destroyed_4.png'),
            pygame.image.load(r'images\enemy\general\be_destroyed_5.png'),
            pygame.image.load(r'images\enemy\general\be_destroyed_6.png')
        ]
