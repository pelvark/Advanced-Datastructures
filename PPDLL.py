#!/usr/bin/env python
#Partially Persistent Doubly-Linked Lists
import sys

class Node(object):
    def __init__(self, key, version):
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
            x = self.newestNext(x, v)
            if x is None:
                return None
            i = i-1

        return x

    # The operation insert takes a key k and an integer i as arguments, and insert the
    # key k as the new ith element in the list, i.e., between the (i − 1)st and ith element
    # of the current newest version.
    def insert(self, k, i):
        if i == 1:

        else:
            x = self.search(self.version, i-1)
        z = self.newestNext(x, self.version) 
        #now x the element at index i-1, it's newest next pointer points to z
        # insert node
        y = Node(k, self.version) 
        y.prev = x
        y.next = z
        #if z is None, insert the point as tail.
        if z is None:
            pass
        else:
            if len(x.extra) >= self.e:
                # make copy node of x
                # set extra pointer (next) of x copy to y
                # set previous pointer of y to x copy
                pass

            else:
                x.extra.append((True, self.version, y))


            if len(z.extra) >= self.e:
                # make copy node of z
                # set extra pointer (prev) of z copy to y
                # set next pointer of y to z copy
                pass
            else:
                z.extra.append((False, self.version, y))
        #if x or z has a full extra list, then a copy node must be made 
        #  copy of x should have most recent extra previous pointer of x, and have a next pointer to new node
        #  same with z but previous and next swapped
        #else   
        #  add extra next pointer in x to new node and extra previous pointer in z to new node
        

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
        


    def newestNext(self, x, v):
        flag = False
        j = len(x.extra) - 1
        while j >= 0:
            if x.extra[j][0] == True and x.extra[j][1] <= v:
                x = x.extra[j][2]
                flag = True
                break
            j = j-1
        
        if flag:
            return x

        if x.next is not None:
            return x.next
        else:
            return None

    def newestPrev(self, x, v):
        flag = False
        j = len(x.extra) - 1
        while j >= 0:
            if x.extra[j][0] == False and x.extra[j][1] <= v:
                x = x.extra[j][2]
                flag = True
                break
            j = j-1
        
        if flag:
            return x

        if x.prev is not None:
            return x.prev
        else:
            return None
        

    def makecopy(self, original, isleft, a):
        copy = Node(original.key, self.version)
        if isleft:
            copy.next = a
            prev = newestPrev(original, self.version)
            if len(prev.extra) >= self.e:
                recopy = self.makecopy(prev, True, copy)
                copy.prev = recopy
            else:
                prev.extra.append((True, self.version, copy))
        else:
            copy.prev = a
            next = newestPrev(original, self.version)
            if len(next.extra) >= self.e:
                recopy = self.makecopy(next, True, copy)
                copy.next = recopy
            else:
                prev.extra.append((False, self.version, copy))

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


