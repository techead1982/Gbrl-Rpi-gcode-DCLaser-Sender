import tkinter
#import Gbrl-Rpi-gcode-DcLaser-Sender
from tkinter import *
from tkinter.filedialog import *   


def openFile():
	fn = askopenfilename(filetype=(("G code",".gcode"),("All","*.*")),title = "Get file dumb dumb")
	print(fn)
tk = tkinter.Tk()

Main = tkinter.Frame(tk, relief=RIDGE, width=800, height=480)
Main.pack()
#Nav = tkinter.Frame(tk, relief=SUNKEN, Main ,width=200, height=200)
#Nav.pack()
open = tkinter.Button(tk, text="Open",command=openFile)
open.pack()
open.place(height = 20,width = 40,x =60,y=10)
Exit = tkinter.Button(tk, text="Exit", command=tk.destroy)
Exit.pack()
Exit.place(height = 20,width = 40,x =10,y=10)
tk.mainloop()
