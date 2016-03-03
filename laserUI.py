import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
Main = tkinter.Frame(tk, relief=RIDGE, width=800, height=480)
Main.pack()
Nav = tkinter.Frame(tk, relief=SUNKEN, Main width=200, height=200)
Nav.pack()

Exit = tkinter.Button(tk, text="Exit", command=tk.destroy)
Exit.pack(side=BOTTOM)
tk.mainloop()
