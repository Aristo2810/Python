import pygame
from joueur import Joueur


class Game:

    def __init__(self):
        self.fen = pygame.display.set_mode((1500, 900))
        self.bg = pygame.image.load("../assets/bg.jpg")
        self.joueur = Joueur()
        self.touche = {}

    def run(self) -> None:
        running = True
        while running:

            self.fen.blit(self.bg, (0, 0))
            self.fen.blit(self.joueur.image, self.joueur.rectangle)
            self.joueur.grp_projectile.draw(self.fen)

            if self.touche.get(pygame.K_RIGHT) and self.joueur.rectangle.x <= 1280:
                self.joueur.droite()
            elif self.touche.get(pygame.K_LEFT) and self.joueur.rectangle.x >= -25:
                self.joueur.gauche()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    self.touche[event.key] = True
                    if event.key == pygame.K_SPACE:
                        self.joueur.lancer()

                elif event.type == pygame.KEYUP:
                    self.touche[event.key] = False

        pygame.quit()
