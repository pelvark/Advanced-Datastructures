#!/usr/bin/env python

class Node(object):
    def __init__(self, key):
        #Initiate an empty node in the tree
        self.key = key

        self.left = None
        self.right = None
        self.brother = None

        self.size = 0
        self.height = 0
        self.depth = 0


    

class ScapegoatTree(object):
    def __init__(self):
        #initiate a new scapegoat tree
        self.root = None
        self.size = 0
        self.max_size = 0


    def insert(self, key):
        self.updateSize(1)
        z = Node(key)
        y = None
        x = self.root
        while x is not None:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        if y == None:
            self.root = z
        elif x == y.right:
            y.right = z
            z.brother = y.left
        else:
            y.left = z
            z.brother = y.right
        

    

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

    




if __name__ == "__main__":
    #handle input and run functions
