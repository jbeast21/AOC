# Day 6

import numpy as np
from collections import Counter

# Part 1
fn = '06.txt'
f = open(fn)
fish = [int(x) for x in f.readline().strip().split(',')]
fish_start = fish.copy()
days = 80
for day in range(days):
    for ind in range(len(fish)):
        if fish[ind] == 0:
            fish.append(8)
            fish[ind] = 6
        else:
            fish[ind] -= 1
print(len(fish))

# Part 2
fish = fish_start.copy()
fishdic = Counter(fish)
fishdic2 = fishdic.copy()
days = 256
for day in range(days):
    births = fishdic[0]
    for i in range(0, 8):
        fishdic[i] = fishdic[i+1]
    fishdic[8] = births
    fishdic[6] += births
print(sum(fishdic.values()))