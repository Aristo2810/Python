import pygame


class Joueur(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.pv = 100
        self.max_pv = 100
        self.att = 10
        self.vitesse = 5
        self.image = pygame.image.load("../assets/player.png")
        self.rectangle = self.image.get_rect()
        self.rectangle.x, self.rectangle.y = 650, 700

    def droite(self): self.rectangle.x += self.vitesse

    def gauche(self): self.rectangle.x -= self.vitesse