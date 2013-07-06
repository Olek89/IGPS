'''
Created on 04-05-2013

@author: Olek
'''

class NodePositionProvider():
    # TODO: Add dynamic position change
    def __init__(self, nodeId):
        # Temporary solution
        self.x = 5 * nodeId
        self.y = 2 * nodeId
        self.z = 0

if __name__ == "__main__":
    pass