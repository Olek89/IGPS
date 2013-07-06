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
        from DataModels import Matrix as M
        subMatrix = M.Matrix(3)
        subMatrix.data[1][2] = 1
        subMatrix.data[0][2] = 1
        subMatrix.data[2][2] = 1
        subMatrix.data[1][0] = 1
        subMatrix.data[1][1] = 1
        subMatrix.data[1][2] = 1
        #subMatrix = self.subMatrixGenerator.ActualGenerateSubMatix(radius)
        return subMatrix