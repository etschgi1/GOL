from tkinter import *


class CustomButton(object):
    """
    int row,col Coordinates
    bool state state alive or dead
    int neighbors count of neighbors 
    """

    def __init__(self, row, col, state, neighbors, Gameboard):
        self.row = row
        self.col = col
        self.state = state
        self.neighbors = neighbors
        self.Gameboard = Gameboard
        # setup button
        self.button = Button(self.Gameboard.root, width=10, height=5, bg="white", text="row: "+str(row) +
                             "col: "+str(col), command=self.Buttonclicked).grid(row=row, column=col)

    def Buttonclicked(self):
        self.button.configure(bg="blue")


class Gameboard(object):
    """
    docstring
    """

    def __init__(self, height, width):
        self.root = Tk()
        self.height = height
        self.width = width
        self.buttons = []

    def buildGrid(self):
        for i in range(self.height):
            for j in range(self.width):
                self.buttons.append(CustomButton(i, j, 0, 0, self))


board = Gameboard(3, 3)

board.buildGrid()
board.root.mainloop()
