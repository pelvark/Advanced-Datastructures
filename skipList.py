#!/usr/bin/env python
import random
import math

class Node(object):
    def __init__(self, key):
        #init
        self.key = key
        self.level = self.randomLevel()
        self.pointers = []


    def randomLevel(self):
        # detemine the highest possible level of a node
        # should be changed to a formula with some probability.
        level = 1
        while random.random() < p and level < 32:
            level += 1
        return level


class SkipList(object):
    def __init__(self):
        #init
        self.head = Node(None)
        self.tail = Node(float("inf"))
        self.maxLevel
        self.size = 0
        self.p = 0.5 # TODO: find better p

    
    def insert(self, key):
        # insert a node with key 
        update = []
        x = self.head
        for i in range(self.maxLevel,0,-1):
            while len(x.pointers) >= i and x.pointers[i-1].key < key:
                x = x.pointers[i-1]
            update.append(x)
        x = x.pointers[i-1]
        if x.key == key:
            # key already in list, replace it or something
            pass
        else:
            x = Node(key)
            update = reversed(update)
            for i in range(0,x.level):
                x.pointers.append(update[i].pointers[i])
                update[i].pointers[i] = x
            self.size += 1
            if self.sizeTooBig():
                self.increaseMaxLevel()
            return True


    def delete(self, key):
        # search for a node with key, and delete it
        pass
        update = []
        x = self.head
        for i in range(self.maxLevel,0,-1):
            while len(x.pointers) >= i and x.pointers[i-1].key < key:
                x = x.pointers[i-1]
            update.append(x)
        x = x.pointers[i-1]
        if x.key == key:
            update = reversed(update)
            for i in range(0,min(x.level, self.maxLevel) + 1):            
                update[i].pointers[i] = x.pointers[i]
            self.size += -1
            if self.sizeTooSmall():
                self.maxLevel += -1
        else:
            return False



    def search(self, key):
        # search for a node with key
        x = self.head
        for i in range(self.maxLevel,0,-1):
            while len(x.pointers) >= i and x.pointers[i-1].key < key:
                x = x.pointers[i-1]
        if len(x.pointers) > 0 and x.pointers[0].key == key:
            return x.pointers[0]
        else:
            return None

    

    #Utility functions
    def increaseMaxLevel(self):
        # Increase max level of list and add the missing pointers
        level = self.maxLevel
        p = self.head
        q = p.pointers[-1]
        while q.level >= level:
            if q.level > level:
                p.pointers.append(q)
                p = q
            q = p.pointers[-1]
        if q == self.tail:
            p.pointers.append(q)
            self.maxLevel += 1
        else:
            print("ERROR, increasing max level has not reached until tail.")


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















if __name__ == "__main__":
    #handle input and run functions
    pass
