import constants
import state
import board

class Piece:
    def __init__(self, blockType, rotations):
        self.rotations = rotations
        [a.reverse() for a in self.rotations]  # need to fix
        [[b.reverse() for b in c] for c in self.rotations]
        self.layout = self.rotations[0]
        self.currentRot = 0
        self.blockType = blockType
        self.resetPos()
        self.lock = False
        self.timeout = 2

    # Centers the piece at the top of the board
    def resetPos(self):
        if self.blockType == state.State.O:
            self.x = 4
        else:
            self.x = 3
        self.y = 20

    # Moves the piece to the "Hold" position
    def hold(self):
        self.x = -5
        self.y = 16
        self.currentRot = 0
        self.layout = self.rotations[0]
        self.lock = False

    # Check if a certain position for the piece intersects the wall or other pieces
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

    # Piece translation with validity checks
    def move(self, x, y):
        if self.valid(self.layout, self.x + x, self.y + y):
            self.x += x
            self.y += y
            if y >= 0:
                self.timeout = 2
            return 0
        else:
            return -1

    # Piece rotation
    def rotate(self, rotations):
        self.timeout = 2

        # Check if simple rotation works
        if self.valid(self.rotations[(self.currentRot + rotations) % 4], self.x, self.y):
            self.layout = self.rotations[(self.currentRot + rotations) % 4]
            self.currentRot = (self.currentRot + rotations) % 4
            return 0

        # SRS kick table implementation
        elif abs(rotations) != 2:
            rot_index = str((4 - self.currentRot) % 4) + "-" + str((4 - ((self.currentRot + rotations) % 4)) % 4)
            print(rot_index)
            if self.getType() == state.State.O:
                return -1
            elif self.getType() == state.State.I:
                table = constants.kick_table["I"][rot_index]
            else:
                table = constants.kick_table["JLTSZ"][rot_index]
            for x, y in table:
                if self.valid(self.rotations[(self.currentRot + rotations) % 4], self.x + x, self.y + y):
                    self.layout = self.rotations[(self.currentRot + rotations) % 4]
                    self.move(x, y)
                    self.currentRot = (self.currentRot + rotations) % 4
                    return 0
                print(x, y, "fail")
            return -1
        return -1

    # Move piece down by 1
    # Places pieces
    def down(self, drop=False):
        if self.lock and not drop:  # Lock in hold position
            return -2
        elif not self.valid(self.layout, self.x, self.y - 1):
            # Make sure the player has time to move their piece before placing
            if not drop and self.timeout > 0:
                self.timeout -= 1
                return 0
            try:
                board.getInstance().place(self)
            except:
                # Lose game (placement invalid because out of range)
                print("Game Over")
                quit()
            return -1
        self.move(0, -1)
        return 0

    # Hard drop
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
