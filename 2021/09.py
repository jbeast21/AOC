# Day 9

import numpy as np

# Part 1
fn = '09.txt'
f = open(fn)
data = []
for line in f:
    data.append([int(x) for x in line.strip()])
data = np.array(data)


def checkLow(x, y, data):
    xrange = len(data[0, :])
    yrange = len(data[:, ])
    height = data[y, x]
    adjacent = []
    for ind in [x+1, x-1]:
        if ind >= 0 and ind < xrange:
            adjacent.append(data[y, ind])
    for ind in [y+1, y-1]:
        if ind >= 0 and ind < yrange:
            adjacent.append(data[ind, x])
    isLow = True
    for h in adjacent:
        if h <= height:
            isLow = False
    return(isLow)


lowpoints = []
risk = []
xrange = len(data[0, :])
yrange = len(data[:, ])
for yind in range(yrange):
    for xind in range(xrange):
        if checkLow(xind, yind, data):
            lowpoints.append([xind, yind])
            risk.append(data[yind, xind]+1)
print(sum(risk))


# Part 2
def adjacentBasin(x, y, data):
    height = data[y, x]
    xrange = len(data[0, :])
    yrange = len(data[:, ])
    points = [[x, y]]
    for ind in [x+1, x-1]:
        if ind >= 0 and ind < xrange:
            if data[y, ind] == 9:
                continue
            if data[y, ind] > height:
                points.append([ind, y])
    for ind in [y+1, y-1]:
        if ind >= 0 and ind < yrange:
            if data[ind, x] == 9:
                continue
            if data[ind, x] > height:
                points.append([x, ind])
    return(points)


basinlist = []
for point1 in lowpoints:
    basin = [point1]
    basinsize = len(basin)
    growing = True
    while growing:
        for point2 in basin:
            basinpoints = adjacentBasin(point2[0], point2[1], data)
            for x in basinpoints:
                if x not in basin:
                    basin.append(x)
        newbasinsize = len(basin)
        if newbasinsize == basinsize:
            growing = False
        basinsize = len(basin)
    basinlist.append(basin)

basinsizes = [len(x) for x in basinlist]
top3 = []
while len(top3) < 3:
    top3.append(max(basinsizes))
    basinsizes.remove(max(basinsizes))

print(np.prod(top3))