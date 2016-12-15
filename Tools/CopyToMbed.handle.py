#!/usr/bin/env python

import sys, os
from CopyToMbed import CopyToMbed

print os.getcwd()

inst = CopyToMbed(sys.argv[1:])
inst.copy(True)
