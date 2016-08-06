from Tkinter import *
from ttk import *

import BoardCalculations
from ComputerPlayer import *
from NoTacToe import *


class NoTacToeUI:

    # Constants for set values hard coded in the program
    MAX_CANVAS = 3
    TAG_TUPLE = ('one', 'two', 'three')
    TAG_DICT = {'one': 1, 'two': 2, 'three': 3}
    BOARD_NUMBER_TUPLE = (3, 1, 2, 3)
    PLAYER_MODE = 0
    COMPUTER_MODE = 1
    MONOID_LABELS = ('1', 'a', 'b', 'ab', 'b2', 'abc', 'c', 'ac', 'bc', 'abc', 'c2', 'ac2', 'bc2', 'abc2', 'd', 'ad',
                     'bd', 'abd')

    def __init__(self):
        # Creates a new instance of NoTacToe (the game logic class)
        self.notactoe = NoTacToe()
        self.comp_player = ComputerPlayer(self.notactoe)
        self.notactoe.reset_game()
        # root is the base window that holds the frames
        self.root = Tk()
        # widgets is a dict used to store all the member variable widgets in the program
        self.widgets = {}
        # widgets['canvas'] is the dict within a dict that store all the Canvas member variables
        self.canvases = {}
        self.canvas_labels = {}
        self.game_in_progress = True
        self.active_boards = 3
        self.notactoe.set_num_active_boards(self.active_boards)
        title_frame = Frame(self.root)
        title_frame.grid(row=0, columnspan=2)
        Label(title_frame, text='Time to play NoTacToe!').grid(row=0)
        Label(title_frame, text='Rules:\n(1) Both players play X.\n(2) Once a board has three-in-a-row it dies.\n'
              '(3) The player who kills the last board loses.').grid(row=1, pady=10)
        self.widgets['player_label'] = Label(title_frame, text='Player 1 turn', font='bold')
        self.widgets['player_label'].grid(row=2)
        self.canvas_window()
        self.control_window()
        self.bottom_window()

    # Creates and displays the canvas objects in a frame
    def canvas_window(self):
        self.widgets['canvas_frame'] = Frame(self.root)
        self.widgets['canvas_frame'].grid(row=1, padx=15)
        for i in range(self.MAX_CANVAS):
            self.canvases[i] = Canvas(self.widgets['canvas_frame'], width=150, height=150)
            self.canvases[i].grid(row=(i/3), column=(i % 3), padx=10, pady=10)
            self.canvas_labels[i] = Label(self.widgets['canvas_frame'], text='1', width=2)
            self.canvas_labels[i].grid(row=(i / 3 + 1), column=(i % 3), padx=10, pady=(0, 10))
        self.paint_canvas()

    # Creates and displays the control options frame
    def control_window(self):
        self.widgets['control_frame'] = Frame(self.root)
        self.widgets['control_frame'].grid(row=0, column=1, rowspan=2)
        Label(self.widgets['control_frame'], text='Number of Boards:').grid(row=0)
        self.widgets['board_variable'] = IntVar()
        self.widgets['board_variable'].set(self.active_boards)
        self.widgets['board_option'] = OptionMenu(self.widgets['control_frame'], self.widgets['board_variable'],
                                                  *self.BOARD_NUMBER_TUPLE, command=self.board_option_callback)
        self.widgets['board_option'].grid(row=1, padx=20, pady=15)
        self.widgets['radio_variable'] = IntVar()
        self.widgets['radio_variable'].set(1)
        self.widgets['radiobutton_player'] = Radiobutton(self.widgets['control_frame'], text="Versus Player",
                                                         variable=self.widgets['radio_variable'],
                                                         value=self.PLAYER_MODE, command=self.reset_callback)
        self.widgets['radiobutton_player'].grid(row=2, sticky='W', padx=20)
        self.widgets['radiobutton_computer'] = Radiobutton(self.widgets['control_frame'], text="Versus Computer",
                                                           variable=self.widgets['radio_variable'],
                                                           value=self.COMPUTER_MODE, command=self.reset_callback)
        self.widgets['radiobutton_computer'].grid(row=3, sticky='W', padx=20)
        Label(self.widgets['control_frame'], text='Composite:').grid(row=4, padx=20, pady=(120, 5))
        self.widgets['composite_label'] = Label(self.widgets['control_frame'], text='1')
        self.widgets['composite_label'].grid(row=5, padx=20, pady=5)

    def bottom_window(self):
        self.widgets['bottom_frame'] = Frame(self.root)
        self.widgets['bottom_frame'].grid(row=2, columnspan=2)
        self.widgets['reset_button'] = Button(self.widgets['bottom_frame'], text='Reset Game',
                                              command=self.reset_callback)
        self.widgets['reset_button'].grid(row=0, pady=(0, 15))

    # Paints the number of canvas objects based on active boards
    def paint_canvas(self):
        for i in range(self.MAX_CANVAS):
            self.canvases[i].delete("all")
            self.canvases[i].unbind('<Button-1>')
            self.canvas_labels[i].config(text=' ')
        for i in range(self.notactoe.get_num_active_boards()):
            self.canvases[i].bind('<Button-1>', lambda e, j=i: self.click(e, j))
            self.canvases[i].create_line(0, 50, 150, 50)
            self.canvases[i].create_line(0, 100, 150, 100)
            self.canvases[i].create_line(50, 0, 50, 150)
            self.canvases[i].create_line(100, 0, 100, 150)
            self.canvas_labels[i].config(text='c')

    # Callback to respond when mouse click occurs in a canvas that the click is bound to.  event returns where the
    # click occurred and what canvas was clicked.  index tells the method mark_x which canvas was clicked for the
    # NoTacToe method

    def click(self, event, board_num):
        box = box_number(event.x, event.y)
        if box >= 0:
            if self.notactoe.mark_x(board_num, box):
                draw_x(box, event.widget)
                self.change_player()
                self.update_monoid_labels(board_num)
                if self.widgets['radio_variable'].get() == self.COMPUTER_MODE and self.game_in_progress:
                    board, box = self.comp_player.random_move()
                    draw_x(box, self.canvases[board])
                    self.change_player()
                    self.update_monoid_labels(board)

    def update_monoid_labels(self, board_num):
        self.canvas_labels[board_num].config(text=BoardCalculations.get_monoid(board_num, self.notactoe))

    # Modifies widgets['player_label'] based on a method to find out current player and react accordingly
    def change_player(self):
        if self.notactoe.get_player() == 1 and len(self.notactoe.dead_boards) == self.active_boards:
            self.widgets['player_label'].config(text='Player 2 wins!')
            self.notactoe.set_player(2)
            self.game_in_progress = False
            # self.results_callback()
        elif self.notactoe.get_player() == 2 and len(self.notactoe.dead_boards) == self.active_boards:
            self.widgets['player_label'].config(text='Player 1 wins!')
            self.notactoe.set_player(1)
            self.game_in_progress = False
            # self.results_callback()
        elif self.notactoe.get_player() == 1:
            self.widgets['player_label'].config(text='Player 2\'s turn')
            self.notactoe.set_player(2)
        elif self.notactoe.get_player() == 2:
            self.widgets['player_label'].config(text='Player 1\'s turn')
            self.notactoe.set_player(1)
        else:
            return False

    def board_option_callback(self, unused_var):
        self.active_boards = self.widgets['board_variable'].get()
        self.notactoe.set_num_active_boards(self.active_boards)
        self.notactoe.reset_game()
        self.paint_canvas()
        self.game_in_progress = True

    def reset_callback(self):
        self.notactoe.reset_game()
        self.paint_canvas()
        self.widgets['player_label'].config(text='Player 1\'s turn')
        self.notactoe.set_player(1)
        self.game_in_progress = True

    def translate_value(self, value):
        return self.MONOID_LABELS[value]


# Static functions
def draw_x(box, canvas):
    canvas.create_line(((box % 3) * 50 + 10), ((int(box / 3) * 50) + 10),
                       ((box % 3) * 50 + 40), ((int(box / 3) * 50) + 40))
    canvas.create_line(((box % 3) * 50 + 10), ((int(box / 3) * 50) + 40),
                       ((box % 3) * 50 + 40), ((int(box / 3) * 50) + 10))


# Returns the number of the box based on the x, y coordinates
def box_number(x, y):
    # If clicked on a line returns None
    if 3 < x < 48:
        if 3 < y < 48:
            return 0
        elif 53 < y < 98:
            return 3
        elif 103 < y < 148:
            return 6
    elif 53 < x < 98:
        if 3 < y < 48:
            return 1
        elif 53 < y < 98:
            return 4
        elif 103 < y < 148:
            return 7
    elif 103 < x < 148:
        if 3 < y < 48:
            return 2
        elif 53 < y < 98:
            return 5
        elif 103 < y < 148:
            return 8

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    nttui = NoTacToeUI()
    nttui.root.mainloop()
