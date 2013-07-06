'''
Created on 13-05-2013

@author: Olek
'''
import socket, logging  # @UnusedImport
from CommunicationModule import MessageTypes as MT
from ConfigurationModule import NodeConnectionConfigurationProvider as NCCP
from DataModels import DataToOtherNode as DTON

class NodeCommunicationSendingModule():

    def __init__(self, sourceNodeId, referenceBeaconMessage):
        self.dataToOtherNode = DTON.DataToOtherNode(sendingNodeId = sourceNodeId,
                                                    messageHeader = referenceBeaconMessage)
    
    def _SendMessageToNode(self, message, nodeId):
        contact = NCCP.NodeConnectionConfigurationProvider(nodeId) 
        logging.info("Node {0} to node {1}: {2}".format(self.dataToOtherNode.sendingNodeId, nodeId, message))
        
        sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
        sock.sendto( message, (contact.nodeIp, contact.nodePort) )
        sock.close()
        
    def InformHomeAboutNewBeaconSignalReceive(self, destinationNodeId):
        dataToSend = self.dataToOtherNode.GetCommonMessageList()
        message = self._JoinMessage( MT.MessageTypes.RECEIVED_BEACON_SIGNAL, dataToSend)
        self._SendMessageToNode(message, destinationNodeId)
        
    def AskNodeToPrepareSubMatrix(self, destinationNodeId):
        dataToSend = self.dataToOtherNode.GetCommonMessageList()
        message = self._JoinMessage( MT.MessageTypes.ASKED_TO_PREPARE_SUB_MATRIX, dataToSend)
        self._SendMessageToNode(message, destinationNodeId)
        
    def InformHomeThatSubMatrixWasCreated(self, destinationNodeId):
        dataToSend = self.dataToOtherNode.GetCommonMessageList()
        message = self._JoinMessage( MT.MessageTypes.SUB_MATRIX_CREATED, dataToSend )
        self._SendMessageToNode(message, destinationNodeId)
        
    def RequestNodeToStartSubMatrixTransfer(self, destinationNodeId):
        dataToSend = self.dataToOtherNode.GetCommonMessageList()
        message = self._JoinMessage( MT.MessageTypes.WHANT_SUB_MATRIX, dataToSend )
        self._SendMessageToNode(message, destinationNodeId)
        
    def SendSubMatrixCellToNode(self, destinationNodeId, subMatrixX, subMatrixY, subMatrixZ, subMatrixValue):
        dataToSend = self.dataToOtherNode.GetSubMatrixMessageList(subMatrixX, subMatrixY, subMatrixZ, subMatrixValue)
        message = self._JoinMessage( MT.MessageTypes.SUB_MATRIX_PART, dataToSend )
        self._SendMessageToNode(message, destinationNodeId)
        
    def SendEndOfSubMatrixIndicator(self, destinationNodeId):
        dataToSend = self.dataToOtherNode.GetCommonMessageList()
        message = self._JoinMessage( MT.MessageTypes.SUB_MATRIX_END, dataToSend )
        self._SendMessageToNode(message, destinationNodeId)
        
    def SendSelfPositionToNode(self, destinationNodeId, otherNodePositionX, otherNodePositionY, otherNodePositionZ):
        dataToSend = self.dataToOtherNode.GetNodePossitionMessageList(otherNodePositionX, otherNodePositionY, otherNodePositionZ)
        message = self._JoinMessage( MT.MessageTypes.FOREIGN_NODE_POSITION, dataToSend )
        self._SendMessageToNode(message, destinationNodeId)
        
    def _JoinMessage(self, joinWord, listOfElementsToJoin):
        return joinWord.join(str(x) for x in listOfElementsToJoin)

if __name__ == "__main__":
    pass