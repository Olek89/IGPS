'''
Created on 30-06-2013

@author: Olek
'''
from Common import NodeStatesEnumerator as NSE
from DataModels import Matrix as M
from ConfigurationModule import Configuration as C

class HomeNodeDbRecord():
    currentId = 0
    
    def __init__(self, messageHeader, receivingNodeId):
        self.recordId = self.currentId
        self.currentId += 1
        
        self.messageHeader         = messageHeader
        self.receivingNodeId       = receivingNodeId
        self.receivingNodePosition = None
        self.receivingNodeStatus   = NSE.NodeStatesEnumerator.NEWRECEIVED
        
        self.calculatedSubMatrix   = M.Matrix(C.Configuration.subMatrixSize)
    
    def __eq__(self, other):
        headerEqual = self.messageHeader == other.messageHeader
        nodeEqual = self.receivingNodeId == other.receivingNodeId
        return headerEqual and nodeEqual
    
    def __str__(self):
        return "\tReceiving Node {0} is {1}".format(self.receivingNodeId, self.receivingNodeStatus)

if __name__ == "__main__":
    pass