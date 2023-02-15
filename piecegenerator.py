import constants
import piece
import state
import numpy as np
from numpy import random
import copy


class Generator:
    def __init__(self, seed=-1):
        if seed != -1:
            random.seed(seed)
        self.queue = ['L', 'L']

    def getNext(self):
        if len(self.queue) == 0:
            self.queue = self.newBag()
        nextpiece = self.queue.pop()
        print("New piece:", nextpiece)
        match nextpiece:
            case 'T':
                blocktype = state.State.T
            case 'I':
                blocktype = state.State.I
            case 'O':
                blocktype = state.State.O
            case 'L':
                blocktype = state.State.L
            case 'J':
                blocktype = state.State.J
            case 'Z':
                blocktype = state.State.Z
            case 'S':
                blocktype = state.State.S
        rotations = constants.rotations[nextpiece]
        return piece.Piece(blocktype, copy.deepcopy(rotations))

    def newBag(self):
        return random.permutation(np.array(['T', 'I', 'O', 'J', 'L', 'S', 'Z'])).tolist()

    def reset(self):
        self.queue = []
