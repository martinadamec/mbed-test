__author__ = 'Jens Vankeirsbilck'


import logging
from faultInjection.PC_injector import PCinjector
from faultInjection.cfeInjector import CFEInjector

logging.basicConfig(level=logging.DEBUG)

def testReadPC():
    inj = PCinjector()
    PC = inj.readPC()
    logging.log(25,"PC is: 0x%X" %PC)

def injectInterJump(disassemblyName,skip='0'):
    inj = CFEInjector(disassemblyName,skip)
    inj.injectInterBlockWithErrorCheck()

def suite(nameSheet, numberOfCFEs,disassemblyName,xmlName,skip='0'):
    inj = CFEInjector(disassemblyName,skip)
    inj.injectionSuiteInterBlock(numberOfCFEs,nameSheet)
    inj.XMLCreation(disassemblyName,xmlName,skip)

def debug(disassemblyName,skip='0'):
    inj = CFEInjector(disassemblyName,skip)
    inj.pcInjector.target.halt()
    r11 = inj.pcInjector.target.readCoreRegister('r11')
    r12 = inj.pcInjector.target.readCoreRegister('r12')
    print "r11 = 0x{:X}; r12 = 0x{:X}\n".format(r11,r12)

def batches(numberOfBatches, numberOfCFEs,disassemblyName,skip='0'):
    inj = CFEInjector(disassemblyName,skip)
    inj.injectionBatchesInterBlock(numberOfBatches,numberOfCFEs)

def randomCFEs(numberOfCFEs, nameSheet, disassamblyName):
    inj = CFEInjector(disassamblyName)
    inj.randomCfeSuite(numberOfCFEs, nameSheet)

def deterministicCFEs(nrIntra, nrInter, nrOutFunction, disassamblyName,xmlCrea):
    inj = CFEInjector(disassamblyName, createXml=xmlCrea)
    inj.deterministicCFEsuite(nrIntra, nrInter, nrOutFunction)