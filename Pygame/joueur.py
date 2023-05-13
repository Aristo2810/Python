import pygame


class Payer(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.joueur_img = pygame.image.load("assets/joueur.png")
        self.image = self.choper_limage(0, 0)

    def choper_limage(self, x: int, y: int):
        img = pygame.Surface([32, 32])
        img.blit(self.joueur_img, (0, 0), (x, y, 32, 32))
        return img


#https://youtu.be/ooITOxbYVTo?t=1518