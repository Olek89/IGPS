'''
Created on 03-05-2013

@author: Olek
'''
from ConfigurationModule import Configuration as C

from NodeController import NodeController as NC
from Common.SimulationMethods import SendFakeBeaconSignalForNodes
import logging

homeNodeId = 1

def MAIN_SIM():
    nodesList = CreateNodes()
        
    try:
        for node in nodesList:
            node.StartNode()
            
        messageHeader = SendFakeBeaconSignalForNodes(nodesList, homeNodeId)
        
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



if __name__== '__main__':
    logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)-80s %(filename)-40s at line:%(lineno)-3d func: %(funcName)-35s thread: %(thread)-5d ',
                         datefmt="%H:%M:%S", filename='logs.log', filemode='w', level=logging.INFO)
    MAIN_SIM()
