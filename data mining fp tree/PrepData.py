# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 23:33:32 2014

@author: yanlanfei
"""
from transaction import transNode

def preprocessData():
    
    try:
        f=open('transData','r')
    except IOError,e:
        print 'could not find the data file:',e
        f.close()
    finally:
        allLines=f.readlines()
        f.close()
    
    transList=[]
    
    for eachline in allLines:
        #print eachline
        tempLine=eachline[0:-1]
        tempLine=tempLine.split(' ')
        
        transID=str(tempLine[0])
        transNumber=int(tempLine[1])
        tempTrans=transNode(transID,transNumber)
        
        for item in range(transNumber):
                tempTrans.itemList.append(tempLine[2+item])
                
        transList.append(tempTrans)
#    for i in range(len(transList)):
#        tem=transList[i]
#        for j in range(tem.itemNumber):
#           print tem.itemList[j]
    return transList
    #for i in range(len(transList)):
    #    tem=transList[i]
    #    for j in range(tem.itemNumber):
    #        print tem.itemList[j]