import sys
import glob
import tkinter as tk
from tkinter import ttk
import serial as s


class NobleLaser(tk.Tk):  # V0.0.1

    def __init__(self, *args, **kwargs):
        Ver = "V 0.0.1"
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Noble Laser " + Ver)
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

		generalPagebutt = tk.Button(self, text="General",width=10,height=2,bg = 'gray',command=lambda: controller.show_frame(GeneralPage))
		#generalPagebutt.place(y=0, x=0)
		generalPagebutt.grid(row=0, column=0)

		filesysPagebutt = tk.Button(self, text="File System",width=10,height=2, command=lambda: controller.show_frame(FileSYSPage))
		#filesysPagebutt.place(y=0, x=0)
		filesysPagebutt.grid(row=0, column=1)

		SerialPagebutt = tk.Button(self, text="Serial",width=10,height=2, command=lambda: controller.show_frame(SerialPage))
		#SerialPagebutt.place(y=0, x=0)
		SerialPagebutt.grid(row=0, column=2)

		NetworkPagebutt = tk.Button(self, text="Network",width=10,height=2, command=lambda: controller.show_frame(NetworkPage))
		#NetworkPagebutt.place(y=0, x=0)
		NetworkPagebutt.grid(row=0, column=3)

		# main Frame with nav buttons //End
		# secondary frame with page controlls //Start

		GeneralControllsframe = ttk.Frame(self)
		GeneralControllsframe.grid(row=1, column=0,columnspan=4,sticky="nsew")

		gbrllbl = ttk.Label(GeneralControllsframe, text="Controller Status", width=16)
		gbrllbl.grid(row=0, column=0)
		gbrlstatus = ttk.Label(GeneralControllsframe, width=16, text="Connected")
		gbrlstatus.grid(row=0, column=1)

		gbrlhome = ttk.Button(GeneralControllsframe, text="Home Laser", width=16)
		gbrlhome.grid(row=1,column=0)
		gbrlstop = ttk.Button(GeneralControllsframe, text="Stop Laser", width=16)
		gbrlstop.grid(row=1, column=1)
		gbrlend = ttk.Button(GeneralControllsframe, text="End Program", width=16)
		gbrlend.grid(row=1, column=2)
		gbrlhold = ttk.Button(GeneralControllsframe, text="Hold Laser", width=16)
		gbrlhold.grid(row=2, column=0)
		gbrlstart = ttk.Button(GeneralControllsframe, text="Start Laser", width=16)
		gbrlstart.grid(row=2, column=1)
		gbrlup = ttk.Button(GeneralControllsframe, text="+Z", width=16)
		gbrlup.grid(row=4, column=0, columnspan=2)
		gbrlleft = ttk.Button(GeneralControllsframe, text="-X", width=16)
		gbrlleft.grid(row=5, column=0)
		gbrlright = ttk.Button(GeneralControllsframe, text="+X", width=16)
		gbrlright.grid(row=5, column=1)
		gbrldown = ttk.Button(GeneralControllsframe, text="-Z", width=16)
		gbrldown.grid(row=6, column=0, columnspan=2)
		gbrldown = ttk.Button(GeneralControllsframe, text="Load Program", width=16)
		gbrldown.grid(row=5, column=2, )

		#testbut = ttk.Button(GeneralControllsframe, text="1")
		#testbut.grid(row=0, column=0)

	# secondary frame with page controlls //End


class FileSYSPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        generalPagebutt = tk.Button(self, text="General",width=10,height=2, command=lambda: controller.show_frame(GeneralPage))
        generalPagebutt.grid(row=0, column=0)

        filesysPagebutt = tk.Button(self, text="File System",width=10,height=2,bg = 'gray', command=lambda: controller.show_frame(FileSYSPage))
        filesysPagebutt.grid(row=0, column=1)

        SerialPagebutt = tk.Button(self, text="Serial",width=10,height=2, command=lambda: controller.show_frame(SerialPage))
        SerialPagebutt.grid(row=0, column=2)

        NetworkPagebutt = tk.Button(self, text="Network",width=10,height=2, command=lambda: controller.show_frame(NetworkPage))
        NetworkPagebutt.grid(row=0, column=3)

        GeneralControllsframe = ttk.Frame(self)  # secondary frame with page controlls
        GeneralControllsframe.grid(row=1, column=0,columnspan=4,sticky="nsew")

        homedirlbl = ttk.Label(GeneralControllsframe, text="Home Dir", width=16)
        homedirlbl.grid(row=0, column=0)
        homedir = ttk.Entry(GeneralControllsframe, width=16)
        homedir.grid(row=0, column=1)

        remotedirlbl = ttk.Label(GeneralControllsframe, text="Remote Dir", width=16)
        remotedirlbl.grid(row=2, column=0)
        remotedir = ttk.Entry(GeneralControllsframe, width=16)
        remotedir.grid(row=2, column=1)

        copytodir = ttk.Button(GeneralControllsframe, text="Copy TO Remote Dir", width=16)
        copytodir.grid(row=3, column=0)

        from_dir = ttk.Button(GeneralControllsframe, text="From TO Remote Dir", width=16)
        from_dir.grid(row=3, column=1)

        Usernamelbl = ttk.Label(GeneralControllsframe, text="Username", width=16)
        Usernamelbl.grid(row=4, column=0)
        Username = ttk.Entry(GeneralControllsframe, width=16)
        Username.grid(row=4, column=1)

        Passwordlbl = ttk.Label(GeneralControllsframe, text="Password", width=16)
        Passwordlbl.grid(row=5, column=0)
        Password = tk.Entry(GeneralControllsframe, width=16)
        Password.grid(row=5, column=1)

        setfilesys = ttk.Button(GeneralControllsframe, text="Set", width=16)
        setfilesys.grid(row=6, column=0, columnspan=2)

    # testbut = ttk.Button(GeneralControllsframe,text="2")
    # testbut.grid(row=0,column =0)


class SerialPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        generalPagebutt = tk.Button(self, text="General",width=10,height=2, command=lambda: controller.show_frame(GeneralPage))
        generalPagebutt.grid(row=0, column=0)

        filesysPagebutt = tk.Button(self, text="File System",width=10,height=2, command=lambda: controller.show_frame(FileSYSPage))
        filesysPagebutt.grid(row=0, column=1)

        SerialPagebutt = tk.Button(self, text="Serial",width=10,height=2,bg = 'gray', command=lambda: controller.show_frame(SerialPage))
        SerialPagebutt.grid(row=0, column=2)

        NetworkPagebutt = tk.Button(self, text="Network",width=10,height=2, command=lambda: controller.show_frame(NetworkPage))
        NetworkPagebutt.grid(row=0, column=3)

        GeneralControllsframe = ttk.Frame(self)  # secondary frame with page controlls
        GeneralControllsframe.grid(row=1, column=0,columnspan=4,sticky="nsew")

        portlbl = ttk.Label(GeneralControllsframe, text="Port", width=16)
        portlbl.grid(row=0, column=0)
        portcb = ttk.Combobox(GeneralControllsframe)
        portcb.config(values=('1', '2', '3', '4'))
        portcb.grid(row=0, column=1)

        baudratelbl = ttk.Label(GeneralControllsframe, text="Baudrate", width=16)
        baudratelbl.grid(row=2, column=0)
        baudrate = ttk.Combobox(GeneralControllsframe)
        baudrate.config(values=('9600', '19200', '38400', '57600', '115200'))
        baudrate.grid(row=2, column=1)

        databitslbl = ttk.Label(GeneralControllsframe, text="Data Bits", width=16)
        databitslbl.grid(row=3, column=0)
        databits = ttk.Combobox(GeneralControllsframe)
        databits.config(values=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))
        databits.grid(row=3, column=1)

        Paritybitslbl = ttk.Label(GeneralControllsframe, text="Paritybits", width=16)
        Paritybitslbl.grid(row=4, column=0)
        Paritybits = ttk.Combobox(GeneralControllsframe)
        Paritybits.config(values=('none N', 'odd (O)', 'even (E)', 'mark (M)', 'space (S)'))
        Paritybits.grid(row=4, column=1)

        stopbitslbl = ttk.Label(GeneralControllsframe, text="Stopbits", width=16)
        stopbitslbl.grid(row=5, column=0)
        stopbits = ttk.Combobox(GeneralControllsframe)
        stopbits.config(values=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))
        stopbits.grid(row=5, column=1)

        setserial = ttk.Button(GeneralControllsframe, text="Set", width=16)
        setserial.grid(row=6, column=0, columnspan=2)

    # testbut = ttk.Button(GeneralControllsframe,text="3")
    # testbut.grid(row=0,column =0)


class NetworkPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        generalPagebutt = tk.Button(self, text="General",width=10,height=2, command=lambda: controller.show_frame(GeneralPage))
        generalPagebutt.grid(row=0, column=0)

        filesysPagebutt = tk.Button(self, text="File System",width=10,height=2, command=lambda: controller.show_frame(FileSYSPage))
        filesysPagebutt.grid(row=0, column=1)

        SerialPagebutt = tk.Button(self, text="Serial",width=10,height=2, command=lambda: controller.show_frame(SerialPage))
        SerialPagebutt.grid(row=0, column=2)

        NetworkPagebutt = tk.Button(self, text="Network",width=10,height=2,bg = 'gray', command=lambda: controller.show_frame(NetworkPage))
        NetworkPagebutt.grid(row=0, column=3)

        GeneralControllsframe = ttk.Frame(self)  # secondary frame with page controlls
        GeneralControllsframe.grid(row=1, column=0,columnspan=4,sticky="nsew")

        static = ttk.Radiobutton(GeneralControllsframe, text="Static")
        static.grid(row=0, column=1)

        dhcp = ttk.Radiobutton(GeneralControllsframe, text="Dhcp")
        dhcp.grid(row=0, column=0)

        ipaddress = ttk.Label(GeneralControllsframe, text="Ip Address")
        ipaddress.grid(row=1, column=0)
        ipaddrv4 = ttk.Entry(GeneralControllsframe, width=16)
        ipaddrv4.grid(row=1, column=1)

        Subnetlbl = ttk.Label(GeneralControllsframe, text="Subnet")
        Subnetlbl.grid(row=2, column=0)
        Subnet = ttk.Entry(GeneralControllsframe, width=16)
        Subnet.grid(row=2, column=1)

        Gatewaylbl = ttk.Label(GeneralControllsframe, text="Gateway")
        Gatewaylbl.grid(row=3, column=0)
        Gateway = ttk.Entry(GeneralControllsframe, width=16)
        Gateway.grid(row=3, column=1)

        dns1lbl = ttk.Label(GeneralControllsframe, text="Dns1", width=16)
        dns1lbl.grid(row=4, column=0)
        dns1 = ttk.Entry(GeneralControllsframe, width=16)
        dns1.grid(row=4, column=1)

        dns2lbl = ttk.Label(GeneralControllsframe, text="Dns2", width=16)
        dns2lbl.grid(row=5, column=0)
        dns2 = ttk.Entry(GeneralControllsframe, width=16)
        dns2.grid(row=5, column=1)

        setnetwork = ttk.Button(GeneralControllsframe, text="Set", width=16)
        setnetwork.grid(row=7, column=0, columnspan=2)

    # testbut = ttk.Button(GeneralControllsframe,text="4")
    # testbut.grid(row=0,column =0)
	
	
class SerialStuff():
	def __init__(self):
		self.ser = serial.Serial()
	def serial_ports():
		if sys.platform.startswith('win'):
			ports = ['COM%s'%(i+1)for i in range(256)]
		elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
			ports = glob.glob('/dev/tty[A-Za-z]*')
		elif sys.platform.startswith('darwin'):
			ports = glob.glob('/dev/tty.*')
		else:
			raise EnvironmentError('Unsupported platform')
		result = []
		for port in ports:
			try:
				s = serial.Serial(port)
				s.close()
				result.append(port)
			except (OSError, serial.SerialException):
				pass
		return result
	def serial_Setup(self,ComPort,BaudRate):
		self.ser.port = ComPort
		self.ser.baudrate = BaudRate
		
	def serial_Setup(self,ComPort,BaudRate,ByteSize):
		self.ser.port = ComPort
		self.ser.baudrate = BaudRate
		self.ser.bytesize = ByteSize
		
	def serial_Setup(self,ComPort,BaudRate,ByteSize,ParityBits):
		self.ser.port = ComPort
		self.ser.baudrate = BaudRate
		self.ser.bytesize = ByteSize
		self.ser.parity = ParityBits
		
	def serial_Setup(self,ComPort,BaudRate,ByteSize,ParityBits,StopBits):
		self.ser.port = ComPort
		self.ser.baudrate = BaudRate
		self.ser.bytesize = ByteSize
		self.ser.parity = ParityBits
		self.ser.stopbits = StopBits
		
	#def Stored_serial_Setup(self):
		#with open('SerialConfig.py','r',encoding='ascii') as f:
			
	#def Auto_Find_Grbl(self):
		#s=''
		#print(s)
			

#class NetworkShit():
	#def __init__():
		#s=''
		#print(s)

app = NobleLaser()

app.mainloop()
