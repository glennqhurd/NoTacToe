import random

from tictactoe_symmetry import *

MONOID_LABELS = ['1', 'a', 'b', 'ab', u'b\u00B2', u'ab\u00B2', 'c', 'ac', 'bc',
                 'abc', u'c\u00B2', u'ac\u00B2', u'bc\u00B2', u'abc\u00B2', 'd', 'ad', 'bd', 'abd']

COLORED_MONOIDS = {'a', u'b\u00B2', 'bc', u'c\u00B2'}

WINNING_MONOIDS_INDEX = {1, 4, 8, 10}

LOSING_POSITIONS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

# BOARD_VALUES stores the non-constant values of the boards
BOARD_VALUES = {'         ': 6, '    X    ': 10, 'XX       ': 15, 'X X      ': 2,
                'X   X    ': 2, 'X    X   ': 2, 'X       X': 1, ' X X     ': 1,
                ' X  X    ': 2, ' X     X ': 1, 'XX X     ': 2, 'XX  X    ': 3,
                'XX   X   ': 14, 'XX    X  ': 1, 'XX     X ': 14, 'XX      X': 14,
                'X X X    ': 1, 'X X   X  ': 3, 'X X    X ': 1, 'X   XX   ': 1,
                ' X XX    ': 3, ' X X X   ': 2, 'XX XX    ': 1, 'XX X X   ': 1,
                'XX X    X': 1, 'XX  XX   ': 2, 'XX  X X  ': 2, 'XX   XX  ': 2,
                'XX   X X ': 3, 'XX   X  X': 3, 'XX    XX ': 2, 'XX    X X': 2,
                'XX     XX': 1, 'X X X  X ': 2, 'X X   X X': 1, 'X   XX X ': 2,
                ' X X X X ': 1, 'XX X X X ': 2, 'XX X X  X': 2, 'XX  XXX  ': 1,
                'XX   XXX ': 1, 'XX   XX X': 1, 'XX X X XX': 1}

LOOKUP_TABLE = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (0, 4): 4,
                (0, 5): 5, (0, 6): 6, (0, 7): 7, (0, 8): 8, (0, 9): 9,
                (0, 10): 10, (0, 11): 11, (0, 12): 12, (0, 13): 13, (0, 14): 14,
                (0, 15): 15, (0, 16): 16, (0, 17): 17, (1, 1): 0, (1, 2): 3,
                (1, 3): 2, (1, 4): 5, (1, 5): 4, (1, 6): 7, (1, 7): 6,
                (1, 8): 9, (1, 9): 8, (1, 10): 11, (1, 11): 10, (1, 12): 13,
                (1, 13): 12, (1, 14): 15, (1, 15): 14, (1, 16): 17, (1, 17): 16,
                (2, 2): 4, (2, 3): 5, (2, 4): 2, (2, 5): 3, (2, 6): 8,
                (2, 7): 9, (2, 8): 6, (2, 9): 7, (2, 10): 12, (2, 11): 13,
                (2, 12): 10, (2, 13): 11, (2, 14): 16, (2, 15): 17, (2, 16): 14,
                (2, 17): 15, (3, 3): 4, (3, 4): 3, (3, 5): 2, (3, 6): 9,
                (3, 7): 8, (3, 8): 7, (3, 9): 6, (3, 10): 13, (3, 11): 12,
                (3, 12): 11, (3, 13): 10, (3, 14): 17, (3, 15): 16, (3, 16): 15,
                (3, 17): 14, (4, 4): 4, (4, 5): 5, (4, 6): 6, (4, 7): 7,
                (4, 8): 8, (4, 9): 9, (4, 10): 10, (4, 11): 11, (4, 12): 12,
                (4, 13): 13, (4, 14): 14, (4, 15): 15, (4, 16): 16, (4, 17): 17,
                (5, 5): 4, (5, 6): 7, (5, 7): 6, (5, 8): 9, (5, 9): 8,
                (5, 10): 11, (5, 11): 10, (5, 12): 13, (5, 13): 12, (5, 14): 15,
                (5, 15): 14, (5, 16): 17, (5, 17): 16, (6, 6): 10, (6, 7): 11,
                (6, 8): 12, (6, 9): 13, (6, 10): 11, (6, 11): 10, (6, 12): 13,
                (6, 13): 12, (6, 14): 15, (6, 15): 14, (6, 16): 17, (6, 17): 16,
                (7, 7): 10, (7, 8): 13, (7, 9): 12, (7, 10): 10, (7, 11): 11,
                (7, 12): 12, (7, 13): 13, (7, 14): 14, (7, 15): 15, (7, 16): 16,
                (7, 17): 17, (8, 8): 10, (8, 9): 11, (8, 10): 13, (8, 11): 12,
                (8, 12): 11, (8, 13): 10, (8, 14): 17, (8, 15): 16, (8, 16): 15,
                (8, 17): 14, (9, 9): 10, (9, 10): 12, (9, 11): 13, (9, 12): 10,
                (9, 13): 11, (9, 14): 16, (9, 15): 17, (9, 16): 14, (9, 17): 15,
                (10, 10): 10, (10, 11): 11, (10, 12): 12, (10, 13): 13, (10, 14): 14,
                (10, 15): 15, (10, 16): 16, (10, 17): 17, (11, 11): 10, (11, 12): 13,
                (11, 13): 12, (11, 14): 15, (11, 15): 14, (11, 16): 17, (11, 17): 16,
                (12, 12): 10, (12, 13): 11, (12, 14): 16, (12, 15): 17, (12, 16): 14,
                (12, 17): 15, (13, 13): 10, (13, 14): 17, (13, 15): 16, (13, 16): 15,
                (13, 17): 14, (14, 14): 10, (14, 15): 11, (14, 16): 12, (14, 17): 13,
                (15, 15): 10, (15, 16): 13, (15, 17): 12, (16, 16): 10, (16, 17): 11,
                (17, 17): 10}


