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
        #self.tail = None

    def newVersion(self):
        self.version += 1

    # The operation search takes a version number v and an integer i as arguments and
    # returns the key of the ith element of the vth version
    def search(self, v, i):
        j = len(self.header) -1
        # follow pointer with largest version smaller than v
        while j >= 0:
            if self.header[j][0] <= v:
                x = self.header[j][1]
                break
            j += -1
        else:
            return None
        while i > 1:
            #find element in extra list with type next (True) and largest version smaller than v
            #if pointer is None, return None
            #follow pointer and decrement i
            x = self.newestNext(x, v)
            if x is None:
                return None
            i += -1
        return x

    # The operation insert takes a key k and an integer i as arguments, and insert the
    # key k as the new ith element in the list, i.e., between the (i − 1)st and ith element
    # of the current newest version.
    def insert(self, k, i):
        y = Node(k, self.version) 
        if i == 1:
            if len(self.header) > 0:
                y.next = self.header[-1][1]
            self.pointerUpdate(y)
        else:
            y.prev = self.search(self.version, i-1)
            y.next = self.newestNext(y.prev, self.version)
            self.pointerUpdate(y)
        return True
        
    # The operation update takes a key and an integer i as arguments, and updates the
    # key in the ith element to the given key in the newest version.
    def update(self, k, i):
        x = self.search(self.version, i)
        if x is None:
            return False
        if x.version == self.version:
            x.key = k
            return True
        copy = Node(k, self.version)
        x.copy = copy
        copy.prev = self.newestPrev(x, self.version)
        copy.next = self.newestNext(x, self.version)
        self.pointerUpdate(copy)
        return True

    ############# UTILITY FUNCTIONS #############
    def newestNext(self, x, v):
        j = len(x.extra) - 1
        while j >= 0:
            if x.extra[j][0] == True and x.extra[j][1] <= v:
                x = x.extra[j][2]
                return x
            j = j-1
        return x.next

    def newestPrev(self, x, v):
        j = len(x.extra) - 1
        while j >= 0:
            if x.extra[j][0] == False and x.extra[j][1] <= v:
                x = x.extra[j][2]
                return x
            j = j-1
        return x.prev
        
    # Recursively makes copy nodes to either left or right. a is the cause of the copying and 
    # isleft is a boolean which is true if a is supposed to be the newest next of the copy, false if newest previous
    def makecopy(self, original, isleft, a):
        copy = Node(original.key, self.version)
        original.copy = copy
        if isleft:
            copy.next = a
            copy.prev = self.newestPrev(original, self.version)
            if copy.prev is not None:
                if copy.prev.version == self.version:
                    copy.prev.next = copy
                elif len(copy.prev.extra) >= self.e:
                    copy.prev = self.makecopy(copy.prev, True, copy)
                else:
                    copy.prev.extra.append([True, self.version, copy])
            else:
                self.header.append([self.version, copy])
        else:
            copy.prev = a
            copy.next = newestNext(original, self.version)
            if copy.next is not None:
                if copy.next.version == self.version:
                    copy.next.prev = copy
                elif len(copy.next.extra) >= self.e:
                    copy.next = self.makecopy(copy.next, False, copy)
                else:
                    copy.next.extra.append([False, self.version, copy])
        return copy

    # Updates pointers of the previous and next nodes of a node.
    def pointerUpdate(self, y):
        if y.prev is not None:
            if y.prev.version == self.version:
                y.prev.next = y
            else:
                j = len(y.prev.extra) - 1
                while j >= 0:
                    if y.prev.extra[j][0] == True and y.prev.extra[j][1] <= self.version:
                        if y.prev.extra[j][1] == self.version:
                            y.prev.extra[j][2] = y
                            break
                        elif len(y.prev.extra) >= self.e:
                            y.prev = self.makecopy(y.prev, True, y)
                            break
                    j = j-1
                else:
                    y.prev.extra.append([True, self.version, y])
        else:
            #y is first element, and self.header should point to it
            if len(self.header) > 0 and self.header[-1][0] == self.version:
                self.header[-1][1] = y
            else:
                self.header.append([self.version, y])

        if y.next is not None:
            if y.next.version == self.version:
                y.next.prev = y
            else:
                j = len(y.next.extra) - 1
                while j >= 0:
                    if y.next.extra[j][0] == True and y.next.extra[j][1] <= self.version:
                        if y.next.extra[j][1] == self.version:
                            y.next.extra[j][2] = y
                            break
                        elif len(y.next.extra) >= self.e:
                            y.next = self.makecopy(y.next, False, y)
                            break
                    j = j-1
                else:
                    y.next.extra.append([False, self.version, y])
        
    def traverseList(self, version):
        i = 1
        result = ""
        while True:
            x = self.search(version, i)
            if x is None:
                break
            result += "-" + str(x.key)
            i += 1
        return result

    def countNodesInVersion(self, version):
        i = 1
        result = []
        while True:
            x = self.search(version, i)
            if x is None:
                break
            result.append((x.key, x.version))
            i += 1
        return result

    def countNodes(self):
        # IMPORTANT: this only works if all keys in the PPLL are distinct,
        # ie. if a key is an id for a node. 
        l = []
        for v in range(0, self.version+1):
            l.extend(self.countNodesInVersion(v))
        result = []
        for i in l:
            if i not in result:
                result.append(i)
        return len(result)


if __name__ == "__main__":
    #handle input and run functions
    e = 2
    ll = LinkedList(e)

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
            result = ll.update(int(l[1]), int(l[2]))
            if result:
                print("S")
                #print("S - comparisons used:",comparisoncounter)
            else:
                print("F")
                #print("F - comparisons used:",comparisoncounter)
        elif l[0] == "S":
            result = ll.search(int(l[1]), int(l[2]))
            if result is not None:
                print("S - value:",result.key )
                #print("S - comparisons used:",comparisoncounter)
            else:
                print("F")
                #print("F - comparisons used:",comparisoncounter)
        elif l[0] == "N":
            result = ll.newVersion()
            print("S")
        elif l[0] == "V":
            print(ll.version)
        elif l[0] == "T":
            print(ll.traverseList(int(l[1])))
        elif l[0] == "TA":
            for i in range(0, ll.version+1):
                print("Version:", i, "list:", ll.traverseList(i))
        elif l[0] == "C":
            result = ll.countNodes()
            print("unique nodes in PPLL:", result)
        else:
            break


