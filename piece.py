import pygame

import board
import state
import copy


class Piece:
    def __init__(self, blockType, rotations):
        self.rotations = rotations
        [a.reverse() for a in self.rotations]  # need to fix
        self.layout = self.rotations[0]
        self.currentRot = 0
        self.blockType = blockType
        self.x = 2
        self.y = 20
        self.lock = False

    def resetPos(self):
        self.x = 2
        self.y = 20

    def hold(self):
        self.x = -5
        self.y = 15
        self.currentRot = 0
        self.layout = self.rotations[0]
        self.lock = False

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
            return 0
        else:
            return -1

    def rotate(self, rotations):
        print("Current:", self.currentRot)
        if self.valid(self.rotations[(self.currentRot + rotations) % 4], self.x, self.y):
            self.layout = self.rotations[(self.currentRot + rotations) % 4]
            self.currentRot = (self.currentRot + rotations) % 4
            print("New:", self.currentRot)
            return 0
        else:
            return -1

    def down(self, drop=False):
        if self.lock and not drop:
            return -2
        elif not self.valid(self.layout, self.x, self.y - 1):
            try:
                board.getInstance().place(self)
            except:
                print("Game Over")
                quit()
            return -1
        self.move(0, -1)
        return 0

    def drop(self):
        self.lock = True
        while True:
            if self.down(True) == -1:
                break

    def getType(self):
        return self.blockType

    def getPos(self):
        return self.x, self.y

    def getLayout(self):
        return self.layout
