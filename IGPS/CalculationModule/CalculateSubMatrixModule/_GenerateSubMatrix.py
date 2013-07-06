'''
Created on 21-03-2013

@author: Olek
'''
import logging
from DataModels import Matrix as M
from ConfigurationModule import Configuration as C
from ConfigurationModule import SubMatrixCalculationConfiguration as SMCC
from _GenerateSubMatrixHelpers import _GenerateSubMatrixHelpers

class _GenerateSubMatrix(object):
    size = C.Configuration.subMatrixSize
    center = size/2 + 1
    
    def ActualGenerateSubMatix(self, radius): #TODO: Quality as parameter
        #TODO: Improve implementation
        logging.debug("Will now generate subMatrix for radius: {0}".format(radius))
        if radius <= SMCC.SubMatrixCalculationConfiguration.minRadius: # TODO: top limitation to match matrix size
            raise Exception("Given radius {0} must be higher then {1}.".format(radius, SMCC.SubMatrixCalculationConfiguration.minRadius))
        
        subMatrix = M.Matrix(self.size)
        
        #TODO: Probability and distribution based on quality
        start = radius - SMCC.SubMatrixCalculationConfiguration.halfDistributionWidth
        stop  = radius + SMCC.SubMatrixCalculationConfiguration.halfDistributionWidth + 1 # TODO: Change range workaround
        radiuses = range(start, stop, 1)#(2*halfWidth)//len(probabilityDistribution))#TODO: Calculate step!
        
        for i in range(len(radiuses)):
            defaultShape = _GenerateSubMatrixHelpers._Circle(self.center, self.center, radiuses[i])
            for x,y in defaultShape:
                subMatrix.data[x][y] += SMCC.SubMatrixCalculationConfiguration.probabilityDistribution[i]
        logging.info("Sub-matrix done for radius: {}".format(radius))
        return subMatrix