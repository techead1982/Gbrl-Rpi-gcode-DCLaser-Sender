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







root.mainloop()