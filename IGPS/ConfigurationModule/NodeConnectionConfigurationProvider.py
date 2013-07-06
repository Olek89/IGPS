'''
Created on 03-05-2013

@author: Olek
'''
import socket

class NodeConnectionConfigurationProvider():
    #TODO: Connect to configuration database 
    def __init__(self, nodeId):
        #Temporary solution
        self.nodeIp = str(socket.gethostbyname(socket.gethostname())) #"10.0.0.10" #str(socket.IP_MULTICAST_LOOP) # TODO: "DNS" server 
        self.nodePort = 3000 + int(nodeId)

if __name__ == "__main__":
    pass