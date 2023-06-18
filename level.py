import pygame
import os
from heat import Heat
from player import Player
from electron import Electron
from ui import UI

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

        self.electrons = [Electron(self.enemy_sprites) for _ in range(6)]
        self.heats = [Heat(self.enemy_sprites) for _ in range(2)]

        self.ui = UI()

    def draw_enemies(self):

        for electron in self.electrons:
            if electron.dead:
                self.electrons[self.electrons.index(electron)] = Electron(self.enemy_sprites)

            x = electron.pos.x + self.player.bgX
            y = electron.pos.y + self.player.bgY
            rel_coords = pygame.Vector2(x, y)

            electron.update_hitbox(rel_coords)
            self.screen.blit(electron.image, rel_coords)

        for heat in self.heats:
            if heat.dead:
                self.heats[self.heats.index(heat)] = Heat(self.enemy_sprites)

            x = heat.pos.x + self.player.bgX
            y = heat.pos.y + self.player.bgY
            rel_coords = pygame.Vector2(x, y)

            heat.update_hitbox(rel_coords)
            self.screen.blit(heat.image, rel_coords)

    def run(self, dt):
        self.screen.blit(self.player.bg, (self.player.bgX, self.player.bgY))

        self.sprites.draw(self.screen)
        self.draw_enemies()

        self.sprites.update(self.screen, self.electrons, self.heats, self.ui, dt)

        if not self.player.answering_question:
            self.enemy_sprites.update(dt)

        self.ui.display(self.player)

        pygame.display.update()