import pygame
import pyscroll.data
import pytmx.util_pygame


class Game:

    def __init__(self):
        self.fen = pygame.display.set_mode((800, 600))
        tmx_carte = pytmx.util_pygame.load_pygame("assets/visuelmax.tmx")
        donne_carte = pyscroll.data.TiledMapData(tmx_carte)
        carte = pyscroll.orthographic.BufferedRenderer(donne_carte, self.fen.get_size())

        self.groupe = pyscroll.PyscrollGroup(map_layer=carte, default_layer=1)

    def run(self) -> None:
        running = True
        while running:

            self.groupe.draw(self.fen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
