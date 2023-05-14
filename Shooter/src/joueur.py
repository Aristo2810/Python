import pygame
from projectile import Projectile


class Joueur(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.pv = 100
        self.max_pv = 100
        self.att = 10
        self.vitesse = 5
        self.image = pygame.image.load("../assets/mery.png")
        self.transfo = pygame.transform.scale(self.image, (200, 200))
        self.image = self.transfo
        self.rectangle = self.image.get_rect()
        self.rectangle.x, self.rectangle.y = 650, 700
        self.grp_projectile = pygame.sprite.Group()

    def droite(self): self.rectangle.x += self.vitesse

    def gauche(self): self.rectangle.x -= self.vitesse

    def lancer(self):
        projectile = Projectile()
        self.grp_projectile.add(projectile)
