import pygame


pygame.init()


class Game:

    def __int__(self):
        self.fen = pygame.display.set_mode((800, 600))

    def run_game(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    running = False
        pygame.quit()
