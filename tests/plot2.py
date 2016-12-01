#!/usr/bin/env python
from __future__ import division
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math

#random tree results
def rtvalues(filename):
    # takes results of randomtree and makes data for averages and variations
    f = open(filename,"r")
    lines = f.readlines()
    averages = []
    depths = []
    for line in lines:
        line = line.split()
        if line[0] == "average":
            averages.append(line[-1])
        if line[0] == "key:":
            depths.append(line[-1])
    depths.sort()
    d = [[x,depths.count(x)] for x in set(depths)]
    d1 = [i[0] for i in d]
    d2 = [i[1] for i in d]
    return averages, d1, d2

randaverages, randd1, randd2 = rtvalues("rresult1")
sortaverages, sortd1, sortd2 = rtvalues("rresult2")
rsortaverages, rsortd1, rsortd2 = rtvalues("rresult3")

#plot with average depth as a function of n.
x = [a*50 for a in range(1,int(len(averages))+1)]
plt.figure(1)
rand, = plt.plot(x, randaverages  , label='random')
sort, = plt.plot(x, sortaverages  , label='sorted')
rsort,= plt.plot(x, rsortaverages , label='reverse sorted')
plt.legend()
plt.xlabel('n')
plt.ylabel('average depth')
plt.savefig('averagedepth.png')

# histogram with variations depths.
plt.figure(2)
plt.plot(randd1, randd2)
plt.xlabel('depth')
plt.ylabel('number of nodes')
plt.savefig("randdepthvariation.png")

plt.figure(3)
plt.plot(sortd1, sortd2)
plt.xlabel('depth')
plt.ylabel('number of nodes')
plt.savefig("sortdepthvariation.png")

plt.figure(4)
plt.plot(rsortd1, rsortd2)
plt.xlabel('depth')
plt.ylabel('number of nodes')
plt.savefig("rsortdepthvariation.png")


#PPLL results
def ppllvalues(filename):
    # takes results of randomtree and makes data for averages and variations
    f = open(filename,"r")
    lines = f.readlines()
    nodes = []
    space = []
    for line in lines:
        line = line.split()
        if line[0] == "nodes:":
            nodes.append(line[-1])
        if line[0] == "space":
            space.append(line[-1])
    return nodes, space

# first test what e value is best with random input, 
# then test that e values result with sorted, random, allfirst
x = [a*100 for a in range(1,int(len(averages))+1)]

#graph node use with different e
nodes2, space2 = ppllvalues("ppll2")
nodes3, space3 = ppllvalues("ppll3")
nodes4, space4 = ppllvalues("ppll4")
nodes8, space8 = ppllvalues("ppll8")

plt.figure(5)
node2, = plt.plot(x, nodes2  , label='e=2')
node3, = plt.plot(x, nodes3  , label='e=3')
node4, = plt.plot(x, nodes4  , label='e=4')
node8, = plt.plot(x, nodes8  , label='e=8')
plt.legend()
plt.xlabel('n')
plt.ylabel('nodes')
plt.savefig('enodes.png')

#graph pointeruse with different e
plt.figure(6)
space2, = plt.plot(x, space2  , label='e=2')
space3, = plt.plot(x, space3  , label='e=3')
space4, = plt.plot(x, space4  , label='e=4')
space8, = plt.plot(x, space8  , label='e=8')
plt.legend()
plt.xlabel('n')
plt.ylabel('space')
plt.savefig('espace.png')

#graph nodes in rand, sort, allfirst with best e
nodesrand, spacerand = ppllvalues("ppllrand")
nodessort, spacesort = ppllvalues("ppllsort")
nodesfirst, spacefirst = ppllvalues("ppllfirst")

plt.figure(7)
nodesrand,   = plt.plot(x, nodesrand   , label='random')
nodessort,   = plt.plot(x, nodessort   , label='sorted')
nodesfirst,  = plt.plot(x, nodesfirst  , label='all first')
plt.legend()
plt.xlabel('n')
plt.ylabel('nodes')
plt.savefig('diffnodes.png')

plt.figure(8)
spacerand,   = plt.plot(x, spacerand   , label='random')
spacesort,   = plt.plot(x, spacesort   , label='sorted')
spacefirst,  = plt.plot(x, spacefirst  , label='all first')
plt.legend()
plt.xlabel('n')
plt.ylabel('space')
plt.savefig('diffspace.png')




########### ANYTHING UNDER HERE IS OLD AND SHOULD BE DELETED

#skiplist results
g = open("skout","r")
lines = g.readlines()
comp = []
for line in lines:
   line = line.split()
   comp.append(line[4])
z = []
for i in range(50,len(comp),100):
    sum = 0
    for k in range(0,50):
        sum += int(comp[i+k])
    z.append(sum/50) 

x = [a*50 for a in range(1,int(len(comp)/100)+1)]
#simple plot with datastructure size as x and average search comparisons y and z for scapegoat trees and skip lists 
plt.figure(1)
plt.plot(x,y,"b",x,z,"r")
plt.xlabel('comparisons')
plt.ylabel('n')
plt.savefig('averagesearch.png')

#plot with y axis scaled logarithmically
plt.figure(2)
plt.plot(x,y,"b",x,z,"r")
plt.yscale('log', basex=2)
plt.xlabel('log(comparisons)')
plt.ylabel('n')
plt.savefig("logscale.png")

ylog = []
zlog = []
for i in range(len(y)):
    ylog.append(y[i]/math.log(x[i],2))
    zlog.append(z[i]/math.log(x[i],2))

#plot with results divided by the size
plt.figure(3)
plt.plot(x,ylog,"b",x,zlog,"r")
plt.xlabel('comparisons/log(n)')
plt.ylabel('n')
plt.savefig("dividedlog.png")


#bigtest results
f = open("bigresult","r")
lines = f.readlines()
length = len(lines)
lines = lines[length/2:]
comp = []
for line in lines:
   line = line.split()
   comp.append(line[4])

comp.sort()
l = [[x,comp.count(x)] for x in set(comp)]
l1 = [i[0] for i in l]
l2 = [i[1] for i in l]

g = open("bigresult","r")
lines = g.readlines()
length = len(lines)
lines = lines[length/2:]
comp = []
for line in lines:
   line = line.split()
   comp.append(line[4])

comp.sort()
k = [[x,comp.count(x)] for x in set(comp)]
k1 = [i[0] for i in k]
k2 = [i[1] for i in k]
#variation counting
plt.figure(4)
plt.plot(l1,l2,"r",k1,k2,"b")
plt.xlabel('searches')
plt.ylabel('i')
plt.savefig("variation.png")




