import bitboards
import text_coloring
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
        return self.__repr__()

    def __repr__(self):
        # Schöne Formattierung des Spielfelds
        res = "+-------+-------+-------+-------+-------+-------+-------+\n"
        for rank in range(7):
            res += "| "
            for file in range(7):
                idx = 7 * file + rank
                if (self.yellow >> idx) & 1 != 0:
                    res += "\t{}\t".format(text_coloring.Style.YELLOW("\u26ab"))
                elif (self.red >> idx) & 1 != 0:
                    res += "\t{}\t".format(text_coloring.Style.RED("\u26ab"))
                else:
                    res += "\t\t"
                res += text_coloring.Style.RESET("")
                if file < 6:
                    res += "| "
            res += "|\n"
            if rank < 6:
                res += "--------------------------------------------------------+\n"
        res += "+-------+-------+-------+-------+-------+-------+-------+\n"
        return res


if __name__ == '__main__':
    bitboards.initialize_bitboards()
    test = GameState.default()
    test.yellow |= 1 << 16
    test.red |= 1 << 24
    print(popcount(bitboards.FILES[0]))
    print(test)
