#!/usr/bin/python

from __future__ import division
import numpy as np
import sys

class Node(object):
    def __init__(self, data, i):
        self.data = data
        self.indx = i

class hashTable:
    def __init__(self,p):
        self.p = p
        self.hashList = [[] for i in range(p)]

    def insert(self,i, bh):
        flag, indx = self.find(i)
        if flag == False:
            node = Node(i,bh.currentSize+1)
            hashValue = i%self.p
            self.hashList[hashValue].append(node)
            bh.insert(node)
        else:
            print "error : item already exists"


    def find(self, i):
        hashValue = i%self.p
        sublist = self.hashList[hashValue]
        for indx in range(len(sublist)):
            if sublist[indx].data == i:
                return True, indx

        return False, None

    def deli(self,i,bh):
        flag, loc = self.find(i)
        if flag==True:
            hashValue = i%self.p
            locHeap = self.hashList[hashValue][loc].indx
            bh.deli(locHeap)
            self.hashList[hashValue].pop(loc)
        else:
            print "error : item not present"





class HeapImplement:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i].data > self.heapList[i // 2].data:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i // 2].indx = i//2

                self.heapList[i] = tmp
                self.heapList[i].indx = i 
            i = i // 2

    def insert(self,node):
        self.currentSize = self.currentSize + 1
        self.heapList.append(node)
        self.percUp(self.currentSize)

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i].data < self.heapList[mc].data:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[i].indx = i

                self.heapList[mc] = tmp
                self.heapList[mc].indx = mc
            i = mc

    def maxChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2].data < self.heapList[i*2+1].data:
                return i * 2 + 1
            else:
                return i * 2

    def deli(self,i):
        if self.heapList[-1].data > self.heapList[i].data:
            self.heapList[i] = self.heapList[-1]
            self.heapList[i].indx = i
            self.heapList.pop()
            self.currentSize = self.currentSize - 1
            self.percUp(i)
        elif self.heapList[-1].data < self.heapList[i].data:
            self.heapList[i] = self.heapList[-1]
            self.heapList[i].indx = i
            self.heapList.pop()
            self.currentSize = self.currentSize - 1
            self.percDown(i)
        elif self.heapList[-1].data == self.heapList[i].data:
            self.heapList.pop()
            self.currentSize = self.currentSize - 1


    def delMax(self, ht):
        if self.currentSize>0:
            maxval = self.heapList[1].data
            self.heapList[1] = self.heapList[self.currentSize]
            self.heapList[1].indx = 1
            self.currentSize = self.currentSize - 1
            self.heapList.pop()
            self.percDown(1)
            
            flag, loc = ht.find(maxval)
            hashValue = maxval%ht.p
            ht.hashList[hashValue].pop(loc)
            
            return maxval

        
def lookup(num,ht):
    flag, indx = ht.find(num)
    if flag == True:
        print "found "+str(num)
    else:
        print str(num)+" not found"


if __name__=='__main__':

    inputFile = sys.argv[1]
    dataFile = open(inputFile,'r').read().split('\n')
    
    p = int(dataFile[0])
    
    operations = int(dataFile[1])
    dataFile.pop(0)
    dataFile.pop(0)

    ht = hashTable(p)
    bh = HeapImplement()

    for i in range(operations-1):
        data = dataFile[i].split()      
        if data[0]=='insert':
            ht.insert(int(data[1]),bh)
        elif data[0]=='delete':
            ht.deli(int(data[1]),bh)
        elif data[0] == 'deleteMax':
            maxvalue =  bh.delMax(ht)
            if maxvalue is None:
                print "error"
            else:
                print maxvalue
        elif data[0] == 'lookup':
            lookup(int(data[1]),ht)
        

    # print all the elements in decreasing order 
    if bh.currentSize==0:
        print " "
    else:
        for i in range(1,bh.currentSize+1):
            print bh.delMax(ht),

