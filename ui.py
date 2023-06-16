import os
import random
import pygame
import json

class UI:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.eUI = pygame.image.load(os.path.join('images', 'eConfigUI2.png')).convert_alpha()
        self.e_config_font = pygame.font.Font(None, 17)
        self.question_font = pygame.font.Font(None, 40)

        self.question_rect = pygame.Rect(50, 50, 750, 400)
        self.question_rect.center = (self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.question_bgcolor = pygame.Color(50, 50, 50)

        f = open('questions.json')
        self.questions = json.load(f)['questions']

        self.current_question_index = 0
        self.response = ""

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

        self.letters = ['a', 'b', 'c', 'd']

    def index_to_letter(self, index):
        return self.letters[index]

    # This gets a random question from json. Called once when player collides with electron
    def get_question(self):
        self.current_question_index = random.randint(0, len(self.questions) - 1)
        self.response = ""

    # This displays that question
    def display_question(self):
        # Background
        pygame.draw.rect(self.screen, self.question_bgcolor, self.question_rect)

        # Question
        question_text = self.questions[self.current_question_index]['question']
        question_surf = self.question_font.render(question_text, True, 'white')
        question_txt_rect = question_surf.get_rect(topleft = self.question_rect.topleft + pygame.Vector2(15, 15))
        self.screen.blit(question_surf, question_txt_rect)

        # Answers
        for i in range(4):
            answer_letter = self.index_to_letter(i)
            answer_text = self.questions[self.current_question_index][answer_letter]
            answer_surf = self.question_font.render(answer_letter + '.  ' + answer_text, True, 'white')
            answer_txt_rect = answer_surf.get_rect(topleft = self.question_rect.topleft + pygame.Vector2(15, 150 + i * 50))
            self.screen.blit(answer_surf, answer_txt_rect)

        # Status (right or wrong)
        color = ''
        if self.response == 'Correct :)':
            color = 'green'
        elif self.response == 'Wrong!':
            color = 'red'
        else:
            color = 'white'
        response_surf = self.question_font.render(self.response, True, color)
        response_txt_rect = question_surf.get_rect(topleft = self.question_rect.topleft + pygame.Vector2(15, 70))
        self.screen.blit(response_surf, response_txt_rect)

    # return 1 2 3 4 depending on correct answer
    def get_answer(self):
        return self.letters.index(self.questions[self.current_question_index]['correct']) + 1

    def set_response(self, response):
        self.response = response

    def display(self, player):

        text_surf = self.e_config_font.render(self.e_configs[player.electrons], False, 'black')
        text_rect = text_surf.get_rect(bottomleft = (68, self.screen.get_height() - 39))

        self.screen.blit(self.eUI, (10, self.screen.get_height() - 90))
        self.screen.blit(text_surf, text_rect)
        # self.create_question()

