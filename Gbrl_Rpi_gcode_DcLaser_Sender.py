import serial
import re
import time
import sys 
from tkinter import *
from tkinter.filedialog import *

class LaserCom():
	comPort = 'COM3'
	baudRate = 115200
	timeOut = 1
	fileName = 'C:\git\Test.txt'
	lineCount = 0
	gcodeCount = 0
	charline = []
	grblBufferSize = 128
	def getFileInfo(self):
		fileName = askopenfilename(filetypes = (("G-code",".gcode"),("NC",".nc"),("All","*.*")))
		#fileName = fd.askopenfilename(filetypes = (("G-code",".gcode"),("NC",".nc"),("All","*.*")))
		return fileName
	def getSettings(self):
		stuff = 0
		#if file exsits then
			#read each lien for settings
			#comPort = com
			#baudRate = baud
			#timeOut = tOut
		#else do nothing
		return stuff
	def setSerial(self,com,baud,tOut):
		comPort = com
		baudRate = baud
		timeOut = tOut
	def streamFile(self,File,textBox,comPort1,baudRate1):
		print("i Work For now L35")
		s = serial.Serial(comPort1,baudRate1)
		s.write("\r\n\r\n")
		time.sleep(2)
		s.flushInput()
		with open(File,'r') as f:
			print("i Work For now L39")
			for line in f:
				lineCount += 1
				lineBlock =line.strip()
				charline.append(len(lineBlock) + 1)
				grblOut = ''
				while sum(charline) >= grblBufferSize - 1 |  s.inWaiting() :
					out_temp = s.readline().strip()
					if out_temp.find('ok') < 0 and out_temp.find('error') < 0 :
						textBox.insert(INSERT,"Debug:"+out_temp+'\n')
						
		
		