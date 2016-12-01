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


def test7(n,f):
    # for PPLL
    # sorted inserts with new version for each, and random searches
    m = n%50
    n = n-m
    for i in range(1,n+1,50):
        for k in range(0,50):
            print("I", i+k, i+k, file=f)
            j = random.randint(1,i+k)
            print("U", i+k, j, file=f)
            print("N", file=f)
        print("C N",file=f)
        print("C S",file=f)
        

def test8(n,f):
    # for PPLL
    # many random inserts with new version each time
    l = list(range(1,n+1))
    random.shuffle(l)
    for i in range(1,n+1,50):
        for k in range(0,50):
            j = random.randint(1,i+k)
            print("I", i+k, j, file=f)
            print("N", file=f)
            j = random.randint(1,i+k)
            print("U", i+k, j, file=f)
            print("N", file=f)
        print("C N",file=f)
        print("C S",file=f)

def test9(n,f):
    # many inserts in first space with new versions, random searches
    for i in range(1,n+1,50):
        for k in range(0,50):
            print("I", i+k, 1, file=f)
            j = random.randint(1,i+k)
            print("U", i+k, j, file=f)
            print("N", file=f)
        print("C N",file=f)
        print("C S",file=f)



if __name__=="__main__":
    if len(sys.argv) == 1:
        print("no arguments given")
    else:
        f = open(sys.argv[3],"w")
        if sys.argv[1] == "random":
            randominput(int(sys.argv[2]), f)
        elif sys.argv[1] == "randomdelete":
            randomwithdeletion(int(sys.argv[2]), f)
        elif sys.argv[1] == "sorted":
            sortedinput(int(sys.argv[2]), f)
        elif sys.argv[1] == "test1":
            test1(int(sys.argv[2]), f)
        elif sys.argv[1] == "test2":
            test2(int(sys.argv[2]), f)
        elif sys.argv[1] == "test3":
            test3(int(sys.argv[2]), f)
        elif sys.argv[1] == "test4":
            test4(int(sys.argv[2]), f)
        elif sys.argv[1] == "test5":
            test5(int(sys.argv[2]), f)
        elif sys.argv[1] == "test6":
            test6(int(sys.argv[2]), f)
        elif sys.argv[1] == "test7":
            test7(int(sys.argv[2]), f)
        elif sys.argv[1] == "test8":
            test8(int(sys.argv[2]), f)
        elif sys.argv[1] == "test9":
            test9(int(sys.argv[2]), f)
    

            
            
