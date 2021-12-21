# Day 21

import numpy as np
from random import randint

# Starting positions
p1_start, p2_start = 7, 4
p1_start, p2_start = p1_start-1, p2_start-1
board = list(range(1, 11))
board_len = len(board)

# Part 1
ddice = 0
ddice_rolls = 0


def roll():
    global ddice
    global ddice_rolls
    ddice += 1
    ddice_rolls += 1
    if ddice > 100:
        ddice = 1
    return(ddice)


def roll3():
    return(roll()+roll()+roll())


def circle(pos):
    global board_len
    while pos >= board_len:
        pos -= 10
    return(pos)


def move(pos):
    pos += roll3()
    return(circle(pos))


p1score, p2score = 0, 0
p1, p2 = p1_start, p2_start
while True:
    p1 = move(p1)
    p1score += board[p1]
    if p1score >= 1000:
        break
    p2 = move(p2)
    p2score += board[p2]
    if p2score >= 1000:
        break
print('Part 1:', ddice_rolls*min([p1score, p2score]))


# Part 2
qdice = {}
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            val = i+k+j
            if val not in qdice:
                qdice[val] = 1
            else:
                qdice[val] += 1
qrolls = list(qdice.keys())
qcounts = list(qdice.values())


def quantmove(pos):
    global board
    poslist = [circle(pos+x) for x in qrolls]
    scores = [board[x] for x in poslist]
    return(poslist, scores)


def list2str(p1, p2, p1score, p2score):
    return(','.join([str(x) for x in [p1, p2, p1score, p2score]]))


def str2list(s):
    return([int(x) for x in s.split(',')])


games_p1turn = {list2str(p1_start, p2_start, 0, 0): 1}
games_p2turn = {}
winners = {'p1':0, 'p2':0}
while games_p1turn:
    games_p2turn = {}
    for key, val in games_p1turn.items():
        [p1, p2, p1score, p2score] = str2list(key)
        p1s, p1scores = quantmove(p1)
        for ind, p1 in enumerate(p1s):
            p1score_new = p1score+p1scores[ind]
            gnum = qcounts[ind]*val
            if p1score_new >= 21:
                winners['p1'] += gnum
                continue
            g = list2str(p1, p2, p1score+p1scores[ind], p2score)
            if not g in games_p2turn:
                games_p2turn[g] = gnum
            else:
                games_p2turn[g] += gnum
    games_p1turn = {}
    for key, val in games_p2turn.items():
        [p1, p2, p1score, p2score] = str2list(key)
        p2s, p2scores = quantmove(p2)
        for ind, p2 in enumerate(p2s):
            p2score_new = p2score+p2scores[ind]
            gnum = qcounts[ind]*val
            if p2score_new >= 21:
                winners['p2'] += gnum
                continue
            g = list2str(p1, p2, p1score, p2score+p2scores[ind])
            if not g in games_p1turn:
                games_p1turn[g] = gnum
            else:
                games_p1turn[g] += gnum     
print('Part 2:',max(winners.values()))