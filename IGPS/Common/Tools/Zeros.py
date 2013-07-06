'''
Created on 24-03-2013

@author: Olek
'''

def Zeros(*args):
    '''Making matrix of zeros of any shape. 
    Based on Stanford materials.
    Example use: Zeros(3,2,4)'''
    if len (args) == 0: return 0
    car = args[0]
    cdr = args[1:]
    return [Zeros(*cdr) for i in range(car)]
        
if __name__ == "__main__":
    pass