# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 14:28:07 2014

@author: yanlanfei
"""

def doStatistic(tl):
    itemDic={}    
    
    itemNumber=21
    for i in range(1,21):
        itemID='item'+str(i)
        itemDic[itemID]=0#initiate the item dictionary which is for statistic
        
    transList=tl#get the processed data
    
    for trans in transList:
        itemNumber=trans.itemNumber
        for i in range(itemNumber):
            #print trans.itemList[i]
            itemDic[trans.itemList[i]]=itemDic[trans.itemList[i]]+1#add 1 to the item.
    #print itemDic
    return itemDic