'''
Created on 03-07-2013

@author: Olek
'''
from DataModels import Matrix as M
from ConfigurationModule import Configuration as C

class HomeNodeDbBeaconPositionRecord():
    currentId = 0
    
    def __init__(self, messageHeader):
        self.recordId = self.currentId
        self.currentId += 1
        
        self.messageHeader         = messageHeader
        self.positionMatrix        = M.Matrix(C.Configuration.matrixSize)
    
    def __str__(self):
        return "{0}\n{1}".format(self.messageHeader, self.positionMatrix)

if __name__ == "__main__":
    pass