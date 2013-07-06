'''
Created on 03-05-2013

@author: Olek
'''

from DataModels import MessageHeader as MH
from NodeController import NodeController as NC
import logging
import datetime, time, random

def MAIN_SIM():
    nodesList = CreateNodes()
        
    try:
        for node in nodesList:
            node.StartNode()
            
        SendFakeBeaconSignalForNodes(nodesList)
        #time.sleep(150) # wait for computations and debug
    
    except:
        raise
    
    finally:
        for node in nodesList:
            node.StopNode()
    print "SIMULATION ENDS"
    
def CreateNodes(nodesIdToBeCreated = [2, 3, 6]):#, 1, 3, 4]):
    nodesList = []
    for nodeId in nodesIdToBeCreated:
        nodesList.append(NC.NodeController (nodeId))
    return nodesList

def SendFakeBeaconSignalForNodes(nodesList):
    messageHeader = MH.MessageHeader(beaconId = 1, homeNodeId = nodesList[-1].nodeId, beaconTimeStamp = datetime.datetime.now())
    time.sleep(1)
    for node in nodesList:
        microseconds = random.Random().randint(10000, 20000)
        receivingTime = messageHeader.beaconTimeStamp + datetime.timedelta(microseconds = microseconds)
        logging.info("Send fake beacon signal to node {}".format(node.nodeId))
        node.beaconReceiver.onBeaconSignalReceive(messageHeader, receivingTime) # Fire event
        time.sleep(0.2) # Introduce communication delays

if __name__== '__main__':
#     logging.basicConfig(format='%(asctime)s.%(msecs)03d %(message)-80s %(filename)-40s at line:%(lineno)-3d func: %(funcName)-35s thread: %(thread)-5d ',
#                         datefmt="%H:%M:%S",
# #                        level=logging.INFO)
#                         level=logging.DEBUG)
    logging.basicConfig(format='%(asctime)s.%(msecs)03d %(message)-80s %(filename)-40s at line:%(lineno)-3d func: %(funcName)-35s thread: %(thread)-5d ',
                         datefmt="%H:%M:%S", filename='logs.log', filemode='w', level=logging.DEBUG)
    MAIN_SIM()