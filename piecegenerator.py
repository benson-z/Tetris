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
            print(self.queue)
        nextpiece = self.queue.pop()
        print("New piece:", nextpiece)
        match(nextpiece):
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
            case 'L':
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
                blocktype = state.State.L
            case 'J':
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
                blocktype = state.State.J
            case 'Z':
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
                blocktype = state.State.Z
            case 'S':
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
                blocktype = state.State.S
        return piece.Piece(blocktype, rotations)
    def newBag(self):
        return random.permutation(np.array(['T', 'I', 'O', 'J', 'L', 'S', 'Z'])).tolist()