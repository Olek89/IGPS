'''
Created on 16-07-2013

@author: Olek
'''
from DataModels import MessageHeader as MH
import datetime, time, random, logging

def SendFakeBeaconSignalForNodes(nodesList, homeNodeId):
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
    
if __name__ == "__main__":
    pass