'''
Created on 05-05-2013

@author: Olek
'''
import MessageHeader as MH
from DataModels import NodePositionRecord as NPR

class DataFromOtherNode():
    '''Defines all data possible from other nodes.'''
    def __init__(self, data, isSubMatrixPart = False, isNodePosition = False):
        '''Creates message header.'''
        if    isSubMatrixPart == False and isNodePosition == False and len(data) == 4: pass
        elif  isSubMatrixPart == True  and isNodePosition == False and len(data) == 8: pass
        elif  isSubMatrixPart == False and isNodePosition == True  and len(data) == 7: pass
        else: raise Exception("Could not set fields due to improper configuration.")
        
        sendingNodeId   = int(data[0])
        homeNodeId      = int(data[1])
        beaconId        = int(data[2])
        beaconTimeStamp = data[3] # TODO: Use TIC instead string
        
        self.sendingNodeId = int(sendingNodeId)
        self.messageHeader = MH.MessageHeader(homeNodeId, beaconId, beaconTimeStamp)
        
        # SubMatrix
        self.subMatrixX = int(data[4]) if isSubMatrixPart else None
        self.subMatrixY = int(data[5]) if isSubMatrixPart else None
        self.subMatrixZ = int(data[6]) if isSubMatrixPart else None
        self.subMatrixValue = int(data[7]) if isSubMatrixPart else None
        
        # Foreign Node Position
        otherNodePositionX = data[4] if isNodePosition else 0
        otherNodePositionY = data[5] if isNodePosition else 0
        otherNodePositionZ = data[6] if isNodePosition else 0
        self.otherNodePosition = NPR.NodePositionRecord(x = otherNodePositionX,
                                                        y = otherNodePositionY,
                                                        z = otherNodePositionZ)

if __name__ == "__main__":
    pass