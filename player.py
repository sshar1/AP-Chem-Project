import math
import time
import pygame
import os

class Player (pygame.sprite.Sprite):

    def __init__(self, pos, bg, bgX, bgY, groups):
        super().__init__(groups)
        self.pos = pos
        self.image = pygame.image.load(os.path.join('images', 'player5.png')).convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.directionVector = pygame.math.Vector2(0, 0)
        self.x_coord = 0
        self.y_coord = 0

        self.bg = bg
        self.bgX = bgX
        self.bgY = bgY

        self.electrons = 0
        self.max_electrons = 15

        self.answering_question = False
        self.dt_sum = 0
        self.question_input_received = False

    def question_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            return 1
        elif keys[pygame.K_2]:
            return 2
        elif keys[pygame.K_3]:
            return 3
        elif keys[pygame.K_4]:
            return 4

    def update(self, screen, electrons, ui, dt):

        # Question ui
        if self.answering_question:
            ui.display_question()
            if self.question_input() == ui.get_answer():
                if not self.question_input_received and self.electrons < self.max_electrons:
                    self.electrons += 1
                self.question_input_received = True
                ui.set_response('Correct :)')
            elif self.question_input() is not None and self.question_input() in [1, 2, 3, 4]:
                self.question_input_received = True
                ui.set_response('Wrong!')
            
            if self.question_input_received:
                # Wait 2 seconds
                self.dt_sum += dt
                if self.dt_sum >= 2:
                    self.question_input_received = False
                    self.dt_sum = 0
                    self.answering_question = False
            return

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

        if self.directionVector.y == 0:
            self.pos.y += math.sin(5 * time.time()) * 0.2

        self.rect.center = self.pos

        self.x_coord = -self.bgX + self.pos.x
        self.y_coord = -self.bgY + self.pos.y

        self.check_collisions(electrons, ui)

    def check_collisions(self, electrons, ui):
        for electron in electrons:
            if self.rect.colliderect(electron.hit_rect) and not electron.dead:
                electron.kill()
                electron.die()
                if self.electrons < self.max_electrons:
                    ui.get_question()
                    self.answering_question = True
                else:
                    print('max electrons obtained')
