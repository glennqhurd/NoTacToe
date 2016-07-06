class Computer_Player:

    def __init__(self, notactoe):
        self.notactoe = notactoe
        self.current_board = []

    def set_current_board(self, board):
        self.current_board = board

    def get_board_info(self):
        active = self.notactoe.get_active_boards()
        board_number = active.index(self.current_board)
        return board_number