import pygame
from joueur import Joueur
from monstre import Monstre


class Game:

    def __init__(self):
        self.fen = pygame.display.set_mode((1500, 900))
        self.bg = pygame.image.load("../assets/bg.jpg")
        self.grp_joueur = pygame.sprite.Group()
        self.joueur = Joueur(self)
        self.grp_joueur.add(self.joueur)
        self.touche = {}
        self.grp_monstres = pygame.sprite.Group()
        self.apparaitre_monstre()

    def apparaitre_monstre(self):
        self.grp_monstres.add(Monstre(self))

    def collision(self, sprite, grp): return pygame.sprite.spritecollide(sprite, grp, False, pygame.sprite.collide_mask)

    def run(self) -> None:
        running = True
        while running:

            self.fen.blit(self.bg, (0, 0))
            self.fen.blit(self.joueur.image, self.joueur.rect)

            for projectiles in self.joueur.grp_projectile:
                projectiles.bouger()
            self.joueur.grp_projectile.draw(self.fen)

            for monstre in self.grp_monstres:
                monstre.avancer()
            self.grp_monstres.draw(self.fen)

            if self.touche.get(pygame.K_RIGHT) and self.joueur.rect.x <= 1280:
                self.joueur.droite()
            elif self.touche.get(pygame.K_LEFT) and self.joueur.rect.x >= -25:
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
