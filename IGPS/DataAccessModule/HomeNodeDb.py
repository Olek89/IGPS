'''
Created on 24-03-2013

@author: Olek
'''
import logging
from DataModels import HomeNodeDbRecord as HNDR
from DataModels import HomeNodeDbBeaconPositionRecord as HNDBPR
from Common import NodeStatesEnumerator as NSE

class HomeNodeDb():
    
    def __init__(self):
        self._recordList = []
        self._beaconPositionList = []
         
    def RegisterNewSignalReceivedAtNode(self, messageHeader, nodeId):
        newRecord = HNDR.HomeNodeDbRecord(messageHeader, nodeId)
        if newRecord in self._recordList:
            raise Exception("Record already created.")
        self._recordList.append(newRecord)
        
    def GetNodesListForSpecificBeaconMessageIdentity(self, messageHeader, inState = None):
        '''Return nodes for which messageHeaderMatch. When inState is given it also has to match'''
        matched = []
        for record in self._recordList:
            if record.messageHeader == messageHeader: 
                if record.receivingNodeStatus == inState or inState == None:
                    matched.append(record.receivingNodeId)
        return matched
    
    def ChangeStateOfNodeForSpecificBeaconMessageIdentity(self, messageHeader, nodeId, newState):
        anyWasChanged = False
        for record in self._recordList:
            if record.messageHeader == messageHeader: 
                if record.receivingNodeId == nodeId:
                    previous = record.receivingNodeStatus
                    record.receivingNodeStatus = newState
                    logging.debug("Record: {0} was at state {1}".format(record, previous))
                    anyWasChanged = True
        if anyWasChanged == False:
            raise Exception("Nothing to change.")
        
        
    def AddValueToSubMatrixCell(self, messageHeader, nodeId, x, y, z, value):
        anyWasChanged = False
        for record in self._recordList:
            if record.messageHeader == messageHeader: 
                if record.receivingNodeId == nodeId:
                    #TODO: Add z coordinate when 3D support is added
                    record.calculatedSubMatrix.data[x][y] += value
                    anyWasChanged = True
        if anyWasChanged == False:
            raise Exception("Nothing to change.")
        
    def SetReceivingNodePosition(self, messageHeader, nodeId, position):
        anyWasChanged = False
        for record in self._recordList:
            if record.messageHeader == messageHeader: 
                if record.receivingNodeId == nodeId:
                    record.receivingNodePosition = position
                    record.receivingNodeStatus   = NSE.NodeStatesEnumerator.POSRECEIVED
                    anyWasChanged = True
        if anyWasChanged == False:
            raise Exception("Nothing to change.")
        
    def GetRecordForMessageHeaderAndNodeId(self, messageHeader, nodeId):
        for record in self._recordList:
            if record.messageHeader == messageHeader: 
                if record.receivingNodeId == nodeId:
                    return record
        raise Exception("No record for given header and node ID.")
    
    #===========================================================================
    # Final data
    #===========================================================================
    def GetBeaconPositionMatrix(self, messageHeader):
        for record in self._beaconPositionList:
            if record.messageHeader == messageHeader: 
                return record.positionMatrix
        # Not yet created
        positionRecord = HNDBPR.HomeNodeDbBeaconPositionRecord(messageHeader = messageHeader)
        self._beaconPositionList.append(positionRecord)
        return positionRecord.positionMatrix
    
    def UpdateBeaconPositionMatrix(self, messageHeader, matrix):
        anyWasChanged = False
        for record in self._beaconPositionList:
            if record.messageHeader == messageHeader: 
                record.positionMatrix = matrix
                anyWasChanged = True
        if anyWasChanged == False:
            raise Exception("Nothing to change.")
        
        
    def __str__(self):
        return "\n".join([str(record) for record in self._beaconPositionList ])
    
if __name__ == "__main__":
    pass
