'''
Created on 20-03-2013

@author: Olek
'''
from CalculateRadius import CalculateRadius
from _GenerateSubMatrix import _GenerateSubMatrix

class CalculateSubMatrixProvider():
    
    def __init__(self):
        self.radiusCalculateUnit = CalculateRadius()
        self.subMatrixGenerator = _GenerateSubMatrix()
    
    def CalculateSubMatrix(self, beaconTimeStamp, receivingTime):
        radius = self.radiusCalculateUnit.CalculateRadiusBasedOnDelay(beaconTimeStamp, receivingTime)
        # TODO: Turn on real submatrix generation
        subMatrix = self.FAKE()
#         subMatrix = self.subMatrixGenerator.ActualGenerateSubMatix(radius)
        return subMatrix
    
    def FAKE(self):
        from DataModels import Matrix as M
        size = 9
        subMatrix = M.Matrix(size)
        for i in range(size):
            for j in range(size):
                subMatrix.data[i][j] = 1
        return subMatrix