#!/usr/bin/env python
#Partially Persistent Doubly-Linked Lists
import sys
size = 0
space = 0

class Node(object):
    def __init__(self, key, version):
        global size
        global space
        size += 1
        space += 5
        self.key = key
        self.next = None
        self.prev = None
        
        self.version = version
        self.extra = []



class LinkedList(object):
    def __init__(self, e):
        global space
        space += 3
        self.header = []
        self.version = 0
        self.e = e

    def newVersion(self):
        self.version += 1

    def search(self, v, i):
        j = len(self.header) -1
        while j >= 0:
            if self.header[j][0] <= v:
                x = self.header[j][1]
                break
            j += -1
        else:
            return None
        while i > 1:
            x = self.newestNext(x, v)
            if x is None:
                return None
            i += -1
        return x

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
        
    def update(self, k, i):
        x = self.search(self.version, i)
        if x is None:
            return False
        if x.version == self.version:
            x.key = k
            return True
        copy = Node(k, self.version)
        #x.copy = copy
        copy.prev = self.newestPrev(x, self.version)
        copy.next = self.newestNext(x, self.version)
        self.pointerUpdate(copy)
        return True

    ############# UTILITY FUNCTIONS #############
    def newestNext(self, x, v):
        j = len(x.extra) - 1
        while j >= 0:
            if x.extra[j][0] == True and x.extra[j][1] <= v:
                return x.extra[j][2]
            j = j-1
        return x.next

    def newestPrev(self, x, v):
        j = len(x.extra) - 1
        while j >= 0:
            if x.extra[j][0] == False and x.extra[j][1] <= v:
                return x.extra[j][2]
            j = j-1
        return x.prev
        
    def makecopy(self, original, isleft, a):
        global space
        copy = Node(original.key, self.version)
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
                    space += 1
            else:
                self.header.append([self.version, copy])
                space += 1
        else:
            copy.prev = a
            copy.next = self.newestNext(original, self.version)
            if copy.next is not None:
                if copy.next.version == self.version:
                    copy.next.prev = copy
                elif len(copy.next.extra) >= self.e:
                    copy.next = self.makecopy(copy.next, False, copy)
                else:
                    copy.next.extra.append([False, self.version, copy])
                    space += 1

        return copy


    # Updates pointers of the previous and next nodes of a node.
    def pointerUpdate(self, y):
        global space
        if y.prev is not None:
            if y.prev.version == self.version:
                y.prev.next = y
            else:
                j = len(y.prev.extra) - 1
                while j >= 0:
                    if y.prev.extra[j][0] == True:
                        if y.prev.extra[j][1] == self.version:
                            y.prev.extra[j][2] = y
                            break
                    j = j-1
                else:
                    if len(y.prev.extra)>self.e:
                        y.prev = self.makecopy(y.prev, True, y)
                    else:
                        y.prev.extra.append([True, self.version, y])
                        space += 1
        else:
            if len(self.header) > 0 and self.header[-1][0] == self.version:
                self.header[-1][1] = y
            else:
                self.header.append([self.version, y])
                space += 1

        if y.next is not None:
            if y.next.version == self.version:
                y.next.prev = y
            else:
                j = len(y.next.extra) - 1
                while j >= 0:
                    if y.next.extra[j][0] == False:
                        if y.next.extra[j][1] == self.version:
                            y.next.extra[j][2] = y
                            break
                    j = j-1
                else:
                    if len(y.next.extra)>self.e:
                        y.next = self.makecopy(y.next, False, y)
                    else:
                        y.next.extra.append([False, self.version, y])
                        space += 1
        
    def traverseList(self, version):
        result = ""
        j = len(self.header) -1
        while j >= 0:
            if self.header[j][0] <= version:
                x = self.header[j][1]
                result += "-" + str(x.key)
                break
            j += -1
        else:
            return result
        while True:
            x = self.newestNext(x, version)
            if x is None:
                return result
            result += "-" + str(x.key)


if __name__ == "__main__":
    #handle input and run functions
    e = 2
    if len(sys.argv)>1:
        e = int(sys.argv[1])
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
            else:
                print("F")
        elif l[0] == "U":
            result = ll.update(int(l[1]), int(l[2]))
            if result:
                print("S")
            else:
                print("F")
        elif l[0] == "S":
            result = ll.search(int(l[1]), int(l[2]))
            if result is not None:
                print("S - value:",result.key )
            else:
                print("F")
        elif l[0] == "N":
            ll.newVersion()
            print("S")
        elif l[0] == "V":
            print(ll.version)
        elif l[0] == "T":
            print(ll.traverseList(int(l[1])))
        elif l[0] == "TA":
            for i in range(0, ll.version+1):
                print("Version:", i, "list:", ll.traverseList(i))
        elif l[0] == "C":
            if l[1] == "N":
                print("nodes:", size)
            elif l[1] == "S":
                print("space used:", space)

        else:
            break


