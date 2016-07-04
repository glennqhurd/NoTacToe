from Tkinter import *
from ttk import *

from NoTacToe import *


class NoTacToeUI:

    MAX_CANVAS = 6
    ACTIVE_BOARDS = 3
    TAG_TUPLE = ('one', 'two', 'three', 'four', 'five', 'six')
    TAG_DICT = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}

    def __init__(self):
        self.notactoe = NoTacToe()
        self.notactoe.create_boards()
        self.root = Tk()
        self.widgets = {}
        self.widgets['canvas'] = {}
        self.notactoe.set_active_boards(self.ACTIVE_BOARDS)
        title_frame = Frame(self.root)
        title_frame.grid(row=0, columnspan=2)
        Label(title_frame, text='NoTacToe: All X\'s, three in a row loses.').grid(row=0)
        self.widgets['player_label'] = Label(title_frame, text='Player 1 turn')
        self.widgets['player_label'].grid(row=1)
        self.canvas_window()
        self.root.mainloop()

    def canvas_window(self):
        self.widgets['canvas_frame'] = Frame(self.root)
        self.widgets['canvas_frame'].grid(row=1)
        for i in range(self.MAX_CANVAS):
            self.widgets['canvas'][i] = Canvas(self.widgets['canvas_frame'], width=150, height=150)
            self.widgets['canvas'][i].grid(row=(i/3), column=(i%3), padx=10, pady=10)
        self.paint_canvas()

    def paint_canvas(self):
        for i in range(self.MAX_CANVAS):
            self.widgets['canvas'][i].delete("all")
            self.widgets['canvas'][i].unbind('<Button-1>')
        for i in range(self.notactoe.get_active()):
            logging.debug(i)
            self.widgets['canvas'][i].bind('<Button-1>', lambda e, i=i: self.click(e, i))
            self.widgets['canvas'][i].create_line(0, 50, 150, 50)
            self.widgets['canvas'][i].create_line(0, 100, 150, 100)
            self.widgets['canvas'][i].create_line(50, 0, 50, 150)
            self.widgets['canvas'][i].create_line(100, 0, 100, 150)

    def input_window(self):
        self.widgets['input_frame'] = Frame(self.root)
        self.widgets['input_frame'].grid(row=1, column=1)


    def drawX(self, box, canvas):
        canvas.create_line(((box % 3) * 50 + 10), ((int(box / 3) * 50) + 10),
                                                  ((box % 3) * 50 + 40), ((int(box / 3) * 50) + 40))
        canvas.create_line(((box % 3) * 50 + 10), ((int(box / 3) * 50) + 40),
                                                  ((box % 3) * 50 + 40), ((int(box / 3) * 50) + 10))

    def click(self, event, index):
        logging.debug(index)
        box = self.box_number(event.x, event.y)
        if box >= 0:
            if self.notactoe.mark_x(index, box):
                self.drawX(box, event.widget)
                self.change_player()

    def box_number(self, x, y):
        # If clicked on a line returns None
        if x > 3 and x < 48:
            if y > 3 and y < 48:
                return 0
            elif y > 53 and y < 98:
                return 3
            elif y > 103 and y < 148:
                return 6
        elif x > 53 and x < 98:
            if y > 3 and y < 48:
                return 1
            elif y > 53 and y < 98:
                return 4
            elif y > 103 and y < 148:
                return 7
        elif x > 103 and x < 148:
            if y > 3 and y < 48:
                return 2
            elif y > 53 and y < 98:
                return 5
            elif y > 103 and y < 148:
                return 8

    def change_player(self):
        if self.notactoe.get_player() == 1 and self.notactoe.number_dead == self.ACTIVE_BOARDS:
            self.widgets['player_label'].config(text='Player 2 wins!')
        elif self.notactoe.get_player() == 2 and self.notactoe.number_dead == self.ACTIVE_BOARDS:
            self.widgets['player_label'].config(text='Player 1 wins!')
        elif self.notactoe.get_player() == 1:
            self.widgets['player_label'].config(text='Player 2 turn')
            self.notactoe.set_player(2)
        elif self.notactoe.get_player() == 2:
            self.widgets['player_label'].config(text='Player 1 turn')
            self.notactoe.set_player(1)
        else:
            return False

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    nttui = NoTacToeUI()
