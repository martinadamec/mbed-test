#!/usr/bin/env python

import sys, getopt, time, shutil
import serial
import serial.tools.list_ports

class ArgumentsException(Exception): pass
class DetectPortException(Exception): pass

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
		optlist, args = getopt.getopt(args, 'f:t:p')

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

		if self.port is None:
			self.port = self.autoDetectPort()


	def sendBreak(self, ser):
		ser.sendBreak()


	def restartMbed(self):
		ser = self.getSerial()
		ser.isOpen()
		self.sendBreak(ser)

	def getSerial(self):
		return serial.Serial(
			port = self.getPort(),
			baudrate = 9600,
			parity = serial.PARITY_NONE,
			stopbits = serial.STOPBITS_ONE,
			bytesize = serial.SEVENBITS
		)

	def getPort(self):
		return '\\.\\' + self.port if sys.platform.startswith('win') else self.port

	def copy(self):
		shutil.copy(self.file, self.target)
		time.sleep(2) # Delay for finish copy

	def autoDetectPort(self):
		# Get list of port with keyword "mbed"
		ports = list(serial.tools.list_ports.grep('mbed'))

		# No port
		if len(ports) == 0:
			raise DetectPortException("Not possible auto-detect mbed port.")

		port = ports[0]
		print 'Auto detect port: %s' % str(port)

		# Get the first one
		return port[0]

if __name__ == '__main__':
	inst = CopyTomMbed(sys.argv[1:])
	inst.copy()
	inst.restartMbed()