'''
Created on 24-03-2013

@author: Olek
'''

def Zeros(*args):
    '''Making matrix of zeros of any shape. 
    Based on Stanford materials.
    Example use: Zeros(3,2,1)
    Produce r = [[[0], [0]], [[0], [0]], [[0], [0]]]'''
    if len (args) == 0: return 0
    currentArray = args[0]
    innerA = args[1:]
    return [Zeros(*innerA) for i in range(currentArray)]
        
if __name__ == "__main__":
    pass