import pygame


class Panier(pygame.sprite.Sprite):
    def __init__(self, largeur_ecran, hauteur_ecran):
        # initialiser la classe Sprite
        super().__init__()
        self.largeur_ecran = largeur_ecran
        self.image = pygame.image.load("assets/panier.png")
        # redimensionnement de l'image
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x = (largeur_ecran // 2) - self.image.get_width() // 2
        self.rect.y = hauteur_ecran - 195
        self.points = 50
        self.max_points = 100
        self.speed = 12

    def move(self):
      keys = pygame.key.get_pressed()
      if keys[pygame.K_RIGHT]:
        if self.rect.x + self.image.get_width() <= self.largeur_ecran:
            self.rect.x += self.speed
      elif keys[pygame.K_LEFT]:
        if self.rect.x > 0:
            self.rect.x -= self.speed

    def add_points(self):
        if self.points + 5 <= self.max_points:
            self.points += 5

    def rm_points(self):
      if self.points - 2 > 0:
        self.points -= 2
      else:
          print('perdu !')