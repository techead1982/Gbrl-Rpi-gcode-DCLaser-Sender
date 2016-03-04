import serial
import re
import time
import sys
import argparse 
from tkinter import *

class LaserCom():
	comPort = 'COM3'
	baudRate = 115200
	timeOut = 1
	fileName = ''
	lineCount = 0
	gcodeCount = 0
	charline = []
	def getFileInfo(self):
		print("HI")
	def setSerial(com,baud,tOut):
		comPort = com
		baudRate = baud
		timeOut = tOut
	def streamFile(File):
		s = serial.Serial(comPort,baudRate,timeOut)
		s.write("\r\n\r\n")
		f = open(File,'r')