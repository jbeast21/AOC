# Day 3

import numpy as np
from collections import Counter

fn = '03.txt'
data = [x for x in open(fn).read().strip().split('\n')]

# Part 1
theta = ''
epsilon = ''
for i in range(len(data[0])):
    counts = Counter([x[i] for x in data])
    if counts['0'] > counts['1']:
        theta += '0'
        epsilon += '1'
    else:
        theta += '1'
        epsilon += '0'
print(int(theta, 2)*int(epsilon, 2))

# Part 2
ox = data.copy()
co = data.copy()
for i in range(len(ox[0])):
    ox_count = Counter([x[i] for x in ox])
    ox_mcv = max(ox_count, key=ox_count.get)
    ox_lcv = min(ox_count, key=ox_count.get)
    if ox_mcv == ox_lcv:
        ox = [x for x in ox if x[i] == '1']
    else:
        ox = [x for x in ox if x[i] == ox_mcv]
    if len(ox) == 1:
        break
for i in range(len(co[0])):
    co_count = Counter([x[i] for x in co])
    co_mcv = max(co_count, key=co_count.get)
    co_lcv = min(co_count, key=co_count.get)
    if co_mcv == co_lcv:
        co = [x for x in co if x[i] == '0']
    else:
        co = [x for x in co if x[i] == co_lcv]
    if len(co) == 1:
        break
print(int(ox[0], 2)*int(co[0], 2))