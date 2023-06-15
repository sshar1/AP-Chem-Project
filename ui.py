import os
import pygame

class UI:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.eUI = pygame.image.load(os.path.join('images', 'eConfigUI2.png')).convert_alpha()
        self.font = pygame.font.Font(None, 17)

        self.e_configs = [
            '-',
            '1s^1',
            '1s^2',
            '1s^2 2s^1',
            '1s^2 2s^2',
            '1s^2 2s^2 2p^1',
            '1s^2 2s^2 2p^2',
            '1s^2 2s^2 2p^3',
            '1s^2 2s^2 2p^4',
            '1s^2 2s^2 2p^5',
            '1s^2 2s^2 2p^6',
            '1s^2 2s^2 2p^6 3s^1',
            '1s^2 2s^2 2p^6 3s^2',
            '1s^2 2s^2 2p^6 3s^2 3p^1',
            '1s^2 2s^2 2p^6 3s^2 3p^2',
            '1s^2 2s^2 2p^6 3s^2 3p^3'
        ]

    def display(self, player):

        text_surf = self.font.render(self.e_configs[player.electrons], False, 'black')
        text_rect = text_surf.get_rect(bottomleft = (68, self.screen.get_height() - 39))

        self.screen.blit(self.eUI, (10, self.screen.get_height() - 90))
        self.screen.blit(text_surf, text_rect)

