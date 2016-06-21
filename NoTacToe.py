from Tkinter import *
from ttk import *

class NoTacToe:

    MAX_CANVAS = 6
    TAG_TUPLE = ('one', 'two', 'three', 'four', 'five', 'six')
    TAG_DICT = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}

    def __init__(self):
        self.root = Tk()
        self.widgets = {}
        self.widgets['canvas'] = {}
        self.canvas_total = 3
        title_frame = Frame(self.root)
        title_frame.grid(row=0, columnspan=2)
        Label(title_frame, text='NoTacToe: All X\'s, three in a row loses.').grid(row=0)
        self.canvas_window()
        self.root.mainloop()

    def canvas_window(self):
        self.widgets['canvas_frame'] = Frame(self.root)
        self.widgets['canvas_frame'].grid(row=1)
        for i in range(6):
            self.widgets['canvas'][i] = Canvas(self.widgets['canvas_frame'], width=150, height=150)
            self.widgets['canvas'][i].grid(row=(i/3), column=(i%3), padx=10, pady=10)
        self.paint_canvas()

    def paint_canvas(self):
        for i in range(self.MAX_CANVAS):
            self.widgets['canvas'][i].delete("all")
            self.widgets['canvas'][i].unbind('<Button-1>')
        for i in range(self.canvas_total):
            self.widgets['canvas'][i].bind('<Button-1>', self.click)
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

    def click(self, event):
        box = self.box_number(event.x, event.y)
        if box >= 0:
            self.drawX(box, event.widget)

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

if __name__ == '__main__':
    ntt = NoTacToe()
