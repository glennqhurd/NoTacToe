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
        self.canvas_total = 5
        self.display_window()
        self.paint_canvas()
        self.root.mainloop()

    def display_window(self):
        self.widgets['window_frame'] = Frame(self.root)
        self.widgets['window_frame'].grid(row=0)
        for i in range(6):
            self.widgets['canvas'][i] = Canvas(self.widgets['window_frame'], width=300, height=300)
            self.widgets['canvas'][i].grid(row=(i/3), column=(i%3), padx=10, pady=10)

    def paint_canvas(self):
        for i in range(self.MAX_CANVAS):
            self.widgets['canvas'][i].delete("all")
            self.widgets['canvas'][i].unbind('<Button-1>')
        for i in range(self.canvas_total):
            self.widgets['canvas'][i].bind('<Button-1>', self.click)
            self.widgets['canvas'][i].create_line(0, 100, 300, 100)
            self.widgets['canvas'][i].create_line(0, 200, 300, 200)
            self.widgets['canvas'][i].create_line(100, 0, 100, 300)
            self.widgets['canvas'][i].create_line(200, 0, 200, 300)

    def drawX(self, box, canvas):
        canvas.create_line(((box % 3) * 100 + 20), ((int(box / 3) * 100) + 20),
                                                  ((box % 3) * 100 + 80), ((int(box / 3) * 100) + 80))
        canvas.create_line(((box % 3) * 100 + 20), ((int(box / 3) * 100) + 80),
                                                  ((box % 3) * 100 + 80), ((int(box / 3) * 100) + 20))

    def click(self, event):
        box = self.box_number(event.x, event.y)
        self.drawX(box, event.widget)

    def box_number(self, x, y):
        # If clicked on a line returns None
        if x > 5 and x < 95:
            if y > 5 and y < 95:
                return 0
            elif y > 105 and y < 195:
                return 3
            elif y > 205 and y < 295:
                return 6
        elif x > 105 and x < 195:
            if y > 5 and y < 95:
                return 1
            elif y > 105 and y < 195:
                return 4
            elif y > 205 and y < 295:
                return 7
        elif x > 205 and x < 295:
            if y > 5 and y < 95:
                return 2
            elif y > 105 and y < 195:
                return 5
            elif y > 205 and y < 295:
                return 8

if __name__ == '__main__':
    ntt = NoTacToe()
