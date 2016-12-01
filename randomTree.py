#!/usr/bin/env python
#random trees
import sys
import random
size = 0
depthsum = 0


class Node(object):
    def __init__(self, key):
        self.key = key
        self.priority = random.randrange(1,2**30)
        self.left = None
        self.right = None



class RandomTree(object):
    def __init__(self):
        self.root = None



    def search(self, key):
        x = self.root
        while x is not None:
            if key < x.key:
                x = x.left
            elif key == x.key:
                return x
            else:
                x = x.right
        return None

    def insert(self, key):
        z = Node(key)
        ancestorList = []
        x = self.root
        while x is not None:
            ancestorList.append(x)
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return False
        if len(ancestorList) == 0:
            self.root = z
            return True
        y = ancestorList.pop()
        if key < y.key:
            y.left = z
        else:
            y.right = z

        while z.priority < y.priority:
            if z == y.left:
                #right rotation
                y.left = z.right
                z.right = y
                if len(ancestorList) > 0:
                    temp_y = y
                    y = ancestorList.pop()
                    if y.left == temp_y:
                        y.left = z
                    else:
                        y.right = z
                else: 
                    self.root = z
                    break
            elif z == y.right:
                #left rotation
                y.right = z.left
                z.left = y
                if len(ancestorList) > 0:
                    temp_y = y
                    y = ancestorList.pop()
                    if y.left == temp_y:
                        y.left = z
                    else:
                        y.right = z
                else: 
                    self.root = z
                    break
            else: 
                print("ERROR: z not y's child")
        return True


    def split(self, k):
        z = Node(key)
        z.priority = 0
        check = self.insert(z)
        if not check:
            return None, None
        return self.root.left, self.root.right


    def merge(self, a, b):
        if a.priority < b.priority:
            if a.right is not None:
                a.right = self.merge(a.right, b)
            else:
                a.right = b
        else:
            if b.left is not None:
                b.left = self.merge(a, b.left)
            else:
                b.left = a


    def delete(self, key):
        y = None
        x = self.root
        while x is not None:
            if key < x.key:
                y = x
                x = x.left
            elif key == x.key:
                break
            else:
                y = x
                x = x.right
        if x is None:
            return False
        if x == self.root:
            rootDeletion = True
        else:
            rootDeletion = False
        if x.left is not None and x.right is not None:
            z = self.merge(x.left, x.right)
            if rootDeletion:
                self.root = z
            elif x == y.left:
                y.left = z
            else:
                y.right = z
        elif x.left is not None:
            if rootDeletion:
                self.root = x.left
            elif x == y.left:
                y.left = x.left
            else:
                y.right = x.left
        elif x.right is not None:
            if rootDeletion:
                self.root = x.right
            elif x == y.left:
                y.left = x.right
            else:
                y.right = x.right
        else:
            if rootDeletion:
                self.root = None
            elif x == y.left:
                y.left = None
            else:
                y.right = None
        return True

    def traverse(self, x, printdepth, depth=1):
        global size 
        global depthsum
        depthsum += depth
        size += 1
        if x.left is not None:
            self.traverse(x.left, printdepth, depth+1)
        if printdepth:
            print("key:", x.key, "|", "depth:", depth)
        if x.right is not None:
            self.traverse(x.right, printdepth, depth+1)




if __name__ == "__main__":
    #handle input and run functions
    tree = RandomTree()

    while True:
        line = sys.stdin.readline()
        l = line.split()
        if len(l)==0:
            break
        if l[0] == "I":
            result = tree.insert(int(l[1]))
            if result:
                print("S")
                #print("S - comparisons used:", comparisoncounter, "rebuildsize:", rebuildsize)
            else:
                print("F")
                #print("F - comparisons used:",comparisoncounter)
        elif l[0] == "D":
            result = tree.delete(int(l[1]))
            if result:
                print("S")
                #print("S - comparisons used:",comparisoncounter)
            else:
                print("F")
                #print("F - comparisons used:",comparisoncounter)
        elif l[0] == "S":
            result = tree.search(int(l[1]))
            if result is not None:
                print("S")
                #print("S - comparisons used:",comparisoncounter)
            else:
                print("F")
                #print("F - comparisons used:",comparisoncounter)
        elif l[0] == "M":
            result1, result2 = tree.split(int(l[1]))
            if result1 is not None or result2 is not None:
                tree.delete(int(l[1]))
                print("S")
            else:
                if self.root.priority == 0:
                    tree.delete(int(l[1]))
                    print("F - error, or tree was empty")
                else:
                    print("F - key chosen possibly already in tree")
        elif l[0] == "T":
            depthsum = 0
            size = 0
            if l[1] == "D":
                tree.traverse(tree.root, True)
            elif l[1] == "A":
                tree.traverse(tree.root, False)
                print("average depth of nodes:", depthsum/size)
        else:
            break



