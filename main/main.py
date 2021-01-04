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
        self.button = Button(self.Gameboard.root, width=10, height=5, bg="black",
                             command=self.Buttonclicked,)
        self.button.grid(row=row, column=col)

    def ChangeButtonColor(self):
        if(self.state == 0):
            self.button.config(bg="white")
        else:
            self.button["bg"] = "black"

    def Buttonclicked(self):
        if self.state == 1:
            self.ChangeButtonColor()
            self.state = 0
        else:
            self.ChangeButtonColor()
            self.state = 1
        print("state: {}".format(self.state))


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
