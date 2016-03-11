import tkinter as tk
from tkinter import ttk


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

        generalPagebutt = ttk.Button(self, text="General", command=lambda: controller.show_frame(GeneralPage))
        generalPagebutt.grid(row=0, column=0)

        filesysPagebutt = ttk.Button(self, text="File System", command=lambda: controller.show_frame(FileSYSPage))
        filesysPagebutt.grid(row=0, column=1)

        SerialPagebutt = ttk.Button(self, text="Serial", command=lambda: controller.show_frame(SerialPage))
        SerialPagebutt.grid(row=0, column=2)

        NetworkPagebutt = ttk.Button(self, text="Network", command=lambda: controller.show_frame(NetworkPage))
        NetworkPagebutt.grid(row=0, column=3)

        # main Frame with nav buttons //End
        # secondary frame with page controlls //Start

        GeneralControllsframe = ttk.Frame(self)
        GeneralControllsframe.grid(row=1, column=0)

        testbut = ttk.Button(GeneralControllsframe, text="1")
        testbut.grid(row=0, column=0)

    # secondary frame with page controlls //End


class FileSYSPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        generalPagebutt = ttk.Button(self, text="General", command=lambda: controller.show_frame(GeneralPage))
        generalPagebutt.grid(row=0, column=0)

        filesysPagebutt = ttk.Button(self, text="File System", command=lambda: controller.show_frame(FileSYSPage))
        filesysPagebutt.grid(row=0, column=1)

        SerialPagebutt = ttk.Button(self, text="Serial", command=lambda: controller.show_frame(SerialPage))
        SerialPagebutt.grid(row=0, column=2)

        NetworkPagebutt = ttk.Button(self, text="Network", command=lambda: controller.show_frame(NetworkPage))
        NetworkPagebutt.grid(row=0, column=3)

        GeneralControllsframe = ttk.Frame(self)  # secondary frame with page controlls
        GeneralControllsframe.grid(row=1, column=0)

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

        generalPagebutt = ttk.Button(self, text="General", command=lambda: controller.show_frame(GeneralPage))
        generalPagebutt.grid(row=0, column=0)

        filesysPagebutt = ttk.Button(self, text="File System", command=lambda: controller.show_frame(FileSYSPage))
        filesysPagebutt.grid(row=0, column=1)

        SerialPagebutt = ttk.Button(self, text="Serial", command=lambda: controller.show_frame(SerialPage))
        SerialPagebutt.grid(row=0, column=2)

        NetworkPagebutt = ttk.Button(self, text="Network", command=lambda: controller.show_frame(NetworkPage))
        NetworkPagebutt.grid(row=0, column=3)

        GeneralControllsframe = ttk.Frame(self)  # secondary frame with page controlls
        GeneralControllsframe.grid(row=1, column=0)

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

        generalPagebutt = ttk.Button(self, text="General", command=lambda: controller.show_frame(GeneralPage))
        generalPagebutt.grid(row=0, column=0)

        filesysPagebutt = ttk.Button(self, text="File System", command=lambda: controller.show_frame(FileSYSPage))
        filesysPagebutt.grid(row=0, column=1)

        SerialPagebutt = ttk.Button(self, text="Serial", command=lambda: controller.show_frame(SerialPage))
        SerialPagebutt.grid(row=0, column=2)

        NetworkPagebutt = ttk.Button(self, text="Network", command=lambda: controller.show_frame(NetworkPage))
        NetworkPagebutt.grid(row=0, column=3)

        GeneralControllsframe = ttk.Frame(self)  # secondary frame with page controlls
        GeneralControllsframe.grid(row=1, column=0)

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

        dns2lbl = ttk.Label(GeneralControllsframe, text="DNS2", width=16)
        dns2lbl.grid(row=6, column=0)
        dns2 = ttk.Entry(GeneralControllsframe, width=16)
        dns2.grid(row=6, column=1)

        setnetwork = ttk.Button(GeneralControllsframe, text="Set", width=16)
        setnetwork.grid(row=7, column=0, columnspan=2)

    # testbut = ttk.Button(GeneralControllsframe,text="4")
    # testbut.grid(row=0,column =0)


app = NobleLaser()
app.mainloop()
