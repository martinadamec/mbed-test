#!/usr/bin/env python

import sys, os
sys.path.extend([os.path.join('..', 'DFE_Injector')])
from main.main import deterDFE

deterDFE("Test", 1)