'''
Created on 28-06-2013

@author: Olek
'''
from Common.Tools import Callable
from Common.Tools.Zeros import Zeros
from math import  pi, sin, cos

class _GenerateSubMatrixHelpers():

    def __Elipse(x, y, a, b, angle = 0, steps = 1000):  # @NoSelf
        '''Return list of X, Y tuples.'''
        X = Zeros(steps);
        Y = Zeros(steps);
        #Angle is given by Degree Value
        beta = -angle * (pi / 180); #Radian rotation
    
        for i in range(steps):
            alpha = float(i * (2*pi / steps)) ; #(360 / steps) * (pi / 180)
            X[i] = int(x + (a * cos(alpha) * cos(beta) - b * sin(alpha) * sin(beta)));
            Y[i] = int(y + (a * cos(alpha) * sin(beta) + b * sin(alpha) * cos(beta)));
        return [(X[i], Y[i]) for i in range(steps)]
    
    _Elipse = Callable.Callable(__Elipse)
    
    def __Circle(x, y, r, steps = 500):  # @NoSelf
        '''Returns circle X, Y tuples with limited 90 degree error'''
        return (_GenerateSubMatrixHelpers._Elipse(x, y, r, r, angle = 0, steps = steps))
    
    _Circle = Callable.Callable(__Circle)

if __name__ == "__main__":
    pass