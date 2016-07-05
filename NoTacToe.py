import logging

class NoTacToe:

    DEFAULT_NUM_BOARDS = 3
    LOSING_POSITIONS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def __init__(self):
        self.active_boards = self.DEFAULT_NUM_BOARDS
        self.board_list = []
        self.dead_boards = []
        self.current_player = 1

    def create_boards(self):
        self.board_list = []
        for i in range(self.active_boards):
            temp_board = []
            for j in range(9):
                temp_board.append(' ')
            self.board_list.append(temp_board)
            logging.debug(self.board_list[i])

    def reset_game(self):
        self.create_boards()
        self.dead_boards = []
        self.current_player = 1

    def mark_x(self, board_number, box):
        if self.is_dead(self.board_list[board_number], board_number):
            return False
        if self.board_list[board_number][box] != 'X':
            self.board_list[board_number][box] = 'X'
            self.check_loser(self.board_list[board_number], board_number)
            return True
        else:
            return False

    def check_loser(self, board, index):
        for i in self.LOSING_POSITIONS:
            if board[i[0]] == 'X' and board[i[1]] == 'X' and board[i[2]] == 'X':
                exists = False
                for i in range(len(self.dead_boards)):
                    if self.dead_boards[i] == index:
                        exists = True
                if not exists:
                    self.dead_boards.append(index)
                return True
        return False

    def is_dead(self, board, index):
        if self.check_loser(board, index):
            return True
        return False

    def set_active_boards(self, number):
        self.active_boards = number

    def get_active(self):
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