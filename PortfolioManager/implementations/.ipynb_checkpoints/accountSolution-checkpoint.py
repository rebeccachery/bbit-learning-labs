#Uncomment line above & run cell to save solution
#TODO Define class that implements accountInterface & allows for the management of an account
import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from implementations.securitySolution import security
from implementations.positionSolution import position
from interfaces.positionInterface import positionInterface
from typing import Any, Dict, Set, Iterable
class account(accountInterface):
    def __init__(self, positions, accountName):
        self.accountName = accountName
        self.positions = set()

    def getName(self):
        return self.accountName

    def getAllPositions(self):
        return iter(self.positions)

    def getPositions(self, securities):
        pass

    def addPositions(self, positions):
        pass

    def removePositions(self, securities):
        pass
        
