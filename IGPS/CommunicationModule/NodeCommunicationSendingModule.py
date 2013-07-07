'''
Created on 13-05-2013

@author: Olek
'''
import time
import socket, logging  # @UnusedImport
from CommunicationModule import MessageTypes as MT
from ConfigurationModule import NodeConnectionConfigurationProvider as NCCP
from DataModels import DataToOtherNode as DTON

class NodeCommunicationSendingModule():

    def __init__(self, sourceNodeId, messageHeader):
        self.dataToOtherNode = DTON.DataToOtherNode(sendingNodeId = sourceNodeId,
                                                    messageHeader = messageHeader)
    
    def _SendMessageToNode(self, messages, nodeId):
        
        contact = NCCP.NodeConnectionConfigurationProvider(nodeId)

        sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
        sock.settimeout(1)
        for i in range(len(messages)):
            message = messages[i]
            print "SENDING:         " + message
            logging.info("Node {0} to node {1}: {2}".format(self.dataToOtherNode.sendingNodeId, nodeId, message))
            sock.sendto( message, (contact.nodeIp, contact.nodePort) )
            receivedAck = None
            try:
                receivedAck = sock.recv(contact.bufferSize)
            except:
                logging.error("Timeout on receiving ack for: " + message)
            finally:
                if receivedAck != "ACK" + message:
                    logging.error("Retry: " + message)
                    i -= 1
                else:
                    print "RECEIVED ACK: " + receivedAck
        sock.close()
        
            #         for message in messages:
#             logging.info("Node {0} to node {1}: {2}".format(self.dataToOtherNode.sendingNodeId, nodeId, message))
#             sock.sendto( message, (contact.nodeIp, contact.nodePort) )
#             data = sock.recv(NCCP.NodeConnectionConfigurationProvider.bufferSize)
#             print data
        
        #try:
        #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.connect((contact.nodeIp, contact.nodePort))
#         for i in range(len(messages)):
#             message = messages[i]
#             print "Wysylam :" + message
#             sock.send(message)
#             ack = sock.recv(NCCP.NodeConnectionConfigurationProvider.bufferSize)
#             print "ACK :" + ack
#             if ack != "ACK" + message:
#                 raise Exception("Missing ACK")
# #                 logging.error("Message resend: {0}".format(messages[i]))
# #                 i -= 1
#             time.sleep(0.01)
#         sock.close()
        #except:
        #    print "Retry"
        #    time.sleep(0.5)
            #self._SendMessageToNode(messages, nodeId)
        
    def InformHomeAboutNewBeaconSignalReceive(self, destinationNodeId):
        dataToSend = self.dataToOtherNode.GetCommonMessageList()
        message = self._JoinMessage( MT.MessageTypes.RECEIVED_BEACON_SIGNAL, dataToSend)
        self._SendMessageToNode([message], destinationNodeId)
        
    def AskNodeToPrepareSubMatrix(self, destinationNodeId):
        dataToSend = self.dataToOtherNode.GetCommonMessageList()
        message = self._JoinMessage( MT.MessageTypes.ASKED_TO_PREPARE_SUB_MATRIX, dataToSend)
        self._SendMessageToNode([message], destinationNodeId)
        
    def InformHomeThatSubMatrixWasCreated(self, destinationNodeId):
        dataToSend = self.dataToOtherNode.GetCommonMessageList()
        message = self._JoinMessage( MT.MessageTypes.SUB_MATRIX_CREATED, dataToSend )
        self._SendMessageToNode([message], destinationNodeId)
        
    def RequestNodeToStartSubMatrixTransfer(self, destinationNodeId):
        dataToSend = self.dataToOtherNode.GetCommonMessageList()
        message = self._JoinMessage( MT.MessageTypes.WHANT_SUB_MATRIX, dataToSend )
        self._SendMessageToNode([message], destinationNodeId)
        
    def SendSubMatrixToNode(self, destinationNodeId, subMatrix):
        messages = []
        # TODO: modify for 3D model
        for x in range(len(subMatrix.data)):
            for y in range(len(subMatrix.data[x])):
                value = subMatrix.data[x][y]
                if 0 != value:
                    dataToSend = self.dataToOtherNode.GetSubMatrixMessageList(subMatrixX = x,
                                                                              subMatrixY = y,
                                                                              subMatrixZ = 0,
                                                                              subMatrixValue = value)
                    message = self._JoinMessage( MT.MessageTypes.SUB_MATRIX_PART, dataToSend )
                    messages.append(message)
        dataToSend = self.dataToOtherNode.GetCommonMessageList()
        message = self._JoinMessage( MT.MessageTypes.SUB_MATRIX_END, dataToSend )
        messages.append(message)
        self._SendMessageToNode(messages, destinationNodeId)
        
    def AskNodeToSendItsPosition(self, destinationNodeId):
        dataToSend = self.dataToOtherNode.GetCommonMessageList()
        message = self._JoinMessage( MT.MessageTypes.ASK_FOREIGN_NODE_POSITION, dataToSend)
        self._SendMessageToNode([message], destinationNodeId)
        
    def SendSelfPositionToNode(self, destinationNodeId, otherNodePosition):
        dataToSend = self.dataToOtherNode.GetNodePossitionMessageList(otherNodePosition.X, otherNodePosition.Y, otherNodePosition.Z)
        message = self._JoinMessage( MT.MessageTypes.FOREIGN_NODE_POSITION, dataToSend )
        self._SendMessageToNode([message], destinationNodeId)
        
    def _JoinMessage(self, joinWord, listOfElementsToJoin):
        return joinWord.join(str(x) for x in listOfElementsToJoin)

if __name__ == "__main__":
    pass