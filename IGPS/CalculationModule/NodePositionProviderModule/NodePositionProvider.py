'''
Created on 02-07-2013

@author: Olek
'''
import random
from DataModels import NodePositionRecord as NPR
from ConfigurationModule import Configuration as C

class NodePositionProvider():

    def __init__(self):
        pass
        
    def GetCurrentPosition(self):
        #TODO: Implement
        pMin = C.Configuration.fakePositionMin
        pMax = C.Configuration.fakePositionMax
        return NPR.NodePositionRecord(x = random.randint(pMin, pMax),
                                      y = random.randint(pMin, pMax),
                                      z = 0)

if __name__ == "__main__":
    pass