import bitboards
import numpy as np
import gmpy2


def popcount(board):
    return gmpy2.popcount(board)


class GameState:

    def __init__(self, red, yellow, turn):
        self.red = red
        self.yellow = yellow
        self.turn = turn

    @classmethod
    def default(cls):
        return GameState(0, 0, True)

    def make_move(self, move):
        assert move >= 0 and move < 7, "Illegal move type"

    def unmake_move(self, move):
        pass

    def __str__(self):
        self.__repr__()

    def __repr__(self):
        # Schöne Formattierung des Spielfelds
        pass


if __name__ == '__main__':
    bitboards.initialize_bitboards()
    test = GameState.default()
    print(popcount(bitboards.FILES[0]))
