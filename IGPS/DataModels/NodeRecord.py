'''
Created on 23-03-2013

@author: Olek
'''

class NodeRecord():

    def __init__(self, recordId, messageHeader, receivingTime, positionSubMatrix):
        self.recordId      = recordId
        self.messageHeader = messageHeader
        self.receivingTime = receivingTime
        self.nodePosition  = positionSubMatrix
        self.subMatrix     = None
        
    def __str__(self):
        hasSubMatrix = self.subMatrix != None
        return "id:{0}\n header:{1}\n received:{2} \n hasSubMatrix:{3}".format(self.recordId, self.messageHeader, self.receivingTime, hasSubMatrix)