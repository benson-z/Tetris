import board
import piece
import gamewindow
import pygame
import state
from piecegenerator import Generator


gen = Generator()
p = gen.getNext()

counter = 0
while True:
    counter += 1
    board.getInstance().draw()
    for event in pygame.event.get():
        # Normal program exit
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                p.rotate(1)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        p.move(-1, 0)
    if keys[pygame.K_RIGHT]:
        p.move(1, 0)
    if keys[pygame.K_DOWN]:
        p.move(0, -1)
    if (counter % 20) == 1:
        if p.down() == -1:
            p = gen.getNext()
            print('New piece')
    p.update()
    gamewindow.update()
    gamewindow.getInstance().fill("black")