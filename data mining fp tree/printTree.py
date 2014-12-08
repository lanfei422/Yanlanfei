# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 13:32:27 2014

@author: yanlanfei
"""

def printFPTree(FPnode):
    que=[]
    que.append(FPnode)
    while(len(que)!=0):
        cn=que.pop(0)
        print str(cn.itemID)+":"+str(cn.supportCount)
        if len(cn.children)!=0:
            que.extend(cn.children)