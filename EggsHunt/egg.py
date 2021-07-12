import pygame
import random


class Egg(pygame.sprite.Sprite):
    def __init__(self, largeur_ecran, hauteur_ecran, panier):
        super().__init__()
        self.largeur_ecran = largeur_ecran
        self.hauteur_ecran = hauteur_ecran
        self.image = pygame.image.load("assets/egg.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.speed = random.randint(1, 3)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largeur_ecran - 40)
        self.paniers = pygame.sprite.Group()
        self.panier = panier
        self.paniers.add(self.panier)

    def spawn(self):
        self.rect.x = random.randint(0, self.largeur_ecran - 40)
        self.rect.y = 0
        self.speed = random.randint(1, 3)

    def fall(self):
        self.rect.y += self.speed
        if self.rect.y >= self.hauteur_ecran:
            self.panier.rm_points()
            self.spawn()

        if pygame.sprite.spritecollide(self, self.paniers, False, pygame.sprite.collide_mask) and self.rect.y >= 360:
            self.panier.add_points()
            self.spawn()