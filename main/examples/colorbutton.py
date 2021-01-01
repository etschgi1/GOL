import tkinter as tk


class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("250x100")
        self.buttonA = tk.Button(self.root,
                                 text="Color",
                                 bg="blue",
                                 fg="red")

        self.buttonB = tk.Button(self.root,
                                 text="Click to change color",
                                 command=self.changeColor)
        self.buttonA.pack(side=tk.LEFT)
        self.buttonB.pack(side=tk.RIGHT)
        self.root.mainloop()

    def changeColor(self):
        self.buttonA.configure(bg="yellow")


app = Test()
