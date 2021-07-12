import pygame
from game import Game

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
#pygame.mixer.init()
game = Game()
game.welcome()
