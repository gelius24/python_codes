from panier import Panier
from egg import Egg
import pygame
pygame.init()
largeur = 800
hauteur = 480
win = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Woody's egg hunt game")
pygame.display.set_icon(pygame.image.load('assets/chocolate.png'))
# le format jpg est mieu pour les background, bannière etc
bg = pygame.image.load("assets/fond.jpg")
# le format png a une transparance
floor = pygame.image.load("assets/sol.png")
chocolat = pygame.image.load('assets/chocolate.png')
chocolat = pygame.transform.scale(chocolat, (60, 60))
running = True
panier = Panier(largeur, hauteur)
# paniers = pygame.sprite.Group()
# paniers.add(panier)
eggs = pygame.sprite.Group()
eggs.add(Egg(largeur, hauteur, panier))
eggs.add(Egg(largeur, hauteur, panier))
# eggs.add(Egg(largeur, hauteur, paniers))
# egg = Egg(largeur, hauteur)
choco_color = (87, 64, 53)


while running:
    win.blit(bg, (0, 0))
    eggs.draw(win)
    win.blit(panier.image, panier.rect)
    win.blit(floor, (0, 0))
    pygame.draw.rect(win, (255, 255, 255), [10, hauteur - 50, largeur - 20, 32])
    largeur_chocolat = panier.points * 3 - 20
    pygame.draw.rect(win, choco_color, [10, hauteur - 50, largeur_chocolat, 32])
    win.blit(chocolat, (largeur_chocolat - chocolat.get_width()//2, 420))
    for every_eggs in eggs:
        every_eggs.fall()
    panier.move()
# update tout sur ecran (update est une portion)
    pygame.display.flip()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
            pygame.quit()
