# Day 5

import numpy as np

# Part 1
fn = '05.txt'
f = open(fn)
data = []
for line in f:
    data.append([int(x) for x in line.strip().replace(' -> ', ',').split(',')])

maxVal = np.max(data) + 1
grid = np.zeros((maxVal, maxVal))
for points in data:
    x1, y1, x2, y2 = points
    if x1 == x2:
        for y in list(range(min([y1, y2]), max([y1, y2])+1)):
            grid[x1, y] += 1
    elif y1 == y2:
        for x in list(range(min([x1, x2]), max([x1, x2])+1)):
            grid[x, y1] += 1
print(len(grid[grid > 1]))

# Part 2
grid = np.zeros((maxVal, maxVal))
for points in data:
    x1, y1, x2, y2 = points
    if x1 == x2:
        for y in list(range(min([y1, y2]), max([y1, y2])+1)):
            grid[x1, y] += 1
    elif y1 == y2:
        for x in list(range(min([x1, x2]), max([x1, x2])+1)):
            grid[x, y1] += 1
    else:
        x = list(range(x1, x2+1))
        if not x:
            x = list(reversed(list(range(x2, x1+1))))
        y = list(range(y1, y2+1))
        if not y:
            y = list(reversed(list(range(y2, y1+1))))
        for xi, yi in list(zip(x, y)):
            grid[xi, yi] += 1
print(len(grid[grid > 1]))