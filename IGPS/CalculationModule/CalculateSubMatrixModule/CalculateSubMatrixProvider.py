'''
Created on 20-03-2013

@author: Olek
'''
from CalculateRadius import CalculateRadius
from ConfigurationModule import SubMatrixCalculationConfiguration as SMCC
from _GenerateSubMatrix import _GenerateSubMatrix

class CalculateSubMatrixProvider():
    
    def __init__(self):
        self.radiusCalculateUnit = CalculateRadius()
        self.subMatrixGenerator = _GenerateSubMatrix()
    
    def CalculateSubMatrix(self, beaconTimeStamp, receivingTime):
        if SMCC.SubMatrixCalculationConfiguration.useFakeCalculationModule == True:
            subMatrix = self.FAKE()
        else:
            radius = self.radiusCalculateUnit.CalculateRadiusBasedOnDelay(beaconTimeStamp, receivingTime)
            subMatrix = self.subMatrixGenerator.ActualGenerateSubMatix(radius)
        return subMatrix
    
    def FAKE(self):
        from DataModels import Matrix as M
        size = SMCC.SubMatrixCalculationConfiguration.fakeSize
        subMatrix = M.Matrix(size)
        for i in range(size):
            for j in range(size):
                subMatrix.data[i][j] = 1
        return subMatrix
    
if __name__ == "__main__":
    pass