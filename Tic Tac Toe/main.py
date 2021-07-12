import pygame
import time


pygame.init()
window = pygame.display.set_mode((720, 720))
colones = 3
pygame.display.set_caption('TicTacToe - WOODY GELIUS')
x_sound = pygame.mixer.Sound('drawX.ogg')
cx_up_left = False
cx_up_middle = False
cx_up_right = False
cx_middle_middle = False
cx_middle_left = False
cx_middle_right = False
cx_dwn_left = False
cx_dwn_middle = False
cx_dwn_right = False
co_up_left = True
co_up_middle = False
co_up_right = False
co_middle_right = False
co_middle_middle = False
co_middle_left = False
co_dwn_left = False
co_dwn_middle = False
co_dwn_right = False
player1 = True
player2 = False


def draw_grid():
    quotient = 720 // colones
    # Starting points
    x = 0
    y = 0

    for i in range(4):
        x = i * quotient
        if x == 240 or x == 480:
            pygame.draw.line(window, (255, 255, 255), (x, 0), (x, 720), 3)
            pygame.draw.line(window, (255, 255, 255), (0, x), (720, x), 3)


def start_setting():
    global cx_middle_left, cx_middle_middle, cx_middle_right, cx_up_left, cx_up_middle, cx_up_right, cx_dwn_left, \
        cx_dwn_middle, cx_dwn_right, co_up_left, co_up_middle, co_up_right, co_up_middle, co_middle_middle, co_middle_right, co_middle_left, \
        co_up_left, co_dwn_left, co_dwn_middle, co_dwn_right
    pygame.Surface.fill(window, (0, 0, 0))
    draw_grid()
    cx_up_left = False
    cx_up_middle = False
    cx_up_right = False
    cx_middle_middle = False
    cx_middle_left = False
    cx_middle_right = False
    cx_dwn_left = False
    cx_dwn_middle = False
    cx_dwn_right = False
    co_up_left = True
    co_up_middle = False
    co_up_right = False
    co_middle_right = False
    co_middle_middle = False
    co_middle_left = False
    co_dwn_left = False
    co_dwn_middle = False
    co_dwn_right = False
    main()


def draw_x():
    # LIGNE MILLIEU
    global cx_middle_left, cx_middle_middle, cx_middle_right, cx_up_left, cx_up_middle, cx_up_right, cx_dwn_left, \
        cx_dwn_middle, cx_dwn_right, player1, player2
    x, y = pygame.mouse.get_pos()
    if x < 240 and y < 240:
        # x_sound.play()
        pygame.draw.line(window, (255, 255, 255), (3, 6), (237, 237), 3)
        pygame.draw.line(window, (255, 255, 255), (237, 6), (2, 232), 3)
        cx_up_left = True
        player1 = False
        player2 = True

    if 480 > x > 240 > y:
        # x_sound.play()
        pygame.draw.line(window, (255, 255, 255), (243, 6), (473, 237), 3)
        pygame.draw.line(window, (255, 255, 255), (473, 6), (243, 237), 3)
        cx_up_middle = True
        player1 = False
        player2 = True

    if 480 < x and y < 240:
        # x_sound.play()
        pygame.draw.line(window, (255, 255, 255), (485, 6), (717, 237), 3)
        pygame.draw.line(window, (255, 255, 255), (717, 6), (485, 237), 3)
        cx_up_right = True
        player1 = False
        player2 = True

    if 480 > x > 240 and 480 > y > 240:
        # x_sound.play()
        pygame.draw.line(window, (255, 255, 255), (250, 250), (460, 460), 3)
        pygame.draw.line(window, (255, 255, 255), (460, 250), (250, 460), 3)
        cx_middle_middle = True
        player1 = False
        player2 = True

    if x < 240 < y < 480:
        # x_sound.play()
        pygame.draw.line(window, (255, 255, 255), (10, 250), (230, 460), 3)
        pygame.draw.line(window, (255, 255, 255), (3, 460), (230, 250), 3)
        cx_middle_left = True
        player1 = False
        player2 = True

    if x > 480 > y > 240:
        # x_sound.play()
        pygame.draw.line(window, (255, 255, 255), (485, 250), (717, 460), 3)
        pygame.draw.line(window, (255, 255, 255), (717, 250), (483, 460), 3)
        cx_middle_right = True
        player1 = False
        player2 = True

    if 240 > x and y > 480:
        pygame.draw.line(window, (255, 255, 255), (6, 485), (237, 717), 3)
        pygame.draw.line(window, (255, 255, 255), (237, 485), (6, 717), 3)
        cx_dwn_left = True
        player1 = False
        player2 = True

    if 240 < x < 480 < y:
        pygame.draw.line(window, (255, 255, 255), (243, 485), (473, 717), 3)
        pygame.draw.line(window, (255, 255, 255), (473, 485), (243, 717), 3)
        cx_dwn_middle = True
        player1 = False
        player2 = True

    if 480 < x and y > 480:
        pygame.draw.line(window, (255, 255, 255), (485, 485), (717, 717), 3)
        pygame.draw.line(window, (255, 255, 255), (717, 485), (485, 717), 3)
        cx_dwn_right = True
        player1 = False
        player2 = True


