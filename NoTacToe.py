import logging

import BoardCalculations


class NoTacToe:

    DEFAULT_NUM_BOARDS = 3
    LOSING_POSITIONS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def __init__(self):
        self.num_active_boards = self.DEFAULT_NUM_BOARDS
        self.board_list = []
        self.dead_boards = set()
        self.current_player = 1
        self.reset_game()

    # resets all the member variables and boards to a default state
    def reset_game(self):
        self.board_list = []
        for i in range(self.num_active_boards):
            temp_board = [' '] * 9
            self.board_list.append(temp_board)
        self.dead_boards = set()
        self.current_player = 1

    # changes the board by replacing a ' ' with an 'X' if there isn't already an 'X' in place
    def mark_box(self, board_number, box, symbol):
        if not self.check_box_legal(board_number, box) and symbol == 'X':
            return False
        else:
            self.board_list[board_number][box] = symbol
            self.check_loser(board_number)
            return True

    def check_box_legal(self, board_number, box):
        return self.board_list[board_number][box] == ' ' and board_number not in self.dead_boards

    def check_box_winning(self, board_number, box):
        if self.check_box_legal(board_number, box):
            self.mark_box(board_number, box, 'X')
            if board_number not in self.dead_boards:
                if BoardCalculations.multiply(self) in BoardCalculations.COLORED_MONOIDS:
                    return True
            self.remove_from_dead(board_number)
            self.mark_box(board_number, box, ' ')
        return False

    # check_loser checks the board to see if there are three Xs in a line and if so checks if the list dead_boards has
    # a value equal to index.  If the value doesn't exist it add index to the dead_boards list.
    def check_loser(self, index):
        for i in self.LOSING_POSITIONS:
            if (self.board_list[index][i[0]] == 'X' and self.board_list[index][i[1]] == 'X' and
                        self.board_list[index][i[2]] == 'X'):
                self.dead_boards.add(index)
                return True
        return False

    def remove_from_dead(self, index):
        if index in self.dead_boards:
            self.dead_boards.remove(index)

    # set and get methods for various member variables
    def set_num_active_boards(self, number):
        self.num_active_boards = number

    def get_num_active_boards(self):
        return self.num_active_boards

    def set_board(self, board_number, list):
        self.board_list[board_number] = list

    def get_board(self, board_number):
        return self.board_list[board_number]

    def set_player(self, player):
        self.current_player = player

    def get_player(self):
        return self.current_player

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    notactoe = NoTacToe()