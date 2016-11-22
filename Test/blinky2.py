#!/usr/bin/env python

import time, sys, inspect, os

path = os.path.dirname(inspect.getfile(inspect.currentframe()))
sys.path.insert(1, os.path.join(path, '..', 'Tools'))
sys.path.extend([os.path.join(path, '..', 'CFE_Injector')])

from main.main import injectInterJump
from CopyToMbed import CopyToMbed
from SendEmail import SendEmail

class BlinkyEmail(SendEmail):

	send_from = "martin.adamec@student.kuleuven.be"

	def addFiles(self, msg):
		self.addXlsxFile(msg, "resultsDeterDFE.xlsx", os.path.join(path, "..", "resultsDeterDFE.xlsx"))


# Copy file to target adn restart
"""
inst = CopyToMbed(sys.argv[1:])
testFilename = inst.copy(True)
time.sleep(1)
"""

try:
	injectInterJump(os.path.join(path, '..', 'test_gcc_arm', 'test_gcc_arm.disasm'))
	#deterDFE("Test", 1)
	"""
	mail = BlinkyEmail("Deter DFE test", "The result in XLSX file.")
	mail.send("martin.adamec@student.kuleuven.be")
	"""
except Exception as e:
	raise # re-raise the error
"""
finally:
	try:
	    os.remove(testFilename)
	    inst.restartMbed()
	except OSError:
		pass
"""
