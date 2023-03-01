import pygame
from constants import *

gameDisplay = pygame.display.set_mode(resolution)
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

# pygame.key.set_repeat(100, 1)

def getInstance():
    return gameDisplay

def update():
    pygame.display.update()
    clock.tick(20)