import unittest

from Computer_Player import *


class Computer_Player_test(unittest.TestCase):
    def test_init_and_get(self):
        comp = Computer_Player()
        test_board = []
        for i in range(3):
            test_board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
        self.assertEqual(test_board, comp.get_board_info())

    def test_get_variable(self):
        comp = Computer_Player()
        test_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual('c', comp.get_variable(test_board))
        test_board = [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']
        self.assertEqual('c2', comp.get_variable(test_board))
        test_board = ['X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual('ad', comp.get_variable(test_board))
        test_board = ['X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual('b', comp.get_variable(test_board))
        test_board = ['X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ']
        self.assertEqual('b', comp.get_variable(test_board))

if __name__ == '__main__':
    unittest.main()