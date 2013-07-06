'''
Created on 30-06-2013

@author: Olek
'''
from Common import NodeStatesEnumerator as NSE

class HomeNodeDbRecord():
    currentId = 0
    
    def __init__(self, messageHeader, receivingNodeId):
        self.recordId = self.currentId
        self.currentId += 1
        
        self.messageHeader   = messageHeader
        self.receivingNodeId = receivingNodeId
        self.receivingNodeStatus = NSE.NodeStatesEnumerator.NEWRECEIVED

if __name__ == "__main__":
    pass