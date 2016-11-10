#!/usr/bin/env python

import sys
from CopyToMbed import CopyToMbed

inst = CopyToMbed(sys.argv[1:])
inst.copy(True)
