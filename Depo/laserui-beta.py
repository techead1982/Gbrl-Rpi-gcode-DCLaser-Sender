from tkinter import *
from tkinter import ttk
from Gbrl_Rpi_gcode_DcLaser_Sender import *
from commands import *

root = Tk()
root.geometry("800x480+100+100")
root.resizable(False, False)

notebook = ttk.Notebook(root)
notebook.pack()

f1 = ttk.Frame(notebook)  # first page, which would get widgets gridded into it
f2 = ttk.Frame(notebook)
f3 = ttk.Frame(notebook)
f4 = ttk.Frame(notebook)
notebook.add(f1, text='General')
notebook.add(f2, text='File System')
notebook.add(f3, text='Serial')
notebook.add(f4, text='Network')

class app():
  def network(self):
    self.static = Radiobutton(f4, text="Static")
    self.static.grid(row=0, column=0)
    self.dhcp = Radiobutton(f4, text="Dhcp")
    self.dhcp.grid(row=0, column=1)
    self.ipaddress = Label(f4, text="Ip Address")
    self.ipaddress.grid(row=1, column=0)
    self.ipaddrv4 = Entry(f4, width=16)
    self.ipaddrv4.grid(row=1, column=1)
    self.Subnetlbl = Label(f4, text="Subnet")
    self.Subnetlbl.grid(row=2, column=0)
    self.Subnet = Entry(f4, width=16)
    self.Subnet.grid(row=2, column=1)
    self.Gatewaylbl = Label(f4, text="Gateway")
    self.Gatewaylbl.grid(row=3, column=0)
    self.Gateway = Entry(f4, width=16)
    self.Gateway.grid(row=3, column=1)
    self.dns1lbl = Label(f4, text="Dns1", width=16)
    self.dns1lbl.grid(row=4, column=0)
    self.dns1 = Entry(f4, width=16)
    self.dns1.grid(row=4, column=1)
    self.dns2lbl = Label(f4, text="DNS2", width=16)
    self.dns2lbl.grid(row=6, column=0)
    self.dns2 = Entry(f4, width=16)
    self.dns2.grid(row=6, column=1
    #self.setnetwork = Button(f4, text="Set", width=16)
    #self.setnetwork.grid(row=7, column=0, columnspan=2)

  def serial(self):
    self.portlbl = Label(f3, text="Port", width=16)
    self.portlbl.grid(row=0, column=0)
    self.portcb = ttk.Combobox(f3)
    self.portcb.config(values=('1', '2', '3', '4'))
    self.portcb.grid(row=0, column=1)
    self.baudratelbl = Label(f3, text="Baudrate", width=16)
    self.baudratelbl.grid(row=2, column=0)
    self.baudrate = ttk.Combobox(f3)
    self.baudrate.config(values=('9600', '19200', '38400', '57600', '115200'))
    self.baudrate.grid(row=2, column=1)
    self.databitslbl = Label(f3, text="Data Bits", width=16)
    self.databitslbl.grid(row=3, column=0)
    self.databits = ttk.Combobox(f3)
    self.databits.config(values=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))
    self.databits.grid(row=3, column=1)
    self.Paritybitslbl = Label(f3, text="Paritybits", width=16)
    self.Paritybitslbl.grid(row=4, column=0)
    self.Paritybits = ttk.Combobox(f3)
    self.Paritybits.config(values=('none N', 'odd (O)', 'even (E)', 'mark (M)', 'space (S)'))
    self.Paritybits.grid(row=4, column=1)
    self.stopbitslbl = Label(f3, text="Stopbits", width=16)
    self.stopbitslbl.grid(row=5, column=0)
    self.stopbits = ttk.Combobox(f3)
    self.stopbits.config(values=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))
    self.stopbits.grid(row=5, column=1)
    self.setserial = Button(f3, text="Set", width=16)
    self.setserial.grid(row=6, column=0, columnspan=2)

  def general(self):






homedirlbl = Label(f2, text="Home Dir", width=16)
homedirlbl.grid(row=0, column=0)
homedir = Entry(f2, width=16)
homedir.grid(row=0, column=1)

remotedirlbl = Label(f2, text="Remote Dir", width=16)
remotedirlbl.grid(row=2, column=0)
remotedir = Entry(f2, width=16)
remotedir.grid(row=2, column=1)

copytodir = Button(f2, text="Copy TO Remote Dir", width=16)
copytodir.grid(row=3, column=0)

from_dir = Button(f2, text="From TO Remote Dir", width=16)
from_dir.grid(row=3, column=1)

Usernamelbl = Label(f2, text="Username", width=16)
Usernamelbl.grid(row=4, column=0)
Username = Entry(f2, width=16)
Username.grid(row=4, column=1)

Passwordlbl = Label(f2, text="Password", width=16)
Passwordlbl.grid(row=5, column=0)
Password = Entry(f2, width=16)
Password.grid(row=5, column=1)

setfilesys = Button(f2, text="Set", width=16)
setfilesys.grid(row=6, column=0, columnspan=2)

gbrllbl = Label(f1, text="Conntroler Status", width=16)
gbrllbl.grid(row=0, column=0)
gbrlstatus = Label(f1, text="Connected", bg="green", fg="black", width=16)
gbrlstatus.grid(row=0, column=2)

gbrlhome = Button(f1, text="Home Laser", width=16, command=)
gbrlhome.grid(column=0, row=1)


app = app()
app.network()
app.serial()
app.general()
root.mainloop()
