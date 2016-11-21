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
        self.extra = []



class LinkedList(object):
    def __init__(self, e):
        self.header = []
        self.version = 0
        self.e = e
        #tail in the newest version
        self.tail = None

    def newversion(self):
        self.version += 1

    # The operation search takes a version number v and an integer i as arguments and
    # returns the key of the ith element of the vth version
    def search(self, v, i):
        flag = False
        j = len(self.header)
        # follow pointer with largest version smaller than v
        while j > 0:
            if self.header[j][0] <= v:
                x = self.header[j][1]
                break
        else:
            return False
        while i > 1:
            #find element in extra list with type next (True) and largest version smaller than v
            #if pointer is None, return None
            #follow pointer and decrement i
            j = len(x.extra) - 1
            while j >= 0:
                if x.extra[j][0] == True and x.extra[j][1] <= v:
                    x = x.extra[j][2]
                    i = i-1
                    flag = True
                    break
                    # continue outer loop
                j = j-1
            
            if flag:
                flag = False
                continue

            if x.next is not None:
                x = x.next
                i = i-1
            else:
                return None

        return x

    # The operation insert takes a key k and an integer i as arguments, and insert the
    # key k as the new ith element in the list, i.e., between the (i − 1)st and ith element
    # of the current newest version.
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

    # The operation update takes a key and an integer i as arguments, and updates the
    # key in the ith element to the given key in the newest version.
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


