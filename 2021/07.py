# Day 7

import numpy as np
from statistics import mean, median

# Part 1
fn = '07.txt'
f = open(fn)
data = [int(x) for x in f.readline().strip().split(',')]
med = median(data)
fuel = 0
for i in data:
    fuel += abs(i - med)
print(fuel)


# Part 2
def fuelCalc(point, ref):
    d = abs(point-ref)
    fuel = (d+1)*d/2
    return(fuel)


minfuel = np.inf
for i in range(max(data)):
    fuel = 0
    for j in data:
        fuel += fuelCalc(j, i)
    if fuel < minfuel:
        minfuel = fuel
print(minfuel)