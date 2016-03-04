# import Gbrl-Rpi-gcode-DcLaser-Sender
import tkinter
#from tkinter import *
from tkinter.filedialog import *


def openFile():
    fn = askopenfilename(filetype=(("G-code", ".gcode"), ("NC", ".nc"), ("All", "*.*")), title="Get file dumb dumb")
    print(fn)


root = Tk()


Userinfo = Frame(root, relief=RIDGE, width=400, height=120, bg="blue")
Userinfo.place(y=0,x=100)

NavC = tkinter.Frame(root, relief=SUNKEN, width=300, height=600, bg="red")
NavC.place(y=0,x=10)
open = Button(NavC, text="Open")
open.pack(side="left")
Ncsend = Button(NavC, text="send", relief=RAISED, bg="blue")
Ncsend.pack()
Ncstart = Button(NavC, text="Start", relief=SUNKEN, fg="black")
Ncstart.pack()

Exit = Button(NavC, fg="green", bg="black",text="Exit", command=root.destroy)
Exit.pack()
#Exit.place(height=20, width=40, x=800, y=480)

root.mainloop()
