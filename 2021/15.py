#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math
from collections import Counter
import re
from statistics import mean, median

#fn = 'test.txt'
fn = 'input.txt'
f = open(fn)

risk = []
for l in f:
    risk.append([int(x) for x in l.strip()])
risk = np.array(risk)

def calcCost(risk, cost, y, x):
    ylen, xlen = risk.shape
    options = []
    if x+1 < xlen:
        c = cost[y, x+1] + risk[y, x]
        options.append(c)
    if y+1 < ylen:
        c = cost[y+1, x] + risk[y, x]
        options.append(c)
    #print(options)
    return(min(options))

def calcCost2(risk, cost, y, x):
    ylen, xlen = risk.shape
    options = [cost[y,x]]
    if x+1 < xlen:
        c = cost[y, x+1] + risk[y, x]
        options.append(c)
    if y+1 < ylen:
        c = cost[y+1, x] + risk[y, x]
        options.append(c)
    if x-1 > 0:
        c = cost[y, x-1] + risk[y, x]
        options.append(c)
    if y-1 > 0:
        c = cost[y-1, x] + risk[y, x]
        options.append(c)
    #print(options)
    return(min(options))

risk2 = risk.copy()
for x in range(1,5):
    risk2 = np.concatenate((risk2,risk+x),axis=0)
risk3 = risk2.copy()
for x in range(1,5):
    risk3 = np.concatenate((risk3,risk2+x),axis=1)

ylen, xlen = risk3.shape
for y in range(ylen):
    for x in range(xlen):
        while risk3[y,x] > 9:
            risk3[y,x] -= 9

cost = risk3*0
risk3[0,0] = 0
cost[ylen-1, xlen-1] = risk3[ylen-1, xlen-1]
for y in range(ylen)[::-1]:
    for x in range(xlen)[::-1]:
        if cost[y, x]: continue
        cost[y, x] = calcCost(risk3, cost, y, x)

its = 100
for _ in range(its):
    for y in range(ylen)[::-1]:
        for x in range(xlen)[::-1]:
            cost[y, x] = calcCost2(risk3, cost, y, x)
    print(cost[0,0])


# In[50]:




