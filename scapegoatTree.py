#!/usr/bin/env python
import sys
import math 
comparisoncounter = 0
rebuildsize = 0

class Node(object):
    def __init__(self, key):
        #Initiate an empty node in the tree
        self.key = key

        self.left = None
        self.right = None


    def size(self):
        if self.left is not None and self.right is not None:
            return self.left.size() + self.right.size() + 1
        elif self.left is not None:
            return self.left.size() + 1
        elif self.right is not None:
            return self.right.size() + 1
        else:
            return 1

    def sizeGivenChildSize(self, childSize, isLeftChild):
        if isLeftChild:
            if self.right is None:
                return childSize + 1
            else:
                return childSize + self.right.size() + 1
        else:
            if self.left is None:
                return childSize + 1
            else:
                return childSize + self.left.size() + 1
            

    def rebuildTree(self):
        #flatten
        l = self.flatten()
        global rebuildsize
        rebuildsize = len(l)
        #rebuild
        self.rebuildFromList(l,0,len(l)-1)


    def flatten(self):
        #flatten tree to list
        l = []
        if self.left is not None:
            l.extend(self.left.flatten())
        l.append(self)
        if self.right is not None:
            l.extend(self.right.flatten())
        return l
    
    def rebuildFromList(self, l, i, j):
        length = len(l)
        if i==j:
            l[0].left = None
            l[0].right = None
            return l[0]
        elif i+1==j:
            l[0].left = None
            l[0].right = None
            l[1].left = l[0]
            l[1].right = None
            return l[1]
        else:
            mid = math.floor((i+j)/2)
            l[mid].left = self.rebuildFromList(l, i, mid-1)
            l[mid].right = self.rebuildFromList(l, mid+1, j)
            return l[mid]


    def traverse(self):
        if self.left is not None:
            self.left.traverse()
        if self is not None:
            print(self.key, end="-")
        if self.right is not None:
            self.right.traverse()
        


class ScapegoatTree(object):
    def __init__(self, alpha):
        #initiate a new scapegoat tree
        self.root = None
        self.size = 0
        self.maxSize = 0
        self.alpha = alpha


    def insert(self, key):
        global comparisoncounter 
        ancestorList = []
        self.updateSize(1)
        depth = 0
        z = Node(key)
        y = None
        x = self.root
        while x is not None:
            ancestorList.append(x)
            y = x
            if key < x.key:
                comparisoncounter += 1
                x = x.left
                depth +=1
            elif key > x.key:
                comparisoncounter += 1
                x = x.right
                depth +=1
            else:
                comparisoncounter += 1
                return False
        if len(ancestorList) == 0:
            self.root = z
        elif key > y.key:
            y.right = z
        else:
            y.left = z
        #check deepness of node inserted
        if self.isDeepNode(depth):
            # find scapegoat node
            size = 0
            previousCandidate = x
            height = 0
            for candidate in reversed(ancestorList):
                height += 1
                isLeftChild = (candidate.left == previousCandidate)
                size = candidate.sizeGivenChildSize(size, isLeftChild)
                if size != 0 and height > math.log(size, 1/self.alpha):
                    # candidate is scapegoat node
                    candidate.rebuildTree()
                    return True
                previousCandidate = candidate
        return True

                
    
    def delete(self, key):
        global comparisoncounter 
        y = None
        x = self.root
        while x is not None:
            if key < x.key:
                comparisoncounter += 1
                y = x
                x = x.left
            elif key > x.key:
                comparisoncounter += 1
                y = x
                x = x.right
            elif key == x.key:
                comparisoncounter += 1
                if y is not None and x == y.left:
                    if x.left is None:
                        y.left = x.right
                    elif x.right is None:
                        y.left = x.left
                    else:
                        z, zparent = self.findSuccessorAndParent(x)            
                        if z == zparent.left:
                            zparent.left = z.right
                        else:
                            zparent.right = z.right
                        y.left = z
                        z.left = x.left
                        z.right = x.right
                if y is not None and x == y.right:
                    if x.left is None:
                        y.right = x.right
                    elif x.right is None:
                        y.right = x.left
                    else:
                        z, zparent = self.findSuccessorAndParent(x)            
                        if z == zparent.left:
                            zparent.left = z.right
                        else:
                            zparent.right = z.right
                        y.right = z
                        z.left = x.left
                        z.right = x.right
                self.updateSize(-1)
                #check whether too many nodes have been deleted.
                if self.isTimeForRebuild():
                    #rebuild tree
                    self.root = self.root.rebuildTree()
                return True
        return False



    def search(self,key):
        global comparisoncounter 
        x = self.root
        while x is not None:
            if key < x.key:
                comparisoncounter += 1
                x = x.left
            elif key == x.key:
                comparisoncounter += 1
                return True
            else:
                comparisoncounter += 1
                x = x.right
        return False




    # extra functions
    def updateSize(self, x):
        self.size = self.size + x
        if self.size > self.maxSize:
            self.maxSize = self.size


    def findSuccessorAndParent(self, x):
        y = x
        x = x.right
        while x.left is not None:
            y = x
            x = x.left
        return x, y

    def isDeepNode(self, depth):
        if depth > math.floor(math.log(self.size, 1/self.alpha)):
            return True
        else: 
            return False


    def isTimeForRebuild(self):
        return self.size < self.alpha*self.maxSize

    
    def printTree(self):
        if self.root is not None:
            self.root.traverse()




if __name__ == "__main__":
    #handle input and run functions
    alpha = 0.75
    if len(sys.argv)>1:
        alpha = float(sys.argv[1])
        if 0<alpha<1:
            pass
        else:
            print("You tried to set p to something not between 0 and 1. I set it to 0.75 intead")
            p = 0.75

    tree = ScapegoatTree(alpha)
    while True:
        line = sys.stdin.readline()
        comparisoncounter = 0
        rebuildsize = 0
        l = line.split()
        if len(l)==0:
            break
        if l[0] == "I":
            result = tree.insert(int(l[1]))
            if result:
                print("S - comparisons used:", comparisoncounter, "rebuildsize:", rebuildsize)
            else:
                print("F - comparisons used:",comparisoncounter)
        elif l[0] == "D":
            result = tree.delete(int(l[1]))
            if result:
                print("S - comparisons used:",comparisoncounter)
            else:
                print("F - comparisons used:",comparisoncounter)
        elif l[0] == "S":
            result = tree.search(int(l[1]))
            if result:
                print("S - comparisons used:",comparisoncounter)
            else:
                print("F - comparisons used:",comparisoncounter)
        else:
            break



