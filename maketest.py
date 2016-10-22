import sys
import random

def randominput(n,f):
    l = list(range(0,n))
    random.shuffle(l)
    for i in l:
        print("I ", i, file=f)
    for i in range(0,n):
        print("S ", random.randrange(0,n), file=f)

def randomwithdeletion(n,f):
    l = list(range(0,n))
    random.shuffle(l)
    for i in l:
        print("I ", i, file=f)
    for i in range(0,n):
        r = random.randint(0,1)
        if r == 1:
            print("S ", random.randrange(0,n), file=f)
        else:
            print("D ", random.randrange(0,n), file=f)

def sortedinput(n,f):
    l = list(range(0,n))
    for i in l:
        print("I ", i, file=f)
    random.shuffle(l)
    for i in l: 
        print("S ", i file=f)








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

            
            