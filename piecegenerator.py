import constants
import piece
import state
import numpy as np
from numpy import random
import copy


class Generator:
    def __init__(self, seed=-1):
        # Initialize random
        # Set random seed for debugging purposes
        if seed != -1:
            random.seed(seed)
        self.queue = []

    # Returns a new piece object based on randomizer
    def getNext(self):
        if len(self.queue) <= 6:
            self.queue += self.newBag()
        nextpiece = self.queue.pop(0)
        blocktype = state.toState(nextpiece)
        rotations = constants.rotations[nextpiece]
        return piece.Piece(blocktype, copy.deepcopy(rotations))

    # Randomizer
    def newBag(self):
        return random.permutation(np.array(['T', 'I', 'O', 'J', 'L', 'S', 'Z'])).tolist()

    # Returns data for displaying the next queue
    def getQueue(self):
        return self.queue[:5]

    def reset(self):
        self.queue = []
