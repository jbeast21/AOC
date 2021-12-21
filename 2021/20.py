# Day 20

import numpy as np
from collections import Counter

fn = '20.txt'
f = open(fn)

iea = ''
image = []
for line in f:
    if not line.strip():
        break
    iea += line.strip()
for line in f:
    image.append([x for x in line.strip()])
image_start = np.array(image)
binaryDic = {'.':'0', '#':'1'}


def padImage(arr, padsize, char):
    ylen, xlen = arr.shape
    ypad = np.array([[char]*xlen]*padsize)
    xpad = np.array([[char]*padsize]*(ylen+2*padsize))
    arr = np.concatenate((ypad, arr, ypad), axis=0)
    arr = np.concatenate((xpad, arr, xpad), axis=1)
    return(arr)


def enhanceImage(arr, x, y):
    s = ''
    for _y in [y-1, y, y+1]:
        for _x in [x-1, x, x+1]:
            s += arr[_y, _x]
    binary = ''
    for char in s:
        binary += binaryDic[char]
    binary = int(binary,2)
    pixel = iea[binary]
    return(pixel)


# Part 1
image = padImage(image_start, 2, '.')
image_out = image.copy()
ylen, xlen = image.shape
rounds = 2
for _ in range(rounds):
    for y in range(ylen):
        for x in range(xlen):
            if x in [0, xlen-1] or y in [0, ylen-1]:
                image_out[y, x] = iea[int(binaryDic[image[y, x]]*9, 2)]
                continue
            image_out[y, x] = enhanceImage(image, x, y)
    image = padImage(image_out, 1, image_out[y, x])
    ylen, xlen = image.shape
    image_out = image.copy()
print('Part 1:', np.char.count(image, '#').sum())

# Part 2
image = padImage(image_start, 2, '.')
image_out = image.copy()
ylen, xlen = image.shape
rounds = 50
for _ in range(rounds):
    for y in range(ylen):
        for x in range(xlen):
            if x in [0, xlen-1] or y in [0, ylen-1]:
                image_out[y, x] = iea[int(binaryDic[image[y, x]]*9, 2)]
                continue
            image_out[y, x] = enhanceImage(image, x, y)
    image = padImage(image_out, 1, image_out[y, x])
    ylen, xlen = image.shape
    image_out = image.copy()
print('Part 2:', np.char.count(image, '#').sum())