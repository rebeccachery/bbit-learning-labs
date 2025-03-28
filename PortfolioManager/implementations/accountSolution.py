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
from interfaces.accountInterface import accountInterface
from typing import Any, Dict, Set, Iterable
class account(accountInterface):
    def __init__(self, positions, accountName):
        self.accountName = accountName
        self.positions = dict()
        for i in positions:
            self.positions[i.getSecurity().getName()] = i

    def getName(self):
        return self.accountName

    def getAllPositions(self):
        return self.positions

    def getPositions(self, securities):
        d = dict()
        for i in securities:
            # if i not in :
            #     continue
            d[i] = self.positions[i]
        return d

    def addPositions(self, positions):
        #self.positions.add()
        pass

    def removePositions(self, securities):
        pass
        
