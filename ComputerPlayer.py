import random


class ComputerPlayer:
    def __init__(self, notactoe):
        self.notactoe = notactoe

    def random_move(self):
        total_length = self.notactoe.get_num_active_boards() * 9
        move = random.randint(0, (total_length - 1))
        for i in range(total_length):
            board_number = ((move + i) % total_length) / 9
            box = (move + i) % 9
            if self.notactoe.check_box(board_number, box):
                self.notactoe.mark_x(board_number, box)
                return board_number, box
        return False, 'No valid moves'

