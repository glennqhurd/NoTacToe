import unittest

from NoTacToe import *


class NoTacToe_test(unittest.TestCase):
    def test_mark_x(self):
        notactoe = NoTacToe()
        notactoe.create_boards()
        self.assertEqual(True, notactoe.mark_x(0, 0))
        self.assertEqual(False, notactoe.mark_x(0, 0))
        self.assertEqual(True, notactoe.mark_x(1, 3))
        board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        notactoe.set_board(0, board)
        self.assertEqual(False, notactoe.mark_x(0, 0))

    def test_check_loser(self):
        notactoe = NoTacToe()
        notactoe.create_boards()
        self.assertEqual(False, notactoe.check_loser(notactoe.get_board(0)))
        notactoe.mark_x(0, 0)
        notactoe.mark_x(0, 1)
        notactoe.mark_x(0, 2)
        self.assertEqual(True, notactoe.check_loser(notactoe.get_board(0)))
        notactoe.mark_x(1, 1)
        notactoe.mark_x(1, 4)
        notactoe.mark_x(1, 7)
        self.assertEqual(True, notactoe.check_loser(notactoe.get_board(1)))
        notactoe.mark_x(2, 2)
        notactoe.mark_x(2, 4)
        notactoe.mark_x(2, 6)
        self.assertEqual(True, notactoe.check_loser(notactoe.get_board(2)))

if __name__ == '__main__':
    unittest.main()