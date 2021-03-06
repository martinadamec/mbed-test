__author__ = 'Jens Vankeirsbilck'

from pyOCD.board import MbedBoard
import logging
import time
import random

class RobotFI:
    def __init__(self, board=None):
        self.flagGrabAddress = 0x10005000
        self.flagPosAddress = 0x10005004
        self.prevPosAddress = 0x10005008
        self.waitTimeAddress = 0x10005024
        if board is None:
            try:
                self.board = self._initialize()
                self.target = self.board.target
            except Exception as e:
                logging.error("could not init RobotFI\n%s" % e)
        else:
            self.board = board
            self.target = self.board.target

    def unInit(self):
        if self.board != None:
            logging.info("Board uninitialised")
            self.board.uninit()

    def changePrevPos(self):
        try:
            self.target.halt()
            flagPos = 0
            while flagPos != 1:
                logging.debug("flagPos was 0, trying again")
                self.target.resume()
                time.sleep(5)
                self.target.halt()
                flagPos = self.target.readMemory(self.flagPosAddress)
                logging.debug("Read flagPos at address 0x{:X} was: 0x{:X}".format(self.flagPosAddress, flagPos))
            prevPos = self.target.readMemory(self.prevPosAddress)
            logging.debug("prevPos is: 0x%X" % prevPos)
            prevPos += 1
            prevPos %= 5
            self.target.writeMemory(self.prevPosAddress, prevPos)
            logging.info("Wrote %s as new prevPos value" % prevPos)
        except Exception as e:
            logging.error("Could not change prevPos!\n%s" % e)
        finally:
            self.target.resume()

    def changeWaitTime(self):
        newTime = random.randrange(4, 1000)
        try:
            self.target.halt()
            oldTime = self.target.readMemory(self.waitTimeAddress)
            self.target.writeMemory(self.waitTimeAddress, newTime)
            logging.debug("waitTime was {:X}, written {:d}".format(oldTime,newTime))
            cur = self.target.readMemory(self.waitTimeAddress)
            logging.info("Waittime cur: 0x{0:X} or {0:d}".format(cur))
        except Exception as e:
            logging.error("Could not change Wait time!\n%s" % e)
        finally:
            self.target.resume()

    # private functions
    def _initialize(self):
        """
            Initialize mbed
        :return: board encapsulating the mbed
        """
        board = None
        try:
            # Search and initialize mbed
            board = MbedBoard.chooseBoard()

            # Confirm LPC1768
            if board.getTargetType() == "lpc1768":
                logging.debug("Target type mbed lpc1768 found")
            else:
                raise Exception("Only NXP LPC1768 supported")
        finally:
            if board is not None:
                return board