from tkinter import *
root = Tk()  # window initialises


root.geometry('600x600')


button = Button(root, text="hallo", state=DISABLED)  # to disable
button2 = Button(root, text="padding", padx=50, pady=50, bg="#7CFC00")  # functions without () only pass name
button.place(x=10,y=23)

# button.pack()
button2.grid(row=1, column=1)
root.mainloop()
