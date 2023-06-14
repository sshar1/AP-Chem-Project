import pygame
import os
from player import Player
from electron import Electron

class Level:
    def __init__(self):

        self.screen = pygame.display.get_surface()
        self.sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        # Background (2500 x 2500) and Cam Setup
        self.bg = pygame.image.load(os.path.join('images', 'background2.png')).convert()
        self.cam_speed = 300

        player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2) 
        bgX, bgY = 0, 0
        self.player = Player(player_pos, self.bg, bgX, bgY, self.sprites)

        self.electrons = [Electron(self.enemy_sprites) for _ in range(8)]

    def run(self, dt):
        self.screen.blit(self.player.bg, (self.player.bgX, self.player.bgY))

        self.sprites.draw(self.screen)
        self.enemy_sprites.draw(self.player.bg)

        print(self.player.x_coord, self.player.y_coord)

        self.sprites.update(self.screen, dt)
        self.enemy_sprites.update(dt)

        pygame.display.update()