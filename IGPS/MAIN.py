'''
Created on 03-05-2013

@author: Olek
'''
from ConfigurationModule import Configuration as C
from DataModels import MessageHeader as MH
from NodeController import NodeController as NC
import logging
import datetime, time, random

homeNodeId = 1

def MAIN_SIM():
    nodesList = CreateNodes()
        
    try:
        for node in nodesList:
            node.StartNode()
            
        messageHeader = SendFakeBeaconSignalForNodes(nodesList)
        
        raw_input("Enter to end simulation and save matrix...\n")
        nodesList[homeNodeId].SaveMatrix(messageHeader)
       
    except:
        raise
    
    finally:
        for node in nodesList:
            node.StopNode()
    print "SIMULATION ENDS"
    
def CreateNodes():
    nodesList = []
    for nodeId in C.Configuration.nodesIdToBeCreated:
        nodesList.append(NC.NodeController (nodeId))
    return nodesList

def SendFakeBeaconSignalForNodes(nodesList):
    messageHeader = MH.MessageHeader(beaconId = 1, homeNodeId = nodesList[homeNodeId].nodeId, beaconTimeStamp = datetime.datetime.now())
    time.sleep(1)
    for node in nodesList:
        if node.nodeId == 1:
            microseconds = 200000
        elif node.nodeId == 2:
            microseconds = 180000
        elif node.nodeId == 3:
            microseconds = 282000
        else:
            microseconds = random.Random().randint(80000, 200000)
        
        receivingTime = messageHeader.beaconTimeStamp + datetime.timedelta(microseconds = microseconds)
        logging.info("Send fake beacon signal to node {0}".format(node.nodeId))
        node.beaconReceiver.onBeaconSignalReceive(messageHeader, receivingTime) # Fire event
        time.sleep(0.2) # Introduce communication delays
    return messageHeader

if __name__== '__main__':
    logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)-80s %(filename)-40s at line:%(lineno)-3d func: %(funcName)-35s thread: %(thread)-5d ',
                         datefmt="%H:%M:%S", filename='logs.log', filemode='w', level=logging.INFO)
    MAIN_SIM()
