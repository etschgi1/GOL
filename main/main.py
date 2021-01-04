from tkinter import *
import time


class CustomButton(object):
    """
    int row,col Coordinates
    bool state state alive or dead
    int neighbors count of neighbors
    """

    def __init__(self, row, col, state, neighbors, Gameboard):
        self.row = row
        self.col = col
        self.index = row*Gameboard.width+col
        self.state = state
        self.neighbors = neighbors
        self.Gameboard = Gameboard
        # setup button
        self.button = Button(master=self.Gameboard.FrameGrid, width=2, height=1,
                             bg="black",
                             command=self.Buttonclicked)
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


class Gameboard(object):
    """
    docstring
    """

    def __init__(self, height, width):
        self.root = Tk()
        self.root.geometry('600x600')  # geometry setup
        # top menu
        self.FrameTopNavigation = Frame(master=self.root)
        self.FrameTopNavigation.place(x=0, y=0, width=600, height=50)
        # button grid
        self.FrameGrid = Frame(master=self.root)
        self.FrameGrid.place(x=0, y=55, width=600, height=540)

        self.height = height
        self.width = width
        self.buttons = []
        self.run = Button(master=self.FrameTopNavigation,
                          width=20, height=5, bg="white", command=self.runSim,
                          text="run", activebackground="green")
        self.run.place(x=0, y=0, width=250, height=50)

    def buildGrid(self):
        for i in range(self.height):
            for j in range(self.width):
                # +1 row for other buttons up top
                self.buttons.append(CustomButton(i, j, 0, 0, self))

    def runSim(self):
        self.run.config(state=DISABLED)  # deactivate start
        print("run sim")
        dirtySim(self, self.height, self.width)

        # todo kill all buttons start new
        self.run.config(state=ACTIVE)


def dirtySim(Gb, height, width):
    cellcount = height*width
    for cellrow in range(height):  # check if cell should live or die
        for cellcol in range(width):
            countNeighbors(Gb, Gb.buttons[cellrow*width+cellcol])


def countNeighbors(Gb, Cell):
    Cellindex = Cell.index
    for rowrelative in range(-1, 2):  # iterate over neighbors
        for colrelative in range(-1, 2):
            if(rowrelative == colrelative and colrelative == 0):  # dont count oneself
                continue
            try:
                # count alive neighbors
                if(Gb.buttons[Cellindex+colrelative+(rowrelative*Gb.width)].state == 1):
                    Gb.buttons[Cellindex].neighbors += 1
            except:
                continue

    print("Cell: r: {} c: {} state: {}, Neighbors {}".format(Cell.row, Cell.col,
                                                             "LIFE" if Cell.state == 1 else "XXXX", Cell.neighbors))


board = Gameboard(3, 3)
board.buildGrid()
board.root.mainloop()
