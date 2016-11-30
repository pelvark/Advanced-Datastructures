#!/usr/bin/env python
import sys
import random
random.seed(42)

def randominput(n,f):
    l = list(range(0,n))
    random.shuffle(l)
    for i in l:
        print("I", i, file=f)
    for i in range(0,n):
        print("S", random.randrange(0,n), file=f)

def randomwithdeletion(n,f):
    l = list(range(0,n))
    random.shuffle(l)
    for i in l:
        print("I", i, file=f)
    for i in range(0,n):
        r = random.randint(0,1)
        if r == 1:
            print("S", random.randrange(0,n), file=f)
        else:
            print("D", random.randrange(0,n), file=f)

def sortedinput(n,f):
    l = list(range(0,n))
    for i in l:
        print("I ", i, file=f)
    random.shuffle(l)
    for i in l: 
        print("S ", i, file=f)

def test1(n,f):
    m = n%50
    n = n-m
    l = list(range(0,n))
    random.shuffle(l)
    for i in range(0,n,50):
        for k in range(0,50):
            print("I", l[i+k], file=f)
        for k in range(0,50):
            print("S", l[random.randrange(0,i+50)], file=f)
             
    
def test2(n,f):
    l = list(range(0,n))
    random.shuffle(l)
    for i in l:
        print("I", i, file=f)
    random.shuffle(l)
    for i in l:
        print("S", i, file=f)

def test3(n,f):
    l = list(range(0,n))
    random.shuffle(l)
    for i in l:
        print("I", i, file=f)

def test4(n,f):
    #random input for random tree
    m = n%50
    n = n-m
    l = list(range(0,n))
    random.shuffle(l)
    for i in range(0,n,50):
        for k in range(0,50):
            print("I", l[i+k], file=f)
        print("T A", file=f)
    print("T D", file=f)
    

def test5(n,f):
    #sorted input for random tree
    m = n%50
    n = n-m
    l = list(range(0,n))
    for i in range(0,n,50):
        for k in range(0,50):
            print("I", l[i+k], file=f)
        print("T A", file=f)
    print("T D", file=f)

def test6(n,f):
    #reverse sorted input for random tree
    m = n%50
    n = n-m
    l = list(range(n-1,-1,-1))
    for i in range(0,n,50):
        for k in range(0,50):
            print("I", l[i+k], file=f)
        print("T A", file=f)
    print("T D", file=f)


def testX(n,f):
    # for PPLL
    # many random inserts and searches in one version
    for i in range(1,n+1):
        print("I", i, i, file=f)
    for i in range(1,n+1):
        print("S", 0, i, file=f)

def testX(n,f):
    # for PPLL
    # many random inserts with new version each time
    l = list(range(1,n+1))
    random.shuffle(l)
    for i in range(1,n+1):
        j = random.randint(1,i)
        print("I", i, j, file=f)
        print("N", file=f)
    for i in range(1,n+1):
        print("S", n, i, file=f)

def testX(n,f):
    pass



if __name__=="__main__":
    if len(sys.argv) == 1:
        print("no arguments given")
    elif sys.argv[1] == "random":
        f = open(sys.argv[3],"w")
        randominput(int(sys.argv[2]), f)
    elif sys.argv[1] == "randomdelete":
        f = open(sys.argv[3],"w")
        randomwithdeletion(int(sys.argv[2]), f)
    elif sys.argv[1] == "sorted":
        f = open(sys.argv[3],"w")
        sortedinput(int(sys.argv[2]), f)
    elif sys.argv[1] == "test1":
        f = open(sys.argv[3],"w")
        test1(int(sys.argv[2]), f)
    elif sys.argv[1] == "test2":
        f = open(sys.argv[3],"w")
        test2(int(sys.argv[2]), f)
    elif sys.argv[1] == "test3":
        f = open(sys.argv[3],"w")
        test3(int(sys.argv[2]), f)
    elif sys.argv[1] == "test4":
        f = open(sys.argv[3],"w")
        test4(int(sys.argv[2]), f)
    elif sys.argv[1] == "test5":
        f = open(sys.argv[3],"w")
        test5(int(sys.argv[2]), f)
    elif sys.argv[1] == "test6":
        f = open(sys.argv[3],"w")
        test6(int(sys.argv[2]), f)
    

            
            
