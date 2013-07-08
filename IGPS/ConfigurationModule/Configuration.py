'''
Created on 24-03-2013

@author: Olek
'''

class Configuration():
    #TODO: Cleanup configuration
    minNumberToStartMatrixCreation = 3
    
    subMatrixSize = 251 # assumed that subMatrix is always smaller then concatenation
    matrixSize    = 301
    
    # TODO: Remove fake mechanism
    fakePositionMin = 20
    fakePositionMax = 60
    
    nodesIdToBeCreated = [i for i in range(1, 3 + 1)] # Range do not include last element
    
if __name__ == "__main__":
    pass