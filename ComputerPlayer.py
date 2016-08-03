import random


class ComputerPlayer:
    MONOID_LABELS = ('1', 'a', 'b', 'ab', 'b2', 'abc', 'c', 'ac', 'bc', 'abc', 'c2', 'ac2', 'bc2', 'abc2', 'd', 'ad',
                     'bd', 'abd')
    # BOARD_VARIABLES stores the non-constant values of the boards
    BOARD_VARIABLES = {'         ': 'c', '    X    ': 'cc', 'XX       ': 'ad', 'X X      ': 'b',
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

    def __init__(self, notactoe):
        self.notactoe = notactoe

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

    def get_variable_index(self, board):
        if ''.join(board) in self.BOARD_VARIABLES:
            return self.MONOID_LABELS.index(self.BOARD_VARIABLES[''.join(board)])
        return 0