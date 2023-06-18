import random
import pygame
import os

class Electron(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.low_bound = 0
        self.up_bound = 2460
        self.pos = pygame.Vector2(random.randint(self.low_bound, self.up_bound), random.randint(self.low_bound, self.up_bound))

        self.image = pygame.image.load(os.path.join('images', 'electron.png')).convert_alpha()
        self.rect = self.image.get_rect(center = self.pos)
        self.hit_rect = self.rect.copy()

        self.direction = self.next_direction()
        self.speed = self.next_speed()
        self.dt_sum = 0

        self.dead = False

    def next_direction(self):
        direct = pygame.Vector2()
        while direct.magnitude() == 0:
            horizontal = random.randint(-1, 1)
            vertical = random.randint(-1, 1)
            direct = pygame.Vector2(horizontal, vertical)

        return direct.normalize()

    def next_speed(self):
        return random.randint(200, 350)
    
    # Every 5 seconds, get random direction and multiply by random speed. If 5 seconds passes or electron touches a boundary, get new random vectors
    def update(self, dt):
        self.dt_sum += dt

        # Runs every 5 seconds
        if self.dt_sum >= 5:
            self.direction = self.next_direction()
            self.speed = self.next_speed()
            self.dt_sum = 0

        self.pos.x += self.direction.x * self.speed * dt
        self.pos.y += self.direction.y * self.speed * dt

        if self.pos.x > self.up_bound or self.pos.x < self.low_bound or self.pos.y > self.up_bound or self.pos.y < self.low_bound:
            self.direction = self.next_direction()
            self.speed = self.next_speed()
            self.dt_sum = 0

            if self.pos.x > self.up_bound: self.pos.x = self.up_bound
            if self.pos.x < self.low_bound: self.pos.x = self.low_bound
            if self.pos.y > self.up_bound: self.pos.y = self.up_bound
            if self.pos.y < self.low_bound: self.pos.y = self.low_bound

        self.rect.center = self.pos

    def die(self):
        self.image = pygame.surface.Surface((0, 0))
        self.dead = True

    def update_hitbox(self, coords):
        self.hit_rect.topleft = coords