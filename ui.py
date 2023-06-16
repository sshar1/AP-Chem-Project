import os
import pygame

class UI:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.eUI = pygame.image.load(os.path.join('images', 'eConfigUI2.png')).convert_alpha()
        self.e_config_font = pygame.font.Font(None, 17)
        self.question_font = pygame.font.Font(None, 40)

        self.question_rect = pygame.Rect(50, 50, 750, 400)
        self.question_rect.center = (self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.question_bgcolor = pygame.Color(50, 50, 50)

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

    # This gets a random question from json
    def get_question(self):
        pass

    # This displays that question
    def display_question(self):
        # Background
        pygame.draw.rect(self.screen, self.question_bgcolor, self.question_rect)

        # Question
        question_surf = self.question_font.render('This is a sample question?', True, 'white')
        question_txt_rect = question_surf.get_rect(topleft = self.question_rect.topleft + pygame.Vector2(15, 15))
        self.screen.blit(question_surf, question_txt_rect)

        # Answers
        for i in range(4):
            answer_surf = self.question_font.render(str(i + 1) + '.  My sample answer', True, 'white')
            answer_txt_rect = answer_surf.get_rect(topleft = self.question_rect.topleft + pygame.Vector2(15, 150 + i * 50))
            self.screen.blit(answer_surf, answer_txt_rect)

    # return 1 2 3 4
    def get_answer(self):
        return 1

    def display_answer(self, msg):
        print(msg)

    def display(self, player):

        text_surf = self.e_config_font.render(self.e_configs[player.electrons], False, 'black')
        text_rect = text_surf.get_rect(bottomleft = (68, self.screen.get_height() - 39))

        self.screen.blit(self.eUI, (10, self.screen.get_height() - 90))
        self.screen.blit(text_surf, text_rect)
        # self.create_question()

