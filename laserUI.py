import Gbrl_Rpi_gcode_DcLaser_Sender


from tkinter import *


def getFile():
    #print(gcodeSender.getFileInfo())
    text1.insert(INSERT,gcodeSender.getFileInfo())



root = Tk()
root.geometry("800x480+100+100")

gcodeSender = Gbrl_Rpi_gcode_DcLaser_Sender.LaserCom()

Userinfo = Frame(root, relief=RIDGE, width=700, height=120, bg="blue")
Userinfo.place(y=0,x=100)
NavC = Frame(root, relief=SUNKEN, width=100, bg="red", height=480)
NavC.place(y=0,x=0)
Send = Frame(root,width=700, bg="yellow", height=360)
Send.place(y=120, x=100)

open = Button(NavC, text="Open",command = getFile)
open.place(y=100, x=0)
Ncsend = Button(NavC, text="Send", relief=RAISED, bg="blue")
Ncsend.place(y=200, x=0)
Ncstart = Button(NavC, text="Start", relief=SUNKEN, fg="black",state="disable")
Ncstart.place(y=300, x=30)
Exit = Button(NavC, fg="green", bg="black",text="Exit", width=80, command=root.destroy)
Exit.place(y=460, x=0)
text1 = Text(Send, width=700, height=300, bg="yellow")
text1.place(y=0, x=0)



root.mainloop()
