'''
Created on 03-05-2013

@author: Olek
'''
import socket

class NodeConnectionConfigurationProvider():
    bufferSize = 100
    reconnectionDelay = 0.2
    #TODO: Connect to configuration database 
    def __init__(self, nodeId):
        #Temporary solution
        self.nodeIp = str(socket.gethostbyname(socket.gethostname()))
        self.nodePort = 3000 + int(nodeId)
        

if __name__ == "__main__":
    pass