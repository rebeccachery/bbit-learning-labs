#Uncomment line above & run cell to save solution
#TODO Define class that implements positionInterface & allows for the management of a position
import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from implementations.securitySolution import security
from interfaces.positionInterface import positionInterface
from interfaces.securityInterface import securityInterface
class position(positionInterface):
    def __init__(self, securityInput, initialPosition):
        super().__init__(security, initialPosition)
        self.initialPosition = initialPosition
        if isinstance(securityInput, securityInterface):
          self.securityInput = securityInput
        else:
          self.securityInput = security(securityInput)  

    def getSecurity(self):
        return self.securityInput

    def getPosition(self):
        return self.initialPosition

    def setPosition(self, inputValue):
        if inputValue < 0:
            raise Exception("Value results in a short position")
        self.initialPosition = inputValue

    def addPosition(self, inputValue):
        if self.initialPosition + inputValue < 0:
            raise Exception("Value results in a short position")
        self.initialPosition += inputValue
        
