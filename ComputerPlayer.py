import random


class ComputerPlayer:
    MONOID_LABELS = ('1', 'a', 'b', 'ab', 'b2', 'abc', 'c', 'ac', 'bc', 'abc', 'cc', 'ac2', 'bcc', 'abcc', 'd', 'ad',
                     'bd', 'abd')
    # BOARD_VARIABLES stores the non-constant values of the boards
    BOARD_VARIABLES = {'         ': 6, '    X    ': 10, 'XX       ': 15, 'X X      ': 2,
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

    def get_variable(self, board_index):
        if ''.join(self.notactoe.board_list[board_index]) in self.BOARD_VARIABLES:
            return self.MONOID_LABELS[self.BOARD_VARIABLES[''.join(self.notactoe.board_list[board_index])]]
        return self.MONOID_LABELS[0]