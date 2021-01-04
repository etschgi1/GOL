from tkinter import *
root = Tk()  # window initialises


def whenclicked():
    button["bg"] = "yellow"
    try:
        lablet.pack_forget()
    except:
        lablet = Label(root, bg="green", padx=50,
                       pady=50).grid(row=1, column=1)


button = Button(root, text="hallo", state=DISABLED)  # to disable
button2 = Button(root, text="padding", padx=50, pady=50,
                 command=whenclicked, bg="#7CFC00")  # functions without () only pass name


# button.pack()
button2.grid(row=1, column=1)
root.mainloop()
