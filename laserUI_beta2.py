import sys
# import socket
import glob
import time
import serial
import tkinter as tk
from tkinter import ttk


class NobleLaser(tk.Tk):  # V0.0.1

    def __init__(self, *args, **kwargs):
        Ver = "V 0.0.1"
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Noble Laser " + Ver + " --- " + ser111.grbl_version)
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
        # main Frame with nav buttons //start

        generalpagebutt = tk.Button(self, text="General", width=10, height=2, bg='gray',command=lambda: controller.show_frame(GeneralPage))
        # generalPagebutt.place(y=0, x=0)
        generalpagebutt.grid(row=0, column=0)

        filesyspagebutt = tk.Button(self, text="File System", width=10, height=2, command=lambda: controller.show_frame(FileSYSPage))
        # filesysPagebutt.place(y=0, x=0)
        filesyspagebutt.grid(row=0, column=1)

        serialpagebutt = tk.Button(self, text="Serial", width=10, height=2, command=lambda: controller.show_frame(SerialPage))
        # SerialPagebutt.place(y=0, x=0)
        serialpagebutt.grid(row=0, column=2)

        networkpagebutt = tk.Button(self, text="Network", width=10, height=2, command=lambda: controller.show_frame(NetworkPage))
        # NetworkPagebutt.place(y=0, x=0)
        networkpagebutt.grid(row=0, column=3)

        # main Frame with nav buttons //End
        # secondary frame with page controlls //Start

        generalcontrollsframe = ttk.Frame(self)
        generalcontrollsframe.grid(row=1, column=0,columnspan=4,sticky="nsew")

        grbllbl = ttk.Label(generalcontrollsframe, text="Controller Status", width=16)
        grbllbl.grid(row=0, column=0)
        grblstatus = ttk.Label(generalcontrollsframe, width=16, text="Connected")
        grblstatus.grid(row=0, column=1)

        grblhome = ttk.Button(generalcontrollsframe, text="Home Laser", width=16)
        grblhome.grid(row=1,column=0)
        grblstop = ttk.Button(generalcontrollsframe, text="Stop Laser", width=16)
        grblstop.grid(row=1, column=1)
        grblend = ttk.Button(generalcontrollsframe, text="End Program", width=16)
        grblend.grid(row=1, column=2)
        grblhold = ttk.Button(generalcontrollsframe, text="Hold Laser", width=16)
        grblhold.grid(row=2, column=0)
        grblstart = ttk.Button(generalcontrollsframe, text="Start Laser", width=16)
        grblstart.grid(row=2, column=1)
        grblup = ttk.Button(generalcontrollsframe, text="+Z", width=16)
        grblup.grid(row=4, column=0, columnspan=2)
        grblleft = ttk.Button(generalcontrollsframe, text="-X", width=16)
        grblleft.grid(row=5, column=0)
        grblright = ttk.Button(generalcontrollsframe, text="+X", width=16)
        grblright.grid(row=5, column=1)
        grbldown = ttk.Button(generalcontrollsframe, text="-Z", width=16)
        grbldown.grid(row=6, column=0, columnspan=2)
        grbldown = ttk.Button(generalcontrollsframe, text="Load Program", width=16)
        grbldown.grid(row=5, column=2, )

        # testbut = ttk.Button(GeneralControllsframe, text="1")
        # testbut.grid(row=0, column=0)

        # secondary frame with page controlls //End


class FileSYSPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        generalpagebutt = tk.Button(self, text="General", width=10, height=2, command=lambda: controller.show_frame(GeneralPage))
        generalpagebutt.grid(row=0, column=0)

        filesyspagebutt = tk.Button(self, text="File System", width=10, height=2, bg='gray', command=lambda: controller.show_frame(FileSYSPage))
        filesyspagebutt.grid(row=0, column=1)

        serialpagebutt = tk.Button(self, text="Serial", width=10, height=2, command=lambda: controller.show_frame(SerialPage))
        serialpagebutt.grid(row=0, column=2)

        networkpagebutt = tk.Button(self, text="Network", width=10, height=2, command=lambda: controller.show_frame(NetworkPage))
        networkpagebutt.grid(row=0, column=3)

        generalcontrollsframe = ttk.Frame(self)  # secondary frame with page controlls
        generalcontrollsframe.grid(row=1, column=0,columnspan=4,sticky="nsew")

        homedirlbl = ttk.Label(generalcontrollsframe, text="Home Dir", width=16)
        homedirlbl.grid(row=0, column=0)
        homedir = ttk.Entry(generalcontrollsframe, width=16)
        homedir.grid(row=0, column=1)

        remotedirlbl = ttk.Label(generalcontrollsframe, text="Remote Dir", width=16)
        remotedirlbl.grid(row=2, column=0)
        remotedir = ttk.Entry(generalcontrollsframe, width=16)
        remotedir.grid(row=2, column=1)

        copytodir = ttk.Button(generalcontrollsframe, text="Copy TO Remote Dir", width=16)
        copytodir.grid(row=3, column=0)

        from_dir = ttk.Button(generalcontrollsframe, text="From TO Remote Dir", width=16)
        from_dir.grid(row=3, column=1)

        usernamelbl = ttk.Label(generalcontrollsframe, text="Username", width=16)
        usernamelbl.grid(row=4, column=0)
        username = ttk.Entry(generalcontrollsframe, width=16)
        username.grid(row=4, column=1)

        passwordlbl = ttk.Label(generalcontrollsframe, text="Password", width=16)
        passwordlbl.grid(row=5, column=0)
        password = tk.Entry(generalcontrollsframe, width=16)
        password.grid(row=5, column=1)

        setfilesys = ttk.Button(generalcontrollsframe, text="Set", width=16)
        setfilesys.grid(row=6, column=0, columnspan=2)

        # testbut = ttk.Button(GeneralControllsframe,text="2")
        # testbut.grid(row=0,column =0)


class SerialPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        generalpagebutt = tk.Button(self, text="General", width=10, height=2, command=lambda: controller.show_frame(GeneralPage))
        generalpagebutt.grid(row=0, column=0)

        filesyspagebutt = tk.Button(self, text="File System", width=10, eight=2, command=lambda: controller.show_frame(FileSYSPage))
        filesyspagebutt.grid(row=0, column=1)

        serialpagebutt = tk.Button(self, text="Serial", width=10, height=2, bg='gray', command=lambda: controller.show_frame(SerialPage))
        serialpagebutt.grid(row=0, column=2)

        networkpagebutt = tk.Button(self, text="Network", width=10, height=2, command=lambda: controller.show_frame(NetworkPage))
        networkpagebutt.grid(row=0, column=3)

        generalcontrollsframe = ttk.Frame(self)  # secondary frame with page controlls
        generalcontrollsframe.grid(row=1, column=0, columnspan=4, sticky="nsew")

        portlbl = ttk.Label(generalcontrollsframe, text="Port", width=16)
        portlbl.grid(row=0, column=0)
        portcb = ttk.Combobox(generalcontrollsframe)
        portcb.config(values=('1', '2', '3', '4'))
        portcb.grid(row=0, column=1)

        baudratelbl = ttk.Label(generalcontrollsframe, text="Baudrate", width=16)
        baudratelbl.grid(row=2, column=0)
        baudrate = ttk.Combobox(generalcontrollsframe)
        baudrate.config(values=('9600', '19200', '38400', '57600', '115200'))
        baudrate.grid(row=2, column=1)

        databitslbl = ttk.Label(generalcontrollsframe, text="Data Bits", width=16)
        databitslbl.grid(row=3, column=0)
        databits = ttk.Combobox(generalcontrollsframe)
        databits.config(values=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))
        databits.grid(row=3, column=1)

        paritybitslbl = ttk.Label(generalcontrollsframe, text="Paritybits", width=16)
        paritybitslbl.grid(row=4, column=0)
        paritybits = ttk.Combobox(generalcontrollsframe)
        paritybits.config(values=('none N', 'odd (O)', 'even (E)', 'mark (M)', 'space (S)'))
        paritybits.grid(row=4, column=1)

        stopbitslbl = ttk.Label(generalcontrollsframe, text="Stopbits", width=16)
        stopbitslbl.grid(row=5, column=0)
        stopbits = ttk.Combobox(generalcontrollsframe)
        stopbits.config(values=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))
        stopbits.grid(row=5, column=1)

        setserial = ttk.Button(generalcontrollsframe, text="Set", width=16)
        setserial.grid(row=6, column=0, columnspan=2)

        # testbut = ttk.Button(GeneralControllsframe,text="3")
        # testbut.grid(row=0,column =0)


class NetworkPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        generalpagebutt = tk.Button(self, text="General", width=10, height=2, command=lambda: controller.show_frame(GeneralPage))
        generalpagebutt.grid(row=0, column=0)

        filesyspagebutt = tk.Button(self, text="File System", width=10, height=2, command=lambda: controller.show_frame(FileSYSPage))
        filesyspagebutt.grid(row=0, column=1)

        serialpagebutt = tk.Button(self, text="Serial", width=10, height=2, command=lambda: controller.show_frame(SerialPage))
        serialpagebutt.grid(row=0, column=2)

        networkpagebutt = tk.Button(self, text="Network", width=10, height=2, bg='gray', command=lambda: controller.show_frame(NetworkPage))
        networkpagebutt.grid(row=0, column=3)

        generalcontrollsframe = ttk.Frame(self)  # secondary frame with page controlls
        generalcontrollsframe.grid(row=1, column=0, columnspan=4, sticky="nsew")

        static = ttk.Radiobutton(generalcontrollsframe, text="Static")
        static.grid(row=0, column=1)

        dhcp = ttk.Radiobutton(generalcontrollsframe, text="Dhcp")
        dhcp.grid(row=0, column=0)

        ipaddress = ttk.Label(generalcontrollsframe, text="Ip Address")
        ipaddress.grid(row=1, column=0)
        ipaddrv4 = ttk.Entry(generalcontrollsframe, width=16)
        ipaddrv4.grid(row=1, column=1)

        subnetlbl = ttk.Label(generalcontrollsframe, text="Subnet")
        subnetlbl.grid(row=2, column=0)
        subnet = ttk.Entry(generalcontrollsframe, width=16)
        subnet.grid(row=2, column=1)

        gatewaylbl = ttk.Label(generalcontrollsframe, text="Gateway")
        gatewaylbl.grid(row=3, column=0)
        gateway = ttk.Entry(generalcontrollsframe, width=16)
        gateway.grid(row=3, column=1)

        dns1lbl = ttk.Label(generalcontrollsframe, text="Dns1")
        dns1lbl.grid(row=4, column=0)
        dns1 = ttk.Entry(generalcontrollsframe, width=16)
        dns1.grid(row=4, column=1)

        dns2lbl = ttk.Label(generalcontrollsframe, text="Dns2")
        dns2lbl.grid(row=5, column=0)
        dns2 = ttk.Entry(generalcontrollsframe, width=16)
        dns2.grid(row=5, column=1)

        setnetwork = ttk.Button(generalcontrollsframe, text="Set", width=16)
        setnetwork.grid(row=7, column=0, columnspan=2)

        # testbut = ttk.Button(GeneralControllsframe,text="4")
        # testbut.grid(row=0,column =0)


class SerialStuff:

    def __init__(self):

        self.ser = serial.Serial()  # creates serial object
        self.grbl_version = "Grbl Not Detected"

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
            self.serial_setup(port, 115200, None, None, None, None)

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
        for port in available_ports:
            # print(port)
            self.serial_setup(port, 115200, None, None, None, None)
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

ser111 = SerialStuff()
ser111.auto_setup(115200, None, None, None, 5)
print(ser111.grbl_version)
app = NobleLaser()

app.mainloop()
