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
            return self.left.size()+self.right.size+1
        elif self.left is not None:
            return self.left.size()
        elif self.right is not None:
            return self.right.size()
        else:
            return 1

    def rebuildTree(self):

        #flatten

        #rebuild

    def flatten(self):
        #flatten tree to list
        l = []
        if self.left is not None:
            l.extend(self.left.flatten())
        l.extend(self)
        if self.right is not None:
            l.extend(self.right.flatten())
        return l
    
    def rebuildFromList(self, l):
        #rebuild a tree from list
        ## Idea so far: recursive build tree from list l[(0:math.floor(l.size()/2)-1)]
        ## recursive build tree from list l[(math.floor(l.size()/2)+1:n-1)]
        ## link those two as left and right subtree on self 
        ## remember to check for leaf case.



class ScapegoatTree(object):
    def __init__(self, alpha):
        #initiate a new scapegoat tree
        self.root = None
        self.size = 0
        self.max_size = 0
        self.alpha = alpha


    def insert(self, key):
        self.updateSize(1)
        depth = 0
        z = Node(key)
        y = None
        x = self.root
        while x is not None:
            y = x
            if key < x.key:
                x = x.left
                depth +=1
            else:
                x = x.right
                depth +=1
        if y == None:
            self.root = z
        elif x == y.right:
            y.right = z
        else:
            y.left = z
        #check deepness of node inserted
        if self.isDeepNode(depth):
            #rebalance tree

    

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

        return None



    def search(self,key):
        x = self.root
        while x is not None:
            if key < x.key:
                x = x.left
            elif key == x.key:
                return x
            else:
                x = x.right
        return None




    # extra functions
    def updateSize(self, x):
        self.size = self.size + x
        if self.size > self.max_size
            self.max_size = self.size


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
        return self.size < self.alpha*self.max_size

    




if __name__ == "__main__":
    #handle input and run functions
