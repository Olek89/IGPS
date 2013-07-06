'''
Created on 02-07-2013

@author: Olek
'''

class NodePositionRecord():

    def __init__(self, x, y, z):
        self.X = int(x)
        self.Y = int(y)
        self.Z = int(z)
        
    def __str__(self):
        return "Node position X: {0}, Y: {1}, Z: {2}".format(self.X, self.Y, self.Z)

if __name__ == "__main__":
    pass