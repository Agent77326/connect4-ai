import numpy as np
import gmpy2
from enum import Enum
import bitboards
import text_coloring


def popcount(board):
    return gmpy2.popcount(board)


class Winner(Enum):
    NONE = 0
    YELLOW = 1
    RED = 2
    DRAW = 3


class GameState:

    def __init__(self, red, yellow, turn):
        self.red = red
        self.yellow = yellow
        self.turn = turn
        self.winner = Winner.NONE

    @classmethod
    def default(cls):
        return GameState(0, 0, True)

    @classmethod
    def from_move_sequence(cls, seq):
        state = GameState.default()
        for move in seq:
            state.make_move(int(move))
        return state

    def is_mate(self):
        if self.turn:
            mating_side = self.yellow
        else:
            mating_side = self.red

        # -
        temp = mating_side & mating_side >> 1
        if (temp & temp >> 2) != 0:
            return True
        # |
        temp = mating_side & mating_side >> 7
        if (temp & temp >> 14) != 0:
            return True
        # /
        temp = mating_side & mating_side >> 8
        if (temp & temp >> 16) != 0:
            return True
        # \
        temp = mating_side & mating_side >> 6
        if (temp & temp >> 12) != 0:
            return True
        return False

    def make_move(self, move):
        assert self.winner == Winner.NONE, "Game is already over"
        assert 0 <= move < 7, "Illegal move type"
        pieces_in_file = popcount(bitboards.FILES[move] & (self.red | self.yellow))
        assert pieces_in_file < 6, "Illegal move, FILE is full"
        if self.turn:
            self.yellow |= 1 << 7 * pieces_in_file + move
        else:
            self.red |= 1 << 7 * pieces_in_file + move
        # Check if game over
        if self.is_mate():
            if self.turn:
                self.winner = Winner.YELLOW
            else:
                self.winner = Winner.RED
            return
        # Draw
        if not self.turn and popcount(self.yellow | self.red) == 42:
            self.winner = Winner.DRAW
        # Swap sides
        self.turn = not self.turn

    def unmake_move(self, move):
        assert 0 <= move < 7, "Illegal move type"
        self.turn = not self.turn
        self.winner = Winner.NONE
        pieces_in_file = popcount(bitboards.FILES[move] & (self.red | self.yellow)) - 1
        assert pieces_in_file >= 0, "This file is empty"
        if self.turn:
            assert (self.yellow >> (7 * pieces_in_file + move)) & 1 != 0, "There is no yellow piece to unmake move on"
            self.yellow ^= 1 << 7 * pieces_in_file + move
        else:
            assert (self.red >> (7 * pieces_in_file + move)) & 1 != 0, "There is no red piece to unmake move on "
            self.red ^= 1 << 7 * pieces_in_file + move

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        # Schöne Formattierung des Spielfelds
        res = "+-------+-------+-------+-------+-------+-------+-------+\n"
        for rank in range(6):
            res += "| "
            for file in range(7):
                idx = 7 * (5 - rank) + file
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
            if rank < 5:
                res += "--------------------------------------------------------+\n"
        res += "+-------+-------+-------+-------+-------+-------+-------+\n"
        return res


if __name__ == '__main__':
    bitboards.initialize_bitboards()
    test = GameState.default()
    test.make_move(1)
    test.make_move(0)
    test.make_move(2)
    test.make_move(0)
    test.make_move(0)
    print(test)
    test.unmake_move(0)
    test.unmake_move(0)
    print(test)
    test = GameState.from_move_sequence("3323130")
    print(test)
    print(test.winner)
    test = GameState.from_move_sequence("01122323353")
    print(test)
    print(test.winner)
    test = GameState.from_move_sequence("32211010030")
    print(test)
    print(test.winner)
    test = GameState.from_move_sequence("0101010")
    print(test)
    print(test.winner)
