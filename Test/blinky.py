#!/usr/bin/env python

import time, sys, inspect, os

path = os.path.dirname(inspect.getfile(inspect.currentframe()))
sys.path.insert(1, os.path.join(path, '..', 'Tools'))
sys.path.extend([os.path.join(path, '..', 'DFE_Injector')])

from main.main import deterDFE
from CopyToMbed import CopyToMbed



# Copy file to target adn restart
inst = CopyToMbed(sys.argv[1:])
testFilename = inst.copy(True)
time.sleep(1)

try:
	deterDFE("Test", 1)
except Exception as e:
	raise # re-raise the error
finally:
	try:
	    os.remove(testFilename)
	    inst.restartMbed()
	except OSError:
		pass