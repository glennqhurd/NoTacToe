class Computer_Player:

    def __init__(self, notactoe):
        self.notactoe = notactoe
        self.total_board = []
        active = self.notactoe.get_active_boards()
        for i in range(len(active)):
            self.total_board.append(active[i])

    def get_board_info(self):
        return self.total_board