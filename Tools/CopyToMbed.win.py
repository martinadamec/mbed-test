#!/usr/bin/env python

import sys, getopt, time, shutil
import serial

class ArgumentsException(Exception): pass

class CopyTomMbed:

	# Parameters
	file = None
	target = None
	port = None

	def __init__(self, args):
		# Dont exist arguments
		if len(args) == 0: 
			raise ArgumentsException("Required arguments are 'f', 't', 'p'.")

		# Get arguments
		optlist, args = getopt.getopt(args, 'f:t:p:')

		# Still have arguments
		if len(args) > 0: 
			raise ArgumentsException("Possible arguments are 'f', 't', 'p'.")

		# Projdeme ziskane argumenty
		for key, val in optlist:
			# Filename
			if key == '-f': 
				self.file = val
			# Target
			if key == '-t': 
				self.target = val
			# Port
			if key == '-p': 
				self.port = val


	def sendBreak(self, ser):
		ser.send_break()


	def restartMbed(self):
		ser = self.getSerial()
		ser.isOpen()
		self.sendBreak(ser)

	def getSerial(self):
		return serial.Serial(
			port = '\\.\\' + self.port,
			baudrate = 9600,
			parity = serial.PARITY_NONE,
			stopbits = serial.STOPBITS_ONE,
			bytesize = serial.SEVENBITS
		)

	def copy(self):
		shutil.copy(self.file, self.target)
		time.sleep(2) # Delay for finish copy


inst = CopyTomMbed(sys.argv[1:])
inst.copy()
inst.restartMbed()