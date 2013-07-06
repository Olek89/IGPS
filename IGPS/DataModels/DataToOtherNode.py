'''
Created on 18-05-2013

@author: Olek
'''

class DataToOtherNode():

    def __init__(self, sendingNodeId, messageHeader):
        self.sendingNodeId = sendingNodeId
        self.messageHeader = messageHeader
    
    def GetCommonMessageList(self):
        data = []
        data.append(self.sendingNodeId)
        data.append(self.messageHeader.homeNodeId)
        data.append(self.messageHeader.beaconId)
        data.append(self.messageHeader.beaconTimeStamp)
        return data
    
    def GetSubMatrixMessageList(self, subMatrixX, subMatrixY, subMatrixZ, subMatrixValue):
        data = self.GetCommonMessageList()
        data.append(subMatrixX)
        data.append(subMatrixY)
        data.append(subMatrixZ)
        data.append(subMatrixValue)
        return data
    
    def GetNodePossitionMessageList(self, otherNodePositionX, otherNodePositionY, otherNodePositionZ):
        data = self.GetCommonMessageList()
        data.append(otherNodePositionX)
        data.append(otherNodePositionY)
        data.append(otherNodePositionZ)
        return data

if __name__ == "__main__":
    pass