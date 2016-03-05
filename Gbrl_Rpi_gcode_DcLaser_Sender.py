import serial
import re
import time
import sys 
from tkinter import *
from tkinter.filedialog import *

comPort = 'COM3'
baudRate = 115200
timeOut = 1
fileName = ''
lineCount = 0
gcodeCount = 0
charline = []
grblBufferSize = 128


class LaserCom():
	
	def getFileInfo(self):
		global fileName 
		fileName = askopenfilename(filetypes = (("G-code",".gcode"),("NC",".nc"),("All","*.*")))
		#fileName = fd.askopenfilename(filetypes = (("G-code",".gcode"),("NC",".nc"),("All","*.*")))
		print(fileName)
		return fileName
		print(fileName + "ok")
		
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
		global comPort
		comPort = com 
		global baudRate
		baudRate = baud
		global timeOut
		timeOut = tOut
	def streamFile(self, File ,textBox,comPort1,baudRate1):
		global lineCount
		global gcodeCount
		#print("i Work For now L35"+ File)
		s = serial.Serial(comPort1,baudRate1,timeout = 0)
		s.write(b'\r\n\r\n')
		time.sleep(2)
		s.flushInput()
		verbose = True
		print(File)
		with open(File,'br') as f:
			print("i Work For now L39")
			for line in f:
				lineCount += 1
				lineBlock =line.strip()
				charline.append(len(lineBlock) + 1)
				grblOut = ''
				while sum(charline) >= grblBufferSize - 1 |  s.inWaiting() :
					
					out_temp = s.readline().strip()
					#print("i Work For now L39"+out_temp.decode("utf-8"))
					if out_temp.find(b'ok') < 0 and out_temp.find(b'error') < 0 :
						textBox.insert('1.0',"Debug:"+out_temp.decode("utf-8")+'\n')
						print("Debug:"+out_temp.decode("utf-8"))
					else:
						grblOut += out_temp.decode("utf-8")
						gcodeCount += 1
						grblOut += str(gcodeCount)
						del charline[0]
				if verbose:
					textBox.insert('1.0',"SND: " + str(lineCount) + " : " + lineBlock.decode("utf-8")+'\n')
					print( "SND: " + str(lineCount) + " : " + lineBlock.decode("utf-8"),)
					newl =b'\n'
					s.write(lineBlock+newl) # Send g-code block to grbl
				if verbose : 
					textBox.insert('1.0',"BUF:",str(sum(charline)),"REC:",grblOut+'\n')
					print ("BUF:",str(sum(charline)),"REC:",grblOut)
		time.sleep(2)
		
		#f.close()
		s.close()