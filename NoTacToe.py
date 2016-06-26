

class NoTacToe:

    DEFAULT_NUM_BOARDS = 3

    def __init__(self):
        self.active_boards = self.DEFAULT_NUM_BOARDS
        self.board_list = []
        self.current_player = 1

    def set_active_boards(self, number):
        self.active_boards = number

    def get_active(self):
        return self.active_boards

    def set_board_list(self, list):
        self.board_list = list

    def get_board_list(self):
        return self.board_list

    def set_player(self, player):
        self.current_player = player

    def get_player(self):
        return self.current_player