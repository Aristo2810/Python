import pygame
from constantes import *
from pygame.locals import *


pygame.init()

fenetre = pygame.display.set_mode((LONGUEUR, LARGEUR))

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = True


pygame.quit()
