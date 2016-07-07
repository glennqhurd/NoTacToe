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

    def get_variable(self, board):
        # Board: ' ' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        if board == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']:
            return 'c'
        # Board: 'X' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        elif board == ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] or \
                        board == [' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' '] or \
                        board == [' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' '] or \
                        board == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X']:
            return '1'
        # Board: ' ' | 'X' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        elif board == [' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' '] or \
                        board == [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' '] or \
                        board == [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' '] or \
                        board == [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ']:
            return '1'
        # Board: ' ' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | 'X' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        elif board == [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']:
            return 'c2'
        # Board: 'X' | 'X' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        elif board == ['X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' '] or \
                        board == [' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' '] or \
                        board == [' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ', ' '] or \
                        board == [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'] or \
                        board == [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X'] or \
                        board == [' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' '] or \
                        board == [' ', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' '] or \
                        board == ['X', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ']:
            return 'ad'
        # Board: 'X' | ' ' | 'X'
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        elif board == ['X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' '] or \
                        board == [' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X'] or \
                        board == [' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X'] or \
                        board == ['X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ']:
            return 'b'
        # Board: 'X' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | 'X' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        elif board == ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '] or \
                        board == [' ', ' ', 'X', ' ', 'X', ' ', ' ', ' ', ' '] or \
                        board == [' ', ' ', ' ', ' ', 'X', ' ', 'X', ' ', ' '] or \
                        board == [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']:
            return 'b'
        # Board: 'X' | ' ' | ' '
        #       -----|-----|-----
        #        ' ' | ' ' | 'X'
        #       -----|-----|-----
        #        ' ' | ' ' | ' '
        elif board == ['X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' '] or \
                        board == [' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', ' '] or \
                        board == ['X', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' '] or \
                        board == [' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X', ' '] or \
                        board == [' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' '] or \
                        board == [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X'] or \
                        board == [' ', 'X', ' ', ' ', ' ', ' ', 'X', ' ', ' '] or \
                        board == [' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', 'X']:
            return 'b'