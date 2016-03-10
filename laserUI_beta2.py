import tkinter as tk
from tkinter import ttk



class NobleLaser(tk.Tk): #V0.0.1
	
	def __init__(self,*args,**kwargs):
		Ver = "V 0.0.1"
		tk.Tk.__init__(self,*args,**kwargs)
		
		tk.Tk.wm_title(self,"Noble Laser "+Ver)
		tk.Tk.wm_geometry(self,"800x480+100+100")
		tk.Tk.wm_resizable(self,False, False)
		#tk.Tk.iconbitmap(self,default="some.ico")
		
		container = tk.Frame(self)
		container.pack(side = "top",fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		
		self.frames = {}
		
		for F in (GeneralPage,FileSYSPage,SerialPage,NetworkPage):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row = 0,column = 0, sticky = "nsew")
		self.show_frame(GeneralPage)
		
	def show_frame(self,cont):
		frame = self.frames[cont]
		frame.tkraise()
			
class GeneralPage(tk.Frame):
	
	def __init__(self,parent,controller):
		
		tk.Frame.__init__(self,parent)
		
		
		generalPagebutt = ttk.Button(self,text = "General")
		generalPagebutt.grid(row=0,column =0)
		
		filesysPagebutt = ttk.Button(self,text = "File System")
		filesysPagebutt.grid(row=0,column =1)
		
		SerialPagebutt = ttk.Button(self,text = "Serial")
		SerialPagebutt.grid(row=0,column =2)
		
		NetworkPagebutt = ttk.Button(self,text = "Network",command = lambda:controller.show_frame(NetworkPage))
		NetworkPagebutt.grid(row=0,column =3)
		
		tframe = ttk.Frame(self)
		tframe.grid(row=1,column=0)
		
		testPagebutt = ttk.Button(tframe,text = "Network")
		testPagebutt.grid(row=0,column =0)
		
		testPagebutt = ttk.Button(tframe,text = "Network")
		testPagebutt.grid(row=0,column =1)
		
		
class FileSYSPage(tk.Frame):
	
	def __init__(self,parent,controller):
		
		tk.Frame.__init__(self,parent)
		
		generalPagebutt = ttk.Button(self,text = "General")
		generalPagebutt.grid(row=0,column =0)
		
		filesysPagebutt = ttk.Button(self,text = "File System")
		filesysPagebutt.grid(row=0,column =1)
		
		SerialPagebutt = ttk.Button(self,text = "Serial")
		SerialPagebutt.grid(row=0,column =2)
		
		NetworkPagebutt = ttk.Button(self,text = "Network")
		NetworkPagebutt.grid(row=0,column =3)
		
class SerialPage(tk.Frame):
	
	def __init__(self,parent,controller):
		
		tk.Frame.__init__(self,parent)
		
		generalPagebutt = ttk.Button(self,text = "General")
		generalPagebutt.grid(row=0,column =0)
		
		filesysPagebutt = ttk.Button(self,text = "File System")
		filesysPagebutt.grid(row=0,column =1)
		
		SerialPagebutt = ttk.Button(self,text = "Serial")
		SerialPagebutt.grid(row=0,column =2)
		
		NetworkPagebutt = ttk.Button(self,text = "Network")
		NetworkPagebutt.grid(row=0,column =3)
		
class NetworkPage(tk.Frame):
	
	def __init__(self,parent,controller):
		
		tk.Frame.__init__(self,parent)
		
		generalPagebutt = ttk.Button(self,text = "General",command = lambda:controller.show_frame(GeneralPage))
		generalPagebutt.grid(row=0,column =0)
		
		filesysPagebutt = ttk.Button(self,text = "File System")
		filesysPagebutt.grid(row=0,column =1)
		
		SerialPagebutt = ttk.Button(self,text = "Serial")
		SerialPagebutt.grid(row=0,column =2)
		
		NetworkPagebutt = ttk.Button(self,text = "Network")
		NetworkPagebutt.grid(row=0,column =3)
		

app = NobleLaser()
app.mainloop()