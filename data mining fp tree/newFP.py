# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 21:33:22 2014

@author: yanlanfei
"""
import collections
import copy

def mapNode(nodeList):
    dic={}
    nl=nodeList.nList
    for i in range(len(nl)):
        dic[nl[i].itemID]=i+1
    result=collections.OrderedDict(sorted(dic.items(),key=lambda t:t[1]))
    return result

def antiMapNode(index,nodeMap):
    for itemID in nodeMap.keys():
        if nodeMap[itemID]==index:
            return itemID
    
def buildST(nodeList,st,nodeMap):
    #change the itemID into the node so that we could easily get tht branches by using FPTree
    
    ST=[]#this is the bounded item list
    
    ST.extend(st)
    ST.sort()
    ST.reverse()
    
    cNode=nodeList.findNode(antiMapNode(ST[-1],nodeMap))
    branch=cNode.startPoint
    
    count=[]
    count.append([0,9999,2])
    k=ST[-1]
    for i in range(1,k+1):#initiate the count array
        count.append([i,0,0])
    
    for node in branch:
        pnode=node
        
        while pnode.itemID!="root":
            index=nodeMap[pnode.itemID]#get the index in count array
            count[index][1]=count[index][1]+node.supportCount
            pnode=pnode.parent
    
    for c in count:
        if count[-1][1]==c[1]:
            c[2]=1
    print "---st count---"
    for c in count:
        print "---"
        print c[0]
        print c[1]
        print c[2]
        print "---"
    print "---st count---"
    result=[branch,count,ST]
    return result
    
def Test(target,fci):
    if len(fci)==0:
        return True
    else:
        for f in fci:
            fEx=f[:-1]
            fCount=f[-1]
            
            targetEx=target[:-1]
            targetCount=target[-1]
            
            uf=set(fEx)
            ut=set(targetEx)
            
            utf=uf.union(ut)
            
            if utf==uf and targetCount<=fCount:
                return False
        return True
#            flag=1
#            for i in targetEx:
#                for j in fEx:
#                    if i==j:
#                        pass
#                    else:
#                        flag=0
#                        break
#                    
#            if flag==1:
#                if targetCount==fCount:
#                    return False
#                else:
#                    return True
#            else:
#                return True

def FPFCI(STTree,fci,threshold,nodeList,nodeMap,root):
    cnt=STTree[1]
    cntf=[]
    tST=STTree[2]
    tST.sort()
    tST.reverse()
    for i in cnt:#create the flaged node
        if i[2]==1 and i[0]!=tST[-1]:
            cntf.append(i[0])
    
    if len(cntf)==0:#if the flaged node array is empty,then the left node is the closed FP
        temp=copy.deepcopy(STTree[2])
        temp.append(cnt[tST[-1]][1])
        if Test(temp,fci):
            fci.append(temp)
    else:
        tST.extend(cntf)# union the nodes flagged,and check if it is the closed FP
        temp=copy.deepcopy(tST)
        temp.sort()
        temp.reverse()
        c=cnt[temp[-1]][1]
        temp.append(c)
        if Test(temp,fci):
            fci.append(temp)
    
    for j in range(tST[-1]-1,1,-1):
        if cnt[j][2]==1:#extend the ST
            tST.append(j)
        else:
            if cnt[j][1]>=threshold:
                print "i am tST"
                print tST
                temp=copy.deepcopy(tST)
                temp.append(j)
                temp.sort()
                temp.reverse()
                tc=cnt[j][1]
                
                temp.append(tc)
                print "i am temp"
                print temp
                if Test(temp,fci):                        
                    if root.findChild(antiMapNode(j,nodeMap))==None:
#                        print root.findChild(antiMapNode(j,nodeMap)).itemID
                        print " i am  the fucking path"
                        tempSTTree=[]
                        tb=STTree[0]
                        tcl=copy.deepcopy(STTree[1])
                        tcl.pop()
                        temp.pop()
                        tst=temp
                        
                        tempSTTree.append(tb)
                        tempSTTree.append(tcl)
                        tempSTTree.append(tst)
                        
                        for i in tcl:
                            if i[1]==tcl[-1][1]:
                                i[2]=1
                        FPFCI(tempSTTree,fci,threshold,nodeList,nodeMap,root)
                    else:
                        print "add [4,3,2]"
                        fci.append(temp)
    temp=copy.deepcopy(tST)
    temp.append(cnt[1][0])
    temp.append(cnt[1][1])
    if cnt[1][2]==0 and Test(temp,fci):
        fci.append(fci)
        
def FCI(nodeList,root,threshold):
    
    fci=[]
    nodeMap=mapNode(nodeList)
    for i in range(len(nodeMap),1,-1):
#        print "process index"+str(i)
#        print ""
        
        st=[]
        st.append(i)
        STTree=buildST(nodeList,st,nodeMap)
        
        if root.findChild(antiMapNode(i,nodeMap))==None:#process the node if it is not the root,or if it is the root, test it.
            FPFCI(STTree,fci,threshold,nodeList,nodeMap,root)
        else:
            ic=STTree[1][i][1]#get the count,[branch,count,ST],count=[index,count,flag]
            #print [i,ic]
            if Test([i,ic],fci):
                fci.append([i,ic])
            if root.findChild(antiMapNode(i,nodeMap)).supportCount!=STTree[1][i]:
                exNode=nodeList.findNode(antiMapNode(i,nodeMap))
                exNodeStartPoint=exNode.startPoint
                tempESP=[]                
                
                for esp in exNodeStartPoint:
                    if esp.parent.itemID=="root":
                        pass
                    else:
                        tempESP.append(esp)
                exNode.startPoint=tempESP
                STTree=buildST(nodeList,st,nodeMap)
                FPFCI(STTree,fci,threshold,nodeList,nodeMap,root)
            
    topNode=[nodeMap[nodeList.nList[0].itemID],nodeList.nList[0].supportCount]
    print fci
    if Test(topNode,fci):
        #test the top one 
        print "add the top"
        fci.append(topNode)
    return fci