import state
import gamewindow
import constants
import pygame
import score


class Board:
    def __init__(self):
        self.reset()

    def getState(self, x, y):
        return self.boardState[y][x]

    def displayActive(self, matrix, x, y, blocktype):
        display = gamewindow.getInstance()
        for line in range(len(matrix)):
            for column in range(len(matrix[line])):
                if matrix[line][column] == 0:
                    continue
                rectangle = pygame.Rect(constants.board_x + (column + x) * constants.block_size,
                                        constants.board_y - (line + y) * constants.block_size,
                                        constants.block_size,
                                        constants.block_size)
                pygame.draw.rect(display, blocktype.value, rectangle)

    def drawPiece(self, piece, shadow=True):
        x, y = piece.getPos()
        self.displayActive(piece.getLayout(), x, y, piece.getType())
        if not shadow:
            return
        for a in range(y + 4):
            if not piece.valid(piece.getLayout(), x, y - a):
                self.displayActive(piece.getLayout(), x, y - a + 1, piece.getType())
                break


    def drawScore(self, scoreText):
        labelText = pygame.font.Font("american-typewriter-bold.ttf", 32).render("Score", True, (255, 255, 255))
        labelRect = labelText.get_rect()
        labelRect.center = (constants.score_pos[0], constants.score_pos[1] - 50)
        gamewindow.getInstance().blit(labelText, labelRect)
        displayText = pygame.font.Font("american-typewriter-bold.ttf", 48).render(scoreText, True, (255, 255, 255))
        displayRect = displayText.get_rect()
        displayRect.center = constants.score_pos
        gamewindow.getInstance().blit(displayText, displayRect)


    def place(self, piece):
        x, y = piece.getPos()
        for line in range(len(piece.getLayout())):
            for column in range(len(piece.getLayout()[line])):
                if (line < 0 or line > 19) or (column < 0 or column > 9):
                    continue
                if piece.getLayout()[line][column] != 0:
                    self.boardState[y + line][x + column] = piece.getType()
        self.update()

    def draw(self):
        display = gamewindow.getInstance()
        for line in range(len(self.boardState)):
            for column in range(len(self.boardState[line])):
                rectangle = pygame.Rect(constants.board_x + column * constants.block_size,
                                        constants.board_y - line * constants.block_size,
                                        constants.block_size,
                                        constants.block_size)
                pygame.draw.rect(display, self.boardState[line][column].value, rectangle)
                pygame.draw.rect(display, (50, 50, 50), rectangle, width=constants.grid)
        if self.holdPiece is not None:
            self.drawPiece(self.holdPiece, shadow=False)
        self.drawScore(score.getInstance().getScore())

    def drawNext(self, queue):
        for p in range(len(queue)):
            self.displayActive(constants.rotations[queue[p]][2], 12, 16 - 3.2 * p, state.toState(queue[p]))

    def hold(self, piece):
        p, self.holdPiece = self.holdPiece, piece
        self.holdPiece.hold()
        return p

    def update(self):
        remove = []
        for row in range(len(self.boardState)):
            if self.boardState[row].count(state.State.EMPTY) != 0:
                remove.append(self.boardState[row])
        score.getInstance().clear(20 - len(remove))
        while len(remove) < 20:
            remove.append([state.State.EMPTY] * 10)
        self.boardState = remove

    def reset(self):
        self.boardState = [[state.State.EMPTY] * 10 for _ in range(20)]
        self.holdPiece = None

b = Board()


def getInstance():
    return b
