import tkinter
from tkinter.constants import *

tk = tkinter.Tk()
Main = tkinter.Frame(tk, relief=RIDGE, width=100, height=300)
Main.pack()
open =tkinter.Button(tk,text="open", relief=SUNKEN,width=100, height=200)
#open.pack()
open.place(x=500,y=500)


#Nav = tkinter.Frame(tk, relief=SUNKEN, Main width=200, height=200)
#Nav.pack()

Exit = tkinter.Button(tk, text="Exit", command=tk.destroy)
Exit.pack(side=BOTTOM)
tk.mainloop()


