# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 19:07:38 2014

@author: yanlanfei
"""

from newFP import *
from build import *

threshold=2
r=buildTree(threshold)
r[1].printList()
f=FCI(r[1],r[0],threshold)
print f