import numpy as np

class GameLogic:

    def __init__(self, width, heigth):
        self.bboard = np.int64(0)
        self.width = width
        self.heigth = heigth

    # see https://stackoverflow.com/a/12174125/9127322
    def setBit(self, value, bit):
        return value | (1<<bit)

    def setPiece(self, x, y, player):
        if not self.validMove(x, y):
            exit("What??")
        self.bboard = self.setBit(self.bboard, y * self.width + x)

    def validMove(self, x, y):
        if y > 0:
            return self.bboard & (1 << y * self.width + x) & (1 << (y - 1) * self.width + x)
        return self.bboard & (1 << y * self.width + x)

    def reset(self):
        self.bboard = np.int64(0)

test = GameLogic(6, 7)
print(test.bboard)
print(bin(test.bboard))
test.setPiece(1, 0, 0)
print(test.bboard)
print(bin(test.bboard))
