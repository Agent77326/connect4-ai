def initialize_ranks():
    global RANKS
    RANKS = []
    for rank in range(7):
        rank_bb = 0
        for file in range(7):
            rank_bb |= 1 << (7* file  + rank)
        RANKS.append(rank_bb)


def initialize_files():
    global FILES
    FILES = []
    for file in range(7):
        file_bb = 0
        for rank in range(7):
            file_bb |= 1 << (7 * file + rank)
        FILES.append(file_bb)

def initialize_bitboards():
    initialize_files()
    initialize_ranks()