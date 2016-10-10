#!/usr/bin/env python
import math 
import fileinput

class Node(object):
    def __init__(self, key):
        #Initiate an empty node in the tree
        self.key = key

        self.left = None
        self.right = None


    def size(self):
        if self.left is not None and self.right is not None:
            return self.left.size() + self.right.size + 1
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

        #TODO: FIX THIS
        #flatten
        l = self.flatten()
        #rebuild
        return self.rebuildFromList(l)


    def flatten(self):
        #flatten tree to list
        l = []
        if self.left is not None:
            l.extend(self.left.flatten())
        l.append(self)
        if self.right is not None:
            l.extend(self.right.flatten())
        return l
    
    def rebuildFromList(self, l):
        length = len(l)
        if length == 1:
            l[0].left = None
            l[0].right = None
            return l[0]
        elif length == 2:
            l[0].left = None
            l[0].right = None
            l[1].left = l[0]
            l[1].right = None
            return l[1]
        else:
            l[math.floor(length/2)].left = self.rebuildFromList(l[0:math.floor(length/2)])
            l[math.floor(length/2)].right = self.rebuildFromList(l[math.floor(length/2)+1:length])
            return l[math.floor(length/2)]


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
                x = x.left
                depth +=1
            elif key > x.key:
                x = x.right
                depth +=1
            else:
                return False
        if len(ancestorList) == 0:
            self.root = z
        elif key > y.key:
            ancestorList[-1].right = z
        else:
            ancestorList[-1].left = z
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
                    break
                previousCandidate = candidate
        return True

                
    
    def delete(self, key):
        y = None
        x = self.root
        while x is not None:
            if key < x.key:
                y = x
                x = x.left
            elif key > x.key:
                y = x
                x = x.right
            elif key == x.key:
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
        x = self.root
        while x is not None:
            if key < x.key:
                x = x.left
            elif key == x.key:
                return True
            else:
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
    tree = ScapegoatTree(alpha)
    for line in fileinput.input():
        l = line.split()
        print ("Command: " + line)
        if l[0] == "I":
            result = tree.insert(int(l[1]))
            if result:
                print("S")
            else:
                print("F")
        elif l[0] == "D":
            result = tree.delete(int(l[1]))
            if result:
                print("S")
            else:
                print("F")
        elif l[0] == "S":
            result = tree.search(int(l[1]))
            if result:
                print("S")
            else:
                print("F")
        else:
            print("ERROR: something other than I S or D was input")

        print("Tree so far:")
        tree.printTree()
        print()



