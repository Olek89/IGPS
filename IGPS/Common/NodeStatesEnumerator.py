'''
Created on 24-03-2013

@author: Olek
'''

class NodeStatesEnumerator():
    #TODO: Update comments
    NEWRECEIVED         = 1 # "Those are data from other node which received yours beacon signal."
    ASKED               = 2 # "Those are data and tolerance for which you will calculate position matrix."
    DONE                = 3 # "Those are data for which other node prepared sub matrix for me."
    WHANT               = 4 # "Those are data for which I made sub matrix and its home node what them."
    END                 = 5 # "Node is currently receiving partial beacon position."
    POSASKED            = 6 # "SubMatrix is received ask about node position"
    POSRECEIVED         = 7 # "Position was received. Ready to add to main matrix."
    NOLONGERNEEDED      = 8 # "Added to main matrix. Can be removed from home node database"

if __name__ == "__main__":
    pass