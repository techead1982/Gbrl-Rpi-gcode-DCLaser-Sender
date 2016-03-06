import Gbrl_Rpi_gcode_DcLaser_Sender

from tkinter import *
from tkinter import ttk

fileName = ''
def getFile():
	global fileName
    #print(gcodeSender.getFileInfo())
	fileName = gcodeSender.getFileInfo()
	print(fileName)
	Uitext1.insert(INSERT,fileName)
	
def sendFile():
	#gcodeSender.setSerial('COM3',115200,1)
	gcodeSender.streamFile(fileName,Uitext1,'COM5',115200)

gcodeSender = Gbrl_Rpi_gcode_DcLaser_Sender.LaserCom()

root = Tk()
root.geometry("800x480+100+100")
root.resizable(False,False)


Userinfo = Frame(root, relief=RIDGE, width=700, height=120, bg="blue")
Userinfo.place(y=0,x=100)
NavC = Frame(root, relief=SUNKEN, width=100, height=480, bg="red")
NavC.place(y=0,x=0)
Send = Frame(root,width=700,  height=360, bg="yellow",)
Send.place(y=120, x=100)

Ncopen = Button(NavC, text="Open",width=11,height=5,command = getFile)
Ncopen.place(y=0, x=0)
Ncsend = Button(NavC, text="Send", width=11,height=5,relief=RAISED, bg="blue")
Ncsend.place(y=100, x=0)
Ncstart = Button(NavC, text="Start",width=11,height=5, relief=SUNKEN, fg="black",command = sendFile)
Ncstart.place(y=200, x=0)
NcExit = Button(NavC, text="Exit", width=11, height=5,fg="green", command=root.destroy)
NcExit.place(y=400, x=0)
Ncsetting = Button(NavC, text="Settings", width=11,height=5,relief=RAISED, bg="blue")
Ncsetting.place(y=300, x=0)
Uitext1 = Text(Userinfo, width=70, height=30, wrap ="word",bg="gray")
Uitext1.place(y=0, x=0)




root.mainloop()
