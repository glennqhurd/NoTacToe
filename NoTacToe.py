import logging

class NoTacToe:

    DEFAULT_NUM_BOARDS = 3
    LOSING_POSITIONS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (6, 7, 8),
                        (2, 4, 6))

    def __init__(self):
        self.active_boards = self.DEFAULT_NUM_BOARDS
        self.board_list = []
        self.number_dead = 0
        self.current_player = 1

    def create_boards(self):
        self.board_list = []
        for i in range(self.active_boards):
            temp_board = []
            for j in range(9):
                temp_board.append(' ')
            self.board_list.append(temp_board)
            logging.debug(self.board_list[i])

    def mark_x(self, board_number, box):
        if self.is_dead(self.board_list[board_number]):
            return False
        if self.board_list[board_number][box] != 'X':
            self.board_list[board_number][box] = 'X'
            self.check_loser(self.board_list[board_number])
            return True
        else:
            return False

    def check_loser(self, board):
        for i in self.LOSING_POSITIONS:
            if board[i[0]] == 'X' and board[i[1]] == 'X' and board[i[2]] == 'X':
                self.number_dead += 1
                return True
        return False
        # if self.board_list[board_number][0] == 'X':
        #     if self.board_list[board_number][1] == 'X':
        #         if self.board_list[board_number][2] == 'X':
        #             return True
        #     if self.board_list[board_number][3] == 'X':
        #         if self.board_list[board_number][6] == 'X':
        #             return True
        #     if self.board_list[board_number][4] == 'X':
        #         if self.board_list[board_number][8] == 'X':
        #             return True
        # if self.board_list[board_number][1] == 'X':
        #     if self.board_list[board_number][4] == 'X':
        #         if self.board_list[board_number][7] == 'X':
        #             return True
        # if self.board_list[board_number][2] == 'X':
        #     if self.board_list[board_number][5] == 'X':
        #         if self.board_list[board_number][8] == 'X':
        #             return True
        #     if self.board_list[board_number][4] == 'X':
        #         if self.board_list[board_number][6] == 'X':
        #             return True
        # if self.board_list[board_number][3] == 'X':
        #     if self.board_list[board_number][4] == 'X':
        #         if self.board_list[board_number][5] == 'X':
        #             return True
        # if self.board_list[board_number][6] == 'X':
        #     if self.board_list[board_number][7] == 'X':
        #         if self.board_list[board_number][8] == 'X':
        #             return True
        # return False

    def is_dead(self, board):
        if self.check_loser(board):
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