from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Button

win = Tk()
win.title("Error program")

def starterror():
    for i in range(0, 50):
        errorwin = Toplevel(win)

btstart = Button(win, text="Start error", command=starterror)
btstart.grid(column=0, row=0)

win.mainloop()
