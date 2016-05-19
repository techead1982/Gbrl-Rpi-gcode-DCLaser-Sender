import sys
import glob
import time
import serial
import queue
import tkinter as tk
from tkinter import ttk, StringVar, IntVar
import threading
import os
import re

#import rexx

import threading
#from Sender import *

#import log

# if __name__ == "__main__":

class NobleLaser(tk.Tk):  # V0.0.1

    def __init__(self, *args, **kwargs):
        ver = "V 0.0.1"
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Noble Laser  + ver +  --- " + ser111.grbl_version)
        tk.Tk.wm_geometry(self, "800x480+100+100")
        tk.Tk.wm_resizable(self, False, False)
        # tk.Tk.iconbitmap(self,default="some.ico")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (GeneralPage, FileSYSPage, SerialPage, NetworkPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(GeneralPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class GeneralPage(tk.Frame):
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
        self.grblleft = tk.Button(self.generalcontrollsframe, text="-X", width=8, height=3)
        self.grblleft.grid(row=5, column=0)
        self.grblright = tk.Button(self.generalcontrollsframe, text="+X", width=8, height=3)
        self.grblright.grid(row=5, column=1)
        self.grbldown = tk.Button(self.generalcontrollsframe, text="-Z", width=8, height=3)
        self.grbldown.grid(row=6, column=0, columnspan=2)
        self.grblload = ttk.Button(self.generalcontrollsframe, text="Load Program", width=32)
        self.grblload.grid(row=2, column=2)
        self.grbl10= ttk.Button(self.generalcontrollsframe, text="1.0", width=10, )
        self.grbl10.grid(row=4,column=2)
        self.grbl010 = ttk.Button(self.generalcontrollsframe, text="0.1", width=10, )
        self.grbl010.grid(row=5, column=2)
        self.grbl001 = ttk.Button(self.generalcontrollsframe, text=".01", width=10, )
        self.grbl001.grid(row=6, column=2)

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
        self.portcb_val = ser111.ser.port
        self.portcb = ttk.Combobox(self.generalcontrollsframe, textvariable=self.portcb_val, state='readonly')
        i = 0
        for port in ser111.portList:
            if port == ser111.ser.port:
                break
            else:
                i += 1

        self.portcb.config(values=ser111.portList)
        self.portcb.current(i)
        self.portcb.grid(row=0, column=1)

        self.baudratelbl = ttk.Label(self.generalcontrollsframe, text="Baudrate", width=16)
        self.baudratelbl.grid(row=2, column=0)
        self.baudrate_val = StringVar()
        self.baudrate_val = ser111.ser.baudrate
        baudratelist = ['9600', '19200', '38400', '57600', '115200']
        self.baudrate = ttk.Combobox(self.generalcontrollsframe, textvariable=self.baudrate_val, state='readonly')
        i = 0
        for brate in baudratelist:
            if brate == str(ser111.ser.baudrate):
                break
            else:
                i += 1

        self.baudrate.config(values=baudratelist)
        self.baudrate.current(i)
        self.baudrate.grid(row=2, column=1)

        self.databitslbl = ttk.Label(self.generalcontrollsframe, text="Data Bits", width=16)
        self.databitslbl.grid(row=3, column=0)
        self.databits_val = StringVar()
        self.databits_val = ser111.ser.bytesize
        databitslist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.databits = ttk.Combobox(self.generalcontrollsframe, textvariable=self.databits_val, state='readonly')
        i = 0
        for dbits in databitslist:
            if dbits == str(ser111.ser.bytesize):
                break
            else:
                i += 1

        self.databits.config(values=databitslist)
        self.databits.current(i)
        self.databits.grid(row=3, column=1)

        self.paritybitslbl = ttk.Label(self.generalcontrollsframe, text="Paritybits", width=16)
        self.paritybitslbl.grid(row=4, column=0)
        self.paritybits_val = StringVar()
        self.paritybits_val = ser111.ser.parity
        paritybitslist = ['N', 'O', 'E', 'M', 'S']
        self.paritybits = ttk.Combobox(self.generalcontrollsframe, textvariable=self.paritybits_val, state='readonly')
        i = 0
        for pbits in paritybitslist:
            if pbits == ser111.ser.parity:
                break
            else:
                i += 1

        self.paritybits.config(values=paritybitslist)
        self.paritybits.current(i)
        self.paritybits.grid(row=4, column=1)

        self.stopbitslbl = ttk.Label(self.generalcontrollsframe, text="Stopbits", width=16)
        self.stopbitslbl.grid(row=5, column=0)
        self.stopbits_val = StringVar()
        self.stopbits_val = ser111.ser.stopbits
        stopbitslist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.stopbits = ttk.Combobox(self.generalcontrollsframe, textvariable=self.stopbits_val, state='readonly')
        i = 0
        for sbits in stopbitslist:
            if sbits == str(ser111.ser.stopbits):
                break
            else:
                i += 1

        self.stopbits.config(values=stopbitslist)
        self.stopbits.current(i)
        self.stopbits.grid(row=5, column=1)

        self.setserial = ttk.Button(self.generalcontrollsframe, text="Set", width=16)
        self.setserial.grid(row=6, column=0, columnspan=2)

        self.update_info()
        # testbut = ttk.Button(GeneralControllsframe,text="3")
        # testbut.grid(row=0,column =0)
    def update_info(self):
        self.portcb_val = ser111.ser.port
        print(ser111.ser.port)


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


class SerialStuff:
    # https://mail.python.org/pipermail/tkinter-discuss/2013-August/003477.html
    def __init__(self):

        self.ser = serial.Serial()  # creates serial object
        self.grbl_version = "Grbl Not Detected"
        self.portList = []
        self.Buffer = []

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
                        # print("No data")
                        u = 1
                    else:
                        self.grbl_version = data
                        # print(data)
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
queue = queue.threading
ser111 = SerialStuff()
ser111.auto_setup(115200, None, None, None, 5)
app = NobleLaser()

app.mainloop()