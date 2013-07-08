'''
Created on 24-03-2013

@author: Olek
'''

class Configuration():
    #TODO: Cleanup configuration
    minNumberToStartMatrixCreation = 3
    
    subMatrixSize = 201  # assumed that single cell is 1 x 1 meter
    matrixSize    = 301 # assumed that single cell is 1 x 1 meter
    
    # TODO: Remove fake mechanism
    fakePositionMin = 20
    fakePositionMax = 60
    
    nodesIdToBeCreated = [i for i in range(1, 3 + 1)] # Range do not include last element
    
if __name__ == "__main__":
    pass