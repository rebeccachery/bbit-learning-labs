#Uncomment line above & run cell to save solution
#TODO Define class that implements positionInterface & allows for the management of a position
import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from interfaces.positionInterface import positionInterface
class position(positionInterface):
    def __init__(self, security, initialPosition):
        super().__init__(security, initialPosition)
        self.security = security
        self.initialPosition = initialPosition

    def getSecurity(self):
        return self.security

    def setPosition(self, inputValue):
        self.security = inputValue

    def addPosition(self, inputValue):
        self.security += inputValue
        
