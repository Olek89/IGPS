'''
Created on 20-03-2013

@author: Olek
'''
import CalculateSubMatrixProvider as CSMP

class CalculateSubMatrixController():
    
    def __init__(self):
        self.subMatrixProvider = CSMP.CalculateSubMatrixProvider()
    
    def CalculateSubMatrix(self, record):
        startTime = record.messageHeader.beaconTimeStamp
        endTime = record.receivingTime
        subMatrix = self.subMatrixProvider.CalculateSubMatrix(startTime, endTime) #TODO: quality
        return subMatrix
    
if __name__ == "__main__":
    pass