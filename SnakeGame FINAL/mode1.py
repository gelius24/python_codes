import pygame
from snake import Snake
from apple import Apple
import random
import sys


class Mode1:
    def __init__(self, game):
        self.game = game
        self.score = 0
        self.snake = Snake()
        self.apple = Apple()
        self.in_game = True
        pygame.mixer.music.load("assets/bgmusic.ogg")
        self.ecran = pygame.display.set_mode((800, 600))

    def draw_game(self):
        self.ecran.fill((0, 0, 0))
#        pygame.draw.rect(self.self.ecran, (0, 255, 0), (self.snake.pos_x, self.snake.pos_y, self.snake.serpent_body, self.snake.serpent_body))
        self.ecran.blit(self.snake.snake_head_img, (self.snake.pos_x, self.snake.pos_y, self.snake.serpent_body, self.snake.serpent_body))
        pygame.draw.rect(self.ecran, (255, 0, 0), (self.apple.apple_pos_x, self.apple.apple_pos_y, self.apple.apple, self.apple.apple))
        self.border()
# afficher le corp du serpent
        for part in self.snake.snake_body_positions[:-1]:
            pygame.draw.rect(self.game.ecran, (0, 255, 0), (part[0], part[1], self.snake.serpent_body, self.snake.serpent_body))
            pygame.draw.line(self.game.ecran, (0, 0, 0), part, (part[0] + 10, part[1]))
            pygame.draw.line(self.game.ecran, (0, 0, 0), part, (part[0], part[1] + 10))

    def border(self):
        pygame.draw.rect(self.ecran, (255, 255, 255), (100, 50, 600, 500), 3)

    def mode1_start(self):
        pygame.mixer.music.play(-1)
        del self.snake
        self.snake = Snake()
        while self.in_game:
            clock = pygame.time.Clock()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.up()
                    elif event.key == pygame.K_DOWN:
                        self.snake.down()
                    elif event.key == pygame.K_RIGHT:
                        self.snake.right()
                    elif event.key == pygame.K_LEFT:
                        self.snake.left()
            if self.apple.apple_pos_x == self.snake.pos_x and self.apple.apple_pos_y == self.snake.pos_y:
                self.apple.apple_pos_x = random.randrange(110, 690, 10)
                self.apple.apple_pos_y = random.randrange(50, 550, 10)
                self.snake.snake_size += 1
                self.score += 1
                self.apple.applebited.play()

            if self.snake.bit:
                self.snake.bited_sound.play()

            if self.snake.pos_x < 99 or self.snake.pos_x > 700 or self.snake.pos_y < 50 or self.snake.pos_y > 550 or self.snake.bit:
                self.in_game = False
                self.score = 0
                self.game.welcome_window = True
                pygame.mixer.music.stop()

            self.border()
            self.snake.head_positions = []
            self.snake.head_positions.append(self.snake.pos_x)
            self.snake.head_positions.append(self.snake.pos_y)
            self.snake.snake_body_positions.append(self.snake.head_positions)

            if len(self.snake.snake_body_positions) > self.snake.snake_size:
                self.snake.snake_body_positions.pop(0)

            self.draw_game()
            self.snake.snake_mouvements()
            self.snake.bited(self.snake.head_positions)

            self.game.msg(pygame.font.SysFont('Lato', 30, False), 'Snake Game', (320, 10, 100, 50), (255, 255, 255))
            self.game.msg(pygame.font.SysFont('Lato', 30, False), '{}'.format(str(self.score)), (375, 30, 50, 50), (255, 255, 255))
            clock.tick(20)
            pygame.display.flip()
