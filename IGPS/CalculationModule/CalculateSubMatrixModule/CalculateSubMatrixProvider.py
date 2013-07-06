'''
Created on 20-03-2013

@author: Olek
'''
from CalculateRadius import CalculateRadius
from ConfigurationModule import Configuration as C
from _GenerateSubMatrix import _GenerateSubMatrix

class CalculateSubMatrixProvider():
    
    def __init__(self):
        self.radiusCalculateUnit = CalculateRadius()
        self.subMatrixGenerator = _GenerateSubMatrix()
    
    def CalculateSubMatrix(self, beaconTimeStamp, receivingTime):
        if C.Configuration.useFakeCalculationModule == True:
            subMatrix = self.FAKE()
        else:
            radius = self.radiusCalculateUnit.CalculateRadiusBasedOnDelay(beaconTimeStamp, receivingTime)
            subMatrix = self.subMatrixGenerator.ActualGenerateSubMatix(radius)
        return subMatrix
    
    def FAKE(self):
        from DataModels import Matrix as M
        size = C.Configuration.fakeSize
        subMatrix = M.Matrix(size)
        for i in range(size):
            for j in range(size):
                subMatrix.data[i][j] = 1
        return subMatrix
    
if __name__ == "__main__":
    pass