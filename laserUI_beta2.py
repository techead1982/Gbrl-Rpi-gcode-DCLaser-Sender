import sys
import glob
import time
import serial
import queue
import tkinter as tk
from tkinter import ttk, StringVar, IntVar
from tkinter.filedialog import *
import re
import Gbrl_Rpi_gcode_DcLaser_Sender
import threading
import os
import re
from SerialClass1 import SerialClass

#import rexx

import threading
#from Sender import *

#import log


cq = queue.Queue(maxsize=0)
rq = queue.Queue(maxsize=0)
wq = queue.Queue(maxsize=0)

class NobleLaser(tk.Tk):  # V0.0.1

    def __init__(self, *args, **kwargs):
        ver = "V 0.0.1"
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Noble Laser  + ver +  --- ")
        tk.Tk.wm_geometry(self, "800x480+100+100")
        tk.Tk.wm_resizable(self, False, False)
        # tk.Tk.iconbitmap(self,default="some.ico")

        #self.cq = queue.Queue
        #self.rq = queue.Queue
        #self.wq = queue.Queue

        sc = SerialStuff(wq_q=wq, cq_q=cq, rq_q=rq)
        sc.start()
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.fileName = ''
        for F in (GeneralPage, FileSYSPage, SerialPage, NetworkPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(GeneralPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



    def getFile(self):
        # print(gcodeSender.getFileInfo())

        self.fileName = askopenfilename(filetypes=(("G-code", ".gcode"), ("NC", ".nc"), ("All", "*.*")))
        print(self.fileName)
        # Uitext1.insert(INSERT, self.fileName)

     #def sendFile():
         #gcodeSender.setSerial('COM3',115200,1)
         #gcodeSender.streamFile(fileName, Uitext1, 'COM5', 115200)

        # self.gcodeSender = Gbrl_Rpi_gcode_DcLaser_Sender.LaserCom()

class GeneralPage(tk.Frame):
    def jog_left(self):

        wq.put("G90")
        wq.put("G21")
        wq.put("G0 X7.8964 Y0.9092")
        wq.put("M03")
        wq.put("G1F1.000000")
        wq.put("G02 X8.0219 Y0.6399 I-3.4214 J-1.758")
        # wq.put("G02 X8.0745 Y0.4848 I-1.0793 J-0.453")
        wq.put("G02 X8.0787 Y0.3367 I-0.3156 J-0.083")
        wq.put("G01 X8.0253 Y0.2424")
        wq.put("G01 X7.9234 Y0.1832")
        wq.put("G02 X7.6956 Y0.1362 I-0.3323 J1.0341")
        wq.put("G02 X7.4563 Y0.1206 I-0.3685 J3.8189")
        wq.put("G02 X7.0323 Y0.1135 I-0.424 J12.5812")
        wq.put("G02 X6.6758 Y0.1184 I-0. J12.8671")
        wq.put("G02 X6.4714 Y0.1289 I0.1219 J4.3999")
        wq.put("G02 X6.2683 Y0.1519 I0.1961 J2.6372")
        wq.put("G02 X6.149 Y0.1781 I0.1423 J0.9319")
        wq.put("G02 X6.0389 Y0.2239 I0.1469 J0.5085")
        wq.put("G01 X5.9785 Y0.2728")
        wq.put("G02 X5.9315 Y0.3372 I0.331 J0.2911")
        wq.put("G02 X5.8874 Y0.4244 I0.5874 J0.3521")
        wq.put("G1  X4.0453 Y3.9646")
        wq.put("G1  X2.2105 Y0.4244")
        wq.put("G02 X2.1601 Y0.3363 I-0.8101 J0.4051")
        wq.put("G02 X2.112 Y0.2728 I-0.4616 J0.2996")
        wq.put("G01 X2.0517 Y0.2241")
        wq.put("G02 X1.9412 Y0.1781 I-0.2575 J0.4629")
        wq.put("G02 X1.8221 Y0.152 I-0.2585 J0.8948")
        wq.put("G02 X1.6153 Y0.1289 I-0.4019 J2.6554")
        wq.put("G02 X1.4068 Y0.1183 I-0.3414 J4.6855")
        wq.put("G02 X1.0656 Y0.1135 I-0.3412 J12.0613")
        wq.put("G02 X0.6716 Y0.1207 I-0. J10.7588")
        wq.put("G02 X0.4554 Y0.1362 I0.1138 J3.1054")
        wq.put("G02 X0.2516 Y0.1833 I0.092 J0.8618")
        wq.put("G01 X0.1637 Y0.2424")
        wq.put("G01 X0.1216 Y0.3337")
        wq.put("G02 X0.1334 Y0.4848 I0.3745 J0.0469")
        wq.put("G02 X0.1897 Y0.6396 I1.1308 J-0.3236")
        wq.put("G02 X0.3227 Y0.9092 I3.4807 J-1.5499")
        wq.put("G1  X2.673 Y5.1927")
        wq.put("G1  X0.49 Y9.2181")
        wq.put("G02 X0.362 Y9.4945 I4.4076 J2.208")
        wq.put("G02 X0.3042 Y9.654 I1.4314 J0.6096")
        wq.put("G02 X0.2934 Y9.8065 I0.3259 J0.0996")
        wq.put("G01 X0.3419 Y9.8968")
        wq.put("G01 X0.4393 Y9.9525")
        wq.put("G02 X0.6643 Y9.9956 I0.3127 J-1.0221")
        wq.put("G02 X0.8993 Y10.0082 I0.3747 J-4.7962")
        wq.put("G02 X1.3314 Y10.0145 I0.4321 J-14.8749")
        wq.put("G02 X1.6875 Y10.0096 I-0. J-13.0917")
        wq.put("G02 X1.8962 Y9.9995 I-0.1321 J-4.8538")
        wq.put("G02 X2.1034 Y9.9763 I-0.1956 J-2.6838")
        wq.put("G02 X2.2259 Y9.9499 I-0.1513 J-0.9992")
        wq.put("G02 X2.3388 Y9.9035 I-0.1434 J-0.5097")
        wq.put("G01 X2.3967 Y9.8552")
        wq.put("G02 X2.4419 Y9.7919 I-0.5033 J-0.4079")
        wq.put("G02 X2.4913 Y9.7036 I-0.8419 J-0.5288")
        wq.put("G1  X4.2122 Y6.4588")
        wq.put("G1  X5.8874 Y9.7036")
        wq.put("G02 X5.9371 Y9.7922 I0.9424 J-0.4712")
        wq.put("G02 X5.9824 Y9.8552 I0.5254 J-0.3295")
        wq.put("G01 X6.0391 Y9.9044")
        wq.put("G02 X6.1416 Y9.9499 I0.2446 J-0.4136")
        wq.put("G02 X6.2531 Y9.9762 I0.2477 J-0.8004")
        wq.put("G02 X6.4448 Y9.9995 I0.3699 J-2.2441")
        wq.put("G02 X6.6383 Y10.0096 I0.3121 J-4.1125")
        wq.put("G02 X6.9792 Y10.0145 I0.3409 J-11.8539")
        wq.put("G02 X7.358 Y10.0085 I-0. J-12.0306")
        wq.put("G02 X7.5782 Y9.9956 I-0.1286 J-4.0819")
        wq.put("G02 X7.7864 Y9.952 I-0.0788 J-0.8949")
        wq.put("G01 X7.8814 Y9.8933")
        wq.put("G01 X7.9294 Y9.8003")
        wq.put("G02 X7.923 Y9.6509 I-0.3508 J-0.0596")
        wq.put("G02 X7.8719 Y9.4949 I-1.3523 J0.3559")
        wq.put("G02 X7.7525 Y9.2188 I-4.1724 J1.6413")
        wq.put("G1  X5.5692 Y5.2161")
        wq.put("G1  X7.8964 Y0.9092")
        wq.put("G1  X7.8964 Y0.9092")
        wq.put("M05")
        wq.put("G0 X0.000 Y0.000")
        wq.put("M05")
        wq.put("M02")






        #val = rq.get(self)
        #print("left: " + val)

        #print("done")
    # def Send_prog



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.generalnavframe = ttk.Frame(self,)
        self.generalnavframe.grid(row=0, column=0, sticky="nsew")

        self.generalpagebutt = tk.Button(self.generalnavframe, text="General", width=10, height=3, command=lambda: controller.show_frame(GeneralPage))
        self.generalpagebutt.grid(row=0, column=0)

        self.filesyspagebutt = tk.Button(self.generalnavframe, text="File System", width=10, height=3, command=lambda: controller.show_frame(FileSYSPage))
        self.filesyspagebutt.grid(row=0, column=1)

        self.serialpagebutt = tk.Button(self.generalnavframe, text="Serial", width=10, height=3, command=lambda: controller.show_frame(SerialPage))
        self.serialpagebutt.grid(row=0, column=2)

        self.networkpagebutt = tk.Button(self.generalnavframe, text="Network", width=10, height=3,command=lambda: controller.show_frame(NetworkPage))
        self.networkpagebutt.grid(row=0, column=3)

        # main Frame with nav buttons //End
        # secondary frame with page controlls //Start

        self.generalcontrollsframe = tk.Frame(self,bg="snow2")
        self.generalcontrollsframe.grid(row=1, column=0, sticky="nsew")

        self.grbllbl = ttk.Label(self.generalcontrollsframe, text="Controller Status", width=16)
        self.grbllbl.grid(row=0, column=0)
        self.grblstatus = ttk.Label(self.generalcontrollsframe, width=16, text="Connected")
        self.grblstatus.grid(row=0, column=1)

        self.grblhome = ttk.Button(self.generalcontrollsframe, text="Home Laser", width=32)
        self.grblhome.grid(row=1,column=0)
        self.grblstop = ttk.Button(self.generalcontrollsframe, text="Stop Laser", width=32)
        self.grblstop.grid(row=1, column=1)
        self.grblend = ttk.Button(self.generalcontrollsframe, text="End Program", width=32)
        self.grblend.grid(row=1, column=2)
        self.grblhold = ttk.Button(self.generalcontrollsframe, text="Hold Laser", width=32)
        self.grblhold.grid(row=2, column=0)
        self.grblstart = ttk.Button(self.generalcontrollsframe, text="Start Laser", width=32)
        self.grblstart.grid(row=2, column=1)
        self.grblup = tk.Button(self.generalcontrollsframe, text="+Z", width=8, height=3)
        self.grblup.grid(row=4, column=0, columnspan=2)
        self.grblleft = tk.Button(self.generalcontrollsframe, text="-X", width=8, height=3, command= lambda: GeneralPage.jog_left(self))
        self.grblleft.grid(row=5, column=0)
        self.grblright = tk.Button(self.generalcontrollsframe, text="+X", width=8, height=3)
        self.grblright.grid(row=5, column=1)
        self.grbldown = tk.Button(self.generalcontrollsframe, text="-Z", width=8, height=3)
        self.grbldown.grid(row=6, column=0, columnspan=2)







        self.grblload = ttk.Button(self.generalcontrollsframe, command= lambda: NobleLaser.getFile(self), text="Load Program", width=32)
        self.grblload.grid(row=2, column=2)




        self.gbrlvar = IntVar()
        self.gbrlvar.set(3)

        self.grbl10= ttk.Radiobutton(self.generalcontrollsframe, text="1.0", width=10, variable=self.gbrlvar, value=1)
        self.grbl10.grid(row=4,column=2)
        self.grbl010 = ttk.Radiobutton(self.generalcontrollsframe, text="0.1", width=10, variable=self.gbrlvar, value=2)
        self.grbl010.grid(row=5, column=2)
        self.grbl001 = ttk.Radiobutton(self.generalcontrollsframe, text=".001", width=10, variable=self.gbrlvar, value=3)
        self.grbl001.grid(row=6, column=2)
        self.topdoor = ttk.Label(self.generalcontrollsframe, text="Top Door", width =40, relief=SOLID, )
        self.topdoor.grid(row=4, column=3)
        self.topbot = ttk.Label(self.generalcontrollsframe, text="Bottom Door", width =40, relief=SOLID, )
        self.topbot.grid(row=5, column=3)
        self.sidedoor = ttk.Label(self.generalcontrollsframe, text="sidedoor", width =40, relief=SOLID, )
        self.sidedoor.grid(row=6, column=3)
        self.generalgcodeframe = ttk.Frame(self)
        self.generalgcodeframe.grid(row=2, column=0, sticky="nsew")

        self.grbltree = ttk.Treeview(self.generalgcodeframe, columns=('#', 'G-code', 'Status', 'Reply'))
        self.grbltree.heading('#0', text='')
        self.grbltree.column('#0', minwidth=0, width=0)
        self.grbltree.heading('#1', text='#')
        self.grbltree.column('#1', minwidth=0, width=50)
        self.grbltree.heading('#2', text='G-code')
        self.grbltree.column('#2', minwidth=0, width=590)
        self.grbltree.heading('#3', text='Status')
        self.grbltree.column('#3', minwidth=0, width=120)
        self.grbltree.heading('#4', text='Reply')
        self.grbltree.column('#4', minwidth=0, width=40)
        self.grbltree.pack(side='bottom', fill='both')
        self.grbltree.insert('', 0, '', values=(1, 'gcode cvbdfg cxfgdfg xfgdsg', 'sent', 'OK'))
        # testbut = ttk.Button(GeneralControllsframe, text="1")
        # testbut.grid(row=0, column=0)

        # secondary frame with page controlls //End


class FileSYSPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.generalnavframe = ttk.Frame(self)
        self.generalnavframe.grid(row=0, column=0, sticky="nsew")

        self.generalpagebutt = tk.Button(self.generalnavframe, text="General", width=10, height=3, command=lambda: controller.show_frame(GeneralPage))
        self.generalpagebutt.grid(row=0, column=0)

        self.filesyspagebutt = tk.Button(self.generalnavframe, text="File System", width=10, height=3, bg='gray', command=lambda: controller.show_frame(FileSYSPage))
        self.filesyspagebutt.grid(row=0, column=1)

        self.serialpagebutt = tk.Button(self.generalnavframe, text="Serial", width=10, height=3, command=lambda: controller.show_frame(SerialPage))
        self.serialpagebutt.grid(row=0, column=2)

        self.networkpagebutt = tk.Button(self.generalnavframe, text="Network", width=10, height=3, command=lambda: controller.show_frame(NetworkPage))
        self.networkpagebutt.grid(row=0, column=3)

        self.generalcontrollsframe = ttk.Frame(self)  # secondary frame with page controlls
        self.generalcontrollsframe.grid(row=1, column=0, sticky="nsew")
        self.homedirlbl = ttk.Label(self.generalcontrollsframe, text="Home Dir", width=16)
        self.homedirlbl.grid(row=0, column=0)
        self.homedir = ttk.Entry(self.generalcontrollsframe, width=16)
        self.homedir.grid(row=0, column=1)

        self.remotedirlbl = ttk.Label(self.generalcontrollsframe, text="Remote Dir", width=16)
        self.remotedirlbl.grid(row=2, column=0)
        self.remotedir = ttk.Entry(self.generalcontrollsframe, width=16)
        self.remotedir.grid(row=2, column=1)

        self.copytodir = ttk.Button(self.generalcontrollsframe, text="Copy TO Remote Dir", width=16)
        self.copytodir.grid(row=3, column=0)

        self.from_dir = ttk.Button(self.generalcontrollsframe, text="From TO Remote Dir", width=16)
        self.from_dir.grid(row=3, column=1)

        self.usernamelbl = ttk.Label(self.generalcontrollsframe, text="Username", width=16)
        self.usernamelbl.grid(row=4, column=0)
        self.username = ttk.Entry(self.generalcontrollsframe, width=16)
        self.username.grid(row=4, column=1)

        self.passwordlbl = ttk.Label(self.generalcontrollsframe, text="Password", width=16)
        self.passwordlbl.grid(row=5, column=0)
        self.password = tk.Entry(self.generalcontrollsframe, width=16)
        self.password.grid(row=5, column=1)

        self.setfilesys = ttk.Button(self.generalcontrollsframe, text="Set", width=16)
        self.setfilesys.grid(row=6, column=0, columnspan=2)

        # testbut = ttk.Button(GeneralControllsframe,text="2")
        # testbut.grid(row=0,column =0)


class SerialPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.generalnavframe = ttk.Frame(self)
        self.generalnavframe.grid(row=0, column=0, sticky="nsew")

        self.generalpagebutt = tk.Button(self.generalnavframe, text="General", width=10, height=3, command=lambda: controller.show_frame(GeneralPage))
        self.generalpagebutt.grid(row=0, column=0)

        self.filesyspagebutt = tk.Button(self.generalnavframe, text="File System", width=10, height=3, command=lambda: controller.show_frame(FileSYSPage))
        self.filesyspagebutt.grid(row=0, column=1)

        self.serialpagebutt = tk.Button(self.generalnavframe, text="Serial", width=10, height=3, bg='gray', command=lambda: controller.show_frame(SerialPage))
        self.serialpagebutt.grid(row=0, column=2)

        self.networkpagebutt = tk.Button(self.generalnavframe, text="Network", width=10, height=3, command=lambda: controller.show_frame(NetworkPage))
        self.networkpagebutt.grid(row=0, column=3)

        self.generalcontrollsframe = ttk.Frame(self)  # secondary frame with page controlls
        self.generalcontrollsframe.grid(row=1, column=0, sticky="nsew")

        self.portlbl = ttk.Label(self.generalcontrollsframe, text="Port", width=16)
        self.portlbl.grid(row=0, column=0)
        self.portcb_val = StringVar()
        self.portcb_val = "" #ser111.ser.port
        self.portcb = ttk.Combobox(self.generalcontrollsframe, textvariable=self.portcb_val, state='readonly')
        i = 0
        #for port in ser111.portList:
        #    if port == ser111.ser.port:
        #        break
        #    else:
        #        i += 1

        #self.portcb.config(values=ser111.portList)
        #self.portcb.current(i)
        #self.portcb.grid(row=0, column=1)

        self.baudratelbl = ttk.Label(self.generalcontrollsframe, text="Baudrate", width=16)
        self.baudratelbl.grid(row=2, column=0)
        self.baudrate_val = StringVar()
        #self.baudrate_val = ser111.ser.baudrate
        baudratelist = ['9600', '19200', '38400', '57600', '115200']
        self.baudrate = ttk.Combobox(self.generalcontrollsframe, textvariable=self.baudrate_val, state='readonly')
        i = 0
        #for brate in baudratelist:
        #    if brate == str(ser111.ser.baudrate):
        #        break
        #    else:
        #        i += 1

        self.baudrate.config(values=baudratelist)
        self.baudrate.current(i)
        self.baudrate.grid(row=2, column=1)

        self.databitslbl = ttk.Label(self.generalcontrollsframe, text="Data Bits", width=16)
        self.databitslbl.grid(row=3, column=0)
        self.databits_val = StringVar()
        #self.databits_val = ser111.ser.bytesize
        databitslist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.databits = ttk.Combobox(self.generalcontrollsframe, textvariable=self.databits_val, state='readonly')
        i = 0
        #for dbits in databitslist:
        #    if dbits == str(ser111.ser.bytesize):
        #        break
        #    else:
        #        i += 1

        self.databits.config(values=databitslist)
        self.databits.current(i)
        self.databits.grid(row=3, column=1)

        self.paritybitslbl = ttk.Label(self.generalcontrollsframe, text="Paritybits", width=16)
        self.paritybitslbl.grid(row=4, column=0)
        self.paritybits_val = StringVar()
        #self.paritybits_val = ser111.ser.parity
        paritybitslist = ['N', 'O', 'E', 'M', 'S']
        self.paritybits = ttk.Combobox(self.generalcontrollsframe, textvariable=self.paritybits_val, state='readonly')
        i = 0
        #for pbits in paritybitslist:
        #    if pbits == ser111.ser.parity:
        #        break
        #    else:
        #        i += 1

        self.paritybits.config(values=paritybitslist)
        self.paritybits.current(i)
        self.paritybits.grid(row=4, column=1)

        self.stopbitslbl = ttk.Label(self.generalcontrollsframe, text="Stopbits", width=16)
        self.stopbitslbl.grid(row=5, column=0)
        self.stopbits_val = StringVar()
        #self.stopbits_val = ser111.ser.stopbits
        stopbitslist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.stopbits = ttk.Combobox(self.generalcontrollsframe, textvariable=self.stopbits_val, state='readonly')
        i = 0
        #for sbits in stopbitslist:
        #    if sbits == str(ser111.ser.stopbits):
        #        break
        #    else:
        #        i += 1

        self.stopbits.config(values=stopbitslist)
        self.stopbits.current(i)
        self.stopbits.grid(row=5, column=1)

        self.setserial = ttk.Button(self.generalcontrollsframe, text="Set", width=16)
        self.setserial.grid(row=6, column=0, columnspan=2)

        self.update_info()
        # testbut = ttk.Button(GeneralControllsframe,text="3")
        # testbut.grid(row=0,column =0)
    def update_info(self):
        #self.portcb_val = ser111.ser.port
        print("ser111.ser.port:)")


class NetworkPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.generalnavframe = ttk.Frame(self)
        self.generalnavframe.grid(row=0, column=0, sticky="nsew")

        self.generalpagebutt = tk.Button(self.generalnavframe, text="General", width=10, height=3, command=lambda: controller.show_frame(GeneralPage))
        self.generalpagebutt.grid(row=0, column=0)

        self.filesyspagebutt = tk.Button(self.generalnavframe, text="File System", width=10, height=3, command=lambda: controller.show_frame(FileSYSPage))
        self.filesyspagebutt.grid(row=0, column=1)

        self.serialpagebutt = tk.Button(self.generalnavframe, text="Serial", width=10, height=3, command=lambda: controller.show_frame(SerialPage))
        self.serialpagebutt.grid(row=0, column=2)

        self.networkpagebutt = tk.Button(self.generalnavframe, text="Network", width=10, height=3, bg='gray', command=lambda: controller.show_frame(NetworkPage))
        self.networkpagebutt.grid(row=0, column=3)

        self.generalcontrollsframe = ttk.Frame(self)  # secondary frame with page controlls
        self.generalcontrollsframe.grid(row=1, column=0, sticky="nsew")

        self.var = IntVar()
        self.var.set(2)

        self.dhcp = ttk.Radiobutton(self.generalcontrollsframe, text="Dhcp", variable=self.var, value=2)
        self.dhcp.grid(row=0, column=1)

        self.static = ttk.Radiobutton(self.generalcontrollsframe, text="Static", variable=self.var, value=1)
        self.static.grid(row=0, column=0)

        self.ipaddress = ttk.Label(self.generalcontrollsframe, text="Ip Address")
        self.ipaddress.grid(row=1, column=0)
        self.ipaddrv4 = ttk.Entry(self.generalcontrollsframe, width=16)
        self.ipaddrv4.grid(row=1, column=1)

        self.subnetlbl = ttk.Label(self.generalcontrollsframe, text="Subnet")
        self.subnetlbl.grid(row=2, column=0)
        self.subnet = ttk.Entry(self.generalcontrollsframe, width=16)
        self.subnet.grid(row=2, column=1)

        self.gatewaylbl = ttk.Label(self.generalcontrollsframe, text="Gateway")
        self.gatewaylbl.grid(row=3, column=0)
        self.gateway = ttk.Entry(self.generalcontrollsframe, width=16)
        self.gateway.grid(row=3, column=1)

        self.dns1lbl = ttk.Label(self.generalcontrollsframe, text="Dns1")
        self.dns1lbl.grid(row=4, column=0)
        self.dns1 = ttk.Entry(self.generalcontrollsframe, width=16)
        self.dns1.grid(row=4, column=1)

        self.dns2lbl = ttk.Label(self.generalcontrollsframe, text="Dns2")
        self.dns2lbl.grid(row=5, column=0)
        self.dns2 = ttk.Entry(self.generalcontrollsframe, width=16)
        self.dns2.grid(row=5, column=1)

        self.setnetwork = ttk.Button(self.generalcontrollsframe, text="Set", width=16)
        self.setnetwork.grid(row=7, column=0, columnspan=2)

        # testbut = ttk.Button(GeneralControllsframe,text="4")
        # testbut.grid(row=0,column =0)


#class infogetter:
    #def __init__(self):
        #self.queue = queue


class SerialStuff(threading.Thread):
    # https://mail.python.org/pipermail/tkinter-discuss/2013-August/003477.html
    def __init__(self, cq_q, wq_q, rq_q):

        self.ser = serial.Serial()  # creates serial object
        self.grbl_version = "Grbl Not Detected"
        self.portList = []
        self.Buffer = []
        self.write_q = wq_q
        self.cammand_q = cq_q
        self.reply_q = rq_q
        self.charline = []
        self.linecount = 1
        self.okcount = 0
        self.grblBufferSize = 128
        self.gcodeCount = 0
        self.auto_setup(115200,None,None,None,None)
        threading.Thread.__init__(self)


    def run(self):
        self.reply_q.put("GV,"+self.grbl_version)
        print(self.grbl_version+":1")
        #print("hi" + self.reply_q.get(self))
        self.ser.open()

        while self.ser.is_open:
            if self.cammand_q.qsize() != 0:
                print("ser cq1")
                textout = self.cammand_q.get()
                textsplit = []
                textsplit = textout.split(",")

                if textsplit[0] == 'Quit':
                    self.ser.close()
                    print("ser cq1 Quit")
                elif textsplit[0] == 'Pause':
                    self.ser.write(bytearray(textsplit[1], 'ascii'))
                    print("ser cq1 Pause")
                elif textsplit[0] == 'Left':
                    self.ser.write(bytearray(textsplit[1], 'ascii'))
                    print("ser cq1 Left")
                elif textsplit[0] == 'Right':
                    self.ser.write(bytearray(textsplit[1], 'ascii'))
                    print("ser cq1 Right")
                elif textsplit[0] == 'Up':
                    self.ser.write(bytearray(textsplit[1], 'ascii'))
                    print("ser cq1 Up")
                elif textsplit[0] == 'Down':
                    self.ser.write(bytearray(textsplit[1], 'ascii'))
                    print("ser cq1 Down")
                print("ser cq1 writen")
                time.sleep(0.1)
                self.cammand_q.task_done()
                print("ser cq1 done")
            while self.write_q.qsize() != 0:
                if self.cammand_q.qsize() != 0:
                    print("ser cq2")
                    # switch{}
                        # case up;
                            # write (gcode+[2])
                        # case down;

                    textout = self.cammand_q.get()
                    self.ser.write(bytearray(textout, 'ascii'))
                    time.sleep(0.1)
                    self.cammand_q.task_done()


                else:
                    print("ser wq")
                    counter = 0
                    while self.gcodeCount != self.linecount:
                        textout = self.write_q.get()

                        lineblock = textout.strip()
                        # lineblock += "\n"
                        self.charline.append(len(lineblock) + 1)
                        grblOut = ''
                        verbose = True
                        okc = 0
                        while sum(self.charline) >= self.grblBufferSize - 1 | self.ser.inWaiting():

                            out_temp = self.ser.readline().strip().decode('ascii')
                            #print("i Work For now L39"+out_temp.decode("utf-8"))
                            if out_temp.find('ok') < 0 and out_temp.find('error') < 0:
                                self.reply_q.put("Error," + out_temp)
                                print("Debug: Error," + out_temp)
                                okc += 2
                            else:

                                s=[]
                                okc += sum(1 for _ in re.finditer(r'\b%s\b' % re.escape('ok'), out_temp))
                                print("okc = " + str(okc))
                                grblOut += out_temp
                                #self.gcodeCount += 1
                                #grblOut += str(self.gcodeCount)
                                #self.okcount += 1 + okc
                                del self.charline[0]

                                #print("L73")
                        self.gcodeCount += 1 + okc - 1
                        grblOut += str(self.gcodeCount)
                        if verbose:
                            # textBox.insert('1.0',"SND: " + str(lineCount) + " : " + lineBlock +'\n')
                            print("SND: " + str(self.linecount) + " : " + lineblock)
                            # newl = b'\n'
                            self.ser.write(bytearray(lineblock + '\n', 'ascii'))  # Send g-code block to grbl
                            # time.sleep(.1)

                        if verbose:
                            # textBox.insert('1.0', "BUF:", str(sum(self.charline)), "REC:", grblOut+'\n')
                            print("BUF: " + str(sum(self.charline)) + "  REC: " + grblOut + " Gcode Oks: " + str(self.gcodeCount))
                        self.linecount += 1


                    # self.ser.write(bytearray(textout, 'ascii'))
                    # time.sleep(0.1)


                    self.write_q.task_done()
            time.sleep(1)
            print("Still Alive...")
        print("Still Aliveeeeeeeeeeeeeeeee...Cake is a lieeeeee")




    def serial_ports(self):  # Finds open serial ports on Computer
        # print("find ports")
        # print(sys.platform)
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i+1)for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
        result = []
        for port in ports:
            self.serial_setup(port, self.ser.baudrate, None, None, None, None)

            # print("after serial")
            try:
                # print(port)
                # print("Yes1")
                self.ser.open()
                # print("Yes2")
                self.ser.close()
                # print("Yes3")

                result.append(port)
            except(OSError, serial.SerialException):
                pass
        self.portList = result
        return result

    def grbl_info(self, ver):  # Sets ver Num
        self.grbl_version = ver
        slef.send = ""
        self.send = "GV,"+self.grbl_version
        self.reply_q.put_nowait(self.send)


    def auto_setup(self, baud_rate, byte_size, parity_bits, stop_bits, time_out):  # used in auto find grbl

        self.ser.baudrate = baud_rate

        if byte_size is not None:
            self.ser.bytesize = byte_size

        if parity_bits is not None:
            self.ser.parity = parity_bits

        if stop_bits is not None:
            self.ser.stopbits = stop_bits

        if time_out is not None:
            self.ser.timeout = time_out

        self.auto_find_grbl()

    def serial_setup(self, comport, baud_rate, byte_size, parity_bits, stop_bits, time_out):  # port setup

        self.ser.port = comport

        if baud_rate is not None:
            self.ser.baudrate = baud_rate

        if byte_size is not None:
            self.ser.bytesize = byte_size

        if parity_bits is not None:
            self.ser.parity = parity_bits

        if stop_bits is not None:
            self.ser.stopbits = stop_bits

        if time_out is not None:
            self.ser.timeout = time_out

        # def Stored_serial_Setup(self):
        # with open('SerialConfig.py','r',encoding='ascii') as f:

    def auto_find_grbl(self):  # finds what port grbl is on and sets it to serial setup
        available_ports = self.serial_ports()
        # print("port start")
        i = 0
        p = ''
        for port in available_ports:
            # print(port)
            self.serial_setup(port, self.ser.baudrate, None, None, None, None)
            try:
                self.ser.open()

                time.sleep(3)
                # test.write(self,'$I')

                while self.ser.inWaiting():
                    data = self.ser.readline().strip().decode('ascii')
                    # print(data)
                    if data.find('Grbl') < 0:
                        print("No data")
                        u = 1
                    else:
                        self.grbl_version = data
                        print(data)
                        i = 1
                        p = port
                        break
                self.ser.close()

            except (OSError, serial.SerialException):
                # print("dam")
                pass
            if i == 1:
                break





# class NetworkShit:
#     #def __init__(self):
#
#     def get_dhcp_info(self):
#         info = []
#         #ipadd = socket.fd
#         #print(ipadd)
#
#         return info
#     def staticip(self, ip_address, subnet_mask, gateway, dns1, dns2):
#queue = queue.threading
#ser111 = SerialStuff()
#ser111.auto_setup(115200, None, None, None, 5)
app = NobleLaser()

app.mainloop()