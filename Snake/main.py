import pygame
from constantes import *
from pygame.locals import *


pygame.init()

fenetre = pygame.display.set_mode((LONGUEUR, LARGEUR))
bg = pygame.image.load("assets/bg.jpg").convert()
fenetre.blit(bg, (0, 0))
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = True

    pygame.display.update()

pygame.quit()
