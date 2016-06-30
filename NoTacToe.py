import logging

class NoTacToe:

    DEFAULT_NUM_BOARDS = 3

    def __init__(self):
        self.active_boards = self.DEFAULT_NUM_BOARDS
        self.board_list = []
        self.current_player = 1

    def create_boards(self):
        self.board_list = []
        for i in range(self.active_boards):
            temp_board = []
            for j in range(9):
                temp_board.append(' ')
            self.board_list.append(temp_board)
            logging.debug(self.board_list[i])

    def mark_x(self, board_number, box_list):
        for i in box_list:
            self.board_list[board_number][i] = 'X'
        logging.debug(self.board_list[board_number])
        return self.board_list[board_number]

    def check_loser(self, board_number):
        if self.board_list[board_number][0] == 'X':
            if self.board_list[board_number][1] == 'X':
                if self.board_list[board_number][2] == 'X':
                    return True
            if self.board_list[board_number][3] == 'X':
                if self.board_list[board_number][6] == 'X':
                    return True
            if self.board_list[board_number][4] == 'X':
                if self.board_list[board_number][8] == 'X':
                    return True
        if self.board_list[board_number][1] == 'X':
            if self.board_list[board_number][4] == 'X':
                if self.board_list[board_number][7] == 'X':
                    return True
        if self.board_list[board_number][2] == 'X':
            if self.board_list[board_number][5] == 'X':
                if self.board_list[board_number][8] == 'X':
                    return True
            if self.board_list[board_number][4] == 'X':
                if self.board_list[board_number][6] == 'X':
                    return True
        if self.board_list[board_number][3] == 'X':
            if self.board_list[board_number][4] == 'X':
                if self.board_list[board_number][5] == 'X':
                    return True
        if self.board_list[board_number][6] == 'X':
            if self.board_list[board_number][7] == 'X':
                if self.board_list[board_number][8] == 'X':
                    return True
        return False

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

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    notactoe = NoTacToe()
    notactoe.create_boards()