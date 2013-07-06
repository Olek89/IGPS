'''
Created on 03-05-2013

@author: Olek
'''
from ConfigurationModule import NodeConnectionConfigurationProvider as NCCP
import socket

def SendMessageToNode(nodeId, MSG):
    nodeContact = NCCP.NodeConnectionConfigurationProvider(nodeId) 
    
    sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    sock.sendto( MSG, (nodeContact.nodeIp, nodeContact.nodePort) )
    sock.close()