'''
Created on 06-07-2013

@author: Olek
'''
from CommunicationModule import NodeCommunicationSendingModule as NCSM
import SocketIssueHelper as SIH
import unittest

class socketIssueTests(unittest.TestCase):
    
    message = "2BEACON6BEACON1BEACON2013-07-06 22:25:44.031000"
    
    def testReceiverGetsAllMessages(self):
        receiverId = 2
        expected = 10000000
        
        receiver = SIH.socketIssueHelper(receiverId = receiverId)
        
        sender = NCSM.NodeCommunicationSendingModule(sourceNodeId = 1, messageHeader = "header")
        sender._SendMessageToNode(messages = [self.message for i in range(expected)], nodeId = receiverId)  # @UnusedVariable
        
        receiver.Stop()
        self.assertEqual(expected, receiver.received)
        
    def testReceiverGetsAllMessagesWhenMultiNodeCommunication(self):
        receiverId = 4
        expected = 30000
        
        receiver = SIH.socketIssueHelper(receiverId = receiverId)
        
        sender1 = NCSM.NodeCommunicationSendingModule(sourceNodeId = 1, messageHeader = "header")
        sender2 = NCSM.NodeCommunicationSendingModule(sourceNodeId = 2, messageHeader = "header")
        messages = [self.message for i in range(expected/3)] # @UnusedVariable
        
        sender1._SendMessageToNode(messages, nodeId = receiverId)
        sender2._SendMessageToNode(messages, nodeId = receiverId)
        sender1._SendMessageToNode(messages, nodeId = receiverId)
        
        receiver.Stop()
        self.assertEqual(expected, receiver.received)

if __name__ == "__main__":
    unittest.main()