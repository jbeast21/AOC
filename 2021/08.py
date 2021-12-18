# Day 8

import numpy as np
from collections import Counter

# Part 1
fn = '08.txt'
f = open(fn)

datain = []
dataout = []
datain_counts = []
dataout_counts = []

for line in f:
    temp = line.strip().split('|')
    datain.append(temp[0].strip().split())
    dataout.append(temp[1].strip().split())

digit_counts = 0
for i in range(len(datain)):
    datain_counts.append(Counter([len(x) for x in datain[i]]))
    dataout_counts.append(Counter([len(x) for x in dataout[i]]))
    digit_counts += sum([dataout_counts[i][x] for x in [2, 3, 4, 7]])
print(digit_counts)


# Part 2
def stringSub(first, second):
    for i in second:
        first = first.replace(i, '')
    return(first)


def stringSum(lis):
    strsum = ''
    for i in lis:
        for j in i:
            if j not in strsum:
                strsum += j
    return(strsum)


valuelist = []
for ind in range(len(datain)):
    key = {}
    for x in range(10):
        key[x] = ''
    line = datain[ind]
    for word in line:
        if len(word) == 2:
            key[1] = ''.join(sorted(word))
            continue
        if len(word) == 3:
            key[7] = ''.join(sorted(word))
            continue
        if len(word) == 4:
            key[4] = ''.join(sorted(word))
            continue
        if len(word) == 7:
            key[8] = ''.join(sorted(word))
            continue
    for word in line:
        if len(word) == 5:
            if len(stringSub(word, stringSum([stringSub(key[8], stringSum([key[4], key[7]])), key[7]]))) == 2:
                key[5] = ''.join(sorted(word))
            if len(stringSub(word, key[1])) == 3:
                key[3] = ''.join(sorted(word))
            if len(stringSub(word, key[4])) == 3:
                key[2] = ''.join(sorted(word))
    for word in line:
        if len(word) == 6:
            if len(stringSub(word, key[7])) == 4:
                key[6] = ''.join(sorted(word))
            if len(stringSub(word, key[4])) == 2:
                key[9] = ''.join(sorted(word))
            if len(stringSub(word, stringSum([stringSub(key[8], stringSum([key[4], key[7]])), key[7]]))) == 1:
                key[0] = ''.join(sorted(word))
    key2 = {}
    for k in key:
        key2[key[k]] = str(k)
    value = ''
    for word in dataout[ind]:
        value += key2[''.join(sorted(word))]
    value = int(value)
    valuelist.append(value)
print(sum(valuelist))