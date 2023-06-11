import pygame
import os
from player import Player

class Level:
    def __init__(self):

        self.screen = pygame.display.get_surface()
        self.sprites = pygame.sprite.Group()

        # Background (5000 x 5000) and Cam Setup
        self.bg = pygame.image.load(os.path.join('images', 'background2.png')).convert()
        self.cam_speed = 300

        player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2) 
        bgX, bgY = 0, 0
        self.player = Player(player_pos, self.bg, bgX, bgY, self.sprites)

    def run(self, dt):
        self.screen.blit(self.player.bg, (self.player.bgX, self.player.bgY))
        self.sprites.draw(self.screen)
        self.sprites.update(self.screen, dt)
        pygame.display.update()