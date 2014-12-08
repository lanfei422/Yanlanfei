# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 22:04:12 2014

@author: yanlanfei
"""

class lnode:
    'list node definition'
    myVersion='1.1'
    
    def __init__(self,itemID,supportCount,startPoint):
        self.itemID=itemID
        self.supportCount=supportCount
        self.startPoint=startPoint 
        #this is the head node of the list which holds the FP node with the same ID
    