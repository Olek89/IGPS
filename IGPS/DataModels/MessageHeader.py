'''
Created on 20-03-2013

@author: Olek
'''

class MessageHeader():

    def __init__(self, homeNodeId, beaconId, beaconTimeStamp):
        self.homeNodeId = int(homeNodeId)
        self.beaconId   = int(beaconId)
        self.beaconTimeStamp = beaconTimeStamp
        
    def __eq__(self, other):
        hId   = self.homeNodeId == other.homeNodeId
        bId   = self.beaconId == other.beaconId
        bTime = str(self.beaconTimeStamp) == str(other.beaconTimeStamp) # TODO: Use TIC float instead
        return hId and bId and bTime
        
    def __str__(self):
        return "HomeID: {0}, BeaconID: {1}, BeaconTime: {2}".format(self.homeNodeId, self.beaconId, self.beaconTimeStamp)
    
    def __repr__(self):
        return self.__str__()