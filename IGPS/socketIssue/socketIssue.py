'''
Created on 06-07-2013

@author: Olek
'''
from CommunicationModule import NodeCommunicationReceivingModule as NCRM
from CommunicationModule import NodeCommunicationSendingModule as NCSM

class socketIssue():
    received = 0
    
    def __init__(self):
        self.nodeReceiver = NCRM.NodeCommunicationReceivingModule(nodeId = 2)
        self.nodeReceiver.onSignalReceivedAtForeignNode += self.addReceived
        
        self.nodeReceiver.Start()
    
    def Stop(self):
        self.nodeReceiver.Stop()
    
    def addReceived(self, *args):
        self.received += 1

if __name__ == "__main__":
    expected = 100
    print "start"
    r = socketIssue()
    message = "2BEACON6BEACON1BEACON2013-07-06 22:25:44.031000"
    s = NCSM.NodeCommunicationSendingModule(sourceNodeId = 1, messageHeader = "header")
    s._SendMessageToNode(messages = [message for i in range(expected)], nodeId = 2)
    
    print r.received - expected
    r.Stop()
    print "end"
    
    