def board_value(board):
    return random.randint(0, 17)


def find_composite(board_list):
    monoid_list = [get_monoid_index(x, board_list) for x in range(len(board_list))]
    return reduce(lambda m1, m2: combine_monoids(m1, m2), monoid_list)


def combine_monoids(monoid1, monoid2):
    monoid_tuple = tuple(sorted((monoid1, monoid2)))
    return LOOKUP_TABLE[monoid_tuple]


def get_monoid_index(board_index, board_list):
    symmetry, index = canonical_board(''.join(board_list[board_index]))
    if symmetry in BOARD_VALUES:
        return BOARD_VALUES[symmetry]
    return 0

def translate_to_monoid(monoid_index):
    return MONOID_LABELS[monoid_index]


def check_box_legal( board_number, box, board_list, dead_boards):
    return board_list[board_number][box] == ' ' and board_number not in dead_boards


def check_box_winning(board_number, box, board_list, dead_boards):
    if check_box_legal(board_number, box, board_list, dead_boards):
        mark_box(board_number, box, board_list, dead_boards, 'X')
        if find_composite(board_list) in WINNING_MONOIDS_INDEX:
            logging.debug("Composite was: %d", find_composite(board_list))
            return True
        remove_from_dead(dead_boards, board_number)
        mark_box(board_number, box, board_list, dead_boards, ' ')
    return False


# changes the board by replacing a ' ' with an 'X' if there isn't already an 'X' in place
def mark_box(board_number, box, board_list, dead_boards, symbol):
    if not check_box_legal(board_number, box, board_list, dead_boards) and symbol == 'X':
        return False
    else:
        board_list[board_number][box] = symbol
        check_loser(board_list, dead_boards, board_number)
        return True


# check_loser checks the board to see if there are three Xs in a line and if so checks if the list dead_boards has
    # a value equal to index.  If the value doesn't exist it add index to the dead_boards list.
def check_loser(board_list, dead_boards, index):
    for i in LOSING_POSITIONS:
        if board_list[index][i[0]] == 'X' and board_list[index][i[1]] == 'X' and board_list[index][i[2]] == 'X':
            dead_boards.add(index)
            return True
    return False


def get_loser_boxes(board_list, index):
    for i in LOSING_POSITIONS:
        if board_list[index][i[0]] == 'X' and board_list[index][i[1]] == 'X' and board_list[index][i[2]] == 'X':
            return board_list[index][i[0]], board_list[index][i[1]], board_list[index][i[2]]


def remove_from_dead(dead_boards, board_number):
    if board_number in dead_boards:
        dead_boards.remove(board_number)
