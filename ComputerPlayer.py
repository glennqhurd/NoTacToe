import random

from tictactoe_symmetry import *


class ComputerPlayer:

    def __init__(self, notactoe):
        self.notactoe = notactoe
        # board_variables stores the non-constant values of the boards
        self.board_variables = {'         ': 'c', '    X    ': 'cc', 'XX       ': 'ad', 'X X      ': 'b',
                                'X   X    ': 'b', 'X    X   ': 'b', 'X       X': 'a', ' X X     ': 'a',
                                ' X  X    ': 'b', ' X     X ': 'a', 'XX X     ': 'b', 'XX  X    ': 'ab',
                                'XX   X   ': 'd', 'XX    X  ': 'a', 'XX     X ': 'd', 'XX      X': 'd',
                                'X X X    ': 'a', 'X X   X  ': 'ab', 'X X    X ': 'a', 'X   XX   ': 'a',
                                ' X XX    ': 'ab', ' X X X   ': 'b', 'XX XX    ': 'a', 'XX X X   ': 'a',
                                'XX X    X': 'a', 'XX  XX   ': 'b', 'XX  X X  ': 'b', 'XX   XX  ': 'b',
                                'XX   X X ': 'ab', 'XX   X  X': 'ab', 'XX    XX ': 'b', 'XX    X X': 'b',
                                'XX     XX': 'a', 'X X X  X ': 'b', 'X X   X X': 'a', 'X   XX X ': 'b',
                                ' X X X X ': 'a', 'XX X X X ': 'b', 'XX X X  X': 'b', 'XX  XXX  ': 'a',
                                'XX   XXX ': 'a', 'XX   XX X': 'a', 'XX X X XX': 'a'}

    def random_move(self):
        total_length = self.notactoe.get_num_active_boards() * 9
        move = random.randint(0, (total_length - 1))
        for i in range(total_length):
            board_number = ((move + i) % total_length) / 9
            box = (move + i) % 9
            if self.notactoe.check_box(board_number, box):
                self.notactoe.mark_x(board_number, box)
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