from Gbrl_Rpi_gcode_DcLaser_Sender import *
import serial
import re
import time
import sys
from tkinter import *
from tkinter.filedialog import *

def hi():
    print("test")

def getFile():
	global fileName
    #print(gcodeSender.getFileInfo())
	fileName = gcodeSender.getFileInfo()
	print(fileName)
	Uitext1.insert(INSERT,fileName)

def sendFile():
	#gcodeSender.setSerial('COM3',115200,1)
	gcodeSender.streamFile(fileName,Uitext1,'COM5',115200)