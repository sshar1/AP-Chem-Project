import sys
import time
import pygame
import os

from level import Level

class Game:
    def __init__(self):

        # Pygame Setup
        pygame.init()
        self.screen = pygame.display.set_mode((1074, 597)) # 1074, 597
        pygame.display.set_caption("The Legend Of Sodium")
        self.start_screen = pygame.image.load(os.path.join('images', 'startScreen.png')).convert()

        self.clock = pygame.time.Clock()

        self.level = Level()

    def start(self):
        pygame.mixer.music.load(os.path.join('music', 'start.mp3'))
        pygame.mixer.music.play(-1)

        dt = 0
        dt_sum = 0
        space = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                pygame.mixer.music.load(os.path.join('music', 'click.mp3'))
                pygame.mixer.music.play()
                space = True

            # Wait 4 seconds after pressing space before starting game
            if space:
                dt_sum += dt
                if dt_sum > 4: break

            dt = self.clock.tick(60) / 1000

            self.screen.blit(self.start_screen, (0, 0))
            pygame.display.update()

        pygame.mixer.music.load(os.path.join('music', 'background.mp3'))
        pygame.mixer.music.play(-1)

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
    game.start()
    game.run()