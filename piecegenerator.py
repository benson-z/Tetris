import piece
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
        return piece.Piece(self.queue.pop())
    def newBag(self):
        return random.permutation(np.array(['T', 'L', 'O', 'J', 'L', 'S', 'Z'])).tolist()