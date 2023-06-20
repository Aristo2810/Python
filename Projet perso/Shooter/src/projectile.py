import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, joueur):
        super().__init__()
        self.vitesse = 5
        self.joueur = joueur
        self.image = pygame.image.load("../assets/projectile.jpg")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.image_origine = self.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = joueur.rect.x + 130, joueur.rect.y
        self.angle = 0

    def tourner(self):
        self.angle += 2
        self.image = pygame.transform.rotozoom(self.image_origine, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def bouger(self):
        self.rect.x += self.vitesse
        if self.rect.x > 1500:
            self.suppr()
        self.tourner()
        if self.joueur.collision(self, self.joueur.game.grp_monstres):
            self.remove()

    def suppr(self): self.joueur.grp_projectile.remove(self)
