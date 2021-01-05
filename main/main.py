
"""Game of Life Implementation"""

import sys
import os
from tkinter import *
import time
import threading


# count for neighbors at which birth occurres
REBIRTH_COUNT = 3
# count at which (or lower) cells die out of lonliness
DEAD_FROM_LONELINESS = 1
# count at which (or higher) cells die of overpopulation
DEAD_FROM_OVERPOPULATION = 4

TIME_BETWEEN_STEPS = 0

GAME_HEIGHT = 50  # sets number of cells in column
GAME_WIDTH = 50  # sets number of cells in a row


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
        self.pixel = PhotoImage(width=1, height=1)
        self.button = Button(master=self.Gameboard.FrameGrid, image=self.pixel, width=10, height=10,
                             bg="black",
                             command=self.Buttonclicked)
        self.button.grid(row=row, column=col)

    def beBorn(self):
        self.Buttonclicked()

    def die(self):
        self.Buttonclicked()

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
        self.frameheight = height*17+50
        self.framewidth = width*17
        self.root.geometry("%dx%d" %
                           (self.framewidth, self.frameheight))  # geometry setup
        self.root.title("Game Of Live")
        self.root.iconphoto(False, PhotoImage(file="main\logo.png"))
        # top menu
        self.FrameTopNavigation = Frame(master=self.root)
        self.FrameTopNavigation.place(
            x=0, y=0, width=self.framewidth, height=50)
        # button grid
        self.FrameGrid = Frame(master=self.root)
        self.FrameGrid.place(x=0, y=55, width=self.framewidth,
                             height=self.frameheight-50)

        self.simrun = FALSE
        self.height = height
        self.width = width
        self.buttons = []
        self.pixel = PhotoImage(width=1, height=1)
        self.run = Button(master=self.FrameTopNavigation, image=self.pixel, compound="c",
                          width=self.framewidth/2, height=50, bg="#96ed6b", command=self.runSim,
                          text="run", activebackground="green")
        self.restart = Button(master=self.FrameTopNavigation, image=self.pixel, compound="c",
                              width=self.framewidth/2, height=50, bg="#ff8400", command=self.restart,
                              text="restart", activebackground="red")
        self.run.grid(row=0, column=0)
        self.restart.grid(row=0, column=1)

    def buildGrid(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(CustomButton(i, j, 0, 0, self))
            self.buttons.append(row)

    def restart(self):
        print("Restarting...")
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def runSim(self):
        self.run.config(state=DISABLED)
        if not self.simrun:
            self.simrun = TRUE
            print("run sim")
            t1 = threading.Thread(target=dirtySim, args=(self,
                                                         self.height, self.width), daemon=TRUE).start()


def dirtySim(Gb, height, width):
    while TRUE:
        cellcount = height*width
        for cellrow in range(height):  # check if cell should live or die
            for cellcol in range(width):
                countNeighbors(
                    Gb, Gb.buttons[cellrow][cellcol], cellrow, cellcol)
        makeStep(Gb)
        resetallneighborcounts(Gb)
        time.sleep(TIME_BETWEEN_STEPS)


def makeStep(Gb):
    for row in range(Gb.height):
        for col in range(Gb.width):
            # apply rules
            Cell = Gb.buttons[row][col]
            if(Cell.state == 0 and Cell.neighbors == REBIRTH_COUNT):  # resurect from the dead
                Cell.beBorn()
            elif(Cell.state == 1 and Cell.neighbors <= DEAD_FROM_LONELINESS):
                Cell.die()
            elif(Cell.state == 1 and Cell.neighbors >= DEAD_FROM_OVERPOPULATION):
                Cell.die()


def resetallneighborcounts(Gb):
    for row in range(Gb.height):
        for col in range(Gb.width):
            Gb.buttons[row][col].neighbors = 0


def countNeighbors(Gb, Cell, row, col):
    ownstate = Cell.state
    Cells = Gb.buttons
    if(ownstate == 1):  # add to neighbors +1
        for rowrel in range(-1, 2):
            for colrel in range(-1, 2):
                try:
                    rowneighbor = row+rowrel
                    colneighbor = col+colrel
                    if(rowneighbor == row and colneighbor == col):
                        continue
                    if(rowneighbor < 0 or colneighbor < 0):
                        continue
                    Cells[rowneighbor][colneighbor].neighbors += 1
                except:
                    continue


def printoutcell(Gb):
    for row in range(Gb.width):
        for col in range(Gb.height):
            Cell = Gb.buttons[row][col]
            print("Cell: r: {} c: {} state: {}, Neighbors {}".format(Cell.row, Cell.col,
                                                                     "LIFE" if Cell.state == 1 else "XXXX", Cell.neighbors))


def main():
    game = Gameboard(GAME_HEIGHT, GAME_WIDTH)
    game.buildGrid()
    game.root.mainloop()


if __name__ == '__main__':
    main()
