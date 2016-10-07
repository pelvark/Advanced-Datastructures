#!/usr/bin/env python
import random

class Node(object):
    def __init__(self, key):
        #init
        self.level = 0
        self.pointers = []


    def determineLevel(self):
        # detemine the highest possible level of a node
        # should be changed to a formula with some probability.
        return randint(1,10) 


class SkipList(object):
    def __init__(self):
        #init
        self.head
        self.tail
        self.max_level

    
    def insert(self, key)
        # insert a node with key 
        x = Node(key)


    def delete(self, key):
        # search for a node with key, and delete it


    def search(self, key):
        # search for a node with key
















if __name__ == "__main__":
    #handle input and run functions
