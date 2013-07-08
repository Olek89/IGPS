'''
Created on 04-05-2013

@author: Olek
'''
from Common.Tools import EventHook as EH
from ConfigurationModule import NodeConnectionConfigurationProvider as NCCP
from DataModels import DataFromOtherNode as DFON
from CommunicationModule import MessageTypes as MT

import threading, socket, logging, time

class NodeCommunicationReceivingModule():
    '''Receives data on socket in thread based on received configuration.
       Fires events with data model according to received data.'''

    def __init__(self, nodeId):
        self.launched = False
        self.nodeId = nodeId
        self.configuration = NCCP.NodeConnectionConfigurationProvider(self.nodeId)
        logging.debug("Node receiver created for node: {0}".format(self.nodeId))
        
        self.process = threading.Thread(target = self._MessageExpecting)
        
        # Possible Events
        self.onSignalReceivedAtForeignNode = EH.EventHook()
        self.onAskedForCalculateSubMatrix = EH.EventHook()
        self.onEndOfPreparingPartialResultByForeignNode = EH.EventHook()
        self.onRequestToSendPartialResult = EH.EventHook()
        self.onPartialResult = EH.EventHook()
        self.onSubMatrixSendingEnd = EH.EventHook()
        self.onReceivingAskOfNodePosition = EH.EventHook()
        self.onReceivingNodePosition = EH.EventHook()
    
    def Start(self):
        if self.launched:
            raise Exception("Already started")
        self.launched = True 
        self.process.start()
        time.sleep(0.5) # Wait for thread to be ready
    
    def Stop(self):
        if self.launched:
            self.launched = False
            self.process.join(timeout = 2)
            self.process._Thread__stop()
        
    def _MessageExpecting(self):
        try:
            ip = self.configuration.nodeIp
            port = self.configuration.nodePort
            ackPort = self.configuration.nodeAckPort
            logging.debug("Node receiver of node: {0} will use IP: {1}, PORT: {2}".format(self.nodeId, ip, port))
            
            self.ack_sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
            self.ack_sock.bind((ip, ackPort))
            self.node_sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
            self.node_sock.bind( (ip, port) )
            while self.launched:
                data, addr = self.node_sock.recvfrom( self.configuration.bufferSize )
                if data is not None:
                    self._SendAck(data, addr)
                    self._DataFromOtherNode(data)
            self.node_sock.close()
            logging.debug("Node receiver ends at: {0}".format(str(self.nodeId)))
            
        except Exception as e:
            logging.info("Node receiver closed at node {0}, because of: {1}".format(self.nodeId, str(e)))
        self.ack_sock.close()
    
    def _SendAck(self, data, addr):
        self.ack_sock.sendto("ACK" + data, addr)
        
    def _DataFromOtherNode(self, rawData):
        logging.info("Node {0} received:  {1}".format(self.nodeId, rawData))
        if  MT.MessageTypes.RECEIVED_BEACON_SIGNAL in rawData:
            parsedData = DFON.DataFromOtherNode(rawData.split(MT.MessageTypes.RECEIVED_BEACON_SIGNAL))
            self.onSignalReceivedAtForeignNode(parsedData)
        
        elif MT.MessageTypes.ASKED_TO_PREPARE_SUB_MATRIX in rawData:
            parsedData = DFON.DataFromOtherNode(rawData.split(MT.MessageTypes.ASKED_TO_PREPARE_SUB_MATRIX))
            self.onAskedForCalculateSubMatrix(parsedData)
        
        elif MT.MessageTypes.SUB_MATRIX_CREATED in rawData:
            parsedData = DFON.DataFromOtherNode(rawData.split(MT.MessageTypes.SUB_MATRIX_CREATED))
            self.onEndOfPreparingPartialResultByForeignNode(parsedData)
        
        elif MT.MessageTypes.WHANT_SUB_MATRIX in rawData:
            parsedData = DFON.DataFromOtherNode(rawData.split(MT.MessageTypes.WHANT_SUB_MATRIX))
            self.onRequestToSendPartialResult(parsedData)
        
        elif MT.MessageTypes.SUB_MATRIX_PART in rawData:
            splitedData = rawData.split(MT.MessageTypes.SUB_MATRIX_PART)
            parsedData = DFON.DataFromOtherNode(splitedData, isSubMatrixPart = True)
            self.onPartialResult(parsedData)
        
        elif MT.MessageTypes.SUB_MATRIX_END in rawData:
            parsedData = DFON.DataFromOtherNode(rawData.split(MT.MessageTypes.SUB_MATRIX_END))
            self.onSubMatrixSendingEnd(parsedData)
        
        elif MT.MessageTypes.ASK_FOREIGN_NODE_POSITION in rawData:
            parsedData = DFON.DataFromOtherNode(rawData.split(MT.MessageTypes.ASK_FOREIGN_NODE_POSITION))
            self.onReceivingAskOfNodePosition(parsedData)
        
        elif MT.MessageTypes.FOREIGN_NODE_POSITION in rawData:
            splitedData = rawData.split(MT.MessageTypes.FOREIGN_NODE_POSITION)
            parsedData = DFON.DataFromOtherNode(splitedData, isNodePosition = True)
            self.onReceivingNodePosition(parsedData)
        
        else: raise Exception( str("Unknown message" + str(rawData)) )

if __name__ == "__main__":
    pass