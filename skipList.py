#!/usr/bin/env python
import sys
import fileinput
import random
import math

comparisoncounter = 0

class Node(object):
    def __init__(self, key):
        #init
        self.key = key
        self.level = self.randomLevel()
        self.pointers = []


    def randomLevel(self):
        # determine the highest possible level of a node
        # should be changed to a formula with some probability.
        level = 1
        while random.random() < p and level < 32:
            level += 1
        return level


class SkipList(object):
    def __init__(self, p):
        #init
        self.head = Node(None)
        self.head.level = 32
        self.tail = Node(float("inf"))
        self.head.pointers.append(self.tail)
        self.maxLevel = 1
        self.size = 0
        self.p = p

    
    def insert(self, key):
        # insert a node with key 
        global comparisoncounter
        update = []
        x = self.head
        for i in range(self.maxLevel,0,-1):
            while len(x.pointers) >= i and x.pointers[i-1].key < key:
                comparisoncounter += 1
                x = x.pointers[i-1]
            comparisoncounter += 1
            update.append(x)
        x = x.pointers[0]
        if x.key == key:
            return False
            # key already in list
        else:
            x = Node(key)
            for i in range(0,min(x.level, self.maxLevel)):
                previousnode = update.pop()
                x.pointers.append(previousnode.pointers[i])
                previousnode.pointers[i] = x
            self.size += 1
            if self.sizeTooBig():
                self.increaseMaxLevel()
            return True
        return False


    def delete(self, key):
        global comparisoncounter
        update = []
        x = self.head
        for i in range(self.maxLevel,0,-1):
            while len(x.pointers) >= i and x.pointers[i-1].key < key:
                comparisoncounter += 1
                x = x.pointers[i-1]
            comparisoncounter += 1
            update.append(x)
        x = x.pointers[i-1]
        if x.key == key:
            for i in range(0,min(x.level, self.maxLevel)):            
                previousnode = update.pop()
                previousnode.pointers[i] = x.pointers[i]
            self.size += -1
            if self.sizeTooSmall():
                self.decreaseMaxLevel()
            return True
        else:
            return False



    def search(self, key):
        global comparisoncounter
        x = self.head
        for i in range(self.maxLevel,0,-1):
            while len(x.pointers) >= i and x.pointers[i-1].key < key:
                comparisoncounter += 1
                x = x.pointers[i-1]
            comparisoncounter += 1
        if len(x.pointers) > 0 and x.pointers[0].key == key:
            return True
        else:
            return False

    

    #Utility functions
    def increaseMaxLevel(self):
        # Increase max level of list and add the missing pointers
        level = self.maxLevel
        p = self.head
        q = p.pointers[-1]
        while q != self.tail:
            if q.level > level:
                p.pointers.append(q)
                p = q
            q = q.pointers[-1]
        p.pointers.append(q)
        self.maxLevel += 1


    def decreaseMaxLevel(self):
        level = self.maxLevel
        p = self.head
        q = p.pointers[-1]
        while q.level >= level:
            if len(q.pointers) < level:
                print("ERROR, trying to decrease level, but too far down")
            else:
                p.pointers.pop()
                p = q
                q = p.pointers[-1]
        p.pointers.pop()
        self.maxLevel += -1


    def sizeTooBig(self):
        # Determine if size is too big
        if math.floor(math.log(self.size, 1/self.p)) > self.maxLevel:
            return True
        else:
            return False
    

    def sizeTooSmall(self):
        # Determine if size is too small
        if math.ceil(math.log(self.size, 1/self.p)) < self.maxLevel:
            return True
        else:
            return False


    def traverseList(self):
        x = self.head
        print("Maxlevel: ",self.maxLevel)
        print("pointers length of head", len(x.pointers))
        for i in range(self.maxLevel,0,-1):
            while x != self.tail:
                print("(", x.key, ")",end=" ")
                x = x.pointers[i-1]
            print()
            x = self.head





if __name__ == "__main__":
    #handle input and run functions
    p = 0.25
    skiplist = SkipList(p)
    while True:
        line = sys.stdin.readline()
        comparisoncounter = 0
        l = line.split()
        if len(l)==0:
            break
        if l[0] == "I":
            result = skiplist.insert(int(l[1]))
            if result:
                print("S - comparisons used: ", comparisoncounter)
            else:
                print("F - comparisons used: ", comparisoncounter)
        elif l[0] == "D":
            result = skiplist.delete(int(l[1]))
            if result:
                print("S - comparisons used: ", comparisoncounter)
            else:
                print("F - comparisons used: ", comparisoncounter)
        elif l[0] == "S":
            result = skiplist.search(int(l[1]))
            if result:
                print("S - comparisons used: ", comparisoncounter)
            else:
                print("F - comparisons used: ", comparisoncounter)
        else:
            break
