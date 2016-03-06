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

ipaddress = Label(f4,text="Ip Address")
ipaddress.grid(row=0, column=0)
ipaddrv4 =Entry(f4, width=16)
ipaddrv4.grid(row=0, column=1)



Subnetlbl = Label(f4,text="Subnet")
Subnetlbl.grid(row=1, column=0)
Subnet =Entry(f4, width=16)
Subnet.grid(row=0, column=1)

Gateway = Label(f4,text="Gateway")
Gateway.grid(row=2, column=0)







root.mainloop()