import pygame


pygame.init()

fen = pygame.display.set_mode((800, 600))
running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
pygame.quit()