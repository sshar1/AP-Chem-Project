import pygame
import os

from enemy import Enemy

class Electron(Enemy):
    def __init__(self, groups):
        super().__init__(groups, pygame.image.load(os.path.join('images', 'electron.png')).convert_alpha(), 200, 350, 5)