from tkinter import *
root = Tk()  # window initialises

test_label = Label(root, text="Hello World!").grid(
    row=0, column=0)  # create a widget, also valid bc obj oriented
test_label2 = Label(root, text="Test Text")  # create a widget

# use grids
# same as row = 1 col = 5 only relative position
test_label2.grid(row=1, column=5)  # or in 2 steps

root.mainloop()
