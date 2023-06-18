import random
import pygame
import os

from enemy import Enemy

class Heat(Enemy):
    def __init__(self, groups):
        super().__init__(groups, pygame.image.load(os.path.join('images', 'heat2.png')).convert_alpha(), 400, 550, 3)