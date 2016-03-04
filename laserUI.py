#import Gbrl-Rpi-gcode-DcLaser-Sender
import Gbrl_Rpi_gcode_DcLaser_Sender
from tkinter import *
  


def getFile():
    print(gcodeSender.getFileInfo())
    
root = Tk()
gcodeSender = Gbrl_Rpi_gcode_DcLaser_Sender.LaserCom()

Main = Frame(root, relief=RIDGE, width=800, height=480)
Main.pack()
#Nav = tkinter.Frame(root, relief=SUNKEN, Main ,width=200, height=200)
#Nav.pack()

open = Button(root, text="Open",command = getFile)
open.pack()
open.place(height = 20,width = 40,x =60,y=10)
Exit = Button(root, text="Exit", command=root.destroy)
Exit.pack()
Exit.place(height = 20,width = 40,x =10,y=10)
root.mainloop()