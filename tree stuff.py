from tkinter import *
from tkinter import ttk

tk = Tk()
tree = ttk.Treeview(columns=('col0','col2','col3'))
tree.heading('#0', text='col1')
tree.heading('col2', text='col2')
tree.heading('col3', text='col3')
# tree.column('col0',stretch=NO,minwidth=0,width=0)

tree.pack()
tk.mainloop()

