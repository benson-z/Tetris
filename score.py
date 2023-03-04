import constants

class Score():
    def __init__(self):
        self.value = 0

    def clear(self, lines, tspin=False):
        if lines <= 0 or lines > 4:
            return
        self.value += constants.scoring_table[str(lines)]
        print(self.value)

    def getScore(self):
        return str(self.value)


score = Score()


def getInstance():
    return score
