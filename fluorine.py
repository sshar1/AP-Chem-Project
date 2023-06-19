import random
import pygame
import os

from enemy import Enemy

class Fluorine(Enemy):
    def __init__(self, player, groups):
        super().__init__(groups, pygame.image.load(os.path.join('images', 'fluorine.png')).convert_alpha(), 50, 100, player, 10)
        self.hit_rect.inflate(-30, -30)