def draw_o():
    global co_up_left, co_up_middle, co_up_right, co_up_middle, co_middle_middle, co_middle_right, co_middle_left, \
        co_up_left, co_dwn_left, co_dwn_middle, co_dwn_right, player1, player2
    x, y = pygame.mouse.get_pos()
    if 480 < x and y < 240:
        pygame.draw.circle(window, (255, 255, 255), (600, 120), 100, 3)
        co_up_right = True
        player1 = True
        player2 = False

    if 480 > x > 240 > y:
        pygame.draw.circle(window, (255, 255, 255), (360, 120), 100, 3)
        co_up_middle = True
        player1 = True
        player2 = False

    if x < 240 and y < 240:
        pygame.draw.circle(window, (255, 255, 255), (120, 120), 100, 3)
        co_up_left = True
        player1 = True
        player2 = False

    if x > 480 > y > 240:
        pygame.draw.circle(window, (255, 255, 255), (600, 360), 100, 3)
        co_middle_right = True
        player1 = True
        player2 = False

    if 480 > x > 240 and 480 > y > 240:
        # x_sound.play()
        pygame.draw.circle(window, (255, 255, 255), (360, 360), 100, 3)
        co_middle_middle = True
        player1 = True
        player2 = False

    if x < 240 < y < 480:
        pygame.draw.circle(window, (255, 255, 255), (120, 360), 100, 3)
        co_middle_left = True
        player1 = True
        player2 = False

    if 240 > x and y > 480:
        pygame.draw.circle(window, (255, 255, 255), (120, 600), 100, 3)
        co_dwn_left = True
        player1 = True
        player2 = False

    if 240 < x < 480 < y:
        pygame.draw.circle(window, (255, 255, 255), (360, 600), 100, 3)
        co_dwn_middle = True
        player1 = True
        player2 = False

    if 480 < x and y > 480:
        pygame.draw.circle(window, (255, 255, 255), (600, 600), 100, 3)
        co_dwn_right = True
        player1 = True
        player2 = False


def main():
    while True:
        draw_grid()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if cx_up_left and cx_up_middle and cx_up_right or cx_middle_left and cx_middle_middle and cx_middle_right or \
                    cx_dwn_left and cx_dwn_middle and cx_dwn_right or cx_dwn_left and cx_middle_left and cx_up_left or \
                    cx_dwn_middle and cx_middle_middle and cx_up_middle or cx_dwn_right and cx_middle_right and cx_up_right \
                    or cx_up_left and cx_middle_middle and cx_dwn_right or cx_up_right and cx_middle_middle and cx_dwn_left:
                print("Player 1 WIN !!!")
                time.sleep(1)
                start_setting()
            elif co_up_left and co_up_middle and co_up_right or co_middle_left and co_middle_middle and co_middle_right or \
                    co_dwn_left and co_dwn_middle and co_dwn_right or co_dwn_left and co_middle_left and co_up_left or \
                    co_dwn_middle and co_middle_middle and co_up_middle or co_dwn_right and co_middle_right and co_up_right \
                    or co_up_left and co_middle_middle and co_dwn_right or co_up_right and co_middle_middle and co_dwn_left:
                print("Player 2 WIN !!!")
                time.sleep(1)
                start_setting()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if player1:
    #           print(pygame.mouse.get_pos())
                draw_x()
              elif player2:
                draw_o()


main()
