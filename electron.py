import random
import pygame
import os

class Electron(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.low_bound = 20
        self.up_bound = 2480
        self.pos = pygame.Vector2(random.randint(self.low_bound, self.up_bound), random.randint(self.low_bound, self.up_bound))
        # self.pos = pygame.Vector2(100, 100)

        self.image = pygame.image.load(os.path.join('images', 'electron.png')).convert_alpha()
        self.rect = self.image.get_rect(center = self.pos)

        self.direction = self.next_direction()
        self.speed = 0
        self.dt_sum = 0

    def next_direction(self):
        horizontal = random.randint(-1, 1)
        vertical = random.randint(-1, 1)
        direct = pygame.Vector2(horizontal, vertical)

        if direct.magnitude() != 0:
            return direct.normalize()
        return direct

    def next_speed(self):
        return random.randint(150, 300)
    
    # Every 5 seconds, get random direction and multiply by random speed. If 5 seconds passes or electron touches a boundary, get new random vectors
    def update(self, dt):
        self.dt_sum += dt

        # Runs every 5 seconds
        if self.dt_sum >= 5:
            self.direction = self.next_direction()
            self.speed = self.next_speed() * dt
            self.dt_sum = 0

        self.pos.x += self.direction.x * self.speed
        self.pos.y += self.direction.y * self.speed

        if self.pos.x > self.up_bound or self.pos.x < self.low_bound or self.pos.y > self.up_bound or self.pos.y < self.low_bound:
            self.direction = self.next_direction()
            self.speed = self.next_speed() * dt
            self.dt_sum = 0
            return

        self.rect.center = self.pos
