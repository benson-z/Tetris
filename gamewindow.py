import pygame
from constants import *

pygame.init()
gameDisplay = pygame.display.set_mode(resolution)
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

bg = pygame.image.load("resources/background.png")
hints = pygame.image.load("resources/background_hints.png")

def getInstance():
    return gameDisplay

def update(showHints = False):
    pygame.display.update()
    clock.tick(20)
    if showHints:
        gameDisplay.blit(hints, (0, 0))
    else:
        gameDisplay.blit(bg, (0, 0))
