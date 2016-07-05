from Tkinter import *
from ttk import *

from NoTacToe import *


class NoTacToeUI:

    # Constants for set values hard coded in the program
    MAX_CANVAS = 3
    TAG_TUPLE = ('one', 'two', 'three')
    TAG_DICT = {'one': 1, 'two': 2, 'three': 3}
    BOARD_NUMBER_TUPLE = (3, 1, 2, 3)
    PLAYER_MODE = 0
    COMPUTER_MODE = 1


    def __init__(self):
        # Creates a new instance of NoTacToe (the game logic class)
        self.notactoe = NoTacToe()
        self.notactoe.create_boards()
        # root is the base window that holds the frames
        self.root = Tk()
        # widgets is a dict used to store all the member variable widgets in the program
        self.widgets = {}
        # widgets['canvas'] is the dict within a dict that store all the Canvas member variables
        self.widgets['canvas'] = {}
        self.active_boards = 3
        self.notactoe.set_active_boards(self.active_boards)
        title_frame = Frame(self.root)
        title_frame.grid(row=0, columnspan=2)
        Label(title_frame, text='Time to play NoTacToe!').grid(row=0)
        Label(title_frame, text='Rules: All X\'s, three in a row loses.  Once a board loses it becomes dead.'
                                'Dead boards can\n no longer be played on, and once all boards are dead the '
                                'game is over.  The player who \nkilled the last board loses.').grid(row=1)
        self.widgets['player_label'] = Label(title_frame, text='Player 1 turn')
        self.widgets['player_label'].grid(row=2)
        self.canvas_window()
        self.control_window()

    # Creates and displays the canvas objects in a frame
    def canvas_window(self):
        self.widgets['canvas_frame'] = Frame(self.root)
        self.widgets['canvas_frame'].grid(row=1)
        for i in range(self.MAX_CANVAS):
            self.widgets['canvas'][i] = Canvas(self.widgets['canvas_frame'], width=150, height=150)
            self.widgets['canvas'][i].grid(row=(i/3), column=(i%3), padx=10, pady=10)
        self.paint_canvas()

    # Creates and displays the control options frame
    def control_window(self):
        self.widgets['control_frame'] = Frame(self.root)
        self.widgets['control_frame'].grid(row=0, column=1, rowspan=2)
        Label(self.widgets['control_frame'], text='Game mode:').grid(row=0)
        self.widgets['board_variable'] = IntVar()
        self.widgets['board_variable'].set(self.active_boards)
        self.widgets['board_option'] = OptionMenu(self.widgets['control_frame'], self.widgets['board_variable'],
                                                  *self.BOARD_NUMBER_TUPLE, command=self.board_option_callback)
        self.widgets['board_option'].grid(row=1, padx=15, pady=15)
        self.widgets['radio_variable'] = IntVar()
        self.widgets['radio_variable'].set(0)
        self.widgets['radiobutton_player'] = Radiobutton(self.widgets['control_frame'], text="Versus Player",
                                                         variable=self.widgets['radio_variable'],
                                                         value=self.PLAYER_MODE)
        self.widgets['radiobutton_player'].grid(row=2, sticky='W', padx=15)
        self.widgets['radiobutton_computer'] = Radiobutton(self.widgets['control_frame'], text="Versus Computer",
                                                           variable=self.widgets['radio_variable'],
                                                           value=self.COMPUTER_MODE)
        self.widgets['radiobutton_computer'].grid(row=3, sticky='W', padx=15)

    # Paints the number of canvas objects based on active boards
    def paint_canvas(self):
        for i in range(self.MAX_CANVAS):
            self.widgets['canvas'][i].delete("all")
            self.widgets['canvas'][i].unbind('<Button-1>')
        for i in range(self.notactoe.get_active_boards()):
            logging.debug(i)
            self.widgets['canvas'][i].bind('<Button-1>', lambda e, i=i: self.click(e, i))
            self.widgets['canvas'][i].create_line(0, 50, 150, 50)
            self.widgets['canvas'][i].create_line(0, 100, 150, 100)
            self.widgets['canvas'][i].create_line(50, 0, 50, 150)
            self.widgets['canvas'][i].create_line(100, 0, 100, 150)

    def drawX(self, box, canvas):
        canvas.create_line(((box % 3) * 50 + 10), ((int(box / 3) * 50) + 10),
                                                  ((box % 3) * 50 + 40), ((int(box / 3) * 50) + 40))
        canvas.create_line(((box % 3) * 50 + 10), ((int(box / 3) * 50) + 40),
                                                  ((box % 3) * 50 + 40), ((int(box / 3) * 50) + 10))

    # Callback to respond when mouse click occurs in a canvas that the click is bound to.  event returns where the
    # click occurred and what canvas was clicked.  index tells the method mark_x which canvas was clicked for the
    # NoTacToe method
    def click(self, event, index):
        logging.debug(index)
        box = self.box_number(event.x, event.y)
        if box >= 0:
            if self.notactoe.mark_x(index, box):
                self.drawX(box, event.widget)
                self.change_player()

    # Returns the number of the box based on the x, y coordinates
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

    # Modifies widgets['player_label'] based on a method to find out current player and react accordingly
    def change_player(self):
        if self.notactoe.get_player() == 1 and len(self.notactoe.dead_boards) == self.active_boards:
            self.widgets['player_label'].config(text='Player 2 wins!')
            self.results_callback()
        elif self.notactoe.get_player() == 2 and len(self.notactoe.dead_boards) == self.active_boards:
            self.widgets['player_label'].config(text='Player 1 wins!')
            self.results_callback()
        elif self.notactoe.get_player() == 1:
            self.widgets['player_label'].config(text='Player 2 turn')
            self.notactoe.set_player(2)
        elif self.notactoe.get_player() == 2:
            self.widgets['player_label'].config(text='Player 1 turn')
            self.notactoe.set_player(1)
        else:
            return False

    def board_option_callback(self, unused_var):
        self.active_boards = self.widgets['board_variable'].get()
        self.notactoe.set_active_boards(self.active_boards)
        self.notactoe.reset_game()
        self.paint_canvas()


    def results_callback(self):
        self.widgets['results_window'] = Toplevel()
        self.widgets['results_window'].wm_title('Game Over')
        Label(self.widgets['results_window'],
              text='Game over!  Player %d wins!' % self.notactoe.current_player).grid(row=0, columnspan=2, pady=15,
                                                                                      padx=15)
        Button(self.widgets['results_window'], text='Play Again',
               command=lambda x=self.widgets['results_window']: self.play_again_callback(x)).grid(row=1, pady=(0, 15),
                                                                                                 padx=15)
        Button(self.widgets['results_window'], text='Quit', command=self.quit_game).grid(row=1, column=1, pady=(0, 15),
                                                                                         padx=15)

    def play_again_callback(self, window):
        self.notactoe.reset_game()
        self.paint_canvas()
        window.destroy()

    def quit_game(self):
        self.root.destroy()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    nttui = NoTacToeUI()
    nttui.root.mainloop()
