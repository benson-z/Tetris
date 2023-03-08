import constants

class Score():
    def __init__(self):
        self.value = 0

    # Changes score based on lines cleared and scoring table (which can be configured in config.json
    # tspin parameter is unused for now
    def clear(self, lines, tspin=False):
        if lines <= 0 or lines > 4:
            return
        self.value += constants.scoring_table[str(lines)]
        print(self.value)

    # Returns current score
    def getScore(self):
        return str(self.value)


score = Score()  # Store instance inside file for easy access


def getInstance():
    return score
