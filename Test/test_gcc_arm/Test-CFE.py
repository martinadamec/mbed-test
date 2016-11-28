#!/usr/bin/env python

import time, sys, inspect, os

path = os.path.dirname(inspect.getfile(inspect.currentframe()))
sys.path.insert(1, os.path.join(path, '..', '..', 'Tools'))
sys.path.extend([os.path.join(path, '..', '..', 'CFE_Injector')])

from main.main import injectInterJump
from CopyToMbed import CopyToMbed
from GetDisasmGroup import GetDisasmGroup


# Copy file to target adn restart
inst = CopyToMbed(sys.argv[1:])
testFilename = inst.copy(True)
time.sleep(1)

try:
	filename = os.path.join(path, '..', '..', 'test_gcc_arm', 'test_gcc_arm.disasm')
	testDisasm_filename = os.path.join(path, 'test_gcc_arm.disasm')

	# Reduce to main
	GetDisasmGroup(filename, 'main', testDisasm_filename)

	# Run test
	injectInterJump(testDisasm_filename)
except Exception as e:
	raise # re-raise the error
finally:
	try:
	    os.remove(testDisasm_filename)
	    os.remove(testFilename)
	    inst.restartMbed()
	except OSError:
		pass
