#!/usr/bin/env python
from __future__ import division
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math

#random tree results
def rtvalues(filename):
    f = open(filename,"r")
    lines = f.readlines()
    averages = []
    depths = []
    comp = []
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

averages, d1, d2 = rtvalues("filename")
#plot with average depth as a function of n.
x = [a*50 for a in range(1,int(len(averages))+1)]
plt.figure(1)
plt.plot(x,averages)
plt.xlabel('n')
plt.ylabel('average depth')
plt.savefig('averagedepth.png')

# histogram with variations depths.
plt.figure(2)
plt.plot(d1, d2)
plt.xlabel('depth')
plt.ylabel('number of nodes')
plt.savefig("depthvariation.png")




#PPLL results







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




