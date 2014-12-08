# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 20:49:56 2014

@author: yanlanfei
"""

class FPnode(object):
    'FP tree node definition'
    myVersion='1.1'
    def __init__(self,itemID,supportCount,parent):
        self.itemID=itemID #item id
        self.supportCount=supportCount #node support count 
        self.parent=parent #the object pointing to parent
        #self.nextBrother=nextBrother #brother list link
        self.children=[] #the node's children
        
    def addChild(self,child):
        self.children.append(child)
    def delChild(self,child):
        self.children.remove(child)
    def findChild(self,it):
        for child in self.children:
            if str(it)==str(child.itemID):
                return child
            else:
                pass
            
        return None        