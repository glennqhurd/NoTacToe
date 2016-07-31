import logging

class NoTacToe:

    DEFAULT_NUM_BOARDS = 3
    LOSING_POSITIONS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def __init__(self):
        self.active_boards = self.DEFAULT_NUM_BOARDS
        self.board_list = []
        for i in range(self.active_boards):
            temp_board = []
            for j in range(9):
                temp_board.append(' ')
            self.board_list.append(temp_board)
            logging.debug(self.board_list[i])
        self.dead_boards = set()
        self.current_player = 1

    # resets the boards to a default state
    def create_boards(self):
        self.board_list = []
        for i in range(self.active_boards):
            temp_board = []
            for j in range(9):
                temp_board.append(' ')
            self.board_list.append(temp_board)
            logging.debug(self.board_list[i])

    # resets all the member variables and boards to a default state
    def reset_game(self):
        self.create_boards()
        self.dead_boards = set()
        self.current_player = 1

    # changes the board by replacing a ' ' with an 'X' if there isn't already an 'X' in place
    def mark_x(self, board_number, box):
        if not self.check_box(board_number, box):
            return False
        else:
            self.board_list[board_number][box] = 'X'
            self.check_loser(board_number)
            return True

    def check_box(self, board_number, box):
        if self.board_list[board_number][box] == ' ' and board_number not in self.dead_boards:
            return True
        else:
            return False

    # check_loser checks the board to see if there are three Xs in a line and if so checks if the list dead_boards has
    # a value equal to index.  If the value doesn't exist it add index to the dead_boards list.
    def check_loser(self, index):
        for i in self.LOSING_POSITIONS:
            if self.board_list[index][i[0]] == 'X' and self.board_list[index][i[1]] == 'X' and \
                            self.board_list[index][i[2]] == 'X':
                if index not in self.dead_boards:
                    self.dead_boards.add(index)
                return True
        return False

    # set and get methods for various member variables
    def set_active_boards(self, number):
        self.active_boards = number

    def get_active_boards(self):
        return self.active_boards

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
    notactoe.create_boards()