from tkinter import *
from tkinter import ttk


tk = Tk()


tree = ttk.Treeview()
tree.insert('', 'end', 'widgets', text='Widget Tour')

tree.pack()
tk.mainloop()

