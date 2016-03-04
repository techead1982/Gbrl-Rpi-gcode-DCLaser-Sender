import Gbrl_Rpi_gcode_DcLaser_Sender


from tkinter import *


def getFile():
    #print(gcodeSender.getFileInfo())
    Userinfo.insert(INSERT,gcodeSender.getFileInfo())



root = Tk()
root.geometry("800x480+100+100")

gcodeSender = Gbrl_Rpi_gcode_DcLaser_Sender.LaserCom()

Userinfo = Frame(root, relief=RIDGE, width=700, height=120, bg="blue")
Userinfo.place(y=0,x=100)
NavC = Frame(root, relief=SUNKEN, width=100, height=480, bg="red")
NavC.place(y=0,x=0)
Send = Frame(root,width=700,  height=360, bg="yellow",)
Send.place(y=120, x=100)

open = Button(NavC, text="Open",width=10,height=10,command = getFile)
open.place(y=50, x=0)
Ncsend = Button(NavC, text="Send", relief=RAISED, bg="blue", height=10,)
Ncsend.place(y=150, x=0)
Ncstart = Button(NavC, text="Start", relief=SUNKEN, fg="black")
Ncstart.place(y=250, x=0)
Exit = Button(NavC, text="Exit",fg="green", bg="black", width=10, height=10, command=root.destroy)
Exit.place(y=460, x=0)
text1 = Text(Userinfo, width=700, height=300, bg="yellow")
text1.place(y=0, x=0)



root.mainloop()
