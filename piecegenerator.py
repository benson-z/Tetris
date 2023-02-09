import piece
import state
import numpy as np
from numpy import random

class Generator():
    def __init__(self, seed = -1):
        if seed != -1:
            random.seed(seed)
        self.queue = []
    def getNext(self):
        if len(self.queue) == 0:
            self.queue = self.newBag()
        match(self.queue.pop()):
            case 'T':
                rotations = [[[0, 1, 0], 
                            [1, 1, 1], 
                            [0, 0, 0]], 
                            [[0, 1, 0], 
                            [0, 1, 1], 
                            [0, 1, 0]], 
                            [[0, 0, 0], 
                            [1, 1, 1], 
                            [0, 1, 0]], 
                            [[0, 1, 0], 
                            [1, 1, 0], 
                            [0, 1, 0]]]
                blocktype = state.State.T
            case 'I':
                rotations = [[[0, 0, 0, 0], 
                            [0, 0, 0, 0], 
                            [1, 1, 1, 1], 
                            [0, 0, 0, 0]],
                            [[0, 1, 0, 0], 
                            [0, 1, 0, 0], 
                            [0, 1, 0, 0], 
                            [0, 1, 0, 0]], 
                            [[0, 0, 0, 0], 
                            [1, 1, 1, 1], 
                            [0, 0, 0, 0], 
                            [0, 0, 0, 0]], 
                            [[0, 0, 1, 0], 
                            [0, 0, 1, 0], 
                            [0, 0, 1, 0], 
                            [0, 0, 1, 0]]]
                blocktype = state.State.I
            case 'O':
                rotations = [[[1, 1], 
                            [1, 1]], 
                            [[1, 1], 
                            [1, 1]], 
                            [[1, 1], 
                            [1, 1]], 
                            [[1, 1], 
                            [1, 1]]]
                blocktype = state.State.O
            case 'J':
                rotations = [[[0, 1, 0], 
                            [0, 1, 0], 
                            [1, 1, 0]], 
                            [[1, 0, 0], 
                            [1, 1, 1], 
                            [0, 0, 0]], 
                            [[0, 1, 1], 
                            [0, 1, 0], 
                            [0, 1, 0]], 
                            [[0, 0, 0], 
                            [1, 1, 1], 
                            [0, 0, 1]]]
                blocktype = state.State.J
            case 'L':
                rotations = [[[0, 1, 0], 
                            [0, 1, 0], 
                            [0, 1, 1]], 
                            [[0, 0, 0], 
                            [1, 1, 1], 
                            [1, 0, 0]], 
                            [[1, 1, 0], 
                            [0, 1, 0], 
                            [0, 1, 0]], 
                            [[0, 0, 1], 
                            [1, 1, 1], 
                            [0, 0, 0]]]
                blocktype = state.State.L
            case 'S':
                rotations = [[[0, 1, 1], 
                            [1, 1, 0], 
                            [0, 0, 0]], 
                            [[0, 1, 0], 
                            [0, 1, 1], 
                            [0, 0, 1]], 
                            [[0, 0, 0], 
                            [0, 1, 1], 
                            [1, 1, 0]], 
                            [[1, 0, 0], 
                            [1, 1, 0], 
                            [0, 1, 0]]
                            ]
                blocktype = state.State.S
            case 'Z':
                rotations = [[[1, 1, 0], 
                            [0, 1, 1], 
                            [0, 0, 0]], 
                            [[0, 0, 1], 
                            [0, 1, 1], 
                            [0, 1, 0]], 
                            [[0, 0, 0],
                            [1, 1, 0], 
                            [0, 1, 1]], 
                            [[0, 1, 0], 
                            [1, 1, 0], 
                            [1, 0, 0]]]
                blocktype = state.State.Z
        return piece.Piece(blocktype, rotations)
    def newBag(self):
        return random.permutation(np.array(['T', 'L', 'O', 'J', 'L', 'S', 'Z'])).tolist()