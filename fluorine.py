import pygame
import os

from enemy import Enemy

class Fluorine(Enemy):
    def __init__(self, groups):
        super().__init__(groups, pygame.image.load(os.path.join('images', 'fluorine.png')).convert_alpha(), 50, 100, 10)

    # Teleports fluorine to random position off screen
    def teleport(self):
        pass