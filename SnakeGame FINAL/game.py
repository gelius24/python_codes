import pygame
from mode1 import Mode1
from mode_2.mode2 import Mode2
from speed_mode import SpeedMode
import sys


sys.path.insert(1, 'mode_2/mode2.py')


class Game:
    def __init__(self):
        self.ecran = pygame.display.set_mode((800, 600))
        self.welcome_window = True
        self.welcome()

    def mode1_on(self):
        mode1 = Mode1(self)
        mode1.mode1_start()

    def mode2_on(self):
        mode2 = Mode2(self)
        mode2.main()

    def welcome(self):
        while self.welcome_window:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.welcome_window = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.mode2_on()
                    if event.key == pygame.K_2:
                        self.mode1_on()
                    if event.key == pygame.K_3:
                        speedm = SpeedMode(self)
                        speedm.speedm_start()

            self.ecran.fill((0, 0, 0))
            self.msg(pygame.font.SysFont('Lato', 20, False), 'Vous devez dévlopper le serpent !', (270, 200, 200, 5), (240, 240, 240))
            self.msg(pygame.font.SysFont('Lato', 20, False), 'Mangez autant de pomme que possible.', (270, 220, 200, 5), (240, 240, 240))
            self.msg(pygame.font.SysFont('Lato', 30, False), 'Tapez sur la toucher 1 pour le mode CUBIC.', (180, 420, 200, 5), (255, 255, 255))
            self.msg(pygame.font.SysFont('Lato', 30, False), 'Tapez sur la toucher 2 pour le mode NON-CUBIC.', (180, 450, 200, 5), (255, 255, 255))
            self.msg(pygame.font.SysFont('Lato', 30, False), 'Tapez sur la toucher 3 pour le mode NON-CUBIC Rapide.', (180, 480, 200, 5), (255, 255, 255))
            pygame.display.flip()

    def msg(self, font, message, message_rect, couleur):
        message = font.render(message, True, couleur)
        self.ecran.blit(message, message_rect)
