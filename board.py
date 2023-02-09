import state
import gamewindow
import constants
import pygame

class Board():
    def __init__(self):
        self.boardState = [[state.State.EMPTY]*10 for _ in range(20)]
        self.boardState[5][5] = state.State.O
        self.boardState[4][5] = state.State.O
        self.boardState[5][4] = state.State.O
        self.boardState[4][4] = state.State.O
    def getState(self, x, y):
        return self.boardState[y][x]
    def displayActive(self, matrix, x, y, blocktype):
        display = gamewindow.getInstance()
        for line in range(len(matrix)):
            for column in range(len(matrix[line])):
                rectangle = pygame.Rect(constants.boardstartx + (column + x) * constants.blocksize, 
                                        constants.boardstarty - (line + y) * constants.blocksize,
                                        constants.blocksize,
                                        constants.blocksize)
                pygame.draw.rect(display, blocktype.value, rectangle)
    def place(self, matrix, x, y, blocktype):
        for line in range(len(matrix)):
            for column in range(len(matrix[line])):
                if (line < 0 or line > 19) or (column < 0 or column > 9):
                    continue
                if matrix[line][column] != state.State.NONE:
                    self.boardState[y + line][x + column] = blocktype
    def draw(self):
        display = gamewindow.getInstance()
        for line in range(len(self.boardState)):
            for column in range(len(self.boardState[line])):
                rectangle = pygame.Rect(constants.boardstartx + column * constants.blocksize, 
                                        constants.boardstarty - line * constants.blocksize,
                                        constants.blocksize,
                                        constants.blocksize)
                pygame.draw.rect(display, self.boardState[line][column].value, rectangle)
                pygame.draw.rect(display, (50, 50, 50), rectangle, width=constants.grid)


b = Board()

def getInstance():
    return b