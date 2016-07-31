import random

from NoTacToe import *
from tictactoe_symmetry import *


class Computer_Player:

    def __init__(self, notactoe):
        self.notactoe = notactoe

    def random_move(self):
        total_length = self.notactoe.get_active_boards * 9
        move = random.randint(0, (total_length - 1))
        for i in range(total_length):
            board_number = ((move + i) % total_length) / 9
            box = (move + i) % 9
            if notactoe.check_box(board_number, box):
                return board_number, box
        return False, 'No valid moves'

    def get_variable(self, board):
        # Board: ' ' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        if canonical_board(board) == canonical_board([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']):
            return 'c'
        # Board: ' ' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | 'X' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        elif canonical_board(board) == canonical_board([' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']):
            return 'c2'
        # Board: 'X' | 'X' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        elif canonical_board(board) == canonical_board(['X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ']):
            return 'ad'
        # Board: 'X' | ' ' | 'X'
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        elif canonical_board(board) == canonical_board(['X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ']):
            return 'b'
        # Board: 'X' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | 'X' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        elif canonical_board(board) == canonical_board(['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']):
            return 'b'
        # Board: 'X' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | 'X'
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        elif canonical_board(board) == canonical_board(['X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ']):
            return 'b'
        # Board: 'X' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | 'X'
        elif canonical_board(board) == canonical_board(['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X']):
            return 'a'
        # Board: ' ' | 'X' | ' '
        #       -----|-----|-----
        #        'X' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        elif canonical_board(board) == canonical_board([' ', 'X', ' ', 'X', ' ', ' ', ' ', ' ', ' ']):
            return 'a'
        # Board: ' ' | 'X' | ' '
        #       -----|-----|-----
        #        ' ' | 'X' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        elif canonical_board(board) == canonical_board([' ', 'X', ' ', ' ', 'X', ' ', ' ', ' ', ' ']):
            return 'b'
        # Board: ' ' | 'X' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | 'X' | ' '
        elif canonical_board(board) == canonical_board([' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X', ' ']):
            return 'a'
        # Board: 'X' | 'X' | ' '
        #       -----|-----|-----
        #        'X' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        elif canonical_board(board) == canonical_board(['X', 'X', ' ', 'X', ' ', ' ', ' ', ' ', ' ']):
            return 'b'
        # Board: 'X' | 'X' | ' '
        #       -----|-----|-----
        #        ' ' | 'X' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        elif canonical_board(board) == canonical_board(['X', 'X', ' ', ' ', 'X', ' ', ' ', ' ', ' ']):
            return 'ab'