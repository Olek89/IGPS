'''
Created on 24-03-2013

@author: Olek
'''
import logging
from DataModels import NodeRecord as NR

class NodeDb():

    def __init__(self):
        self._currentId = 0
        self._records = []
        
    def RegisterNewBeaconMessage(self, messageHeader, receivingTime, positionSubMatrix):
        record = NR.NodeRecord(recordId = self._currentId, 
                               messageHeader = messageHeader, 
                               receivingTime = receivingTime,
                               positionSubMatrix = positionSubMatrix)
        self._records.append(record)
        self._currentId += 1
    
    def GetRecordForMessageHeader(self, messageHeader):
        for record in self._records:
            if record.messageHeader == messageHeader:
                return record
        logging.debug("Record:" + "\n".join( [str(x) for x in self._records]))
        messageWarning = "NodeDataSource does not contains: {0}".format(messageHeader) 
        raise Exception(messageWarning)
    
    def AddSubMatrixToRecord(self, recordToUpdate, subMatrix):
        for record in self._records:
            if record == recordToUpdate:
                record.subMatrix = subMatrix
                return None
        raise Exception("Record could not be updated.")

if __name__ == "__main__":
    pass