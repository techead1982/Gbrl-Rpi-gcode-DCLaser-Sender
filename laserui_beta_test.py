import threading
from tkinter import ttk

from Gbrl_Rpi_gcode_DcLaser_Sender import *
from commands import *


class gSenderAPP(threading.Thread):
	def __init__(self):
	
		self.root = Tk()
		self.root.title("NobleLase v0.0.1")
		self.root.geometry("800x480+100+100")
		self.root.resizable(False, False)
		self.s = StringVar()
		
		self.notebook = ttk.Notebook(self.root)
		self.notebook.pack()

		self.f1 = ttk.Frame(self.notebook)  # first page, which would get widgets gridded into it
		self.f2 = ttk.Frame(self.notebook)
		self.f3 = ttk.Frame(self.notebook)
		self.f4 = ttk.Frame(self.notebook)
		
		self.notebook.add(self.f1, text='Genanl')
		self.notebook.add(self.f2, text='File System')
		self.notebook.add(self.f3, text='Serial')
		self.notebook.add(self.f4, text='Network')
		
		self.static = Radiobutton(self.f4, text="Static")
		self.static.grid(row=0, column=1)
		
		self.dhcp = Radiobutton(self.f4, text="Dhcp")
		self.dhcp.grid(row=0, column=0)
		
		self.ipaddress = Label(self.f4, text="Ip Address")
		self.ipaddress.grid(row=1, column=0)
		self.ipaddrv4 = Entry(self.f4, width=16)
		self.ipaddrv4.grid(row=1, column=1)

		self.Subnetlbl = Label(self.f4, text="Subnet")
		self.Subnetlbl.grid(row=2, column=0)
		self.Subnet = Entry(self.f4, width=16)
		self.Subnet.grid(row=2, column=1)

		self.Gatewaylbl = Label(self.f4, text="Gateway")
		self.Gatewaylbl.grid(row=3, column=0)
		self.Gateway = Entry(self.f4, width=16)
		self.Gateway.grid(row=3, column=1)

		self.dns1lbl = Label(self.f4, text="Dns1", width=16)
		self.dns1lbl.grid(row=4, column=0)
		self.dns1 = Entry(self.f4, width=16)
		self.dns1.grid(row=4, column=1)

		self.dns2lbl = Label(self.f4, text="DNS2", width=16)
		self.dns2lbl.grid(row=6, column=0)
		self.dns2 = Entry(self.f4, width=16)
		self.dns2.grid(row=6, column=1)

		self.setnetwork = Button(self.f4, text="Set", width=16)
		self.setnetwork.grid(row=7, column=0, columnspan=2)

		self.portlbl = Label(self.f3, text="Port", width=16)
		self.portlbl.grid(row=0, column=0)
		self.portcb = ttk.Combobox(self.f3)
		self.portcb.config(values=('1', '2', '3', '4'))
		self.portcb.grid(row=0, column=1)

		self.baudratelbl = Label(self.f3, text="Baudrate", width=16)
		self.baudratelbl.grid(row=2, column=0)
		self.baudrate = ttk.Combobox(self.f3)
		self.baudrate.config(values=('9600', '19200', '38400', '57600', '115200'))
		self.baudrate.grid(row=2, column=1)

		self.databitslbl = Label(self.f3, text="Data Bits", width=16)
		self.databitslbl.grid(row=3, column=0)
		self.databits = ttk.Combobox(self.f3)
		self.databits.config(values=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))
		self.databits.grid(row=3, column=1)

		self.Paritybitslbl = Label(self.f3, text="Paritybits", width=16)
		self.Paritybitslbl.grid(row=4, column=0)
		self.Paritybits = ttk.Combobox(self.f3)
		self.Paritybits.config(values=('none N', 'odd (O)', 'even (E)', 'mark (M)', 'space (S)'))
		self.Paritybits.grid(row=4, column=1)

		self.stopbitslbl = Label(self.f3, text="Stopbits", width=16)
		self.stopbitslbl.grid(row=5, column=0)
		self.stopbits = ttk.Combobox(self.f3)
		self.stopbits.config(values=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))
		self.stopbits.grid(row=5, column=1)

		self.setserial = Button(self.f3, text="Set", width=16)
		self.setserial.grid(row=6, column=0, columnspan=2)

		self.homedirlbl = Label(self.f2, text="Home Dir", width=16)
		self.homedirlbl.grid(row=0, column=0)
		self.homedir = Entry(self.f2, width=16)
		self.homedir.grid(row=0, column=1)

		self.remotedirlbl = Label(self.f2, text="Remote Dir", width=16)
		self.remotedirlbl.grid(row=2, column=0)
		self.remotedir = Entry(self.f2, width=16)
		self.remotedir.grid(row=2, column=1)

		self.copytodir = Button(self.f2, text="Copy TO Remote Dir", width=16)
		self.copytodir.grid(row=3, column=0)

		self.from_dir = Button(self.f2, text="From TO Remote Dir", width=16)
		self.from_dir.grid(row=3, column=1)

		self.Usernamelbl = Label(self.f2, text="Username", width=16)
		self.Usernamelbl.grid(row=4, column=0)
		self.Username = Entry(self.f2, width=16)
		self.Username.grid(row=4, column=1)

		self.Passwordlbl = Label(self.f2, text="Password", width=16)
		self.Passwordlbl.grid(row=5, column=0)
		self.Password = Entry(self.f2, width=16)
		self.Password.grid(row=5, column=1)

		self.setfilesys = Button(self.f2, text="Set", width=16)
		self.setfilesys.grid(row=6, column=0, columnspan=2)

		self.gbrllbl = Label(self.f1, text="Conntroler Status", width=16)
		self.gbrllbl.grid(row=0, column=0)
		self.gbrlstatus = Label(self.f1, text="Connected", bg="green", fg="black", width=16)
		self.gbrlstatus.grid(row=0, column=1)

		self.gbrlhome = Button(self.f1, text="Home Laser", width=16, command=hi, bg="blue")
		self.gbrlhome.grid(row=1,column=0)
		self.gbrlstop = Button(self.f1, text="Stop Laser", width=16, bg="red")
		self.gbrlstop.grid(row=1, column=1)
		self.gbrlend = Button(self.f1, text="End Program", width=16, bg="green")
		self.gbrlend.grid(row=1, column=2)
		self.gbrlhold = Button(self.f1, text="Hold Laser", width=16, bg="green")
		self.gbrlhold.grid(row=2, column=0)
		self.gbrlstart = Button(self.f1, text="Start Laser", width=16, bg="green")

		self.gbrlstart.grid(row=2, column=1)
		self.gbrlup = Button(self.f1, text="+Z", width=16, bg="green")
		self.gbrlup.grid(row=4, column=0, columnspan=2)
		self.gbrlleft = Button(self.f1, text="-X", width=16, bg="green")
		self.gbrlleft.grid(row=5, column=0)
		self.gbrlright = Button(self.f1, text="+X", width=16, bg="green")
		self.gbrlright.grid(row=5, column=1)
		self.gbrldown = Button(self.f1, text="-Z", width=16, bg="green")
		self.gbrldown.grid(row=6, column=0, columnspan=2)
		self.gbrldown = Button(self.f1, text="Load Program", width=16, bg="green")
		self.gbrldown.grid(row=5, column=2, )

		#self.gbrltext = Text(self.f1,height=10,width=10,bg="gray")
		#self.gbrltext.insert('1.0',self.s.get())
		#self.gbrltext.grid(row=2,column=0,columnspan=1)
		
		self.root.update()
		threading.Thread.__init__(self)
		
		self.root.mainloop()
		 
if __name__=='__main__':
	app = gSenderAPP()
	app.start()
	#root.mainloop()

# root.mainloop()
