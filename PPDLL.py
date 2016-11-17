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

    def search(self, v, i):
        if len(self.header)>0:
            # follow pointer with largest version smaller than v
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
            x = self.header[-1]
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
    pass
