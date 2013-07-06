'''
Created on 05-05-2013

@author: Olek
'''

class Callable:
    def __init__(self, anycallable):
        self.__call__ = anycallable        

if __name__ == "__main__":
    pass