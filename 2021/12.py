# Day 12

from collections import Counter

# Part 1
fn = '12.txt'
data = []
for line in open(fn):
    data.append(line.strip().split('-'))

pathdic = {}
for a, b in data:
    if a not in pathdic:
        pathdic[a] = []
    if b not in pathdic:
        pathdic[b] = []
    pathdic[a] += [b]
    if a != 'start':
        pathdic[b] += [a]
pathdic.pop('end')


def checkSmallCave(path):
    count = Counter(path)
    toPass = True
    for i in count:
        if i.islower():
            if count[i] > 1:
                toPass = False
    return(toPass)


def addPath(paths, pathdic):
    paths2 = []
    for i in paths:
        if i[-1] == 'end':
            paths2.append(i)
            continue
        for j in pathdic[i[-1]]:
            tpath = i+[j]
            if checkSmallCave(tpath):
                paths2.append(tpath)
    return(paths2)


paths = [['start']]
len1 = len(paths)
len2 = 0
while len1 != len2:
    len1 = len(paths)
    paths = addPath(paths, pathdic)
    len2 = len(paths)

print(len(paths))


# Part 2
def checkSmallCave2(path):
    count = Counter(path)
    toPass = True
    oneSmallCave = False
    for i in count:
        if i.islower():
            if count[i] > 2:
                toPass = False
            if count[i] > 1:
                if oneSmallCave:
                    toPass = False
                else:
                    oneSmallCave = True
    return(toPass)


def addPath2(paths, pathdic):
    paths2 = []
    for i in paths:
        if i[-1] == 'end':
            paths2.append(i)
            continue
        for j in pathdic[i[-1]]:
            tpath = i+[j]
            if checkSmallCave2(tpath):
                paths2.append(tpath)
    return(paths2)


paths = [['start']]
len1 = len(paths)
len2 = 0
while len1 != len2:
    len1 = len(paths)
    paths = addPath2(paths, pathdic)
    len2 = len(paths)

print(len(paths))