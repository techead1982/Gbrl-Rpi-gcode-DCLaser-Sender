import serial
import re
import time
import sys
#import argparse 
from tkinter import *
from tkinter.filedialog import *

class LaserCom():
	comPort = 'COM3'
	baudRate = 115200
	timeOut = 1
	fileName = ''
	lineCount = 0
	gcodeCount = 0
	charline = []
	
	def getFileInfo(self):
		fileName = askopenfilename(filetypes = (("G-code",".gcode"),("NC",".nc"),("All","*.*")))
		#fileName = fd.askopenfilename(filetypes = (("G-code",".gcode"),("NC",".nc"),("All","*.*")))
		return fileName
	def setSerial(self,com,baud,tOut):
		comPort = com
		baudRate = baud
		timeOut = tOut
	def streamFile(File):
		s = serial.Serial(self,comPort,baudRate,timeOut)
		s.write("\r\n\r\n")
		f = open(File,'r')