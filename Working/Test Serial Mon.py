import serial
from tkinter import *

serialPort = "/dev/cu.usbmodem1D11"
baudRate = 115200
ser = serial.Serial(serialPort , baudRate, timeout=0, writeTimeout=0) #ensure non-blocking

#make a TkInter Window

root = Tk()
root.wm_title("Reading Serial")

# make a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# make a text box to put the serial output
log = Text ( root, width=20, height=10, takefocus=0)
log.pack()

# attach text box to scrollbar
log.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=log.yview)

#make our own buffer
#useful for parsing commands
#Serial.readline seems unreliable at times too


v=StringVar()
v.set("hi")

e = Entry(root, textvariable=v)
e.pack()

def sendBut():
    global eatsh
    s = v.get()
    i = 0
    print(s)
    eatsh = s+"\n"


b = Button(root, text="Send", command=sendBut)
b.pack()





def readSerial():
    global serBuffer
    global eatsh


    while True:
        c = ser.read().decode('ascii') # attempt to read a character from Serial

        #was anything read?
        if len(c) == 0:
            break

        # get the buffer from outside of this function
        # serBuffer
        # eatsh

        if eatsh !="":

            ser.write(eatsh.encode('ascii'))
            eatsh =""
        # check if character is a delimeter
        if c == '\r':
            c = '' # don't want returns. chuck it

        if c == '\n':
            serBuffer += "\n" # add the newline to the buffer

            #add the line to the TOP of the log
            log.insert('0.0', serBuffer)
            serBuffer = "" # empty the buffer
        else:
            serBuffer += c # add to the buffer

    root.after(10, readSerial) # check serial again soon




serBuffer =""
eatsh = ""

# after initializing serial, an arduino may need a bit of time to reset
root.after(100, readSerial)

root.mainloop()