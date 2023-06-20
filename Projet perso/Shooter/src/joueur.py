import pygame
from projectile import Projectile


class Joueur(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.pv = 100
        self.max_pv = 100
        self.att = 10
        self.vitesse = 5
        self.image = pygame.image.load("../assets/mery.png")
        self.transfo = pygame.transform.scale(self.image, (200, 200))
        self.image = self.transfo
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 650, 700
        self.grp_projectile = pygame.sprite.Group()

    def droite(self):
        if not self.game.collision(self, self.game.grp_monstres):
            self.rect.x += self.vitesse

    def gauche(self): self.rect.x -= self.vitesse

    def lancer(self):
        projectile = Projectile(self)
        self.grp_projectile.add(projectile)

    def collision(self, sprite, grp):
        return pygame.sprite.spritecollide(sprite, grp, False, pygame.sprite.collide_mask)
