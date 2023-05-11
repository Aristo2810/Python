import pygame
from constantes import *
from pygame.locals import *


pygame.init()
fenetre = pygame.display.set_mode((LONGUEUR, LARGEUR))
bg = pygame.image.load("assets/bg.jpg").convert()
bg = pygame.transform.scale(bg, (LONGUEUR, LARGEUR))
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = True

    fenetre.fill((0, 0, 0))
    fenetre.blit(bg, (0, 0))
    pygame.display.flip()

pygame.quit()
