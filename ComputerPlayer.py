import random

import BoardCalculations
import NoTacToe


class ComputerPlayer:
    def __init__(self, notactoe):
        self.notactoe = notactoe
        self.testtactoe = NoTacToe.NoTacToe()

    # def make_move(self):
    #     total_length = self.notactoe.get_num_active_boards() * 9
    #     move = random.randint(0, (total_length - 1))
    #     for i in range(total_length):
    #         board_number = ((move + i) % total_length) / 9
    #         box = (move + i) % 9
    #         if self.notactoe.check_box_legal(board_number, box):
    #             self.notactoe.mark_box(board_number, box)
    #             return board_number, box
    #     return False, 'No valid moves'

    def make_move(self, find_winning):
        assertion = False
        if find_winning:
            total_length = self.notactoe.get_num_active_boards() * 9
            move = random.randint(0, (total_length - 1))
            for i in range(total_length):
                board_number = ((move + i) % total_length) / 9
                box = (move + i) % 9
                if self.notactoe.check_box_winning(board_number, box):
                    self.notactoe.mark_box(board_number, box, 'X')
                    return board_number, box
        total_length = self.notactoe.get_num_active_boards() * 9
        move = random.randint(0, (total_length - 1))
        for i in range(total_length):
            board_number = ((move + i) % total_length) / 9
            box = (move + i) % 9
            if self.notactoe.check_box_legal(board_number, box):
                self.notactoe.mark_box(board_number, box, 'X')
                return board_number, box
        assert assertion, 'No valid moves'

    def check_monoid(self, move):
        if BoardCalculations.find_composite(self.notactoe) in BoardCalculations.COLORED_MONOIDS:
            return True
        else:
            return False