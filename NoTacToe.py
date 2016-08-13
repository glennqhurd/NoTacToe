import logging


class NoTacToe:

    DEFAULT_NUM_BOARDS = 3

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