import unittest

from NoTacToe import *


class NoTacToe_test(unittest.TestCase):
    def test_mark_x(self):
        notactoe = NoTacToe()
        notactoe.create_boards()
        test_board = ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        index_list = [0]
        self.assertEqual(test_board, notactoe.mark_x(0, index_list))
        test_board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        index_list = [1, 2]
        self.assertEqual(test_board, notactoe.mark_x(0, index_list))
        test_board = [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ']
        index_list = [3]
        self.assertEqual(test_board, notactoe.mark_x(1, index_list))

if __name__ == '__main__':
    unittest.main()