#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Day 13

import numpy as np

fn = '13.txt'
f = open(fn)
data = []
folds = []
for line in f:
    if not line.strip():
        continue
    if 'fold' not in line:
        data.append([int(x) for x in line.strip().split(',')])
    elif 'fold' in line:
        folds.append(line.strip().replace('fold along ', ''))

data = np.array(data)
max_x = data[:, 0].max()+1
max_y = data[:, 1].max()+1

paper = np.zeros((max_y, max_x))
for x, y in data:
    paper[y, x] = 1


def chooseFold(s, paper):
    if 'y' in s:
        return(foldY(s, paper))
    if 'x' in s:
        return(foldX(s, paper))


def foldY(s, paper):
    ind = int(s.replace('y=', ''))
    paper1 = paper[0:ind, :]
    paper2 = np.flipud(paper[(ind+1):, :])
    if paper1.shape != paper2.shape:
        y1 = paper1.shape[0]
        y2 = paper2.shape[0]
        if y1 > y2:
            paper2 = resizeY(y1, paper2)
        elif y2 > y1:
            paper1 = resizeY(y2, paper1)
    newpaper = makeOnes(paper1+paper2)
    return(newpaper)


def resizeY(ind, arr):
    y, x = arr.shape
    arr2 = arr.copy()
    arr2.resize((ind, x))
    return(np.roll(arr2, ind-y, axis=0))


def resizeX(ind, arr):
    y, x = arr.shape
    arr2 = arr.copy()
    arr2.resize((y, ind))
    return(np.roll(arr2, ind-x, axis=1))


def foldX(s, paper):
    ind = int(s.replace('x=', ''))
    paper1 = paper[:, 0:ind]
    paper2 = np.fliplr(paper[:, (ind+1):])
    if paper1.shape != paper2.shape:
        x1 = paper1.shape[1]
        x2 = paper2.shape[1]
        if x1 > x2:
            paper2 = resizeX(x1, paper2)
        elif x2 > x1:
            paper1 = resizeX(x2, paper1)
    newpaper = makeOnes(paper1+paper2)
    return(newpaper)


def makeOnes(arr):
    y, x = arr.shape
    for yind in range(y):
        for xind in range(x):
            if arr[yind, xind]:
                arr[yind, xind] = 1
    return(arr)


part1 = 1
for i in folds:
    paper = chooseFold(i, paper)
    if part1:
        print('Part 1:', np.sum(paper))
        part1 -= 1

# Part 2
print('Part 2:')
for i in paper:
    line = ''
    for j in i:
        if j == 0:
            line += '.'
        elif j == 1:
            line += '#'
    print(line)

