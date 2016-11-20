#!/usr/bin/env python
#Partially Persistent Doubly-Linked Lists
import sys

class Node(object):
    def __init__(self, key, version, e):
        self.key = key
        self.next = None
        self.prev = None
        
        self.version = version
        self.copy = None
        self.extra = [None]*e



class LinkedList(object):
    def __init__(self):
        self.header = []
        self.version = 0

    def newversion(self):
        self.version += 1

    # The operation search takes a version number v and an integer i as arguments and
    # returns the key of the ith element of the vth version
    def search(self, v, i):
        j = len(self.header)
        # follow pointer with largest version smaller than v
        while j > 0:
            if self.header[j][0] <= v:
                x = self.header[j][1]
                break
        else:
            return False
        while i>0:
            #find element in extra list with largest version smaller than v
            #if pointer is None, return false
            #follow pointer and decrement i
            

    def insert(self, k, i):
        if i == 1:
            
            # Then the element is placed first and a pointer is added to self.header
        elif len(self.header)>0:
            x = self.header[-1][1]
        else: 
            return False
        while i>1:
            #find element in extra list with largest version smaller than current version
            #if pointer is None, return false
            #follow pointer and decrement i
        #now x the element at index i-1, it's newest next pointer points to y
        #if y is None, insert the point as tail.
        #if x or y has a full extra list, then a copy node must be made 
        #  copy of x should have most recent extra previous pointer of x, and have a next pointer to new node
        #  same with y but previous and next swapped
        #else   
        #  add extra next pointer in x to new node and extra previous pointer in y to new node
        #  

    def update(self, k, i):
        elif len(self.header)>0:
            x = self.header[-1]
        else: 
            return False
        while i>1:
            #find element in extra list with largest version smaller than current version
            #if pointer is None, return false
            #follow pointer and decrement i
        




if __name__ == "__main__":
    #handle input and run functions
    ll = LinkedList()

    while True:
        line = sys.stdin.readline()
        l = line.split()
        if len(l)==0:
            break
        if l[0] == "I":
            result = ll.insert(int(l[1]), int(l[2]))
            if result:
                print("S")
                #print("S - comparisons used:", comparisoncounter, "rebuildsize:", rebuildsize)
            else:
                print("F")
                #print("F - comparisons used:",comparisoncounter)
        elif l[0] == "U":
            result = tree.update(int(l[1]), int(l[2]))
            if result:
                print("S")
                #print("S - comparisons used:",comparisoncounter)
            else:
                print("F")
                #print("F - comparisons used:",comparisoncounter)
        elif l[0] == "S":
            result = ll.search(int(l[1]), int(l[2]))
            if result is not None:
                print("S")
                #print("S - comparisons used:",comparisoncounter)
            else:
                print("F")
                #print("F - comparisons used:",comparisoncounter)
        elif l[0] == "N":
            result = ll.newversion
            print("S")
        else:
            break


