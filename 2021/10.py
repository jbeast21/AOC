# Day 10

from collections import Counter
from statistics import median

# Part 1
fn = '10.txt'
data = [x.strip() for x in open(fn)]


def negValueCheck(dic):
    check = False
    for val in dic.values:
        if val < 0:
            check = True
            break
    return(check)


def removeChunk(s):
    if '<>' in s:
        return(s.replace('<>', ''))
    elif '()' in s:
        return(s.replace('()', ''))
    elif '[]' in s:
        return(s.replace('[]', ''))
    elif '{}' in s:
        return(s.replace('{}', ''))
    else:
        return(s)


def removeAllChunks(s):
    shrinking = True
    size = len(s)
    while shrinking:
        s = removeChunk(s)
        if len(s) == size:
            shrinking = False
        size = len(s)
    return(s)


def findCloser(s):
    for i in range(len(s)):
        if s[i] == ')': return(')')
        if s[i] == ']': return(']')
        if s[i] == '}': return('}')
        if s[i] == '>': return('>')
    return('')


values = {'(':1, ')':-1, '[':1, ']':-1, '{':1, '}':-1, '<':1, '>':-1}
reverse = {'(':')', '[':']', '{':'}', '<':'>'}
points = {')':3, ']':57, '}':1197, '>':25137}

illegal = ''
counter = {')':0, ']':0, '}':0, '>':0}
for i in data:
    line = removeAllChunks(i)
    if not line: continue
    illegal += findCloser(line)    

sc = Counter(illegal)
score = 0
for i in points:
    score += points[i]*sc[i]
print(score)

# Part 2
def calcScore(s):
    score = 0
    points = {')':1, ']':2, '}':3, '>':4}
    for i in s:
        score = score*5+points[i]
    return(score)


def finishLine(s):
    line = ''
    reverse = {'(':')', '[':']', '{':'}', '<':'>'}
    for i in s:
        line += reverse[i]
    return(line[::-1])


points2 = {')':1, ']':2, '}':3, '>':4}
illegal = ''
counter = {')':0, ']':0, '}':0, '>':0}
scores = []
for i in data:
    line = removeAllChunks(i)
    if not line:
        continue
    if findCloser(line):
        continue
    scores.append(calcScore(finishLine(line)))
print(median(scores))