import unittest

from Computer_Player import *
from NoTacToe import *


class Computer_Player_test(unittest.TestCase):
    def test_init_and_get(self):
        notactoe = NoTacToe
        comp = Computer_Player(notactoe)
        test_board = []
        for i in range(3):
            test_board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
        self.assertEqual(test_board, comp.get_board_info())

if __name__ == '__main__':
    unittest.main()