# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 15:41:59 2014

@author: yanlanfei
"""

from statistic import doStatistic
from PrepData import preprocessData
from nodeList import nodeList
from lnode import lnode
from FPnode import FPnode
from transDesc import processTransForTree
from printTree import printFPTree

def buildTree(thshd):
    transList=preprocessData()#get the transaction
    itemDic=doStatistic(transList)#get each item's support count
    
    nL=nodeList()#create a node list 
    
    for itemKey in itemDic.keys():
        ln=lnode(itemKey,itemDic[itemKey],[])
        nL.addNode(ln)#add the item info into the node list
        
    nL.sortByDesc()# sort the list by support count descending
    
    threshold=thshd#set the threshold and filter the list
    while(nL.nList[len(nL.nList)-1].supportCount<threshold):
        nL.nList.pop()
    
    root=FPnode("root",0,0)#build the tree
    for index in range(len(transList)):
        pTrans=processTransForTree(nL.nList,transList[index])
        cnode=root
        for item in pTrans:
            
            findResult=cnode.findChild(item)
            if findResult==None:
                
                tempNode=FPnode(item,1,cnode)
                cnode.addChild(tempNode)
                nL.insertLevelList(tempNode)
                cnode=tempNode
                
            
            else:
                
                cnode=findResult
                cnode.supportCount=cnode.supportCount+1
    result=[root,nL]
    return result