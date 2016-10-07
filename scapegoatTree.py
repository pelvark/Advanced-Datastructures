#!/usr/bin/env python
import math 

class Node(object):
    def __init__(self, key):
        #Initiate an empty node in the tree
        self.key = key

        self.left = None
        self.right = None


    def size(self):
        if self.left is not None and self.right is not None:
            return self.left.size() + self.right.size + 2
        elif self.left is not None:
            return self.left.size() + 1
        elif self.right is not None:
            return self.right.size() + 1
        else:
            return 0

    def sizeGivenChildSize(self, childSize, isLeftChild):
        if isLeftChild:
            if self.right is None:
                return childSize + 1
            else:
                return childSize + self.right.size()
        else:
            if self.left is None:
                return childSize + 1
            else:
                return childSize + self.left.size()
            

    def rebuildTree(self):

        #flatten
        l = self.flatten()
        #rebuild
        self.rebuildFromList(l)


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
        #rebuild a tree from list
        ## Idea so far: recursive build tree from list l[(0:math.floor(l.size()/2)-1)]
        ## recursive build tree from list l[(math.floor(l.size()/2)+1:n-1)]
        ## link those two as left and right subtree on self 
        ## remember to check for leaf case.

        left = math.floor(l.size()/2)-1
        right = math.floor(l.size()/2)+1
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
            else:
                x = x.right
                depth +=1
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
                # TODO: Fix that size can be 0
                print(size)
                if size != 0 and height > math.log(size, 1/self.alpha):
                    # candidate is scapegoat node
                    candidate.rebuildTree()
                    break
                previousCandidate = candidate

                
    
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
                if x == y.left:
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
                if x == y.right:
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
            self.root.rebuildTree()



    def search(self,key):
        x = self.root
        while x is not None:
            if key < x.key:
                x = x.left
            elif key == x.key:
                return True
                return x
            else:
                x = x.right
        return False
        return None




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

    




if __name__ == "__main__":
    #handle input and run functions
    pass
