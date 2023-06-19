import random
import pygame
import os

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, image, min_speed, max_speed, player, update_time):
        super().__init__(groups)

        self.screen = pygame.display.get_surface()

        self.low_bound = 0
        self.up_bound = 2500 - image.get_width()
        self.pos = self.next_pos()
        self.teleport(player) # Make sure position is off screen of player camera

        self.image = image
        self.rect = self.image.get_rect(center = self.pos)
        self.hit_rect = self.rect.copy()

        self.min_speed = min_speed
        self.max_speed = max_speed
        self.update_time = update_time

        self.direction = self.next_direction()
        self.speed = self.next_speed()
        self.dt_sum = 0

        self.dead = False

    # Teleports enemy to random position that is out of range of player
    def teleport(self, player):
        minX = int(-player.bgX)
        maxX = int(-player.bgX + self.screen.get_width())
        minY = int(-player.bgY)
        maxY = int(-player.bgY + self.screen.get_height())

        pos = self.next_pos()

        while (pos.x in range(minX, maxX) or pos.y in range(minY, maxY)):
            pos = self.next_pos()

        self.pos = pos

    def next_pos(self):
        return pygame.Vector2(random.randint(self.low_bound, self.up_bound), random.randint(self.low_bound, self.up_bound))

    def next_direction(self):
        direct = pygame.Vector2()
        while direct.magnitude() == 0:
            horizontal = random.randint(-1, 1)
            vertical = random.randint(-1, 1)
            direct = pygame.Vector2(horizontal, vertical)

        return direct.normalize()

    def next_speed(self):
        return random.randint(self.min_speed, self.max_speed)
    
    # Every updaate_time seconds, get random direction and multiply by random speed. If update_time seconds passes or sprite touches a boundary, get new random vectors
    def update(self, dt):
        self.dt_sum += dt

        # Runs every update_time seconds
        if self.dt_sum >= self.update_time:
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
        self.kill()

    def update_hitbox(self, coords):
        self.hit_rect.topleft = coords