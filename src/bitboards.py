def print_bitboard(board):
    res = "+-------+-------+-------+-------+-------+-------+-------+\n"
    for rank in range(6):
        res += "| "
        for file in range(7):
            idx = 7 * (5 - rank) + file
            if (board >> idx) & 1 != 0:
                res += "\t\u26ab\t"
            else:
                res += "\t\t"
            if file < 6:
                res += "| "
        res += "|\n"
        if rank < 5:
            res += "--------------------------------------------------------+\n"
    res += "+-------+-------+-------+-------+-------+-------+-------+\n"
    print(res)


def initialize_ranks():
    global RANKS
    RANKS = []
    for rank in range(6):
        rank_bb = 0
        for file in range(7):
            rank_bb |= 1 << (7 * rank + file)
        RANKS.append(rank_bb)


def initialize_files():
    global FILES
    FILES = []
    for file in range(7):
        file_bb = 0
        for rank in range(6):
            file_bb |= 1 << (7 * rank + file)
        FILES.append(file_bb)


def initialize_bitboards():
    initialize_files()
    initialize_ranks()
