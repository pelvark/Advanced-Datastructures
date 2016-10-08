#!/usr/bin/env python
import random

class Node(object):
    def __init__(self, key):
        #init
        self.key = key
        self.level = 0
        self.pointers = []


    def determineLevel(self):
        # detemine the highest possible level of a node
        # should be changed to a formula with some probability.
        return randint(1,10) 


class SkipList(object):
    def __init__(self):
        #init
        self.head = Node(None)
        self.tail = Node(float("inf"))
        self.maxLevel
        self.size = 0

    
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
        pass


    def sizeTooBig(self):
        # Determine if size is too big
        pass
















if __name__ == "__main__":
    #handle input and run functions
    pass
