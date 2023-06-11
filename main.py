import sys
import pygame
import os

from level import Level

class Game:
    def __init__(self):

        # Pygame Setup
        pygame.init()
        self.screen = pygame.display.set_mode((1074, 597)) 
        pygame.display.set_caption("The Legend Of Sodium")
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        running = True
        dt = 0

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False
                    pygame.quit()
                    sys.exit()
            self.level.run(dt)

            # this gets the amount of time since it was last called in seconds with 60 fps
            dt = self.clock.tick(60) / 1000

if __name__ == '__main__':
    game = Game()
    game.run()