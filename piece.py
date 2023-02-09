import board
import state

class Piece():
    def __init__(self, blocktype, rotations):
        self.layout = rotations[0]
        self.rotations = rotations
        self.blocktype = blocktype
        self.x = 2
        self.y = 20
    def valid(self, layout, x, y):
        right = 0
        left = 3
        down = 20
        for row in range(len(layout)):
            for column in range(len(layout[row])):
                if layout[row][column] != 0:
                    right = max(right, column)
                    left = min(left, column)
                    down = min(down, row)
                    if (y + row < 0 or y + row > 19) or (x + column < 0 or x + column > 9):
                        continue
                    try:
                        if board.getInstance().getState(x + column, y + row) != state.State.EMPTY:
                            return False
                    except:
                        pass
        if right + x > 9 or left + x < 0 or down + y < 0:
            return False
        return True
    def move(self, x, y):
        if self.valid(self.layout, self.x + x, self.y + y):
            self.x += x
            self.y += y
    def rotate(self, rotations):
        pass
    def update(self):
        board.getInstance().displayActive(self.layout, self.x, self.y, self.blocktype)
    def down(self):
        if not self.valid(self.layout, self.x, self.y - 1):
            board.getInstance().place(self.layout, self.x, self.y, self.blocktype)
            return -1
        self.move(0, -1)
        return 0