__author__ = 'Jens Vankeirsbilck'


import logging
logging.basicConfig(level=25)
from faultInjection.registerFaultInjector import RegisterFaultInjector
from faultInjection.instructionAwareFI import InstructionAwareFI
from faultInjection.memoryFaultInjector import MemoryFaultInjector
from faultInjection.specialRegisterFaultInjector import SpecialRegisterFaultInjector
from faultInjection.mmio.ethernetFaultInjector import EthernetFaultInjector
from faultInjection.randomDfeInjection import RandomDFE

from faultInjection.WetenschapsDag import RobotFI


# Starts the suite that injects tries faults into registers
# looping over all 32 bit possibilities
def injectRegisterSuite(tries, nameWorkSheet):
    inj = RegisterFaultInjector()
    logging.debug("Starting the injectionSuite")
    inj.injectionSuite(tries, nameWorkSheet)
    inj.unInit()

def reset():
    inj = RegisterFaultInjector()
    inj.resetDevice()
    inj.unInit()

def instrAwareFI(bitPos):
    inj = InstructionAwareFI()
    inj.injectInstructionAware(bitPos)
    inj.unInit()

def injSuite(nameSheet, tries):
    inj = InstructionAwareFI()
    inj.injectionSuite(tries, nameSheet)
    inj.unInit()

def randomSuite(nameSheet, nrOfFaults):
    inj = RandomDFE()
    inj.injectionSuite(nrOfFaults, nameSheet)
    inj.unInit()

def deterDFE(nameSheet, nrOfDFE):
    inj= InstructionAwareFI()
    inj.injectionSuiteDeterDFE(nrOfDFE, nameSheet)
    inj.unInit()

def readMem(address):
    inj = MemoryFaultInjector()
    inj._readMemLoc(address)
    inj.target.reset()

def detPC():
    inj = RegisterFaultInjector()
    inj.target.halt()
    lr = inj.target.readCoreRegister('lr')
    print "LR: 0x%X" % lr
    bit2 = (lr >> 2) & 1
    if(bit2 == 0):
        print "Reading MSP"
        sp = inj.target.readCoreRegister('msp')
        print "sp: 0x%X" %sp
    else:
        print "Reading PSP"
        sp = inj.target.readCoreRegister('psp')
    for i in range(0,28,4):
        stack = inj.target.readMemory(sp+i)
        print "StackValue: 0x%X" %stack

def testInjectMWTD():
    inj = EthernetFaultInjector()
    inj.injectMWTD()

def testInjectInPacketTx():
    inj = EthernetFaultInjector()
    inj.injectInPacketTx()

def testInjectInPacketRx():
    inj = EthernetFaultInjector()
    inj.injectInPacketRx()