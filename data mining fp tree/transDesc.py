# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 16:40:35 2014

@author: yanlanfei
"""

def processTransForTree(nList,trans):
    tempTrans=[]#nList is the node list sorted by support count,trans is the transaction
    for lnode in nList:
        if lnode.itemID in trans.itemList:
            tempTrans.append(lnode.itemID)
    return tempTrans