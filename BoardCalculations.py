import random

MONOID_LABELS = ('1', 'a', 'b', 'ab', 'b2', 'abc', 'c', 'ac', 'bc', 'abc', 'c2', 'ac2', 'bc2', 'abc2', 'd', 'ad', 'bd',
                 'abd')

BOARD_VALUES = {'         ': 'c', '    X    ': 'cc', 'XX       ': 'ad', 'X X      ': 'b',
                'X   X    ': 'b', 'X    X   ': 'b', 'X       X': 'a', ' X X     ': 'a',
                ' X  X    ': 'b', ' X     X ': 'a', 'XX X     ': 'b', 'XX  X    ': 'ab',
                'XX   X   ': 'd', 'XX    X  ': 'a', 'XX     X ': 'd', 'XX      X': 'd',
                'X X X    ': 'a', 'X X   X  ': 'ab', 'X X    X ': 'a', 'X   XX   ': 'a',
                ' X XX    ': 'ab', ' X X X   ': 'b', 'XX XX    ': 'a', 'XX X X   ': 'a',
                'XX X    X': 'a', 'XX  XX   ': 'b', 'XX  X X  ': 'b', 'XX   XX  ': 'b',
                'XX   X X ': 'ab', 'XX   X  X': 'ab', 'XX    XX ': 'b', 'XX    X X': 'b',
                'XX     XX': 'a', 'X X X  X ': 'b', 'X X   X X': 'a', 'X   XX X ': 'b',
                ' X X X X ': 'a', 'XX X X X ': 'b', 'XX X X  X': 'b', 'XX  XXX  ': 'a',
                'XX   XXX ': 'a', 'XX   XX X': 'a', 'XX X X XX': 'a'}


def board_value(board):
    return random.randint(0, 17)

def multiply(*nums):
    answer = 1
    for i in nums:
        answer *= i
    return answer % 18