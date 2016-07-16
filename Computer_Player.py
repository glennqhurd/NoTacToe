import random

from NoTacToe import *
from tictactoe_symmetry import *


class Computer_Player:

    def __init__(self):
        self.notactoe = NoTacToe()
        self.total_board = []
        active = self.notactoe.get_active_boards()
        for i in range(active):
            board_list = self.notactoe.get_board(i)
            self.total_board += board_list

    def get_board_info(self):
        return self.total_board

    def random_move(self):
        move = random.randint(0, (len(self.total_board) - 1))
        count = 0
        board = move / 9
        box = move % 9
        while not self.notactoe.check_box(board, box):
            count += 1
            if count == len(self.total_board):
                return
            if move >= (len(self.total_board) - 1):
                move = 0
            else:
                move += 1
            board = move / 9
            box = move % 9
        return board, box

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