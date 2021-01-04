import tkinter as tk


def toggle1():
    if button1.config('text')[-1] == 'ON':
        button1.config(text='OFF', bg="red",
                       activebackground="red", textvariable=0)
        print(button1.config('textvariable')[-1])
    else:
        button1.config(text='ON', bg="green",
                       activebackground="green", textvariable=1)
        print(button1.config('textvariable')[-1])


root = tk.Tk()
button1 = tk.Button(
    text="OFF",
    width=12,
    height=1,
    borderwidth=0,
    command=toggle1,
    relief="raised",
    state="normal",
    bg="red",
    activebackground="red",
    repeatdelay=1
)
button1.pack(pady=5)
root.mainloop()
