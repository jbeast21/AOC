# Day 11

import numpy as np

fn = '11.txt'
data = []
for line in open(fn):
    data.append([int(x) for x in line.strip()])
data = np.array(data)


def findFlashes(d):
    flashes = data*0
    xsize, ysize = d.shape
    for y in range(ysize):
        for x in range(xsize):
            if d[y, x] > 9:
                flashes[y, x] = 1
    return(flashes)


def flash(d, yind, xind):
    global flashcounts
    global flashcounts_round
    flashcounts += 1
    flashcounts_round += 1
    x_len, y_len = d.shape
    for y in [yind-1, yind, yind+1]:
        for x in [xind-1, xind, xind+1]:
            if y < 0 or x < 0:
                continue
            if y >= y_len or x >= x_len:
                continue
            d[y, x] += 1
    return(d)


steps = 1000
flashcounts = 0
flashcounts_round = 0
x_len, y_len = data.shape
for i in range(steps):
    if i == 100:
        print('Part 1:', flashcounts)
    data_flashed = data*0
    data = data+1
    flashes = findFlashes(data)
    while flashes.sum() > 0:
        for yind in range(x_len):
            for xind in range(y_len):
                if flashes[yind, xind]:
                    if not data_flashed[yind, xind]:
                        data = flash(data, yind, xind)
                        data_flashed[yind, xind] += 1
                    flashes[yind, xind] = 0
        flashes = findFlashes(data)
        for yind in range(x_len):
            for xind in range(y_len):
                if flashes[yind, xind]:
                    if data_flashed[yind, xind]:
                        flashes[yind, xind] = 0
    for yind in range(y_len):
        for xind in range(x_len):
            if data_flashed[yind, xind]:
                data[yind, xind] = 0
    if data.sum() == 0:
        break

print('Part 2:', i+1)