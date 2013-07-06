'''
Created on 04-05-2013

@author: Olek
'''
#import threading
import time, logging

from Common.Tools import EventHook as EH

class BeaconCommunicationModule():

    def __init__(self):
        self.launched = False
        self.onBeaconSignalReceive = EH.EventHook()
    
    def Start(self):
        self.launched = True
        #threading.Thread(target = self._BeaconExpecting).start()
        logging.debug("Beacon receiver started")
    
    def Stop(self):
        self.launched = False
    
    def _BeaconExpecting(self):
        #TODO: Communication with real device
        while self.launched:
            time.sleep(0.1)

if __name__ == "__main__":
    pass