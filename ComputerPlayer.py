import logging
import random

import BoardCalculations
import NoTacToe


class ComputerPlayer:
    def __init__(self, notactoe):
        self.notactoe = notactoe
        self.testtactoe = NoTacToe.NoTacToe()
        self.find_winning = True

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

    # Uses self.find_winning to determine whether the computer plays smart or not, True for smart False for not.
    def make_move(self):
        if self.find_winning:
            total_length = self.notactoe.get_num_active_boards() * 9
            move = random.randint(0, (total_length - 1))
            for i in range(total_length):
                board_number = ((move + i) % total_length) / 9
                box = (move + i) % 9
                if BoardCalculations.check_box_winning(board_number, box, self.notactoe.board_list,
                                                       self.notactoe.dead_boards):
                    BoardCalculations.mark_box(board_number, box, self.notactoe.board_list, self.notactoe.dead_boards,
                                               'X')
                    logging.debug("Computer smart move Board number: %d Box: %d", board_number, box)
                    return board_number, box
        total_length = self.notactoe.get_num_active_boards() * 9
        move = random.randint(0, (total_length - 1))
        for i in range(total_length):
            board_number = ((move + i) % total_length) / 9
            box = (move + i) % 9
            if BoardCalculations.check_box_legal(board_number, box, self.notactoe.board_list,
                                                 self.notactoe.dead_boards):
                BoardCalculations.mark_box(board_number, box, self.notactoe.board_list, self.notactoe.dead_boards, 'X')
                logging.debug("Computer dumb move Board number: %d Box: %d", board_number, box)
                return board_number, box
        assert False, 'No valid moves'

    def check_monoid(self, move):
        return BoardCalculations.find_composite(self.notactoe) in BoardCalculations.COLORED_MONOIDS

    #Made a helper function that can toggle whether or not self.find_winning is true or false
    def toggle_winning(self, winning):
        self.find_winning = winning
