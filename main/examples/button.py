from tkinter import *
root = Tk()  # window initialises


def whenclicked():
    button["bg"] = "yellow"
    myLabel = Label(root, text="Button clicked")
    myLabel.pack()


button = Button(root, text="hallo", state=DISABLED)  # to disable
button2 = Button(root, text="padding", padx=50, pady=50,
                 command=whenclicked, bg="#7CFC00")  # functions without () only pass name


button.pack()
button2.pack()
root.mainloop()
