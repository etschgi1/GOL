from tkinter import *
root = Tk()  # window initialises


def click():
    hello = "Hello " + e.get()
    lableout = Label(root, text=hello).pack()


e = Entry(root, width=50, fg="grey", borderwidth=10)
e.insert(0, "Please enter your name")  # Standard Text
b = Button(root, text="Enter name", width=45, command=click)


e.pack()
b.pack()
root.mainloop()
