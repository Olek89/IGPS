'''
Created on 03-05-2013

@author: Olek
'''

from DataAccessModule import NodeDb as NDB
from DataAccessModule import HomeNodeDb as HNDB
from ConfigurationModule import Configuration as C
from DataModels import Matrix as M
from CommunicationModule import BeaconCommunicationModule as BCM
from CommunicationModule import NodeCommunicationReceivingModule as NCRM
from CommunicationModule import NodeCommunicationSendingModule as NCSM
from Common import NodeStatesEnumerator as NSE
from CalculationModule.CalculateSubMatrixModule import CalculateSubMatrixController as CSMCM
from CalculationModule.NodePositionProviderModule import NodePositionProvider as NPP

import logging
from CommunicationModule.NodeCommunicationSendingModule import NodeCommunicationSendingModule

class NodeController():

    def __init__(self, nodeId):
        self.launched = False
        self.nodeId = nodeId
        
        # Data Access Module
        self.nodeDb = NDB.NodeDb()
        self.homeNodeDb = HNDB.HomeNodeDb()
        
        # Communication Module
        self.beaconReceiver = BCM.BeaconCommunicationModule()
        self.beaconReceiver.onBeaconSignalReceive += self._BeaconSignalReceived
        
        self.nodeReceiver = NCRM.NodeCommunicationReceivingModule(self.nodeId)
        self.nodeReceiver.onSignalReceivedAtForeignNode += self._SignalReceivedAtForeignNode
        self.nodeReceiver.onAskedForCalculateSubMatrix += self._AskedForCalculateSubMatrix
        self.nodeReceiver.onEndOfPreparingPartialResultByForeignNode += self._RegisterReadyNodeToDownloadFromSubMatrix
        self.nodeReceiver.onRequestToStartSendingPartialResult += self._StartSendingCalculatedSubMatrix
        self.nodeReceiver.onPartialResult += self._AddPartialResult
        self.nodeReceiver.onSubMatrixSendingEnd += self._ReceivedSubMatrixSendingEnd
        self.nodeReceiver.onReceivingNodePosition += self._ReceivedReceivingNodePosition
        
        # Calculation Module
        self.calculationModule = CSMCM.CalculateSubMatrixController()
        self.nodePositionProvider = NPP.NodePositionProvider()
        
        # Downloading queue manager
        self.isCurrentlyComputing = False
        
        logging.debug("Node created: " + str(self.nodeId))
        
    def StartNode(self):
        if False == self.launched:
            self.beaconReceiver.Start()
            self.nodeReceiver.Start()
            self.launched = True
        else:
            raise Exception("Already launched")
        logging.info("Node Started: " + str(self.nodeId))
    
    def StopNode(self):
        self.launched = False
        self.beaconReceiver.Stop()
        self.nodeReceiver.Stop()
    
    #===========================================================================
    # Methods for sending data
    #===========================================================================
    def _AskNodeForCalculateSubMatrix(self, messageHeader, nodeId):
        sender = NodeCommunicationSendingModule(sourceNodeId = self.nodeId, referenceBeaconMessage = messageHeader)
        sender.AskNodeToPrepareSubMatrix(destinationNodeId = nodeId)
        self.homeNodeDb.ChangeStateOfNodeForSpecificBeaconMessageIdentity(messageHeader = messageHeader,
                                                                          nodeId = nodeId,
                                                                          newState = NSE.NodeStatesEnumerator.ASKED)
    
    def _InformHomeThatSubMatrixWasCalculated(self, messageHeader, nodeId):
        sender = NodeCommunicationSendingModule(sourceNodeId = self.nodeId, referenceBeaconMessage = messageHeader)
        sender.InformHomeThatSubMatrixWasCreated(destinationNodeId = nodeId)
        
    def _AskNodeToStartTransmittingSubMatrix(self, messageHeader, nodeId):
        sender = NodeCommunicationSendingModule(sourceNodeId = self.nodeId, referenceBeaconMessage = messageHeader)
        sender.RequestNodeToStartSubMatrixTransfer(destinationNodeId = nodeId)
        self.homeNodeDb.ChangeStateOfNodeForSpecificBeaconMessageIdentity(messageHeader = messageHeader,
                                                                          nodeId = nodeId,
                                                                          newState = NSE.NodeStatesEnumerator.WHANT)
        
    def _SendCellValue(self, messageHeader, nodeId, x, y, z, value):
        sender = NodeCommunicationSendingModule(sourceNodeId = self.nodeId, referenceBeaconMessage = messageHeader)
        sender.SendSubMatrixCellToNode(destinationNodeId = nodeId, subMatrixX = x, subMatrixY = y, subMatrixZ = z, subMatrixValue = value)
       
    def _SendSelfPosition(self, messageHeader, nodeId):
        sender = NodeCommunicationSendingModule(sourceNodeId = self.nodeId, referenceBeaconMessage = messageHeader)
        record = self.nodeDb.GetRecordForMessageHeader(messageHeader)
        sender.SendSelfPositionToNode(destinationNodeId  = nodeId,
                                      otherNodePositionX = record.nodePosition.X,
                                      otherNodePositionY = record.nodePosition.Y,
                                      otherNodePositionZ = record.nodePosition.Z)
    
    def _SendTransimissionEnd(self, messageHeader, nodeId):
        sender = NodeCommunicationSendingModule(sourceNodeId = self.nodeId, referenceBeaconMessage = messageHeader)
        sender.SendEndOfSubMatrixIndicator(destinationNodeId = nodeId)
                                   
    #===========================================================================
    # Events requested by Beacon receiver
    #===========================================================================
    def _BeaconSignalReceived(self, messageHeader, receivingTime):
        self.nodeDb.RegisterNewBeaconMessage(messageHeader, receivingTime, self.nodePositionProvider.GetCurrentPosition())
        sender = NCSM.NodeCommunicationSendingModule(sourceNodeId = self.nodeId, referenceBeaconMessage = messageHeader)
        sender.InformHomeAboutNewBeaconSignalReceive(messageHeader.homeNodeId)
        
    #===========================================================================
    # Events requested by foreign nodes service
    #===========================================================================
    def _SignalReceivedAtForeignNode(self, dataFromOtherNode):
        messageHeader = dataFromOtherNode.messageHeader
        nodeId = dataFromOtherNode.sendingNodeId
        self.homeNodeDb.RegisterNewSignalReceivedAtNode(messageHeader = messageHeader, nodeId = nodeId)
        
        nodesForMessage = self.homeNodeDb.GetNodesListForSpecificBeaconMessageIdentity(messageHeader = messageHeader)
        if len(nodesForMessage) >= 3: #TODO: move to configuration file
            nodesToAsk = self.homeNodeDb.GetNodesListForSpecificBeaconMessageIdentity(messageHeader = messageHeader, inState = NSE.NodeStatesEnumerator.NEWRECEIVED)
            for node in nodesToAsk:
                self._AskNodeForCalculateSubMatrix(messageHeader = messageHeader, nodeId = node)
    
    def _AskedForCalculateSubMatrix(self, dataFromOtherNode):
        record = self.nodeDb.GetRecordForMessageHeader(messageHeader = dataFromOtherNode.messageHeader)
        subMatrix = self.calculationModule.CalculateSubMatrix(record = record)
        self.nodeDb.AddSubMatrixToRecord(recordToUpdate = record, subMatrix = subMatrix)
        
        self._InformHomeThatSubMatrixWasCalculated(messageHeader = dataFromOtherNode.messageHeader, nodeId = dataFromOtherNode.messageHeader.homeNodeId)
    
    def _RegisterReadyNodeToDownloadFromSubMatrix(self, dataFromOtherNode):
        self.homeNodeDb.ChangeStateOfNodeForSpecificBeaconMessageIdentity(messageHeader = dataFromOtherNode.messageHeader,
                                                                          nodeId = dataFromOtherNode.sendingNodeId,
                                                                          newState = NSE.NodeStatesEnumerator.DONE)
        if False == self.isCurrentlyComputing:
            self.isCurrentlyComputing = True
            self._AskNodeToStartTransmittingSubMatrix(messageHeader = dataFromOtherNode.messageHeader, nodeId = dataFromOtherNode.sendingNodeId)
    
    def _StartSendingCalculatedSubMatrix(self, dataFromOtherNode):
        record = self.nodeDb.GetRecordForMessageHeader(messageHeader = dataFromOtherNode.messageHeader)
        subMatrix = record.subMatrix
        # TODO: modify for 3D model
        for x in range(len(subMatrix.data)):
            for y in range(len(subMatrix.data[x])):
                value = subMatrix.data[x][y]
                if 0 != value:
                    self._SendCellValue(messageHeader = dataFromOtherNode.messageHeader, 
                                        nodeId = dataFromOtherNode.sendingNodeId, 
                                        x = x, y = y, z = 0, value = value)
        #TODO: Send position on request 
        self._SendSelfPosition(messageHeader = dataFromOtherNode.messageHeader, 
                               nodeId        = dataFromOtherNode.sendingNodeId)
        self._SendTransimissionEnd(messageHeader = dataFromOtherNode.messageHeader, 
                                   nodeId        = dataFromOtherNode.sendingNodeId)
    
    def _AddPartialResult(self, dataFromOtherNode):
        self.homeNodeDb.AddValueToSubMatrixCell(messageHeader = dataFromOtherNode.messageHeader,
                                                nodeId        = dataFromOtherNode.sendingNodeId,
                                                x             = dataFromOtherNode.subMatrixX,
                                                y             = dataFromOtherNode.subMatrixY,
                                                z             = dataFromOtherNode.subMatrixZ,
                                                value         = dataFromOtherNode.subMatrixValue)
    
    def _ReceivedReceivingNodePosition(self, dataFromOtherNode):
        # TODO: Add ask for node position
        self.homeNodeDb.SetReceivingNodePosition(messageHeader = dataFromOtherNode.messageHeader,
                                                 nodeId        = dataFromOtherNode.sendingNodeId,
                                                 position      = dataFromOtherNode.otherNodePosition)
        
    def _ReceivedSubMatrixSendingEnd(self, dataFromOtherNode):
        #TODO: Implement concatenation
        self.homeNodeDb.ChangeStateOfNodeForSpecificBeaconMessageIdentity(messageHeader = dataFromOtherNode.messageHeader,
                                                                          nodeId        = dataFromOtherNode.sendingNodeId,
                                                                          newState      = NSE.NodeStatesEnumerator.END)
        # TODO: Position on request
        nodePosition = None
        while nodePosition != None:
            nodePosition = self.homeNodeDb.GetReceivingNodePosition(messageHeader = dataFromOtherNode.messageHeader,
                                                                    nodeId        = dataFromOtherNode.sendingNodeId)
        nodesToAsk = self.homeNodeDb.GetNodesListForSpecificBeaconMessageIdentity(messageHeader = dataFromOtherNode.messageHeader, inState = NSE.NodeStatesEnumerator.DONE)
        if (len(nodesToAsk) >= 1):
            self._ReceiveMissingSubMatrices(dataFromOtherNode.messageHeader)
        else:
            self._GenerateFinalPositionMatrix(dataFromOtherNode.messageHeader)
        
    def _GenerateFinalPositionMatrix(self, messageHeader):
        matrix = M.Matrix(C.Configuration.matrixSize)
        for nodePosition, subMatrix in self.homeNodeDb.YieldOverSubMatrices(messageHeader):
            for xLocal in range(len(subMatrix.data)):
                for yLocal in range(len(subMatrix.data[xLocal])):
                    # TODO: Add 3D
                    #for zLocal in range(len(subMatrix.data[xLocal][yLocal])):
                    logging.debug("Will add {0} to x:{1} y:{2}".format(subMatrix.data[xLocal][yLocal], nodePosition.X + xLocal, nodePosition.Y + yLocal))
                    if True: #TODO: subMatrix.data[xLocal][yLocal] != 0:
                        matrix.data[nodePosition.X + xLocal][nodePosition.Y + yLocal] += \
                            subMatrix.data[xLocal][yLocal]
        self.homeNodeDb.RegisterBeaconPositionMatrix(messageHeader = messageHeader, matrix = matrix)
        self.isCurrentlyComputing = False
        logging.critical(matrix)
        
    def _ReceiveMissingSubMatrices(self, messageHeader):
        import time
        time.sleep(1)
        nodesToAsk = self.homeNodeDb.GetNodesListForSpecificBeaconMessageIdentity(messageHeader = messageHeader, inState = NSE.NodeStatesEnumerator.DONE)
        if (len(nodesToAsk) >= 1):
            self.isCurrentlyComputing = True
            self._AskNodeToStartTransmittingSubMatrix(messageHeader = messageHeader, nodeId = nodesToAsk[0])
            self.homeNodeDb.ChangeStateOfNodeForSpecificBeaconMessageIdentity(messageHeader = messageHeader,
                                                                              nodeId        = nodesToAsk[0],
                                                                              newState      = NSE.NodeStatesEnumerator.WHANT)
            
if __name__ == "__main__":
    pass