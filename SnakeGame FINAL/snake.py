import pygame


class Snake:
    def __init__(self):
        self.pos_x = 300
        self.pos_y = 300
        self.direction_x = 0
        self.direction_y = 0
        self.serpent_body = 10
        self.snake_body_positions = []
        self.snake_size = 1
        self.bit = False
        self.bited_sound = pygame.mixer.Sound('assets/bit_sound.ogg')
        self.snake_head_img = pygame.image.load("assets/snake_head.png")

    def snake_mouvements(self):
        self.pos_x += self.direction_x
        self.pos_y += self.direction_y

    def up(self):
        self.direction_y = -10
        self.direction_x = 0

    def down(self):
        self.direction_y = 10
        self.direction_x = 0

    def right(self):
        self.direction_x = 10
        self.direction_y = 0

    def left(self):
        self.direction_x = -10
        self.direction_y = 0

    def bited(self, snake_head_positions):
        for part in self.snake_body_positions[:-1]:
            if snake_head_positions == part:
                self.bit = True
