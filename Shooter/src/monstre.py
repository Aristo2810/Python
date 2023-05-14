import pygame
import random


class Monstre(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.pv = 100
        self.max_pv = 100
        self.att = 5
        self.vitesse = random.randint(2, 6)
        self.image = pygame.image.load("../assets/ange.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 1300, 675

    def avancer(self):
        if not self.game.collision(self, self.game.grp_joueur):
            self.rect.x -= self.vitesse
