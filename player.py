import math
import time
import pygame
import os

# TODO when moving up/down from rest, movement may be jittery for some moments. This is a result of the bobbing with sin. When pressing W and S at the same time, you go up and down

class Player (pygame.sprite.Sprite):

    def __init__(self, pos, bg, bgX, bgY, groups):
        super().__init__(groups)
        self.pos = pos
        self.image = pygame.image.load(os.path.join('images', 'player5.png')).convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.directionVector = pygame.math.Vector2(0, 0)

        self.bg = bg
        self.bgX = bgX
        self.bgY = bgY

        self.eUI = pygame.image.load(os.path.join('images', 'eConfigUI2.png')).convert_alpha()

        self.electrons = 0

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

    def update(self, screen, dt):
        # Camera scrolling logic
        keys = pygame.key.get_pressed()
        self.directionVector = pygame.math.Vector2(0, 0)

        if keys[pygame.K_w] or keys[pygame.K_s]:
            self.directionVector.y = 1
        if keys[pygame.K_a] or keys[pygame.K_d]:
            self.directionVector.x = 1

        if self.directionVector.magnitude() != 0:
            self.directionVector = self.directionVector.normalize()

        # W is pressed
        if keys[pygame.K_w]:
            if self.pos.y > screen.get_height() / 2:
                self.pos.y -= 200 * dt * self.directionVector.y
                cam_speed = 0
                if self.pos.y <= screen.get_height() / 2:
                    self.pos.y = screen.get_height() / 2
            else:
                cam_speed = 300
            self.bgY += cam_speed * dt * self.directionVector.y
            if self.bgY >= 0:
                self.bgY = 0
                self.pos.y -= cam_speed * dt * self.directionVector.y
                if self.pos.y - self.image.get_width() / 2 <= 0:
                    self.pos.y = self.image.get_width() / 2

        # S is pressed
        if keys[pygame.K_s]:
            if self.pos.y < screen.get_height() / 2: 
                self.pos.y += 200 * dt * self.directionVector.y
                cam_speed = 0
                if self.pos.y >= screen.get_height() / 2:
                    self.pos.y = screen.get_height() / 2
            else:
                cam_speed = 300
            self.bgY -= cam_speed * dt * self.directionVector.y
            if self.bgY - screen.get_height() <= self.bg.get_height() * -1:
                self.bgY = screen.get_height() - self.bg.get_height()
                self.pos.y += cam_speed * dt * self.directionVector.y
                if self.pos.y + self.image.get_width() / 2 >= screen.get_height():
                    self.pos.y = screen.get_height() - self.image.get_width() / 2

        # A is pressed
        if keys[pygame.K_a]:
            if self.pos.x > screen.get_width() / 2:
                self.pos.x -= 200 * dt * self.directionVector.x
                cam_speed = 0
                if self.pos.x <= screen.get_width() / 2:
                    self.pos.x = screen.get_width() / 2
            else:
                cam_speed = 300
            self.bgX += cam_speed * dt * self.directionVector.x
            if self.bgX >= 0:
                self.bgX = 0
                self.pos.x -= cam_speed * dt * self.directionVector.x
                if self.pos.x - self.image.get_width() / 2 <= 0:
                    self.pos.x = self.image.get_width() / 2

        # D is pressed
        if keys[pygame.K_d]:
            if self.pos.x < screen.get_width() / 2: # if player is left of the center on the screen and they try to move right, move the player right until it's on the center
                self.pos.x += 200 * dt * self.directionVector.x
                cam_speed = 0
                if self.pos.x >= screen.get_width() / 2: # if player moves past the center of the screen, move them back to the center
                    self.pos.x = screen.get_width() / 2
            else:
                cam_speed = 300
            self.bgX -= cam_speed * dt * self.directionVector.x
            if self.bgX - screen.get_width() <= self.bg.get_width() * -1:
                self.bgX = screen.get_width() - self.bg.get_width()
                self.pos.x += cam_speed * dt * self.directionVector.x
                if self.pos.x + self.image.get_width() / 2 >= screen.get_width():
                    self.pos.x = screen.get_width() - self.image.get_width() / 2

        self.pos.y += math.sin(5 * time.time()) * 0.2
        self.rect.center = self.pos

        screen.blit(self.eUI, (10, screen.get_height() - (10 + 80)))

    def getEConfig(self):
        return self.e_configs[self.electrons]
