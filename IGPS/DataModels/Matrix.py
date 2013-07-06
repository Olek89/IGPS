'''
Created on 24-03-2013

@author: Olek
'''
from Common.Tools import Zeros as Z

class Matrix():

    def __init__(self, size):
        self.data = Z.Zeros(size, size)
        
    def __str__(self):
        #rotated = zip(*self.data[::-1])
        rotated_ccw = zip(*self.data)[::-1]
        result = ""
        for row in rotated_ccw:
            result += " ".join(str(x) for x in row)
            result += "\n";
        return result[:-1]
            
    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    pass