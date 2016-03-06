from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("800x480+100+100")
root.resizable(False,False)

notebook = ttk.Notebook(root)
notebook.pack()

f1 = ttk.Frame(notebook)   # first page, which would get widgets gridded into it
f2 = ttk.Frame(notebook)
f3 = ttk.Frame(notebook)
f4 = ttk.Frame(notebook)
notebook.add(f1, text='Genanl')
notebook.add(f2, text='Setting')
notebook.add(f3, text='Serial')
notebook.add(f4, text='Network')

static = Radiobutton(f4, text="Static")
static.grid(row=0, column=0)

dhcp = Radiobutton(f4, text="Dhcp")
dhcp.grid(row=0, column=1)

ipaddress = Label(f4,text="Ip Address")
ipaddress.grid(row=1, column=0)
ipaddrv4 =Entry(f4, width=16)
ipaddrv4.grid(row=1, column=1)



Subnetlbl = Label(f4,text="Subnet")
Subnetlbl.grid(row=2, column=0)
Subnet =Entry(f4, width=16)
Subnet.grid(row=2, column=1)

Gatewaylbl = Label(f4,text="Gateway")
Gatewaylbl.grid(row=3, column=0)
Gateway = Entry(f4,width=16)
Gateway.grid(row=3, column=1)


portlbl = Label(f3, text ="Port", width=16)
portlbl.grid(row=0, column=0)
portcb = ttk.Combobox(f3)
portcb.config(values=('1','2','3','4'))
portcb.grid(row=0, column=1)
baudratelbl=Label(f3, text ="Baudrate", width=16)
baudratelbl.grid(row=2, column=0)
baudrate =Spinbox(f3, values=('9600', '19200', '38400', '57600','115200'))
baudrate.grid(row=2, column=1)
databitslbl =Label(f3,text="Data Bits", width=16)
databitslbl.grid(row=3, column=0)
databits = ttk.Combobox(f3)
databits.config(values=('1','2','3','4','5','6','7','8','9','10'))
databits.grid(row=3,column=1)
Paritybitslbl =Label(f3, text="Paritybits")
Paritybitslbl.grid(row=4,column=0)
Paritybits = ttk.Combobox(f3)
Paritybits.config(values=('none N', 'odd (O)', 'even (E)', 'mark (M)','space (S)'))
Paritybits.grid(row=4,column=1)









root.mainloop()