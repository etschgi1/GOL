from tkinter import *
import time


REBIRTH_COUNT = 3
DEAD_FROM_LONELINESS = 1
DEAD_FROM_OVERPOPULATION = 4
TIME_BETWEEN_STEPS = 1


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
            row = []
            for j in range(self.width):
                row.append(CustomButton(i, j, 0, 0, self))
            self.buttons.append(row)

    def runSim(self):
        self.run.config(state=DISABLED)  # deactivate start
        print("run sim")
        i = 0
        time.sleep(TIME_BETWEEN_STEPS)
        dirtySim(self, self.height, self.width)
        i += 1

        # todo kill all buttons start new
        self.run.config(state=ACTIVE)


def dirtySim(Gb, height, width):
    cellcount = height*width
    for cellrow in range(height):  # check if cell should live or die
        for cellcol in range(width):
            countNeighbors(Gb, Gb.buttons[cellrow][cellcol], cellrow, cellcol)
    makeStep(Gb)
    resetallneighborcounts(Gb)


def makeStep(Gb):
    for row in range(Gb.height):
        for col in range(Gb.width):
            # apply rules
            Cell = Gb.buttons[row][col]
            if(Cell.state == 0 and Cell.neighbors == REBIRTH_COUNT):  # resurect from the dead
                Cell.beBorn()
                print("born")
            elif(Cell.state == 1 and Cell.neighbors <= DEAD_FROM_LONELINESS):
                print("lonly")
                Cell.die()
            elif(Cell.state == 1 and Cell.neighbors >= DEAD_FROM_OVERPOPULATION):
                print("overpop")
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
    board = Gameboard(6, 6)
    board.buildGrid()
    board.root.mainloop()


if __name__ == '__main__':
    main()
