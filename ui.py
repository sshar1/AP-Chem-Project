import os
import random
import pygame
import json

class UI:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.eUI = pygame.image.load(os.path.join('images', 'eConfigUI2.png')).convert_alpha()
        self.win_screen_img = pygame.image.load(os.path.join('images', 'winScreen.png')).convert_alpha()
        self.lose_screen_img = pygame.image.load(os.path.join('images', 'loseScreen.png')).convert_alpha()
        self.e_config_font = pygame.font.Font(None, 17)
        self.question_font = pygame.font.Font(None, 30) 
        self.answer_font = pygame.font.Font(None, 25) 

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

    def get_response_color(self):
        if 'Correct :)' in self.response:
            return 'green'
        elif 'Wrong!' in self.response:
            return 'red'
        else:
            return 'white'

    # Return 1 2 3 4 depending on correct answer
    def get_answer(self):
        return self.letters.index(self.questions[self.current_question_index]['correct']) + 1

    def set_response(self, response):
        self.response = response

    def blit_text(self, surface, text, pos, font, color=pygame.Color('white')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width = self.question_rect.topright[0] - 20
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

    # Displays the question
    def display_question(self):
        # Background
        pygame.draw.rect(self.screen, self.question_bgcolor, self.question_rect)

        # Question
        txt = self.questions[self.current_question_index]['question']
        self.blit_text(self.screen, txt, self.question_rect.topleft + pygame.Vector2(15, 15), self.question_font)

        # Answers
        for i in range(4):
            answer_letter = self.index_to_letter(i)
            txt = answer_letter + '.  ' + self.questions[self.current_question_index][answer_letter]
            self.blit_text(self.screen, txt, self.question_rect.topleft + pygame.Vector2(15, 150 + i * 70), self.answer_font)

        # Status (right or wrong)
        response_surf = self.question_font.render(self.response, True, self.get_response_color())
        response_txt_rect = response_surf.get_rect(topleft = self.question_rect.topleft + pygame.Vector2(15, 100))
        self.screen.blit(response_surf, response_txt_rect)

    def display_e_config(self, player):
        text_surf = self.e_config_font.render(self.e_configs[player.electrons], False, 'black')
        text_rect = text_surf.get_rect(bottomleft = (68, self.screen.get_height() - 45))

        self.screen.blit(text_surf, text_rect)

    def display_heat(self, player):
        text_surf = self.e_config_font.render("Heats: " + str(player.heats), False, 'black')
        text_rect = text_surf.get_rect(bottomleft = (68, self.screen.get_height() - 33))

        self.screen.blit(text_surf, text_rect)

    def win_screen(self):
        self.screen.blit(self.win_screen_img, (0, 0))

    def lose_screen(self):
        self.screen.blit(self.lose_screen_img, (0, 0))

    def display(self, player):
        self.screen.blit(self.eUI, (10, self.screen.get_height() - 90))

        self.display_e_config(player)
        self.display_heat(player)