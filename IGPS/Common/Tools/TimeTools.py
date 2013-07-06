'''
Created on 22-03-2013

@author: Olek
'''

import datetime
import random

def GetStartTime():
    seconds = random.Random().random()
    return datetime.datetime.now() - datetime.timedelta(seconds = seconds)
    
def GetEndTime():
    seconds = random.Random().random()
    return datetime.datetime.now() + datetime.timedelta(seconds = seconds)

if __name__ == "__main__":
    pass