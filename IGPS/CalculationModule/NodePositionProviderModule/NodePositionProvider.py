'''
Created on 02-07-2013

@author: Olek
'''
import random
from DataModels import NodePositionRecord as NPR
from ConfigurationModule import Configuration as C

class NodePositionProvider():

    def __init__(self, nodeId):
        self.nodeId = nodeId
        
    def GetCurrentPosition(self):
        #TODO: Implement
        if self.nodeId == 1:
            # r = 70
            x = 50
            y = 10
        elif self.nodeId == 2:
            # r = 60
            x = 0
            y = 0
        elif self.nodeId == 3:
            # r = 110
            x = 30
            y = -30
        else:
            pMin = C.Configuration.fakePositionMin
            pMax = C.Configuration.fakePositionMax
            x = random.randint(pMin, pMax)
            y = random.randint(pMin, pMax)
        
        return NPR.NodePositionRecord(x = x, y = y, z = 0)

if __name__ == "__main__":
    pass