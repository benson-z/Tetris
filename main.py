import board
import constants
import gamewindow
import pygame
from piecegenerator import Generator

# Initialize
gen = Generator()
p = gen.getNext()

counter = 0
while True:
    # Time counter
    counter += 1

    # Draw current board state
    board.getInstance().draw()

    # Event handler
    for event in pygame.event.get():
        # Normal program exit
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Handles KEYDOWN events (events that only should happen once per keypress)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_a:
                p.rotate(1)
            elif event.key == pygame.K_d:
                p.rotate(-1)
            elif event.key == pygame.K_SPACE:
                p.drop()
                p = gen.getNext()
            elif event.key == pygame.K_LSHIFT:
                p = board.getInstance().hold(p)
                if p is None:
                    p = gen.getNext()
                p.resetPos()
            elif event.key == pygame.K_TAB:
                constants.showHints = not constants.showHints

    # Handles repeating keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        p.move(-1, 0)
    if keys[pygame.K_RIGHT]:
        p.move(1, 0)
    if keys[pygame.K_DOWN]:
        p.move(0, -1)

    # Periodic drop rate
    if (counter % 5) == 0:
        if p.down() == -1:
            p = gen.getNext()

    # Update
    board.getInstance().drawPiece(p)
    board.getInstance().drawNext(gen.getQueue())
    gamewindow.update(constants.showHints)