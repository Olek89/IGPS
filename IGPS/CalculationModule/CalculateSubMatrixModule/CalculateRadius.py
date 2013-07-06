'''
Created on 21-03-2013

@author: Olek
'''
import datetime
import logging
from ConfigurationModule.Constants import Constants as C

class CalculateRadius():

    def CalculateRadiusBasedOnDelay(self, beaconTimeStamp, receivingTime):
        '''
        We assume that beacon is synchronized, but in time possible rescale may be performed on submatrix.
        '''
        deltaTime = (receivingTime - beaconTimeStamp)
        seconds = datetime.timedelta.total_seconds(deltaTime)
        radius = C.WaveSpeedInMpS * seconds        
        timeAccuracy = 1 # TODO: Add accuracy based on time synchronization
        
        radius = int(radius * timeAccuracy) #TODO: remove workaround
        logging.debug("Radius calculated: {0}".format(radius))
        return radius
    
if __name__ == "__main__":
    pass