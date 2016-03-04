import Gbrl_Rpi_gcode_DcLaser_Sender


from tkinter import *


def getFile():
    #print(gcodeSender.getFileInfo())
    Uitext1.insert(INSERT,gcodeSender.getFileInfo())



root = Tk()
root.geometry("800x480+100+100")
root.resizable(False,False)

gcodeSender = Gbrl_Rpi_gcode_DcLaser_Sender.LaserCom()

Userinfo = Frame(root, relief=RIDGE, width=700, height=120, bg="blue")
Userinfo.place(y=0,x=100)
NavC = Frame(root, relief=SUNKEN, width=100, height=480, bg="red")
NavC.place(y=0,x=0)
Send = Frame(root,width=700,  height=360, bg="yellow",)
Send.place(y=120, x=100)

Ncopen = Button(NavC, text="Open",width=10,height=10,command = getFile)
Ncopen.place(y=5, x=0)
Ncsend = Button(NavC, text="Send", relief=RAISED, bg="blue", height=10,)
Ncsend.place(y=150, x=0)
Ncstart = Button(NavC, text="Start", relief=SUNKEN, fg="black")
Ncstart.place(y=250, x=0)
NcExit = Button(NavC, text="Exit",fg="green", width=5, height=5, command=root.destroy)
NcExit.place(y=460, x=0)
Uitext1 = Text(Userinfo, width=70, height=30, bg="gray")
Uitext1.place(y=0, x=0)



root.mainloop()
