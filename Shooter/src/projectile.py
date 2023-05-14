import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.vitesse = 5
        self.image = pygame.image.load("../assets/projectile.png")
        self.rectangle = self.image.get_rect()

