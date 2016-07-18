import random

from NoTacToe import *
from tictactoe_symmetry import *


class Computer_Player:

    def __init__(self):
        self.notactoe = NoTacToe()
        self.total_board = self.notactoe.get_active_boards()
        self.total_length = 9 * self.total_board

    def get_board_info(self):
        return self.total_board

    def random_move(self):
        move = random.randint(0, (self.total_length - 1))
        for i in range(self.total_length):
            board = (move % self.total_length) / 9
            box = move % 9
            if self.notactoe.check_box(board, box):
                return board, box
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