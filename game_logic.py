import numpy as np


# see https://stackoverflow.com/a/12174125/9127322
def set_bit(board, bit):
    board |= 1 << bit


class GameState:

    def __init__(self, width, heigth, red, yellow, turn):
        self.red = red
        self.yellow = yellow
        self.turn = turn
        self.width = width
        self.heigth = heigth

    @classmethod
    def default(cls):
        return GameState(6, 7, 0, 0, True)

    def make_move(self, move):
        assert move >= 0 and move < 7, "Illegal move type"

    def __str__(self):
        self.__repr__()

    def __repr__(self):
        #Schöne Formattierung des Spielfelds
        pass


if __name__ == '__main__':
    test = GameState.default()
    print(test.red)
