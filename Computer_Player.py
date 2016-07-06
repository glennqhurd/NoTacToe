from NoTacToe import *

class Computer_Player:

    def __init__(self):
        self.notactoe = NoTacToe()
        self.total_board = []
        active = self.notactoe.get_active_boards()
        for i in range(active):
            board_list = self.notactoe.get_board(i)
            self.total_board.append(board_list)

    def set_notactoe(self, notactoe_var):
        self.notactoe = notactoe_var

    def get_board_info(self):
        return self.total_board