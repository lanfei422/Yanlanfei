# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 22:09:01 2014

@author: yanlanfei
"""

class nodeList(object):
    'this is the list definition'
    myVersion='1.1'
    
    def __init__(self):
        self.nList=[]#initiate the list
        
    def addNode(self,lnode):
        self.nList.append(lnode)
        
    def delNode(self,lnode):
        self.nList.remove(lnode)
        
    def setLnodeNext(self,lnode):
        #set the head of the list with the same support node.
        lnodeID=lnode.itemID
        length=len(self.nList)
        for i in range(length):
            if(self.nList[i].itemID==lnodeID):
                self.nList[i].startPoint=lnode
                break
        
    def sortByDesc(self):
        self.nList.sort(lambda ob1,ob2:-cmp(ob1.supportCount,ob2.supportCount))
        
    def printList(self):
        for node in self.nList:
            print node.itemID
            print node.supportCount
            print ' '
        
    def insertLevelList(self,FPnode):
        for item in self.nList:
            if str(item.itemID)==str(FPnode.itemID):
                item.startPoint.append(FPnode)
    def findNode(self,itemID):
        for i in self.nList:
            if i.itemID==itemID:
                return i