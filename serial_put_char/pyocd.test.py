from pyOCD.board import MbedBoard
import time
import sys

import logging
#logging.basicConfig(level=logging.INFO)

class TestCore:

	# Board
	board = None
	initSleepTime = 0

	def __init__(self, board = None):
		if board is None:
			self.chooseBoard()

	def chooseBoard(self):
		self.board = MbedBoard.chooseBoard()

	def getTarget(self):
		return self.board.target

	def getFlash(self):
		return self.board.flash

	def runTests(self):
		raise NotImplementedError("Method 'runTests' must be implemented!")

	def clean(self):
		self.board.uninit()

	def initSleep(self):
		time.sleep(self.initSleepTime)


class BlinkyTest(TestCore):

	initSleepTime = 2

	# Adress to memory of each led
	addresses = {
		1: 0x2009C034,
		2: 0x2009C034,
		3: 0x2009C034,
		4: 0x2009C034,
	}

	# Mask for detecting if led is ON
	masks = {
		1: 0x00040000, # 18-bit
		2: 0x00100000, # 20-bit
		3: 0x00200000, # 21-bit
		4: 0x00800000, # 23-bit
	}

	def isLedOn(self, target, led):
		address = self.addresses[led]
		mask = self.masks[led]
		num = target.readMemory(address);
		return num & mask > 0

	def runTests(self, cleanAfter = True):
		self.runTest_1()

		# Clean
		if cleanAfter:
			self.clean()

	def runTest_1(self):
		target = self.getTarget()

		# Reset
		target.reset()
		self.initSleep()

		for i in range(0, 30):
			time.sleep(0.6)
			target.halt()
			for i in range(1, 5):
				print "led %d: %s" % (i, 'ON' if self.isLedOn(target, i) else 'OFF')
			print "---\n\r"
			sys.stdout.flush()
			target.resume()

test = BlinkyTest()
test.runTests(False)
