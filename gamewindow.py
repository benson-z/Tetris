import pygame
from constants import *

gameDisplay = pygame.display.set_mode(resolution)
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

def getInstance():
    return gameDisplay

def update():
    for event in pygame.event.get():
        # Normal program exit
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    clock.tick(20)