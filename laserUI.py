import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
label = tkinter.Label(tk, text="Hello, World")
label.pack(fill=X, expand=1)
button = tkinter.Button(tk,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()