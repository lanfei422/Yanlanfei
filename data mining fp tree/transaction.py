# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 13:48:11 2014

@author: yanlanfei
"""

class transNode(object):
    def __init__(self,transID,number):#transaction node using to do statistic
        self.transID=transID
        self.itemNumber=number
        self.itemList=[]