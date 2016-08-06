import unittest

from ComputerPlayer import *
from NoTacToe import *


class Computer_Player_test(unittest.TestCase):
    # def test_init_and_get(self):
    #     comp = ComputerPlayer()
    #     test_board = 3
    #     self.assertEqual(test_board, comp.get_board_info())
    #
    # def test_get_variable(self):
    #     comp = ComputerPlayer()
    #     test_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    #     self.assertEqual('c', comp.get_variable(test_board))
    #     test_board = [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']
    #     self.assertEqual('c2', comp.get_variable(test_board))
    #     test_board = ['X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    #     self.assertEqual('ad', comp.get_variable(test_board))
    #     test_board = ['X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
    #     self.assertEqual('b', comp.get_variable(test_board))
    #     test_board = ['X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ']
    #     # self.assertEqual('b', comp.get_variable(test_board))
    #
    # def test_random_move(self):
    #     comp = ComputerPlayer()
    #     test = (2, 2)
    #     for i in range(2):
    #         for j in range(9):
    #             comp.notactoe.mark_x(i, j)
    #     comp.notactoe.mark_x(2, 0)
    #     comp.notactoe.mark_x(2, 1)
    #     comp.notactoe.mark_x(2, 4)
    #     comp.notactoe.mark_x(2, 5)
    #     comp.notactoe.mark_x(2, 6)
    #     self.assertEqual(test, comp.random_move())

    def test_get_variable(self):
        notactoe = NoTacToe()
        comp = ComputerPlayer(notactoe)
        notactoe.board_list[0] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual('c', comp.get_variable(0))
        notactoe.board_list[0] = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        self.assertEqual('1', comp.get_variable(0))


if __name__ == '__main__':
    unittest.main()