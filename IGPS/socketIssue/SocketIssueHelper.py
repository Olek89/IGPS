'''
Created on 08-07-2013

@author: Olek
'''
from CommunicationModule import NodeCommunicationReceivingModule as NCRM

class socketIssueHelper:
    received = 0
    
    def __init__(self, receiverId):
        self.nodeReceiver = NCRM.NodeCommunicationReceivingModule(nodeId = receiverId)
        self.nodeReceiver.onSignalReceivedAtForeignNode += self.addReceived
        self.nodeReceiver.Start()
    
    def Stop(self):
        self.nodeReceiver.Stop()
    
    def addReceived(self, *args):
        self.received += 1

if __name__ == "__main__":
    pass