import random
import pygame


class Apple:
    def __init__(self):
        self.direction_x = 0
        self.direction_y = 0
        self.apple = 10
        self.apple_pos_x = random.randrange(110, 690, 10)
        self.apple_pos_y = random.randrange(50, 550, 10)
        self.applebited = pygame.mixer.Sound('assets/applebite.ogg')
