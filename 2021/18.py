# Day 18

import numpy as np
import re
from math import floor, ceil

fn = 'input.txt'
f = open(fn)
data = []
for line in f:
    data.append(line.strip())


def addition(a, b):
    z = '['+a+','+b+']'
    return(z)


def reduce(s):
    toExplode = True
    while toExplode:
        nestcount = 0
        for i in range(len(s)):
            if s[i] == '[':
                nestcount += 1
            elif s[i] == ']':
                nestcount -= 1
            if nestcount == 5:
                break
        if nestcount == 5:
            s = explode(s, i)
        else:
            toExplode = False
    nums = [int(x) for x in
            s.replace('[', ',').replace(']', ',').split(',') if x]
    if max(nums) > 9:
        s = reduce(split(s))
    return(s)


def split(s):
    nums = [int(x) for x in
            s.replace('[', ',').replace(']', ',').split(',') if x]
    nums = [x for x in nums if x > 9]
    leftnum = floor(nums[0]/2)
    rightnum = ceil(nums[0]/2)
    s = s.replace(str(nums[0]), '['+str(leftnum)+','+str(rightnum)+']', 1)
    return(s)


def explode(s, i):
    exp_str = s[i:s.find(']', i)+1]
    exp_left, exp_right = [int(x) for x in exp_str[1:-1].split(',')]
    s = s[:i] + 'y' + s[s.find(']', i)+1:]
    leftnum = re.findall('[0-9]+', s[:i])
    rightnum = re.findall('[0-9]+', s[i:])
    if leftnum:
        temp = s[:i][::-1].replace(leftnum[-1][::-1], 'x', 1)[::-1] + s[i:]
        s = temp.replace('x', str(sum([int(leftnum[-1]), exp_left])), 1)
    if rightnum:
        temp = s[:i] + s[i:].replace(rightnum[0], 'x', 1)
        s = temp.replace('x', str(sum([int(rightnum[0]), exp_right])), 1)
    s = s.replace('y', '0', 1)
    return(s)


def magnitude(s):
    y = re.findall('[0-9]+,[0-9]+', s)
    if y:
        leftnum, rightnum = [int(x) for x in y[0].split(',')]
        mag = 3*leftnum+2*rightnum
        s = s.replace('['+y[0]+']', str(mag))
        s = magnitude(s)
    return(s)


# Part 1
hw = data[0]
for i in data[1:]:
    hw = reduce(addition(hw, i))
print('Part 1:', int(magnitude(hw)))

# Part 2
mags = []
for i in data:
    for j in data:
        if i == j:
            continue
        mags.append(int(magnitude(reduce(addition(i, j)))))
print('Part 2:', max(mags))